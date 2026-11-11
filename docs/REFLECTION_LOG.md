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

## R-009 — 2026-11-09 — Dossier de revue pédagogique indépendante

- **Demande du porteur** : extraire les transcriptions réelles V0.7, surtout
  v1.2 (12 scénarios/26 réponses), critères, grille humaine vierge, observations
  M09/M10/M11 et premiers défauts, paramètres/tokens ; livrer un ZIP pour revue
  critique dans ChatGPT, sans nouvelle fonctionnalité ou changement du coach.
- **Accord de périmètre D-027** : gel du référentiel, moteur et prompts jusqu'au
  retour pédagogique. Aucun nouvel appel API pour cette préparation.
- **Dossier** : quatre JSONL existants, documents Markdown par scénario,
  contextes système v1.2 exacts, ressources et grille vierge, provenance et
  manifestes. Transcriptions/observations séparées pour limiter l'ancrage.
- **Limites tracées** : les anciens systèmes complets n'ont pas été archivés ;
  l'ancienne empreinte partagée par v1/v1.1 ne couvre pas leurs compléments.
  L'évocation d'une réponse « d'hier » dans M09 est une entrée fictive, pas la
  preuve d'un ancien événement réel. Les mêmes cas ont servi aux ajustements.
- **Mémoire et livraison** : [PEDAGOGICAL_REVIEW_PACKAGE.md](PEDAGOGICAL_REVIEW_PACKAGE.md).
  Les transcriptions et le ZIP restent hors Git, livrés localement au porteur ;
  leur génération ne constitue pas une revue indépendante ou une notation humaine.

## R-010 — 2026-11-09 — Revue consultable dans le dépôt public

- **Demande du porteur** : publier les transcriptions fictives exactes sur la
  branche de la PR #6, dans `pedagogy/evaluations/mistral-small-v07/`, avec README
  immédiatement exploitable par un réviseur, historique, critères et grilles vierges.
- **Visibilité vérifiée** : GitHub indique PUBLIC ; D-028 autorise précisément
  ce corpus contrôlé. Aucune modification de visibilité n'est faite par l'assistant.
- **Choix de fidélité** : copie des 25 fichiers du ZIP sans retouche, ajout
  d'un README et d'un manifeste distinct ; empreintes d'origine conservées.
- **Contrôles** : identité des réponses et des anciennes traces, cellules de
  jugement vides, absence de secrets/coordonnées réelles et de fichiers privés.
  Les liens pseudo-Markdown inventés dans les réponses restent des citations,
  pas des cibles de navigation ; le contrôleur de liens est corrigé en ce sens.
- **Suite** : revue critique indépendante. D-027 maintient le gel du moteur,
  du référentiel et des prompts jusqu'au retour pédagogique ; aucune note ni
  nouvelle requête Mistral. Voir le README public et PEDAGOGICAL_REVIEW_PACKAGE.

## R-011 — 2026-11-10 — Enseigner et vérifier sans sur-guider

- **Retour du porteur** : première V0.8 selon le nouveau cadrage validé,
  accompagnement différencié par nature d’apprentissage ; bienveillance exigeante,
  correction précise, explications et vérification régulière sans lassitude.
- **Accord D-029** : tranche minimale sur la base #6, V0.7 et candidat V0.3
  préservés. Les cinq familles, leur choix, le seuil « une sollicitation » et
  l’heuristique de ressources restent des propositions testables.
- **Arbitrages** : pas de quota syntaxique de questions ; réponse directe et
  arrêt possibles ; feedback avant nouvelle vérification. Une version immuable
  par fil évite de mélanger les contextes et garde la comparaison possible.
- **Indépendance** : autorisation explicite du porteur pour confier les 12 cas
  réservés à un assistant distinct, sans lecture du prompt ni du jeu de développement.
  Contexte gelé avant leur création ; aucun ajustement sur les résultats réservés.
- **Limites** : les grilles restent vierges, les auteurs artificiels peuvent
  partager des biais, une comparaison courte n’établit ni gain causal ni transfert.
  Voir [le bilan](V08_IMPLEMENTATION.md) et le protocole source V0.8.

## R-012 — 11/11/2026 — C2 après revue qualitative D03/D09

Le porteur refuse de considérer c1 comme validée : allongement sans gain démontré,
WBS parfois confondue avec activités, vérifications multiples. D-030 autorise c2,
un comparatif limité puis corrections/tests autonomes dans le cadre existant.
La vérification formative est appréciée à l’échelle du dialogue ; une reformulation
correcte peut suffire pour conclure. L’intervention dominante n’est pas un quota
syntaxique ni une nouvelle machine à états. Les cinq natures restent souples.
Sources professionnelles ciblées et exemples originaux relus par l’assistant,
avec limites de validation humaine explicites. Le moteur gelé n’est pas modifié :
injection existante du contexte, bases temporaires, pas de nouvelle interface.
Réservé fermé à la conception ; aucune nouvelle délégation. Voir le rapport c2
pour les essais, budgets, constats et la prochaine étape transmissible à une IA.

### Résultat autonome de R-012

Après les 18 comparatifs initiaux, diagnostic étendu sans toucher au gel :
18 réponses sur sondes conceptuelles, 12 sur garde-fous et 6 en répétition c2.
Total 54, aucune erreur API, 132 977 tokens. La moindre verbosité relative à c1
ne s’accompagne pas d’un gain convaincant complet ; nouvelles erreurs textuelles
sur M08/M09/M11. Décision de développement : ne pas promouvoir c2, conserver le
navigateur inchangé et publier les échecs. Les autorisations backend restent
intactes. Aucun réservé, nouvelle délégation ou suite payante automatique.
Prochain travail utile : revue externe des exemples et des réponses sensibles,
puis éventuelle candidate distincte, pas fusion ou essai institutionnel.

## R-013 — 11/11/2026 — Prescription contextualisée et autonomie accompagnée

Le porteur demande d’élargir la comparaison au-delà d’A2. L’évaluation examine
ce que le coach propose spontanément quand l’étudiant ignore la méthode, quand
une formulation suffit et quand un exemple ou un brouillon rend l’activité
accessible. Le cas indique le raisonnement, la preuve ou la décision à laisser
à l’étudiant. Commanditaire et cahier des charges ont chacun six situations
sur 24. Le premier échantillon est fixé avant réponse et couvre les cinq
domaines, avec trois cas client/exigences. Le travail reste au niveau du
banc d’essai, des ressources proposées et de la documentation. Voir
[la campagne et ses résultats](CAMPAGNE_TRANSVERSALE.md).

### Résultat de R-013

Les 36 appels annoncés ont réussi et produit 89 777 tokens. La lecture
de développement repère des aides concrètes en enquête, coopération et
essai comparatif. Elle relève aussi des exigences inventées, une confusion
sur la date de remise et des généralisations à partir de trois volontaires.
La baisse de longueur de c2 ne résout pas ces défauts. Les observations et
les citations sont disponibles avec les grilles vierges. Priorité proposée
à la traçabilité des faits, critères et accords dans le cahier des charges.


## R-014 — Ressources et autonomie accompagnée

La bibliothèque répond au souhait de trouver une méthode depuis une difficulté vécue. Les sources professionnelles éclairent les pratiques, mais ne valident pas automatiquement leurs adaptations PTD. L’essai TX05/TX07 montre que fournir une fiche ne suffit pas à empêcher des chiffres ou contraintes inventés. Le résultat est un constat de développement, non une évaluation humaine. Voir `docs/BIBLIOTHEQUE_METHODES.md`.


## R-015 — Comparer les modèles ne suffit pas

Sur deux cas de développement, Medium 3.5 évite certaines inventions lorsque la fiche est imposée mais en produit sans fiche ; la recherche manque encore TX05. Pas de conclusion générale. Large 4 échoue techniquement avec la configuration existante ; diagnostic séparé à poursuivre sans modifier les gels. Voir `docs/COMPARAISON_MODELES_MISTRAL.md`.


## R-016 — Budget de raisonnement et qualité pédagogique

La reproduction de TX05 confirme qu’un plafond commun de 700 tokens peut être entièrement consommé en raisonnement avant toute réponse finale. Large 4 low répond dans ce plafond, mais conserve des défauts pédagogiques. Ne pas confondre correction technique et validation pédagogique. Les traces et les hypothèses de prix sont dans `docs/MISTRAL_LARGE4.md`.


## R-017 — Ressources de calcul et mémoire ne garantissent pas la qualité

Le porteur privilégie la recherche de pertinence, quitte à dépenser davantage en tests, et souligne la continuité sur un semestre. Sans plafond demandé, Large medium produit encore des décisions attribuées à tort au commanditaire. La mémoire doit rester corrigeable, sourcée et séparée par périmètre ; elle reste à concevoir. Voir `docs/ESSAIS_SANS_PLAFOND_ET_MEMOIRE.md`.
