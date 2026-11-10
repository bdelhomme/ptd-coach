#!/usr/bin/env python3
"""Replay V0.6/V0.7 through the application's actual context and service.

Synthetic inputs only. Human rubrics are output annotations, never model input.
"""

import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import tempfile
import uuid

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from ptd_coach.chat_config import settings, provider_from_settings
from ptd_coach.chat_context import ChatContext, PROMPT_VERSION
from ptd_coach.chat_service import ChatService
from ptd_coach.service import DomainError
from run_coach_eval_v07 import cases_from_file, iter_turns


def evaluate(suite, context, provider=None, selected=None, max_cases=None):
    with tempfile.TemporaryDirectory(prefix="ptd-synthetic-eval-") as directory:
        service = ChatService(Path(directory) / "eval.sqlite3", provider, max_calls=1000, context=context) if provider else None
        cases = [case for case in suite["cases"] if not selected or case["id"] in selected]
        if selected and set(selected) - {c["id"] for c in cases}:
            raise ValueError("Unknown selected case")
        if max_cases:
            cases = cases[:max_cases]
        for case in cases:
            conversation = service.create("student_demo_01", str(uuid.uuid4()),
                {"scope": case["scope"], "synthetic_confirmed": True,
                 "coach_version": getattr(context, "coach_version", "v07")}) if service else None
            for index, turn in enumerate(iter_turns(case), 1):
                record = {"suite": suite["id"], "case_id": case["id"], "scope": case["scope"],
                          "turn": index, "student": turn["student"], "prompt_version": getattr(context, "version", PROMPT_VERSION),
                          "context_sha256": context.digest, "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                          "expected_for_human_review": turn.get("look_for", []),
                          "red_flags_for_human_review": turn.get("red_flags", []),
                          "critical_veto_to_review": turn.get("critical"),
                          "provider": provider.name if provider else "dry-run", "response": None, "status": "not_called"}
                if service:
                    try:
                        conversation = service.send("student_demo_01", conversation["id"], str(uuid.uuid4()),
                            {"message": turn["student"], "version": conversation["version"]})
                        invocation = conversation["invocations"][-1]
                        record.update(invocation, response=conversation["messages"][-1]["content"],
                                      status="model_called" if provider.name == "mistral" else "mock_called")
                    except DomainError as error:
                        record.update(status="api_error", error=error.code)
                        yield record
                        break
                yield record


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--suite", default=str(ROOT / "pedagogy/qa/COACH_MULTI_TURN_CASES_V07.json"))
    parser.add_argument("--provider", choices=("dry-run", "mock", "mistral"), default="dry-run")
    parser.add_argument("--allow-billable", action="store_true")
    parser.add_argument("--model", help="Override MISTRAL_MODEL for this comparison")
    parser.add_argument("--case", action="append")
    parser.add_argument("--max-cases", type=int)
    parser.add_argument("--output", required=True, help="JSONL outside Git; existing files are never overwritten")
    args = parser.parse_args(argv)
    if args.provider == "mistral" and not args.allow_billable:
        parser.error("Mistral requires --allow-billable")
    if args.max_cases is not None and args.max_cases < 1:
        parser.error("--max-cases must be positive")
    suite = cases_from_file(Path(args.suite))
    if args.case and set(args.case) - {c["id"] for c in suite["cases"]}:
        parser.error("Unknown selected case")
    context, provider = ChatContext(), None
    if args.provider != "dry-run":
        config = settings(ROOT)
        config["CHAT_PROVIDER"] = args.provider
        if args.model:
            config["MISTRAL_MODEL"] = args.model
        provider = provider_from_settings(config)
        if not provider.configured:
            parser.error("MISTRAL_API_KEY missing in environment or local .env")
    failed, count, tokens, unknown = False, 0, 0, 0
    output = Path(args.output)
    output.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
    with output.open("x", encoding="utf-8") as sink:
        output.chmod(0o600)
        for record in evaluate(suite, context, provider, set(args.case or []), args.max_cases):
            sink.write(json.dumps(record, ensure_ascii=False) + "\n")
            sink.flush()
            count += 1
            failed |= record["status"] == "api_error"
            total = record.get("usage", {}).get("total_tokens")
            tokens += total or 0
            unknown += total is None
    print(json.dumps({"records": count, "known_total_tokens": tokens, "unmeasured_records": unknown,
                      "api_errors": failed, "output": str(output)}, ensure_ascii=False))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
