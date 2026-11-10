# Architecture pédagogique

## Évolution expérimentale V0.8 — D-029

Le porteur autorise désormais un contexte pédagogique adaptatif séparé, avec
enseignement explicite, correction précise et vérification dosée. Familles F1–F5
combinables, sans routage hard/soft ni profil étudiant. V0.7, A2 et le candidat
V0.3 sont conservés. Les modalités et l’efficacité restent à éprouver :
[contrat V0.8](PTD_V08_CONTRAT_PEDAGOGIQUE.md) et
[bilan de mise en œuvre](V08_IMPLEMENTATION.md). Les sections suivantes gardent
l’historique des tranches et propositions antérieures.

## Mise à jour applicative — étape 2, D-026

Le premier coach Mistral local est désormais développé dans un service séparé
avec historique multi-tours, ressources et mesure des tokens, sans modifier A2
ou le candidat V0.3. La demande du porteur succède au report historique D-025.
Les détails pédagogiques V0.6/V0.7 restent proposés ; aucune validation
institutionnelle n'est déduite du code. Voir [le guide d'essai](TRY_CONVERSATION_COACH.md),
[le rapport de recette](CONVERSATION_COACH_REPORT.md) et
[ADR-0007](adr/0007-local-conversation-mistral.md).
Les mentions de non-implémentation ci-dessous décrivent les cadrages antérieurs.


## Noyau et recette proposés — V0.6/V0.7, 2026-11-09

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
