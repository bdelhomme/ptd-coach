# Premier coach conversationnel — compte rendu du 2026-11-09

## Périmètre et base

Demande D-026 : conversation réelle à plusieurs tours avec Mistral, modèle
initial `mistral-small-latest` configurable, ressources, réflexivité, action,
tokens, séparation privé/collectif et interface locale, A2 conservé.
Branche `feat/mistral-conversation-coach`, base GitHub actualisée `d8e252a`
de la PR #4 encore ouverte au départ. Cette contribution est une PR dépendante
de cette branche ; aucun merge de #4 ou dans `main` n'est présumé.

## Fichiers et comportement

- `ptd_coach/chat_provider.py` : fournisseurs Mistral réel et mock, réponses
  texte et usage ; endpoint fixe, clé serveur, erreurs nettoyées, pas de retry.
- `chat_context.py` : prompt V0.7 et R01–R03 inchangés, complément applicatif
  versionné, empreinte du contexte complet individuel + collectif.
- `chat_config.py`, `chat_service.py`, `chat_schema.sql` : configuration,
  scopes filtrés par SQL, persistance séparée d'A2, ledger des appels et clés
  idempotentes. Aucun outil de partage/écriture métier pour le modèle.
- `server.py`, `__main__.py`, `.env.example` : routes indépendantes et
  initialisation ; A2 garde son fournisseur simulé. `web/index.html` ajoute
  seulement un lien vers le nouveau coach, sans changer le parcours A2.
- `web/coach.html`, `coach.js`, `coach.css` : compte fictif, nouveau fil privé
  ou d'équipe, messages, ressources, tokens, reprise et export du fil autorisé.
  Texte rendu avec nœuds DOM sûrs, sans HTML ni liens actifs émis par le modèle.
- `scripts/run_conversation_eval.py` : batterie V0.6/V0.7 via le contexte et
  le service applicatifs ; critères de jugement réservés au fichier de sortie.
- `tests/test_chat.py`, `tests/test_chat_http.py` : tests indépendants des API
  payantes. Les 48 tests précédents sont conservés.
- Guide Mac, contrat `conversation.v1`, ADR-0007, AGENTS, décisions/journal,
  état/passation, spécifications et tickets 004/005 mis à jour.

Les décisions D-001 à D-025 restent historiques. D-026 autorise le développement,
sans validation institutionnelle des propositions V0.6/V0.7. Candidat V0.3,
scénarios A2, ancien schéma SQL et contrats JSON conservés sans migration.

## Recettes API réellement exécutées

Clé fournie par le porteur dans `.env` ignoré ; jamais affichée. Appels vers
Mistral, données synthétiques exclusivement, température 0,2 et sortie max 700.
Le modèle demandé et la valeur renvoyée sont `mistral-small-latest` ; l'API
n'a pas résolu cet alias en identifiant de révision immuable.

| Passage | Réponses | Tokens entrée | Sortie | Total |
|---|---:|---:|---:|---:|
| Smoke M01, v1 | 2 | 6 149 | 108 | 6 257 |
| V0.7 complète, v1 | 26 | 81 375 | 3 485 | 84 860 |
| V0.7 complète, v1.1 | 26 | 85 021 | 2 983 | 88 004 |
| V0.7 complète, **v1.2 courante** | **26** | **87 949** | **3 996** | **91 945** |

Chaque passage est distinct, sans écrasement des erreurs antérieures. Les
26 réponses finales couvrent 12 cas, sans erreur API ni usage manquant.
Ces nombres ne comprennent pas les échanges interactifs de recette navigateur.
Ce sont des compteurs d'usage API, pas des notes pédagogiques ou des euros.

Contexte final : `conversation-v1.2+v07-proposed`, empreinte
`c321c72fa966b1d13a0e29f1ac8fcd120daafe3859f02b75477a05682322487a`.
SHA-256 du JSONL final :
`3e64f913ae685074e52b4be03f14932b334e345b99d14fb05e88d8ae57e85754`.
Les transcriptions fictives des quatre passages et la grille CSV humaine
sont livrées localement dans le dossier de sortie `recette-conversation/`,
hors du dépôt applicatif. Aucun secret dans ces artefacts.

## Observations qualitatives — ne remplace pas une évaluation humaine

- Le premier passage fournit des ressources sans quiz, respecte l'arrêt et
  refuse des demandes d'accès privé ou d'enregistrement. Il révèle aussi des
  erreurs : contexte d'ancienne réponse inventé (M09), confusion d'une demande
  d'appropriation avec une restitution (M10), annulation de partage affirmée
  sans outil (M11). Ces erreurs sont conservées dans la trace initiale.
- v1.1 précise les capacités et la provenance ; v1.2 ajoute une information
  exacte sur la conservation du fil, après des affirmations de non-conservation
  observées en v1.1. Le prompt source V0.7 reste inchangé : c'est le complément
  applicatif qui évolue et entre désormais dans l'empreinte complète.
- Le passage final M11 répond qu'aucun partage n'est effectué et ne prétend
  plus l'annuler. M09 refuse un numéro de norme invérifiable. M10 reste parfois
  orienté vers une restitution plutôt qu'une vérification de compréhension.
  Des réponses sont longues et certaines références restent approximatives.
  La grille humaine doit examiner ces limites, l'autonomie et les formulations
  de confidentialité ; aucune réussite globale de la recette n'est revendiquée.

Une grille de **26 lignes non notées** est préparée avec l'outil V0.7. Son
résumé donne `REVIEW_INCOMPLETE` tant que le porteur/les lecteurs n'ont pas rempli
les cinq dimensions et le veto. Les compteurs et les tests techniques ne sont
pas une preuve d'apprentissage, de conformité juridique ou de sécurité SSO.

## Tests locaux et navigateur

`make verify` réussi : **94 fichiers suivis et 72 tests**, dont les 48
antérieurs et 24 nouveaux. `git diff --cached --check` sans erreur. Contrôle
complémentaire : clé locale exacte absente de tous les fichiers suivis, `.env`
ignoré, candidat/scénarios/contrats A2 et décisions D-001 à D-025 préservés.
Les nouveaux tests couvrent privé entre comptes/équipes/rôles,
collectif limité à l'équipe, contexte sans autres fils ni critères QA,
export filtré, replay et conflit de clé, concurrence/version, échecs et appel
incertain après redémarrage, plafonds et tokens inconnus, API/HTTP/configuration.
La CI n'utilise aucune clé et ne contacte pas Mistral.

Deux tours réels ont déjà été vérifiés dans le navigateur : difficulté de
coordination puis adaptation à un point d'équipe de cinq minutes, sans parcours
A2 imposé. Consommation de cette première conversation : 6 685 tokens. L'interface finale a été rechargée après redémarrage : reconnexion fictive,
reprise des quatre messages existants, affichage des trois ressources et
rendu sûr des emphases vérifiés. Capture livrée hors Git :
`apercu-coach-mistral.jpg`. Le serveur de travail utilise le port 8766 ; A2 reste accessible
sur la racine du même serveur.

## Limites et suite

Démo Mac/loopback, identités librement sélectionnables, aucune donnée réelle.
Le mot privé exprime une règle backend par identité, pas une protection contre
une personne utilisant un autre compte de démo. Pas de synthèse validée, partage
de ce nouveau fil, SSO, effacement utilisateur ou déploiement institutionnel.
Les fils ne passent jamais d'un scope à l'autre. Le modèle ne reçoit aucun outil
d'action ; des affirmations textuelles erronées restent possibles.

Les limites locales d'appels/tokens sont bornées et configurables, sans garantie
de plafond financier du compte Mistral. Les appels interrompus peuvent être
facturés sans usage connu ; ils ne sont pas relancés automatiquement. La
rétention contractuelle du fournisseur et les droits/licences institutionnels
restent à examiner avec l'établissement avant un pilote réel.

Suite immédiate : essayer la conversation, remplir la grille V0.7, faire relire
R01–R03 et discuter les défauts observés avant d'élargir le périmètre.

## Publication vérifiée

Branche publiée, commit applicatif `34c5b0e` ;
[PR #5](https://github.com/bdelhomme/ptd-coach/pull/5) ouverte vers
`docs/integrate-pedagogy-v06-v07`, dépendante de #4. Aucun merge automatique.
CI push réussie sur le commit applicatif :
[exécution 42629214730](https://github.com/bdelhomme/ptd-coach/actions/runs/42629214730).
Les résultats des derniers commits documentaires sont suivis dans la PR.
