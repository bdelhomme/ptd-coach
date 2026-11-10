# Journal d'exécution c2 — passation reproductible

11 novembre 2026, heure de Paris. Opérateur : assistant intégrateur du chat courant.
Aucune nouvelle délégation ; l’agent qui avait créé le réservé n’est pas consulté.
Ce journal expose actions, arbitrages et preuves, pas un raisonnement interne.

## Séquence exécutée

1. Dépôt propre sur `d01b56a`, synchronisation distante ; PR #4 à #7 ouvertes,
   création de `feat/v08-candidate2` depuis la branche #7. Socle : 96 tests passent.
2. Lecture du retour qualitatif du porteur, décisions et contrat ; vérifications
   publiques PMI/Microsoft/APM consignées dans la relecture conceptuelle.
3. Nouveaux prompt, fiche et contexte, sans toucher au moteur gelé, à l'interface,
   aux anciens contextes ou à la réserve. Relecture des exemples avant usage.
4. Gel c2 SHA-256 `1fdd717ec1af511f4171313f547ae8a2604d82c8c2e348e7eb8915457d715012` ;
   13 tests ciblés puis 109 au total, 96 lignes dry-run et 96 réponses mock.
5. Commit `fe47d189f915406fca50de547316e84219c5444a`, branche publiée, PR #8 ouverte
   avant premier appel réel. Aucun réglage payant en CI.
6. Premier essai 18 réponses : aucune erreur API, mais erreurs WBS et relances
   encore présentes. Diagnostic étendu dans le périmètre annoncé, sans corriger c2.
7. Sondes 18 réponses, garde-fous 12 et répétition 6. Aucune erreur API ; total
   54 réponses et 132 977 tokens. Arrêt des appels à ce budget, aucun essai réservé.
8. Verbatim/messages exacts publiables, observations séparées, grilles vierges.
   Nouveaux tests de provenance et fidélité : **111 tests réussis**, 181 fichiers
   suivis contrôlés, diff sans erreur. Clé exacte absente de tous les fichiers
   suivis ; recherche de coordonnées/chemins locaux sans signal dans les changements.
   53 fichiers historiques vérifiés identiques ; ancien réservé/référentiel par
   empreinte seulement, lignes D-001 à D-029 préservées. Pas d'audit exhaustif revendiqué.

## Rejouer les quatre passages (payants)

Utiliser un nouveau dossier à chaque essai, `.env` ignoré, modèle configuré
`mistral-small-latest`, `CHAT_MAX_TOKENS=700`. Le contexte est figé : un changement
exige une nouvelle version. Ces commandes consomment au maximum 54 appels si les
quatre passages réussissent ; arrêter au premier échec, ne pas relancer aveuglément.

```bash
.venv/bin/python scripts/compare_conversation_c2.py --provider mistral --allow-billable --case D03 --case D09 --max-calls 18 --output-dir local-data/c2-first-new
.venv/bin/python scripts/compare_conversation_c2.py --provider mistral --allow-billable --suite pedagogy/qa/COACH_CONCEPT_CASES_C2.json --max-calls 18 --output-dir local-data/c2-concepts-new
.venv/bin/python scripts/compare_conversation_c2.py --provider mistral --allow-billable --suite pedagogy/qa/COACH_MULTI_TURN_CASES_V07.json --variant c2 --case M06 --case M07 --case M08 --case M09 --case M10 --case M11 --max-calls 12 --output-dir local-data/c2-safety-new
.venv/bin/python scripts/compare_conversation_c2.py --provider mistral --allow-billable --case D03 --case D09 --variant c2 --repetition 1 --max-calls 6 --output-dir local-data/c2-repeat-new
```

Les dossiers locaux réels portent les mêmes noms sans `-new`. Le corpus public
est dans [v08-c2-comparison](../pedagogy/evaluations/v08-c2-comparison/README.md),
quatre sous-dossiers numérotés. Les JSONL portent suite, variante, répétition,
modèle, paramètres, empreintes et messages exacts. L'indice de répétition sert
à l'ordre ; ce n'est pas une graine aléatoire ni une garantie de reproductibilité.
La clé A/B/C est aléatoire et séparée ; les verbatim ne sont jamais reformulés.

## État à reprendre

[Rapport](V08_C2_REPORT.md) et [observations](../pedagogy/evaluations/v08-c2-comparison/OBSERVATIONS.md).
C2 non retenue pour adoption : améliorations locales sur certaines sondes,
mais erreurs WBS, clôture et réponses sensibles encore insuffisantes. Le service
n'a réalisé aucune action métier et ses tests d'autorisations passent. Le
navigateur continue de proposer V0.7/c1 ; aucune nouvelle fonction ni fusion.
Avant une future candidate distincte, définir une hypothèse corrigeant ces
échecs sur développement. La réserve reste à part, sans outil d'ouverture c2.
Une revue humaine peut remplir les grilles ; l'assistant ne l'a pas remplacée.
