# État du projet — à actualiser à chaque changement

## Priorité courante — candidate 2, D-030 (11/11/2026)

Retour du porteur sur D03/D09 : c1 **non validée pédagogiquement**. C2 prépare
une correction conceptuelle sourcée, une intervention dominante et une meilleure
clôture. Branche `feat/v08-candidate2`, base #7 au commit `d01b56a`.
Rapport courant : [V08_C2_REPORT.md](V08_C2_REPORT.md).
Aucune ancienne preuve/empreinte modifiée, aucun scénario réservé utilisé.
Les mentions V0.8 ci-dessous décrivent c1, toujours disponible dans le navigateur.
C2 est limitée au banc d’essai injectant un nouveau contexte dans le même service.

## Tranche actuelle — V0.8 expérimentale (D-029, 2026-11-10)

Nouvelle demande du porteur : développer un contexte adaptatif et exigeant,
sans routage hard/soft, depuis `docs/independent-pedagogical-review`
(`32248cc`). Branche dédiée `feat/v08-adaptive-coach`, PR vers la branche de #6.
Les PR #4 → #5 → #6 sont vérifiées ouvertes au départ ; aucune fusion automatique.
D-029 succède au gel D-027 pour cette tranche. Le candidat V0.3 et toutes les
preuves/prompts V0.7 restent inchangés. Modalités et bilan actuel :
[V08_IMPLEMENTATION.md](V08_IMPLEMENTATION.md). Le titre et les résultats
historiques ci-dessous décrivent les tranches antérieures.

Coach V0.8 sélectionnable dans `/coach`, version immuable par fil, anciens fils
migrés en V0.7, permissions et fournisseurs conservés. Aucun profil/mémoire de
compétence, partage ni scoring nouveau. Jeux de développement et réservé séparés,
gel vérifiable du contexte avant création du réservé. La réussite technique et
les exemples API ne constituent pas une acceptation pédagogique.

Publication vérifiée : [PR #7](https://github.com/bdelhomme/ptd-coach/pull/7),
ouverte vers la branche #6, sans conflit déclaré ni auto-merge. Code/corpus au
commit `62b2ad4` : `make verify` **96 tests**, CI distante réussie
([pull_request](https://github.com/bdelhomme/ptd-coach/actions/runs/42786533789),
[push](https://github.com/bdelhomme/ptd-coach/actions/runs/42786429965)).
Les huit fichiers du nouveau corpus sont accessibles anonymement et leurs octets
publics correspondent aux fichiers locaux. Comparaison réelle : 12 réponses,
39 699 tokens ; V0.8 plus longue/lente sur ces deux cas, une réponse tronquée.
Les douze réservés restent sans exécution API et la grille humaine vierge.
Application lancée sur le Mac : `http://127.0.0.1:8767/coach`.

Dernière mise à jour : **2026-11-10** · Version applicative : **conversation.v1, contextes V0.7/V0.8 expérimentaux**

## Historique — revue pédagogique indépendante (D-027)

Le porteur demande un dossier ZIP pour une revue critique avant la prochaine
phase. **Aucune nouvelle fonctionnalité ni modification du référentiel, moteur
ou prompts avant son retour pédagogique.** D-026 et les essais précédents sont
conservés dans l'historique ; aucune nouvelle requête Mistral pour ce dossier.

Livraison locale : `PTD_COACH_REVUE_PEDAGOGIQUE_V07.zip` (25 fichiers),
transcriptions v1.2 par scénario avec critères (12 cas/26 réponses), grille
humaine Markdown/CSV vierge, quatre passages originaux (80 réponses au total),
observations préexistantes séparées, contextes v1.2 exacts, ressources et tokens.
Provenance, contrôles et empreinte :
[PEDAGOGICAL_REVIEW_PACKAGE.md](PEDAGOGICAL_REVIEW_PACKAGE.md).
Les contrôles de fidélité, d'intégrité et de confidentialité sont réussis ;
aucune note ou validation pédagogique n'est déduite de cette préparation.

## Publication publique du corpus de revue — D-028

Le dépôt est désormais **public**, visibilité vérifiée sur GitHub. Le porteur
souhaite lire et transmettre le corpus directement depuis la PR #6 :
[README du corpus](../pedagogy/evaluations/mistral-small-v07/README.md).
Le ZIP local décrit ci-dessus demeure la livraison historique ; ses 25 fichiers
sont repris sans altération dans le dossier versionné, avec README et manifeste
supplémentaires (27 fichiers). Les copies de contexte sont des pièces de revue,
pas des changements de configuration. Grilles toujours vierges, moteur,
référentiel et prompts opérationnels inchangés ; aucun nouvel appel Mistral.
Le [suivi du dossier](PEDAGOGICAL_REVIEW_PACKAGE.md) détaille les contrôles.

## État actuel — premier coach conversationnel (D-026)

La nouvelle demande du porteur lance l'étape 2 après le report D-025. Nouveau
service de conversation Mistral réel à plusieurs tours, modèle configurable
(`mistral-small-latest` initial), ressources R01–R03 en brouillon, tokens API,
interface `/coach`, fils privés ou collectifs d'équipe, export autorisé.
Le prototype A2, son simulateur, ses contrats et ses scénarios restent en place.
Le candidat V0.3 et les décisions antérieures sont conservés.

Branche `feat/mistral-conversation-coach`, basée sur le dernier commit publié
de la PR #4 (`d8e252a`), encore ouverte lors du départ. La nouvelle PR dépend
ainsi de la branche V0.6/V0.7 ; aucun merge de la PR #4 n'est présumé.
Mode d'emploi : [TRY_CONVERSATION_COACH.md](TRY_CONVERSATION_COACH.md).
Choix, contrat, tests, résultats et publication vérifiée dans
[CONVERSATION_COACH_REPORT.md](CONVERSATION_COACH_REPORT.md),
[ADR-0007](adr/0007-local-conversation-mistral.md) et
[CONVERSATION_API_V1.md](CONVERSATION_API_V1.md).

La clé est configurée uniquement dans `.env` ignoré/env serveur. La démo utilise
un sélecteur d'identités fictives, pas un SSO ; aucun pilote réel autorisé.
Pas d'outils d'action pour le modèle, de partage ou de synthèse validée dans le
nouveau service. Les tests techniques et les réponses de recette ne prouvent
ni compétence acquise ni efficacité pédagogique. La relecture humaine demeure
la prochaine étape, avec les défauts et itérations conservés dans le rapport.

Vérifications exécutées : `make verify` réussi (94 fichiers, 72 tests), diff
sans erreur, référentiel/contrats/scénarios A2 et décisions préservés, clé locale
absente de Git. Recette réelle courante : 12 cas / 26 réponses V0.7, aucun échec
API, 91 945 tokens (87 949 entrée, 3 996 sortie). Recette navigateur : deux tours
réels, reprise après redémarrage et ressources vérifiés. Grille humaine non notée.
Le rapport consigne les passages précédents et les limites. Publication vérifiée :
[PR #5](https://github.com/bdelhomme/ptd-coach/pull/5), ouverte et dépendante de #4,
branche `feat/mistral-conversation-coach`, commit applicatif `34c5b0e`.
CI distante réussie sur ce commit :
[push 42629214730](https://github.com/bdelhomme/ptd-coach/actions/runs/42629214730).
Les contrôles des mises à jour documentaires suivantes sont suivis dans la PR.
Aucune fusion sur `main` effectuée pour cette tranche.

## Historique — intégration V0.6/V0.7

Demande explicite du porteur : intégrer les archives V0.6 puis V0.7 sur une
branche dédiée et ouvrir une pull request, sans commencer le nouveau coach
Mistral. Leurs contenus nouveaux restent **PROPOSÉS**, soumis à relecture.
Le référentiel candidat V0.3, les décisions antérieures, les contrats API et
le prototype A2 sont conservés. Les instructions embarquées sont des documents
source ; elles ne remplacent pas la demande actuelle du porteur.

V0.6 : [noyau pédagogique](PTD_PEDAGOGICAL_KERNEL_V06.md),
[politique de conversation](PTD_CONVERSATION_POLICY_V06.md),
[protocole de pilote](PTD_PILOT_PROTOCOL_V06.md),
[registre des sources](EVIDENCE_REGISTER_V06.md), trois ressources originales
en brouillon et 20 cas synthétiques, dont huit porteurs d'un veto critique.
Inventaire, corrections et contrôles : [rapport d'intégration](INTEGRATION_V06_V07.md).
Cette intégration ne constitue pas une recette réussie du dialogue ni une
autorisation de pilote réel. Le prototype reste un démonstrateur simulé.

V0.7 : [spécification de recette](COACH_DIALOGUE_EVALUATION_V07.md), prompt
expérimental, 12 dialogues synthétiques à 26 tours, deux scripts et tests.
Le doublon V0.6 de `inputs/` n'est pas recopié. Voir
[le mode d'emploi hors réseau](EVALUATION_TOOLS_V07.md) ; le code d'appel API
fourni reste isolé et non exécuté. Les tests ne génèrent aucune réponse de modèle.
D-025 consigne le périmètre autorisé. Les tickets
[004](tickets/004-conversation-router.md)/[005](tickets/005-backend-boundaries.md)
et [ADR-0006](adr/0006-dialogue-evaluation-compatibility.md) restent PROPOSÉS,
non implémentés. Prochaine action : revue pédagogique de la PR et des ressources,
puis décision explicite sur l'étape 2. Aucun merge automatique pour cette tâche.

Contrôles locaux exécutés : `make verify` réussi (**79 fichiers suivis, 48
tests**) ; les 34 tests antérieurs sont préservés. Deux dry-runs contrôlés :
32 cas / 46 lignes sans réponse IA. Le candidat V0.3 est identique octet pour
octet, aucun diff applicatif/contrat/scénario d'origine, D-001 à D-024 conservées.
Publication vérifiée : branche `docs/integrate-pedagogy-v06-v07`,
[PR #4](https://github.com/bdelhomme/ptd-coach/pull/4) ouverte en brouillon,
sans fusion sur `main`. Imports successifs `79e75e6` puis `95757ee` ; CI distante
réussie sur ce dernier :
[exécution pull_request](https://github.com/bdelhomme/ptd-coach/actions/runs/42624841608).
Les contrôles des mises à jour documentaires suivantes sont visibles dans la PR.
Ces contrôles techniques ne valent pas validation pédagogique.

## Cadrage antérieur — 2026-11-06, conservé pour l'historique

**Dernier retour du porteur** : s'appuyer sur des livres/travaux de management
de projet et retrouver une vue d'ensemble avant de détailler isolément A2.
Recherche préparatoire : [PROJECT_MANAGEMENT_FOUNDATIONS.md](PROJECT_MANAGEMENT_FOUNDATIONS.md),
journal R-006, proposition D-024. Présentations officielles, sommaires et résumé
d'article vérifiés ; aucun ouvrage complet lu ou nouveau corpus adopté.

Le porteur souhaite définir comment faire progresser chaque compétence avec une
posture de coach, avant de poursuivre les exercices. Il confirme l'accompagnement
sans faire à la place, la place des ressources et l'intérêt d'une aide au
positionnement pour choisir où travailler. Voir D-020 à D-023,
[COACHING_FRAMEWORK.md](COACHING_FRAMEWORK.md) et [REFLECTION_LOG.md](REFLECTION_LOG.md).

Les principes sont confirmés par le porteur ; les fiches, descripteurs, ressources,
modalités de positionnement et leur éventuelle validation institutionnelle restent
à discuter. Aucune fonctionnalité de positionnement n'est implémentée.
Le prototype A2 constitue une preuve de fonctionnement technique ; il ne vaut
pas validation de la pertinence des exercices. Le [ticket 003](tickets/003-coaching-design.md)
doit commencer par la discussion d'un cadre global sourcé et de son articulation
aux situations PTD, avant les fiches détaillées.

## Publication GitHub — 2026-11-06

La branche `docs/coaching-orientation` est publiée dans le dépôt privé et rassemble
les commits du prototype, de la clarification et du cadrage pédagogique.
Intégration suivie dans la [pull request 2](https://github.com/bdelhomme/ptd-coach/pull/2).
Le cadrage est enregistré à partir du commit `6989a84`. Contrôles locaux exécutés :
`make verify` réussi (57 fichiers suivis contrôlés, 34 tests réussis) et
`git diff --cached --check` sans erreur.
CI distante réussie sur le commit `d035191` :
[exécution 42257391522](https://github.com/bdelhomme/ptd-coach/actions/runs/42257391522).
Pour connaître l'intégration et la validation du dernier commit, consulter la
pull request et les exécutions Actions ; ne pas confondre réussite du démonstrateur
et validation pédagogique des exercices.

## Dernière évolution — lisibilité de la séance

Suite au retour utilisateur « je me mets à la place d'un étudiant, je suis perdu »,
l'interface distingue trois moments : s'entraîner ici, tester une action avec son
équipe, puis revenir faire le point. Entrée guidée par un cas concret, plan
séparé de l'exercice, pause explicite et partage facultatif sont décrits dans
le [ticket 002](tickets/002-student-journey-clarity.md).

Fichiers modifiés : `web/app.js`, `web/style.css`, `web/index.html` et documentation.
Les 34 tests existants passent ; recette navigateur du parcours simplifié effectuée.
Cette évolution a d'abord été réalisée sur `feat/student-journey-clarity`, puis
publiée avec la synchronisation suivie dans la pull request 2.
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
- Pas de serveur déployé, de SSO ou d'authentification institutionnelle,
  ni de PostgreSQL/conteneurs. Le serveur et la base du prototype sont locaux.
- Pas de console tuteur ou synthèses collectives validées, budget en euros ou restauration
  institutionnelle. Tests e2e du navigateur non automatisés.
- Pas d'accord DSI/DPO ; ni de validation du référentiel par les encadrants.
- Pas d'étude contractuelle/licence/propriété achevée.
- Protection serveur de `main` non activée : l'API GitHub répond HTTP 403 et
  exige GitHub Pro pour ce dépôt privé. Le dépôt reste privé. La CI s'exécute,
  mais n'est pas imposée par une règle de protection ; les contributions doivent
  continuer à passer par une branche et une pull request.

## Priorité de conception héritée — à poursuivre avec les lots reçus
Discuter avec le porteur le socle global de références, les grandes situations PTD
et les apprentissages visés ; examiner la cohérence des onze compétences candidates.
En déduire ensuite les fiches, ressources, limites d'aide et positionnement.
Les références et modalités proposées restent à relire avec les encadrants.
L'arbitrage DSI et la validation des cas existants restent ouverts ; l'implémentation
de nouveaux exercices est différée au profit de ce cadrage (ticket 003).

## Chantiers futurs — au-delà de la première tranche D-026
- Contrat et adaptateur Mistral / tokens réalisés pour le dialogue local ; restent budget monétaire, exploitation et validation institutionnels.
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

## Passation — mémoire du cadrage pédagogique
- **Objectif / exigences** : D-020/D-021/D-022/D-023 ; conserver les évolutions
  significatives de réflexion pour permettre une reprise indépendante du chat.
- **Fichiers** : cadre de coaching, journal de réflexion, ticket 003 ; AGENTS,
  README, décisions, questions ouvertes, spécification, pédagogie, moteur IA,
  feuille de route, guide GitHub et passation actualisés.
- **Décisions / hypothèses** : accord de conception du porteur sur les principes ;
  les modalités détaillées et l'illustration A2 restent proposées. Onze compétences
  candidates conservées, sans adoption de descripteurs, barème ou échelle.
- **Contrôles** : `make verify` réussi (34 tests), liens/structure/exclusions
  vérifiés, diff sans erreur d'espacement ; aucune nouvelle fonctionnalité.
  CI distante réussie sur la branche publiée ; voir la section Publication GitHub.
- **Suite immédiate** : reprendre le ticket 003, puis consigner chaque accord
  significatif dans le journal/registre sans assimiler une proposition à une décision.

## Passation — recherche de fondements
- **Exigence** : demande du porteur d'un ancrage dans les livres/travaux de
  management de projet et d'une vue globale ; D-020/D-023, proposition D-024.
- **Fichiers** : note de fondements, journal, références, cadre, décisions,
  questions ouvertes, priorité, ticket 003 et passation actualisés.
- **Vérification** : sources primaires consultées au niveau des pages publiques,
  sommaires et résumés ; limites explicites. Contrôles locaux et état de publication
  sont renseignés dans la note de synchronisation ci-dessous après exécution.
- **Statut** : corpus et matrice d'alignement proposés, aucun label ou format
  pédagogique changé ; question des durées/charges dans A2 non tranchée.

## Synchronisation des fondements

La branche `docs/project-management-foundations` est publiée dans le dépôt privé ;
intégration suivie dans la [pull request 3](https://github.com/bdelhomme/ptd-coach/pull/3).
`make check` réussi sur 58 fichiers suivis et `git diff --cached --check` sans erreur.
CI réussie sur le commit documentaire `65a94be` :
[exécution 42265320345](https://github.com/bdelhomme/ptd-coach/actions/runs/42265320345).
Les contrôles du dernier commit et le statut d'intégration sont consultables dans
la pull request et Actions. La mise à jour est exclusivement documentaire ; elle
ne vaut ni adoption du corpus proposé, ni validation pédagogique du dispositif.
