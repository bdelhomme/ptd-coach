"""Guard the explicitly frozen baseline and the deduplicated import inventory."""
import hashlib
import json
from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class PedagogyIntegrationTest(unittest.TestCase):
    def test_candidate_v03_is_preserved_byte_for_byte(self):
        candidate = ROOT / "pedagogy/competencies/candidate-v0.3.json"
        self.assertEqual(hashlib.sha256(candidate.read_bytes()).hexdigest(),
                         "56558fec5b3005019a65b0e600b53c6c908ea157d50358e852dd5667411851d8")

    def test_import_targets_exist_and_v06_cases_have_one_canonical_source(self):
        manifest = json.loads((ROOT / "assets/PEDAGOGY_IMPORTS_V06_V07.json").read_text(encoding="utf-8"))
        self.assertEqual([a["version"] for a in manifest["archives"]], ["0.6", "0.7"])
        imported = []
        duplicates = []
        for archive in manifest["archives"]:
            for entry in archive["files"]:
                if entry["action"] == "integrated":
                    self.assertTrue((ROOT / entry["target"]).is_file())
                    imported.append(entry["target"])
                elif entry["action"] == "deduplicated":
                    duplicates.append(entry["target"])
        self.assertEqual(len(imported), 14)
        self.assertEqual(len(set(imported)), len(imported))
        self.assertEqual(duplicates, ["pedagogy/qa/COACH_ACCEPTANCE_CASES_V06.json"])
        self.assertFalse((ROOT / "inputs/COACH_ACCEPTANCE_CASES_V06.json").exists())


if __name__ == "__main__":
    unittest.main()
