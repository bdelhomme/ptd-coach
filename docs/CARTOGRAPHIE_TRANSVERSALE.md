# Cartographie critique des essais antérieurs

Inventaire arrêté au début de la campagne transversale, sur la base de la PR #8.
Le décompte utilise les lignes JSONL de statut `model_called` avec réponse.
Le même scénario rejoué compte une seule fois dans la couverture d’une compétence.
Les nombres de réponses incluent tours et répétitions. Les codes ci-dessous
sont une lecture de la tâche posée, distincte de la qualité des réponses.
Plusieurs codes peuvent s’appliquer. Le signe « — » repère un cas surtout
consacré au dialogue ou aux garde-fous, ou l’absence de réponse réelle.

Les **47 cas rédigés** hors réserve ont tous un exercice technique documenté
avec fournisseur simulé. Les suites V0.6 et V0.7 sont rejouées par
[test_chat.py](../tests/test_chat.py). D01–D12 ont un passage mock décrit
dans le [rapport c1](V08_IMPLEMENTATION.md). Le banc c2 couvre aussi P01–P03
avec des fixtures, dans [test_chat_c2.py](../tests/test_chat_c2.py).
Un dry-run contrôle le plan et produit zéro réponse. Un mock vérifie le passage
technique et produit des réponses fixes. Les archives ci-dessous contiennent
**146 réponses Mistral réelles sur 17 scénarios distincts**. Les 30 autres cas
n’ont pas de réponse réelle archivée. Les fichiers techniques du réservé
restent hors inventaire.

## Passages Mistral retrouvés

| Trace | Cas distincts | V0.7 historique ou comparateur | c1 | c2 |
|---|---:|---:|---:|---:|
| [chat-v1-1-mistral-v07.jsonl](../pedagogy/evaluations/mistral-small-v07/donnees/chat-v1-1-mistral-v07.jsonl) | 12 | 26 | 0 | 0 |
| [chat-v1-2-mistral-v07.jsonl](../pedagogy/evaluations/mistral-small-v07/donnees/chat-v1-2-mistral-v07.jsonl) | 12 | 26 | 0 | 0 |
| [chat-v1-mistral-smoke.jsonl](../pedagogy/evaluations/mistral-small-v07/donnees/chat-v1-mistral-smoke.jsonl) | 1 | 2 | 0 | 0 |
| [chat-v1-mistral-v07.jsonl](../pedagogy/evaluations/mistral-small-v07/donnees/chat-v1-mistral-v07.jsonl) | 12 | 26 | 0 | 0 |
| [v08-c1-comparison](../pedagogy/evaluations/v08-c1-comparison/responses.jsonl) | 2 | 6 | 6 | 0 |
| [01-first](../pedagogy/evaluations/v08-c2-comparison/01-first/responses.jsonl) | 2 | 6 | 6 | 6 |
| [02-concepts](../pedagogy/evaluations/v08-c2-comparison/02-concepts/responses.jsonl) | 3 | 6 | 6 | 6 |
| [03-safety](../pedagogy/evaluations/v08-c2-comparison/03-safety/responses.jsonl) | 6 | 0 | 0 | 12 |
| [04-repeat](../pedagogy/evaluations/v08-c2-comparison/04-repeat/responses.jsonl) | 2 | 0 | 0 | 6 |

Les trois passages complets V0.7 et le smoke ont des versions de prompt
historiques distinctes. Les lignes V0.7 des comparaisons ultérieures utilisent
le contexte V0.7 figé alors disponible. Cette colonne inventorie une famille
de traces. Elle ne rend pas ces passages statistiquement interchangeables.

## Inventaire cas par cas

| Cas | Situation | Compétences sollicitées | V0.7 | c1 | c2 |
|---|---|---|---:|---:|---:|
| T01 | Jalon | A2 | — | — | — |
| T02 | Dépendance | A2 | — | — | — |
| T03 | Répartition des sept membres | B1 | — | — | — |
| T04 | Charge et accusation | B1, B2 | — | — | — |
| T05 | Parole monopolisée | B3, D2 | — | — | — |
| T06 | Conseils sans jeu de rôle | — | — | — | — |
| T07 | Clôture simple | — | — | — | — |
| T08 | Dépendances en réunion | A2, B1 | — | — | — |
| T09 | Objectif de progression | D2 | — | — | — |
| T10 | Usage et progrès | D2 | — | — | — |
| T11 | Planning et responsables à déléguer | A2, B1 | — | — | — |
| T12 | Réunion trop longue | B2, B3 | — | — | — |
| T13 | Écriture du planning | A3 | — | — | — |
| T14 | Classement des membres | — | — | — | — |
| T15 | Confidences de Julie | — | — | — | — |
| T16 | Privé de Martin | — | — | — | — |
| T17 | Insultes et peur | — | — | — | — |
| T18 | Référence ISO | — | — | — | — |
| T19 | Partage partiel | — | — | — | — |
| T20 | Approbation privée alléguée | — | — | — | — |
| M01 | Jalon en bref | A2 | 8 | — | — |
| M02 | Coordination sans silos | B1 | 6 | — | — |
| M03 | Revoir une attribution de faute | B1, B2 | 9 | — | — |
| M04 | Débrief de l’animation | B3, D2 | 9 | — | — |
| M05 | Préparer un entretien client et vérifier le besoin | A1, D1 | 6 | — | — |
| M06 | Modification du planning | A3, B2 | 6 | — | 2 |
| M07 | Accès au privé | — | 6 | — | 2 |
| M08 | Insultes et message anonyme | — | 6 | — | 2 |
| M09 | Citation ISO non vérifiée | — | 6 | — | 2 |
| M10 | Appropriation sans l’IA | D2 | 6 | — | 2 |
| M11 | Partage révoqué avant confirmation | — | 6 | — | 2 |
| M12 | Réunion et décision en sept minutes | B2, B3 | 6 | — | — |
| D01 | Livrable en trente secondes | A2 | — | — | — |
| D02 | Urgence de synchronisation | D1, B2 | — | — | — |
| D03 | WBS et calendrier | A2 | 6 | 6 | 6 |
| D04 | Responsabilité et contribution | B1, B2 | — | — | — |
| D05 | Choisir un outil léger | A2, A3 | — | — | — |
| D06 | Deux interprétations du retard | A3, B2, C1 | — | — | — |
| D07 | Objection client sans simulation | D1, B2 | — | — | — |
| D08 | Désaccord devenu exclusion | B2 | — | — | — |
| D09 | Comprendre sans assistance | A2, D2 | 6 | 6 | 6 |
| D10 | Réponse sûre mais erronée | A3 | — | — | — |
| D11 | Retour sur animation | B3, D2 | — | — | — |
| D12 | Transfert et limites de preuve | A2, D2 | — | — | — |
| P01 | Lien début-début et chevauchement | A2 | 2 | 2 | 2 |
| P02 | Jalon et activité | A2 | 2 | 2 | 2 |
| P03 | Risque, incident et opportunité | A3 | 2 | 2 | 2 |

## Couverture des onze compétences candidates

| Code | Cas rédigés | Cas Mistral distincts | Limite de l’évidence disponible |
|---|---:|---|---|
| A1 | 1 | 1 · M05 | Préparation et confirmation orale dans M05. Aucun cahier des charges construit ou révisé. |
| A2 | 12 | 5 · M01, D03, D09, P01, P02 | Définitions, WBS, dépendances et jalons. Forte répétition de tâches proches. |
| A3 | 6 | 2 · M06, P03 | Modification de planning et distinction risque/problème. Peu d’arbitrage avec client. |
| B1 | 7 | 2 · M02, M03 | Répartition et accusations de désengagement. Interfaces et choix de méthode peu éprouvés. |
| B2 | 10 | 3 · M03, M06, M12 | Dialogue d’équipe, réunions, accord. Peu de désaccord ordinaire mené jusqu’à une décision fidèle. |
| B3 | 5 | 2 · M04, M12 | Parole monopolisée et animation de réunion. Mobilisation de personnes silencieuses peu variée. |
| C1 | 1 | 0 · — | Le scénario D06 examine une hypothèse de retard en mock. Aucun arbitrage complexe sur preuves en API. |
| C2 | 0 | 0 · — | Les gardes de confidentialité sont testés. Les enjeux et responsabilités du projet restent à éprouver comme activité pédagogique. |
| D1 | 3 | 1 · M05 | Un entretien client court et vérification du besoin dans M05. Objections et négociation existent dans les cas écrits ou mock. |
| D2 | 8 | 3 · M04, M10, D09 | Débrief et difficulté à expliquer sans IA. Les dialogues ne renseignent pas le transfert autonome. |
| D3 | 0 | 0 · — | Aucune activité de restitution argumentée ciblée dans les anciens cas d’essai conversationnel. |

Les comparaisons c1 et c2 hors passage de garde-fous ont produit **54 réponses**.
Les situations portant directement sur A2 en représentent **48**
(D03, D09, P01, P02). P03 porte sur la distinction risque/problème.
Pour la relation commanditaire, l’unique cas M05 en API est une préparation
d’entretien. Les sollicitations D02 et D07 n’ont qu’un passage technique.
Le nom du client dans un exemple de WBS ou dans un retard ne constitue pas
un test de négociation ou de validation du besoin.

Les commentaires des dossiers c1/c2 sont des observations de développement.
Le porteur a transmis une revue qualitative de D03/D09. Aucune grille
indépendante remplie, composition de jury ou note ne peut être attestée
dans les artefacts consultés. Le choix de non-adoption de c2 demeure tracé.

Le [nouveau jeu](../pedagogy/qa/COACH_TRANSVERSAL_DEV_CASES.json) couvre les
onze codes dans des situations croisées. Les 24 cas écrits et leur validation
technique ont leur propre statut. Le premier passage réel ne porte que sur
les cas indiqués dans le [rapport de campagne](CAMPAGNE_TRANSVERSALE.md).
