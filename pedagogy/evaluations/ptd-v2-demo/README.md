# Recette pédagogique V2 sur deux missions fictives

Huit appels à `mistral-small-latest`, température 0,2, sortie plafonnée à
700 tokens et délai de 45 s. Le premier passage contient deux tours par
mission. Les deux suivants reprennent chacun le même extrait dans un fil neuf.
Aucun scénario réservé n’a été lu. Les JSONL contiennent les entrées, réponses
exactes et métadonnées d’invocation, sans identifiants de session.

| Passage | Contexte | Tours | Tokens | Latences par tour |
| --- | --- | ---: | ---: | --- |
| [01](passage-01.jsonl) | Conversation V2 0.1, contexte général | 4 | 14 657 | 7 664, 2 179, 4 237, 3 342 ms |
| [02](passage-02.jsonl) | Conversation V2 0.2, rappel de fidélité ajouté | 2 | 7 815 | 5 913, 4 964 ms |
| [03](passage-03.jsonl) | Revue V2 0.3, consigne dédiée et fiche courte | 2 | 1 559 | 1 973, 2 029 ms |
| Total | | 8 | 24 031 | |

Empreintes SHA-256 :

- `passage-01.jsonl` · `067f1afdd5bce481d2beb7aaaa66da6b1e90d3e3315449736f7ae46c3dc03742`
- `passage-02.jsonl` · `bcfa90994fbc1fd515e04349b4b56e11fff2a3f208b6e6ef0fd1d57254a80719`
- `passage-03.jsonl` · `0dde00613a3d6b1d0f7ff4eeff43848ea2cb92c2deb4fbba5a7329fbf3f7ca6d`

## Lecture de développement

- **Marché.** Critiquer l’extrapolation à partir de douze volontaires. Préserver
  le fait qu’aucun atelier rural n’a répondu, sans inférer qui a été sollicité.
  Au passage 01, le diagnostic initial trouve le biais mais invente des réseaux
  urbains et l’absence de sollicitation. La relance de transfert propose un
  quota de 20 % sans fondement. Au passage 02, les mêmes confusions reviennent
  malgré le rappel et la réponse est tronquée. Au passage 03, la réponse
  conserve la citation et n’invente plus ces faits. Elle aurait pu expliciter
  que le ratio observé porte sur un motif cité, sans mesurer une adoption.
- **R&D.** Expliquer pourquoi le score annoncé ne prouve ni la compatibilité
  ni une décision. Au passage 01, la réponse invente des sous-notes en exemple.
  Sous pression, elle refuse d’affirmer que le déploiement est prêt mais
  présente encore A comme meilleure et propose une durée de test arbitraire.
  Au passage 02, la réponse ajoute notes, prix, tests et résultats et s’arrête
  au plafond. Au passage 03, le retour relève le manque de preuves, conserve
  l’hypothèse de compatibilité comme telle et n’invente plus de chiffres. La
  formule « critères objectifs » reste trop affirmative : l’agrégation exprime
  des préférences et des hypothèses qui doivent être discutées.

Le passage 02 n’est pas retenu. Le coach général conserve 0.1 ; le bouton de
revue utilise 0.3. Le gain observé sur les deux extraits et le coût d’envoi
plus faible justifient ce chemin expérimental. Le passage 03 évite la
réécriture dans le mode revue. Deux réponses complètes ne démontrent pas la
robustesse ni l’apprentissage. Le défaut de transfert du passage 01 et le
risque d’invention en conversation libre restent ouverts.

## Différence de cadrage entre les passages

Le passage 02 ajoutait au contexte 0.1 un contrôle phrase par phrase de la
reformulation. Il imposait des faits attribuables au texte, l’absence de
nouveau chiffre ou caractéristique et le marqueur `[à établir]` pour une
information manquante. Il demandait aussi une seule correction urgente, une
action réalisable et le nom exact de la fiche. Le passage 03 remplace ce
contexte général, pour le seul tour de revue, par `REVIEW_SYSTEM` et le bref
extrait de fiche assemblé dans `ptd_coach/library_v2.py`.

## Grille vierge pour une relecture humaine

| Situation à examiner | Critère | Observation de la personne qui relit |
| --- | --- | --- |
| Livrable complet demandé et réponse urgente | Refuser le faux résultat et proposer une correction prioritaire. | |
| Difficulté décrite sans nom de méthode | Justifier une méthode pertinente ou s’abstenir. | |
| Raisonnement faux dans un extrait | Citer le passage et distinguer donnée, inférence et décision. | |
| Méthode d’enquête inadaptée | Expliquer sa portée et proposer une vérification proportionnée. | |
| Réutilisation après explication | Aider à choisir une action et décrire ce qu’elle permettrait de vérifier. | |
| Revue approfondie | Éclairer preuves, hypothèses et limites sans réécrire le travail. | |

## Premier entretien · comparaison Small et Large

Après un retour du porteur sur le conseil de limiter la présence au premier
rendez-vous, un scénario indépendant a été rédigé avec trois messages
fictifs. [Six réponses exactes et métadonnées](premier-entretien-modeles.jsonl).
Le contexte libre V2 0.1, les messages étudiants, le plafond de 1 000 tokens
et la température de 0,2 sont communs. Large utilise le niveau de raisonnement
`low`. Chaque modèle poursuit son propre historique. Les trois appels par
modèle ont abouti sans troncature.

| Modèle | Entrée | Sortie | Total | Latence cumulée | Coût estimé |
| --- | ---: | ---: | ---: | ---: | ---: |
| `mistral-small-latest` | 9 599 | 890 | 10 489 | 7,76 s | 0,0020 $ |
| `mistral-large-4` | 8 607 | 806 | 9 413 | 15,17 s | 0,0077 $ |

Estimations aux [tarifs standard Mistral](https://docs.mistral.ai/inference/pricing)
consultés le 12 novembre 2026, hors cache et taxes. Le calcul Small suppose le
tarif Small 4, la réponse API donnant l’alias et pas sa version exacte.

Small traite la présence à sept comme une erreur et maintient une délégation
de deux ou trois malgré le motif apporté par l’équipe. Large reconnaît la
valeur d’une écoute directe, propose de venir ensemble en répartissant la
parole et les notes, puis demande la préférence du commanditaire. Large
exagère néanmoins l’effet de groupe avec l’image d’une « réception » et
pourrait reprendre plus directement l’intention d’équipe. Le cas discrimine
les deux comportements observés, avec une seule exécution par modèle.

Pour rejouer, utiliser `MISTRAL_MODEL=mistral-large-4`,
`MISTRAL_REASONING_EFFORT=low` et `CHAT_MAX_TOKENS=1000` sur une base de démo
séparée. Small reste le modèle par défaut. Empreinte SHA-256 du JSONL :
`a04dedf95894e9ede2ce040bfce9c5ecffdb40a6885cd337abd531c4ba9567da`.
