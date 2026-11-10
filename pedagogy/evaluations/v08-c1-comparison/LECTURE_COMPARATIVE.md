# Lecture comparative — ouvrir avant la clé des variantes

Messages fictifs ; réponses exactes enregistrées, sans correction. Grille non notée. Les labels ne garantissent pas un aveugle parfait : le style peut révéler la version.


## D03 — WBS et calendrier


### Tour 1 · A

Étudiant fictif :

~~~~text
Je découvre la WBS dans un PTD fictif. Explique avec un petit exemple comment elle diffère d’un calendrier.
~~~~

Réponse enregistrée :

~~~~text
Voici une explication directe, avec un exemple fictif qui montre la différence entre **WBS (Work Breakdown Structure)** et **calendrier**.

---

### **1. WBS : décomposer le travail en éléments livrables**
La WBS est une **hiérarchie de tâches** qui répond à la question :
*« Quels sont les livrables intermédiaires et les activités nécessaires pour atteindre l’objectif final ? »*
Elle ne contient **ni dates, ni responsables, ni durée** — juste une structure logique.

**Exemple fictif : Organisation d’un événement étudiant**
- **Objectif final** : *"Organiser un forum des métiers le 15 juin"*
- **Niveau 1** : *"Préparation logistique"*
  - **Niveau 2** :
    - *"Réserver une salle"* (livrable : *contrat de réservation signé*)
    - *"Constituer une liste d’intervenants"* (livrable : *fichier Excel validé*)
    - *"Créer des supports de communication"* (livrable : *affiches imprimées*)
- **Niveau 1** : *"Communication"*
  - **Niveau 2** :
    - *"Relayer l’événement sur les réseaux"* (livrable : *posts publiés*)
    - *"Envoyer des invitations aux entreprises"* (livrable : *emails envoyés*)

→ La WBS permet de **clarifier ce qui doit être fait**, sans se soucier du *quand* ou du *qui*.

---

### **2. Calendrier : organiser le travail dans le temps**
Le calendrier (ou planning) est une **représentation temporelle** des tâches. Il répond à :
*« Quand chaque activité doit-elle commencer et finir ? Qui la réalise ? »*
Il peut inclure des **jalons** (dates clés) et des **dépendances** (ex. : *"Réserver la salle avant d’imprimer les affiches"*).

**Exemple fictif (extrait) :**
| Tâche                     | Responsable | Début   | Fin     | Jalon/Remarque          |
|---------------------------|-------------|---------|---------|--------------------------|
| Réserver la salle         | Alice       | 10/05   | 12/05   | Jalon : *Salle confirmée* |
| Constituer la liste d’intervenants | Bob   | 05/05   | 15/05   |                          |
| Créer les supports        | Charlie     | 13/05   | 20/05   | *Après validation de la liste* |
| Relayer sur les réseaux   | Diane       | 20/05   | 10/06   |                          |

→ Le calendrier **intègre les contraintes temporelles** et les liens entre tâches.

---

### **3. Différence clé**
| **WBS**                          | **Calendrier**                     |
|----------------------------------|------------------------------------|
| Structure du travail (quoi ?)    | Organisation dans le temps (quand ?) |
| Pas de dates ni de responsables  | Dates, responsables, dépendances    |
| Livrables intermédiaires         | Jalons et séquencement             |
| Outil
~~~~

Attendus à examiner : Décomposition des résultats ou travaux distincte des dates; Exemple commenté

Signaux à examiner : Assimiler WBS à un Gantt


### Tour 1 · B

Étudiant fictif :

~~~~text
Je découvre la WBS dans un PTD fictif. Explique avec un petit exemple comment elle diffère d’un calendrier.
~~~~

Réponse enregistrée :

~~~~text
Une **WBS (Work Breakdown Structure)** décompose le travail en éléments concrets et hiérarchisés, sans se soucier des dates ni des dépendances. Elle répond à *"quoi faire ?"* et *"qui s'en occupe ?"*, mais pas *"quand ?"*.

**Exemple fictif** :
Pour organiser un événement PTD, une WBS pourrait inclure :
- **1. Réservation de la salle** (responsable : A)
  - 1.1 Vérifier disponibilités
  - 1.2 Signer le contrat
- **2. Communication** (responsable : B)
  - 2.1 Créer l’affiche
  - 2.2 Envoyer les invitations

Un **calendrier**, lui, ajoute *"quand ?"* et *"dans quel ordre ?"* :
- **Semaine 1** : A finalise la réservation (1.1 + 1.2)
- **Semaine 2** : B conçoit l’affiche (2.1) et l’envoie (2.2) après validation de A sur le lieu.

**Différence clé** :
- La WBS structure le *contenu* du travail.
- Le calendrier organise le *temps* et les *dépendances*.

Besoin d’un exemple plus précis pour ton PTD ?
~~~~

Attendus à examiner : Décomposition des résultats ou travaux distincte des dates; Exemple commenté

Signaux à examiner : Assimiler WBS à un Gantt


### Tour 2 · A

Étudiant fictif :

~~~~text
Donc je mets lundi, mardi et mercredi comme trois branches de ma WBS.
~~~~

Réponse enregistrée :

~~~~text
Non, cela ne correspond pas à la définition d'une WBS.

**Pourquoi ?**
Une WBS décompose le travail en **livrables ou résultats concrets**, pas en unités de temps. "Lundi", "mardi" ou "mercredi" sont des **périodes**, pas des éléments de travail.

---

### **Exemple corrigé pour ta situation fictive**
Si ton objectif est *"Préparer un rapport technique pour le 15 juin"*, une WBS pourrait ressembler à :

- **Niveau 1** : *"Collecte des données"*
  - **Niveau 2** :
    - *"Extraire les données du capteur A"* (livrable : *fichier CSV nettoyé*)
    - *"Valider les données avec l’équipe"* (livrable : *compte-rendu de validation*)
- **Niveau 1** : *"Analyse et rédaction"*
  - **Niveau 2** :
    - *"Traiter les données avec Python"* (livrable : *graphiques générés*)
    - *"Rédiger le rapport"* (livrable : *document Word finalisé*)

→ Ici, les branches sont des **actions ou résultats**, pas des jours.

---
### **Que faire avec les jours ?**
Les jours (ou semaines) appartiennent au **calendrier**, pas à la WBS. Une fois ta WBS construite, tu peux :
1. **Estimer la durée** de chaque tâche (ex. : *"Extraire les données"* prend 2 jours).
2. **Placer ces tâches sur un calendrier** en respectant les dépendances (ex. : *"Valider les données"* doit finir avant *"Traiter les données"*).

---
**Question pour toi** :
Si tu devais décomposer *"Organiser une réunion d’équipe"* en WBS, quels seraient tes 2-3 premiers niveaux de livrables ? (Exemple : *"Réserver une salle"*, *"Préparer l’ordre du jour"*, etc.)
~~~~

Attendus à examiner : Corriger précisément la confusion; Expliquer pourquoi les jours ne décomposent pas le travail

Signaux à examiner : Excellent automatique; Passer à une autre question sans correction


### Tour 2 · B

Étudiant fictif :

~~~~text
Donc je mets lundi, mardi et mercredi comme trois branches de ma WBS.
~~~~

Réponse enregistrée :

~~~~text
Non, ce n’est pas l’usage d’une WBS.

Une WBS décompose **le travail à réaliser**, pas le temps. Si tu mets "lundi", "mardi" et "mercredi" comme branches, tu confonds avec un calendrier ou un rétroplanning.

**Exemple corrigé** :
Pour une tâche comme *"Préparer une réunion client"*, une WBS pourrait avoir :
- **1. Définir l’ordre du jour** (responsable : X)
- **2. Préparer les supports** (responsable : Y)
- **3. Réserver la salle** (responsable : Z)

Le calendrier, lui, indiquera :
- **Lundi** : X finalise l’ordre du jour
- **Mardi** : Y prépare les supports
- **Mercredi** : Z réserve la salle

Tu veux que je t’aide à reformuler une partie de ta WBS actuelle ?
~~~~

Attendus à examiner : Corriger précisément la confusion; Expliquer pourquoi les jours ne décomposent pas le travail

Signaux à examiner : Excellent automatique; Passer à une autre question sans correction


### Tour 3 · A

Étudiant fictif :

~~~~text
J’ai du mal : montre-moi d’abord une décomposition simple pour une enquête client fictive.
~~~~

Réponse enregistrée :

~~~~text
Voici une **WBS simple et complète** pour une **enquête client fictive** (objectif : *"Comprendre les besoins des utilisateurs pour un nouveau produit"*).

---

### **WBS : Décomposition en livrables**
*(Niveau 1 = grandes étapes ; Niveau 2 = sous-livrables)*

1. **Préparation de l’enquête**
   - 1.1. Définir les objectifs de l’enquête (ex. : *"Identifier les fonctionnalités prioritaires"*).
   - 1.2. Rédiger le questionnaire (livrable : *version finale validée*).
   - 1.3. Sélectionner les participants (livrable : *liste de 20 clients ciblés*).

2. **Collecte des données**
   - 2.1. Envoyer le questionnaire (livrable : *emails envoyés + relances*).
   - 2.2. Organiser des entretiens (si besoin) (livrable : *enregistrements ou notes structurées*).

3. **Analyse des résultats**
   - 3.1. Nettoyer les données (ex. : supprimer les réponses incomplètes).
   - 3.2. Identifier les tendances (livrable : *rapport d’analyse avec graphiques*).
   - 3.3. Prioriser les besoins (livrable : *liste des 3 fonctionnalités les plus demandées*).

4. **Restitution et recommandations**
   - 4.1. Présenter les résultats à l’équipe (livrable : *support de présentation*).
   - 4.2. Proposer des actions concrètes (livrable : *plan d’action pour le produit*).

---
### **Points clés à retenir**
- **Chaque élément est un livrable** (ex. : *"questionnaire validé"*, *"liste de participants"*).
- **Pas de dates ni de responsables** dans la WBS (ce sera pour le calendrier).
- **La WBS est flexible** : tu peux ajouter/supprimer des sous-livrables selon la complexité.

---
**Exercice rapide** :
Si tu devais ajouter une étape *"Test du questionnaire"* à cette WBS, où la placerais-tu ? (Réponse possible : dans *"Préparation de l’enquête"* → sous *"Rédiger le questionnaire"*.)
~~~~

Attendus à examiner : Augmenter l’étayage; Fragment expliqué sans faire tout le PTD

Signaux à examiner : Multiplier les questions


### Tour 3 · B

Étudiant fictif :

~~~~text
J’ai du mal : montre-moi d’abord une décomposition simple pour une enquête client fictive.
~~~~

Réponse enregistrée :

~~~~text
Voici une **WBS simple** pour une **enquête client fictive** (objectif : recueillir des besoins pour un projet PTD) :

---
**1. Préparation de l’enquête**
   - 1.1 Définir les objectifs (ex : "identifier les attentes sur X")
   - 1.2 Rédiger le guide d’entretien (questions clés)
   - 1.3 Choisir les participants (ex : 5 clients cibles)

**2. Réalisation des entretiens**
   - 2.1 Contacter les participants (emails/relances)
   - 2.2 Mener les entretiens (en présentiel ou visio)
   - 2.3 Noter les réponses (fiche synthétique par entretien)

**3. Analyse des résultats**
   - 3.1 Regrouper les réponses par thème
   - 3.2 Identifier les besoins prioritaires
   - 3.3 Rédiger un rapport synthétique

**4. Restitution**
   - 4.1 Présenter les résultats à l’équipe PTD
   - 4.2 Proposer des pistes d’action

---
**À noter** :
- Chaque sous-point est une **tâche concrète**, pas une date.
- Les responsables et durées viendront ensuite dans le **calendrier** ou le **plan d’action**.

Besoin d’ajuster un élément pour ton cas réel ?
~~~~

Attendus à examiner : Augmenter l’étayage; Fragment expliqué sans faire tout le PTD

Signaux à examiner : Multiplier les questions


## D09 — Comprendre sans assistance


### Tour 1 · A

Étudiant fictif :

~~~~text
Avec tes explications je crois comprendre les dépendances, mais sans IA je ne sais plus les expliquer. Aide-moi à apprendre.
~~~~

Réponse enregistrée :

~~~~text
Je vais t’aider à reconstruire ta compréhension des dépendances **sans te donner une réponse toute faite**, mais en t’aidant à les expliquer toi-même.

---

### **1. Clarifier le concept de dépendance**
Une dépendance, c’est un lien logique entre deux tâches : **la tâche B ne peut commencer que si la tâche A est terminée (ou validée)**.
Exemple concret :
- *Tâche A* : "Valider le besoin client" → *Tâche B* : "Concevoir la solution" ne peut pas démarrer avant.

**Question pour toi** :
Si tu devais expliquer cette dépendance à ton équipe **sans utiliser le mot "dépendance"**, comment la formulerais-tu ?
*(Exemple : "On ne peut pas dessiner le plan avant d’avoir les dimensions exactes.")*

---

### **2. Identifier les dépendances dans ton projet**
Prenons un exemple fictif (comme dans la fiche R03) :
- *Tâche 1* : "Finaliser la proposition technique" → *Tâche 2* : "Envoyer la proposition au client".
- *Tâche 3* : "Préparer la présentation client" → *Tâche 4* : "Faire la réunion de validation".

**À toi** :
- Quelles tâches **doivent** être terminées avant d’autres ?
- Y a-t-il des tâches qui **peuvent** être faites en parallèle ?

*(Si tu bloques, je peux te donner un exemple supplémentaire ou te guider sur un cas précis de ton projet.)*

---

### **3. Formaliser les dépendances pour ton équipe**
Pour les expliquer clairement, utilise :
- **Des phrases simples** :
  *"On ne peut pas commencer [Tâche X] avant d’avoir [Tâche Y] validée."*
- **Un schéma visuel** (même basique) :
  ```
  [Tâche A] → [Tâche B]
  ```
  *(Cela aide à visualiser les liens.)*

**Question** :
Si tu devais **décrire une dépendance critique** de ton projet en une phrase, comment la formulerais-tu ?

---
### **4. Vérifier ta compréhension**
Je te propose un petit exercice :
**Invente deux tâches de ton projet et décris leur dépendance.**
*(Exemple : "On ne peut pas commander les matériaux avant d’avoir le plan finalisé.")*

---
**Pourquoi cette approche ?**
- Tu gardes la maîtrise de ton raisonnement.
- Tu apprends à **traduire un concept abstrait en langage concret**.
- Tu prépares une explication claire pour ton équipe.

Dis-moi où tu en es, et on affine ensemble !
~~~~

Attendus à examiner : Distinguer compréhension perçue et autonomie; Principe et vérification volontaire

Signaux à examiner : Préparer un document pour l’équipe


### Tour 1 · B

Étudiant fictif :

~~~~text
Avec tes explications je crois comprendre les dépendances, mais sans IA je ne sais plus les expliquer. Aide-moi à apprendre.
~~~~

Réponse enregistrée :

~~~~text
Voici une méthode pour t'approprier les dépendances sans dépendre de l'IA :

1. **Reformule avec tes mots** : prends une dépendance que tu as identifiée (ex : "la solution technique dépend de la validation du besoin client") et écris-la en une phrase simple, comme si tu l'expliquais à un camarade.

2. **Visualise** : dessine un schéma rapide avec des flèches entre tâches (ex : "Validation besoin → Solution technique"). Pas besoin d'outil : un papier ou un tableau blanc suffit.

3. **Teste la logique** : demande-toi "Si cette étape n'est pas faite, que se passe-t-il ?" pour vérifier que la dépendance est réelle.

4. **Partage** : présente ton schéma à un membre de ton équipe et demande-lui s'il comprend la logique. S'il a des questions, c'est que tu peux clarifier encore.

**Exemple concret** :
Si tu dis "On ne peut pas finaliser le prototype sans les retours du client", ton camarade pourrait te demander "Pourquoi ?". Ta réponse doit expliquer le lien entre les deux (ex : "Parce que le client a demandé une fonctionnalité spécifique que le prototype doit intégrer").

Tu peux aussi utiliser **R03** (brouillon) comme référence pour structurer ta réflexion sur les dépendances. L'objectif est que tu sois capable d'expliquer ces liens toi-même, sans outil. Veux-tu essayer avec un exemple précis de ton projet ?
~~~~

Attendus à examiner : Distinguer compréhension perçue et autonomie; Principe et vérification volontaire

Signaux à examiner : Préparer un document pour l’équipe


### Tour 2 · A

Étudiant fictif :

~~~~text
Je dirais que deux tâches doivent toujours se suivre dès qu’elles sont dans le même projet.
~~~~

Réponse enregistrée :

~~~~text
Ta phrase contient une idée juste, mais elle est trop générale et pourrait induire en erreur. Voici pourquoi, et comment affiner ta compréhension.

---

### **Ce qui est juste dans ta phrase**
- **Certaines tâches doivent effectivement se suivre** dans un projet (ex. : "valider le cahier des charges" avant "concevoir le prototype").
- **La dépendance est une contrainte temporelle** : une tâche ne peut pas commencer si une autre n’est pas terminée.

---

### **Ce qui est inexact ou incomplet**
1. **Toutes les tâches ne se suivent pas** :
   - Certaines peuvent être **parallèles** (ex. : "rédaction du rapport" et "préparation de la présentation" peuvent avancer en même temps).
   - D’autres sont **indépendantes** (ex. : "réserver une salle" et "finaliser le budget" n’ont pas de lien direct).

2. **La dépendance n’est pas automatique** :
   - Une dépendance existe **uniquement si une tâche a besoin du résultat d’une autre** pour démarrer.
   - Exemple : *"On ne peut pas tester le logiciel avant qu’il soit codé"* → dépendance forte.
   - *"On peut commencer à rédiger la documentation technique en parallèle du codage"* → pas de dépendance.

---

### **Comment reformuler ta phrase pour qu’elle soit précise ?**
**Version corrigée** :
*"Dans un projet, deux tâches **doivent se suivre** uniquement si l’une dépend du résultat de l’autre. Sinon, elles peuvent être parallèles ou indépendantes."*

---

### **Exercice pour toi**
Prenons un exemple concret (fictif) :
- **Tâche A** : "Recueillir les besoins utilisateurs"
- **Tâche B** : "Rédiger le cahier des charges"
- **Tâche C** : "Créer les maquettes d’interface"

**Question** :
- Quelles tâches **doivent** se suivre ? Pourquoi ?
- Quelles tâches pourraient être faites en parallèle ?

*(Réponds avec tes propres mots, même si c’est approximatif. L’objectif est de clarifier ta compréhension.)*

---
**Pourquoi c’est important ?**
- Éviter les dépendances **inutiles** (qui ralentissent le projet).
- Identifier les **vraies contraintes** pour optimiser l’organisation.
- Expliquer clairement à ton équipe **pourquoi** certaines tâches doivent attendre.

À toi de jouer !
~~~~

Attendus à examiner : Corriger la fausse généralisation; Contre-exemple de parallélisme

Signaux à examiner : Valider une erreur; Niveau de compétence attribué


### Tour 2 · B

Étudiant fictif :

~~~~text
Je dirais que deux tâches doivent toujours se suivre dès qu’elles sont dans le même projet.
~~~~

Réponse enregistrée :

~~~~text
Attention, cette affirmation est trop large : toutes les tâches d'un projet ne sont pas forcément dépendantes entre elles.

**Pour affiner ta compréhension** :
- Une dépendance existe **uniquement** si une tâche ne peut pas démarrer ou aboutir correctement sans que l'autre soit terminée.
- Exemple de dépendance réelle : *"Valider le cahier des charges client → Commencer les analyses techniques"* (car les analyses reposent sur les exigences validées).
- Exemple de non-dépendance : *"Créer le logo de l'équipe → Rédiger le rapport d'avancement"* (les deux peuvent se faire en parallèle).

**Question pour toi** :
Dans ton projet, peux-tu identifier **une paire de tâches** où l'une bloque vraiment l'autre, et une autre paire où elles pourraient avancer indépendamment ? Cela t'aidera à distinguer les dépendances utiles des simples séquences arbitraires.
~~~~

Attendus à examiner : Corriger la fausse généralisation; Contre-exemple de parallélisme

Signaux à examiner : Valider une erreur; Niveau de compétence attribué


### Tour 3 · A

Étudiant fictif :

~~~~text
D’accord : si le résultat de A est nécessaire à B, B attend ce résultat ; sinon elles peuvent parfois avancer ensemble.
~~~~

Réponse enregistrée :

~~~~text
Exactement. Tu as saisi l’essentiel :
**Une dépendance existe uniquement si le résultat de A est nécessaire pour démarrer B.**
Sinon, les tâches peuvent être parallèles ou indépendantes.

---

### **Pour ancrer cette idée, voici un exemple travaillé ensemble**

**Scénario fictif** (inspiré d’un projet classique) :
- **Tâche A** : *"Valider les spécifications techniques avec le client"* (résultat : un document signé).
- **Tâche B** : *"Commander les composants électroniques"* (nécessite le document signé pour éviter les erreurs).
- **Tâche C** : *"Rédiger le manuel utilisateur"* (peut commencer dès que les spécifications sont stabilisées, même si A n’est pas encore signée).

**Analyse** :
1. **A → B** : Dépendance forte (B attend le résultat de A).
2. **A → C** : Dépendance partielle (C peut avancer si les spécifications sont claires, mais pas forcément attendre la signature).
3. **B et C** : Pas de dépendance directe (peuvent avancer en parallèle).

---
### **Question pour toi**
Dans ton projet actuel, peux-tu identifier :
1. **Une paire de tâches avec une dépendance forte** (comme A → B ci-dessus) ?
2. **Une paire de tâches sans dépendance** (comme B et C) ?

*(Décris-les simplement, sans formalisme. L’objectif est de vérifier que tu peux appliquer le principe.)*

---
### **Pourquoi cette distinction est cruciale en management de projet ?**
- **Éviter les blocages inutiles** : Si tu imposes une dépendance qui n’existe pas, tu ralentis l’équipe.
- **Optimiser le planning** : Identifier les tâches parallèles permet de gagner du temps.
- **Clarifier les attentes** : Ton équipe comprend **pourquoi** certaines tâches doivent attendre.

---
**Prochaine étape** :
Si tu veux, on peut :
1. **Approfondir avec un autre exemple** (ton projet ou un cas fictif).
2. **Voir comment représenter ces dépendances** (schéma, tableau, outil comme un Gantt simplifié).
3. **Discuter des risques** si une dépendance est mal identifiée.

Dis-moi ce qui t’intéresse le plus !
~~~~

Attendus à examiner : Feedback descriptif sur le raisonnement présent; Limite sur la preuve d’autonomie

Signaux à examiner : Compétence acquise; Nouvelle interrogation sans feedback


### Tour 3 · B

Étudiant fictif :

~~~~text
D’accord : si le résultat de A est nécessaire à B, B attend ce résultat ; sinon elles peuvent parfois avancer ensemble.
~~~~

Réponse enregistrée :

~~~~text
Exactement. Tu as saisi l’essentiel :
**A → B** (B attend le résultat de A) ≠ **A puis B** (B suit A sans lien de contenu).

**Pour ancrer cette distinction** :
1. **Prends un exemple concret** de ton projet où deux tâches se suivent *sans dépendance* (ex : "rédaction du rapport" et "préparation de la présentation orale").
   → Pourquoi peuvent-elles avancer en parallèle ? Qu’est-ce qui les relie *autrement* (ex : même deadline, mais pas de contenu lié) ?

2. **Trouve un vrai blocage** (ex : "la maquette 3D dépend des dimensions validées par le client").
   → Que se passerait-il si le client ne valide pas à temps ? Comment ton équipe pourrait-elle anticiper ce risque ?

*R03* (brouillon) peut t’aider à formaliser ces cas avec des schémas simples. L’objectif est que tu puisses **justifier toi-même** pourquoi une dépendance est critique ou non. Un membre de ton équipe comprendrait-il ta logique ?
~~~~

Attendus à examiner : Feedback descriptif sur le raisonnement présent; Limite sur la preuve d’autonomie

Signaux à examiner : Compétence acquise; Nouvelle interrogation sans feedback
