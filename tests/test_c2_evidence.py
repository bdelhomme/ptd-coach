"""Public fictitious evidence integrity; no model calls or pedagogical scoring."""
import csv
import hashlib
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from compare_conversation_c2 import summarize, verify_c2_freeze, REVIEW_FIELDS


class C2EvidenceTest(unittest.TestCase):
    def test_manifest_exact_messages_and_reports_match_54_responses(self):
        folder = ROOT / 'pedagogy/evaluations/v08-c2-comparison'
        manifest = json.loads((folder / 'MANIFESTE.json').read_text())
        files = {p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()}
        self.assertEqual(files, set(manifest['files']) | {'MANIFESTE.json'})
        for name, expected in manifest['files'].items():
            data = (folder / name).read_bytes()
            self.assertEqual(len(data), expected['bytes'])
            self.assertEqual(hashlib.sha256(data).hexdigest(), expected['sha256'])
        combined = []
        for name, count in (('01-first', 18), ('02-concepts', 18), ('03-safety', 12), ('04-repeat', 6)):
            rows = [json.loads(line) for line in (folder / name / 'responses.jsonl').read_text().splitlines()]
            self.assertEqual(len(rows), count)
            self.assertEqual(len({(r['case_id'], r['variant'], r['turn']) for r in rows}), count)
            report = json.loads((folder / name / 'MESURES.json').read_text())
            self.assertEqual(report['summary'], summarize(rows))
            self.assertIsNone(report['human_pedagogical_verdict'])
            markdown = (folder / name / 'LECTURE_COMPARATIVE.md').read_text()
            for row in rows:
                self.assertEqual(row['status'], 'model_called')
                self.assertEqual(row['c2_freeze_sha256'], verify_c2_freeze())
                self.assertEqual(hashlib.sha256(json.dumps(row['messages_exact'], ensure_ascii=False, sort_keys=True).encode()).hexdigest(), row['messages_sha256'])
                self.assertEqual(hashlib.sha256(row['messages_exact'][0]['content'].encode()).hexdigest(), row['system_sha256'])
                self.assertEqual(row['messages_exact'][-1]['content'], row['student'])
                self.assertIn('~~~~text\n' + row['response'] + '\n~~~~', markdown)
                self.assertEqual(row['max_tokens'], 700)
            combined.extend(rows)
        self.assertEqual(len(combined), 54)
        self.assertEqual(sum(r['usage']['total_tokens'] for r in combined), 132977)
        aggregate = json.loads((folder / 'MESURES_AGREGEES.json').read_text())
        self.assertFalse(aggregate['reserved_executed'])
        self.assertIsNone(aggregate['human_verdict'])
        self.assertEqual(aggregate['responses'], 54)

    def test_all_human_review_cells_stay_blank(self):
        folder = ROOT / 'pedagogy/evaluations/v08-c2-comparison'
        total = 0
        for path in folder.glob('*/GRILLE_VIERGE.csv'):
            with path.open() as file:
                rows = list(csv.DictReader(file))
            total += len(rows)
            self.assertTrue(all(not row[key] for row in rows for key in REVIEW_FIELDS))
        self.assertEqual(total, 54)


if __name__ == '__main__':
    unittest.main()
