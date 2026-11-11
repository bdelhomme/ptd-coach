import tempfile
import unittest
from pathlib import Path
from ptd_coach.chat_context_reliable import ReliableContext
from ptd_coach.chat_context_library import LibraryContext
from ptd_coach.chat_provider import MockChatProvider
from ptd_coach.chat_service import ChatService
from ptd_coach.service import DomainError
import uuid

class ReliabilityContextTest(unittest.TestCase):
    def test_separate_version_and_resource_selection(self):
        base=LibraryContext(); candidate=ReliableContext()
        self.assertNotEqual(base.digest,candidate.digest)
        self.assertNotEqual(base.version,candidate.version)
        self.assertIn("absence d'accord ne signifie pas refus",candidate.system('individual',[]))
        for message in ['Notre client change d’avis','Rédiger le cahier des charges','Bonjour']:
            self.assertEqual([r['id'] for r in base.select_resources(message,[])],
                             [r['id'] for r in candidate.select_resources(message,[])])

    def test_scope_access_remains_enforced(self):
        with tempfile.TemporaryDirectory() as d:
            service=ChatService(Path(d)/'test.sqlite3',MockChatProvider(),context=ReliableContext())
            item=service.create('student_demo_01',str(uuid.uuid4()),{'scope':'individual','synthetic_confirmed':True,'coach_version':'v08'})
            with self.assertRaises(DomainError):
                service.conversation('student_demo_02',item['id'])
            self.assertEqual(service.conversation('student_demo_01',item['id'])['scope'],'individual')

    def test_mock_comparison_has_paired_outputs_and_blank_review(self):
        import csv, json, subprocess, sys
        with tempfile.TemporaryDirectory() as tmp:
            out=Path(tmp)/'out'
            subprocess.run([sys.executable,'scripts/compare_reliable_context.py','--provider','mock','--output-dir',str(out)],check=True,capture_output=True)
            rows=[json.loads(line) for line in (out/'responses.jsonl').read_text().splitlines()]
            self.assertEqual(len(rows),12)
            self.assertEqual({r['case_id'] for r in rows},{'TX05','TX07','TX22'})
            self.assertEqual({r['variant'] for r in rows},{'bibliotheque','fiabilite'})
            self.assertTrue(all(r['max_tokens_requested'] is None for r in rows))
            with (out/'GRILLE_VIERGE.csv').open() as stream:
                review=list(csv.DictReader(stream))
            self.assertEqual(len(review),12)
            self.assertTrue(all(not any(value for key,value in row.items() if key not in ('case_id','turn','label')) for row in review))

    def test_unbounded_mode_is_explicit_and_scoped(self):
        from ptd_coach.__main__ import apply_test_output_policy
        from ptd_coach.chat_provider_reasoning import MistralReasoningProvider
        large=MistralReasoningProvider('key','mistral-large-4',700,45,'medium')
        self.assertEqual(apply_test_output_policy(large,False,True).max_tokens,700)
        with self.assertRaises(ValueError): apply_test_output_policy(large,True,False)
        with self.assertRaises(ValueError): apply_test_output_policy(MockChatProvider(),True,True)
        self.assertIsNone(apply_test_output_policy(large,True,True).max_tokens)
