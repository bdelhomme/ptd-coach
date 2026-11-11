"""Experimental opt-in bundle; existing candidate contexts and fingerprints remain untouched."""
import hashlib
import json
from .chat_context_v08_c2 import ChatContextV08C2
from .library import catalogue, select

class LibraryContext(ChatContextV08C2):
    version = 'conversation-v08-c2-library-experimental-0.1'

    def __init__(self, root=None):
        super().__init__() if root is None else super().__init__(root)
        self.resources = [self.convert(m) for m in catalogue()]
        self.digest = hashlib.sha256((self.system('individual', self.resources) + self.system('collective', self.resources)).encode()).hexdigest()

    @staticmethod
    def convert(m):
        return {'id': m['id'], 'title': m['nom'], 'status': 'brouillon', 'content': json.dumps(m, ensure_ascii=False)}

    def select_resources(self, message, history):
        choice = select(message, history)
        return [self.convert(choice['method'])] if choice else []

    def system(self, scope, resources=()):
        return super().system(scope, resources) + ('\n\nBibliothèque expérimentale : si une fiche fournie est utile, cite son identifiant et son nom exacts, explique brièvement pourquoi et propose une première application proportionnée. N’invente aucune source ou valeur de projet. Les exemples de fiche sont fictifs ; ne les attribue pas au projet. S’il n’y a pas de fiche pertinente, réponds directement. Les décisions et validations appartiennent aux personnes concernées.')
