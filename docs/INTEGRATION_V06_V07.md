# Intégration pédagogique V0.6 puis V0.7 — 2026-11-09

**Statut : branche publiée, PR de revue ouverte en brouillon ; propositions non adoptées.**
Demande du porteur : intégrer les contenus et outils fournis, préserver
l'historique et le candidat V0.3, vérifier et ouvrir une PR sans démarrer le
nouveau coach Mistral. Références : D-001/D-009/D-010/D-012/D-020 à D-024.

Base synchronisée : `efb3962c8488b9b064de0c6dd4279d9b111ab758` sur `main`.
Branche : `docs/integrate-pedagogy-v06-v07`. Deux commits d'import successifs
permettent de relire V0.6 (`79e75e6`) avant V0.7 (`95757ee`) ; aucun historique
réécrit. Une mise à jour documentaire finale consigne les contrôles et la PR.

## V0.6 — huit fichiers intégrés

- [Noyau pédagogique](PTD_PEDAGOGICAL_KERNEL_V06.md).
- [Politique de conversation](PTD_CONVERSATION_POLICY_V06.md).
- [Protocole de pilote](PTD_PILOT_PROTOCOL_V06.md).
- [Registre critique des sources](EVIDENCE_REGISTER_V06.md).
- [R01 : coordination](../pedagogy/resources/R01-coordination-et-engagements.md).
- [R02 : débrief](../pedagogy/resources/R02-debrief-factuel.md).
- [R03 : cadrage et planification](../pedagogy/resources/R03-cadrage-et-planification.md).
- [Vingt cas de recette](../pedagogy/qa/COACH_ACCEPTANCE_CASES_V06.json).

Le noyau propose une théorie d'action et une correspondance des onze codes.
E1–E4 sont une grille analytique de coopération, jamais quatre nouveaux codes.
Le dialogue souple et les sept intentions proposés complètent le cadrage du
ticket 003 ; ils ne remplacent ni la machine A2 ni les contrats API.

## V0.7 — six fichiers intégrés après V0.6

- [Spécification d'évaluation des dialogues](COACH_DIALOGUE_EVALUATION_V07.md).
- [Prompt expérimental](../pedagogy/prompts/COACH_SYSTEM_DRAFT_V07.md).
- [Douze dialogues, 26 tours](../pedagogy/qa/COACH_MULTI_TURN_CASES_V07.json).
- [Exécuteur expérimental](../scripts/run_coach_eval_v07.py).
- [Préparation et résumé des grilles humaines](../scripts/review_coach_eval_v07.py).
- [Tests de l'outillage](../tests/test_eval_v07.py).

Le script d'appel fourni est importé **à l'identique**, sans raccordement au
prototype. Prompt et suites JSON sont également conservés à l'identique.
Le chemin API fourni n'a pas été exécuté et ne constitue pas un développement
du nouveau coach Mistral. Le périmètre D-025 est limité à cette intégration.

## Suivi et passation

- [Manifeste des archives et empreintes source](../assets/PEDAGOGY_IMPORTS_V06_V07.json)
  : les 19 fichiers source sont recensés, dont 14 intégrés, quatre briefs de
  livraison analysés sans copie et un doublon dédupliqué. Les ZIP restent hors Git.
- [Mode d'emploi hors réseau](EVALUATION_TOOLS_V07.md) et
  [tests de préservation/intégration](../tests/test_pedagogy_integration.py).
- [ADR-0006 proposé](adr/0006-dialogue-evaluation-compatibility.md) : aucune
  migration de contrats ou de machine à états réalisée.
- [Ticket 004](tickets/004-conversation-router.md), futur dialogue souple, et
  [ticket 005](tickets/005-backend-boundaries.md), contrôles d'isolation :
  proposés et non démarrés, réservés à une étape ultérieure.
- AGENTS, README, état, passation, registre/journal, feuille de route, ticket 003,
  questions ouvertes, spécifications produit/pédagogie/IA, cadre de coaching,
  architecture, sources, développement et guide des tests actualisés.

## Écarts et arbitrages d'intégration

- Aucun chemin de contenu V0.6 n'existait dans la base ; pas de conflit Git.
- Les README de livraison et briefs `codex/` servent à l'analyse de provenance,
  sans être recopiés comme consignes actives. La demande utilisateur actuelle
  fait autorité, notamment le report du développement Mistral et l'ouverture
  d'une PR. Les archives ne prouvent pas de nouvelles décisions validées.
- Les mentions V0.4/V0.5 restent des déclarations du lot : ces versions n'ont
  pas été fournies. Le socle déjà présent est conservé et référencé.
- V0.6 annonçait six cas critiques ; le JSON en contient **huit**, T13–T20.
  Le protocole est corrigé, sans modifier les scénarios.
- Le noyau annonçait quatre fonctions, la politique en liste **sept** ; cette
  incohérence de comptage est corrigée sans changer la politique.
- Le DOI transmis pour Tannenbaum & Cerasoli (2013) était erroné ; il est
  corrigé dans le registre et R02 selon la
  [notice PubMed](https://pubmed.ncbi.nlm.nih.gov/23516804/) :
  `10.1177/0018720812448394`. Lecture limitée à la notice/résumé.
- Les niveaux d'accès aux sources dans le registre sont attribués aux auteurs
  du lot. Aucune lecture intégrale supplémentaire ou validation scientifique
  ne leur est substituée par l'intégration.
- La copie `inputs/COACH_ACCEPTANCE_CASES_V06.json` de V0.7 est strictement
  identique au fichier V0.6 : omise ; le test fourni utilise désormais le chemin
  canonique `pedagogy/qa/COACH_ACCEPTANCE_CASES_V06.json`.
- La spécification V0.7 reçoit une note d'intégration datée : ses mentions
  d'absence sur `main` décrivent la préparation du lot, pas un nouvel état constaté.
- Deux corrections limitées dans le script de revue : refuser une entrée vide
  lors de la création d'une grille et compter un veto déjà signalé même si
  les autres dimensions ne sont pas encore remplies. Une grille incomplète
  ne passe jamais le seuil. Six tests supplémentaires vérifient ces défauts,
  l'absence d'appel en dry-run, les historiques, les critères hors contexte,
  la sélection et les erreurs simulées. Aucun jugement humain remplacé.

Il n'y a pas eu de conflit de fusion Git. Les écarts ci-dessus sont des
incohérences documentaires ou d'outillage résolues explicitement. Les ressources
et seuils restent soumis à relecture ; l'efficacité et la sécurité institutionnelle
ne sont pas établies. Le résumé CSV ne prouve pas la couverture complète d'une
suite : comparer les IDs/tours avant de conclure. Les limites de reproductibilité
du banc fourni sont décrites dans son mode d'emploi, à traiter à l'étape 2.

## Préservation

`pedagogy/competencies/candidate-v0.3.json` reste identique à la base : SHA-256
`56558fec5b3005019a65b0e600b53c6c908ea157d50358e852dd5667411851d8`.
Les décisions D-001 à D-024 sont conservées ; aucune proposition du lot n'est
promue VALIDÉE. Prototype A2, schémas, scénarios d'origine et règles d'accès
restent inchangés. Aucune donnée réelle ni clé ajoutée.

## Vérification et publication

Après V0.6 : `make verify` réussi (67 fichiers suivis, 34 tests antérieurs) et
`git diff --cached --check` sans erreur. L'import documentaire ne
constitue pas un essai de modèle, un jugement pédagogique humain, une preuve
d'apprentissage ou une recette de sécurité backend.

Après V0.7 : `make verify` réussi (**79 fichiers suivis, 48 tests** : 34
antérieurs, douze de l'outillage et deux de préservation/intégration).
Les six tests fournis passaient aussi avant les compléments. Dry-runs des
deux suites, V0.7 avec R01–R03 : **32 cas / 46 lignes JSONL**, IDs/tours uniques,
`response: null`, `provider: dry-run`, `status: not_called` vérifiés sur chaque
ligne. Les fichiers de sortie sont locaux, hors du dépôt.

Comparaison automatisée avec la base : aucun diff du candidat V0.3, des scénarios
d'origine, des schémas, du code applicatif ou des trois fichiers de tests
antérieurs ; chaque ligne de décision D-001 à D-024 est conservée.

Le contrôle d'espacement a détecté deux espaces finaux sur la date du README ;
corrigés avant publication. `make check` et `git diff --cached --check`
réussis après correction.

Publication vérifiée : [PR #4](https://github.com/bdelhomme/ptd-coach/pull/4),
ouverte en brouillon vers `main`, déclarée sans conflit par GitHub.
Sur `95757ee`, CI distante réussie sur
[pull_request](https://github.com/bdelhomme/ptd-coach/actions/runs/42624841608)
et [push](https://github.com/bdelhomme/ptd-coach/actions/runs/42624832705).
Les statuts des commits documentaires suivants sont consultables dans la PR.
Aucune fusion sur `main` réalisée pour cette tâche.
