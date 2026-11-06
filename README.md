# PTD Coach — dossier source et futur dépôt applicatif

**Statut : cadrage versionné (v0.1 du dépôt), aucun logiciel métier encore développé.**  
**Date de référence : 6 novembre 2026.**  
**Pilote envisagé : Chimie ParisTech – PSL, PTD 2027.**

PTD Coach vise le **développement individuel des compétences de management de projet** à partir d'un **projet réel mené en équipe**, avec deux accompagnements complémentaires : un coach IA individuel et un coach IA collectif, supervisés par des encadrants humains. La coordination générale garde une vision transversale, sans accès aux conversations privées.

Ce dépôt est fait pour être repris par **n'importe quel développeur ou assistant IA**. Les décisions et leur justification figurent dans des fichiers plutôt que dans les historiques de conversation.

## Commencer ici

1. Lire [`docs/PROJECT_STATUS.md`](docs/PROJECT_STATUS.md) : ce qui existe et la prochaine tâche.
2. Lire [`AGENTS.md`](AGENTS.md) : règles de contribution, notamment pour les IA.
3. Lire [`docs/PRODUCT_SPEC.md`](docs/PRODUCT_SPEC.md), [`docs/PEDAGOGY.md`](docs/PEDAGOGY.md) et [`docs/DECISIONS.md`](docs/DECISIONS.md).
4. Consulter [`docs/REFERENCE_MATERIAL.md`](docs/REFERENCE_MATERIAL.md) pour les quatre documents transmis en 2026 et leurs limites.
5. Consulter [`docs/ROADMAP.md`](docs/ROADMAP.md), puis créer une branche pour toute évolution.

## Structure

- `docs/` : spécifications, architecture, données, coût, sécurité, feuilles de route, journaux de décisions.
- `docs/adr/` : choix d'architecture argumentés (ADR).
- `pedagogy/` : référentiel candidat et premiers scénarios structurés.
- `contracts/json-schemas/` : propositions de contrats neutres vis-à-vis des fournisseurs IA.
- `tests/` : stratégie et cas de recette à développer.
- `infra/` : futur environnement portable ; **pas encore installé**.
- `assets/` : manifeste des documents source ; originaux non intégrés au dépôt.

## Règles de publication

**Créer d'abord un dépôt GitHub PRIVÉ.** Ne pas ajouter de documents confidentiels, de données étudiantes, de clés API ou de secrets. Les documents institutionnels originaux ne sont pas joints volontairement ; le manifeste précise les sources à récupérer et leurs versions. Aucun choix de licence logicielle n'est présumé : droits et réutilisation doivent être clarifiés avec l'établissement.

## Prochain jalon

Décider avec la DSI du socle d'hébergement/cible, puis développer une **tranche verticale testable avec données fictives** : un étudiant fictif travaille A2 (planification) de l'objectif au débrief, avec fournisseur IA simulé puis Mistral. La qualification réglementaire du système est à examiner *avant* un pilote avec vrais étudiants.

## Historique

- **2026-11-06, bootstrap v0.1** : création du dossier, reconstruction fidèle des décisions issues du cadrage, contrats candidats, documentation de passation, sans code applicatif.
