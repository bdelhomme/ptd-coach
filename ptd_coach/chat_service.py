"""Scoped conversations; model text has no permission to change business data."""

from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import sqlite3
import threading
import uuid

from .chat_context import ChatContext, PROMPT_VERSION
from .identities import USERS
from .service import DomainError, exact_fields, now, require, text


class ChatService:
    format_version = "conversation.v1"

    def __init__(self, database, provider, max_calls=100, context=None):
        self.database, self.provider, self.max_calls = str(database), provider, max_calls
        self.context = context or ChatContext()
        self.slots = threading.BoundedSemaphore(3)
        path = Path(database)
        path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
        with self.connect() as db:
            version = db.execute("PRAGMA user_version").fetchone()[0]
            if version == 0:
                db.executescript((Path(__file__).parent / "chat_schema.sql").read_text())
            elif version != 1:
                raise ValueError("Unsupported conversation database")
        path.chmod(0o600)

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.database, timeout=10)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys = ON")
        try:
            with db:
                yield db
        finally:
            db.close()

    def student(self, actor):
        require(actor in USERS and USERS[actor]["role"] == "student", 403,
                "forbidden", "Les conversations de démonstration sont réservées aux comptes étudiants fictifs.")

    def accessible(self, db, actor, cid):
        self.student(actor)
        row = db.execute("SELECT * FROM conversations WHERE id = ? AND "
                         "((scope = 'individual' AND owner_id = ?) OR (scope = 'collective' AND team_id = ?))",
                         (cid, actor, USERS[actor]["team"])).fetchone()
        require(row is not None, 404, "not_found", "Conversation introuvable.")
        return row

    @staticmethod
    def key(key):
        try:
            uuid.UUID(key)
        except (ValueError, TypeError, AttributeError):
            raise DomainError(400, "invalid_key", "Une clé d'idempotence UUID est requise.") from None

    def public_config(self):
        return {"provider": self.provider.name, "model": self.provider.model,
                "configured": self.provider.configured, "max_output_tokens": self.provider.max_tokens,
                "max_calls": self.max_calls, "max_turns": 24, "prompt_version": PROMPT_VERSION,
                "context_sha256": self.context.digest, "synthetic_only": True}

    def listing(self, actor):
        self.student(actor)
        with self.connect() as db:
            return [dict(row) for row in db.execute(
                "SELECT id, scope, version, pending, created_at FROM conversations WHERE "
                "(scope = 'individual' AND owner_id = ?) OR (scope = 'collective' AND team_id = ?) "
                "ORDER BY created_at DESC", (actor, USERS[actor]["team"]))]

    def snapshot(self, db, actor, cid):
        row = self.accessible(db, actor, cid)
        messages = [dict(m) for m in db.execute(
            "SELECT role, content, author_id, created_at FROM chat_messages WHERE conversation_id = ? ORDER BY id", (cid,))]
        requests = [dict(status=r["status"], **json.loads(r["metadata"])) for r in db.execute(
            "SELECT status, metadata FROM chat_requests WHERE conversation_id = ? ORDER BY created_at", (cid,))]
        sums = {k: sum(r["usage"].get(k) or 0 for r in requests)
                for k in ("prompt_tokens", "completion_tokens", "total_tokens")}
        return {"format": self.format_version, "id": cid, "scope": row["scope"],
                "version": row["version"], "pending": bool(row["pending"]),
                "messages": messages, "invocations": requests,
                "usage": {"known_tokens": sums, "unmeasured_calls": sum(
                    r["usage"].get("total_tokens") is None for r in requests)},
                "proposed_updates": []}

    def conversation(self, actor, cid):
        with self.connect() as db:
            return self.snapshot(db, actor, cid)

    def create(self, actor, key, payload):
        self.student(actor)
        self.key(key)
        exact_fields(payload, {"scope", "synthetic_confirmed"})
        require(payload["scope"] in ("individual", "collective") and payload["synthetic_confirmed"] is True,
                message="Confirmez l'usage de données fictives et choisissez un espace.")
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            prior = db.execute("SELECT id, scope FROM conversations WHERE owner_id = ? AND creation_key = ?", (actor, key)).fetchone()
            if prior:
                require(prior["scope"] == payload["scope"], 409, "idempotency_conflict", "Clé déjà utilisée pour un autre espace.")
                return self.snapshot(db, actor, prior["id"])
            cid = str(uuid.uuid4())
            db.execute("INSERT INTO conversations (id,scope,owner_id,team_id,creation_key,created_at) VALUES (?,?,?,?,?,?)",
                       (cid, payload["scope"], actor, USERS[actor]["team"], key, now()))
            return self.snapshot(db, actor, cid)

    def _reserve(self, actor, cid, key, payload):
        self.student(actor)
        self.key(key)
        exact_fields(payload, {"message", "version"})
        message = text(payload["message"], minimum=1)
        require(type(payload["version"]) is int and payload["version"] > 0)
        fingerprint = hashlib.sha256(json.dumps([cid, payload], sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = self.accessible(db, actor, cid)
            prior = db.execute("SELECT * FROM chat_requests WHERE actor_id = ? AND command_key = ?", (actor, key)).fetchone()
            if prior:
                require(prior["fingerprint"] == fingerprint, 409, "idempotency_conflict", "Clé déjà utilisée pour un autre message.")
                if prior["status"] == "failed":
                    error = json.loads(prior["error"])
                    raise DomainError(**error)
                require(prior["status"] != "pending", 409, "call_pending",
                        "Cet appel est en cours ou son résultat est incertain. Rechargez ; aucun second appel automatique.")
                return None, self.snapshot(db, actor, cid)
            require(not row["pending"], 409, "call_pending", "Une réponse est déjà attendue dans cette conversation.")
            require(row["version"] == payload["version"], 409, "stale_version", "La conversation a changé. Rechargez avant de poursuivre.")
            require(self.provider.configured, 503, "missing_key", "Ajoutez MISTRAL_API_KEY dans .env puis redémarrez le serveur.")
            history = [dict(m) for m in db.execute("SELECT role, content FROM chat_messages WHERE conversation_id = ? ORDER BY id", (cid,))]
            require(len(history) < 48 and sum(len(m["content"]) for m in history) + len(message) <= 60000,
                    409, "conversation_limit", "Ouvrez une nouvelle conversation : limite de contexte atteinte, sans suppression de l'historique.")
            require(db.execute("SELECT COUNT(*) FROM chat_requests").fetchone()[0] < self.max_calls,
                    429, "call_limit", "Plafond local d'appels atteint. Ajustez CHAT_MAX_CALLS manuellement si nécessaire.")
            metadata = {"provider": self.provider.name, "model_requested": self.provider.model,
                        "model_returned": None, "prompt_version": PROMPT_VERSION,
                        "context_sha256": self.context.digest, "max_tokens": self.provider.max_tokens,
                        "temperature": 0.2, "usage": {}, "latency_ms": None, "finish_reason": None}
            db.execute("INSERT INTO chat_requests VALUES (?,?,?,?,?,?,?,?)",
                       (actor, key, cid, fingerprint, "pending", json.dumps(metadata), None, now()))
            db.execute("UPDATE conversations SET pending = 1 WHERE id = ?", (cid,))
            messages = [{"role": "system", "content": self.context.system(row["scope"])}] + history + [{"role": "user", "content": message}]
        return (messages, message, metadata), None

    def send(self, actor, cid, key, payload):
        require(self.slots.acquire(blocking=False), 429, "busy", "Trois réponses sont déjà en préparation. Réessayez plus tard.")
        try:
            reserved, replay = self._reserve(actor, cid, key, payload)
            if reserved is None:
                return replay
            messages, message, metadata = reserved
            try:
                result = self.provider.complete(messages)
                require(type(result.message) is str and 0 < len(result.message.strip()) <= 30000,
                        502, "invalid_response", "Réponse vide ou trop longue du fournisseur.")
            except Exception as error:
                if not isinstance(error, DomainError):
                    error = DomainError(502, "provider_error", "Erreur du fournisseur ; aucun nouvel appel automatique.")
                with self.connect() as db:
                    db.execute("UPDATE chat_requests SET status = 'failed', error = ? WHERE actor_id = ? AND command_key = ?",
                               (json.dumps({"status": error.status, "code": error.code, "message": error.message}), actor, key))
                    db.execute("UPDATE conversations SET pending = 0 WHERE id = ?", (cid,))
                raise error from None
            metadata.update(model_returned=result.model_returned, usage=result.usage,
                            latency_ms=result.latency_ms, finish_reason=result.finish_reason)
            with self.connect() as db:
                db.execute("BEGIN IMMEDIATE")
                self.accessible(db, actor, cid)
                db.executemany("INSERT INTO chat_messages (conversation_id,role,content,author_id,created_at) VALUES (?,?,?,?,?)",
                               [(cid, "user", message, actor, now()), (cid, "assistant", result.message, "coach", now())])
                db.execute("UPDATE chat_requests SET status = 'succeeded', metadata = ? WHERE actor_id = ? AND command_key = ?",
                           (json.dumps(metadata), actor, key))
                db.execute("UPDATE conversations SET pending = 0, version = version + 1 WHERE id = ?", (cid,))
                return self.snapshot(db, actor, cid)
        finally:
            self.slots.release()

    def export(self, actor, cid):
        return {"format": "ptd-coach-conversation-export.v1", "exported_at": now(),
                "conversation": self.conversation(actor, cid)}
