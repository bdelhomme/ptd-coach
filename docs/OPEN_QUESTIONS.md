# Questions ouvertes — ordre de résolution

| Priorité | Question | Décideur / interlocuteurs | Bloque quoi ? |
|---|---|---|---|
| P0 | Quels droits sur le code et les contenus produits dans le cadre des fonctions à Chimie ParisTech ? Quelle licence éventuelle ? | Direction, juridique, auteur(s) | Publication/open source/transfert |
| P0 | Quelles données peuvent être utilisées et à quelles conditions ? Base légale, conservation, AIPD, qualification du système IA | DPO, établissement | Pilote avec vrais étudiants |
| P0 | Quelle est l'infrastructure cible acceptée (containers, SSO, sortie Internet, logs, backups) ? | DSI | Choix techniques définitifs |
| P0 | Quel référentiel institutionnel de compétences et quels acquis PTD ont déjà été actés ? | Responsables pédagogiques | Finalisation du référentiel |
| P0 | Quelles capacités concrètes, situations PTD, interventions du coach et limites d'aide retenir pour chaque compétence candidate ? | Porteur puis encadrants | Fiches de coaching avant nouveaux exercices, ticket 003 |
| P0 | Quels ouvrages/référentiels retenir pour une vue globale du management de projet et comment justifier l'alignement des situations PTD avec les onze compétences candidates ? | Porteur puis encadrants | Cadre d'ensemble avant détail d'A2 ; corpus préparatoire non adopté, D-024 |
| P1 | Comment organiser le positionnement formatif : ressenti, expériences disponibles, confirmation de la priorité et reprise après action ? Faut-il une échelle et laquelle ? | Porteur, encadrants ; DPO pour les données | Spécification du positionnement individuel privé ; aucune échelle arrêtée |
| P1 | Quelles ressources courtes proposer, avec quelles sources, droits, versions et relecture pédagogique ? | Porteur, encadrants, établissement pour les droits | Catalogue de ressources et aide contextualisée |
| P1 | À quels moments le coach doit-il proposer l'appui de l'encadrant humain, et selon quelle procédure ? | Porteur et encadrants | Limites d'intervention dans les fiches de coaching |
| P1 | Procédure exacte d'autorisation d'accès aux extraits ciblés du coach collectif | DPO, pédagogues, étudiants | Écran accès exceptionnel |
| P1 | Exacte articulation rapport final, dossier école 6 pages et page individuelle | Coordination PTD | Portfolios, remises |
| P1 | Quelles dates de PTD 2027 seront confirmées par la scolarité ? | Scolarité | Parcours daté |
| P1 | Quel modèle Mistral / endpoint / contrat de rétention / hébergement ? | DSI, DPO, équipe produit | Adaptateur production |
| P1 | Quel budget maximal et limites d'usage individuels ? | Coordination, direction | FinOps |
| P2 | Quelle procédure d'évaluation du pilote permet d'observer des apprentissages réels ? | Pédagogues / évaluation | Déploiement plus large |
| P2 | Quel hébergeur de démonstration ? | Porteur du prototype | Démo publique à données fictives |

## Questions de revue ajoutées le 2026-11-09

- Les encadrants approuvent-ils la théorie d'action, la grille analytique E1–E4,
  le rôle transversal de D2 et l'articulation proposée des onze codes ?
- Qui relit R01–R03, leurs sources et droits avant usage pédagogique ?
- Comment calibrer la grille de dialogue, les désaccords entre lecteurs et les
  seuils de recette proposés (0–2, 90 %, zéro veto) sans les confondre avec
  une mesure des compétences étudiantes ?
- Quel périmètre et contrat retenir pour l'étape 2 après nouvelle demande ?
  L'ADR-0006 et les tickets 004/005 restent proposés, aucun modèle choisi ni testé.

**Principe :** ne jamais résoudre une question ouverte par supposition silencieuse. Si une tranche de développement exige un arbitrage, l'expliciter dans le ticket.

## Tranche autorisée D-026

Le modèle initial de la démo est désormais `mistral-small-latest`, configurable,
et le contrat de conversation v1 est implémenté séparément d'A2. Cela ne tranche
pas le modèle ni le contrat fournisseur pour une exploitation institutionnelle.
La grille humaine V0.7 et la relecture des ressources restent à effectuer.

## Questions ouvertes V0.8 — D-029

- Le guidage supplémentaire aide-t-il l’appropriation sans rendre les réponses
  trop longues ? Le passage D03/D09 montre un risque de sur-guidage et troncature.
- Quelles dimensions/veto et règles de désaccord fixer avant le passage réservé ?
- Qui réalise la double lecture humaine et la relecture conceptuelle des exemples ?
- Qui assume la relecture, les droits et les métadonnées de R01–R03 encore brouillons ?

Le lot de comparaison est descriptif et sa grille vierge ; aucun seuil ni verdict
humain n’est déduit des tests. Voir [le bilan](V08_IMPLEMENTATION.md).
