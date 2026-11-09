# PTD Coach V0.6 — noyau pédagogique et théorie d'action

**Statut : PROPOSÉ (version du 07/11/2026).** Les principes généraux ci-dessous réexpriment des orientations approuvées par le porteur ; les architectures fines, critères et scénarios restent à éprouver. Conserver `candidate-v0.3.json` intact.

## 1. Le problème précis à résoudre

Le PTD génère simultanément (a) une réponse pour un commanditaire, (b) une activité collective de sept étudiants et (c) des occasions d'acquisition individuelle. Ces trois résultats ne sont pas interchangeables. Un groupe peut livrer un excellent projet avec une faible participation de certains membres ; un étudiant peut déclarer avoir bien coopéré sans que ce comportement ait été observé. Le succès d'un chatbot se distingue encore de ces trois résultats.

**Question de conception** : comment aider chaque étudiant à mobiliser des concepts et comportements de management de projet dans ses situations PTD, puis à en tirer un apprentissage réutilisable, tout en soutenant le fonctionnement du groupe ?

PTD Coach est un **médiateur d'apprentissage**, pas un chef de projet algorithmique, un dispositif de surveillance ou un évaluateur institutionnel.

## 2. Théorie d'action — hypothèses explicitement vérifiables

| Déclencheur / intervention | Mécanisme visé | Signe immédiat d'utilité | Preuve d'apprentissage plus robuste | Biais/risque |
|---|---|---|---|---|
| Besoin de méthode → ressource contextualisée | Rendre une pratique intelligible | L'étudiant comprend le concept et sait expliquer sa pertinence | Résout une situation nouvelle **sans IA** | Répète un texte sans compréhension |
| Blocage de projet → clarification et analyse des options | Enrichir raisonnement et jugement de situation | Formule critères, contraintes, incertitudes | Choisit et justifie une action pertinente dans le PTD | L'IA prend la décision pour lui |
| Expérience vécue → courte réflexivité factuelle | Transformer l'expérience en hypothèses et ajustements | Distingue observation, attribution et alternative | Réinvestit une amélioration puis revient sur son effet | Rationalisation a posteriori |
| Objectif choisi → accompagnement longitudinal | Soutenir l'autorégulation et l'initiative | Objectif observable, occasion et signe d'action choisis | Capacité démontrée dans un autre contexte, sans coaching | Dépendance et inflation d'objectifs |
| Difficulté de fonctionnement collectif → débrief d'équipe | Construire une compréhension et une adaptation communes | Une règle ou action est discutée puis validée par les humains | Processus collectif évolue de façon observable | Fausse harmonie, mise en cause de personnes |

**Attention :** l'effet propre de chacune de ces interventions avec un LLM/Mistral n'est pas établi. L'évaluation doit examiner aussi les effets nuls et négatifs.

## 3. Architecture du référentiel — sans remplacer les 11 codes

### A. Conduire le projet (situations : cadrer → construire → piloter)
- **A1** Analyser et reformuler une demande : écoute client, exigences, questionnement, critères de réussite, reformulation validée.
- **A2** Structurer et planifier : livrables/tâches, enchaînements, dépendances, contraintes, jalons, marges et révision.
- **A3** Piloter et adapter : constater les écarts, expliciter les risques, arbitrer, adapter avec justification.
- **C1** Résoudre un problème complexe : définir le problème, comparer hypothèses/solutions, évaluer preuves/incertitudes.

### B. Agir efficacement dans une équipe (situations : coopérer → décider → réguler)
Le regroupement **E1–E4 est une grille analytique**, non quatre nouveaux codes du référentiel.

| Capacités de travail en équipe | Dimensions CATME éclairantes (non reproduction d'échelle) | Codes actuels reliés | Exemple observable dans un PTD |
|---|---|---|---|
| **E1 Contribuer, aider, apprendre pour contribuer** | Contribute; Relevant KSA; Expecting quality | B1, C1 | Prévenir un retard, fournir une contribution de qualité, aider sans remplacer |
| **E2 Coordonner des travaux interdépendants** | Keeping on track; Contribute | B1, A2, A3 | Rendre visibles les dépendances, dates et versions, identifier une interface de travail |
| **E3 Communiquer, écouter et construire une décision** | Interacting; Keeping on track | B2 | Reformuler une objection, confronter des arguments, expliciter un arbitrage |
| **E4 Réguler le fonctionnement collectif et exercer un leadership distribué** | Interacting; Keeping on track; Expecting quality | B3, B2 | Proposer un retour d'expérience, favoriser la parole, faire évoluer une règle commune |

**Correction nécessaire de la première V0.4 :** CATME ne se résume pas à l'entraide et à la communication ; la contribution technique, le souci de la qualité et la mobilisation de savoirs pertinents doivent rester visibles. Ne pas recopier ses échelles ou attribuer à CATME les formulations E1–E4. La revue du CDIO 3.0 met aussi en lumière les perspectives diverses, l'inclusion et le travail interdisciplinaire dans le PTD.

### C. Agir en situation professionnelle
- **C2** Intégrer les enjeux, responsabilités, impacts et limites d'une solution.
- **D1** Interagir avec le commanditaire/parties prenantes et négocier la compréhension du besoin.
- **D3** Restituer une réponse intelligible, argumentée et adaptée au destinataire.

### D. Capacité d'apprentissage transversale
- **D2** Analyser une expérience pour progresser : distinguer fait rapporté / interprétation / alternative ; tirer une leçon et envisager une nouvelle action.

D2 reste un code candidat du référentiel **et** joue un rôle transversal dans le moteur. Cette double fonction doit être discutée avec les encadrants ; ne pas la résoudre par suppression arbitraire.

## 4. Ce que PTD Coach doit réellement faire — deux niveaux de coaching

### Coach individuel : laboratoire privé de compréhension et de réflexion
- Accès à des ressources de projet et d'équipe, sans questionnement obligatoire.
- Préparation d'une action réelle choisie par l'étudiant (ex. demander une reformulation au client, clarifier une dépendance).
- Retour sur événement concret avec une ou deux questions utiles, pas une procédure obligatoire en huit étapes.
- Identification d'une priorité personnelle **optionnelle**, avec mémoire courte contrôlée par l'étudiant.
- Reprise explicite à la demande ; l'IA n'invente pas ce qui s'est passé depuis la dernière séance.
- Aucun transfert privé→équipe, tuteur, coordonnateur ou autre membre sans action autorisée et confirmée par l'étudiant.

### Coach collectif : support au dialogue humain et à la coordination
- Les sept étudiants sont **physiquement en dialogue oral**, et une seule personne saisit leur synthèse à l'IA écrite affichée.
- Interventions courtes, à la demande ou à des jalons choisis ; non obligatoires à chacun des 17 créneaux.
- Propose une revue de processus (« Comment avez-vous identifié les dépendances ? »), pas une enquête sur la valeur des individus (« Qui ne fait rien ? »).
- Toute synthèse/engagement reste un **brouillon** tant que le groupe ne l'a pas explicitement validé.
- Peut proposer une fiche ressource ; jamais déclarer qu'une décision est prise parce qu'elle est dans la conversation.

### Tuteur humain et coordination
- Tuteur : situation du projet et synthèses collectives **validées** ; preuves individuelles seulement si volontairement partagées ; possibilité d'orienter les apports et d'intervenir dans les difficultés persistantes.
- Coordination : vue agrégée des besoins et des jalons ; pas d'accès libre aux chats individuels ni aux verbatims collectifs par défaut.
- En cas de conflit grave, exclusion, discrimination, mise en danger, données sensibles ou conflit d'intérêt : relais humain explicite, ne pas arbitrer à la place de l'établissement.

## 5. Les trois objets que la mémoire doit séparer

| Objet | Valeur pédagogique | Accès et statut |
|---|---|---|
| **Mémoire collective** : exigences validées, jalons, décisions, difficultés de processus, prochain point | Continuité du projet et de l'équipe | Équipe/tuteur selon habilitations ; contenus **confirmés** |
| **Mémoire individuelle** : objectifs choisis, ressources consultées si conservées, intentions, débriefs personnels | Continuité du coaching personnalisé | Étudiant seul ; confidentialité backend, partage explicite granulaire |
| **Référentiel pédagogique** : concepts, ressources versionnées, critères de qualité, exemples fictifs | Cohérence et vérifiabilité | Commun à tous, maintenu par responsables pédagogiques |

Un LLM ne décide pas des autorisations, ne fusionne pas les mémoires et n'écrit pas directement dans les bases métier. Les propositions du modèle sont validées par le backend et par l'humain lorsqu'un consentement ou une décision collective est requis.

## 6. Le parcours PTD 2027 : occasions, non succession de modules

Base : 17 jeudis de trois heures entre le 7 janvier et le 10 juin 2027, quatre cycles et quatre revues (28/01, 11/03, 29/04, 03/06), challenge croisé le 25/03, **calendrier prévisionnel à valider**. Environ 30 minutes de tuteur sont intégrées au créneau ; pas d'ajout de 17 obligations IA.

| Cycle | Situations dominantes | Support collectif *facultatif* | Possibilités individuelles |
|---|---|---|---|
| **C1 : 7–28 janvier** | Client, reformulation, répartition, première planification, règles de coopération | Clarifier comment se prennent les décisions et comment les informations circulent | Comprendre une méthode, choisir si utile une capacité à travailler |
| **C2 : 4 fév.–11 mars** | Premières réalisations, interdépendances, premières tensions, qualité du travail | Un débrief court d'un obstacle réel et une amélioration choisie | Préparer un échange, clarifier un blocage, analyser sa contribution |
| **C3 : 25 mars–29 avril** | Challenge, retours, écarts, arbitrages, adaptation | Revue de l'apprentissage issu d'un événement, sans blâme | Examiner des hypothèses alternatives et les changements décidés |
| **C4 : 13 mai–10 juin** | Qualité finale, restitution, bilan de méthode et de coopération | Identifier les pratiques d'équipe réutilisables | Bilan étayé de deux situations et transfert vers une autre expérience |

**Proposition de rythme** : quatre sollicitations de revue collective autour des jalons (un clic « faire un point »), non quatre séances obligatoires. En dehors, le groupe peut consulter une ressource ou utiliser l'aide à la demande. Les étudiants qui ne sollicitent pas le coach ne sont pas « en retard » dans une progression artificielle.

## 7. Trois ressources originales à publier après relecture

- `R01-coordination-et-engagements.md` : clarifier contribution, interdépendances et qualité, sans cloisonner les sept étudiants.
- `R02-debrief-factuel.md` : retour d'expérience court, faits et interprétations, sans jugement de personnalité.
- `R03-cadrage-et-planification.md` : besoin, tâches, dépendances, jalons et incertitudes.

Chaque fiche doit inclure objectifs, situation typique, méthode, exemple **fictif**, erreurs fréquentes, usage limité de l'IA, sources d'appui et statut « brouillon / relu / approuvé ». Leurs formulations sont originales ; elles ne reproduisent pas les échelles CATME, IPMA, CDIO ou des pages de manuels sous droits.

## 8. Décisions candidates, dépendances et non-décisions

**Rappel du lot source, à rapprocher du registre existant** : apprentissages individuels dans un vrai collectif ; aide sans substitution ; ressources ; réflexivité contextualisée ; coopération centrale ; pas de note ni de diagnostic automatique. Les jeux de rôle non prioritaires et les modalités nouvelles restent PROPOSÉS : la demande d’intégration ne les valide pas.

**Propositions nouvelles pour revue** : classification E1–E4 ; sept intentions d’intervention combinables ; déclencheurs de débrief ; seuils de concision ; mémoire d'objectifs ; lot initial de ressources ; protocole de recette en deux niveaux.

**Ouvert** : validation institutionnelle du référentiel, échelles, durée et fréquence des sollicitations, méthodes d'observation par tuteur et de retours des pairs, rédaction du consentement et politique de conservation, licence du dépôt et accès aux textes intégrals.

**À ne pas faire maintenant** : convertir les 11 codes en score numérique, rendre les simulations obligatoires, imposer les questionnaires d'entrée, développer des tableaux de bord de « leadership » ou stocker des noms de camarades comme des données d'évaluation.

## 9. Priorités de travail autonomes

1. Faire une recette pédagogique **sur 20 conversations fictives**, dont cas négatifs et refus d'assistance, avant de coder de nouvelles fonctionnalités.
2. Faire relire trois ressources originales par deux encadrants ; enregistrer corrections et sources.
3. Implémenter dans un simulateur un routeur de réponse non contraignant : ressource directe, clarification, préparation d'action, débrief, refus/relai humain. Ne pas promettre une classification parfaite par l'IA.
4. Mesurer les défauts pédagogiques (surenquête, conclusions prématurées, fuite, substitution, fatigue) au moins autant que les performances apparentes.
5. Ensuite seulement, évaluer la qualité du comportement de Mistral sur les mêmes scénarios et mesurer tokens, coûts et latence.

Voir `PTD_CONVERSATION_POLICY_V06.md`, `PTD_PILOT_PROTOCOL_V06.md` et `EVIDENCE_REGISTER_V06.md`.
