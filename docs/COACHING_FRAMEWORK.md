# Cadre de conception — coaching, ressources et auto-positionnement

## Mise à jour applicative — étape 2, D-026

Le premier coach Mistral local est désormais développé dans un service séparé
avec historique multi-tours, ressources et mesure des tokens, sans modifier A2
ou le candidat V0.3. La demande du porteur succède au report historique D-025.
Les détails pédagogiques V0.6/V0.7 restent proposés ; aucune validation
institutionnelle n'est déduite du code. Voir [le guide d'essai](TRY_CONVERSATION_COACH.md),
[le rapport de recette](CONVERSATION_COACH_REPORT.md) et
[ADR-0007](adr/0007-local-conversation-mistral.md).
Les mentions de non-implémentation ci-dessous décrivent les cadrages antérieurs.


## Complément de conception V0.6/V0.7 — 2026-11-09

Le [noyau V0.6](PTD_PEDAGOGICAL_KERNEL_V06.md) articule les situations de
projet, la coopération et l'apprentissage individuel ; la
[politique V0.6](PTD_CONVERSATION_POLICY_V06.md) propose des interventions
souples, ressources directes et arrêt possible. La
[recette V0.7](COACH_DIALOGUE_EVALUATION_V07.md) prépare une évaluation humaine
des réponses. Ces contenus et les trois ressources R01–R03 sont **PROPOSÉS**,
non validés institutionnellement. E1–E4 sont analytiques, le candidat V0.3 est
conservé. Il ne s'agit ni de fonctions implémentées ni d'une nouvelle échelle
étudiante. D-025 reporte le nouveau coach Mistral ; voir
[l'intégration](INTEGRATION_V06_V07.md) pour le périmètre et les écarts.

Date : **2026-11-06**. Principes de conception confirmés par le porteur :
D-020/D-021/D-022. Les modalités décrites comme **PROPOSÉES** restent à discuter.
Les onze compétences de `candidate-v0.3.json` sont toujours candidates, sans
validation scientifique ou institutionnelle présumée.

**Complément de méthode du 2026-11-06** : le porteur demande un ancrage dans des
ouvrages/travaux et une vue globale avant le détail isolé d'A2. Voir
[les fondements préparatoires](PROJECT_MANAGEMENT_FOUNDATIONS.md), R-006 et D-024.
Les fiches ci-dessous doivent être articulées à cette vue d'ensemble ; aucun
corpus ou découpage nouveau n'est adopté automatiquement.

## Pourquoi ce cadrage devient prioritaire

Le premier prototype A2 a permis de tester un parcours, la persistance et les
frontières de confidentialité. Après une amélioration de lisibilité de l'interface,
le porteur a questionné la pertinence des exercices d'apprentissage eux-mêmes.
La suite consiste à définir comment accompagner la progression pour chaque
compétence avant de produire davantage d'exercices ou d'écrans.

Ce document consigne la réflexion ; il ne décrit pas des fonctionnalités déjà
implémentées. Le prototype reste un démonstrateur technique à données fictives.

## 1. Posture d'accompagnement

**Principe confirmé** : aider l'étudiant à comprendre, examiner et agir sans
prendre en charge à sa place les choix et apprentissages visés. Donner des
explications et des ressources fait partie de l'aide ; le coach peut expliquer
directement une méthode lorsque le besoin s'en fait sentir.

**Formulation étudiante proposée** :

> Le coach vous aide à comprendre, à explorer des possibilités et à examiner votre
> travail. Vous gardez la responsabilité de vos choix, de vos actions et de vos conclusions.

**Modalités proposées** : partir d'une difficulté ou d'une expérience de projet,
faire expliciter une proposition, poser une question principale à la fois,
apporter un repère, examiner plusieurs possibilités, préparer une expérimentation
choisie par l'étudiant, puis aider à distinguer faits rapportés et interprétations.

L'exercice est une intervention possible, au même titre qu'une explication,
un exemple fictif commenté, une simulation, l'analyse d'une trace ou un débrief.
Il n'est pas présumé nécessaire à chaque séance ou pour toute compétence.
Les indications ne doivent pas transformer l'accès à une explication en une
épreuve préalable obligatoire. Une séance peut reprendre une difficulté antérieure.

### Limites d'aide à préciser dans chaque fiche

| Le coach peut proposer | Travail intellectuel et décisions laissés à l'étudiant |
|---|---|
| Une méthode et une ressource courte | Comprendre leur pertinence pour sa situation |
| Un exemple travaillé sur une situation fictive | Construire et justifier une réponse pour son projet |
| Des questions, incohérences à examiner, pistes alternatives | Choisir, décider avec les personnes concernées et expérimenter |
| Une aide à la relecture ou à l'expression d'une idée | Assumer le sens et la justification du contenu produit |

Cette frontière n'est pas une interdiction générale de l'assistance rédactionnelle.
Elle doit protéger le raisonnement visé dans la tâche, sans laisser l'étudiant
sans aide. Le coach ne confirme pas une décision collective au nom du groupe et
n'attribue pas de note, de niveau institutionnel ou de profil psychologique.
La procédure de recours à l'encadrant humain reste à spécifier.

## 2. Ressources

**Principe confirmé** : proposer des ressources utiles à la progression.

**Organisation proposée** : ressources courtes, accessibles à la demande et liées
au besoin rencontré ; fiche méthode, exemple fictif commenté, grille de questions,
puis référence pour approfondir lorsque pertinent. Le coach peut aussi proposer
une ressource en expliquant à quel besoin elle répond, sans l'imposer systématiquement.

Une fiche de coaching doit préciser le rôle de la ressource, le moment possible
de mobilisation, ce qu'elle explique et le travail qui reste à l'étudiant.
Le catalogue, les sources exactes, les droits de réutilisation, l'accessibilité,
les versions et la relecture pédagogique restent **À DÉCIDER**.
Ne pas ajouter les documents institutionnels originaux à Git sans autorisation.

## 3. Aide au positionnement

**Principe confirmé** : aider l'étudiant à identifier les compétences à travailler,
à choisir une priorité et à revenir sur sa progression. Le positionnement reste
formatif, privé et compatible avec D-009/D-012. Il ne remplace pas les grilles
institutionnelles ou le jugement des encadrants.

**Modalités proposées, non validées comme échelle** :

1. Décrire quelques capacités concrètes pour chaque compétence candidate.
2. Faire exprimer le ressenti de l'étudiant face à ces capacités.
3. Chercher une expérience précise à raconter ou une trace qu'il choisit d'examiner.
4. Relier ce qu'il souhaite mieux réussir à une situation actuelle du PTD.
5. Proposer une priorité que l'étudiant peut confirmer, modifier ou écarter.
6. Reprendre ce positionnement après une expérience pour examiner ce qui a changé.

Questions illustratives : « Comment vous sentez-vous pour le faire ? »,
« Avez-vous une expérience précise à raconter ? »,
« Qu'aimeriez-vous mieux réussir dans votre projet actuel ? ».

Le ressenti et les éléments disponibles sont distingués : l'absence d'exemple
signifie qu'on manque d'éléments, pas que la compétence est faible.
Une seule réponse, le volume de messages ou une expérience rapportée ne suffisent
pas à certifier une compétence. Aucune échelle chiffrée ou à quatre niveaux n'est
adoptée par ces échanges. Éviter le classement et la comparaison entre étudiants.

Les données de positionnement restent dans le domaine privé individuel : mêmes
restrictions backend, contexte IA, recherche, exports et droits d'accès que les
réflexions privées. Un éventuel partage doit porter sur un objet sélectionné et
un destinataire explicitement confirmé ; aucun accès tuteur/coordination implicite.
La modélisation et les routes correspondantes restent à spécifier.

## 4. Fiche de coaching par compétence — structure proposée

| Rubrique | Ce qu'il faut expliciter avec le porteur et les encadrants |
|---|---|
| Compétence et version | Référence candidate, sans renommer silencieusement les labels |
| Capacités observables | Ce que l'étudiant pourrait faire ou expliquer en situation |
| Situations PTD | Moments où cette capacité devient utile |
| Positionnement | Questions de ressenti, expériences disponibles, incertitudes |
| Difficultés possibles | Obstacles concrets à examiner, sans diagnostic de personnalité |
| Interventions du coach | Questions, explications, ressources, exemples ou simulations possibles |
| Limites d'aide | Ce que l'IA apporte et ce qui doit rester à construire/décider par l'étudiant |
| Expérimentation | Action choisie dans l'équipe et observation recherchée |
| Retour et repositionnement | Faits rapportés, interprétations, leçons et prochaine priorité |
| Ressources | Besoin traité, provenance, droits, version et statut de relecture |
| Intervention humaine | Situations nécessitant le concours de l'encadrant |
| Statut | Brouillon, points discutés avec le porteur, relecture encadrant, questions ouvertes |

Les onze fiches ne sont pas encore rédigées ou approuvées.

### Illustration A2 — proposition à examiner

Compétence candidate conservée : **Structurer et planifier le projet**.
Capacités illustratives, **PROPOSÉES** : découper un objectif en tâches ; repérer
les dépendances et validations ; adapter un planning lorsqu'une contrainte change.

Exemple de départ : « Dans votre planning, quelle tâche vous semble la plus
incertaine aujourd'hui ? ». Selon la réponse, le coach pourrait faire préciser
une dépendance, apporter une courte explication et un exemple fictif, puis aider
l'étudiant à choisir une action. L'étudiant construit son organisation, l'essaie
et examine ensuite ce qui s'est passé. Cette illustration ne constitue ni la
fiche A2 définitive, ni un exercice obligatoire, ni une grille de validation.

## 5. Parcours envisagé et impact sur le prototype

Enchaînement **PROPOSÉ** :

`Me situer → choisir une priorité → trouver des repères → essayer → faire le point → me repositionner`.

Il s'agit d'une logique d'accompagnement à discuter, pas d'une nouvelle machine à
états adoptée. L'interface, les contrats, les schémas et les données versionnés ne
sont pas modifiés automatiquement à partir de ce document.
Les ressources et le positionnement ne sont pas encore implémentés dans la démo.

Le nombre d'objectifs actifs reste une proposition (D-016), les douze rubriques
de fiche et les capacités A2 restent proposées. La conception doit préserver
l'autonomie de l'étudiant et éviter l'ajout systématique de devoirs.

## Suite immédiate

Traiter [le ticket 003](tickets/003-coaching-design.md) : discuter d'abord un cadre
global sourcé, le relier aux situations et objectifs PTD et vérifier l'articulation
des compétences candidates. En déduire ensuite les fiches, leurs limites d'aide et
ressources. Définir les critères de relecture et changements applicatifs seulement
après accord sur le cadrage concerné.
Historique et décisions : [journal](REFLECTION_LOG.md), [registre](DECISIONS.md).
