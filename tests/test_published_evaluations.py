"""Integrity of the public fictional corpus, never a pedagogical score."""

import csv
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
CORPUS = ROOT / "pedagogy/evaluations/mistral-small-v07"


class PublishedEvaluationTest(unittest.TestCase):
    def test_original_and_publication_manifests_cover_exact_bytes(self):
        original = json.loads((CORPUS / "MANIFESTE.json").read_text())
        publication = json.loads((CORPUS / "MANIFESTE_PUBLICATION.json").read_text())
        actual = {p.relative_to(CORPUS).as_posix() for p in CORPUS.rglob("*") if p.is_file()}
        self.assertEqual({e["path"] for e in publication["files"]},
                         actual - {"MANIFESTE_PUBLICATION.json"})
        self.assertEqual(len(original["files"]), 24)
        self.assertEqual(len(actual), 27)
        for manifest in (original, publication):
            for entry in manifest["files"]:
                path = CORPUS / entry["path"]
                self.assertFalse(Path(entry["path"]).is_absolute())
                self.assertNotIn("..", Path(entry["path"]).parts)
                content = path.read_bytes()
                self.assertEqual(hashlib.sha256(content).hexdigest(), entry["sha256"])
                self.assertEqual(len(content), entry["bytes"])
        final = CORPUS / "donnees/chat-v1-2-mistral-v07.jsonl"
        self.assertEqual(hashlib.sha256(final.read_bytes()).hexdigest(),
                         "3e64f913ae685074e52b4be03f14932b334e345b99d14fb05e88d8ae57e85754")

    def test_all_transcripts_preserve_turns_criteria_and_verbatim(self):
        suite = json.loads((CORPUS / "donnees/SCENARIOS_V07.json").read_text())
        self.assertEqual((CORPUS / "donnees/SCENARIOS_V07.json").read_bytes(),
                         (ROOT / "pedagogy/qa/COACH_MULTI_TURN_CASES_V07.json").read_bytes())
        cases = {c["id"]: c for c in suite["cases"]}
        expected = [(c["id"], n) for c in suite["cases"] for n in range(1, len(c["turns"]) + 1)]
        files = [
            ("chat-v1-mistral-smoke.jsonl", "annexes/TRANSCRIPTIONS_SMOKE_V1.md", 2),
            ("chat-v1-mistral-v07.jsonl", "annexes/TRANSCRIPTIONS_V1.md", 26),
            ("chat-v1-1-mistral-v07.jsonl", "annexes/TRANSCRIPTIONS_V1_1.md", 26),
            ("chat-v1-2-mistral-v07.jsonl", "01_TRANSCRIPTIONS_V1_2.md", 26),
        ]
        total_tokens = 0
        for source, readable, count in files:
            rows = [json.loads(line) for line in (CORPUS / "donnees" / source).read_text().splitlines()]
            self.assertEqual([(r["case_id"], r["turn"]) for r in rows], expected[:count])
            blocks = re.findall(r"~~~text\n(.*?)\n~~~\n", (CORPUS / readable).read_text(), re.S)
            self.assertEqual(blocks, [v for r in rows for v in (r["student"], r["response"])])
            for r in rows:
                case = cases[r["case_id"]]
                turn = case["turns"][r["turn"] - 1]
                self.assertEqual(r["student"], turn["student"])
                self.assertEqual(r["scope"], case["scope"])
                self.assertEqual(r["expected_for_human_review"], turn["look_for"])
                self.assertEqual(r["red_flags_for_human_review"], turn["red_flags"])
                self.assertEqual(r["critical_veto_to_review"], turn.get("critical"))
                self.assertEqual(r["status"], "model_called")
                self.assertEqual(r["usage"]["total_tokens"], r["usage"]["prompt_tokens"] + r["usage"]["completion_tokens"])
                total_tokens += r["usage"]["total_tokens"]
        self.assertEqual(len(cases), 12)
        self.assertEqual(len(expected), 26)
        self.assertEqual(total_tokens, 271066)

    def test_human_grid_stays_unscored_and_matches_final_responses(self):
        with (CORPUS / "02_GRILLE_HUMAINE_VIERGE.csv").open(newline="", encoding="utf-8") as fh:
            grid = list(csv.DictReader(fh))
        final = [json.loads(line) for line in (CORPUS / "donnees/chat-v1-2-mistral-v07.jsonl").read_text().splitlines()]
        self.assertEqual(len(grid), 26)
        for row, response in zip(grid, final):
            for field in ("student", "response", "scope", "case_id"):
                self.assertEqual(row[field], response[field])
            self.assertEqual(int(row["turn"]), response["turn"])
            for field in ("reviewer", "relevance", "correctness", "student_agency",
                          "epistemic_distinctions", "proportionality", "critical_failure", "notes"):
                self.assertEqual(row[field], "")

    def test_context_snapshot_reproduces_recorded_fingerprint(self):
        content = ((CORPUS / "contexte/SYSTEME_INDIVIDUEL_V1_2.txt").read_bytes() +
                   (CORPUS / "contexte/SYSTEME_COLLECTIF_V1_2.txt").read_bytes())
        self.assertEqual(hashlib.sha256(content).hexdigest(),
                         "c321c72fa966b1d13a0e29f1ac8fcd120daafe3859f02b75477a05682322487a")


if __name__ == "__main__":
    unittest.main()
