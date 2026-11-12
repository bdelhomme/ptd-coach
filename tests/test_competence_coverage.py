import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_competence_coverage import COMPETENCIES,SELECTED,load_cases

class CompetenceCoverageTest(unittest.TestCase):
    def test_selected_cases_span_candidate_codes_and_group(self):
        _,_,cases=load_cases()
        self.assertEqual(len(cases),12)
        self.assertEqual({x for c in cases for x in c['competencies']},COMPETENCIES)
        self.assertEqual(sum(c['scope']=='collective' for c in cases),7)
        self.assertEqual(sum(len(c['turns']) for c in cases),24)

    def test_mock_outputs_every_turn_without_evaluation_leak(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            subprocess.run([sys.executable,'scripts/run_competence_coverage.py','--provider','mock','--output-dir',str(out)],check=True,capture_output=True)
            rows=[json.loads(x) for x in (out/'responses.jsonl').read_text().splitlines()]
            self.assertEqual(len(rows),24)
            self.assertEqual({r['case_id'] for r in rows},set(SELECTED))
            self.assertTrue(all(r['max_tokens_requested'] is None for r in rows))
            first_turn={r['case_id']:r['student'] for r in rows if r['turn']==1}
            for r in rows:
                messages=r['messages_exact']
                self.assertEqual(len(messages),2 if r['turn']==1 else 4)
                self.assertEqual(messages[1]['content'],first_turn[r['case_id']])
                self.assertEqual(messages[-1]['content'],r['student'])
                sent=' '.join(m['content'] for m in r['messages_exact'])
                self.assertNotIn('expected_for_human_review',sent)
            with (out/'GRILLE_VIERGE.csv').open() as f: review=list(csv.DictReader(f))
            self.assertEqual(len(review),24)
            self.assertTrue(all(not any(v for k,v in r.items() if k not in ('case_id','turn','label')) for r in review))

    def test_explicit_case_subset_is_limited_to_development(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            subprocess.run([sys.executable,'scripts/run_competence_coverage.py','--provider','mock','--case','TX15','--output-dir',str(out)],check=True,capture_output=True)
            report=json.loads((out/'MESURES.json').read_text())
            self.assertEqual(report['selected_cases'],['TX15'])
            self.assertEqual(report['planned_calls'],2)
            self.assertEqual(report['completed_calls'],2)
