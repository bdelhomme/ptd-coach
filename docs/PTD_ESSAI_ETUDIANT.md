# Essai comme étudiant dans PTD Coach

Cet espace de recette utilise une mission fictive dans un centre de
recherche. Le groupe de sept étudiants étudie pour le centre Atlas comment
faire évoluer sa culture vers des solutions davantage centrées sur les
clients. Le déroulé offre six situations possibles du cadrage à la restitution.
Les méthodes d’enquête, résultats et recommandations restent à construire.

L’essai part d’une difficulté repérée dans un fil local avec GPT-OSS. Le sujet
décrit dans le chat et la mission fictive attachée au profil divergeaient.
Le coach a donné une liste de recommandations, puis a parlé à l’étudiant
comme s’il représentait le centre. L’essai crée une mission cohérente,
affiche son titre dans le coach et ajoute une consigne locale sur le rôle
d’étudiant, le besoin de coaching et la reprise après une réponse trop directive.

Depuis le dépôt avec `ALBERT_API_KEY` dans le fichier local ignoré `.env` :

```sh
CHAT_PROVIDER=albert ALBERT_MODEL=openai/gpt-oss-120b CHAT_MAX_TOKENS=2000 \
  .venv/bin/python -m ptd_coach --essai-etudiant --port 8805 --data-dir local-data/essai-etudiant-atlas
```

Ouvrir [le coach](http://127.0.0.1:8805/coach), choisir **Étudiant démo A** et
créer un fil. Vérifier le titre **Faire évoluer la culture d’un centre de
recherche** et l’indication **Albert API**. **Notre projet** présente le
sujet et le commanditaire. **Faire le point** permet d’avancer entre les
situations de l’essai. Le fil privé et le fil d’équipe suivent les
autorisations habituelles. N’utiliser que des informations fictives.

Le mode `--essai-etudiant` initialise des bases projet et conversation
distinctes. Les données de mission et de séance viennent du serveur.
Le contexte `conversation-ptd-v2-student-trial-0.1` hérite de la V2 0.2.
Les autres lancements conservent leurs missions et contextes d’origine.
L’essai ne crée pas de mécanisme de changement de mission par fil.

La recette dans le navigateur a ouvert un fil privé vide avec la mission
visible et GPT-OSS 120B via Albert. Dans un fil jetable séparé, deux appels
réels ont abouti (4,7 s et 22,5 s). Le coach a posé une question ciblée au
lancement et a conservé le rôle de l’équipe au tour suivant. Sur ce second
tour, il a proposé un tableau illustratif et un cadre d’analyse assez
directifs. Le test ne valide pas la posture sur la durée.
