"""Validate editable Gantt plans and identify finish-to-start conflicts."""

from datetime import date, timedelta
import re

from .service import exact_fields, require, text


MAX_TASKS = 100
MAX_DURATION = 3660
MIN_DATE = date(2000, 1, 1)
MAX_DATE = date(2100, 12, 31)
TASK_ID = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,63}")
ISO_DAY = re.compile(r"[0-9]{4}-[0-9]{2}-[0-9]{2}")


def _task_id(value):
    require(type(value) is str and TASK_ID.fullmatch(value), message="Identifiant de tâche invalide.")
    return value


def _task_start(value):
    message = "Choisissez une date valide entre 2000 et 2100."
    require(type(value) is str and ISO_DAY.fullmatch(value), message=message)
    try:
        start = date.fromisoformat(value)
    except ValueError:
        require(False, message=message)
    require(MIN_DATE <= start <= MAX_DATE, message=message)
    return start


def _validate_tasks(value):
    require(type(value) is list and len(value) <= MAX_TASKS,
            message=f"Le planning accepte jusqu’à {MAX_TASKS} tâches et jalons.")
    tasks = {}
    for entry in value:
        exact_fields(entry, ("id", "name", "start", "duration", "predecessors"))
        task_id = _task_id(entry["id"])
        require(task_id not in tasks, message="Deux tâches ont le même identifiant.")
        name = text(entry["name"], 1, 120)
        require(not re.search(r"[\ud800-\udfff]", name), message="Le nom de la tâche contient un caractère invalide.")
        start = _task_start(entry["start"])
        duration = entry["duration"]
        require(type(duration) is int and 0 <= duration <= MAX_DURATION,
                message=f"Renseignez une durée entière de 0 à {MAX_DURATION} jours.")
        require(start + timedelta(days=max(0, duration - 1)) <= MAX_DATE,
                message="Une tâche se termine au-delà du 31 décembre 2100.")
        raw_predecessors = entry["predecessors"]
        require(type(raw_predecessors) is list and len(raw_predecessors) < MAX_TASKS,
                message="La liste des prédécesseurs est invalide.")
        predecessors = [_task_id(item) for item in raw_predecessors]
        require(len(set(predecessors)) == len(predecessors),
                message="Un prédécesseur figure plusieurs fois pour la même tâche.")
        tasks[task_id] = {"id": task_id, "name": name, "start": start.isoformat(),
                          "duration": duration, "predecessors": predecessors}

    checked, visiting = set(), set()

    def visit(task_id):
        require(task_id in tasks, message="Une dépendance pointe vers une tâche inconnue.")
        require(task_id not in visiting, message="Les dépendances forment un cycle.")
        if task_id in checked:
            return
        visiting.add(task_id)
        for predecessor in tasks[task_id]["predecessors"]:
            visit(predecessor)
        visiting.remove(task_id)
        checked.add(task_id)

    for task_id in tasks:
        visit(task_id)
    return list(tasks.values())


def validate_gantt(value):
    exact_fields(value, ("tasks", "baseline"))
    tasks = _validate_tasks(value["tasks"])
    baseline = value["baseline"]
    if baseline is not None:
        exact_fields(baseline, ("tasks",))
        baseline = {"tasks": _validate_tasks(baseline["tasks"])}
    return {"tasks": tasks, "baseline": baseline}


def gantt_warnings(value):
    """Compute schedule conflicts from a validated plan without moving tasks."""
    tasks = value["tasks"]
    start_dates = {task["id"]: date.fromisoformat(task["start"]) for task in tasks}
    available_dates = {task["id"]: start_dates[task["id"]] + timedelta(days=task["duration"]) for task in tasks}
    return [
        {"task_id": task["id"], "predecessor_id": predecessor,
         "earliest_start": available_dates[predecessor].isoformat()}
        for task in tasks
        for predecessor in task["predecessors"]
        if start_dates[task["id"]] < available_dates[predecessor]
    ]
