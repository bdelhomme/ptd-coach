# État du projet — à actualiser à chaque changement

Dernière mise à jour : **2026-11-06** · Version documentaire : **0.2 — prototype local**

## Dernière évolution — lisibilité de la séance

Suite au retour utilisateur « je me mets à la place d'un étudiant, je suis perdu »,
l'interface distingue trois moments : s'entraîner ici, tester une action avec son
équipe, puis revenir faire le point. Entrée guidée par un cas concret, plan
séparé de l'exercice, pause explicite et partage facultatif sont décrits dans
le [ticket 002](tickets/002-student-journey-clarity.md).

Fichiers modifiés : `web/app.js`, `web/style.css`, `web/index.html` et documentation.
Les 34 tests existants passent ; recette navigateur du parcours simplifié effectuée.
La branche `feat/student-journey-clarity` est locale, sans nouvelle CI distante.
Les décisions pédagogiques, scénarios versionnés d'origine, contrats et permissions
backend sont conservés. L'entrée guidée crée une nouvelle séance fictive ; elle
ne supprime aucune séance enregistrée. La compréhension réelle par un étudiant
reste à vérifier avec un essai utilisateur.

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
- CI GitHub Actions réussie sur la branche de préparation :
  [exécution 42235620971](https://github.com/bdelhomme/ptd-coach/actions/runs/42235620971).
  Intégration suivie dans la [pull request 1](https://github.com/bdelhomme/ptd-coach/pull/1).
- Prototype A2 exécutable sur `http://127.0.0.1:8765` via `make run` : sélection
  d'objectif/cas, explication, exercice, plan d'action, expérience déclarée,
  débrief, bilan privé et clôture sans niveau attribué.
- Persistance SQLite locale, sessions fictives, requêtes filtrées par propriétaire,
  fournisseur simulé avec contrats validés, transitions explicites, contrôle de
  version et commandes idempotentes.
- Preuve sélectionnée séparément, partage confirmé vers le tuteur fictif de
  l'équipe, révocation, audit de métadonnées et export limité au propriétaire.
- 34 tests locaux réussis : dix documentaires, dix-sept domaine/contrats et sept
  HTTP. Parcours complet et partage/révocation vérifiés dans le navigateur.
  Architecture provisoire : [ADR-0005](adr/0005-local-a2-prototype.md) ;
  contrat et recette : [ticket 001](tickets/001-a2-local.md).

## Non réalisé
- Pas de serveur déployé, d'API Mistral, de SSO ou d'authentification institutionnelle,
  ni de PostgreSQL/conteneurs. Le serveur et la base du prototype sont locaux.
- Pas de coach collectif, synthèses validées, budget réel ou restauration
  institutionnelle. Tests e2e du navigateur non automatisés.
- La branche `feat/a2-local-prototype` est locale : les contrôles du nouveau
  prototype n'ont pas encore été exécutés par GitHub Actions.
- Pas d'accord DSI/DPO ; ni de validation du référentiel par les encadrants.
- Pas d'étude contractuelle/licence/propriété achevée.
- Protection serveur de `main` non activée : l'API GitHub répond HTTP 403 et
  exige GitHub Pro pour ce dépôt privé. Le dépôt reste privé. La CI s'exécute,
  mais n'est pas imposée par une règle de protection ; les contributions doivent
  continuer à passer par une branche et une pull request.

## Prochaine priorité
Faire relire par un encadrant les trois cas et leurs feedbacks **PROPOSÉS** du
prototype A2, puis arbitrer la pile/infrastructure avec la DSI. Le périmètre local
du ticket 001 est réalisé ; il ne constitue pas un pilote institutionnel validé.

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

## Passation — premier prototype A2
- **Objectif / exigences** : F-01/F-03/F-04/F-09/F-12/F-13/F-14 ;
  D-001/D-009/D-010/D-012. Parcours individuel privé, sans notation automatique.
- **Fichiers** : `ptd_coach/`, `web/`, `tests/test_a2_service.py`,
  `tests/test_a2_http.py`, `pedagogy/scenarios/A2-demo-cases-v0.1.json`,
  `docs/tickets/001-a2-local.md`, ADR-0005, Makefile et documentation actualisée.
- **Tests** : `make test` (34 réussis), parcours navigateur complet, partage et
  révocation, rechargement et redémarrage du serveur. Aucun test distant annoncé.
- **Décisions / hypothèses** : D-019 et ADR-0005 documentent un choix technique
  provisoire ; D-015 reste proposée. Décisions pédagogiques validées, référentiel
  candidat et scénario A2 d'origine conservés ; trois cas de démo ajoutés comme propositions.
- **Limites / suite** : les comptes librement sélectionnables ne protègent pas
  contre une personne utilisant une autre identité fictive. Démonstration locale
  exclusivement ; relecture pédagogique, avis DSI et authentification réelle à préparer.
