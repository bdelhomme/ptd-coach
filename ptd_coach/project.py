"""Semester project and explicit human confirmations for the local demo."""

from contextlib import contextmanager
import hashlib
import json
import os
from pathlib import Path
import sqlite3
import stat
from uuid import UUID, uuid4

from .identities import USERS
from .service import exact_fields, now, require, text


KINDS = (
    "fact", "hypothesis", "proposal", "requirement", "criterion",
    "question", "decision", "obstacle", "action", "review", "note",
)
SCOPES = ("individual", "collective")
SLOT = "Jeudi matin · créneau PTD prévu dans l’emploi du temps, obligatoire en théorie"
PROJECTS = {
    "team_demo_01": {
        "title": "Simplifier le prêt de matériel",
        "sponsor": "Atelier des Arts (fictif)",
        "brief": "Le commanditaire souhaite améliorer le prêt de matériel aux associations. "
                 "L’équipe doit comprendre les usages et vérifier ses propositions.",
        "weeks": (
            ("Comprendre la demande",
             "L’atelier souhaite un « système simple ». Le mot simple reste à préciser."),
            ("Clarifier le besoin",
             "Le commanditaire évoque les retours difficiles à retrouver. "
             "Quels cas concrets permettraient de vérifier le besoin ?"),
            ("Organiser le travail",
             "Deux groupes préparent des livrables liés. "
             "Il reste à décider quelles informations ils doivent s’échanger."),
            ("Examiner une évolution",
             "Le commanditaire évoque un export des prêts. La portée de la demande reste à confirmer."),
            ("Faire face à un imprévu",
             "Le matériel prévu est indisponible et l’essai prend du retard. "
             "L’équipe hésite entre simplifier l’essai et décaler la restitution. "
             "Deux membres disent avoir du mal à se remobiliser."),
            ("Préparer la restitution",
             "Le commanditaire souhaite entendre les résultats et les limites. "
             "L’équipe prépare les éléments qu’elle peut justifier."),
        ),
    },
    "team_demo_02": {
        "title": "Se repérer à la médiathèque",
        "sponsor": "Médiathèque des Tilleuls (fictive)",
        "brief": "L’équipe étudie les difficultés d’orientation dans une médiathèque fictive.",
        "weeks": (
            ("Comprendre la demande", "Le commanditaire souhaite rendre les espaces plus lisibles."),
            ("Clarifier le besoin", "L’équipe cherche des situations concrètes à observer."),
            ("Organiser le travail", "L’équipe discute de ses livrables et responsabilités."),
            ("Examiner une évolution", "Le commanditaire soulève une question à clarifier."),
            ("Faire face à un imprévu", "L’équipe doit adapter une expérimentation."),
            ("Préparer la restitution", "L’équipe fait le point sur les preuves disponibles."),
        ),
    },
}
PUBLIC_ITEM_FIELDS = (
    "id", "scope", "kind", "text", "source", "origin", "week", "confirmed_at",
    "confirmed_by", "version", "created_at", "updated_at",
)


class ProjectService:
    """Persist facts, drafts and confirmations without any model write path."""

    def __init__(self, database):
        path = Path(database)
        self.database = str(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        try:
            descriptor = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        except FileExistsError:
            if not stat.S_ISREG(path.lstat().st_mode):
                raise ValueError("A regular file is required for the project database")
            path.chmod(0o600)
        else:
            os.close(descriptor)
        with self.connect() as db:
            version = db.execute("PRAGMA user_version").fetchone()[0]
            if version in (0, 1):
                schema = Path(__file__).with_name("project_schema.sql").read_text(encoding="utf-8")
                db.executescript("BEGIN IMMEDIATE;\n" + schema + "\nCOMMIT;")
            elif version != 2:
                raise RuntimeError("Unsupported semester project database version")
            db.executemany("INSERT OR IGNORE INTO semester_projects(team_id) VALUES (?)",
                           ((team,) for team in PROJECTS))

    @contextmanager
    def connect(self):
        db = sqlite3.connect(self.database, timeout=10)
        db.row_factory = sqlite3.Row
        db.execute("PRAGMA foreign_keys = ON")
        db.execute("PRAGMA secure_delete = ON")
        try:
            with db:
                yield db
        finally:
            db.close()

    @staticmethod
    def identity(actor, write=False):
        user = USERS.get(actor)
        roles = ("student",) if write else ("student", "tutor")
        require(user is not None and user["role"] in roles and user["team"] in PROJECTS,
                403, "forbidden", "Accès à ce projet refusé.")
        return user

    @staticmethod
    def project(db, team, include_situation):
        row = db.execute("SELECT current_week, version FROM semester_projects WHERE team_id = ?", (team,)).fetchone()
        fixture = PROJECTS[team]
        project = {"id": team, "title": fixture["title"], "sponsor": fixture["sponsor"],
                   "brief": fixture["brief"], "slot": SLOT, "current_week": row["current_week"],
                   "version": row["version"], "max_week": len(fixture["weeks"])}
        if include_situation:
            project["week_title"], project["week_description"] = fixture["weeks"][row["current_week"] - 1]
        return project

    @staticmethod
    def item(row, student):
        result = {name: row[name] for name in PUBLIC_ITEM_FIELDS}
        result["confirmed"] = row["confirmed_at"] is not None
        result["shared"] = row["shared_to"] is not None
        if not student:
            result["confirmed_by"] = None
        return result

    def _snapshot(self, db, actor, user):
        student = user["role"] == "student"
        team = user["team"]
        if student:
            rows = db.execute(
                "SELECT * FROM project_items WHERE team_id = ? "
                "AND (scope = 'collective' OR (scope = 'individual' AND owner_id = ?)) "
                "ORDER BY week DESC, updated_at DESC, id",
                (team, actor),
            )
        else:
            rows = db.execute(
                "SELECT * FROM project_items WHERE team_id = ? AND scope = 'collective' "
                "AND confirmed_at IS NOT NULL AND shared_to = ? ORDER BY week DESC, updated_at DESC, id",
                (team, actor),
            )
        return {"project": self.project(db, team, include_situation=student),
                "items": [self.item(row, student) for row in rows]}

    def snapshot(self, actor):
        user = self.identity(actor)
        with self.connect() as db:
            db.execute("BEGIN")
            return self._snapshot(db, actor, user)

    @staticmethod
    def fields(payload):
        kind = payload["kind"]
        require(kind in KINDS, message="Choisissez un type de repère connu.")
        return kind, text(payload["text"], 1, 2000), text(payload["source"], 1, 300)

    @staticmethod
    def revision(payload, current):
        require(type(payload["version"]) is int and payload["version"] > 0,
                message="La version doit être un entier positif.")
        require(payload["version"] == current, 409, "stale_version",
                "Cet élément a changé. Actualisez le projet avant de réessayer.")

    def create(self, actor, payload, key=None):
        user = self.identity(actor, write=True)
        exact_fields(payload, ("scope", "kind", "text", "source", "origin"))
        scope = payload["scope"]
        origin = payload["origin"]
        require(scope in SCOPES and origin in ("human", "ai"), message="Espace ou origine invalide.")
        kind, content, source = self.fields(payload)
        if key is not None:
            try:
                key = str(UUID(key))
            except (ValueError, TypeError, AttributeError):
                require(False, message="Une clé de création UUID est requise.")
            encoded = json.dumps([key, scope, kind, content, source, origin], ensure_ascii=False).encode()
            fingerprint = hashlib.sha256(encoded).hexdigest()
        team = user["team"]
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            if key is not None:
                prior = db.execute(
                    "SELECT item_id, fingerprint FROM project_create_commands "
                    "WHERE actor_id = ? AND command_key = ?", (actor, key),
                ).fetchone()
                if prior is not None:
                    require(prior["item_id"] is not None and prior["fingerprint"] == fingerprint,
                            409, "idempotency_conflict", "Cette clé de création a déjà été utilisée.")
                    return self._snapshot(db, actor, user)
            week = db.execute("SELECT current_week FROM semester_projects WHERE team_id = ?", (team,)).fetchone()[0]
            item_id = str(uuid4())
            timestamp = now()
            db.execute(
                "INSERT INTO project_items (id, team_id, owner_id, scope, kind, text, source, origin, week, "
                "created_at, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (item_id, team, actor, scope, kind, content, source, origin, week, timestamp, timestamp),
            )
            if key is not None:
                db.execute("INSERT INTO project_create_commands VALUES (?, ?, ?, ?)",
                           (actor, key, item_id, fingerprint))
            return self._snapshot(db, actor, user)

    def update(self, actor, item_id, payload):
        exact_fields(payload, ("kind", "text", "source", "version"))
        return self._change(actor, item_id, payload, "update", fields=self.fields(payload))

    def delete(self, actor, item_id, payload):
        exact_fields(payload, ("version",))
        return self._change(actor, item_id, payload, "delete")

    def confirm(self, actor, item_id, payload):
        exact_fields(payload, ("version",))
        return self._change(actor, item_id, payload, "confirm")

    def share(self, actor, item_id, payload):
        exact_fields(payload, ("version",))
        return self._change(actor, item_id, payload, "share")

    def revoke(self, actor, item_id, payload):
        exact_fields(payload, ("version",))
        return self._change(actor, item_id, payload, "revoke")

    @staticmethod
    def audit_share(db, row, actor, recipient, action, timestamp):
        db.execute(
            "INSERT INTO project_share_audit (item_id, item_version, actor_id, recipient_id, action, occurred_at) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (row["id"], row["version"], actor, recipient, action, timestamp),
        )

    def _change(self, actor, item_id, payload, action, fields=None):
        user = self.identity(actor, write=True)
        team = user["team"]
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute(
                "SELECT * FROM project_items WHERE id = ? AND team_id = ? "
                "AND (scope = 'collective' OR (scope = 'individual' AND owner_id = ?))",
                (item_id, team, actor),
            ).fetchone()
            require(row is not None, 404, "not_found", "Repère introuvable.")
            self.revision(payload, row["version"])
            timestamp = now()
            if action == "delete":
                if row["shared_to"] is not None:
                    self.audit_share(db, row, actor, row["shared_to"], "revoke_on_delete", timestamp)
                # Prevent a late retry from recreating a deleted record and discard its content fingerprint.
                db.execute("UPDATE project_create_commands SET item_id = NULL, fingerprint = NULL WHERE item_id = ?",
                           (item_id,))
                db.execute("DELETE FROM project_items WHERE id = ?", (item_id,))
                return self._snapshot(db, actor, user)
            if action == "update":
                if row["shared_to"] is not None:
                    self.audit_share(db, row, actor, row["shared_to"], "revoke_on_edit", timestamp)
                assignment = "kind = ?, text = ?, source = ?, confirmed_at = NULL, confirmed_by = NULL, shared_to = NULL"
                values = fields
            elif action == "confirm":
                require(row["confirmed_at"] is None, 409, "already_confirmed", "Ce repère est déjà confirmé.")
                assignment, values = "confirmed_at = ?, confirmed_by = ?", (timestamp, actor)
            elif action == "share":
                require(row["scope"] == "collective" and row["confirmed_at"] is not None,
                        409, "not_shareable", "Seuls les repères collectifs confirmés sont partageables.")
                require(row["shared_to"] is None, 409, "already_shared", "Ce repère est déjà partagé.")
                tutors = [uid for uid, profile in USERS.items() if profile["role"] == "tutor" and profile["team"] == team]
                require(len(tutors) == 1, 409, "tutor_unavailable", "Aucun tuteur unique n’est associé à cette équipe.")
                self.audit_share(db, row, actor, tutors[0], "share", timestamp)
                assignment, values = "shared_to = ?", (tutors[0],)
            else:
                require(row["shared_to"] is not None, 409, "not_shared", "Ce repère n’est pas partagé.")
                self.audit_share(db, row, actor, row["shared_to"], "revoke", timestamp)
                assignment, values = "shared_to = NULL", ()
            # Assignments are selected above from fixed statements and never received from the client.
            db.execute(
                f"UPDATE project_items SET {assignment}, updated_at = ?, version = version + 1 WHERE id = ?",
                (*values, timestamp, item_id),
            )
            return self._snapshot(db, actor, user)

    def next_week(self, actor, payload):
        user = self.identity(actor, write=True)
        exact_fields(payload, ("version",))
        team = user["team"]
        with self.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            project = self.project(db, team, include_situation=False)
            self.revision(payload, project["version"])
            require(project["current_week"] < project["max_week"], 409, "end_of_demo",
                    "La dernière semaine de démonstration est déjà ouverte.")
            db.execute("UPDATE semester_projects SET current_week = current_week + 1, version = version + 1 "
                       "WHERE team_id = ?", (team,))
            return self._snapshot(db, actor, user)

    def context(self, actor, scope):
        """Select a bounded set of whole confirmed items in one conversation scope."""
        user = self.identity(actor, write=True)
        require(scope in SCOPES, message="Espace de conversation inconnu.")
        with self.connect() as db:
            db.execute("BEGIN")
            project = self.project(db, user["team"], include_situation=False)
            rows = db.execute(
                "SELECT kind, text, source, origin, week, confirmed_at FROM project_items "
                "WHERE team_id = ? AND scope = ? AND (? = 'collective' OR owner_id = ?) "
                "AND confirmed_at IS NOT NULL ORDER BY confirmed_at DESC, id LIMIT 5",
                (user["team"], scope, scope, actor),
            )
            return {"project": {key: project[key] for key in ("title", "sponsor", "brief", "slot", "current_week")},
                    "items": [dict(row) for row in rows]}
