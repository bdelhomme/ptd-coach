"""Team-only, explicitly saved workbench drafts, separate from coach memory."""

from datetime import date
import json

from .gantt import gantt_warnings, validate_gantt
from .service import exact_fields, require, text


SPEC_FIELDS = (
    "context", "need", "scope", "exclusions", "stakeholders", "deliverables",
    "requirements", "constraints", "verification", "acceptance", "assumptions",
    "questions", "sponsor_evidence",
)

DEFAULTS = {
    "gantt": {"tasks": [], "baseline": None},
    "specification": {"sections": dict.fromkeys(SPEC_FIELDS, ""), "reference": None},
    "raci": {"roles": [], "rows": []},
    "risks": {"rows": []},
    "decisions": {"rows": []},
    "decision-matrix": {"criteria": [], "options": []},
    "calendar": {"start": "", "end": "", "sessions": ""},
}

REGISTER_FIELDS = {
    "risks": ("type", "statement", "impact", "signal", "response", "owner"),
    "decisions": ("type", "statement", "rationale", "authority", "source", "next"),
}


def plain(value, limit=400, required=False):
    require(type(value) is str, message="Saisissez du texte.")
    return text(value, int(required), limit)


def bounded(value, limit):
    require(type(value) is list and len(value) <= limit, message=f"Liste limitée à {limit} entrées.")
    return value


def sections(value):
    exact_fields(value, SPEC_FIELDS)
    return {key: plain(value[key], 900) for key in SPEC_FIELDS}


def validate_spec(value):
    exact_fields(value, ("sections", "reference"))
    current = sections(value["sections"])
    reference = value["reference"]
    if reference is not None:
        exact_fields(reference, ("sections", "source"))
        reference = {"sections": sections(reference["sections"]), "source": plain(reference["source"], 300, True)}
        require(any(reference["sections"].values()), message="La référence doit contenir du texte.")
    return {"sections": current, "reference": reference}


def validate_raci(value):
    exact_fields(value, ("roles", "rows"))
    roles = [plain(role, 70, True) for role in bounded(value["roles"], 10)]
    require(len({role.casefold() for role in roles}) == len(roles), message="Deux rôles portent le même nom.")
    rows = []
    for row in bounded(value["rows"], 30):
        exact_fields(row, ("activity", "assignments"))
        assignments = bounded(row["assignments"], len(roles))
        require(len(assignments) == len(roles) and all(a in ("", "R", "A", "RA", "C", "I") for a in assignments),
                message="Les attributions doivent correspondre aux rôles et aux codes RACI.")
        rows.append({"activity": plain(row["activity"], 120, True), "assignments": assignments})
    return {"roles": roles, "rows": rows}


def validate_register(kind, value):
    exact_fields(value, ("rows",))
    fields = REGISTER_FIELDS[kind]
    rows = []
    for row in bounded(value["rows"], 20):
        exact_fields(row, fields)
        cleaned = {field: plain(row[field], 180, field in ("type", "statement")) for field in fields}
        choices = ("Risque", "Problème") if kind == "risks" else ("Envisagée", "Prise")
        require(cleaned["type"] in choices, message="Statut du registre inconnu.")
        if kind == "decisions" and cleaned["type"] == "Prise":
            require(cleaned["source"] and cleaned["authority"], message="Indiquez qui a décidé et la source de l’accord.")
        rows.append(cleaned)
    return {"rows": rows}


def validate_matrix(value):
    exact_fields(value, ("criteria", "options"))
    criteria = []
    for criterion in bounded(value["criteria"], 8):
        exact_fields(criterion, ("name", "weight"))
        weight = criterion["weight"]
        require(type(weight) is int and 0 <= weight <= 100, message="Chaque poids est un entier de 0 à 100.")
        criteria.append({"name": plain(criterion["name"], 70, True), "weight": weight})
    options = []
    for option in bounded(value["options"], 10):
        exact_fields(option, ("name", "scores"))
        scores = bounded(option["scores"], len(criteria))
        require(len(scores) == len(criteria), message="Une case est requise par critère.")
        cleaned = []
        for cell in scores:
            exact_fields(cell, ("score", "reason"))
            score = cell["score"]
            require(score is None or (type(score) is int and 0 <= score <= 5), message="La note est inconnue ou un entier de 0 à 5.")
            cleaned.append({"score": score, "reason": plain(cell["reason"], 120, score is not None)})
        options.append({"name": plain(option["name"], 70, True), "scores": cleaned})
    return {"criteria": criteria, "options": options}


def validate_calendar(value):
    exact_fields(value, ("start", "end", "sessions"))
    start = plain(value["start"], 10)
    end = plain(value["end"], 10)
    if start or end:
        try:
            beginning, ending = date.fromisoformat(start), date.fromisoformat(end)
            require(beginning.isoformat() == start and ending.isoformat() == end,
                    message="Utilisez le format AAAA-MM-JJ.")
            require(beginning <= ending, message="La fin précède le début.")
        except ValueError:
            require(False, message="Indiquez les deux dates de la mission au format AAAA-MM-JJ.")
    return {"start": start, "end": end, "sessions": plain(value["sessions"], 500)}


VALIDATORS = {
    "gantt": validate_gantt, "specification": validate_spec, "raci": validate_raci,
    "risks": lambda value: validate_register("risks", value),
    "decisions": lambda value: validate_register("decisions", value),
    "decision-matrix": validate_matrix, "calendar": validate_calendar,
}


class Workbench:
    def __init__(self, project, demos):
        self.project = project
        self.demos = demos
        with project.connect() as db:
            db.execute("""
                CREATE TABLE IF NOT EXISTS workbench_drafts (
                    team_id TEXT NOT NULL REFERENCES semester_projects(team_id),
                    kind TEXT NOT NULL,
                    version INTEGER NOT NULL,
                    body TEXT NOT NULL,
                    PRIMARY KEY (team_id, kind)
                )
            """)

    def example(self, actor):
        team = self.project.identity(actor, write=True)["team"]
        return self.demos[team]

    def result(self, kind, data, version):
        result = {"data": data, "version": version}
        if kind == "gantt":
            result["warnings"] = gantt_warnings(data)
        return result

    def read(self, actor, kind):
        team = self.project.identity(actor, write=True)["team"]
        require(kind in DEFAULTS, 404, "not_found", "Outil inconnu.")
        with self.project.connect() as db:
            row = db.execute("SELECT version, body FROM workbench_drafts WHERE team_id=? AND kind=?",
                             (team, kind)).fetchone()
        return self.result(kind, json.loads(row["body"]), row["version"]) if row else self.result(kind, DEFAULTS[kind], 0)

    def save(self, actor, kind, payload):
        team = self.project.identity(actor, write=True)["team"]
        require(kind in VALIDATORS, 404, "not_found", "Outil inconnu.")
        exact_fields(payload, ("data", "version"))
        version = payload["version"]
        require(type(version) is int and version >= 0, message="La version est invalide.")
        data = VALIDATORS[kind](payload["data"])
        encoded = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
        with self.project.connect() as db:
            db.execute("BEGIN IMMEDIATE")
            row = db.execute("SELECT version, body FROM workbench_drafts WHERE team_id=? AND kind=?",
                             (team, kind)).fetchone()
            actual = row["version"] if row else 0
            # A replay of an already saved snapshot is harmless.
            if row and actual == version + 1 and row["body"] == encoded:
                return self.result(kind, data, actual)
            require(actual == version, 409, "stale_version", "Ce brouillon a changé. Rechargez l’outil avant de réessayer.")
            if kind == "specification" and row:
                reference = json.loads(row["body"])["reference"]
                require(reference is None or data["reference"] == reference, 409, "reference_immutable",
                        "La référence initiale est conservée. Documentez l’évolution dans le registre des décisions.")
            db.execute("INSERT INTO workbench_drafts VALUES (?, ?, ?, ?) ON CONFLICT(team_id, kind) "
                       "DO UPDATE SET version=excluded.version, body=excluded.body",
                       (team, kind, actual + 1, encoded))
        return self.result(kind, data, actual + 1)
