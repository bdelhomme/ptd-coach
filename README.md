# PTD Coach — dossier source et futur dépôt applicatif

**Statut : premier prototype local A2, données fictives et coach simulé ; non destiné à un pilote réel.**
**Date de référence : 6 novembre 2026.**  
**Pilote envisagé : Chimie ParisTech – PSL, PTD 2027.**

PTD Coach vise le **développement individuel des compétences de management de projet** à partir d'un **projet réel mené en équipe**, avec deux accompagnements complémentaires : un coach IA individuel et un coach IA collectif, supervisés par des encadrants humains. La coordination générale garde une vision transversale, sans accès aux conversations privées.

Ce dépôt est fait pour être repris par **n'importe quel développeur ou assistant IA**. Les décisions et leur justification figurent dans des fichiers plutôt que dans les historiques de conversation.

## Commencer ici

### Essayer le prototype local

Depuis le répertoire du dépôt :

```sh
make bootstrap
make verify
make run
```

Ouvrir **http://127.0.0.1:8765**, puis choisir un compte fictif. Le parcours A2
va de l'objectif au bilan privé, avec sélection d'une preuve à partager au tuteur.
Le serveur écoute uniquement sur ce Mac ; aucun appel IA externe n'est effectué.
Les comptes sont librement sélectionnables pour vérifier les rôles : n'utiliser
que des données inventées. Voir [DEVELOPMENT.md](docs/DEVELOPMENT.md) et
[le ticket 001](docs/tickets/001-a2-local.md).

### Reprendre le développement

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
- `ptd_coach/` : domaine A2, persistance locale, fournisseur simulé et serveur de démonstration.
- `web/` : interface locale sans dépendance externe.
- `tests/` : contrôles du dépôt, tests du domaine et tests HTTP sur données synthétiques.
- `infra/` : documentation ; environnement institutionnel et conteneurs à construire.
- `scripts/`, `Makefile`, `.github/workflows/` : outillage documentaire et contrôles automatisés ; voir [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md).
- `assets/` : manifeste des documents source ; originaux non intégrés au dépôt.

## Règles de publication

**Créer d'abord un dépôt GitHub PRIVÉ.** Ne pas ajouter de documents confidentiels, de données étudiantes, de clés API ou de secrets. Les documents institutionnels originaux ne sont pas joints volontairement ; le manifeste précise les sources à récupérer et leurs versions. Aucun choix de licence logicielle n'est présumé : droits et réutilisation doivent être clarifiés avec l'établissement.

## Prochain jalon

Faire relire le parcours et les feedbacks du prototype A2 par un encadrant,
puis arbitrer avec la DSI la pile et l'infrastructure cible avant migration et
adaptation Mistral. La qualification réglementaire du système est à examiner
*avant* un pilote avec vrais étudiants.

## Historique

- **2026-11-06, bootstrap v0.1** : création du dossier, reconstruction fidèle des décisions issues du cadrage, contrats candidats, documentation de passation, sans code applicatif.
- **2026-11-06, prototype A2 local** : parcours individuel persistant, simulateur,
  partage explicite et révocation, export personnel et tests de confidentialité ;
  architecture technique provisoire selon ADR-0005.
