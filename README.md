# PTD Coach — dossier source et futur dépôt applicatif

**Statut : prototype local A2 expérimental ; priorité actuelle au cadrage du coaching par compétence.**
**Date de référence : 6 novembre 2026.**  
**Pilote envisagé : Chimie ParisTech – PSL, PTD 2027.**

PTD Coach vise le **développement individuel des compétences de management de projet** à partir d'un **projet réel mené en équipe**, avec deux accompagnements complémentaires : un coach IA individuel et un coach IA collectif, supervisés par des encadrants humains. La coordination générale garde une vision transversale, sans accès aux conversations privées.

Ce dépôt est fait pour être repris par **n'importe quel développeur ou assistant IA**. Les décisions et leur justification figurent dans des fichiers plutôt que dans les historiques de conversation.

## Commencer ici

### Priorité actuelle : définir le coaching avant de poursuivre les exercices

Le porteur confirme l'accompagnement sans faire à la place, la place de ressources
et l'intérêt d'aider l'étudiant à se positionner pour choisir où travailler.
Les fiches, descripteurs et modalités restent à discuter ; les onze compétences
demeurent candidates. Lire [le cadre de coaching](docs/COACHING_FRAMEWORK.md),
[le journal des réflexions](docs/REFLECTION_LOG.md) et [le ticket 003](docs/tickets/003-coaching-design.md).
Le prototype ci-dessous permet des essais techniques ; ses exercices ne sont
pas approuvés par le seul fait qu'ils sont exécutables.

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

Co-concevoir avec le porteur une première fiche de coaching A2, puis les autres
compétences candidates ; préciser les ressources, les limites d'aide et le
positionnement formatif privé. Faire relire les propositions par les encadrants.
L'arbitrage DSI, l'adaptation Mistral et la qualification réglementaire restent
nécessaires avant un pilote avec vrais étudiants.

## Historique

- **2026-11-06, bootstrap v0.1** : création du dossier, reconstruction fidèle des décisions issues du cadrage, contrats candidats, documentation de passation, sans code applicatif.
- **2026-11-06, prototype A2 local** : parcours individuel persistant, simulateur,
  partage explicite et révocation, export personnel et tests de confidentialité ;
  architecture technique provisoire selon ADR-0005.
- **2026-11-06, évolution du cadrage** : priorité aux fiches de coaching,
  à l'aide sans substitution, aux ressources et au positionnement formatif ;
  journal de réflexion et consigne de mémoire continue dans le dépôt.
