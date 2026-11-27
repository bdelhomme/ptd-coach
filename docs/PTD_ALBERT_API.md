# Essai de PTD Coach avec Albert API

La reprise porte sur le fournisseur conversationnel de la V2. Albert API est
la passerelle DINUM utilisée pour cet essai. Le modèle est un choix distinct,
configurable par `ALBERT_MODEL`. Le fournisseur se sélectionne avec
`CHAT_PROVIDER=albert`. Le modèle généraliste proposé par défaut dans ce mode
est `openai/gpt-oss-120b`.

À la demande du porteur, le premier essai vise DeepSeek V4 Flash. Le
27 novembre 2026, le catalogue authentifié Albert expose l’identifiant exact
`deepseek-v4-flash-0731`. La DINUM le présente comme une expérimentation
jusqu’au 1er décembre et recommande son usage pour le code, compte tenu des
limites qu’elle signale pour la conversation généraliste. La capacité de
raisonnement ne garantit pas la pertinence du coaching. Pour un prochain
essai de coaching généraliste, `gpt-oss-120b` est le candidat proposé.
[Catalogue DINUM](https://guides.ia.numerique.gouv.fr/albert-api/modeles/available-models).

## Essayer depuis le navigateur

Utiliser la clé de son compte dans `.env` local, ignoré par Git, sous le nom
`ALBERT_API_KEY`. La connexion passe par ProConnect.
[Portail Albert API](https://ia.numerique.gouv.fr/outils-ia/albert-api/).

Depuis la racine du dépôt :

```sh
CHAT_PROVIDER=albert ALBERT_MODEL=deepseek-v4-flash-0731 CHAT_MAX_TOKENS=2000 \
  .venv/bin/python -m ptd_coach --port 8803 --data-dir local-data/essai-albert-navigateur
```

Ouvrir [le coach DeepSeek](http://127.0.0.1:8803/coach), choisir un étudiant
de démonstration et utiliser un fil d’équipe ou privé fictif. Pour essayer
`gpt-oss-120b`, fixer `ALBERT_MODEL=openai/gpt-oss-120b`, remplacer le port
par `8804` et utiliser le dossier `local-data/essai-albert-gpt-oss-navigateur`.
[Coach GPT-OSS 120B](http://127.0.0.1:8804/coach).

Le fournisseur textuel appelle seulement `/v1/chat/completions` sur l’hôte
officiel via TLS. Le contexte est assemblé après vérification des droits,
comme pour Mistral. Le navigateur montre le fournisseur actif. La clé reste
sur le serveur local. Le retour exploité contient le texte final et les
métadonnées de génération, avec le modèle retourné, les tokens communiqués,
la durée et la raison d’arrêt. L’appel utilise le format texte, avec un
délai, un plafond et sans répétition automatique. L’instance de recette
garde sa propre base. [Contrat HTTP Albert](https://albert.api.etalab.gouv.fr/reference).

## Rejouer les trajectoires fictives

```sh
PYTHONPATH=. .venv/bin/python scripts/try_albert_ptd.py \
  --out local-data/essai-albert/offline.jsonl
ALBERT_MODEL=deepseek-v4-flash-0731 CHAT_MAX_TOKENS=2000 CHAT_TIMEOUT_SECONDS=45 \
  PYTHONPATH=. .venv/bin/python scripts/try_albert_ptd.py --live \
  --out local-data/essai-albert/deepseek.jsonl
```

Le script rejoue les deux [trajectoires de développement](../pedagogy/qa/PTD_SEMESTER_V2_DEV.json)
et enrichit chaque ligne avec le [verbatim GLM Flash de référence](../pedagogy/evaluations/ptd-v2-demo/semestre-v2.jsonl).
Le cadre de comparaison reprend le contexte V2 0.2, la température 0,2,
le plafond de 2 000 tokens et le délai de 45 secondes. Les deux modèles
poursuivent leurs propres réponses, donc l’historique peut diverger dès
le deuxième tour. Albert règle le raisonnement selon le modèle choisi.
Le mode réel est explicite, borné à huit appels au maximum et s’arrête à
la première erreur. L’option `--turns 1` permet de tester le lancement seul.
La sortie utilise un nouveau fichier. Les critères
qualitatifs restent à relire humainement. Le passage simulé a terminé les
huit tours, avec les huit empreintes de message système identiques à GLM.

Pour la reprise, lire les colonnes `same_system_as_glm`, `invocation`,
`look_for` et `red_flags`. Examiner la fidélité aux faits, la distinction
entre les deux rendus, l’aide à la décision et la qualité du retour sur
le travail d’équipe. Les tokens seuls ne renseignent pas le coût réel ni
la qualité. En cas de refus du modèle, consulter le catalogue `/v1/models`
de la clé et renseigner explicitement le modèle du prochain essai.

## Résultat exploratoire

Les [verbatims et les mesures](../pedagogy/evaluations/ptd-albert-2026-11-27/README.md)
couvrent le lancement avec les deux modèles, puis le blocage DeepSeek au
tour suivant. Le diagnostic ciblé confirme l’épuisement du budget au cours
du raisonnement avant tout texte final. GPT-OSS 120B a répondu au premier
tour, avec un écart dans le décompte des participants et un rendez-vous
trop centré sur l’exposé du plan. La comparaison sur plusieurs tours reste
à exécuter pour ce modèle.

La suite locale passe 168 tests, hors des deux contrôles qui ouvrent le jeu
réservé. La recette dans le navigateur a vérifié le profil fictif et l’affichage
d’Albert et du modèle actif.
