#!/usr/bin/env python3
"""Replay two published fictitious PTD trajectories through the current coach."""

import argparse
import json
from pathlib import Path
import tempfile
from uuid import uuid4

from ptd_coach.chat_config import provider_from_settings, settings
from ptd_coach.demo_v2 import PROJECTS_V2
from ptd_coach.library_v2 import SemesterWorkshopContext, WorkshopChatService, WorkshopMockProvider
from ptd_coach.project import ProjectService
from ptd_coach.service import DomainError


ROOT = Path(__file__).resolve().parents[1]
SUITE = ROOT / "pedagogy/qa/PTD_SEMESTER_V2_DEV.json"
BASELINE = ROOT / "pedagogy/evaluations/ptd-v2-demo/semestre-v2.jsonl"
STEPS = (1, 4, 6, 7)


def replay(provider, directory, output, limit=8):
    suite = json.loads(SUITE.read_text(encoding="utf-8"))
    if suite["status"] != "development" or suite["data"] != "synthetic_only":
        raise ValueError("Le test attend les trajectoires fictives de développement.")
    project = ProjectService(directory / "project.sqlite3", PROJECTS_V2)
    context = SemesterWorkshopContext(project)
    reference = {}
    for line in BASELINE.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row["context"] == context.version:
            reference[row["trajectory"], row["turn"]] = row
    selected = [(track, idx, step, turn)
                for track in suite["trajectories"]
                for idx, (step, turn) in enumerate(zip(STEPS, track["turns"]), start=1)]
    if len(selected) != 8 or len(suite["trajectories"]) != 2 or any(
            len(track["turns"]) != len(STEPS) for track in suite["trajectories"]):
        raise ValueError("Le test attend exactement huit tours sur deux trajectoires.")
    for track, idx, step, turn in selected:
        row = reference[track["id"], idx]
        if row["message"] != turn["student"] or row["simulated_step"] != step:
            raise ValueError("Le scénario diffère du passage GLM de référence.")
    service = WorkshopChatService(directory / "chat.sqlite3", provider, max_calls=limit, context=context)
    conversations = {}
    for track, idx, step, turn in selected[:limit]:
        actor = track["actor"]
        state = project.snapshot(actor)
        while state["project"]["current_week"] < step:
            state = project.next_week(actor, {"version": state["project"]["version"]})
        if idx == 1:
            conversations[actor] = service.create(actor, uuid4().hex, {
                "scope": "collective", "synthetic_confirmed": True, "coach_version": context.coach_version,
            })
        thread = conversations[actor]
        row = {"trajectory": track["id"], "turn": idx, "simulated_step": step,
               "stage": turn["stage"], "message": turn["student"],
               "provider": provider.name, "model_requested": provider.model,
               "max_tokens": provider.max_tokens, "timeout_seconds": getattr(provider, "timeout", None),
               "look_for": turn["look_for"], "red_flags": turn["red_flags"],
               "baseline": reference[track["id"], idx]}
        try:
            thread = service.send(actor, thread["id"], uuid4().hex, {
                "message": turn["student"], "version": thread["version"],
            })
        except DomainError as error:
            row.update(status="failed", error=error.code)
            print(json.dumps(row, ensure_ascii=False), file=output, flush=True)
            raise
        conversations[actor] = thread
        invocation = thread["invocations"][-1]
        row.update(status="succeeded", answer=thread["messages"][-1]["content"], invocation=invocation,
                   same_system_as_glm=invocation["system_sha256"] == row["baseline"]["invocation"]["system_sha256"])
        print(json.dumps(row, ensure_ascii=False), file=output, flush=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True, help="Nouveau fichier JSONL.")
    parser.add_argument("--live", action="store_true", help="Autorise jusqu’à huit appels réels à Albert API.")
    parser.add_argument("--turns", type=int, choices=range(1, 9), default=8,
                        help="Nombre de tours à rejouer, dans l’ordre du corpus.")
    args = parser.parse_args()
    if args.live:
        config = settings(ROOT, v2=True, provider_override="albert")
        provider = provider_from_settings(config)
        if not provider.configured:
            parser.error("ALBERT_API_KEY absente de l’environnement et du fichier .env local.")
    else:
        provider = WorkshopMockProvider()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    try:
        with tempfile.TemporaryDirectory() as tmp, args.out.open("x", encoding="utf-8") as output:
            replay(provider, Path(tmp), output, args.turns)
    except (DomainError, FileExistsError) as error:
        parser.exit(1, str(error) + "\n")
    print(f"Résultats écrits dans {args.out}")


if __name__ == "__main__":
    main()
