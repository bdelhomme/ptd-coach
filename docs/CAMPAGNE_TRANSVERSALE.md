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

## Résultats du premier passage

Le passage du 11 novembre 2026 a produit **36 réponses réelles** sur les six
cas annoncés, sans erreur API. Les trois variantes ont demandé et reçu
l’alias `mistral-small-latest`. Le plafond est resté à 700 tokens.

| Contexte | Réponses | Entrée | Sortie | Total tokens | Caractères | Latence médiane | Tronquées |
|---|---:|---:|---:|---:|---:|---:|---:|
| V0.7 | 12 | 41 596 | 3 123 | 44 719 | 12 569 | 2 294 ms | 1 |
| c1 | 12 | 20 698 | 5 746 | 26 444 | 22 657 | 4 394 ms | 6 |
| c2 | 12 | 16 388 | 2 226 | 18 614 | 8 793 | 1 |

Total **89 777 tokens**. Le [dossier de revue](../pedagogy/evaluations/transversale/README.md)
donne les sorties, les messages exacts, les mesures, la clé des variantes
et les grilles vierges. La [lecture de développement](../pedagogy/evaluations/transversale/OBSERVATIONS.md)
cite les tours à examiner. L’échantillon sollicite dix codes. Les tâches A2
directes restent dans le jeu de 24 cas et dans les anciennes traces. Ce choix
d’échantillonnage répond au déséquilibre initial.

Le cahier des charges est le défaut commun le plus net. Les trois réponses
du premier tour de TX07 ajoutent des fonctionnalités, contraintes ou seuils
que l’étudiant n’a pas établis. Les trois atteignent le plafond de sortie.
Les deux versions c1/c2 ajoutent encore l’identité de l’emprunteur au second
tour. TX05 montre aussi que préserver un accord conditionnel et chiffrer la
faisabilité sont deux tâches différentes. TX18 contient un exemple de
prescription spontanée utile lorsque les versions proposent une comparaison
à distance fixe. Les trois variantes généralisent dans TX22 au-delà des trois
volontaires. Le comparatif éclaire des priorités de conception. Le verdict
pédagogique indépendant reste ouvert.

## Recommandations pour une éventuelle prochaine candidate

1. **Rendre les statuts du cahier des charges explicites.** Partir d’un fait
   rapporté, montrer une seule exigence provisoire et son contrôle. Faire
   valider les seuils, la collecte et les engagements. TX07 montre que
   la mention « brouillon » ne suffit pas à empêcher une invention.
2. **Aider d’abord sur la décision concrète.** En TX05, reformuler les
   deux options et la condition de confirmation avant de détailler les
   fonctionnalités. En TX14, donner une formulation immédiatement utile
   et préserver l’accord du groupe sur l’unité.
3. **Enseigner une démarche à la taille du problème.** En TX18, proposer
   un essai court avec une mesure comparable et dire ce qu’il permet
   d’observer. En TX22, relier les observations à une affirmation de portée
   limitée et à la prochaine question, que l’étudiant doit pouvoir expliquer.
4. **Éprouver le choix des ressources.** Prioriser les fiches commanditaire,
   exigences et changement pour une relecture par des encadrants. Comparer
   ensuite leur apport sur des formulations naturelles et des tours
   suivants. L’audit montre 24 tours client/exigences sans fiche sélectionnée
   par c1/c2. Une intervention directe reste une option utile.
5. **Arbitrer sur des cas divergents.** Faire lire les mêmes réponses à deux
   lecteurs, relever les incidents séparément et discuter les désaccords.
   Les 18 autres cas de développement fournissent des situations de
   confirmation et de mise en difficulté. Réserver la mesure de transfert
   à une activité distincte, avec des preuves produites sans aide.

Ces recommandations restent à arbitrer avec le porteur. Les choix de
formulation, seuils, ressources et critères de passage vers une future
candidate demandent une décision fondée sur les exemples et la revue.
Aucune candidate nouvelle n’a été développée dans cette tranche.

## Passation

L’assistant intégrateur a produit cette tranche sans nouvelle délégation.
Le jeu, le rapport de plan et le banc ont été engagés localement dans
`a61c5d5` avant le premier appel réel. Le banc a réutilisé le service et les
contextes figés. La phase locale initiale a passé 113 tests hors API avant
le passage réel. Deux anciens tests qui ouvrent la réserve ont été filtrés
pour cette exécution locale, ainsi que ce fichier au contrôle documentaire.
Les tests HTTP ont été exécutés sur localhost avec la permission réseau
de la session. Les contrôles automatiques de CI préexistants gardent leur
portée de syntaxe et d’intégrité, sans afficher les scénarios réservés.

Après archivage, **114 tests locaux** ont réussi dans le même périmètre,
dont le contrôle des empreintes, des 36 requêtes et réponses exactes et
des grilles vierges. Le contrôle documentaire porte sur 196 fichiers
hors jeu réservé. Les cinq artefacts produits par le passage ont été
comparés octet pour octet aux copies publiées. La différence Git des
contextes, gels, corpus antérieurs, ressources, référentiel et code
applicatif est vide par rapport à la base.

La clé est restée dans la configuration locale ignorée. Les jeux, artefacts
et permissions du service historiques sont conservés. Le premier passage
est terminé. La suite utile consiste à faire relire les verbatim à l’aide
de la grille, puis à arbitrer les fiches et les hypothèses avant de changer
un contexte. La PR est dédiée à l’évaluation et à la documentation.
