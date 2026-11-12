import csv
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from run_lifecycle_audit import IDS,load_suite

class LifecycleAuditTest(unittest.TestCase):
    def test_synthetic_scenarios_cover_stages_and_all_candidate_codes(self):
        _,suite,_=load_suite();cases=suite['cases']
        self.assertEqual(suite['data'],'synthetic_only')
        self.assertEqual(len(cases),14)
        self.assertEqual(sum(len(c['turns']) for c in cases),28)
        self.assertEqual({code for c in cases for code in c['competencies']},{'A1','A2','A3','B1','B2','B3','C1','C2','D1','D2','D3'})
        self.assertIn('équipe et motivation',{c['stage'] for c in cases})
        self.assertIn('cahier des charges',{c['stage'] for c in cases})

    def test_mock_separates_threads_and_human_rubric(self):
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            subprocess.run([sys.executable,'scripts/run_lifecycle_audit.py','--provider','mock','--output-dir',str(out)],check=True,capture_output=True)
            rows=[json.loads(x) for x in (out/'responses.jsonl').read_text().splitlines()]
            self.assertEqual(len(rows),28)
            self.assertEqual({r['case_id'] for r in rows},set(IDS))
            first={r['case_id']:r['student'] for r in rows if r['turn']==1}
            for r in rows:
                messages=r['messages_exact'];self.assertEqual(len(messages),2 if r['turn']==1 else 4)
                self.assertEqual(messages[1]['content'],first[r['case_id']])
                self.assertEqual(messages[-1]['content'],r['student'])
                for criterion in r['expected_for_human_review']:
                    self.assertNotIn(criterion,' '.join(m['content'] for m in messages))
            with (out/'GRILLE_VIERGE.csv').open() as f:review=list(csv.DictReader(f))
            self.assertEqual(len(review),28)
            self.assertTrue(all(not any(v for k,v in r.items() if k not in ('case_id','turn','label')) for r in review))

    def test_failure_stops_without_automatic_retry_and_preserves_report(self):
        from unittest.mock import patch
        from contextlib import redirect_stdout
        from io import StringIO
        from ptd_coach.service import DomainError
        import run_lifecycle_audit as runner
        class FailedProvider:
            name='mock';model='mock-error';max_tokens=0;configured=True
            calls=0
            def complete(self,messages):
                self.calls+=1
                raise DomainError(502,'mock_failure','Échec fictif')
        fake=FailedProvider()
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            with patch.object(runner,'MockChatProvider',return_value=fake), redirect_stdout(StringIO()):
                result=runner.main(['--provider','mock','--output-dir',str(out)])
            report=json.loads((out/'MESURES.json').read_text())
            self.assertEqual(result,1)
            self.assertEqual(fake.calls,1)
            self.assertEqual(report['attempted_calls'],1)
            self.assertEqual(report['completed_calls'],0)
            self.assertTrue(report['stopped_on_error'])
            self.assertEqual(len((out/'responses.jsonl').read_text().splitlines()),1)
