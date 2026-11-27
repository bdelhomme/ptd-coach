"""Opt-in fictional student trial with an explicit mission and coaching stance."""

from .demo_v2 import DEMOS, PROJECTS_V2
from .library_v2 import SemesterWorkshopContext
from .project import ProjectService


RESEARCH_MISSION = {
    "title": "Faire évoluer la culture d’un centre de recherche",
    "sponsor": "Centre de recherche Atlas · fictif",
    "brief": "Quels leviers pour faire évoluer la culture d’un centre de recherche vers la conception "
             "de solutions centrées client ? Une équipe de sept étudiants mène l’étude pour le commanditaire. "
             "Les pratiques du centre, les personnes à consulter et les livrables précis restent à établir.",
    "weeks": (
        ("Prise en main", "Le sujet vient d’être donné. Préparer ce que l’équipe veut clarifier au premier rendez-vous."),
        ("Cadrage de l’étude", "Délimiter les situations de travail à étudier et les résultats attendus."),
        ("Préparation de l’enquête", "Choisir comment recueillir les points de vue et quels cas pourraient manquer."),
        ("Analyse", "Distinguer observations, explications possibles et idées de changement."),
        ("Discussion des options", "Préparer une discussion avec le commanditaire à partir des preuves réunies."),
        ("Restitution", "Présenter les recommandations, leurs conditions et les limites de l’étude."),
    ),
}

TRIAL_PROJECTS = {**PROJECTS_V2, "team_demo_01": RESEARCH_MISSION}
TRIAL_EXAMPLES = {**DEMOS, "team_demo_01": {
    "excerpt": "Deux personnes nous ont décrit comment elles recueillent les retours clients. "
               "Cela suffit pour conclure que tous les projets du centre utilisent la même démarche.",
}}


class StudentTrialProject(ProjectService):
    def __init__(self, database):
        super().__init__(database, TRIAL_PROJECTS)

    def context(self, actor, scope):
        context = super().context(actor, scope)
        team = self.identity(actor, write=True)["team"]
        week = context["project"]["current_week"]
        context["project"]["stage"], context["project"]["situation"] = self.fixtures[team]["weeks"][week - 1]
        return context


class StudentTrialContext(SemesterWorkshopContext):
    @property
    def version(self):
        return super().version if self.review.get() else "conversation-ptd-v2-student-trial-0.1"

    def system(self, scope, resources=()):
        system = super().system(scope, resources)
        if self.review.get():
            return system
        return system + """

Pour cet essai, l'interlocuteur est un étudiant en PTD ou son équipe.
L'équipe étudie la demande du commanditaire de l'extérieur. Une citation de
la demande, le mot « nous » ou « notre valeur ajoutée » ne change pas ce rôle.
Distingue l'équipe étudiante, le commanditaire et les utilisateurs qu'elle
étudie. Appuie-toi sur la mission et sa situation ; précise une éventuelle
divergence avec le message au lieu d'inventer une nouvelle mission.

Lire le titre d'un sujet ne suffit pas à comprendre le besoin de coaching.
Si l'étudiant dit comprendre le sujet sans poser de question sur sa
démarche, commence par une question ciblée sur ce qu'il veut faire ou
éclaircir pour sa prochaine étape. Laisse-lui le travail d'enquête,
l'interprétation et le choix des recommandations. Si une réponse a devancé
ce travail, reconnais-le et reviens à une observation, un choix ou un test
que l'étudiant peut mener lui-même. Donne une explication de méthode ou un
exemple court si la demande le justifie, en distinguant un exemple des faits.
"""
