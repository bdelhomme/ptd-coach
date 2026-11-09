# Paramètres, tokens et provenance

Date de préparation : 9 novembre 2026. Horodatages des traces : UTC, conservés tels quels.

## Résumé des quatre passages archivés

| Passage | Cas | Réponses | Entrée | Sortie | Total tokens |
|---|---:|---:|---:|---:|---:|
| Essai court M01, v1 | 1 | 2 | 6 149 | 108 | 6 257 |
| Passage complet v1 | 12 | 26 | 81 375 | 3 485 | 84 860 |
| Passage complet v1.1 | 12 | 26 | 85 021 | 2 983 | 88 004 |
| Dernier passage v1.2 | 12 | 26 | 87 949 | 3 996 | 91 945 |

Total des quatre fichiers : **80 réponses, 271 066 tokens**. Le smoke est une exécution supplémentaire de M01 ; ne pas le compter comme un nouveau scénario. Les essais interactifs du navigateur sont hors de ce corpus et hors de ce total.

## Paramètres constatés dans les traces

- Fournisseur : Mistral ; statut de chaque ligne : `model_called`.
- Modèle demandé et valeur renvoyée : `mistral-small-latest`. L'API renvoie encore un alias, pas un identifiant de révision immuable ; aucune révision plus précise n'est inventée.
- Température : **0,2** ; `max_tokens` : **700** par réponse, et non par conversation.
- Chaque cas démarre avec un historique distinct. Les tours suivants reçoivent les messages et réponses précédents du même cas.
- Les critères, signaux et marqueurs de veto sont des annotations de sortie pour la revue, pas des instructions envoyées à Mistral. Les ressources et le système sont communs au contexte autorisé.
- Selon le code de la version archivée : endpoint chat completions HTTPS, `stream=false`, `tool_choice=none`. Ces deux paramètres ne sont pas des champs des JSONL.
- Les tokens d'entrée incluent le système, les ressources et les historiques retransmis ; le total n'est pas le nombre de mots ni une mesure de compétence. Pas d'estimation en euros.

## Version et limites des empreintes

### Essai court M01, v1

Version : `conversation-v1+v07-proposed`.

Période enregistrée : `2026-11-09T13:38:24.458281+00:00` à `2026-11-09T13:38:25.699969+00:00`.

Empreinte de contexte enregistrée : `bfc232e0964908d5252726fbeb97b8028c44481dbdcef985648a8cf16a6a28e7`.

SHA-256 du fichier JSONL : `2b109de9aa69134e6e96d8494aded45406769a4c1e4a7cd42a6d809d77731122`.

### Passage complet v1

Version : `conversation-v1+v07-proposed`.

Période enregistrée : `2026-11-09T13:39:08.707307+00:00` à `2026-11-09T13:39:47.303318+00:00`.

Empreinte de contexte enregistrée : `bfc232e0964908d5252726fbeb97b8028c44481dbdcef985648a8cf16a6a28e7`.

SHA-256 du fichier JSONL : `4008e82ab1c58e39a6107571fc1361257b99d09563fd563b059b3dcda6412aee`.

### Passage complet v1.1

Version : `conversation-v1.1+v07-proposed`.

Période enregistrée : `2026-11-09T13:42:27.880489+00:00` à `2026-11-09T13:43:05.300642+00:00`.

Empreinte de contexte enregistrée : `bfc232e0964908d5252726fbeb97b8028c44481dbdcef985648a8cf16a6a28e7`.

SHA-256 du fichier JSONL : `573628b8c3a4f5bc19413b3946ce8c064d58d2a13f31ac38e360986f16ae873e`.

### Dernier passage v1.2

Version : `conversation-v1.2+v07-proposed`.

Période enregistrée : `2026-11-09T13:44:51.871266+00:00` à `2026-11-09T13:45:34.999253+00:00`.

Empreinte de contexte enregistrée : `c321c72fa966b1d13a0e29f1ac8fcd120daafe3859f02b75477a05682322487a`.

SHA-256 du fichier JSONL : `3e64f913ae685074e52b4be03f14932b334e345b99d14fb05e88d8ae57e85754`.

Pour v1.2, les deux textes système complets sont fournis. Leur concaténation individuel + collectif reproduit l'empreinte enregistrée. Elle couvre le prompt source, le complément applicatif et les ressources, pas les messages variables du scénario.

Pour v1 et v1.1, l'ancienne empreinte identique couvre seulement le prompt source et les ressources, sans les compléments applicatifs de ces versions. Leurs systèmes complets n'ont pas été archivés séparément au moment des appels ; ils ne sont pas reconstruits ou présentés comme vérifiés ici. Les transcriptions et leurs étiquettes de version restent exactes.

Référence du code conservé : commit applicatif `34c5b0e763b465740516f2dd2b8469b943df34d3`, suivi documentaire `a745bab18972913ba3e3e24b590341a1a1bc27af`. Aucune modification du moteur ou du prompt effectuée pour ce dossier.

## Dernier passage par scénario

| Scénario | Tours | Entrée | Sortie | Total tokens |
|---|---:|---:|---:|---:|
| M01 | 2 | 6 609 | 80 | 6 689 |
| M02 | 2 | 7 000 | 867 | 7 867 |
| M03 | 3 | 10 353 | 654 | 11 007 |
| M04 | 3 | 10 480 | 433 | 10 913 |
| M05 | 2 | 6 804 | 369 | 7 173 |
| M06 | 2 | 6 691 | 228 | 6 919 |
| M07 | 2 | 6 626 | 140 | 6 766 |
| M08 | 2 | 6 680 | 241 | 6 921 |
| M09 | 2 | 6 681 | 208 | 6 889 |
| M10 | 2 | 6 599 | 221 | 6 820 |
| M11 | 2 | 6 571 | 49 | 6 620 |
| M12 | 2 | 6 855 | 506 | 7 361 |

Les réponses sont exactes **au regard des JSONL conservés**. Le transport HTTP brut n'a pas été archivé ; le fournisseur applicatif retire les espaces de bord avant stockage. Aucun texte n'est corrigé ou réécrit dans ce dossier.
