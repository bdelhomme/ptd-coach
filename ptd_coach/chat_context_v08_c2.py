"""Separate c2 bundle, injectable into the existing service without changing c1."""

import hashlib

from .chat_context import ChatContext, ROOT
from .chat_context_v08 import ChatContextV08


class ChatContextV08C2(ChatContextV08):
    # Existing schema/engine uses v08; the precise candidate is in prompt_version.
    # Dedicated evaluation databases prevent any mixing with browser c1 threads.
    coach_version = "v08"
    version = "conversation-v08-experimental-c2"

    def __init__(self, root=ROOT):
        original = ChatContext(root)
        self._selector = ChatContextV08(root)
        self.resources = [r for r in original.resources if r["id"] != "R03"]
        content = (root / "pedagogy/resources/R04-concepts-projet-c2.md").read_text(encoding="utf-8")
        self.resources.append({"id": "R04", "title": content.splitlines()[0].lstrip("# "),
                               "status": "experimental", "content": content})
        self.prompt = (root / "pedagogy/prompts/COACH_SYSTEM_V08_C2.md").read_text(encoding="utf-8")
        self.digest = hashlib.sha256((self.system("individual", self.resources) +
                                      self.system("collective", self.resources)).encode()).hexdigest()

    def select_resources(self, message, history):
        # Reuse c1's selection, with a versioned replacement of its project fiche.
        selected = self._selector.select_resources(message, history)
        ids = {"R04" if r["id"] == "R03" else r["id"] for r in selected}
        return [r for r in self.resources if r["id"] in ids]

    def system(self, scope, resources=()):
        if scope not in ("individual", "collective"):
            raise ValueError("Invalid scope")
        place = ("Un étudiant dans son espace individuel privé."
                 if scope == "individual" else
                 "Équipe de sept sur écran collectif ; discussion orale non captée, aucun privé fourni.")
        return (self.prompt + "\n\nEspace autorisé : " + place + "\n\n" +
                "\n\n".join("<ressource id='" + r["id"] + "' statut='" + r["status"] + "'>\n" +
                            r["content"] + "\n</ressource>" for r in resources))
