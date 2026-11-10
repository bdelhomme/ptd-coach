#!/usr/bin/env python3
"""Paired fictional V0.7/V0.8 collection. No automatic pedagogical verdict."""

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import random
import statistics
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ptd_coach.chat_config import settings, provider_from_settings
from ptd_coach.chat_context import ChatContext
from ptd_coach.chat_context_v08 import ChatContextV08
from run_coach_eval_v07 import cases_from_file
from run_conversation_eval import evaluate

FREEZE = ROOT / "pedagogy/qa/V08_CONTEXT_FREEZE.json"
DIMENSIONS = ("exactitude", "utilite", "adequation", "intervention", "feedback_correctif",
              "verification", "dosage", "sources_limites", "autonomie", "confidentialite",
              "veto", "satisfaction_probable", "effort_demande", "alternative", "commentaire", "lecteur")


def verify_freeze():
    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    for name, digest in freeze["files"].items():
        if hashlib.sha256((ROOT / name).read_bytes()).hexdigest() != digest:
            raise ValueError("Contexte modifié depuis le gel : " + name)
    return hashlib.sha256(FREEZE.read_bytes()).hexdigest()


def collect(suite, provider=None, selected=None):
    """Interleave complete conversations; histories remain isolated per variant/case."""
    contexts = {"v07": ChatContext(), "v08": ChatContextV08()}
    cases = [case for case in suite["cases"] if not selected or case["id"] in selected]
    for index, case in enumerate(cases):
        order = ("v07", "v08") if index % 2 == 0 else ("v08", "v07")
        for version in order:
            one_case = dict(suite, cases=[case])
            for record in evaluate(one_case, contexts[version], provider):
                record["variant"] = version
                yield record
                if record["status"] == "api_error":
                    return  # Stop the entire bounded run, never silently retry.


def summary(records):
    result = {}
    for variant in ("v07", "v08"):
        rows = [r for r in records if r["variant"] == variant]
        latencies = [r["latency_ms"] for r in rows if r.get("latency_ms") is not None]
        result[variant] = {
            "records": len(rows), "api_errors": sum(r["status"] == "api_error" for r in rows),
            "usage": {k: sum(r.get("usage", {}).get(k) or 0 for r in rows)
                      for k in ("prompt_tokens", "completion_tokens", "total_tokens")},
            "unmeasured_records": sum(r.get("usage", {}).get("total_tokens") is None for r in rows),
            "median_latency_ms": statistics.median(latencies) if latencies else None,
            "max_latency_ms": max(latencies) if latencies else None,
            "returned_models": sorted({r["model_returned"] for r in rows if r.get("model_returned")}),
            "truncated_responses": sum(r.get("finish_reason") == "length" for r in rows),
            "response_characters": sum(len(r.get("response") or "") for r in rows),
            "question_marks": sum((r.get("response") or "").count("?") for r in rows),
        }
    return result


def write_review(folder, records, suite):
    # Labels are shuffled once per run; keep the key separate from the first reading.
    versions = ["v07", "v08"]
    random.SystemRandom().shuffle(versions)
    labels = dict(zip(versions, ("A", "B")))
    (folder / "CLE_VARIANTES.json").write_text(json.dumps(labels, indent=2) + "\n")
    out = ["# Lecture comparative — ouvrir avant la clé des variantes\n",
           "Messages fictifs ; réponses exactes enregistrées, sans correction. Grille non notée. "
           "Les labels ne garantissent pas un aveugle parfait : le style peut révéler la version.\n"]
    with (folder / "GRILLE_VIERGE.csv").open("x", encoding="utf-8", newline="") as sink:
        fields = ("case_id", "turn", "label") + DIMENSIONS
        writer = csv.DictWriter(sink, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for case in suite["cases"]:
            selected = [r for r in records if r["case_id"] == case["id"]]
            if not selected:
                continue
            out.append("\n## " + case["id"] + " — " + case.get("title", "Scénario") + "\n")
            for turn in sorted({r["turn"] for r in selected}):
                rows = sorted((r for r in selected if r["turn"] == turn), key=lambda r: labels[r["variant"]])
                for r in rows:
                    label = labels[r["variant"]]
                    out.extend([f"\n### Tour {turn} · {label}\n", "Étudiant fictif :\n",
                                "~~~~text\n" + r["student"] + "\n~~~~\n", "Réponse enregistrée :\n",
                                "~~~~text\n" + (r["response"] if r["response"] is not None else
                                                 "[Aucune réponse générée : " + r["status"] + "]") + "\n~~~~\n",
                                "Attendus à examiner : " + "; ".join(r["expected_for_human_review"]) + "\n",
                                "Signaux à examiner : " + "; ".join(r["red_flags_for_human_review"]) + "\n"])
                    writer.writerow({"case_id": r["case_id"], "turn": turn, "label": label})
    (folder / "LECTURE_COMPARATIVE.md").write_text("\n".join(out), encoding="utf-8")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default=str(ROOT / "pedagogy/qa/COACH_DEV_CASES_V08.json"))
    parser.add_argument("--provider", choices=("dry-run", "mock", "mistral"), default="dry-run")
    parser.add_argument("--allow-billable", action="store_true")
    parser.add_argument("--unlock-reserved", action="store_true")
    parser.add_argument("--max-calls", type=int, default=12, help="Explicit ceiling, default 12 attempts")
    parser.add_argument("--case", action="append")
    parser.add_argument("--output-dir", required=True, help="New directory; never overwrite a run")
    args = parser.parse_args(argv)
    if args.provider == "mistral" and not args.allow_billable:
        parser.error("Mistral requires --allow-billable")
    freeze_sha = verify_freeze()
    suite = cases_from_file(Path(args.suite))
    if suite.get("split") == "reserved" and not args.unlock_reserved:
        parser.error("Reserved cases require --unlock-reserved after the prompt freeze; never tune on these results")
    selected = set(args.case or [])
    if selected - {c["id"] for c in suite["cases"]}:
        parser.error("Unknown case")
    planned = 2 * sum(len(c["turns"]) for c in suite["cases"] if not selected or c["id"] in selected)
    if args.max_calls < 1 or (args.provider == "mistral" and planned > args.max_calls):
        parser.error("Planned calls exceed the explicit limit; select fewer cases or set --max-calls")
    config = settings(ROOT)
    provider = None
    if args.provider != "dry-run":
        config["CHAT_PROVIDER"] = args.provider
        provider = provider_from_settings(config)
        if not provider.configured:
            parser.error("MISTRAL_API_KEY missing")
    folder = Path(args.output_dir)
    folder.mkdir(mode=0o700, parents=True, exist_ok=False)
    records = []
    with (folder / "responses.jsonl").open("x", encoding="utf-8") as sink:
        for record in collect(suite, provider, selected):
            record.update(freeze_sha256=freeze_sha, suite_sha256=hashlib.sha256(Path(args.suite).read_bytes()).hexdigest())
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            sink.flush()
            records.append(record)
    report = {"timestamp_utc": datetime.now(timezone.utc).isoformat(), "provider": args.provider,
              "planned_calls": planned, "attempt_ceiling": args.max_calls, "freeze_sha256": freeze_sha,
              "model_requested": provider.model if provider else None,
              "parameters": {"temperature": 0.2, "max_tokens": config["CHAT_MAX_TOKENS"],
                             "timeout_seconds": config["CHAT_TIMEOUT_SECONDS"], "stream": False, "tool_choice": "none"},
              "split": suite.get("split", "regression"), "summary": summary(records),
              "currency_cost": None, "cost_note": "No verified tariff supplied; tokens are measured, not a billing statement.",
              "pedagogical_verdict": None}
    (folder / "MESURES.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    write_review(folder, records, suite)
    print(json.dumps(report, ensure_ascii=False))
    return int(any(r["status"] == "api_error" for r in records))


if __name__ == "__main__":
    sys.exit(main())
