# État du projet — à actualiser à chaque changement

Dernière mise à jour : **2026-11-06** · Version documentaire : **0.1**

## Réalisé
- Cadrage des finalités individuelles / collectives et des trois rôles pédagogiques.
- Analyse documentaire initiale du planning PTD 2027 et des grilles 2026 tuteurs / rapporteurs / clients (voir `REFERENCE_MATERIAL.md`).
- Décisions validées reconstituées dans `DECISIONS.md` ; onze compétences **candidates**.
- Première spécification du parcours individuel, de l'orchestration conversationnelle et des données.
- Initialisation d'un dépôt Git local exportable, avec premier commit.
- Publication des deux commits d'origine, sans réécriture, dans le dépôt
  [GitHub privé bdelhomme/ptd-coach](https://github.com/bdelhomme/ptd-coach), branche `main`.
- Préparation sur `chore/development-environment` d'un socle documentaire portable :
  `Makefile`, contrôleur du dépôt, dix tests et workflow GitHub Actions.
- Environnement local `.venv/` et `.env` ignorés par Git, configuration `mock`
  d'exemple ; aucun service applicatif lancé. Mode d'emploi : [DEVELOPMENT.md](DEVELOPMENT.md).
- Contrôles locaux exécutés le 2026-11-06 : `git fsck --full`, contrôle des
  32 objets de contenu historiques (formats courants de secrets/adresses),
  `make bootstrap` deux fois, `make verify` (dix tests réussis),
  `git diff --cached --check`. Aucun signal détecté dans l'historique contrôlé ;
  ce contrôle ne constitue pas un audit exhaustif.

## Non réalisé
- Aucun serveur ni application n'a été créé.
- Pas de code frontend/backend, pas d'API Mistral ni d'authentification, pas de base,
  pas de tests automatisés applicatifs. Les tests du dépôt ne prouvent pas l'isolation des données.
- Pas d'accord DSI/DPO ; ni de validation du référentiel par les encadrants.
- Pas d'étude contractuelle/licence/propriété achevée.

## Prochaine priorité (ticket 001)
Écrire la spécification de bout en bout du cycle individuel **A2 — Structurer et planifier un projet**, puis implémenter une tranche verticale fonctionnant en mode **simulateur** sur des données fictives, avec tests d'isolation entre étudiants.

## Après ticket 001
- Contrat et adaptateur Mistral, journal de tokens, budget.
- Coach collectif, validation des synthèses et console tuteur.
- Préparation des revues, calendrier 2027, coordination.
- Analyse DPO/DSI et pilote limité.

## Comment reprendre
Lire `README.md` et `AGENTS.md`. Vérifier les décisions ouvertes ; ne pas inférer des arbitrages depuis le code ou des conversations anciennes.

## Passation — préparation du dépôt
- **Objectif / références** : dépôt privé, historique conservé, environnement de
  contribution vérifiable ; D-010, D-011, D-018 et ADR-0001.
- **Fichiers** : `Makefile`, `scripts/check_repository.py`,
  `tests/test_repository_checks.py`, `.github/workflows/repository-checks.yml`,
  `docs/DEVELOPMENT.md`, ce fichier, `README.md`, `tests/README.md`, `infra/README.md`.
- **Décisions / hypothèses** : outillage documentaire uniquement ; D-015 reste
  proposée. Aucun changement du référentiel, des scénarios ou des principes validés.
- **Limites / suite** : valider la pile avec la DSI puis traiter le ticket 001 ;
  appliquer les critères de recette applicatifs avant toute démonstration réelle.
