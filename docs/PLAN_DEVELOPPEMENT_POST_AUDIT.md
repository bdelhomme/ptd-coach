# Plan de développement proposé après l'audit PTD

Ce plan traduit l'[audit du 12 novembre](AUDIT_GLOBAL_PTD_2026_11_12.md) en
tranches réalisables. Ce sont des propositions de réalisation et de tests, pas
une validation pédagogique institutionnelle. Toutes les étapes de développement
utilisent des données fictives, conservent les contextes et jeux gelés et ne
fusionnent pas automatiquement les PR. Le jeu réservé historique reste fermé à
l'ajustement. Chaque tranche conserve une procédure de reprise, tests et limites.

## 1. Répondre juste avant d'élargir

**Problème déclencheur :** TX08 affirme à tort qu'une application ne peut pas
être un livrable ; TX10 et TX18 rapportent au passé des essais futurs ; TX17
transforme une option en décision ; PV08 invente un fait personnel ; PV13 ajoute
une précision non établie à l'accord du client.

**Tranche proposée :** un nouveau contexte versionné et isolé, avec exemples
conceptuels vérifiés et distinction explicite entre fait rapporté, hypothèse,
option, essai prévu, résultat observé et décision confirmée. Étudier si une
représentation applicative de ces statuts peut être utile, sans confier au
modèle le pouvoir de déclarer un accord, de partager ou d'agir. Une réponse doit
continuer à expliquer et à aider ; le contrôle ne doit pas générer un refus ou
une question systématique. Une vérification automatique est une hypothèse à
évaluer, pas une preuve de vérité.

**Recette :** reproduire les cas cités et de nouvelles variantes avec mots,
chiffres et interlocuteurs différents ; vérifier WBS/livrable, conditionnel,
chronologie, provenance et qualité de l'aide. Vérifier l'absence de fuite entre
fils et l'absence d'action. Comparer à contexte et modèle fixés ; grille humaine
vierge ; ne pas interpréter des corrections sur des cas connus comme transfert.

## 2. Une entrée compréhensible pour l'étudiant et l'équipe

**Problème déclencheur :** l'interface présente une conversation et des
versions techniques, sans aider clairement l'étudiant à situer sa difficulté
dans le déroulement du PTD ; la version ouverte peut être une ancienne instance.

**Tranche proposée :** une entrée simple « sur quoi voulez-vous avancer ? »
avec situations concrètes : démarrer, comprendre la demande, préparer le cahier
des charges, organiser la prochaine séance, difficulté d'équipe, vérifier un
résultat, préparer la restitution. Choix facultatif et modifiable ; le coach
reste utilisable en question libre. Le créneau prévu le jeudi matin, obligatoire
en théorie, est un contexte de projet à confirmer ; les disponibilités entre
séances ne doivent pas être supposées. Visibilité explicite privé/collectif,
transmission au fournisseur et statut expérimental. Les décisions prises par
l'équipe restent ses propres décisions.

**Recette :** essais locaux sur mobile et ordinateur avec utilisateurs fictifs :
un étudiant qui ne connaît pas le nom d'une méthode trouve une entrée, comprend
l'espace et ce qui est envoyé, peut revenir en arrière, et demande une aide sans
subir de questionnaire. Vérifier navigation clavier, labels et contraste, puis
prévoir un audit d'accessibilité adapté ; ne pas revendiquer une conformité WCAG
sur la seule base des contrôles automatiques.

## 3. Accompagner les baisses d'élan et la vie du groupe

**Problème déclencheur :** PV07 suppose une cause unique et une réunion longue ;
PJ02 demande trois réponses à chacun en 20 minutes et suggère du travail entre
jeudis sans disponibilité connue ; PV09 utilise une formule ambiguë sur la
transmission des messages.

**Tranche proposée :** des aides proportionnées dans le temps disponible :
clarifier un obstacle, choisir un résultat atteignable dans la séance, rendre
visible une progression sans scoring, préparer une discussion sur les charges.
Prévoir plusieurs hypothèses possibles, le droit de ne pas parler de sa vie
privée et une sortie sans exercice. En cas de difficulté personnelle ou de
moqueries répétées, proposer des choix et un relais humain adapté sans diagnostic,
médiation imposée, promesse absolue de confidentialité ou contact automatique.

**Recette :** retester PV07–11 et PJ02, puis des situations différentes écrites
après le gel ; demander une relecture pédagogique et de pertinence des relais.
Contrôler les engagements hors créneau et l'absence d'interprétation des
personnes ; aucune mesure ou note de motivation n'est produite.

## 4. Cahier des charges, ressources et mémoire maîtrisée

**Problème déclencheur :** l'équipe a besoin d'un support évolutif ; le
sélecteur peut choisir une fiche hors sujet, et l'historique d'un fil ne constitue
pas une mémoire de semestre.

**Tranches proposées :**

- Préparer un canevas de cahier des charges manipulable par les étudiants :
  besoin, source, exigence, critère, statut, date et personne qui confirme ;
  autoriser les champs inconnus et la relecture, sans validation automatique.
- Réviser la découverte de fiches sur des difficultés formulées simplement ;
  rendre leur statut visible, expliquer pourquoi une ressource est proposée,
  et permettre une réponse directe. Relecture documentaire et enseignante avant
  de faire passer une fiche pour un contenu approuvé.
- Concevoir une mémoire **relisible, modifiable, supprimable et volontaire**,
  distincte entre espace individuel et espace collectif, avec provenance et
  statut. Le partage à un tuteur nécessite une action et des droits explicites.
  Spécification et prototype fictif d'abord ; pas de mémoire longitudinale
  automatique ni de données réelles avant arbitrages et protections appropriés.

**Recette :** essais d'exigences incomplètes, contradictoires ou modifiées ;
recherche avec et sans bon outil ; correction et révocation d'un souvenir ;
interdiction d'injecter le privé d'une autre personne ; autorisation et retrait
du partage côté serveur. Relecture humaine des sources et modèles vierges.

## 5. Préparer l'usage responsable et mesurer l'apprentissage

Le prototype local ne fournit ni authentification réelle, ni politique de
rétention institutionnelle, ni audit de sécurité complet. En parallèle de la
conception pédagogique, définir avec les responsables les identités, droits,
consentements, stockage, suppression, sauvegarde et conditions du fournisseur.
Rester sur des données fictives jusqu'à ces décisions et validations.

Après les tests de développement, préparer une batterie indépendante non utilisée
pour ajuster les prompts, puis une évaluation par au moins deux lecteurs lorsque
possible : justesse, utilité, autonomie et incidents ; conserver désaccords et
citations, sans note étudiante. Étudier séparément une tâche de transfert réalisée
sans coach. Suivre aussi les erreurs réseau, le délai et les tokens ; ne pas faire
de l'optimisation de coût un critère qui masque une perte pédagogique.
