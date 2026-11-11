import json
import tempfile
import unittest
from pathlib import Path
from ptd_coach.library import catalogue, select
from ptd_coach.chat_context_library import LibraryContext
from ptd_coach.chat_service import ChatService
from ptd_coach.chat_provider import MockChatProvider

class LibraryTests(unittest.TestCase):
    def test_catalogue_has_sources_and_candidate_competencies(self):
        entries = catalogue()
        self.assertEqual(len(entries), 10)
        self.assertEqual(len({x['id'] for x in entries}), len(entries))
        ids = {x['id'] for x in entries}
        valid = {'A1','A2','A3','B1','B2','B3','C1','C2','D1','D2','D3'}
        for item in entries:
            self.assertTrue(set(item['competences']) <= valid)
            self.assertTrue(set(item['liens']) <= ids)
            self.assertTrue(item['source']['url'].startswith('https://'))
            for field in ('resume','etapes','exemple','modele','erreurs','limites','apprentissage','tuteur','coach','statut'):
                self.assertTrue(item[field], (item['id'], field))
            self.assertIn('Brouillon', item['statut'])

    def test_situation_without_method_name_and_no_irrelevant_tool(self):
        self.assertEqual(select('Notre client change d’avis tout le temps')['method']['id'], 'M06')
        self.assertEqual(select('Notre projet prend du retard')['method']['id'], 'M08')
        self.assertIsNone(select('Bonjour, merci pour votre aide.'))

    def test_context_only_in_short_followup_and_only_user_messages(self):
        history = [{'role':'user','content':'Comment rédiger le cahier des charges ?'}, {'role':'assistant','content':'Expliquons cela.'}]
        choice = select('Peux-tu donner un exemple ?', history)
        self.assertEqual(choice['method']['id'], 'M03')
        self.assertTrue(choice['context_used'])
        self.assertIsNone(select('Bonjour, merci pour votre aide.', history))
        self.assertIsNone(select('Peux-tu donner un exemple ?', [{'role':'assistant','content':'Le cahier des charges'}]))

    def test_bundle_keeps_fictitious_examples_and_records_selection(self):
        context = LibraryContext()
        selected = context.select_resources('Rédiger le cahier des charges', [])
        self.assertEqual(selected[0]['id'], 'M03')
        system = context.system('individual', selected)
        self.assertIn('M03', system)
        self.assertIn('N’invente aucune source ou valeur', system)
        self.assertEqual(context.select_resources('Bonjour', []), [])

    def test_isolated_service_retains_access_controls(self):
        with tempfile.TemporaryDirectory() as tmp:
            service = ChatService(Path(tmp)/'test.sqlite3', MockChatProvider(), context=LibraryContext())
            self.assertEqual(service.public_config()['prompt_version'], 'conversation-v08-c2-library-experimental-0.1')
            with self.assertRaises(Exception):
                service.student('unknown')

class LibraryHTTPTests(unittest.TestCase):
    def test_public_library_without_chat_or_provider(self):
        import threading
        import urllib.request
        from ptd_coach.server import DemoServer
        with DemoServer(('127.0.0.1', 0), None, None) as server:
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            try:
                base = 'http://127.0.0.1:' + str(server.server_address[1])
                with urllib.request.urlopen(base + '/api/library') as response:
                    self.assertEqual(len(json.load(response)), 10)
                with urllib.request.urlopen(base + '/bibliotheque') as response:
                    self.assertIn('Bibliothèque', response.read().decode())
            finally:
                server.shutdown(); thread.join()
