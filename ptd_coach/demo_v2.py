"""Fictional engineering missions. Fixtures are offered for explicit loading."""

from .workbench import SPEC_FIELDS


PROJECTS_V2 = {
    "team_demo_01": {
        "title": "Étudier un service de reprise",
        "sponsor": "Fabricant des Rives · fictif",
        "brief": "Évaluer les conditions d’un pilote de reprise d’emballages auprès de petits ateliers. "
                 "La mission produit une recommandation argumentée et rend visibles les limites du terrain.",
        "weeks": (
            ("Demande ouverte", "« Est-ce qu’un service de reprise trouverait son public ? » Clarifier la décision et le périmètre."),
            ("Protocole et terrain", "Deux réseaux peuvent relayer l’étude. Leur couverture est inconnue."),
            ("Accès retardé", "Un relais ne transmettra pas les invitations à la date prévue."),
            ("Changement demandé", "Le commanditaire envisage une comparaison avec un second secteur. L’accord n’est pas établi."),
            ("Résultats exploratoires", "Le groupe de répondants volontaires comporte peu d’ateliers ruraux."),
            ("Restitution", "Préparer une recommandation conditionnelle, ses preuves et ses limites."),
            ("Retour d’expérience", "Identifier ce que l’équipe réutiliserait dans une autre enquête."),
        ),
    },
    "team_demo_02": {
        "title": "Évaluer une solution de veille technique",
        "sponsor": "Bureau Horizon R&D · fictif",
        "brief": "Comparer des solutions de transmission d’alertes techniques. Étudier besoins, sources, "
                 "compatibilité et faisabilité avant toute recommandation de pilote.",
        "weeks": (
            ("Demande ouverte", "« Moderniser la veille » ne précise ni le processus ni la décision à prendre."),
            ("Délimitation du périmètre", "L’équipe précise quand les alertes sont lues et dans quel environnement."),
            ("Qualité des sources", "Deux fournisseurs publient des performances calculées sur des périmètres différents."),
            ("Expertise indisponible", "Le créneau de l’expert fictif est décalé. L’équipe compare des vérifications de remplacement."),
            ("Faisabilité", "Une option prometteuse ne répond pas encore à une contrainte d’intégration."),
            ("Arbitrage", "Une variation des pondérations inverse l’ordre de deux options."),
            ("Revue commanditaire", "Présenter un essai réversible et les conditions nécessaires pour aller plus loin."),
            ("Retour d’expérience", "Distinguer décision, hypothèse technique et résultat effectivement démontré."),
        ),
    },
}


def task(id, name, start, duration, *predecessors):
    return {"id": id, "name": name, "start": start, "duration": duration,
            "predecessors": list(predecessors)}


def specification(**fields):
    return {"sections": {key: fields.get(key, "") for key in SPEC_FIELDS}, "reference": None}


MARKET_BASELINE = [
    task("brief", "Reformuler la demande", "2026-10-01", 7),
    task("protocole", "Prétester le protocole", "2026-10-08", 7, "brief"),
    task("recrutement", "Recruter les ateliers", "2026-10-15", 7, "protocole"),
    task("entretiens", "Réaliser les entretiens", "2026-10-22", 7, "recrutement"),
    task("analyse", "Analyser les entretiens", "2026-10-29", 7, "entretiens"),
    task("restitution", "Restituer au commanditaire", "2026-11-05", 0, "analyse"),
]

TECH_PLAN = [
    task("usage", "Qualifier les usages", "2026-10-08", 7),
    task("sources", "Vérifier les sources", "2026-10-15", 14, "usage"),
    task("expert", "Consulter l’expert", "2026-10-22", 7, "usage"),
    task("options", "Comparer les options", "2026-10-29", 14, "sources", "expert"),
    task("pilote", "Examiner la faisabilité d’un pilote", "2026-11-12", 14, "options"),
    task("revue", "Présenter l’arbitrage", "2026-11-26", 0, "pilote"),
]


DEMOS = {
    "team_demo_01": {
        "excerpt": "Notre étude prouve que deux ateliers sur trois adopteront le service. "
                   "Sur douze réponses volontaires via deux réseaux, huit citent la simplicité de dépôt. "
                   "Aucun atelier rural n’a répondu. Nous recommandons un déploiement national.",
        "calendar": {"start": "2026-10-01", "end": "2027-01-28",
                     "sessions": "Créneau de travail jeudi matin. Deux entretiens et une restitution à convenir."},
        "gantt": {"tasks": [
            *MARKET_BASELINE[:2],
            task("recrutement", "Recruter les ateliers", "2026-10-15", 11, "protocole"),
            task("entretiens", "Réaliser les entretiens", "2026-10-26", 7, "recrutement"),
            task("analyse", "Analyser les entretiens", "2026-11-02", 7, "entretiens"),
            task("restitution", "Restituer au commanditaire", "2026-11-09", 0, "analyse"),
        ], "baseline": {"tasks": MARKET_BASELINE}},
        "specification": specification(
            context="Le Fabricant des Rives envisage un service de reprise pour de petits ateliers.",
            need="Éclairer la décision de tester un pilote local.",
            scope="Explorer les usages et les obstacles dans une région test.",
            exclusions="Déploiement national et évaluation d’un prix de marché.",
            stakeholders="Commanditaire, réseaux relais, ateliers et équipe d’étude.",
            deliverables="Protocole, synthèse exploratoire et note de recommandation conditionnelle.",
            verification="Relier les recommandations à des observations et documenter les profils absents.",
            assumptions="Les deux réseaux couvrent des usages différents. À vérifier.",
            questions="Qui peut autoriser la mise en relation ? Quelles régions sont dans le périmètre ?",
        ),
    },
    "team_demo_02": {
        "excerpt": "La plateforme A est objectivement la meilleure : notre matrice lui attribue 3,8/5. "
                   "Nous avons privilégié l’intégration sans consulter les équipes concernées. "
                   "La compatibilité avec l’environnement isolé est supposée. Nous préconisons un déploiement direct.",
        "calendar": {"start": "2026-10-08", "end": "2027-02-04",
                     "sessions": "Créneau jeudi matin. Revue des contraintes puis examen d’un essai avec le commanditaire."},
        "gantt": {"tasks": TECH_PLAN, "baseline": None},
        "specification": specification(
            context="Le Bureau Horizon R&D reçoit des alertes techniques via plusieurs sources.",
            need="Retrouver les alertes utiles avant une revue, avec une responsabilité de lecture explicite.",
            scope="Usages, cartographie des sources et comparaison d’options en environnement fictif.",
            exclusions="Déploiement sur les systèmes opérationnels.",
            stakeholders="Service R&D, permanence, équipe d’intégration et commanditaire.",
            deliverables="Cartographie des usages, tableau de comparaison et recommandation avec limites.",
            assumptions="La compatibilité des options avec un environnement isolé reste inconnue.",
            questions="Quelle preuve serait suffisante pour autoriser un essai ?",
        ),
        "decision-matrix": {
            "criteria": [{"name": "Intégration", "weight": 60}, {"name": "Couverture", "weight": 40}],
            "options": [
                {"name": "Option A", "scores": [{"score": 5, "reason": "Essai fictif simplifié"},
                                                {"score": 2, "reason": "Deux sources couvertes sur le périmètre test"}]},
                {"name": "Option B", "scores": [{"score": 2, "reason": "Adaptation nécessaire"},
                                                {"score": 5, "reason": "Cinq sources couvertes sur le périmètre test"}]},
            ],
        },
    },
}
