import csv
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import run_coach_eval_v07 as runner
import review_coach_eval_v07 as review


class TestCoachEvaluationHarness(unittest.TestCase):
    def setUp(self):
        self.prompt = (ROOT / "pedagogy/prompts/COACH_SYSTEM_DRAFT_V07.md").read_text(encoding="utf-8")
        self.multi = runner.cases_from_file(ROOT / "pedagogy/qa/COACH_MULTI_TURN_CASES_V07.json")
        self.single = runner.cases_from_file(ROOT / "pedagogy/qa/COACH_ACCEPTANCE_CASES_V06.json")

    def test_case_counts_and_turn_counts(self):
        self.assertEqual(len(self.single["cases"]), 20)
        self.assertEqual(len(self.multi["cases"]), 12)
        self.assertEqual(sum(len(x["turns"]) for x in self.multi["cases"]), 26)

    def test_dry_runs_never_call_network_and_yield_expected_records(self):
        with patch.object(runner, "call_mistral", side_effect=AssertionError("Network forbidden")) as call:
            records = list(runner.evaluate(self.multi, self.prompt, provider="dry-run"))
            call.assert_not_called()
        self.assertEqual(len(records), 26)
        self.assertTrue(all(r["response"] is None and r["status"] == "not_called" for r in records))
        self.assertEqual(records[0]["case_id"], "M01")
        self.assertEqual(records[1]["turn"], 2)

    def test_single_cases_supported(self):
        records = list(runner.evaluate(self.single, self.prompt, provider="dry-run"))
        self.assertEqual(len(records), 20)
        self.assertEqual([x["case_id"] for x in records if x["critical_veto_to_review"]],
                         ["T13", "T14", "T15", "T16", "T17", "T18", "T19", "T20"])

    def test_rubric_is_not_sent_to_model_and_history_is_case_scoped(self):
        # Stub only: no request, key or real model is involved.
        with patch.object(runner, "call_mistral", return_value={"response": "Réponse fictive"}) as call:
            records = list(runner.evaluate(self.multi, self.prompt, provider="mistral",
                                          selected={"M01", "M02"}))
        self.assertEqual(len(records), 4)
        histories = [args.args[2] for args in call.call_args_list]
        # evaluate mutates each list as the conversation progresses. Inspect its
        # final content: criteria must never have been included in any message.
        for history in histories:
            self.assertEqual(set(history[0]), {"role", "content"})
            self.assertTrue(all(set(m) == {"role", "content"} for m in history))
            text = "\n".join(m["content"] for m in history)
            self.assertNotIn("Commencer par un questionnaire", text)
            self.assertNotIn("Attribuer une partie définitive à chaque étudiant", text)
        self.assertIn(self.multi["cases"][0]["turns"][0]["student"], histories[0][1]["content"])
        self.assertNotIn(histories[0][1], histories[2])
        self.assertEqual([m["role"] for m in histories[0]],
                         ["system", "user", "assistant", "user", "assistant"])

    def test_failed_call_stops_case_without_inventing_followup(self):
        with patch.object(runner, "call_mistral", side_effect=RuntimeError("simulated error")) as call:
            records = list(runner.evaluate(self.multi, self.prompt, provider="mistral",
                                          selected={"M03"}))
        self.assertEqual(call.call_count, 1)
        self.assertEqual(len(records), 1)
        self.assertEqual(records[0]["status"], "api_error")
        self.assertIsNone(records[0]["response"])

    def test_selection_and_case_limit_preserve_whole_conversations(self):
        records = list(runner.evaluate(self.multi, self.prompt, selected={"M03", "M04"}, max_cases=1))
        self.assertEqual([(r["case_id"], r["turn"]) for r in records],
                         [("M03", 1), ("M03", 2), ("M03", 3)])

    def test_dry_run_error_and_empty_inputs_cannot_create_review_sheet(self):
        with tempfile.TemporaryDirectory() as d:
            source, output = Path(d) / "responses.jsonl", Path(d) / "ratings.csv"
            for record in (None, {"status": "not_called"}, {"status": "api_error"}):
                source.write_text("" if record is None else json.dumps(record) + "\n", encoding="utf-8")
                with self.assertRaises(ValueError):
                    review.make_sheet(source, output, "lecteur")
                self.assertFalse(output.exists())

    def test_partial_rating_reports_known_veto_without_passing_gate(self):
        with tempfile.TemporaryDirectory() as d:
            ratings = Path(d) / "ratings.csv"
            with ratings.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.DictWriter(fh, fieldnames=review.FIELDS)
                writer.writeheader()
                writer.writerow({"case_id": "M07", "turn": 1, "critical_failure": "oui"})
            result = review.summary(ratings)
            self.assertEqual(result["decision"], "REVIEW_INCOMPLETE")
            self.assertEqual(result["critical_failures_identified"], 1)
            self.assertIsNone(result["adequate_rate_if_complete"])

    def test_partial_model_ratings_below_gate_require_revision(self):
        with tempfile.TemporaryDirectory() as d:
            ratings = Path(d) / "ratings.csv"
            with ratings.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.DictWriter(fh, fieldnames=review.FIELDS)
                writer.writeheader()
                for turn in range(1, 4):
                    row = {"case_id": "M03", "turn": turn, "critical_failure": "non",
                           **{dim: "2" for dim in review.DIMS}}
                    if turn == 3:
                        row["correctness"] = "0"
                    writer.writerow(row)
            self.assertEqual(review.summary(ratings)["decision"], "NEEDS_REVISION")

    def test_private_and_collective_scopes_explicit(self):
        private = runner.prepare_system(self.prompt, "individual")
        collective = runner.prepare_system(self.prompt, "collective")
        self.assertIn("espace privé", private)
        self.assertIn("écran collectif", collective)
        self.assertNotEqual(private, collective)

    def test_non_synthetic_data_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            file = Path(d) / "cases.json"
            obj = dict(self.single, data="real_student_data")
            file.write_text(json.dumps(obj), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "synthetic_only"):
                runner.cases_from_file(file)

    def test_manual_scoring_requires_human_entry(self):
        with tempfile.TemporaryDirectory() as d:
            folder = Path(d)
            responses = folder / "responses.jsonl"
            responses.write_text(json.dumps({"status": "model_called", "case_id": "M01", "turn": 1,
                            "scope": "individual", "student": "essai fictif", "response": "Réponse fictive"}) + "\n", encoding="utf-8")
            ratings = folder / "ratings.csv"
            self.assertEqual(review.make_sheet(responses, ratings, "lecteur"), 1)
            self.assertEqual(review.summary(ratings)["decision"], "REVIEW_INCOMPLETE")
            with ratings.open(newline="", encoding="utf-8") as fh:
                rows = list(csv.DictReader(fh))
            for dim in review.DIMS:
                rows[0][dim] = "2"
            rows[0]["critical_failure"] = "non"
            with ratings.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.DictWriter(fh, fieldnames=review.FIELDS)
                writer.writeheader(); writer.writerows(rows)
            self.assertEqual(review.summary(ratings)["decision"], "MEETS_PROPOSED_SCREENING_GATE")
            rows[0]["critical_failure"] = "oui"
            with ratings.open("w", newline="", encoding="utf-8") as fh:
                writer = csv.DictWriter(fh, fieldnames=review.FIELDS)
                writer.writeheader(); writer.writerows(rows)
            self.assertEqual(review.summary(ratings)["decision"], "NEEDS_REVISION")


if __name__ == "__main__":
    unittest.main()
