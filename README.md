# PTD Coach — dossier source et futur dépôt applicatif

**Statut : premier coach conversationnel Mistral local ; A2 simulé conservé.**
**Date de référence : 9 novembre 2026.**
**Pilote envisagé : Chimie ParisTech – PSL, PTD 2027.**

PTD Coach vise le **développement individuel des compétences de management de projet** à partir d'un **projet réel mené en équipe**, avec deux accompagnements complémentaires : un coach IA individuel et un coach IA collectif, supervisés par des encadrants humains. La coordination générale garde une vision transversale, sans accès aux conversations privées.

Ce dépôt est fait pour être repris par **n'importe quel développeur ou assistant IA**. Les décisions et leur justification figurent dans des fichiers plutôt que dans les historiques de conversation.

## Revue pédagogique publique

Le dépôt est désormais public. Le corpus fictif V0.7 est consultable dans
[le dossier de revue](pedagogy/evaluations/mistral-small-v07/README.md) :
12 scénarios, 26 réponses exactes v1.2, grilles vierges et anciens passages.
Cette publication autorisée (D-028) n'ajoute aucune donnée étudiante réelle
et ne modifie pas le coach. La revue indépendante précède toute nouvelle phase.

## Commencer ici

### Essayer une vraie conversation

Voir [le guide Mac](docs/TRY_CONVERSATION_COACH.md) : `make bootstrap`, renseigner
`MISTRAL_API_KEY` dans `.env` ignoré, puis `make run`. Ouvrir
**http://127.0.0.1:8765/coach** et choisir un compte étudiant fictif.
Le modèle initial est `mistral-small-latest`, configurable avec `MISTRAL_MODEL`.
Conserver `AI_PROVIDER=mock` pour A2 ; le dialogue indépendant utilise
`CHAT_PROVIDER=mistral` (ou `mock` hors réseau).

La conversation peut expliquer, aider à préparer une action et examiner une
expérience sans parcours imposé. Elle utilise R01–R03 (brouillons), affiche les
tokens API et distingue privé et collectif par permissions backend. Les identités
restent fictives et librement sélectionnables : aucune donnée réelle.
Lire [le rapport de recette](docs/CONVERSATION_COACH_REPORT.md), les limites
et [le contrat versionné](docs/CONVERSATION_API_V1.md). Les tests n'établissent
pas une validation scientifique ou institutionnelle du coaching.

Les lots V0.6/V0.7 restent proposés pour relecture ; leur
[inventaire d'intégration](docs/INTEGRATION_V06_V07.md) conserve la provenance.
D-026 lance l'étape 2 initialement différée par D-025 ; A2 et le candidat V0.3
restent préservés.

### Cadrage conservé

Le porteur confirme l'accompagnement sans faire à la place, la place de ressources
et l'intérêt d'aider l'étudiant à se positionner pour choisir où travailler.
Les fiches, descripteurs et modalités restent à discuter ; les onze compétences
demeurent candidates. Lire [le cadre de coaching](docs/COACHING_FRAMEWORK.md),
[le journal des réflexions](docs/REFLECTION_LOG.md) et [le ticket 003](docs/tickets/003-coaching-design.md).
Le dernier retour demande une vue globale appuyée sur des ouvrages et travaux
avant le détail d'A2 : voir [la recherche préparatoire](docs/PROJECT_MANAGEMENT_FOUNDATIONS.md).
Le corpus et son adaptation au PTD restent à discuter.
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

**Consigne de création historique : dépôt initialement privé.** La visibilité
actuelle publique et la publication du corpus fictif sont consignées par D-028. Ne pas ajouter de documents confidentiels, de données étudiantes, de clés API ou de secrets. Les documents institutionnels originaux ne sont pas joints volontairement ; le manifeste précise les sources à récupérer et leurs versions. Aucun choix de licence logicielle n'est présumé : droits et réutilisation doivent être clarifiés avec l'établissement.

## Prochain jalon

Évaluer les réponses avec la grille humaine V0.7, discuter les limites observées
et faire relire les ressources. La présence d'une API et les tests techniques
ne constituent pas une preuve d'apprentissage. L'avis DSI/DPO, la validation
pédagogique et l'authentification institutionnelle restent nécessaires avant
un pilote avec de vraies données.

## Historique

- **2026-11-06, bootstrap v0.1** : création du dossier, reconstruction fidèle des décisions issues du cadrage, contrats candidats, documentation de passation, sans code applicatif.
- **2026-11-06, prototype A2 local** : parcours individuel persistant, simulateur,
  partage explicite et révocation, export personnel et tests de confidentialité ;
  architecture technique provisoire selon ADR-0005.
- **2026-11-06, évolution du cadrage** : priorité aux fiches de coaching,
  à l'aide sans substitution, aux ressources et au positionnement formatif ;
  journal de réflexion et consigne de mémoire continue dans le dépôt.

- **2026-11-09, intégration V0.6 puis V0.7** : spécifications proposées,
  ressources, cas synthétiques et outils de recette hors application ; D-025,
  candidat V0.3 inchangé, développement Mistral différé.

- **2026-11-09, étape 2 autorisée (D-026)** : service conversationnel séparé,
  API Mistral configurable, espaces privé/collectif, mesure des tokens, UI locale,
  tests de frontières et recette réelle V0.7 ; données fictives uniquement.
