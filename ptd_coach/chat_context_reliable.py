"""Opt-in research candidate; does not change c1/c2 prompts or their resources."""
import hashlib
from .chat_context import ROOT
from .chat_context_library import LibraryContext


class ReliableContext(LibraryContext):
    version = 'conversation-v08-library-reliability-experimental-0.1'

    def __init__(self, root=ROOT):
        self.reliability = (root / 'pedagogy/prompts/COACH_CADRAGE_FIABILITE_V01.md').read_text(encoding='utf-8')
        super().__init__(root)
        self.digest = hashlib.sha256((self.system('individual', self.resources) +
                                      self.system('collective', self.resources)).encode()).hexdigest()

    def system(self, scope, resources=()):
        return super().system(scope, resources) + '\n\n' + self.reliability
