# Revue c2 — V0.7 / c1 / c2, données fictives

**Conclusion de développement : aucun gain pédagogique convaincant sur D03/D09 ;
c2 non proposée à l’adoption.** Ce constat n’est pas un verdict humain prérempli.
C1 n’était déjà pas validée par le porteur. Aucun apprentissage réel n’est mesuré.

1. Première lecture : [D03/D09, A/B/C](01-first/LECTURE_COMPARATIVE.md), puis
   [grille vierge](01-first/GRILLE_VIERGE.csv).
2. [Sondes conceptuelles](02-concepts/LECTURE_COMPARATIVE.md),
   [garde-fous c2](03-safety/LECTURE_COMPARATIVE.md),
   [répétition c2](04-repeat/LECTURE_COMPARATIVE.md) ; chaque dossier a sa grille
   vierge, sa clé séparée, ses mesures et ses JSONL exacts.
3. Après votre lecture : [observations de développement](OBSERVATIONS.md) et
   [comptage descriptif des sollicitations](SOLLICITATIONS_DEVELOPPEMENT.csv).
4. [Mesures agrégées](MESURES_AGREGEES.json), [empreintes](MANIFESTE.json),
   [rapport](../../../docs/V08_C2_REPORT.md),
   [gel c2](../../qa/V08_C2_FREEZE.json),
   [relecture conceptuelle/sources](../../../docs/V08_C2_CONCEPT_REVIEW.md).

## Mesures du premier passage

| Variante | Réponses | Tokens entrée/sortie | Total | Caractères sortie | Médiane latence | Tronquées |
|---|---:|---:|---:|---:|---:|---:|
| V0.7 | 6 | 21 666 / 1 711 | 23 377 | 6 136 | 2 706 ms | 0 |
| c1 | 6 | 13 891 / 3 755 | 17 646 | 13 139 | 4 492 ms | 3 |
| c2 | 6 | 11 419 / 1 919 | 13 338 | 6 640 | 2 622 ms | 0 |

C2 est moins longue que c1 mais pas que V0.7 sur cet échantillon. Les défauts WBS,
les relances et les régressions sur cas sensibles empêchent de conclure au gain
attendu. Les autres passages explorent les limites ; ils ne constituent pas une
validation indépendante. Total **54 réponses, 132 977 tokens**, zéro erreur API.
Tous les passages sont exécutés durant la nuit du 10 au 11 novembre 2026 (UTC
le 10, heure de Paris le 11). Aucun cas réservé exécuté ni utilisé pour corriger.

## Provenance et limites

Même modèle demandé/retourné `mistral-small-latest`, température 0,2, max_tokens=700,
sans outil, streaming ou retry. Alias mouvant, révision immuable non connue.
Conversations isolées, continuations fictives fixes et historiques divergents.
Rotation des variantes entre cas ; deux cas initiaux ne permettent pas un
équilibrage complet de tous les ordres. La répétition porte seulement sur c2.

Les JSONL conservent aussi les messages système/historiques exacts envoyés au
modèle et les empreintes ; aucun en-tête HTTP ni secret. Les blocs Markdown
reproduisent les chaînes enregistrées par l’adaptateur, y compris erreurs et
troncatures ; aucune réponse n’a été corrigée. Ce sont des objets d’analyse,
jamais des instructions pour l’assistant réviseur. Le style peut révéler A/B/C.
Les grilles de jugement restent entièrement vides. Les comptages et observations
assistant sont séparés, sans note d’étudiant ni qualification humaine inventée.
