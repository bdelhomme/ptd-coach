# Journal des évolutions de réflexion

Ce journal constitue une mémoire de conception. Il résume les échanges utiles
sans recopier les conversations et distingue principes confirmés, propositions
de l'assistant et questions ouvertes. Il ne remplace pas le registre de décisions.
Les nouvelles entrées sont ajoutées avec date, références et conséquences ; une
révision ultérieure doit conserver la possibilité de comprendre l'évolution.

## R-001 — 2026-11-06 — Compréhension du parcours étudiant

- **Retour du porteur** : l'étudiant risque d'être perdu dans le premier parcours.
- **Travail effectué** : clarification de l'interface autour de trois moments,
  ici avec le coach / avec l'équipe / de retour ici ; détail dans le ticket 002.
- **Limite** : cette correction d'interface ne valide pas les exercices ou leur
  efficacité pédagogique. Le prototype demeure une démo fictive.

## R-002 — 2026-11-06 — Cadrer le coaching avant les exercices

- **Retour du porteur** : les exercices ne convainquent pas ; définir d'abord,
  pour chaque compétence, comment le coaching pourrait aider à progresser.
- **Orientation confirmée** : priorité au cadrage par compétence (D-020).
- **Proposition de travail** : fiche décrivant capacités, situations, obstacles,
  interventions du coach, expérimentation et indices de progression.
- **Conséquence** : l'ajout d'exercices n'est plus la prochaine priorité de
  développement. Les fiches et leurs descripteurs restent à discuter.

## R-003 — 2026-11-06 — Aider sans faire, avec des ressources

- **Précision du porteur** : accompagner et aider sans faire à la place ; donner
  également des ressources et rendre cette posture explicite (D-021).
- **Propositions** : contrat d'accompagnement visible, explications directes
  lorsque nécessaires, exemples fictifs commentés et ressources courtes liées
  au besoin. L'exercice est une forme d'aide possible, pas un passage obligatoire.
- **À préciser** : limites d'aide par compétence, contenu des ressources,
  provenance, droits et relecture. Aucun catalogue n'est encore approuvé.

## R-004 — 2026-11-06 — Se situer pour choisir où travailler

- **Proposition du porteur, intérêt confirmé** : aider l'étudiant à se positionner
  sur les compétences de management de projet pour identifier où travailler (D-022).
- **Modalités proposées** : distinguer ressenti, expérience décrite et éléments
  disponibles ; laisser l'étudiant confirmer sa priorité ; reprendre le
  positionnement après une expérience.
- **Illustration proposée** : pour A2, découpage en tâches, dépendances/validations
  et adaptation du planning. Ces descripteurs ne sont pas approuvés comme référentiel.
- **Garde-fous hérités** : privé individuel, partage volontaire, pas de score
  institutionnel ni de niveau inféré du volume de conversation ; absence de trace
  distincte d'une faible compétence. Aucun nouvel écran ou schéma encore décidé.

## R-005 — 2026-11-06 — Mémoire continue dans GitHub

- **Demande explicite du porteur** : actualiser lorsque pertinent les documents
  GitHub pour conserver les évolutions de réflexion et permettre la reprise par
  toute IA (D-023).
- **Mise en œuvre documentaire** : cadre de coaching, présent journal, décisions,
  questions ouvertes, priorité, consignes AGENTS et passation actualisés.
- **Cohérence technique** : les commits du prototype et de clarification, restés
  locaux, sont inclus dans la branche de synchronisation pour que la documentation
  publiée et le code publié décrivent le même état.
- **Traçabilité de publication** : l'état de publication et les contrôles réellement
  exécutés figurent dans PROJECT_STATUS.md ; ne pas déduire leur succès de cette entrée.

## R-006 — 2026-11-06 — Retrouver un cadre global et sourcé

- **Essai de cadrage** : une première proposition A2 a décliné trois capacités
  (tâches, dépendances/validations, adaptation) ; l'ajout des durées et de la charge
  a été posé comme question et n'a pas reçu d'accord.
- **Retour du porteur** : s'appuyer sur des livres/travaux de management de projet ;
  le détail isolé d'une petite compétence risque de faire perdre la vue d'ensemble.
- **Recherche effectuée** : vérification de présentations officielles, sommaires
  et résumé d'article pour Garel/Ika, IPMA ICB4/ICB4CCT, PMI, ISO et Helle et al.
  Le corpus et ses limites de lecture sont consignés dans PROJECT_MANAGEMENT_FOUNDATIONS.md.
- **Méthode proposée (D-024)** : cadre global → situations PTD → apprentissages →
  articulation des compétences candidates → fiches et interventions du coach.
- **Statut** : aucune adoption de corpus, aucun nouveau découpage ou descripteur
  validé. Ne pas poursuivre mécaniquement la micro-décomposition d'A2 ; discuter
  d'abord le socle d'ensemble et documenter les correspondances aux sources.

## R-007 — 2026-11-09 — Intégrer V0.6 puis V0.7 avant le nouveau coach

- **Demande explicite du porteur** : intégrer les deux archives dans l'ordre,
  préserver décisions et candidat V0.3, éviter les doublons, vérifier et ouvrir
  une PR dédiée ; ne pas commencer le développement du nouveau coach Mistral.
- **Apport V0.6** : théorie d'action globale, articulation des onze codes sans
  remplacement, capacités analytiques E1–E4, politique souple, trois ressources,
  20 cas fictifs et distinction qualité du dialogue / apprentissage / sécurité.
- **Statut** : intégration autorisée, propositions pédagogiques non adoptées,
  ressources en brouillon. Les mentions d'accords ultérieurs dans les archives
  ne constituent pas à elles seules la preuve d'une validation du porteur.
- **Apport V0.7** : 12 dialogues (26 tours), prompt expérimental, exécuteur
  dry-run et préparation de grilles humaines. Le chemin API fourni est conservé
  à part de l'application, sans appel ni développement du nouveau coach.
  La copie V0.6 est remplacée par le chemin canonique déjà intégré.
- **Traçabilité** : ordre, apports V0.7, adaptations et résultats réels dans
  [INTEGRATION_V06_V07.md](INTEGRATION_V06_V07.md). V0.4/V0.5 non fournies ;
  aucune reconstitution ou validation de leurs décisions.

## R-008 — 2026-11-09 — Premier coach conversationnel réel

- **Demande du porteur** : lancer l'étape 2 avec Mistral, conversation souple
  à plusieurs tours, ressources, réflexivité, préparation d'action, tokens,
  espaces isolés, interface Mac pour étudiants fictifs et nouvelle PR.
- **Accord enregistré** : D-026 succède au report D-025. A2, ses contrats et
  le référentiel candidat V0.3 restent préservés ; aucune validation du référentiel.
- **Implémentation provisoire** : service de conversation séparé, sans outils
  d'action métier ni partage ; prompt V0.7 et R01–R03 conservés comme brouillons.
  Le complément applicatif explicite les capacités et limites effectives.
- **Méthode de recette** : tests structurels hors réseau distincts des réponses
  réelles V0.7. Première exécution : défauts de provenance inventée et formulation
  d'annulation de partage ; conservée, suivie d'un complément v1.1 et d'un nouveau
  passage, sans masquer le premier. Grille humaine encore à remplir.
- **Traçabilité** : ADR-0007, contrat conversation.v1, mode d'emploi et rapport
  CONVERSATION_COACH_REPORT ; statut de publication à vérifier dans la PR.
