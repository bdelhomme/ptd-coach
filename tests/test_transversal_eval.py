"""Checks for the transversal development campaign and its bounded runner."""
import csv
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from collections import Counter
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_transversal_eval as campaign
from test_chat import RecordingProvider
from ptd_coach.service import DomainError


class TransversalEvalTest(unittest.TestCase):
    def test_suite_covers_five_domains_and_eleven_candidate_competencies(self):
        suite = campaign.cases_from_file(campaign.SUITE)
        cases = suite["cases"]
        self.assertEqual(Counter(c["domain"] for c in cases), {
            "commanditaire": 6, "besoin_cdc": 6, "cooperation": 4,
            "pilotage_resolution": 4, "restitution_reflexivite": 4,
        })
        reference = json.loads((ROOT / "pedagogy/competencies/candidate-v0.3.json").read_text())
        self.assertEqual({code for c in cases for code in c["competencies"]},
                         {c["id"] for c in reference["competencies"]})
        self.assertEqual({c["method_signal"] for c in cases}, {"spontanee", "choix", "aucune"})
        self.assertTrue(all(c["student_work"] and len(c["turns"]) >= 2 for c in cases))
        selected = [c for c in cases if c["id"] in suite["first_comparison"]]
        self.assertEqual(len({c["domain"] for c in selected}), 5)
        self.assertEqual({c["scope"] for c in selected}, {"individual", "collective"})
        self.assertEqual(3 * sum(len(c["turns"]) for c in selected), campaign.CALL_CEILING)

    def test_mock_runs_full_suite_without_sending_review_criteria(self):
        provider = RecordingProvider()
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory) / "result"
            with patch.object(campaign, "provider_from_settings", return_value=provider):
                report = campaign.run("mock", folder)
            rows = [json.loads(line) for line in (folder / "responses.jsonl").read_text().splitlines()]
            self.assertTrue(report["complete"])
            self.assertEqual(len(rows), 144)
            self.assertEqual(report["mistral_attempts_recorded"], 0)
            self.assertEqual(sum(len(call) == 2 for call in provider.calls), 72)
            for row, call in zip(rows, provider.calls):
                self.assertEqual(row["messages_exact"], call)
                self.assertEqual(call[-1], {"role": "user", "content": row["student"]})
                serialized = json.dumps(call, ensure_ascii=False)
                self.assertTrue(all(expectation not in serialized for expectation in row["expected_for_human_review"]))
                self.assertEqual(hashlib.sha256(json.dumps(call, sort_keys=True, ensure_ascii=False).encode()).hexdigest(),
                                 row["messages_sha256"])
            with (folder / "GRILLE_VIERGE.csv").open() as stream:
                grid = list(csv.DictReader(stream))
            self.assertEqual(len(grid), len(rows))
            self.assertTrue(all(not line[k] for line in grid for k in campaign.REVIEW_FIELDS))

    def test_paid_guard_and_failure_produce_a_single_record_without_retry(self):
        provider = RecordingProvider()
        with tempfile.TemporaryDirectory() as directory, patch.object(
            campaign, "provider_from_settings", return_value=provider
        ) as factory, patch.object(provider, "complete", side_effect=DomainError(502, "fixture", "sanitized")) as call:
            folder = Path(directory) / "result"
            with self.assertRaises(ValueError):
                campaign.run("mistral", folder)
            factory.assert_not_called()
            report = campaign.run("mistral", folder, allow_billable=True)
            call.assert_called_once()
            self.assertFalse(report["complete"])
            self.assertEqual(report["mistral_attempts_recorded"], 1)
            row = json.loads((folder / "responses.jsonl").read_text())
            self.assertEqual(row["error"], "fixture")
            self.assertIsNone(row["response"])
            self.assertGreaterEqual(row["latency_ms"], 0)
            self.assertIn("messages_exact", row)

    def test_dry_run_records_plan_without_instantiating_provider(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(campaign, "provider_from_settings") as factory:
            folder = Path(directory) / "result"
            report = campaign.run("dry-run", folder)
            factory.assert_not_called()
            self.assertTrue(report["complete"])
            self.assertEqual(report["planned_records"], 144)
            self.assertEqual(sum(s["responses"] for s in report["summary"].values()), 0)
