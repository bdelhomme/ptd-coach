# Outils expérimentaux V0.7 — mode d'emploi de l'intégration

**PROPOSÉ ; données fictives uniquement ; aucune réponse IA générée pour ce lot.**
Références : D-025, [protocole de dialogue](COACH_DIALOGUE_EVALUATION_V07.md).
Ces scripts fournis dans l'archive restent indépendants de l'application A2.
Ils ne constituent ni un coach développé ni un contrôle d'accès.

## Vérifier sans réseau ni clé

Depuis la racine, avec Python 3.9+ et la bibliothèque standard :

```sh
make verify
.venv/bin/python -m unittest discover -s tests -p 'test_eval_v07.py' -v
.venv/bin/python scripts/run_coach_eval_v07.py --provider dry-run --output /tmp/ptd-v07-dry.jsonl
.venv/bin/python scripts/run_coach_eval_v07.py --provider dry-run --suite pedagogy/qa/COACH_ACCEPTANCE_CASES_V06.json --output /tmp/ptd-v06-dry.jsonl
```

Résultats attendus : V0.7 = 12 cas et 26 enregistrements, V0.6 = 20 cas et
20 enregistrements. Chaque ligne est un objet JSON avec `suite`, `case_id`,
`turn`, `scope`, `provider: dry-run`, `status: not_called`, `response: null`,
date UTC, version de prompt et critères destinés à la relecture humaine.
Ces critères ne sont pas envoyés au modèle dans le chemin expérimental fourni.
Chaque cas dispose d'un historique distinct ; les tours conservent les réponses
précédentes uniquement lorsqu'elles ont réellement été générées.

`--case M03` sélectionne un cas ; `--max-cases 1` limite le nombre de cas,
pas le nombre de tours. `--resource-dir pedagogy/resources` charge les trois
brouillons R01–R03 dans le contexte de recette ; aucune mémoire privée.

Les sorties doivent rester hors Git (`local-data/` ignoré ou dossier temporaire).
Aucun script ne vérifie la réalité du caractère fictif au-delà de l'étiquette
`synthetic_only` : la préparation du corpus demeure une responsabilité humaine.
Le dry-run n'est pas une simulation de réponse et n'alimente pas la démo A2.

## Relecture humaine — après une future expérience autorisée

Le script `review_coach_eval_v07.py sheet` prépare un CSV seulement si tous les
enregistrements fournis portent `status: model_called`. Les entrées vides,
dry-run ou en erreur sont refusées. Les tests utilisent des réponses fabriquées
en mémoire, jamais une API. Les cinq dimensions et le veto restent à remplir
par un lecteur humain ; les cases vides donnent `REVIEW_INCOMPLETE`.

Le résumé calcule le seuil proposé uniquement sur les lignes de la feuille :
il ne garantit ni la couverture de toute la suite d'origine, ni l'indépendance
des lecteurs. Conserver les entrées, comparer les IDs/tours à la sélection
prévue et vérifier l'intégralité avant toute conclusion. Un veto renseigné
est compté même si les autres notes sont encore vides.

## Limites et étape 2

Le code d'appel Mistral **déjà fourni** est importé sans raccordement à
`ptd_coach/` ou `web/`. Son exécution et le développement du nouveau coach
restent reportés par D-025. Aucun appel facturable, clé ou modèle testé ici.
Une future recette devra notamment fixer la version réelle du modèle, conserver
l'empreinte du prompt/des ressources, les paramètres, les erreurs et la
couverture des cas ; le seul label `v0.7-proposed` n'assure pas cette reproductibilité.
Un code de sortie CLI réussi ne suffit pas à conclure : contrôler les statuts
JSONL et les cas attendus avant relecture, notamment en présence d'erreurs API.
Voir [ADR-0006](adr/0006-dialogue-evaluation-compatibility.md) et les tickets
[004](tickets/004-conversation-router.md)/[005](tickets/005-backend-boundaries.md).
