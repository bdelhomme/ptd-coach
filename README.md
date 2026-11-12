# PTD Coach

PTD Coach vise le **développement individuel des compétences de management de projet** à partir d'un **projet réel mené en équipe**, avec deux accompagnements complémentaires : un coach IA individuel et un coach IA collectif, supervisés par des encadrants humains. La coordination générale garde une vision transversale, sans accès aux conversations privées.

Le travail porte sur l’ensemble du PTD, du démarrage au bilan. Les 29 dialogues
fictifs de l’audit abordent notamment le cahier des charges, la coordination
d’équipe, la motivation et la restitution. Ils mettent en jeu les onze
compétences candidates et servent à repérer les défauts du coach.
[Audit global du PTD — 12 novembre 2026](docs/AUDIT_GLOBAL_PTD_2026_11_12.md).

- **À la racine `/`**, l’application intégrée réunit le coach, la bibliothèque,
  l’atelier de projet et le point d’étape. Suivez une équipe fictive sur six
  jeudis et essayez les vues étudiant et tuteur. [Guide de démonstration](docs/DEMO_PTD_INTEGREE.md).
- **Sur `/historique-a2`**, le premier prototype simulé illustre A2, la
  compétence candidate « Structurer et planifier le projet ».
- **Sur `/coach` avec `--coach-historique`**, l’interface historique permet
  de comparer V0.7 et V0.8. [Modes de comparaison](docs/TRY_CONVERSATION_COACH.md).

## Essais et versions

> [Cadrage de fiabilité expérimental](docs/CADRAGE_FIABILITE_V01.md) : essais comparatifs et limites, sans validation pédagogique.

> Expérimentation [Mistral Large 4](docs/MISTRAL_LARGE4.md) : cause de l’échec, lancement local, comparaison et limites pédagogiques.

> [Bibliothèque expérimentale de méthodes](docs/BIBLIOTHEQUE_METHODES.md), consultable localement sans API. Les fiches sont soumises à relecture.

**Campagne transversale D-031** · 24 cas fictifs couvrant les onze compétences
candidates. Le rapport donne accès à la cartographie, aux ressources proposées,
à la grille et aux résultats comparatifs. [Rapport de campagne](docs/CAMPAGNE_TRANSVERSALE.md).

**Candidate 2 en revue — D-030** : [rapport et commandes](docs/V08_C2_REPORT.md),
[relecture conceptuelle et sources](docs/V08_C2_CONCEPT_REVIEW.md).
V0.7/c1 et leurs corpus sont conservés ; c1 n’est pas pédagogiquement validée.
C2 est un contexte distinct pour comparaison, pas une nouvelle fonctionnalité
ni un remplacement silencieux du coach actuellement affiché dans `/coach`.

**V0.8 expérimentale — tranche D-029** : contexte pédagogique adaptatif séparé,
choix V0.7/V0.8 dans `/coach`, 24 cas fictifs répartis développement/réserve.
[Essayer sur Mac](docs/TRY_CONVERSATION_COACH.md) ·
[Arbitrages et résultats](docs/V08_IMPLEMENTATION.md) ·
[Contrat pédagogique](docs/PTD_V08_CONTRAT_PEDAGOGIQUE.md).
Le candidat V0.3 et la revue V0.7 sont conservés. Aucune efficacité pédagogique
n’est déduite des tests techniques.

**Pilote envisagé : Chimie ParisTech – PSL, PTD 2027.**

Ce dépôt est fait pour être repris par **n'importe quel développeur ou assistant IA**. Les décisions et leur justification figurent dans des fichiers plutôt que dans les historiques de conversation.

## Revue pédagogique publique

Le dépôt est désormais public. Le corpus fictif V0.7 est consultable dans
[le dossier de revue](pedagogy/evaluations/mistral-small-v07/README.md) :
12 scénarios, 26 réponses exactes v1.2, grilles vierges et anciens passages.
Cette publication autorisée (D-028) n'ajoute aucune donnée étudiante réelle
et ne modifie pas le coach. Le corpus a été préparé pour une revue indépendante.

## Commencer ici

### Essayer le PTD intégré

Après `make bootstrap`, lancez `CHAT_PROVIDER=mock make run` et ouvrez
[PTD Coach](http://127.0.0.1:8765/) avec un compte étudiant fictif. Pour une
conversation Mistral, renseignez `MISTRAL_API_KEY` dans `.env` ignoré et lancez
`CHAT_PROVIDER=mistral make run`. Le modèle est configurable avec
`MISTRAL_MODEL` et A2 conserve `AI_PROVIDER=mock`.

La conversation libre s’appuie sur les méthodes expérimentales et les repères
confirmés du périmètre du fil. Le tuteur consulte uniquement les repères
collectifs confirmés et partagés avec son compte. Les identités sont fictives
et librement sélectionnables. [Recette et limites](docs/RAPPORT_PTD_INTEGRE.md) ·
[Préparation d’un pilote](docs/CHECKLIST_PILOTE_PTD.md).

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
Le cadrage s’appuie sur des références de management de projet et sur les
situations rencontrées tout au long du PTD. Voir
[la recherche préparatoire](docs/PROJECT_MANAGEMENT_FOUNDATIONS.md).
Le corpus et son adaptation au PTD restent à discuter.
Le prototype ci-dessous permet des essais techniques ; ses exercices ne sont
pas approuvés par le seul fait qu'ils sont exécutables.

### Essayer la démonstration historique A2

Depuis le répertoire du dépôt :

```sh
make bootstrap
make verify
make run
```

Ouvrir [la démo A2](http://127.0.0.1:8765/historique-a2), puis choisir un compte fictif. Le parcours A2
va de l'objectif au bilan privé, avec sélection d'une preuve à partager au tuteur.
Le serveur écoute uniquement sur ce Mac et le parcours A2 utilise le simulateur local.
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
- `ptd_coach/` : coach conversationnel, démonstration A2, fournisseurs IA et persistance locale.
- `web/` : interface locale sans dépendance externe.
- `tests/` : contrôles du dépôt, tests du domaine et tests HTTP sur données synthétiques.
- `infra/` : documentation ; environnement institutionnel et conteneurs à construire.
- `scripts/`, `Makefile`, `.github/workflows/` : outillage documentaire et contrôles automatisés ; voir [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md).
- `assets/` : manifeste des documents source ; originaux non intégrés au dépôt.

## Règles de publication

**Consigne de création historique : dépôt initialement privé.** La visibilité
actuelle publique et la publication du corpus fictif sont consignées par D-028. Ne pas ajouter de documents confidentiels, de données étudiantes, de clés API ou de secrets. Les documents institutionnels originaux ne sont pas joints volontairement ; le manifeste précise les sources à récupérer et leurs versions. Aucun choix de licence logicielle n'est présumé : droits et réutilisation doivent être clarifiés avec l'établissement.

## Prochain jalon

Le plan proposé après l’audit donne la priorité à la fiabilité des réponses,
à l’entrée dans le parcours étudiant et à l’accompagnement des difficultés
d’équipe. La relecture humaine des réponses et des ressources reste à mener.
[Plan de développement proposé](docs/PLAN_DEVELOPPEMENT_POST_AUDIT.md).
L'avis DSI/DPO, la validation pédagogique et l'authentification institutionnelle
restent nécessaires avant un pilote avec de vraies données.

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
