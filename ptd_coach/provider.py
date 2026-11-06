"""Deterministic, offline provider; no autonomous writes or grading."""

import json
from typing import Protocol


class AIProvider(Protocol):
    def complete(self, request: dict) -> str:
        ...


class MockProvider:
    def complete(self, request):
        activity = request["activity"]
        case = json.loads(request["authorized_context"][0]["text"])
        messages = {
            "explain": (
                "Une tâche décrit une action ; un jalon marque un résultat à vérifier. "
                "Une dépendance signifie qu'une action attend une autre action ou une validation. "
                "Pour planifier, explicitez aussi qui valide et à quel moment.\n\n"
                "Dans ce cas : " + case["focus"]
            ),
            "prepare_action": (
                "Votre plan est enregistré. Lors de l'occasion prévue, observez ce qui se passe "
                "avant de conclure. Vous pourrez ensuite rapporter les faits, votre interprétation "
                "et une leçon pour la suite."
            ),
            "debrief": (
                "Ces éléments sont votre récit d'une expérience, non une observation directe "
                "du coach. Relisez les faits séparément de votre interprétation.\n\n"
                "Quelle leçon souhaitez-vous conserver dans votre bilan personnel ?"
            ),
            "weekly_review": (
                "Votre bilan reste dans votre espace individuel. Un parcours terminé "
                "n'atteste pas d'un niveau de compétence. Si vous le souhaitez, choisissez "
                "un texte précis à partager avec votre tuteur."
            ),
        }
        if activity == "practice":
            if request["student_message"]:
                excerpt = request["student_message"][:180]
                if len(request["student_message"]) > 180:
                    excerpt += "…"
                message = (
                    "Vous avez écrit : « " + excerpt + " ».\n\n"
                    "Point à examiner : " + case["focus"] + " "
                    "Cette dépendance détermine quelles tâches peuvent avancer sans reprendre "
                    "plus tard un travail fondé sur une hypothèse.\n\n"
                    "Quel jalon et quel responsable de validation rendraient votre proposition vérifiable ?"
                )
            else:
                message = case["context"] + "\n\n" + case["question"]
        else:
            message = messages.get(activity, "Votre action explicite a été enregistrée.")
        return json.dumps({
            "message": message,
            "pedagogical_intent": activity,
            "suggested_next_state": None,
            "proposed_updates": [],
            "needs_human_support": False,
        }, ensure_ascii=False)
