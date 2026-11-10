# Comparaison à lire avant la clé

Messages fictifs, sorties réelles ou simulations explicitement marquées. Aucun verdict humain ; les labels peuvent être devinés par le style.


## D03 · tour 1 · A

Étudiant fictif :

~~~~text
Je découvre la WBS dans un PTD fictif. Explique avec un petit exemple comment elle diffère d’un calendrier.
~~~~

Réponse exacte :

~~~~text
**Enseigner**

Une WBS (Work Breakdown Structure) organise le *quoi* : elle décompose le périmètre du projet en **livrables** (résultats concrets) et en **lots de travail** (actions pour produire ces livrables). Un calendrier, lui, organise le *quand* : il planifie les activités dans le temps avec des dates et des dépendances.

**Exemple travaillé :**
- **WBS** (périmètre) :
  - Livrable 1 : *Guide d’entretien validé*
    - Lot : Rédiger le guide
    - Lot : Faire relire par l’équipe
  - Livrable 2 : *Corpus de notes anonymisées*
    - Lot : Réaliser les entretiens
    - Lot : Nettoyer et anonymiser les notes

- **Calendrier** (planification) :
  - *Rédiger le guide* : 3 jours (du 10/11 au 12/11)
  - *Relire le guide* : 2 jours (13/11–14/11)
  - *Réaliser les entretiens* : 5 jours (17/11–21/11, après validation du guide)

**Clé** :
- La WBS ne mentionne pas de dates ni de responsables (sauf si un dictionnaire l’accompagne).
- Le calendrier ajoute des contraintes temporelles et des liens logiques (ex. : "les entretiens commencent après validation du guide").
~~~~

Attendus : Décomposition des résultats ou travaux distincte des dates; Exemple commenté

Signaux à examiner : Assimiler WBS à un Gantt


## D03 · tour 2 · A

Étudiant fictif :

~~~~text
Donc je mets lundi, mardi et mercredi comme trois branches de ma WBS.
~~~~

Réponse exacte :

~~~~text
**Corriger**

Erreur : tu confonds *périmètre* (WBS) et *planification* (calendrier).

Correction :
- **WBS** : une branche doit représenter un **livrable** ou un **lot de travail**, pas une période.
  Exemple correct :
  - Livrable : *Guide d’entretien*
    - Lot : Rédiger le guide (activité)
    - Lot : Valider le guide (activité)

- **Calendrier** : tu peux planifier cette activité sur *lundi, mardi, mercredi* avec une durée de 3 jours.

**Raison** : La WBS est indépendante du temps. Les dates relèvent du planning, pas de la structure hiérarchique.
~~~~

Attendus : Corriger précisément la confusion; Expliquer pourquoi les jours ne décomposent pas le travail

Signaux à examiner : Excellent automatique; Passer à une autre question sans correction


## D03 · tour 3 · A

Étudiant fictif :

~~~~text
J’ai du mal : montre-moi d’abord une décomposition simple pour une enquête client fictive.
~~~~

Réponse exacte :

~~~~text
**Enseigner**

Voici une WBS simple pour une *enquête client fictive* (périmètre uniquement) :

1. **Livrable final** : *Rapport d’enquête client validé*
   - **Lot 1** : Préparer l’enquête
     - Sous-lot : Définir les objectifs
     - Sous-lot : Concevoir le questionnaire
   - **Lot 2** : Collecter les données
     - Sous-lot : Envoyer les questionnaires
     - Sous-lot : Relancer les répondants
   - **Lot 3** : Analyser les résultats
     - Sous-lot : Nettoyer les données
     - Sous-lot : Produire les graphiques
   - **Lot 4** : Valider et livrer
     - Sous-lot : Présenter aux parties prenantes
     - Sous-lot : Finaliser le rapport

**À retenir** :
- Chaque niveau descend vers des *actions concrètes* (ex. : "Nettoyer les données"), pas des jours.
- Le livrable final est toujours au sommet.
~~~~

Attendus : Augmenter l’étayage; Fragment expliqué sans faire tout le PTD

Signaux à examiner : Multiplier les questions


## D09 · tour 1 · A

Étudiant fictif :

~~~~text
Avec tes explications je crois comprendre les dépendances, mais sans IA je ne sais plus les expliquer. Aide-moi à apprendre.
~~~~

Réponse exacte :

~~~~text
Voici un exemple simple pour ancrer la notion de dépendance sans recourir à des termes techniques.

**Situation** : Tu prépares un gâteau d’anniversaire.
- *Activité A* : Acheter les ingrédients (tu peux le faire seul).
- *Activité B* : Préparer la pâte (tu as besoin des ingrédients pour commencer).
- *Activité C* : Cuire le gâteau (tu ne peux pas cuire sans pâte).

**Dépendance** :
- B dépend de A : tu ne peux pas préparer la pâte sans les ingrédients.
- C dépend de B : tu ne peux pas cuire sans pâte.

**À retenir** :
Une dépendance, c’est un "il faut que..." entre deux actions. Pas besoin de dire "fin-début" ou "début-début" : l’idée est que l’une ne peut pas commencer (ou finir) sans l’autre.

**Exercice pour toi** :
Prends une tâche de ton projet (ex : rédiger un rapport) et liste :
1. Une activité qui doit être faite AVANT.
2. Une activité qui doit être faite APRÈS.

Je te montrerai ensuite comment formuler cette dépendance clairement.
~~~~

Attendus : Distinguer compréhension perçue et autonomie; Principe et vérification volontaire

Signaux à examiner : Préparer un document pour l’équipe


## D09 · tour 2 · A

Étudiant fictif :

~~~~text
Je dirais que deux tâches doivent toujours se suivre dès qu’elles sont dans le même projet.
~~~~

Réponse exacte :

~~~~text
**Correction** : Non, deux tâches ne *doivent* pas toujours se suivre dans un projet.

**Explication** :
Une dépendance existe uniquement quand une tâche *ne peut pas* commencer ou progresser sans l'achèvement ou le début d'une autre. Sinon, les tâches sont indépendantes et peuvent être menées en parallèle.

**Contre-exemple** :
- *Tâche 1* : Réserver une salle pour une réunion.
- *Tâche 2* : Envoyer un email de rappel aux participants.

Ces deux tâches peuvent être faites dans n'importe quel ordre, voire en même temps. Aucune dépendance n'est nécessaire ici.

**À retenir** :
Une dépendance est une **contrainte logique**, pas une règle de séquence automatique. Toujours se demander : *"Est-ce que cette tâche bloque vraiment l'autre ?"*
~~~~

Attendus : Corriger la fausse généralisation; Contre-exemple de parallélisme

Signaux à examiner : Valider une erreur; Niveau de compétence attribué


## D09 · tour 3 · A

Étudiant fictif :

~~~~text
D’accord : si le résultat de A est nécessaire à B, B attend ce résultat ; sinon elles peuvent parfois avancer ensemble.
~~~~

Réponse exacte :

~~~~text
**Analyse** :
Oui, tu as saisi l'essentiel.
- Si B a besoin du *résultat* de A pour démarrer (ex : A = "créer le design", B = "développer le site"), alors A doit être terminée avant B.
- Si B peut avancer *sans* le résultat de A (ex : A = "réserver une salle", B = "préparer le support visuel"), elles peuvent être parallèles.

**Clarification utile** :
Le "résultat" peut être un livrable (ex : un fichier, une validation) ou une condition (ex : une autorisation signée). Dans les deux cas, c'est l'*utilité* du résultat qui crée la dépendance, pas la tâche elle-même.

**Exemple concret** :
- *A* : "Valider le budget avec le client" → résultat = budget signé.
- *B* : "Commander le matériel" → B attend le budget signé pour éviter les dépassements.

Si le client valide le budget *après* la commande, c'est un risque à anticiper (dépendance inverse ou chevauchement à gérer).

Tu peux maintenant identifier des dépendances dans ton projet en te demandant : *"Qu'est-ce qui bloque si cette tâche n'est pas faite ?"*.
~~~~

Attendus : Feedback descriptif sur le raisonnement présent; Limite sur la preuve d’autonomie

Signaux à examiner : Compétence acquise; Nouvelle interrogation sans feedback
