import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_thursday_audit import IDS,load_suite

class ThursdayAuditTest(unittest.TestCase):
    def test_suite_is_fictitious_and_preserves_conditional_obligation(self):
        _,suite,_=load_suite()
        self.assertEqual(suite['data'],'synthetic_only')
        self.assertEqual(tuple(c['id'] for c in suite['cases']),IDS)
        self.assertTrue(all(len(c['turns'])==2 for c in suite['cases']))
        self.assertIn('obligatoire en théorie',suite['cases'][0]['turns'][0]['student'])
    def test_mock_no_other_conversation_or_rubric_in_model_context(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            subprocess.run([sys.executable,'scripts/run_thursday_audit.py','--provider','mock','--output-dir',str(out)],check=True,capture_output=True)
            rows=[json.loads(x) for x in (out/'responses.jsonl').read_text().splitlines()]
            self.assertEqual(len(rows),6)
            for r in rows:
                messages=r['messages_exact'];self.assertEqual(len(messages),2 if r['turn']==1 else 4)
                for criterion in r['expected_for_human_review']:
                    self.assertNotIn(criterion,' '.join(m['content'] for m in messages))
            with (out/'GRILLE_VIERGE.csv').open() as f:review=list(csv.DictReader(f))
            self.assertEqual(len(review),6)
            self.assertTrue(all(not any(v for k,v in r.items() if k not in ('case_id','turn','label')) for r in review))

    def test_one_selected_development_case_runs_two_turns(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            subprocess.run([sys.executable,'scripts/run_thursday_audit.py','--provider','mock','--case','PJ02','--output-dir',str(out)],check=True,capture_output=True)
            report=json.loads((out/'MESURES.json').read_text())
            self.assertEqual(report['selected_cases'],['PJ02'])
            self.assertEqual(report['planned_calls'],2)
            self.assertEqual(report['completed_calls'],2)
