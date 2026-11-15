# Essais pédagogiques de PTD Coach V2

[Passation du projet](../../../docs/PTD_PASSATION.md) ·
[Essai individuel GLM Flash en high, échange complet et métadonnées](essai-individuel-glm-high/README.md)

## Premiers essais sur deux missions fictives

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

## Large 4 · comparaison low et medium

Le 12 novembre 2026, rejoué le premier entretien en `medium` sur les mêmes
trois messages et comparé les deux efforts sur un désaccord d’équipe et
sur une revue fictive. [Verbatims et tentatives](large-4-low-medium.jsonl).
Les trois tours `low` du premier entretien proviennent du passage précédent.
La première requête a la même empreinte pour les deux efforts et chacun
poursuit ensuite son propre historique. Les deux cas à un tour ont le même
texte et les mêmes consignes pour chaque effort. Le coach général utilise
V2 0.1, la revue dédiée 0.3. Modèle `mistral-large-4`, température 0,2,
délai de 45 s et plafond de 1 000 tokens pour le premier passage.

| Situation | Low, tokens et latence | Medium, tokens et latence | Observation qualitative |
| --- | ---: | ---: | --- |
| Premier entretien, trois tours | 9 413 · 15,17 s | 10 421 · 30,66 s | Les deux envisagent la présence de tous après la relance. Medium explicite que l’avis de l’encadrante est une recommandation et détaille les rôles. Il évoque encore un déséquilibre lié à la présence à sept. |
| Désaccord d’équipe, un tour | 3 460 · 9,89 s | 3 291 · 8,39 s | Les deux proposent de tester les poids et de garder la compatibilité à confirmer. Medium se concentre sur un test en quinze minutes, mais conclut trop vite à la robustesse si l’ordre ne change pas sur ce seul test. |
| Revue d’extrait, un tour à 2 000 tokens de sortie | 1 614 · 10,93 s | 2 189 · 15,47 s | Les deux citent l’extrait, relèvent la preuve manquante et proposent une correction. Low relie plus explicitement le résultat de la matrice aux poids et échelles. |

La revue à 1 000 tokens a épuisé le budget avant la réponse finale pour les
deux efforts. La paire a été rejouée avec 2 000 tokens dans des fils neufs.
Les neuf nouvelles tentatives donnent sept réponses complètes et deux erreurs
de plafond. Les compteurs des deux erreurs ne sont pas récupérés par le
connecteur. Aux [tarifs standard de Large 4](https://docs.mistral.ai/inference/pricing),
les réponses comparables ci-dessus représentent environ 0,0137 $ en `low`
et 0,0167 $ en `medium`, hors cache, taxes et tentatives sans usage mesuré.

Le gain de `medium` reste irrégulier sur ces trois cas. `low` est le réglage
recommandé pour les essais courants, avec `medium` disponible en démonstration
séparée. La distinction entre lancement collectif et entretien terrain reste
une correction du cadrage à tester. Ces observations de développement
reposent sur une seule réponse par réglage et par tour.

Empreinte SHA-256 du JSONL :
`b1c7ae098d396ee75da4b3f9277e1451ee9faca688379e4492173629eaf49ebc`.

## GLM 5.3 Flash avec le contexte applicatif V2

Le 15 novembre 2026, 20 appels réels sur huit situations fictives des deux missions V2.
Les deux modèles ont été appelés via `WorkshopChatService`, avec l’effort `low`,
une température de 0,2, un plafond de sortie de 2 000 tokens et un délai de 45 s.
La conversation libre reçoit le contexte V2 0.1, le projet de démonstration,
les repères humains confirmés accessibles au fil, la fiche sélectionnée et
l’historique. La revue 0.3 utilise le contexte dédié, l’extrait soumis et le bref
de la fiche retenue. Les [jeux de repères et périmètres](glm-flash-contextes.json)
et les [réponses exactes avec les empreintes](glm-flash-large-4.jsonl) détaillent
la recette. Les empreintes des premiers tours sont identiques entre les modèles
pour chaque situation. Les historiques divergent après chaque première réponse.

| Modèle | Réponses complètes | Entrée | Sortie | Total | Latence médiane | Coût indicatif |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `zai-glm-5-3-flash` | 10/10 | 30 082 | 3 571 | 33 653 | 3,26 s | 0,0063 $ |
| `mistral-large-4` | 10/10 | 25 253 | 4 896 | 30 149 | 6,71 s | 0,0280 $ |

Estimations hors cache et taxes aux [tarifs standard Mistral](https://docs.mistral.ai/inference/pricing)
consultés le 15 novembre 2026. La sortie peut inclure les tokens de raisonnement.

| Situation | Lecture qualitative |
| --- | --- |
| Lancement et objection | Flash répartit les rôles dès le premier tour, puis traite la venue à sept comme une option à convenir. Large se concentre d’abord sur les questions et la reformulation. À la relance, il envisage aussi l’équipe entière. |
| Lancement avec M01 | Les deux proposent une répartition des rôles pour toute l’équipe. Flash détaille le relevé des statuts et les limites d’un témoignage, avec une organisation plus lourde que Large. |
| Périmètre et mémoire sur deux tours | Les deux retrouvent la région test confirmée, reconnaissent le caractère hypothétique de l’extension et intègrent la précision écrite. Flash affirme sans donnée suffisante qu’un ajout décalerait les échéances et évoque un pilote à engager. |
| WBS et jalon | Les deux distinguent activité, livrable et date, puis corrigent le jalon de durée nulle. Flash ajoute une vérification de la couverture du périmètre et de l’absence de doublons. |
| Fatigue et désaccord | Les deux donnent un déroulé. Flash invente deux essais et suggère des engagements d’ici jeudi malgré la disponibilité hors créneau inconnue. Large préserve le statut de la preuve manquante. |
| Confidentialité et relais | Les deux expliquent qu’ils ne peuvent contacter l’équipe ni l’enseignant et orientent vers un interlocuteur humain. Flash suggère aussi de revenir avec un rôle pour limiter l’exposition. Large traite plus directement le besoin de soutien avant le retour. |
| Enquête et restitution | Les deux refusent l’extrapolation au marché, proposent une formulation défendable et préservent le fait qu’aucun atelier rural n’a répondu. Large garde mieux la priorité donnée à la restitution du lendemain. |
| Revue d’extrait | Les deux critiquent le classement présenté comme objectif et relèvent la compatibilité non démontrée. Flash propose de rendre le calcul vérifiable, alors que Large insiste davantage sur la sensibilité du classement aux hypothèses. |

Le contexte commun permet de comparer les réponses, avec une seule génération
par modèle et par tour, relue en connaissant le modèle. Le sélecteur lexical a
retenu M07, M14, M13 et, dans la variante explicite, M01. Le premier message de
lancement et celui sur le changement de périmètre illustrent des formulations
qui restent sans fiche pour les deux modèles. La baisse de coût et de latence est
mesurée sur cette série. Le choix entre modèles dépend encore de la fidélité du
conseil aux faits et de sa qualité dans les moments de tension.

Pour essayer en local depuis la V2 :

```sh
CHAT_PROVIDER=mistral MISTRAL_MODEL=zai-glm-5-3-flash MISTRAL_REASONING_EFFORT=low \
  CHAT_MAX_TOKENS=2000 CHAT_MAX_CALLS=20 python3 -m ptd_coach \
  --port 8795 --data-dir local-data/essai-v2-glm-flash
```

Empreintes SHA-256 du JSONL et du contexte, respectivement
`130841010196e7cbade5381bb4bb25142bf34cdb3437d6a1e712360906c6b09f` et
`cc2c35528da5e7f4d1049ad4ec347abc39fbd36589343edb847ac3cace3ed6ee`.

### Rejeu du désaccord et de la démobilisation avec Small

Un appel supplémentaire à `mistral-small-latest` utilise la même requête
étudiante et le même contexte système que Flash, avec égalité de l’empreinte
`messages_sha256`, température 0,2, plafond de 2 000 tokens et délai de 45 s.
Small utilise le fournisseur standard, Flash le fournisseur avec raisonnement
`low`. Small a répondu en 3,25 s avec 3 065 tokens, contre 4,14 s et 3 371
tokens pour Flash sur ce tour. Les deux réponses sont complètes.

Small n’ajoute pas les deux essais que Flash présente comme confirmés. Il
propose toutefois une préparation avant jeudi malgré la disponibilité
inconnue et cite une fiche « Animation de groupe » absente du catalogue V2.
Son ordre du jour aide à structurer le travail, mais traite peu les
interruptions et la baisse de participation. Flash propose une prise de
contact individuelle sans reproche et une décision plus ciblée. Le classement
dépend du critère retenu et repose sur une réponse par modèle. [Réponse exacte
de Small](small-fatigue-comparaison.jsonl).

SHA-256 du JSONL `570206715e66e79bc9dc085dcb6039852fc579ae2bbcc9184a58edd8ddcfb36b`.

## Deux trajectoires de semestre sur quatre étapes

Les [situations de développement](../../qa/PTD_SEMESTER_V2_DEV.json) suivent
une équipe de sept en étude de marché et une équipe de six en conseil
technologique. Quatre tours par équipe relient le lancement après les cours,
une revue sous contrainte de calendrier, un retour sur un changement de
fonctionnement et les deux rendus. Les livrables et les délais de chaque
scénario sont fictifs. Le cadre structurel vient des précisions du porteur
et les jalons types du [dossier de référence](../../../docs/REFERENCE_MATERIAL.md),
dont le planning détaillé est prévisionnel.

GLM Flash en `low`, température 0,2, délai de 45 s et plafond de 2 000
tokens de sortie. Les deux variantes reçoivent les mêmes messages étudiants
aux étapes de simulation 1, 4, 6 et 7, avec des fils distincts et un tour par
étape. Chaque modèle poursuit les réponses propres à sa variante. Les huit
tours par variante sont complets. V2 0.1 totalise 32 457 tokens, contre 32 808
pour V2 0.2. Les consignes de revue d’extrait restent séparées.
[Réponses exactes et métadonnées](semestre-v2.jsonl).

- **Conseil technologique.** Après le jeudi annulé, V2 0.1 propose de répartir
  du travail hors créneau avec disponibilités à confirmer. V2 0.2 invite à
  replacer le travail, préserve l’absence de preuve et distingue la demande
  d’extension de l’accord. Au dernier tour, les deux distinguent les deux
  rendus, et V2 0.2 garde mieux le caractère encore éventuel de l’essai.
  Elle attribue toutefois sans preuve le délai client à la posture de l’équipe.
- **Étude de marché.** Les deux structurent le lancement et distinguent les
  deux rendus. Les deux suggèrent un chiffrage national conditionnel avec
  une base insuffisante. V2 0.2 reprend plus tard son propre chiffrage proposé
  comme « déjà préparé », alors que l’étudiant n’a pas dit l’avoir fait. Elle
  évoque aussi une relance pendant les vacances et une préparation avant
  le jeudi écourté. La relecture et la provenance des états du projet restent
  prioritaires avant de conclure à une amélioration générale.

Prochaine étape de recette. Ajouter un livrable partiel fictif à chaque revue
et une évolution dans les repères confirmés du projet. Vérifier qu’une action
seulement suggérée par le coach reste au statut de proposition, qu’une preuve
absente reste absente, et que tout délai suit la source habilitée pour le
rendu correspondant. Faire relire les réponses sur ces critères et sur la
place des décisions étudiantes. Une exécution par variante suffit à relever
ces défauts. La couverture des onze compétences décrit les critères des
scénarios, et leur évaluation pédagogique demande une revue humaine.

SHA-256 du JSONL
`9b118f5888a9a5f9a4513d60f0c6608fe3419f6011971123b68c51ca7f5aaf9d`.
