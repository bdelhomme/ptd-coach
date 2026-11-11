#!/usr/bin/env python3
"""Run the public synthetic development campaign on the three frozen contexts."""

import argparse
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import random
import re
import sys
import time

from compare_conversation_c2 import (
    ROOT, VARIANTS, Capture, collect, digest, settings, provider_from_settings,
    summarize, verify_c2_freeze,
)
from run_coach_eval_v07 import cases_from_file

SUITE = ROOT / "pedagogy/qa/COACH_TRANSVERSAL_DEV_CASES.json"
CALL_CEILING = 36
REVIEW_FIELDS = (
    "exactitude", "diagnostic", "pertinence_methode", "proportionnalite",
    "enseignement", "etayage", "correction_verification", "autonomie",
    "relation_commanditaire", "acceptabilite", "limites_securite",
    "prescription_observee", "travail_intellectuel_laisse", "sollicitations",
    "incident_critique", "citation_et_justification", "lecteur",
)


class TimedProvider(Capture):
    """Keep a duration even when the service records a sanitized API failure."""

    def complete(self, messages):
        started = time.monotonic()
        try:
            return super().complete(messages)
        finally:
            self.elapsed_ms = round((time.monotonic() - started) * 1000)


def verbatim(text):
    fence = "~" * max(4, 1 + max(map(len, re.findall(r"~+", text)), default=0))
    return f"{fence}text\n{text}\n{fence}\n"


def write_review(folder, rows, cases):
    variants = list(dict.fromkeys(row["variant"] for row in rows))
    random.SystemRandom().shuffle(variants)
    labels = dict(zip(variants, "ABC"))
    (folder / "CLE_VARIANTES.json").write_text(json.dumps(labels, indent=2) + "\n", encoding="utf-8")
    lines = [
        "# Lecture comparative par scénario\n",
        "Consulter la clé après la lecture. L'identité peut rester reconnaissable au style.\n",
    ]
    with (folder / "GRILLE_VIERGE.csv").open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=("case_id", "turn", "label") + REVIEW_FIELDS,
                                lineterminator="\n")
        writer.writeheader()
        for case in cases:
            if not any(row["case_id"] == case["id"] for row in rows):
                continue
            lines.append(f"## {case['id']} · {case['title']}\n")
            lines.append(f"Travail laissé à l'étudiant ou à l'équipe — {case['student_work']}\n")
            for index, turn in enumerate(case["turns"], 1):
                replies = [row for row in rows if row["case_id"] == case["id"] and row["turn"] == index]
                if not replies:
                    continue
                lines.extend([f"### Tour {index}\n", verbatim(turn["student"]),
                              "Attendus proposés · " + " / ".join(turn["look_for"]) + "\n",
                              "Points de vigilance · " + " / ".join(turn["red_flags"]) + "\n"])
                for row in sorted(replies, key=lambda item: labels[item["variant"]]):
                    label = labels[row["variant"]]
                    response = row["response"] if row["response"] is not None else f"[{row['status']}]"
                    lines.extend([f"**Variante {label}**\n", verbatim(response)])
                    if row["response"] is not None:
                        writer.writerow(dict(case_id=case["id"], turn=index, label=label))
    (folder / "LECTURE_COMPARATIVE.md").write_text("\n".join(lines), encoding="utf-8")


def run(provider_name, folder, allow_billable=False):
    if provider_name == "mistral" and not allow_billable:
        raise ValueError("Le passage Mistral demande --allow-billable.")
    suite = cases_from_file(SUITE)
    if suite.get("split") != "development":
        raise ValueError("Jeu de développement attendu.")
    selected = suite["first_comparison"] if provider_name == "mistral" else None
    cases = [case for case in suite["cases"] if selected is None or case["id"] in selected]
    if selected is not None and (len(selected) != 6 or [case["id"] for case in cases] != selected):
        raise ValueError("Échantillon Mistral invalide.")
    planned = len(VARIANTS) * sum(len(case["turns"]) for case in cases)
    if provider_name == "mistral" and planned != CALL_CEILING:
        raise ValueError("Le plan du passage réel doit comporter exactement 36 tentatives.")
    freeze_hash = verify_c2_freeze()
    suite_hash = digest(SUITE.read_bytes())
    provider = None
    config = settings(ROOT)
    if provider_name != "dry-run":
        if config["CHAT_MAX_TOKENS"] != 700:
            raise ValueError("CHAT_MAX_TOKENS=700 est requis pour la comparabilité.")
        config["CHAT_PROVIDER"] = provider_name
        provider = TimedProvider(provider_from_settings(config))
        if not provider.configured:
            raise ValueError("Clé Mistral locale absente.")
    folder.mkdir(mode=0o700, parents=True, exist_ok=False)
    rows = []
    with (folder / "responses.jsonl").open("x", encoding="utf-8") as stream:
        for row in collect(suite, provider, selected):
            row.update(c2_freeze_sha256=freeze_hash, suite_sha256=suite_hash)
            if row["status"] == "api_error" and provider:
                row["latency_ms"] = provider.elapsed_ms
            stream.write(json.dumps(row, ensure_ascii=False) + "\n")
            stream.flush()
            rows.append(row)
    report = {
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "provider": provider_name,
        "selected_cases": [case["id"] for case in cases],
        "planned_records": planned,
        "mistral_attempt_ceiling": CALL_CEILING if provider_name == "mistral" else 0,
        "mistral_attempts_recorded": len(rows) if provider_name == "mistral" else 0,
        "model_requested": provider.model if provider else None,
        "parameters": {"max_tokens": 700, "temperature": 0.2, "stream": False,
                       "tool_choice": "none", "timeout_seconds": config["CHAT_TIMEOUT_SECONDS"]},
        "c2_freeze_sha256": freeze_hash, "suite_sha256": suite_hash,
        "summary": summarize(rows), "complete": len(rows) == planned and all(
            row["status"] != "api_error" for row in rows),
        "human_verdict": None,
    }
    (folder / "MESURES.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n",
                                        encoding="utf-8")
    write_review(folder, rows, cases)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--provider", choices=("dry-run", "mock", "mistral"), default="dry-run")
    parser.add_argument("--allow-billable", action="store_true")
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    try:
        report = run(args.provider, args.output_dir, args.allow_billable)
    except (ValueError, FileExistsError) as error:
        parser.error(str(error))
    print(json.dumps(report, ensure_ascii=False))
    return int(not report["complete"])


if __name__ == "__main__":
    sys.exit(main())
