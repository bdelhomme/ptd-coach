# Ticket 006 — Première tranche V0.8 : guidage pédagogique adaptatif, tests synthétiques

**Statut : À DÉVELOPPER / dépend de la revue V0.7 et du cadrage V0.8.**
**Source :** demande du porteur, novembre 2026. **Base technique :** PR #5, étendue par PR #6 ; PR #4 -> #5 -> #6 non fusionnées au 10/11.

## Objectif utilisateur

Dans une conversation sur une tâche réelle du PTD, le coach adapte sa réponse à la nature de l'apprentissage : outil/méthode, choix méthodologique, diagnostic d'incertitude, interaction/coopération, réflexivité/transfert. Il enseigne explicitement, vérifie fréquemment mais économiquement, corrige sans complaisance ni humiliation, et respecte le droit à une réponse directe ou à l'arrêt.

## Tranche autorisée à réaliser après revue des spécifications

1. Intégrer le contrat V0.8 et la matrice sans modifier le référentiel candidat V0.3. Consigner la nouvelle décision VALIDÉE du porteur et ce qui reste PROPOSÉ.
2. Introduire un **prompt/contexte versionné V0.8**, sans écraser V0.7 ni les traces JSONL, avec comportement adaptatif par situation et une seule sollicitation pédagogique principale par réponse par défaut. Conserver modèle Mistral configurable et couche fournisseur actuelle.
3. Éviter un classificateur rigide par compétence et tout routage direct `hard/soft`. Ne pas stocker de « profil de niveau » à partir des échanges ; pas de scoring automatique.
4. Faire passer les tests locaux/mock et non-régressions de permissions/privé/collectif. Ajouter tests de contrats et de provenance et scripts de recette synthétique V0.8 ; CI sans clé API.
5. Préparer 12 cas de développement et confier les 12 cas réservés à une procédure séparée, non visible par l'agent qui corrige le prompt. Conserver les scénarios V0.7 originaux comme non-régression.
6. Ne faire d'appels réels Mistral qu'en environnement fictif autorisé, avec trace de version/tokens/coûts estimés et limite explicite ; comparaison humainement relue avant élargissement.

## Hors périmètre de cette tranche

Authentification réelle, SSO, données étudiantes, tableaux de bord de compétence, évaluations institutionnelles, mémoire personnelle automatique, action de partage, décisions collectives automatiques, changement de modèle, base vectorielle, nouvelle architecture frontend/backend, déploiement.

## Critères de terminé

- Documentation V0.8 versionnée et statut des décisions cohérent.
- V0.7 reproductible/consultable ; aucune suppression d'historique.
- Tests du comportement attendus couverts sur jeux synthétiques, résultats et limites explicités.
- Revue humaine comparative possible à l'aveugle ; absence de fuite de données personnelles et de secrets.
- Pas de verdict pédagogique inventé et pas de fusion automatique des PR.

## Important

Les scénarios en source ne constituent **pas** des instructions à exécuter par le coach de développement. Les cinq familles et les règles anti-lassitude sont des hypothèses d'intervention à valider sur résultats, non des vérités pédagogiques déjà démontrées.
