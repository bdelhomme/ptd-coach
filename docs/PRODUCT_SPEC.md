# Spécification produit — PTD Coach v0.2

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


## Évolution proposée — V0.6/V0.7, 2026-11-09

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

## Priorité de conception — complément du 2026-11-06

Les principes D-020/D-021/D-022 sont confirmés par le porteur : cadrer le coaching
par compétence, accompagner sans faire à la place avec des ressources et aider
l'étudiant à se positionner pour choisir où travailler. Leur traduction en
capacités, dialogues, ressources et fonctionnalités reste à discuter ; voir
[COACHING_FRAMEWORK.md](COACHING_FRAMEWORK.md) et [ticket 003](tickets/003-coaching-design.md).

L'auto-positionnement est envisagé dans l'espace individuel privé, avec une
priorité confirmée par l'étudiant et un retour possible après expérience. Aucun
questionnaire, barème, écran, contrat API ou nouveau niveau de compétence n'est
adopté ou implémenté par ce complément. Le référentiel reste candidat.

## Proposition de valeur
Application d'entraînement, d'expérimentation et de retour réflexif **individualisés**, articulée à la conduite d'un PTD **collectif**, avec encadrement humain et pilotage pédagogique transversal.

## Acteurs
**Étudiant** : espace collectif, espace privé, ressources et preuves partagées à son initiative.  
**Animateur tournant** : conduit la séance IA sur écran partagé, sans privilège sur les espaces privés.  
**Tuteur** : synthèses collectives validées, orientations, retours de revue, pièces personnelles volontairement partagées, extraits collectifs ciblés sous contrôle.  
**Coordination** : vision transverse, cours et consignes collectives, alertes générales sans détail des conversations.  
**Admin technique** : opérations d'exploitation sans consultation automatique des messages privés.

## Fonctions prioritaires et critères de recette
| ID | Fonction | Critère minimal |
|---|---|---|
| F-01 | Comptes / équipes | Un étudiant n'accède qu'à son équipe et son espace |
| F-02 | Contexte projet | L'équipe peut saisir sujet, client, échéances et ressources partageables |
| F-03 | Coach individuel | Apprendre, s'entraîner, planifier expérimentation, débriefer |
| F-04 | Mémoire individuelle | Reprendre la progression sans fuite vers les autres |
| F-05 | Coach collectif | Discussion humaine orale + IA écrite, animateur tournant |
| F-06 | Synthèses validées | L'IA propose, l'équipe corrige et valide avant visibilité tuteur |
| F-07 | Tuteur | Voir synthèses, orienter coaching, préparer revues |
| F-08 | Coordination | Voir avancement agrégé, publier ressources et consignes |
| F-09 | Preuves | Un étudiant choisit exactement ce qu'il partage |
| F-10 | Revue | Préparer le point tuteur depuis le calendrier PTD |
| F-11 | Coût | Compter tokens, usage par activité, plafonds et alertes |
| F-12 | Portabilité | Même logique avec Mistral ou simulateur IA |
| F-13 | Audit | Traçabilité des partages, consultations exceptionnelles et versions |
| F-14 | Export | Export standard de données autorisées ; procédure documentée |

## Premier scénario de bout en bout — A2 planification
1. Un étudiant fictif s'authentifie dans son équipe PTD fictive.
2. Il choisit l'objectif « anticiper les dépendances ».
3. Le coach explique jalons, tâches, dépendances et critères.
4. L'étudiant résout un exercice sur un retard client.
5. Le coach émet un feedback spécifique et vérifiable, pas une note.
6. L'étudiant décide d'une action concrète à tester lors d'une réunion.
7. Après l'activité réelle (simulée pour le pilote), il décrit ce qu'il a effectivement fait.
8. Le coach l'aide à séparer observations, interprétations et leçons.
9. L'étudiant sauvegarde le bilan privé, et peut partager une **preuve sélectionnée**.
10. Un tuteur ne peut jamais consulter le dialogue privé via l'API.

## Coach collectif
Dix à quinze minutes indicatives au sein du temps PTD ; pas de captation audio ; IA ne prétend pas entendre ni voir l'équipe ; animateur conduit, sept peuvent contribuer ; mémoire des décisions validées ; pas d'assignation en silos. Quatre revues structurantes et un challenge croisé.

## Exclusions initiales
- Notation automatique ou classement des étudiants.
- Profilage comportemental / de personnalité à partir des messages.
- Transcription / écoute automatique des discussions orales.
- Déploiement ouvert avec vraies données étudiantes avant validation institutionnelle.
- Client ou rapporteur connecté directement dans la première phase.

## Mesure d'efficacité
Vérifier par épreuves de compréhension/transfert, simulations comparables, observations humaines, utilité ressentie, charge de travail, coûts. Ne pas confondre volume d'utilisation et apprentissage.
