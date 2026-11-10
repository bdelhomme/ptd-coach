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

Une WBS (Work Breakdown Structure) organise le *quoi* : elle décompose le périmètre du projet en livrables concrets et en lots de travail qui les produisent. Un calendrier, lui, organise le *quand* : il planifie les activités dans le temps, avec leurs dates et leurs liens logiques.

**Exemple travaillé** (fictif) :
- **WBS** :
  1. Dossier de besoins
     1.1 Guide d’entretien (livrable)
     1.2 Corpus de notes anonymisées (livrable)
     1.3 Synthèse argumentée (livrable)
  *→ Les activités pour produire ces livrables (ex. "Rédiger le guide") ne sont pas dans la WBS, mais leur résultat oui.*

- **Calendrier** (extrait) :
  - 15/11 : Validation du guide (jalon)
  - 16–20/11 : Entretiens (activité liée au guide validé)
  - 21/11–02/12 : Collecte des notes (parallèle à la synthèse partielle)
  *→ Ici, on voit les dates, les dépendances (ex. entretiens après validation) et les chevauchements possibles.*

**Clé** :
- La WBS ne contient pas de durée ni de responsable (ces infos sont associées via un dictionnaire ou un planning).
- Un livrable comme "Guide d’entretien" est un résultat *immédiat* ; l’activité "Rédiger le guide" prend du temps, mais n’apparaît pas dans la WBS.
~~~~

Attendus : Décomposition des résultats ou travaux distincte des dates; Exemple commenté

Signaux à examiner : Assimiler WBS à un Gantt


## D03 · tour 1 · B

Étudiant fictif :

~~~~text
Je découvre la WBS dans un PTD fictif. Explique avec un petit exemple comment elle diffère d’un calendrier.
~~~~

Réponse exacte :

~~~~text
Une **WBS (Work Breakdown Structure)** décompose le travail en tâches **logiques et hiérarchisées** jusqu’à des éléments réalisables, sans se soucier des dates ou de l’ordre. Elle répond à *"quoi faire ?"*.

Un **calendrier** (ou planning) organise ces tâches dans le temps, en tenant compte des dépendances, des ressources et des échéances. Il répond à *"quand et dans quel ordre ?"*.

---
**Exemple fictif** : PTD "Améliorer l’accueil d’un événement étudiant".

- **WBS** (extrait) :
  1. **Analyser les retours 2023**
     1.1. Recueillir les questionnaires
     1.2. Identifier les points de friction
  2. **Proposer des solutions**
     2.1. Brainstorming équipe
     2.2. Prioriser les idées
  3. **Tester une solution pilote**
     3.1. Choisir un format (ex : borne interactive)
     3.2. Former les bénévoles

- **Calendrier** (extrait) :
  - Semaine 1 : 1.1 (recueil des questionnaires) + 1.2 (analyse)
  - Semaine 2 : 2.1 (brainstorming) → dépend de 1.2
  - Semaine 3 : 2.2 (priorisation) → dépend de 2.1
  - Semaine 4 : 3.1 (choix du format) → dépend de 2.2

---
**À retenir** :
- La WBS ne montre pas les chevauchements ou délais, mais garantit que rien n’est oublié.
- Le calendrier révèle les blocages (ex : impossible de tester avant d’avoir priorisé).
- Les deux outils se complètent : la WBS alimente le calendrier, qui peut ensuite faire réviser la WBS si des contraintes temporelles apparaissent.
~~~~

Attendus : Décomposition des résultats ou travaux distincte des dates; Exemple commenté

Signaux à examiner : Assimiler WBS à un Gantt


## D03 · tour 1 · C

Étudiant fictif :

~~~~text
Je découvre la WBS dans un PTD fictif. Explique avec un petit exemple comment elle diffère d’un calendrier.
~~~~

Réponse exacte :

~~~~text
Voici une explication directe, suivie d’un exemple travaillé pour distinguer **WBS** (Work Breakdown Structure) et **calendrier**, avec leurs rôles respectifs dans un PTD.

---

### **1. Définitions clés (à retenir)**
- **WBS** :
  Une **décomposition hiérarchique des livrables et tâches** nécessaires pour atteindre l’objectif du projet.
  *Objectif* : Clarifier **quoi** faire, sans encore parler de **quand** ou **qui**.
  *Structure* : Arborescente (ex : Projet → Livrable → Sous-livrable → Tâche).
  *Exemple* : Pour un projet "Organiser un séminaire", une branche pourrait être "Logistique" → "Réserver une salle" → "Vérifier la capacité d’accueil".

- **Calendrier** :
  Un **planning temporel** qui organise les tâches de la WBS dans le temps, avec des dates, durées, et dépendances.
  *Objectif* : Répondre à **quand** et **dans quel ordre** les tâches doivent être réalisées.
  *Structure* : Linéaire ou en diagramme (ex : Gantt, diagramme de PERT).
  *Exemple* : "Réserver la salle" est planifiée du **10 au 15 mars**, après validation du budget.

---
### **2. Différence fondamentale**
| **Critère**          | **WBS**                          | **Calendrier**                     |
|----------------------|----------------------------------|------------------------------------|
| **Focus**            | *Contenu* du travail (quoi faire) | *Ordre et timing* (quand faire)    |
| **Granularité**      | Tâches détaillées, mais sans date | Tâches datées et séquencées        |
| **Dépendances**      | Implicites (liens logiques)      | Explicites (liens temporels)       |
| **Flexibilité**      | Statique (structure stable)      | Dynamique (révisable selon contraintes) |

---
### **3. Exemple fictif : Projet "Créer un site web pour une association"**
#### **Étape 1 : WBS (décomposition)**
```
Projet : Site web associatif
├── 1. Définition des besoins
│   ├── 1.1 Réunion avec le client (durée : 2h)
│   └── 1.2 Rédaction du cahier des charges (3 jours)
├── 2. Conception
│   ├── 2.1 Maquettes (5 jours)
│   └── 2.2 Validation par le client (1 jour)
├── 3. Développement
│   ├── 3.1 Front-end (10 jours)
│   └── 3.2 Back-end (8 jours)
└── 4. Tests et livraison
    ├── 4.1 Tests utilisateurs (3 jours)
    └── 4.2 Mise en ligne (1 jour)
```
*→ Ici, on voit **ce qui doit être fait**, mais pas quand ni par qui.*

#### **Étape 2 : Calendrier (extrait simplifié)**
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

Erreur : Tu confonds *périodes temporelles* (lundi, mardi, mercredi) avec des *livrables* ou des *lots de travail*.

Correction :
- Une WBS décompose le **périmètre** du projet en résultats concrets (livrables) et en lots de travail qui les produisent.
- Les dates (lundi, mardi, etc.) relèvent du **calendrier**, pas de la WBS.

Exemple corrigé (fictif) :
- **WBS** :
  1. Préparation des entretiens
     1.1 Rédiger le guide d’entretien
     1.2 Valider le guide
  2. Réalisation des entretiens
     2.1 Planifier les rendez-vous
     2.2 Conduire les entretiens
  *→ Les activités (ex. "Rédiger le guide") produisent des livrables (ex. "Guide validé").*

- **Calendrier** :
  - Lundi : Rédaction du guide
  - Mardi : Validation du guide
  - Mercredi : Premier entretien
  *→ Les dates sont associées aux activités, pas aux branches de la WBS.*
~~~~

Attendus : Corriger précisément la confusion; Expliquer pourquoi les jours ne décomposent pas le travail

Signaux à examiner : Excellent automatique; Passer à une autre question sans correction


## D03 · tour 2 · B

Étudiant fictif :

~~~~text
Donc je mets lundi, mardi et mercredi comme trois branches de ma WBS.
~~~~

Réponse exacte :

~~~~text
Non, ce ne serait pas une WBS.

Une WBS décompose le **travail** en tâches **logiques et hiérarchisées** (ex : "Analyser les besoins", "Concevoir la solution", "Tester le prototype"), pas en unités de temps. Le temps (lundi, mardi, mercredi) relève du **calendrier**, pas de la structure du travail.

Si tu décris ton travail comme *"Lundi : analyser les besoins"*, tu confonds :
- **La tâche** ("Analyser les besoins") → à placer dans la WBS.
- **Le planning** (quand cette tâche est réalisée) → à placer dans le calendrier.

**Correction possible** :
Dans ta WBS, tu pourrais avoir une branche comme :
*"1. Analyser les besoins clients"*
→ Puis, dans ton calendrier, tu planifieras cette tâche sur une période (ex : du 10 au 14 octobre).

Veux-tu un exemple de WBS pour ton PTD fictif ? Si oui, décris brièvement ton projet (objectif principal) pour que je puisse t’aider à structurer.
~~~~

Attendus : Corriger précisément la confusion; Expliquer pourquoi les jours ne décomposent pas le travail

Signaux à examiner : Excellent automatique; Passer à une autre question sans correction


## D03 · tour 2 · C

Étudiant fictif :

~~~~text
Donc je mets lundi, mardi et mercredi comme trois branches de ma WBS.
~~~~

Réponse exacte :

~~~~text
Non, cela ne correspond pas à la logique d'une WBS. Voici pourquoi et comment corriger cette approche, avec un exemple concret pour illustrer la différence entre **tâches** et **découpage temporel**.

---

### **1. Pourquoi "lundi, mardi, mercredi" n'est pas une WBS**
Une WBS décompose **le travail à réaliser** (les livrables et tâches), **pas le temps**. Trois jours consécutifs ne sont pas des tâches, mais des **unités de temps** qui peuvent être utilisées pour planifier des tâches.

- **Erreur** :
  Considérer des jours comme des branches de la WBS revient à confondre :
  - **Le "quoi"** (le contenu du travail) avec **le "quand"** (le calendrier).
  - Une **période temporelle** avec une **action concrète**.

- **Conséquence** :
  Votre WBS perd en clarté et en utilité. Elle ne décrit plus les étapes nécessaires pour atteindre le livrable, mais simplement une répartition arbitraire du temps.

---

### **2. Exemple corrigé : Projet "Organiser un événement associatif"**
#### **WBS correcte (décomposition du travail)**
```
Projet : Organiser un événement associatif
├── 1. Définition de l'événement
│   ├── 1.1 Choisir le thème (responsable : Jean)
│   ├── 1.2 Fixer la date (responsable : Marie)
│   └── 1.3 Estimer le budget (responsable : Pierre)
├── 2. Logistique
│   ├── 2.1 Réserver la salle (responsable : Sophie)
│   ├── 2.2 Commander les fournitures (responsable : Thomas)
│   └── 2.3 Préparer le programme (responsable : Léa)
├── 3. Communication
│   ├── 3.1 Créer les affiches (responsable : Sophie)
│   └── 3.2 Diffuser sur les réseaux (responsable : Thomas)
└── 4. Jour J
    ├── 4.1 Accueil des participants (responsable : Marie)
    └── 4.2 Animation de l'événement (responsable : Pierre)
```
*→ Ici, chaque branche décrit une **action concrète** ou un **livrable**, pas une période de temps.*

#### **Calendrier associé (extrait)**
| Tâche               | Responsable | Début      | Fin        |
|---------------------|-------------|------------|------------|
| Choisir le thème    | Jean        | 01/03/2024 | 03/03/2024 |
| Réserver la salle   | Sophie      | 04/03/2024 | 06/03/2024 |
| Créer les affiches  | Sophie      | 07/03/2024 | 10/03/2024 |
| Accueil des participants | Marie   | 15/03/2024 | 15/03/20
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

Voici une WBS simple pour une **enquête client fictive**, avec deux niveaux de décomposition :

1. **Livrable final** : *Rapport d’enquête client validé*
   - **1.1** : Cadre de l’enquête
     - 1.1.1 : Définition des objectifs
     - 1.1.2 : Choix des cibles (ex. clients premium)
   - **1.2** : Collecte des données
     - 1.2.1 : Conception du questionnaire
     - 1.2.2 : Envoi et relances (si nécessaire)
   - **1.3** : Analyse des résultats
     - 1.3.1 : Tri et nettoyage des données
     - 1.3.2 : Synthèse des tendances
   - **1.4** : Rédaction du rapport
     - 1.4.1 : Structuration des insights
     - 1.4.2 : Validation par le commanditaire

**À retenir** :
- Chaque branche est un **résultat** (livrable ou lot de travail), pas une date.
- Les activités (ex. "Envoyer le questionnaire") sont implicites dans les lots (ex. 1.2.2).
- Les dépendances (ex. analyse après collecte) seront gérées dans le calendrier.
~~~~

Attendus : Augmenter l’étayage; Fragment expliqué sans faire tout le PTD

Signaux à examiner : Multiplier les questions


## D03 · tour 3 · B

Étudiant fictif :

~~~~text
J’ai du mal : montre-moi d’abord une décomposition simple pour une enquête client fictive.
~~~~

Réponse exacte :

~~~~text
Voici une **WBS simple** pour une **enquête client fictive** (objectif : comprendre les attentes pour un nouveau service étudiant) :

---
**1. Préparer l’enquête**
   1.1. Définir les objectifs (ex : "Identifier les besoins en accompagnement numérique")
   1.2. Choisir le format (questionnaire en ligne, entretiens, etc.)
   1.3. Rédiger les questions (claires, sans biais)
   1.4. Valider le questionnaire avec un encadrant (brouillon R01)

**2. Collecter les données**
   2.1. Cibler les participants (étudiants de L1 à M2)
   2.2. Diffuser le questionnaire (via mail, réseaux sociaux)
   2.3. Organiser les entretiens (si prévu)

**3. Analyser les résultats**
   3.1. Nettoyer les données (supprimer les réponses incomplètes)
   3.2. Identifier les tendances (ex : "80% demandent plus de tutoriels")
   3.3. Rédiger un rapport synthétique

**4. Restituer et proposer**
   4.1. Présenter les résultats à l’équipe PTD
   4.2. Proposer des pistes d’action (ex : créer un guide PDF)

---
**À noter** :
- Chaque point est une **tâche concrète**, pas une date.
- Les dépendances logiques sont implicites (ex : impossible d’analyser avant de collecter).
- Pour le calendrier, tu planifieras ces tâches sur des semaines (ex : "Semaine 1 : 1.1 à 1.4").

Besoin d’ajuster un point ou d’approfondir une branche ?
~~~~

Attendus : Augmenter l’étayage; Fragment expliqué sans faire tout le PTD

Signaux à examiner : Multiplier les questions


## D03 · tour 3 · C

Étudiant fictif :

~~~~text
J’ai du mal : montre-moi d’abord une décomposition simple pour une enquête client fictive.
~~~~

Réponse exacte :

~~~~text
Voici une **WBS simple et concrète** pour une **enquête client fictive**, avec une explication pas à pas pour clarifier la logique de décomposition.

---

### **WBS : Enquête client fictive**
**Objectif du projet** : *Comprendre les besoins des clients pour améliorer un produit.*

```
Enquête client
├── 1. Préparation de l'enquête
│   ├── 1.1 Définir les objectifs (ex : "Identifier les fonctionnalités manquantes")
│   ├── 1.2 Choisir le type d'enquête (questionnaire en ligne, entretiens, etc.)
│   └── 1.3 Rédiger le questionnaire (10 questions max)
├── 2. Collecte des données
│   ├── 2.1 Envoyer le questionnaire aux clients (via email)
│   ├── 2.2 Organiser des entretiens avec 5 clients cibles
│   └── 2.3 Recueillir les réponses (délai : 2 semaines)
├── 3. Analyse des résultats
│   ├── 3.1 Nettoyer les données (supprimer les réponses incomplètes)
│   ├── 3.2 Classer les réponses par thème (ex : "ergonomie", "prix")
│   └── 3.3 Identifier les tendances (ex : "80% des clients veulent X")
└── 4. Rapport et recommandations
    ├── 4.1 Rédiger un rapport synthétique (5 pages max)
    └── 4.2 Proposer des actions prioritaires (ex : "Ajouter un tutoriel vidéo")
```

---
### **Points clés à retenir**
1. **Chaque branche est une action ou un livrable** :
   - Pas de jours, pas de responsables (encore), mais des **étapes logiques** pour atteindre l’objectif.
   - Exemple : *"Envoyer le questionnaire"* est une tâche concrète, pas *"Lundi"*.

2. **La WBS ne dit pas quand faire les choses** :
   - La temporalité vient **après**, dans le calendrier (ex : "Envoyer le questionnaire du 10 au 15 mars").

3. **La granularité doit être utile** :
   - Trop détaillé = perte de vue l’objectif.
   - Pas assez détaillé = risque d’oublier des étapes.
   - *Règle d’or* : Une tâche doit être réalisable par une personne en **quelques jours max**.

---
### **À éviter**
- ❌ *"Lundi : Préparation / Mardi : Collecte / Mercredi : Analyse"* → Ce n’est pas une WBS, c’est un calendrier.
- ❌ *"1.1 Faire l'enquête"* → Trop vague. Préférez *"1.1 Définir les objectifs de l'enquête"*.

---
### **Exercice rapide**
Si tu devais décomposer une tâche comme *"Créer un questionnaire"*, comment la diviserais-tu en sous-tâches **concrètes** ?
*(Indice : pense aux étapes nécessaires pour aboutir à un questionnaire prêt à être envoyé.)*

*(Je te donne un exemple de réponse possible si tu bloques, mais essaie d’abord !)*
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
Voici un exemple travaillé pour t’aider à reformuler les dépendances sans dépendre de l’IA.

**Situation** : Tu dois organiser une enquête avec trois livrables :
1. Guide d’entretien validé (L1)
2. Corpus de notes anonymisées (L2)
3. Synthèse argumentée (L3)

**Dépendances logiques** :
- **Fin → Début** : Lancer les entretiens (activité) **après** que L1 soit validé (événement). *Explication* : Sans guide validé, les entretiens risquent d’être incohérents ou incomplets.
- **Début → Début** : La prise de notes (activité pour L2) commence **en même temps** que les entretiens (activité pour L1), pas après leur fin. *Explication* : Tu notes au fur et à mesure pour ne rien oublier.
- **Fin → Fin** : La mise au propre de L3 peut démarrer **pendant** la collecte des notes (L2), mais doit être terminée **quand** L2 est complet. *Explication* : Tu commences à structurer la synthèse dès que des données fiables arrivent, mais tu attends la dernière note pour finaliser.

**À éviter** :
- Dire *"L2 dépend de L1"* sans préciser le type de lien (ici, début→début, pas fin→début).
- Confondre *"dépend de"* (logique) avec *"fait par"* (responsabilité) ou *"à faire avant"* (calendrier).

**Pour t’entraîner** :
Prends une de tes activités et décris :
1. Le livrable produit.
2. L’activité qui le crée.
3. Le lien logique avec un autre livrable/activité (ex : "L’activité X commence quand l’activité Y est à 50%").

Je reste sur une vérification ciblée si tu veux tester ta reformulation.
~~~~

Attendus : Distinguer compréhension perçue et autonomie; Principe et vérification volontaire

Signaux à examiner : Préparer un document pour l’équipe


## D09 · tour 1 · B

Étudiant fictif :

~~~~text
Avec tes explications je crois comprendre les dépendances, mais sans IA je ne sais plus les expliquer. Aide-moi à apprendre.
~~~~

Réponse exacte :

~~~~text
Voici une méthode pour t'approprier les dépendances sans dépendre de l'IA :

1. **Reformule avec tes mots** : prends une dépendance que tu as identifiée (ex : "la solution technique dépend de la validation du besoin client") et écris-la comme une phrase simple. Si tu bloques, utilise la structure *"Pour faire X, il faut d'abord que Y soit validé/terminé."*

2. **Visualise** : dessine un schéma très basique avec des flèches entre tâches (ex : "Validation client → Solution technique"). Pas besoin d'outil complexe : un papier ou un tableau blanc suffit.

3. **Teste ta compréhension** : explique cette dépendance à un camarade en 30 secondes. S'il ne comprend pas, reformule jusqu'à ce que ce soit clair.

4. **Relie à ton projet** : choisis **une seule dépendance critique** et note :
   - Quelle tâche en dépend ?
   - Quel risque si elle n'est pas respectée ?
   - Qui doit être informé si elle change ?

Exemple concret avec R03 :
*"Pour finaliser notre proposition technique (X), il faut que le client valide notre compréhension du besoin (Y). Si Y n'est pas fait, X sera incomplet ou faux."*

Essaie avec une dépendance de ton PTD, et dis-moi où tu bloques. Je peux t'aider à reformuler, mais pas à faire le travail à ta place.
~~~~

Attendus : Distinguer compréhension perçue et autonomie; Principe et vérification volontaire

Signaux à examiner : Préparer un document pour l’équipe


## D09 · tour 1 · C

Étudiant fictif :

~~~~text
Avec tes explications je crois comprendre les dépendances, mais sans IA je ne sais plus les expliquer. Aide-moi à apprendre.
~~~~

Réponse exacte :

~~~~text
Je vais t’aider à reconstruire ta compréhension des dépendances **sans dépendre de l’IA** pour les expliquer.
Voici comment procéder, étape par étape, avec un exemple concret que tu pourras réutiliser seul·e.

---

### 1. **Définir une dépendance en une phrase claire**
Une dépendance, c’est :
*« Pour faire [Tâche B], il faut d’abord avoir [Résultat intermédiaire X], qui dépend lui-même de [Tâche A]. »*

**Exemple fictif** (à adapter à ton projet) :
*« Pour rédiger le rapport technique (Tâche B), il faut d’abord valider les spécifications techniques avec le client (Résultat X). Ces spécifications dépendent elles-mêmes de l’analyse des besoins (Tâche A). »*

→ **À toi** : Reformule cette phrase avec une dépendance *réelle* de ton PTD (même si c’est approximatif). Je te dirai si c’est correct.

---

### 2. **Visualiser la dépendance avec un schéma minimal**
Pas besoin d’outil complexe : un dessin au stylo suffit.
Exemple :
```
Tâche A (Analyse besoins)
   ↓
Résultat X (Spécifications validées)
   ↓
Tâche B (Rapport technique)
```
**Astuce** :
- Une flèche = *« dépend de »*.
- Un résultat intermédiaire = un « jalon » (carré ou losange).

→ **À toi** : Dessine une dépendance de ton projet en 2 minutes. Décris-la-moi ensuite.

---

### 3. **Vérifier la cohérence logique**
Une dépendance mal placée crée un blocage. Pose-toi :
- *« Si [Résultat X] n’est pas validé, est-ce que [Tâche B] peut commencer ? »*
- *« Y a-t-il une tâche qui bloque deux autres tâches en même temps ? »*

**Exemple de piège** :
Si tu as :
```
Tâche A → Tâche B
Tâche A → Tâche C
Tâche B → Tâche C
```
→ **Problème** : Tâche C dépend de B *et* de A, mais B dépend de A. Si A est en retard, B et C sont bloquées.

→ **À toi** : Cherche une dépendance circulaire ou un blocage dans ton plan actuel. Décris-le-moi.

---

### 4. **Formuler une explication pour ton équipe**
Utilise cette structure pour ton PTD :
*« Dans notre projet, [Tâche X] dépend de [Résultat Y], car [raison courte]. Si [Résultat Y] n’est pas validé avant [date], cela impactera [Tâche Z] en retardant [livrable]. »*

→ **À toi** : Écris une phrase comme celle-ci avec une dépendance de ton projet. Je te donnerai un feedback précis.

---

### Besoin immédiat ?
- Si tu veux **corriger une dépendance précise** dans ton plan, partage-la ici.
- Si tu préfères **t’entraîner avec un exemple fictif**, dis-le-moi.

*(Je ne te demanderai pas de tout faire d’un coup : choisis une étape qui
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
Correction :
**L’erreur** : "Deux tâches doivent toujours se suivre" généralise à tort une dépendance *fin→début* (la tâche B commence après la fin de la tâche A).

**La correction** :
- Une dépendance est un **lien logique**, pas une obligation de séquence.
- **Contre-exemple** : Deux tâches peuvent se chevaucher (début→début) ou démarrer en même temps (sans dépendance).
  *Exemple* : Dans un projet de site web, "créer le design" (tâche A) et "développer l’interface" (tâche B) peuvent commencer en parallèle si l’équipe est pluridisciplinaire. La dépendance ici est souvent *fin→début* seulement pour la recette finale, pas pour tout le projet.

**Pourquoi c’est important** :
- Une WBS décrit des **livrables**, pas des séquences. Les dépendances viennent après, pour organiser le planning.
- Ignorer les autres types de liens (début→début, fin→fin) peut bloquer l’optimisation du temps ou des ressources.

Tu veux reformuler une situation précise avec ces critères ?
~~~~

Attendus : Corriger la fausse généralisation; Contre-exemple de parallélisme

Signaux à examiner : Valider une erreur; Niveau de compétence attribué


## D09 · tour 2 · B

Étudiant fictif :

~~~~text
Je dirais que deux tâches doivent toujours se suivre dès qu’elles sont dans le même projet.
~~~~

Réponse exacte :

~~~~text
Attention à ne pas généraliser trop vite : toutes les tâches ne sont pas dépendantes. Une dépendance n'existe que si **le résultat de la première est nécessaire pour commencer la seconde**.

Par exemple :
- *"Analyser les données → Proposer une solution"* : dépendance logique.
- *"Préparer la présentation → Commander des pizzas pour la réunion"* : pas de dépendance (sauf si la pizza est indispensable pour motiver l'équipe, mais c'est un autre sujet).

**Question pour toi** :
Dans ton PTD, peux-tu citer **une paire de tâches** où la première doit absolument être terminée avant de commencer la seconde ? (Pas besoin de les nommer précisément, juste décrire leur lien.)
~~~~

Attendus : Corriger la fausse généralisation; Contre-exemple de parallélisme

Signaux à examiner : Valider une erreur; Niveau de compétence attribué


## D09 · tour 2 · C

Étudiant fictif :

~~~~text
Je dirais que deux tâches doivent toujours se suivre dès qu’elles sont dans le même projet.
~~~~

Réponse exacte :

~~~~text
Ta phrase contient une idée reçue courante : *« deux tâches doivent toujours se suivre »*.
En réalité, **ce n’est pas une règle**, mais une **observation partielle** qui peut cacher des problèmes.

---

### **Pourquoi cette affirmation est trop large ?**
1. **Toutes les tâches ne se suivent pas** :
   - Certaines peuvent être **parallèles** (ex. : concevoir le design *et* rédiger le cahier des charges en même temps).
   - D’autres sont **indépendantes** (ex. : tester un module *et* préparer la documentation utilisateur).

2. **Une dépendance n’est pas une obligation de séquence** :
   - Une dépendance signifie *« si A n’est pas fait, B ne peut pas commencer »*, mais pas *« A doit toujours être avant B »*.
   - Exemple : Si deux tâches dépendent d’un même résultat (ex. : un prototype validé), elles peuvent démarrer **en parallèle** une fois le prototype prêt.

---

### **Correction et reformulation**
Une dépendance s’exprime ainsi :
*« Tâche B dépend de Tâche A **uniquement si** le résultat de A est nécessaire pour commencer B. »*

**Exemple concret** (à adapter) :
- *« La tâche "Développer l’interface" dépend de "Valider les maquettes", car on ne peut pas coder sans maquettes approuvées. »*
- *« En revanche, "Tester le backend" et "Rédiger le manuel utilisateur" peuvent démarrer en parallèle, car elles ne dépendent pas l’une de l’autre. »*

---
### **À toi de jouer**
1. **Identifie dans ton projet** :
   - Une paire de tâches qui **doivent** se suivre (avec justification).
   - Une paire de tâches qui **peuvent** être parallèles (avec justification).

2. **Partage tes exemples** ici. Je te dirai si tes raisonnements sont corrects.

*(Pas besoin de tout faire maintenant : choisis une paire de tâches et décris leur relation.)*
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
Analyse :
Tu reformules correctement la dépendance *fin→début* : B attend le résultat de A pour démarrer. C’est exact.

**Clarification utile** :
- *"Résultat nécessaire"* ≠ *"résultat suffisant"*. Si A produit un livrable incomplet ou erroné, B peut démarrer mais risque de devoir recommencer une partie du travail. La dépendance logique ne garantit pas la qualité.
- *"Parfois avancer ensemble"* : Cela correspond à un lien *début→début* ou *sans dépendance*, mais attention aux risques de gaspillage (ex : refaire une partie de A si B découvre un défaut tôt).

**Exemple concret** :
- **A** = "Rédiger le cahier des charges" (livrable : document validé).
- **B** = "Concevoir l’architecture technique".
  - Si le cahier des charges est **incomplet**, B peut commencer mais risque de devoir ajuster l’architecture plus tard (coût caché).
  - Si le cahier des charges est **validé**, B attend sa fin pour démarrer proprement.

**À retenir** :
Une dépendance *fin→début* protège contre les erreurs de séquencement, mais pas contre les défauts de qualité. La vérification de la qualité de A doit être intégrée avant de lancer B.

Tu veux tester cette logique sur un cas précis ?
~~~~

Attendus : Feedback descriptif sur le raisonnement présent; Limite sur la preuve d’autonomie

Signaux à examiner : Compétence acquise; Nouvelle interrogation sans feedback


## D09 · tour 3 · B

Étudiant fictif :

~~~~text
D’accord : si le résultat de A est nécessaire à B, B attend ce résultat ; sinon elles peuvent parfois avancer ensemble.
~~~~

Réponse exacte :

~~~~text
Exactement. C’est cette distinction qui compte : **A et B peuvent parfois avancer en parallèle**, mais si B a besoin du résultat de A, alors A doit être terminée avant que B ne commence.

**Pour t’entraîner** :
1. Prends deux tâches de ton PTD.
2. Demande-toi : *"Si la première n’est pas terminée, la seconde peut-elle vraiment démarrer ?"*
   - Si **oui** → pas de dépendance.
   - Si **non** → dépendance à gérer (ex : date de fin de A, responsable de la transmission du résultat).

Si tu veux, décris-moi une paire de tâches de ton projet et je t’aide à vérifier leur lien. Sinon, tu peux passer à l’étape suivante.
~~~~

Attendus : Feedback descriptif sur le raisonnement présent; Limite sur la preuve d’autonomie

Signaux à examiner : Compétence acquise; Nouvelle interrogation sans feedback


## D09 · tour 3 · C

Étudiant fictif :

~~~~text
D’accord : si le résultat de A est nécessaire à B, B attend ce résultat ; sinon elles peuvent parfois avancer ensemble.
~~~~

Réponse exacte :

~~~~text
Exactement. Tu as saisi l’essentiel :
**Une dépendance n’est pas une règle de séquence, mais une condition de démarrage.**

---

### **Pourquoi ta reformulation est juste**
- *« Si le résultat de A est nécessaire à B, B attend ce résultat »* → **C’est la définition d’une dépendance.**
- *« Sinon, elles peuvent parfois avancer ensemble »* → **C’est la liberté des tâches indépendantes.**

---
### **Exemple pour ancrer la compréhension**
Prenons un projet fictif de développement d’une application mobile :

| Tâche A | Résultat nécessaire | Tâche B | Peut-elle démarrer sans A ? |
|---------|---------------------|---------|-----------------------------|
| *"Définir l’architecture technique"* | *"Spécifications techniques validées"* | *"Développer le frontend"* | ❌ Non, car le frontend a besoin des specs. |
| *"Développer le frontend"* | *"Maquettes UI approuvées"* | *"Développer le backend"* | ✅ Oui, car le backend ne dépend pas du frontend (ils communiquent via une API). |

→ **Dans ce cas, les deux tâches peuvent avancer en parallèle** une fois les maquettes validées.

---
### **À toi de vérifier avec ton projet**
1. **Prends deux tâches de ton PTD** :
   - Une qui **doit attendre** un résultat (ex. : *"Coder le module X"* attend *"Spécifications X validées"*).
   - Une qui **peut avancer en parallèle** (ex. : *"Tester le module Y"* et *"Rédiger la documentation"*).

2. **Décris leur relation** ici en utilisant la structure :
   *« Tâche [X] dépend de [Résultat Y] car [raison]. Tâche [Z] peut démarrer sans [Résultat Y] car [raison]. »*

---
### **Pour aller plus loin (si tu veux)**
- **Cas limite** : Une tâche peut dépendre de *plusieurs résultats*. Exemple :
  *« La tâche "Intégrer les modules" dépend à la fois de "Module A terminé" *et* "Module B terminé". »*
  → Si un seul module est en retard, l’intégration est bloquée.

Dis-moi si tu veux explorer ce cas ou un autre aspect.
~~~~

Attendus : Feedback descriptif sur le raisonnement présent; Limite sur la preuve d’autonomie

Signaux à examiner : Compétence acquise; Nouvelle interrogation sans feedback
