"""A2 domain, scoped persistence and explicit human commands for a local demo."""

from datetime import datetime, timezone
from contextlib import contextmanager
import hashlib
import json
from pathlib import Path
import sqlite3
import uuid

from .contracts import validate_coach
from .identities import USERS
from .provider import MockProvider


ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "pedagogy/scenarios/A2-demo-cases-v0.1.json").read_text())
SCENARIO = json.loads((ROOT / "pedagogy/scenarios/A2-first-cycle.json").read_text())
COMPETENCIES = json.loads((ROOT / "pedagogy/competencies/candidate-v0.3.json").read_text())
CASE_BY_ID = {case["id"]: case for case in CASES["cases"]}
GOAL = "Anticiper les dépendances dans un projet"
# Field names are also the allowlist: clients never supply owner, role or next state.
ACTIONS = {
    "learn": ("OBJECTIVE_SELECTED", "LEARNING", (), "explain"),
    "practice": ("LEARNING", "PRACTICING", (), "practice"),
    "answer": ("PRACTICING", "PRACTICING", ("answer",), "practice"),
    "plan": ("PRACTICING", "EXPERIMENT_PLANNED", ("action", "when", "observation"), "prepare_action"),
    "start_experience": ("EXPERIMENT_PLANNED", "AWAITING_EXPERIENCE", (), None),
    "report": ("AWAITING_EXPERIENCE", "REFLECTING", ("facts", "interpretation", "lesson", "experience_reported"), "debrief"),
    "review": ("REFLECTING", "REVIEWED", ("private_summary",), "weekly_review"),
    "close": ("REVIEWED", "CLOSED", (), None),
}


class DomainError(Exception):
    def __init__(self, status, code, message):
        super().__init__(message)
        self.status, self.code, self.message = status, code, message


def require(condition, status=400, code="invalid_request", message="Requête invalide."):
    if not condition:
        raise DomainError(status, code, message)


def exact_fields(payload, names):
    require(type(payload) is dict and set(payload) == set(names),
            message="Les champs de la requête ne correspondent pas à cette action.")


def text(value, minimum=10, maximum=4000):
    require(type(value) is str and minimum <= len(value.strip()) <= maximum,
            message="Renseignez un texte de {} à {} caractères.".format(minimum, maximum))
    return value.strip()


def now():
    return datetime.now(timezone.utc).isoformat()


class Service:
    def __init__(self, database, provider=None):
        self.database = str(database)
        self.provider = provider if provider is not None else MockProvider()
        path = Path(database)
        path.parent.mkdir(parents=True, exist_ok=True)
        with self.connect() as db:
            version = db.execute("PRAGMA user_version").fetchone()[0]
            if version == 0:
                db.executescript((Path(__file__).parent / "schema.sql").read_text())
            elif version != 1:
                raise RuntimeError("Unsupported local database version")
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
                "forbidden", "Cet espace est réservé au propriétaire étudiant.")

    def owned(self, db, actor, cycle_id):
        self.student(actor)
        row = db.execute("SELECT * FROM cycles WHERE id = ? AND owner_id = ?",
                         (cycle_id, actor)).fetchone()
        require(row is not None, 404, "not_found", "Parcours introuvable.")
        return row

    def snapshot(self, db, actor, cycle_id):
        row = self.owned(db, actor, cycle_id)
        result = dict(row)
        result["data"] = json.loads(result["data"])
        result["messages"] = [dict(item) for item in db.execute(
            "SELECT m.role, m.content, m.created_at FROM messages m "
            "JOIN cycles c ON c.id = m.cycle_id WHERE c.id = ? AND c.owner_id = ? ORDER BY m.id",
            (cycle_id, actor))]
        return result

    def cycle(self, actor, cycle_id):
        with self.connect() as db:
            return self.snapshot(db, actor, cycle_id)

    def cycles(self, actor):
        self.student(actor)
        with self.connect() as db:
            return [self.snapshot(db, actor, row["id"]) for row in db.execute(
                "SELECT id FROM cycles WHERE owner_id = ? ORDER BY created_at DESC", (actor,))]

    def run_command(self, actor, key, operation, payload, apply):
        require(actor in USERS, 401, "unauthorized", "Session requise.")
        try:
            uuid.UUID(key)
        except (ValueError, TypeError, AttributeError):
            raise DomainError(400, "invalid_key", "Une clé d'idempotence UUID est requise.")
        fingerprint = hashlib.sha256(json.dumps(
            [operation, payload], sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            prior = db.execute("SELECT * FROM commands WHERE actor_id = ? AND command_key = ?",
                               (actor, key)).fetchone()
            if prior:
                require(prior["fingerprint"] == fingerprint, 409, "idempotency_conflict",
                        "Cette clé a déjà été utilisée pour une autre commande.")
                return json.loads(prior["response"])
            result = apply(db)
            db.execute("INSERT INTO commands VALUES (?, ?, ?, ?)",
                       (actor, key, fingerprint, json.dumps(result, ensure_ascii=False)))
            return result

    def event(self, db, actor, kind, object_id):
        db.execute("INSERT INTO events(actor_id, kind, object_id, created_at) VALUES (?, ?, ?, ?)",
                   (actor, kind, object_id, now()))

    def create(self, actor, key, payload):
        self.student(actor)
        exact_fields(payload, {"case_id"})
        require(type(payload["case_id"]) is str and payload["case_id"] in CASE_BY_ID)

        def apply(db):
            cycle_id = str(uuid.uuid4())
            db.execute("INSERT INTO cycles VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (cycle_id, actor, USERS[actor]["team"], "OBJECTIVE_SELECTED", 1,
                        payload["case_id"], SCENARIO["version"], COMPETENCIES["version"],
                        json.dumps({"goal": GOAL, "case_version": CASES["version"]}), now()))
            self.event(db, actor, "cycle_created", cycle_id)
            return self.snapshot(db, actor, cycle_id)
        return self.run_command(actor, key, "create", payload, apply)

    def check_version(self, row, version):
        require(type(version) is int and row["version"] == version, 409, "version_conflict",
                "Ce parcours a changé. Rechargez-le avant de réessayer.")

    def coach(self, row, data, activity, student_message):
        request = {
            "mode": "individual", "activity": activity, "pedagogical_state": row["state"],
            "competency_ids": ["A2"], "prompt_version": "a2-local-mock-v0.1",
            "authorized_context": [
                {"kind": "synthetic_case", "text": json.dumps(CASE_BY_ID[row["case_id"]], ensure_ascii=False)},
                {"kind": "owner_cycle", "text": json.dumps(data, ensure_ascii=False)},
            ],
            "student_message": student_message,
        }
        try:
            validate_coach(request, "request")
            raw = self.provider.complete(request)
            require(type(raw) is str and len(raw) <= 32000)
            response = json.loads(raw)
            validate_coach(response, "response")
            require(0 < len(response["message"].strip()) <= 12000)
            return response["message"]
        except Exception:
            # Provider exceptions must not disclose request text or mutate the transaction.
            raise DomainError(502, "provider_error",
                              "Le simulateur n'a pas répondu correctement. Votre action n'a pas été enregistrée ; vous pouvez réessayer.") from None

    def act(self, actor, cycle_id, key, payload):
        exact_fields(payload, {"action", "version", "fields"})
        action = payload["action"]
        require(type(action) is str and action in ACTIONS)
        source, target, fields, activity = ACTIONS[action]
        exact_fields(payload["fields"], fields)
        values = {}
        for name in fields:
            value = payload["fields"][name]
            if name == "experience_reported":
                require(value is True, message="Confirmez que vous rapportez une expérience vécue ou simulée.")
                values[name] = True
            else:
                values[name] = text(value)

        def apply(db):
            row = self.owned(db, actor, cycle_id)
            self.check_version(row, payload["version"])
            require(row["state"] == source, 409, "invalid_transition",
                    "Cette action n'est pas disponible à cette étape.")
            data = json.loads(row["data"])
            if action == "plan":
                require(bool(data.get("answer")), 409, "practice_required",
                        "Enregistrez d'abord une réponse à l'exercice.")
            data.update(values)
            message = self.coach(row, data, activity,
                                 values.get("answer", json.dumps(values, ensure_ascii=False) if values else "")) if activity else None
            # Only this explicit human command sets target; model suggestions are never applied.
            db.execute("UPDATE cycles SET state = ?, version = version + 1, data = ? "
                       "WHERE id = ? AND owner_id = ?",
                       (target, json.dumps(data, ensure_ascii=False), cycle_id, actor))
            if values:
                db.execute("INSERT INTO messages(cycle_id, role, content, created_at) VALUES (?, ?, ?, ?)",
                           (cycle_id, "student", json.dumps(values, ensure_ascii=False), now()))
            if message:
                db.execute("INSERT INTO messages(cycle_id, role, content, created_at) VALUES (?, ?, ?, ?)",
                           (cycle_id, "coach", message, now()))
            self.event(db, actor, "action_" + action, cycle_id)
            return self.snapshot(db, actor, cycle_id)
        return self.run_command(actor, key, "action:" + cycle_id, payload, apply)

    def share(self, actor, cycle_id, key, payload):
        exact_fields(payload, {"version", "text", "recipient_id", "confirmed"})
        selected_text = text(payload["text"], maximum=2000)
        require(payload["confirmed"] is True, message="Confirmez explicitement le partage de ce texte.")
        recipient = payload["recipient_id"]
        require(type(recipient) is str and recipient in USERS)

        def apply(db):
            row = self.owned(db, actor, cycle_id)
            self.check_version(row, payload["version"])
            require(row["state"] in {"REVIEWED", "CLOSED"}, 409, "review_required",
                    "Sauvegardez votre bilan avant de sélectionner une preuve.")
            require(USERS[recipient]["role"] == "tutor" and USERS[recipient]["team"] == row["team_id"],
                    403, "forbidden", "Le destinataire doit être le tuteur de cette équipe fictive.")
            share_id = str(uuid.uuid4())
            db.execute("INSERT INTO shares(id, cycle_id, owner_id, recipient_id, text, created_at) "
                       "VALUES (?, ?, ?, ?, ?, ?)", (share_id, cycle_id, actor, recipient, selected_text, now()))
            db.execute("UPDATE cycles SET version = version + 1 WHERE id = ? AND owner_id = ?", (cycle_id, actor))
            self.event(db, actor, "evidence_shared", share_id)
            return {"id": share_id, "version": 1}
        return self.run_command(actor, key, "share:" + cycle_id, payload, apply)

    def shares(self, actor):
        require(actor in USERS and USERS[actor]["role"] in {"student", "tutor"},
                403, "forbidden", "Aucune preuve accessible pour ce rôle.")
        owner = USERS[actor]["role"] == "student"
        column = "owner_id" if owner else "recipient_id"
        # column is chosen from the two literals above, never from request data.
        with self.connect() as db:
            rows = db.execute("SELECT id, owner_id, recipient_id, text, version, created_at "
                              "FROM shares WHERE " + column + " = ? AND revoked = 0 ORDER BY created_at DESC", (actor,))
            return [dict(row, owner_label=USERS[row["owner_id"]]["label"]) for row in rows]

    def revoke(self, actor, share_id, key, payload):
        self.student(actor)
        exact_fields(payload, {"version"})

        def apply(db):
            row = db.execute("SELECT * FROM shares WHERE id = ? AND owner_id = ?", (share_id, actor)).fetchone()
            require(row is not None, 404, "not_found", "Preuve introuvable.")
            self.check_version(row, payload["version"])
            db.execute("UPDATE shares SET revoked = 1, version = version + 1 WHERE id = ? AND owner_id = ?", (share_id, actor))
            self.event(db, actor, "evidence_revoked", share_id)
            return {"id": share_id, "revoked": True, "version": row["version"] + 1}
        return self.run_command(actor, key, "revoke:" + share_id, payload, apply)

    def export(self, actor, cycle_id):
        return {"format": "ptd-coach-private-cycle", "version": "0.1",
                "exported_at": now(), "cycle": self.cycle(actor, cycle_id)}
