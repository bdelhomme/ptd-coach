#!/usr/bin/env python3
"""Créer une grille de jugement humain puis résumer des évaluations remplies.

ZÉRO jugement pédagogique automatique. L'outil calcule seulement des statistiques
sur les appréciations saisies par des lecteurs humains.
"""
import argparse
import csv
import json
from pathlib import Path

DIMS = ["relevance", "correctness", "student_agency", "epistemic_distinctions", "proportionality"]
FIELDS = ["reviewer", "case_id", "turn", "scope", "student", "response"] + DIMS + ["critical_failure", "notes"]


def records(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]


def make_sheet(input_path, output_path, reviewer):
    data = records(input_path)
    if not data or any(x["status"] != "model_called" for x in data):
        raise ValueError("Feuille de jugement réservée aux réponses réellement générées")
    with open(output_path, "w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=FIELDS)
        writer.writeheader()
        for x in data:
            writer.writerow({"reviewer": reviewer, "case_id": x["case_id"], "turn": x["turn"],
                             "scope": x["scope"], "student": x["student"], "response": x["response"],
                             **{d: "" for d in DIMS}, "critical_failure": "", "notes": ""})
    return len(data)


def summary(csv_path):
    with open(csv_path, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        raise ValueError("Feuille vide")
    incomplete = []
    adequate = 0
    critical = 0
    for x in rows:
        values = [x.get(k, "").strip() for k in DIMS]
        critical_val = x.get("critical_failure", "").strip().lower()
        crit = critical_val == "oui"
        critical += int(crit)
        if any(v not in ("0", "1", "2") for v in values) or critical_val not in ("oui", "non"):
            incomplete.append((x["case_id"], x["turn"]))
            continue
        adequate += int(not crit and all(int(v) >= 1 for v in values) and sum(map(int, values)) >= 8)
    completed = len(rows) - len(incomplete)
    out = {"total": len(rows), "completed": completed, "incomplete": incomplete,
           "adequate_among_completed": adequate,
           "adequate_rate_if_complete": round(adequate / len(rows), 3) if not incomplete else None,
           "critical_failures_identified": critical,
           "decision": "REVIEW_INCOMPLETE" if incomplete else (
               "MEETS_PROPOSED_SCREENING_GATE" if adequate / len(rows) >= .9 and not critical else "NEEDS_REVISION")}
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)
    sheet = sub.add_parser("sheet")
    sheet.add_argument("--responses", required=True)
    sheet.add_argument("--out", required=True)
    sheet.add_argument("--reviewer", default="reviewer-1")
    report = sub.add_parser("summary")
    report.add_argument("--sheet", required=True)
    args = p.parse_args()
    if args.command == "sheet":
        print(json.dumps({"rows": make_sheet(args.responses, args.out, args.reviewer)}))
    else:
        print(json.dumps(summary(args.sheet), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
