# PTD Coach V2 · essai et passation

La V2 part de la [PR #16](https://github.com/bdelhomme/ptd-coach/pull/16) au commit
`629273f`. Les comptes, organismes, documents, dates de projet et dialogues de
recette sont fictifs. La bibliothèque reste en brouillon pédagogique.

## Lancer et essayer

Depuis le dépôt, sur Mac :

```sh
make bootstrap
CHAT_PROVIDER=mock .venv/bin/python -m ptd_coach --port 8790 --data-dir local-data/essai-v2
```

Ouvrir [la V2](http://127.0.0.1:8790/). En mode Mistral, conserver
`MISTRAL_API_KEY` uniquement dans `.env` ignoré par Git et lancer avec
`CHAT_PROVIDER=mistral`. Le modèle (`MISTRAL_MODEL`), la sortie
(`CHAT_MAX_TOKENS`), le délai (`CHAT_TIMEOUT_SECONDS`) et le budget
(`CHAT_MAX_CALLS`) restent configurables. Les bases V2 sont séparées.
`--ptd-v1` retrouve la démo de la PR #16, `--coach-historique` les contextes
de comparaison et `/historique-a2` le prototype simulé.

1. **Sans compte**, ouvrir Bibliothèque. Chercher Gantt ou filtrer par compétence.
   Ouvrir M08 puis passer par **Exemple travaillé**, **Modèle** (CSV) et
   **Approfondir** (limites, repères tuteur et références).
2. **Étudiant démo A**, mission d’étude de marché. Dans le coach d’équipe,
   écrire « Le recrutement prend du retard, comment ajuster notre planning ? ».
   Ouvrir M08 depuis le fil, puis le Gantt. Charger l’exemple, afficher la
   référence et passer la durée de **Recruter les ateliers** de 11 à 12 jours.
   Les entretiens deviennent incohérents avec leur prédécesseur. Déplacer leur
   début ou examiner un autre scénario, enregistrer, puis **Imprimer / PDF**.
   Revenir à la fiche, puis au même fil.
3. Ouvrir **Cahier des charges**. Charger le document fictif, renseigner la
   source de la référence et la figer. Modifier le périmètre puis enregistrer.
   Comparer les champs modifiés. Le registre des décisions distingue une
   demande ou une décision envisagée d’un arbitrage pris et sourcé.
4. Ouvrir un fil privé, puis **Faire relire un extrait fictif**. Charger
   l’extrait de la mission, vérifier la destination et consentir à son
   enregistrement dans ce fil et à l’envoi si Mistral est actif. Le mock
   illustre l’interaction. Mistral donne une revue expérimentale.
5. **Étudiant démo C**, mission de conseil technologique. Charger son exemple
   d’**Analyse multicritère**. Faire varier le poids de l’intégration de 60 à
   10 : les scores passent de 3,8/3,2 à 2,6/4,4. La conclusion dépend des
   préférences. Le second projet propose son propre cahier des charges,
   planning, extrait, calendrier et situations de faisabilité.
6. Essayer **RACI**, **Risques**, **Décisions** et **Calendrier de mission**.
   Le calendrier saisi s’affiche dans le projet. **Faire le point** propose
   des situations facultatives, sept pour A et huit pour C, indépendantes du
   calendrier. Ouvrir la vue tuteur pour retrouver les repères collectifs
   explicitement partagés. Les brouillons d’atelier sont réservés aux membres
   de l’équipe, y compris pendant la recette mobile.

## Architecture et arbitrages

- `pedagogy/library/methodes-v2.json` est la source canonique de 15 fiches.
  Elle contient définitions, démarche, tableaux d’exemples, modèle vierge,
  erreurs, limites, apprentissage, repères tuteur et références. Les sources
  distinguent guides professionnels et pratique documentée, par exemple les
  exigences contractuelles de planification de Crossrail. Les adaptations
  PTD ne constituent pas des preuves d’efficacité. La bibliothèque V0.1 et
  ses identifiants historiques restent intacts.
- `library_v2.py` sélectionne au plus une méthode par signaux lexicaux. Une
  relance courte peut reprendre le dernier tour étudiant. Les exemples
  complets, modèles et notes tuteurs ne sont pas injectés. Les identifiants
  sélectionnés, versions et empreintes figurent dans la trace d’invocation.
- `workbench.py` conserve un brouillon versionné par outil et par équipe.
  Le serveur résout l’identité depuis la session, refuse les tuteurs et
  contrôle les écritures concurrentes. Après conflit, le navigateur préserve
  le brouillon local jusqu’au choix explicite de charger la version enregistrée.
  La référence du cahier des charges est immuable et porte une source. Elle
  ne certifie pas un accord du commanditaire. La revue ciblée exige la
  confirmation du caractère fictif côté serveur. Aucun document ni brouillon
  de l’atelier n’est injecté automatiquement.
- Le Gantt utilise des jours calendaires et des liens fin-début, sans
  réordonnancement automatique. Les dates incohérentes sont signalées et les
  cycles rejetés. Pas de calcul de charge, de chemin critique ni de jours
  ouvrés. Le rendu natif évite une dépendance graphique. La matrice suppose une
  échelle commune de 0 à 5 et compare seulement les options renseignées sur
  les critères pondérés. L’analyse fait varier un poids à la fois.
- Les espaces, la confirmation et la révocation de D-039 restent en place.
  La revue d’extrait utilise le fil sélectionné et les mêmes droits. Sur les
  prochains tours du même fil, l’extrait fait partie de son historique. Aucun
  import de fichier, aucune donnée réelle et aucun déploiement institutionnel.

## Revue et recette

Le Gantt et les autres formulaires ont été confiés successivement à deux
agents sur des contrats bornés. Une revue indépendante avec raisonnement élevé
a contrôlé le périmètre des brouillons, la frontière d’envoi des extraits et
les règles du Gantt. Elle a trouvé un blocage de reprise après conflit et une
ambiguïté de format de date : rechargement explicite et validation stricte
ont été ajoutés. Elle a comparé les avertissements JavaScript et Python sur
162 combinaisons et trouvé les mêmes résultats.

Le parcours dans le navigateur a été vérifié avec le mock : recommandation
M08, exemple, conflit de dépendance, sauvegarde et retour au fil, référence du
cahier des charges, revue d’extrait, calendrier et inversion d’ordre dans la
matrice. Deux onglets ont confirmé qu’un enregistrement concurrent est détecté
sans effacer le texte local. La revue visuelle a comparé le catalogue, une fiche et le diagramme
à 1 280 px et à 390 px, avec défilement interne pour les tableaux. L’agent Gantt
a exercé l’impression PDF. Le test mobile a été fait en émulation.

Les 162 tests locaux passent hors lecture du jeu réservé. Les tests automatisés
couvrent le catalogue et les onze compétences, le Gantt,
la séparation des équipes, les autorisations, les conflits de version,
la conservation de la référence et la frontière avec le fournisseur. La recette
Mistral et ses défauts sont documentés avec les [verbatims et métriques](../pedagogy/evaluations/ptd-v2-demo/README.md).

À poursuivre : validation humaine des fiches, essai de transfert des méthodes,
lecture des preuves et des sources plus approfondie, couverture réelle sur
l’ensemble des compétences et recette sur téléphone physique. Les fiches
spécifiques sur l’animation de réunion, le PDCA, l’évaluation des sources et
la faisabilité restent à approfondir. Le [dossier
pilote](CHECKLIST_PILOTE_PTD.md) s’applique toujours.
