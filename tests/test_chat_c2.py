"""c2 uses the existing engine and keeps all previous commitments intact."""
import csv
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

from ptd_coach.chat_context_v08_c2 import ChatContextV08C2
from ptd_coach.chat_service import ChatService
import test_chat_http as http
from test_chat import RecordingProvider

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import compare_conversation_c2 as comparison


class C2Test(unittest.TestCase):
    def test_fiche_replaces_r03_without_changing_c1(self):
        context = ChatContextV08C2()
        self.assertEqual([r['id'] for r in context.select_resources('Dépendances et planning fictifs', [])], ['R04'])
        self.assertEqual([r['id'] for r in context.select_resources('coordination de l’équipe', [])], ['R01'])
        self.assertEqual(context.select_resources('Merci, stop', []), [])
        comparison.verify_freeze()
        self.assertNotEqual(context.digest, comparison.ChatContextV08().digest)

    def test_c2_freeze_and_example_review_precede_evaluation(self):
        self.assertEqual(len(comparison.verify_c2_freeze()), 64)
        review = json.loads((ROOT / 'pedagogy/qa/V08_C2_FREEZE.json').read_text())
        self.assertIn('docs/V08_C2_CONCEPT_REVIEW.md', review['files'])
        self.assertIn('pedagogy/resources/R04-concepts-projet-c2.md', review['files'])

    def test_reserved_or_arbitrary_suite_is_rejected_before_read(self):
        with patch.object(Path, 'read_text', side_effect=AssertionError('must not open')):
            for path in (ROOT / 'pedagogy/qa/COACH_RESERVED_CASES_V08.json', Path('/tmp/copy.json')):
                with self.assertRaises(ValueError):
                    comparison.load_suite(path)

    def test_all_development_runs_isolate_context_and_exclude_oracles(self):
        for name in ('COACH_DEV_CASES_V08.json', 'COACH_CONCEPT_CASES_C2.json', 'COACH_MULTI_TURN_CASES_V07.json'):
            suite = comparison.load_suite(ROOT / 'pedagogy/qa' / name)
            for case in suite['cases']:
                for turn in case['turns']:
                    turn['look_for'] = ['ORACLE_C2_NEVER_SENT']
            provider = RecordingProvider()
            rows = list(comparison.collect(suite, provider))
            self.assertEqual(len(rows), 3 * sum(len(c['turns']) for c in suite['cases']))
            self.assertNotIn('ORACLE_C2_NEVER_SENT', json.dumps(provider.calls))
            self.assertTrue(all(r['prompt_version'].endswith('c2') for r in rows if r['variant'] == 'c2'))
            for r in rows:
                self.assertEqual(hashlib.sha256(json.dumps(r['messages_exact'], ensure_ascii=False, sort_keys=True).encode()).hexdigest(), r['messages_sha256'])

    def test_filtered_order_rotates_and_histories_are_independent(self):
        suite = comparison.load_suite(ROOT / 'pedagogy/qa/COACH_DEV_CASES_V08.json')
        rows = list(comparison.collect(suite, RecordingProvider(), {'D03', 'D09'}))
        self.assertEqual(len(rows), 18)
        self.assertEqual([(r['case_id'], r['variant']) for r in rows if r['turn'] == 1],
            [('D03', 'v07'), ('D03', 'c1'), ('D03', 'c2'), ('D09', 'c1'), ('D09', 'c2'), ('D09', 'v07')])
        self.assertEqual(sum(len(r['messages_exact']) == 2 for r in rows), 6)
        for r in rows:
            self.assertEqual(len(r['messages_exact']), r['turn'] * 2)

    def test_failure_stops_whole_pass_without_retry(self):
        from ptd_coach.service import DomainError
        provider = RecordingProvider()
        suite = comparison.load_suite(ROOT / 'pedagogy/qa/COACH_DEV_CASES_V08.json')
        with patch.object(provider, 'complete', side_effect=DomainError(502, 'fixture', 'sanitized')) as call:
            rows = list(comparison.collect(suite, provider))
        self.assertEqual(call.call_count, 1)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]['status'], 'api_error')

    def test_paid_gate_and_call_ceiling_precede_provider(self):
        with tempfile.TemporaryDirectory() as directory, patch('ptd_coach.chat_provider.build_opener') as network:
            for args in (['--provider', 'mistral'], ['--provider', 'mistral', '--allow-billable']):
                with patch('sys.stderr', new=io.StringIO()), self.assertRaises(SystemExit):
                    comparison.main(['--output-dir', directory + '/run'] + args)
            network.assert_not_called()

    def test_review_is_unscored_and_preserves_exact_text(self):
        suite = comparison.load_suite(ROOT / 'pedagogy/qa/COACH_DEV_CASES_V08.json')
        rows = list(comparison.collect(suite, RecordingProvider(), {'D03', 'D09'}))
        with tempfile.TemporaryDirectory() as directory:
            folder = Path(directory)
            comparison.write_review(folder, rows)
            with (folder / 'GRILLE_VIERGE.csv').open() as file:
                grid = list(csv.DictReader(file))
            self.assertEqual(len(grid), 18)
            self.assertTrue(all(not r[k] for r in grid for k in comparison.REVIEW_FIELDS))
            markdown = (folder / 'LECTURE_COMPARATIVE.md').read_text()
            self.assertTrue(all('~~~~text\n' + r['response'] + '\n~~~~' in markdown for r in rows))


class C2HttpTest(http.ChatHttpTest):
    def setUp(self):
        super().setUp()
        # Existing HTTP surface, only a context injection and an isolated test DB.
        self.chat.context = ChatContextV08C2()
        self.chat.contexts['v08'] = self.chat.context

    def create(self, session, scope='individual'):
        status, _, row = self.request('/api/coach/conversations', 'POST',
            {'scope': scope, 'synthetic_confirmed': True, 'coach_version': 'v08'}, session)
        self.assertEqual(status, 201)
        return '/api/coach/conversations/' + row['id']


if __name__ == '__main__':
    unittest.main()
