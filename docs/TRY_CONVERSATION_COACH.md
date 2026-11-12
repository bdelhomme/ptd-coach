# Essayer le premier coach sur Mac

Ce guide concerne le mode historique. Le lancement standard ouvre
[le PTD intégré](DEMO_PTD_INTEGREE.md). Ajoutez `--coach-historique` pour
retrouver les fils et le sélecteur de versions décrits ci-dessous.

## Essai V0.8 et comparaison V0.7 — 2026-11-10

Après `make bootstrap`, conserver la clé uniquement dans `.env` ignoré,
`CHAT_PROVIDER=mistral`, `MISTRAL_MODEL=mistral-small-latest` (configurable).
Lancer `.venv/bin/python -m ptd_coach --coach-historique`, puis ouvrir `http://127.0.0.1:8765/coach`.
Si ce port héberge une ancienne démo : `.venv/bin/python -m ptd_coach --coach-historique --port 8767`,
puis `http://127.0.0.1:8767/coach`. Pour un essai sans coût :
`CHAT_PROVIDER=mock .venv/bin/python -m ptd_coach --coach-historique --port 8767` ; les réponses sont
alors fixes et ne testent pas la pédagogie de Mistral.

Choisir un compte fictif, une **version du coach**, l’espace privé ou collectif,
confirmer les données fictives puis créer le fil. V0.8 est proposée pour les
nouveaux essais ; chaque ancien fil reste V0.7. Pour comparer, créer un fil de
chaque version et saisir les mêmes messages inventés. Les versions sont affichées
sur les fils, tokens et latence sous les réponses. Exporter séparément chaque fil.
La version se choisit avant création ; elle ne se change pas au milieu d’un fil.

Protocole, scénarios, commandes de comparaison et résultats réellement exécutés :
[V08_IMPLEMENTATION.md](V08_IMPLEMENTATION.md).

**Prototype local, données fictives uniquement.** Le parcours A2 simulé reste
disponible. La nouvelle conversation à plusieurs tours utilise Mistral ; elle
n'impose ni A2, ni jeu de rôle, ni objectif ou questionnaire préalable.

## Préparer et lancer

Depuis le dossier du dépôt :

```sh
make bootstrap
make verify
.venv/bin/python -m ptd_coach --coach-historique
```

Dans le fichier `.env` local (caché dans le Finder, exclu de Git), renseigner :

```dotenv
APP_ENV=development
AI_PROVIDER=mock
CHAT_PROVIDER=mistral
MISTRAL_MODEL=mistral-small-latest
MISTRAL_API_KEY=
CHAT_MAX_TOKENS=700
CHAT_TIMEOUT_SECONDS=45
CHAT_MAX_CALLS=100
```

Mettre la clé après `MISTRAL_API_KEY=` **uniquement dans ce fichier local**,
jamais dans le navigateur, le chat, un commit ou une capture. L'environnement
du processus peut remplacer les valeurs du fichier. Redémarrer le serveur
après changement. Ne pas remplacer `AI_PROVIDER=mock` : il concerne A2.
Le mode `CHAT_PROVIDER=mock` permet aussi d'essayer l'interface hors réseau ;
il affiche explicitement une réponse fixe de simulation.

Ouvrir **http://127.0.0.1:8765/coach**. Si le port est occupé :

```sh
.venv/bin/python -m ptd_coach --coach-historique --port 8766
```

Puis **http://127.0.0.1:8766/coach**. Le serveur écoute seulement sur ce Mac.
Le prototype A2 reste à la racine du même port, avec son fournisseur simulé.

## Première conversation

1. Ouvrir le compte fictif A, B ou C.
2. Choisir un espace privé ou collectif et confirmer les données fictives.
3. Commencer une conversation, puis écrire une question ou adapter un exemple.
4. Relancer librement : « On n'a que cinq minutes jeudi ; adapte ces repères. »
5. Lire les ressources R01–R03 (brouillons), le modèle renvoyé et les tokens.
   Actualiser permet de reprendre après rechargement ; sélectionner le fil voulu.

Exemple : « Dans notre équipe fictive de sept, chacun avance de son côté.
Comment nous coordonner sans que tu décides à notre place ? »
Autres besoins : définition, échange client à préparer, désaccord à examiner,
retour sur une réunion. Les réponses soutiennent la réflexion ; elles ne sont
ni des consignes institutionnelles ni des décisions de l'équipe.

Privé A : A seul. Collectif équipe 1 : A et B. C est dans une autre équipe.
Tuteur/coordination/admin : aucun accès aux transcriptions. **Le sélecteur de
comptes n'est pas une authentification réelle** ; tout utilisateur de la démo
peut changer d'identité. Aucun contenu réel, sensible ou confidentiel.

Les fils restent dans `local-data/coach-demo.sqlite3`, séparé d'A2. L'export
porte seulement sur le fil autorisé sélectionné. Pas de partage automatique,
de synthèse validée, d'audio ou de copie du privé vers le collectif.

## Coûts, limites et erreurs

Chaque envoi Mistral transmet le prompt, les trois ressources et l'historique
de ce fil. Les tokens d'entrée répétés sont inclus dans la consommation cumulée.
Une absence de mesure est affichée, sans inventer un coût. Le modèle renvoyé
peut encore être un alias ; changer de modèle via `MISTRAL_MODEL` puis redémarrer.

Plafonds techniques : sortie 700 tokens par défaut, 24 tours/60 000 caractères
par fil, 100 réservations d'appel dans cette base par défaut, 3 appels concurrents.
Modifier les variables documentées n'altère pas le référentiel pédagogique.
`CHAT_MAX_CALLS` compte aussi les essais en erreur ; ce n'est pas une facture.

Clé absente/refusée, quota ou réseau : un message explicite remplace toute fausse
réponse. Il n'y a aucun retry automatique. Après une coupure, réessayer le même
message conserve sa clé côté page. Si le serveur s'est interrompu pendant un appel,
le fil reste en attente/incertain : vérifier avant tout nouvel essai ; la facture
peut être inconnue. Ne jamais supprimer la base pour prétendre annuler une facture.

## Recette pédagogique V0.7

Les tests automatiques ne jugent pas la pertinence d'un modèle. Pour rejouer
les cas fictifs **via le même contexte et service que l'application** :

```sh
.venv/bin/python scripts/run_conversation_eval.py --provider dry-run --output local-data/v07-dry.jsonl
.venv/bin/python scripts/run_conversation_eval.py --provider mock --output local-data/v07-mock.jsonl
.venv/bin/python scripts/run_conversation_eval.py --provider mistral --allow-billable --output local-data/v07-mistral.jsonl
.venv/bin/python scripts/review_coach_eval_v07.py sheet --responses local-data/v07-mistral.jsonl --out local-data/v07-review.csv
```

Le troisième appel est réel et consomme des tokens. Les fichiers de résultat
ne sont pas écrasés ; choisir un autre nom pour une nouvelle expérience.
Options : `--case M03`, `--model autre-modele`, `--max-cases 1`, et `--suite`
pour le fichier canonique V0.6. Le script sort en erreur si un appel échoue.
Les critères de correction restent hors du contexte envoyé au modèle.

Faire remplir le CSV par un lecteur humain, puis utiliser la commande `summary`
documentée dans [EVALUATION_TOOLS_V07.md](EVALUATION_TOOLS_V07.md). Les scores
portent sur les réponses du coach, jamais sur un étudiant. Un dry-run contient
des réponses nulles, un mock des réponses fixes : aucune réussite pédagogique
ne peut en être déduite. Une sortie JSONL réelle n'est pas une grille déjà notée.

Implémentation et limites : [ADR-0007](adr/0007-local-conversation-mistral.md),
[contrat v1](CONVERSATION_API_V1.md), [rapport de recette](CONVERSATION_COACH_REPORT.md).

API vérifiée sur la [documentation officielle Mistral](https://docs.mistral.ai/api/endpoint/chat)
le 2026-11-09 : chat completions, modèle configurable, messages et compteurs d'usage.
