# Campagne d’évaluation pédagogique transversale

Décision D-031 · 11 novembre 2026 · branche `eval/campagne-transversale` depuis
`df80557`, branche de la PR #8. Le porteur demande d’étudier l’aide
méthodologique et l’autonomie accompagnée sur les onze compétences candidates.
V0.7, c1, c2, leurs gels et preuves servent de comparateurs. Le référentiel
V0.3 reste la base des codes de compétence. Les activités sont fictives.

- [Cartographie des essais antérieurs](CARTOGRAPHIE_TRANSVERSALE.md).
- [Jeu de développement de 24 cas](../pedagogy/qa/COACH_TRANSVERSAL_DEV_CASES.json).
- [Grille de revue](../pedagogy/evaluations/transversale/GRILLE.md).
- [Audit et fiches proposées](AUDIT_RESSOURCES_TRANSVERSALES.md).

## Lacunes sur le commanditaire et le cahier des charges

Les traces historiques de M05 éprouvent un conseil avant entretien et une
vérification rapide du besoin. D02 et D07 travaillent en simulation technique
l’accord et l’objection. On dispose de peu d’observations sur une demande qui
se précise après confrontation à un usage, sur la négociation de ce que l’équipe
peut réellement rendre ou sur une décision avec plusieurs parties concernées.

La production et la relecture d’un cahier des charges exigent des opérations
distinctes. Partir d’un besoin attesté, distinguer une solution suggérée et une
contrainte, écrire une exigence vérifiable, confronter des demandes incompatibles,
vérifier ce qui est faisable, tracer la source et faire confirmer le statut.
L’aide légitime peut inclure une ligne déjà rédigée à partir de faits, un exemple
complet fictif ou une critique. Le test vérifie qui recueille la preuve, justifie
le choix et confirme l’accord.

TX01–TX06 couvrent découverte, entretien, indisponibilité, attentes opposées,
changement et objection. TX07–TX12 couvrent le brouillon, la distinction
besoin/solution/contrainte, les parties prenantes absentes, la faisabilité,
les contradictions et la relecture. TX13–TX24 croisent coordination, décisions,
pilotage, recherche de preuves, restitution et réflexivité. Chaque cas indique
le travail intellectuel à laisser à l’étudiant ou à l’équipe. Les continuations
sont fixées pour comparer les variantes et réintroduisent un fait, une erreur,
une demande de formulation ou une limite de temps.

## Premier passage prévu avant consultation des réponses

| Cas | Diagnostic ou aide attendue | Cadre |
|---|---|---|
| TX01 | Clarifier la demande d’écran et reformuler le besoin provisoire | Individuel |
| TX05 | Proposer un examen d’impact et préserver l’accord conditionnel | Collectif |
| TX07 | Aider à construire le cahier des charges à partir des éléments disponibles | Collectif |
| TX14 | Préparer une phrase de coopération sous contrainte de temps | Individuel |
| TX18 | Proposer un essai bref pour éclairer un choix de réglage | Collectif |
| TX22 | Aider à argumenter une diapositive et s’approprier la justification | Individuel |

Six cas, deux tours et trois variantes donnent **36 tentatives Mistral au
maximum**. Trois cas concernent le commanditaire ou les exigences et les cinq
domaines apparaissent. Chaque cas démarre avec un historique vide et un espace
individuel ou collectif synthétique. La rotation des variantes donne deux cas
à chaque version dans chacune des trois positions. Même configuration de modèle,
température 0,2 et plafond 700 tokens. Le banc conserve les erreurs et leur
durée si le fournisseur échoue, et interrompt le passage au premier échec
sans nouvel appel automatique. Le jeu réservé demeure hors de la campagne.

Les mesures décrivent les réponses produites et leur coût en tokens. Un alias
de modèle peut évoluer. Deux tours préécrits peuvent donner des contextes
différents après la première réponse. Le faible échantillon ne couvre pas tous
les cas de la batterie. Les grilles indépendantes sont à remplir après lecture
des sorties exactes.

## Commandes et contrôles

Depuis la racine du dépôt, avec Python de l’environnement de travail.

```bash
.venv/bin/python scripts/run_transversal_eval.py --provider dry-run --output-dir local-data/transversale-dry-nouveau
.venv/bin/python scripts/run_transversal_eval.py --provider mock --output-dir local-data/transversale-mock-nouveau
.venv/bin/python scripts/run_transversal_eval.py --provider mistral --allow-billable --output-dir local-data/transversale-reel-nouveau
```

Les deux premières commandes ont été exécutées avec les 24 cas. Le dry-run
a produit 144 lignes de plan sans réponses. Le mock a produit 144 réponses
fixes, 48 par contexte. Les tests couvrent la répartition, les onze codes,
les messages exacts, l’absence de critères de correction dans le contexte,
les historiques isolés, la grille vierge et le plafond d’appels.

Le script ouvre uniquement le jeu canonique de la campagne et vérifie le gel
c2 et le gel c1. La clé reste en environnement serveur. Les appels passent par
le service de conversation existant, qui conserve les contrôles de périmètre.

## Résultats et décisions

La campagne rend les réponses exactes disponibles pour une revue qualitative.
Le rapport de résultats et les observations de développement seront ajoutés
après le passage réel. Les recommandations restent des hypothèses de travail
pour une prochaine décision du porteur.
