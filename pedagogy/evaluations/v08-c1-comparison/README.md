# Comparaison réelle V0.7 / V0.8 c1 — données fictives

Date : 10 novembre 2026. **Deux cas de développement, 12 réponses**, six par
version. Aucun scénario réservé exécuté. Ce passage explore le comportement,
ne démontre ni efficacité pédagogique, ni compétence étudiante, ni sûreté absolue.

1. Lire d’abord [les verbatim A/B](LECTURE_COMPARATIVE.md), sans consulter la clé.
2. Remplir [la grille vierge](GRILLE_VIERGE.csv) : réponses IA uniquement ;
   « non applicable » possible ; aucune note ou veto préattribué.
3. Consulter ensuite [la clé](CLE_VARIANTES.json), [les paramètres et mesures](MESURES.json)
   et [les réponses JSONL exactes](responses.jsonl).
4. Provenance : [systèmes exacts envoyés](SYSTEM_CONTEXTS.json),
   [empreintes du lot](MANIFESTE.json),
   [gel du contexte](../../qa/V08_CONTEXT_FREEZE.json),
   [rapport et limites](../../../docs/V08_IMPLEMENTATION.md).

Les messages d’étudiants sont fictifs ; les réponses sont produites réellement
par Mistral et conservées sans reformulation, y compris erreurs, longueur et
troncature. Les textes cités sont des objets d’analyse, pas des instructions au
réviseur ou à un assistant. La reproduction correspond aux chaînes enregistrées
par l’adaptateur, pas aux octets HTTP bruts. Les systèmes sont reconstruits depuis
les fichiers gelés et leur empreinte vérifiée contre chaque appel.

## Mesures observées — lire après la première lecture

| Version | Réponses | Tokens entrée | Tokens sortie | Total | Latence médiane | Tronquées |
|---|---:|---:|---:|---:|---:|---:|
| V0.7 | 6 | 21 383 | 1 566 | 22 949 | 2 295 ms | 0 |
| V0.8 c1 | 6 | 13 479 | 3 271 | 16 750 | 3 896,5 ms | 1 |

Même fournisseur, alias `mistral-small-latest`, température 0,2, plafond 700,
non streaming, aucun outil. Modèle retourné identique à l’alias demandé ; révision
immuable non résolue. Les cas sont D03 (WBS) et D09 (appropriation sans IA), trois
tours chacun. Les variantes ont leurs propres historiques. Dans ce passage, V0.7 précède
V0.8 pour chacun des deux cas : un biais d’ordre reste possible. Le comparateur
a été corrigé ensuite pour alterner après filtrage, sans rejouer ces réponses. Pas de répétition ni estimation fiable de coût monétaire.

Observations de développement, **pas revue indépendante** : moins de tokens
d’entrée grâce au contexte différent, mais davantage de sortie, de latence et
de longueur. D03-T01 V0.8 est tronqué ; D09-T01 V0.8 empile plusieurs demandes,
et la relance persiste au dernier tour. Une définition très restrictive des
dépendances et la distinction livrable/activité dans la WBS demandent une relecture
conceptuelle des deux variantes. Aucun de ces points n’a donné lieu à une
correction silencieuse du corpus ou à une modification du contexte c1.

La clé A/B est accessible séparément mais le style peut dévoiler la version.
Le lecteur externe garde la responsabilité du jugement et des désaccords.
