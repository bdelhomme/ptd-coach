# Architecture pédagogique

## Finalité et principe
Le PTD réel est un terrain d'apprentissage. L'individu apprend à gérer des projets en comprenant les méthodes, en s'entraînant, en les expérimentant dans l'équipe et en débriefant. Le coach collectif facilite les décisions réelles sans prendre la place des étudiants.

## Orientation de conception confirmée le 2026-11-06

Le porteur confirme la priorité au cadrage par compétence, à l'accompagnement
sans faire à la place, aux ressources et à l'aide au positionnement pour choisir
où travailler (D-020/D-021/D-022). Voir [le cadre de coaching](COACHING_FRAMEWORK.md)
et [le journal des réflexions](REFLECTION_LOG.md).

L'exercice devient une intervention possible, à choisir selon le besoin ;
l'explication, l'exemple fictif, la ressource et le débrief ont également leur place.
Les fiches de coaching et les descripteurs concrets sont à co-concevoir, avant
l'ajout de nouveaux exercices. Les exemples existants ne sont pas validés par le
seul fait que le prototype fonctionne.

Un auto-positionnement formatif et privé est à concevoir : distinguer ressenti,
expérience décrite et éléments disponibles ; aider l'étudiant à confirmer une
priorité et à se repositionner après action. Questions et éventuelles échelles
restent proposées ; aucune notation ou certification de compétence automatique.
Ces orientations ne modifient pas encore la machine à états ou les JSON existants.

## Boucle d'apprentissage (proposée)
`OBJECTIVE_SELECTED → LEARNING → PRACTICING → EXPERIMENT_PLANNED → AWAITING_EXPERIENCE → REFLECTING → REVIEWED → CLOSED`.

Les transitions peuvent permettre reprise, retour en arrière et abandon non pénalisant. Un état n'est **pas** un niveau de compétence. Toute expérience réelle est déclarée ou documentée, jamais observée directement par l'IA.

## Onze compétences candidates, version 0.3 (NON VALIDÉE)
| Code | Domaine | Compétence |
|---|---|---|
| A1 | Projet | Analyser et reformuler une demande |
| A2 | Projet | Structurer et planifier le projet |
| A3 | Projet | Piloter et adapter la réalisation |
| B1 | Coopération | Organiser et coordonner le travail collectif |
| B2 | Coopération | Communiquer et construire des décisions collectives |
| B3 | Coopération | Animer et responsabiliser un collectif |
| C1 | Résolution | Analyser un problème complexe et construire une réponse argumentée |
| C2 | Résolution | Intégrer les enjeux et responsabilités du projet |
| D1 | Pratique professionnelle | Interagir avec un commanditaire et les parties prenantes |
| D2 | Pratique professionnelle | Analyser son expérience pour progresser |
| D3 | Pratique professionnelle | Produire et présenter une restitution professionnelle argumentée |

Ces onze labels **ne sont pas tirés mot pour mot d'une norme**. Ils sont issus d'un travail d'alignement initial entre syllabus PTD, grilles 2026 et cadres ISO/IPMA/CDIO/CTI. Voir `REFERENCE_MATERIAL.md`. Les descripteurs à 4 niveaux sont des propositions, pas une échelle psychométrique validée.

## Parcours réel 2027 (proposition de Laurence, sous réserve de validation)
- **Cycle 1, 7–28 janvier** : besoin et premières preuves ; charte, entretien client, cadrage, planning initial ; revue 1 le 28/01.
- **Cycle 2, 4 février–11 mars** : produire une première réponse ; revue 2 le 11/03.
- **Cycle 3, 25 mars–29 avril** : challenge croisé 25/03, mise à l'épreuve, adaptation, revue 3 le 29/04.
- **Cycle 4, 13 mai–3 juin** : consolidation, transmission, revue 4 le 03/06 ; finalisation 10/06 ; soutenances proposées 14–15/06.
- **Rythme** : 17 jeudis × 3h = 51h ; tuteur 30 min inclus dans le créneau de groupe.

### Alignement individuel / collectif
L'IA collective est accessible au groupe et suit les livrables. Le parcours individuel privé privilégie 2 objectifs actifs **proposés** (à tester), avec explication, mise en situation, action réelle, débrief. Ne pas ajouter automatiquement de nouveaux devoirs : exploiter les traces déjà prévues par l'équipe et l'école.

## Modes du moteur pédagogique
`EXPLAIN` (expliquer), `GUIDED_QUESTION` (questionner), `PRACTICE` (exercice), `ROLEPLAY` (simulation), `PLAN_ACTION` (expérimentation), `REFLECT` (débrief), `COLLECTIVE_REVIEW` (séance d'équipe), `TUTOR_HANDOFF` (sollicitation d'appui humain).

## Feedback
Évaluer la réponse/exercice présent, pas « le niveau de la personne ». Feedback concret : objectif → éléments bien pris en compte → angle mort → justification → prochaine tentative. Éviter compliments génériques et surinterprétation psychologique. Principes à confronter aux travaux de Hattie/Timperley, Nicol/MacFarlane-Dick.

## Évaluation
Ne pas remplacer les grilles 2026. Séparer production collective, réflexivité, preuves individuelles partagées et observations du tuteur. Une compétence *travaillée* n'est pas une compétence *démontrée* ; un niveau *insuffisamment documenté* n'est pas un niveau bas.
