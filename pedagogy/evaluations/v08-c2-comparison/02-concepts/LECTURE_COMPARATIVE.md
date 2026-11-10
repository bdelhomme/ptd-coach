# Comparaison à lire avant la clé

Messages fictifs, sorties réelles ou simulations explicitement marquées. Aucun verdict humain ; les labels peuvent être devinés par le style.


## P01 · tour 1 · A

Étudiant fictif :

~~~~text
Dans un exemple fictif, B peut commencer après le début de A, sans attendre sa fin. Cela veut dire qu’il n’y a aucune dépendance ?
~~~~

Réponse exacte :

~~~~text
Corriger :
L’exemple montre une dépendance début-début (A → début de B), pas l’absence de dépendance.
Une dépendance existe dès qu’une activité conditionne le démarrage d’une autre, même partiellement.
~~~~

Attendus : Corriger la fausse équivalence parallélisme/indépendance; Décrire un lien début-début sans cours exhaustif

Signaux à examiner : Définition universelle fin-début; Déduire indépendance du chevauchement


## P01 · tour 1 · B

Étudiant fictif :

~~~~text
Dans un exemple fictif, B peut commencer après le début de A, sans attendre sa fin. Cela veut dire qu’il n’y a aucune dépendance ?
~~~~

Réponse exacte :

~~~~text
Non, cela signifie qu'il y a une **dépendance partielle** entre A et B, et non une absence totale de dépendance.

### Explication :
- **Aucune dépendance** : B pourrait commencer et se terminer sans que A n'ait commencé.
- **Dépendance partielle** : B peut commencer **après le début de A**, mais pas avant. Cela implique que :
  - Une partie de A doit être réalisée avant que B ne puisse démarrer (par exemple, une étape préliminaire ou une ressource partagée).
  - B ne peut pas être totalement indépendant de A, mais il n'a pas besoin d'attendre la fin complète de A.

### Exemple concret :
- **A** : "Rédiger le cahier des charges" (tâche longue).
- **B** : "Commencer la conception technique" (peut démarrer une fois que les grandes lignes du cahier des charges sont posées, même si la rédaction n'est pas terminée).

### En termes de planification :
- Cela se modélise souvent par une **dépendance de type "Start-to-Start" (SS)** dans les diagrammes de réseau (comme un PERT ou un Gantt).
- Cela réduit les temps d'attente, mais nécessite une coordination pour éviter les conflits (ex. : B ne doit pas utiliser une ressource que A modifie encore).

### À vérifier dans votre plan :
- Si B dépend d'une **partie spécifique** de A, cette dépendance doit être explicitée dans votre documentation (ex. : "B commence quand 30% de A est validé").
- Cela évite les blocages imprévus.

---
**Question pour approfondir** :
Si votre équipe a identifié ce type de dépendance, comment comptez-vous la documenter pour que chacun comprenne clairement le point de départ de B ? (Ex. : critère de déclenchement, responsable de validation intermédiaire ?)
~~~~

Attendus : Corriger la fausse équivalence parallélisme/indépendance; Décrire un lien début-début sans cours exhaustif

Signaux à examiner : Définition universelle fin-début; Déduire indépendance du chevauchement


## P01 · tour 1 · C

Étudiant fictif :

~~~~text
Dans un exemple fictif, B peut commencer après le début de A, sans attendre sa fin. Cela veut dire qu’il n’y a aucune dépendance ?
~~~~

Réponse exacte :

~~~~text
Non, cela signifie qu'il y a une **dépendance partielle** : B peut démarrer dès qu'une partie de A est avancée, mais pas avant. Ce n'est pas une absence totale de dépendance.

Exemple concret :
- **A** = "Finaliser l'analyse des besoins" (3 jours)
- **B** = "Prototyper une solution" (5 jours)
→ B peut commencer après 1 jour de A (quand les besoins principaux sont identifiés), mais pas dès le premier jour.

**À vérifier** :
- Quelles tâches de A doivent être terminées avant de lancer B ?
- Y a-t-il un risque si B commence trop tôt (ex. : solution basée sur des besoins incomplets) ?

Si aucune tâche de A n'est nécessaire pour B, alors oui, il n'y a pas de dépendance. Sinon, c'est une dépendance avec chevauchement.

*(Ressource utile : R03, section "Identifier les dépendances")*
~~~~

Attendus : Corriger la fausse équivalence parallélisme/indépendance; Décrire un lien début-début sans cours exhaustif

Signaux à examiner : Définition universelle fin-début; Déduire indépendance du chevauchement


## P01 · tour 2 · A

Étudiant fictif :

~~~~text
Donc une dépendance peut autoriser le chevauchement, en contraignant le début ou la fin. C’est cette distinction qui me manquait ; on peut arrêter.
~~~~

Réponse exacte :

~~~~text
Conclure :
Tu as reformulé que la dépendance (début-début, fin-début, etc.) encadre le chevauchement sans l’interdire, en contraignant un repère temporel précis. Cela montre la distinction entre absence de dépendance et dépendance autorisant un parallélisme partiel.
~~~~

Attendus : Feedback descriptif et clôture; Aucun nouvel exercice

Signaux à examiner : Menu ou nouvelle sollicitation


## P01 · tour 2 · B

Étudiant fictif :

~~~~text
Donc une dépendance peut autoriser le chevauchement, en contraignant le début ou la fin. C’est cette distinction qui me manquait ; on peut arrêter.
~~~~

Réponse exacte :

~~~~text
Oui, exactement. La dépendance **autorise le chevauchement** en contraignant soit le **début**, soit la **fin** (ou les deux) des tâches concernées. C’est cette nuance qui permet d’optimiser un planning sans ignorer les contraintes réelles.

### Clarification des cas possibles :
1. **Début contraint** (ex. : *Start-to-Start* ou *SS*) :
   - B ne peut commencer qu’après le début de A (mais pas forcément après sa fin).
   - *Exemple* : B = "Tester le module X" peut démarrer dès que A = "Développer une première version du module X" a commencé (même si A n’est pas terminée).

2. **Fin contrainte** (ex. : *Finish-to-Start* ou *FS*) :
   - B ne peut commencer qu’après la fin de A.
   - *Exemple* : B = "Livrer le rapport final" ne peut commencer qu’après A = "Valider le rapport par le client".

3. **Chevauchement complet** (rare) :
   - B peut commencer et finir **avant** A (ex. : tâches indépendantes).
   - *Exemple* : A = "Concevoir l’interface" et B = "Rédiger la documentation utilisateur" peuvent se chevaucher librement.

---

### Pourquoi cette distinction est utile ?
- **Éviter les blocages** : En identifiant clairement les contraintes (début/fin), vous évitez les attentes inutiles ou les conflits de ressources.
- **Optimiser le temps** : Un chevauchement partiel (ex. : *SS*) permet de gagner du temps sans sacrifier la qualité.
- **Documenter les critères** : Pour les dépendances *SS*, précisez **quel critère déclenche B** (ex. : "B commence quand A a atteint 50% de son avancement").

---
**Pour aller plus loin** :
Si votre équipe utilise un diagramme de Gantt ou un PERT, comment pourriez-vous représenter cette dépendance *Start-to-Start* ? (Ex. : flèche en pointillés avec une annotation ?) Cela pourrait aider à visualiser les chevauchements sans ambiguïté.
~~~~

Attendus : Feedback descriptif et clôture; Aucun nouvel exercice

Signaux à examiner : Menu ou nouvelle sollicitation


## P01 · tour 2 · C

Étudiant fictif :

~~~~text
Donc une dépendance peut autoriser le chevauchement, en contraignant le début ou la fin. C’est cette distinction qui me manquait ; on peut arrêter.
~~~~

Réponse exacte :

~~~~text
Exactement. Une dépendance fixe des contraintes temporelles (début/fin) mais n'interdit pas nécessairement le chevauchement, tant que les conditions sont respectées.

Si tu veux creuser un cas précis dans ton PTD, je peux t'aider à identifier les dépendances critiques ou à reformuler les règles de synchronisation pour l'équipe. Sinon, bonne continuation.
~~~~

Attendus : Feedback descriptif et clôture; Aucun nouvel exercice

Signaux à examiner : Menu ou nouvelle sollicitation


## P02 · tour 1 · A

Étudiant fictif :

~~~~text
Dans un planning fictif je mets « réunion de validation du guide » comme jalon de deux heures. Est-ce précis ?
~~~~

Réponse exacte :

~~~~text
Corriger.

Un jalon est un événement repère sans durée. Ici, « réunion de validation du guide » est une activité (deux heures), pas un jalon.

Pour le planning, modélisez :
- Activité : « Réunion de validation du guide » (2h)
- Jalon : « Guide validé » (durée nulle), placé à la fin de l'activité.
~~~~

Attendus : Distinguer activité de réunion et événement guide accepté; Durée du travail distincte du repère

Signaux à examiner : Toute réunion est un jalon; Le travail de validation est instantané


## P02 · tour 1 · B

Étudiant fictif :

~~~~text
Dans un planning fictif je mets « réunion de validation du guide » comme jalon de deux heures. Est-ce précis ?
~~~~

Réponse exacte :

~~~~text
Non, ce n'est pas assez précis pour un jalon utile.

**Pourquoi ?**
Un jalon doit indiquer *quand* et *par qui* la validation est attendue, pas seulement *quoi*. Ici, la durée (2h) est un détail d'organisation interne, pas une condition de passage à l'étape suivante.

**Exemple de reformulation plus précis :**
*« Validation du guide par [nom du client ou du responsable] le [date] avant 16h »*

**Ce que cela change :**
- Le jalon devient un *point de décision* (le guide est-il validé ?) plutôt qu'une simple tâche.
- La responsabilité est claire (évite les "on verra").
- La date permet de synchroniser les dépendances (ex. : "si validation le 15/05, alors finalisation du support le 16/05").

**À vérifier ensuite :**
- La validation dépend-elle d'une autre tâche ? (ex. : le guide doit être relu en interne avant)
- Qui prépare les documents pour cette réunion ? (responsable temporaire)

*Besoin d'ajuster un planning existant ou d'en construire un nouveau ?*
~~~~

Attendus : Distinguer activité de réunion et événement guide accepté; Durée du travail distincte du repère

Signaux à examiner : Toute réunion est un jalon; Le travail de validation est instantané


## P02 · tour 1 · C

Étudiant fictif :

~~~~text
Dans un planning fictif je mets « réunion de validation du guide » comme jalon de deux heures. Est-ce précis ?
~~~~

Réponse exacte :

~~~~text
Non, ce n'est pas assez précis pour un jalon utile.

Un jalon doit indiquer **ce qui est validé**, **par qui** et **quand** (date/heure), pas seulement une activité. Par exemple :
*« Validation du guide utilisateur par le client le 15/05 à 14h »*.

Cela permet de :
- Vérifier si le livrable est prêt à temps.
- Identifier les dépendances (ex. : le guide doit être finalisé avant cette réunion).
- Ajuster le planning si la validation est reportée.

Tu peux préciser le statut du document (brouillon, version 1, etc.) et les critères de validation (ex. : « conforme au besoin client »).
~~~~

Attendus : Distinguer activité de réunion et événement guide accepté; Durée du travail distincte du repère

Signaux à examiner : Toute réunion est un jalon; Le travail de validation est instantané


## P02 · tour 2 · A

Étudiant fictif :

~~~~text
Je sépare la réunion, activité de deux heures, et « guide accepté », jalon sans durée, si l’accord est effectivement obtenu.
~~~~

Réponse exacte :

~~~~text
Analyser.

Votre distinction est correcte :
- L’activité « Réunion de validation du guide » (2h) produit un résultat : le guide est présenté et discuté.
- Le jalon « Guide accepté » marque l’aboutissement de cette activité, à condition que l’accord soit formellement obtenu.

Cela reflète bien la définition : un jalon est un événement repère (ici, l’acceptation), sans durée, tandis que l’activité est le travail qui y mène.

Si l’accord n’est pas garanti, le jalon reste incertain. Dans ce cas, le risque « Le client pourrait ne pas accepter le guide » peut être documenté, avec une réponse possible (ex. : itération de modification avant nouvelle validation).
~~~~

Attendus : Confirmer les distinctions exactes sans sur-certification; Pas de question supplémentaire par défaut

Signaux à examiner : Accord supposé validé; Nouvel exercice automatique


## P02 · tour 2 · B

Étudiant fictif :

~~~~text
Je sépare la réunion, activité de deux heures, et « guide accepté », jalon sans durée, si l’accord est effectivement obtenu.
~~~~

Réponse exacte :

~~~~text
Exactement. Cette séparation est une bonne pratique pour clarifier **ce qui est un événement temporel** (la réunion) et **ce qui est un résultat validé** (le jalon).

### Points forts de cette approche :
1. **Distinction claire** :
   - *Activité* : "Réunion de validation du guide" (2h, responsable : [X], date : [Y])
   - *Jalon* : "Guide accepté" (condition : signature ou email de validation, date cible : [Z])

2. **Flexibilité** :
   - Si la réunion est reportée, le jalon reste valide tant que la validation n'est pas obtenue.
   - Si la réunion a lieu mais que le guide n'est pas accepté, le jalon n'est pas atteint.

3. **Alignement avec R03** :
   Le jalon devient un *résultat intermédiaire* (compétence A2 : "Définir les résultats intermédiaires"), et la réunion est une *tâche* (compétence A3 : "Identifier les tâches").

### À vérifier maintenant :
- **Dépendance** : La réunion de validation dépend-elle d'une autre tâche ? (ex. : "guide relu et corrigé avant la réunion")
- **Critère d'acceptation** : Comment sait-on que le guide est "accepté" ? (ex. : email de validation, signature, etc.)
- **Responsable** : Qui prépare la réunion ? Qui valide le guide ?

*Si tu veux tester cette structure sur un exemple concret ou un extrait de planning, je peux t'aider à l'analyser.*
~~~~

Attendus : Confirmer les distinctions exactes sans sur-certification; Pas de question supplémentaire par défaut

Signaux à examiner : Accord supposé validé; Nouvel exercice automatique


## P02 · tour 2 · C

Étudiant fictif :

~~~~text
Je sépare la réunion, activité de deux heures, et « guide accepté », jalon sans durée, si l’accord est effectivement obtenu.
~~~~

Réponse exacte :

~~~~text
Oui, c’est une séparation plus claire et cohérente.

- **« Réunion de validation du guide »** : activité de deux heures, avec un responsable et un ordre du jour précis.
- **« Guide accepté »** : jalon (sans durée), qui marque l’aboutissement de la validation.

Cela permet de distinguer :
1. **Ce qui est fait** (la réunion).
2. **Ce qui est obtenu** (l’accord).

Si tu veux renforcer la rigueur, tu peux ajouter :
- **Qui participe** à la réunion.
- **Quels documents** sont présentés.
- **Quels critères** définissent un accord (ex. : signature, email de validation).

Cela évite les ambiguïtés sur ce qui est considéré comme "terminé".
~~~~

Attendus : Confirmer les distinctions exactes sans sur-certification; Pas de question supplémentaire par défaut

Signaux à examiner : Accord supposé validé; Nouvel exercice automatique


## P03 · tour 1 · A

Étudiant fictif :

~~~~text
Client fictif : l’échéance de réponse est déjà passée hier, sans réponse. Je note « risque : client déjà en retard ». Corrige mon registre.
~~~~

Réponse exacte :

~~~~text
**Correction :**
L'énoncé « risque : client déjà en retard » est un **problème constaté** (l'échéance est dépassée), pas un risque.

**Correction proposée :**
« Risque : nouveau retard possible si le client ne répond pas aujourd'hui » (incertitude future).

**Raison :**
Un risque est une **incertitude** pouvant affecter un objectif. Un problème déjà survenu relève du suivi, pas de l'analyse des risques.
~~~~

Attendus : Problème rapporté vs risque futur; Aucune cause ou probabilité inventée

Signaux à examiner : Risque forcément déjà réalisé; Cause certaine


## P03 · tour 1 · B

Étudiant fictif :

~~~~text
Client fictif : l’échéance de réponse est déjà passée hier, sans réponse. Je note « risque : client déjà en retard ». Corrige mon registre.
~~~~

Réponse exacte :

~~~~text
Voici une correction précise et une explication pour t'aider à reformuler ce risque de manière plus opérationnelle et moins subjective :

**Ton registre actuel :**
*« risque : client déjà en retard »*
→ Problèmes identifiés :
- Formulation passive ("déjà en retard") qui attribue une responsabilité externe sans action concrète.
- Pas de lien clair avec l’impact sur le projet (ex. : blocage de tâches, retard de livrable).
- Le terme "risque" est correct, mais la description manque de neutralité et de précision.

---

**Correction proposée :**
*« Risque : absence de validation client sur le besoin (échéance dépassée hier). Impact potentiel : impossibilité de démarrer les tâches dépendantes (ex. : conception technique) d’ici [date]. Option d’atténuation : relance immédiate par [responsable] avec demande de confirmation écrite sous 48h. »*

**Pourquoi cette version ?**
1. **Faits objectifs** :
   - L’échéance est dépassée (fait vérifiable).
   - L’absence de validation est un blocage identifié (pas une accusation).

2. **Impact mesurable** :
   - Exemple concret de tâches bloquées (conception technique).
   - Délai réaliste pour une relance (48h).

3. **Action corrective** :
   - Désigne un responsable (à adapter à ton équipe).
   - Précise un objectif clair (confirmation écrite).

---
**Variante plus concise (si tu préfères) :**
*« Risque : validation client non reçue à échéance (hier). Conséquence : retard possible sur les tâches critiques (ex. : [tâche X]). Mesure : relance par [nom] avec échéance de réponse fixée à [date]. »*

---
**À toi de jouer :**
- Complète les éléments entre crochets avec les détails de ton projet.
- Vérifie si cette formulation correspond à ce que tu veux exprimer.

*Question pour aller plus loin (si tu veux creuser) :*
Est-ce que cette description de risque te semble suffisante pour déclencher une action immédiate dans ton équipe ? Si non, quel autre élément manquerait selon toi ?
~~~~

Attendus : Problème rapporté vs risque futur; Aucune cause ou probabilité inventée

Signaux à examiner : Risque forcément déjà réalisé; Cause certaine


## P03 · tour 1 · C

Étudiant fictif :

~~~~text
Client fictif : l’échéance de réponse est déjà passée hier, sans réponse. Je note « risque : client déjà en retard ». Corrige mon registre.
~~~~

Réponse exacte :

~~~~text
Ton observation est pertinente, mais la formulation peut être plus précise et neutre pour l'équipe.

**Suggestion :**
*« Le client n’a pas répondu à notre proposition dans les délais annoncés. Risque identifié : retard de validation externe, avec impact possible sur le planning interne. »*

Cela :
- **Décrit un fait** (absence de réponse) sans interprétation hâtive ("déjà en retard" suppose une intention).
- **Relie le risque à un impact concret** (validation externe bloquée).
- **Ouvre une piste d’action** (examiner les alternatives si la validation tarde).

Si tu veux creuser les causes possibles (surcharge, désaccord, oubli), tu peux ajouter une note séparée pour l’équipe, sans mélanger observation et hypothèses.
~~~~

Attendus : Problème rapporté vs risque futur; Aucune cause ou probabilité inventée

Signaux à examiner : Risque forcément déjà réalisé; Cause certaine


## P03 · tour 2 · A

Étudiant fictif :

~~~~text
Le retard passé est un problème ; un report des entretiens reste un risque. Et une réponse anticipée pour la prochaine étape pourrait être une opportunité.
~~~~

Réponse exacte :

~~~~text
**Analyse :**
Tu reformules correctement :
- Le retard passé est un **problème** (fait avéré).
- Le report des entretiens est un **risque** (incertitude future).
- Une réponse anticipée est une **opportunité** (événement incertain positif).

**Clarification utile :**
Un risque peut être **positif** (opportunité) ou **négatif** (menace). Ici, la réponse anticipée est bien une opportunité liée au même événement (la réponse du client).

**Exemple pour ancrer :**
- *Problème* : « Le client n’a pas répondu à l’échéance du 10/11. »
- *Risque* : « Si le client répond tard, les entretiens pourraient être décalés. »
- *Opportunité* : « Si le client répond aujourd’hui, la prochaine étape pourrait démarrer plus tôt. »
~~~~

Attendus : Feedback précis sur passé/futur et opportunité; Ne pas demander un exercice de plus

Signaux à examiner : Félicitation automatique ou compétence acquise


## P03 · tour 2 · B

Étudiant fictif :

~~~~text
Le retard passé est un problème ; un report des entretiens reste un risque. Et une réponse anticipée pour la prochaine étape pourrait être une opportunité.
~~~~

Réponse exacte :

~~~~text
Voici une reformulation qui intègre tes précisions tout en restant dans un registre **factuel, neutre et actionnable** pour un plan de projet. Je distingue clairement les éléments que tu as ajoutés :

---

**Version structurée :**
1. **Problème identifié (fait passé) :**
   *« Problème : échéance de validation client dépassée hier (retard confirmé). »*

2. **Risque actuel (dépendant du client) :**
   *« Risque : report possible des entretiens de clarification, impactant le planning des tâches [préciser si connu, ex. : "analyse des besoins"]. »*
   → *Pourquoi cette formulation ?*
   - "Report possible" est plus précis que "reste un risque" (qui est redondant avec le mot "risque").
   - L'impact est lié à une activité concrète (ex. : entretiens = source de données pour la conception).

3. **Opportunité (si réponse anticipée) :**
   *« Opportunité : une réponse client reçue avant [date] permettrait de démarrer [tâche Y] avec [X jours] d’avance, réduisant la pression sur le jalon [nom du jalon]. »*
   → *Exemple concret :*
   Si les entretiens sont prévus pour affiner les spécifications, une réponse anticipée pourrait permettre de commencer la maquette dès [date], évitant un goulot d’étranglement.

---

**Pourquoi cette structure ?**
- **Séparation claire** : Problème (passé) / Risque (futur incertain) / Opportunité (scénario positif).
- **Terminologie projet** : Utilise des termes comme "impact", "jalon", ou "tâche" pour ancrer dans le vocabulaire du PTD.
- **Neutralité** : Évite les jugements ("le client est lent") au profit de descriptions factuelles.

---
**À toi d’adapter :**
- Remplace les éléments entre crochets ([tâche Y], [X jours], etc.) par les détails de ton projet.
- Si tu veux ajouter une **mesure d’atténuation** pour le risque (ex. : "prévoir une version simplifiée des entretiens en parallèle"), tu peux l’intégrer sous le risque.

---
**Question pour vérifier la compréhension :**
Est-ce que cette reformulation te permet de :
1. Distinguer clairement ce qui est déjà arrivé (problème) de ce qui pourrait arriver (risque/opportunité) ?
2. Identifier des actions concrètes pour chaque cas ?

*(Si tu veux affiner un point précis, dis-le-moi.)*
~~~~

Attendus : Feedback précis sur passé/futur et opportunité; Ne pas demander un exercice de plus

Signaux à examiner : Félicitation automatique ou compétence acquise


## P03 · tour 2 · C

Étudiant fictif :

~~~~text
Le retard passé est un problème ; un report des entretiens reste un risque. Et une réponse anticipée pour la prochaine étape pourrait être une opportunité.
~~~~

Réponse exacte :

~~~~text
D'accord, reformulons pour distinguer **faits**, **risques** et **opportunités** sans mélanger les niveaux.

**Version ajustée :**
*« Le client n’a pas répondu à notre proposition dans les délais (fait). Cela crée un risque : report des entretiens et décalage du planning (conséquence). En parallèle, une réponse anticipée pour la prochaine étape serait une opportunité à anticiper (ex. : finaliser X en avance si validation reçue). »*

Cela permet à l’équipe de :
1. **Clarifier l’impact** (retard = blocage possible).
2. **Identifier une piste proactive** (anticiper une validation pour gagner du temps).
3. **Éviter de confondre cause et effet** (le retard n’est pas forcément une faute, mais un facteur à gérer).

Si tu veux prioriser une action immédiate (ex. : relance formelle, vérification des canaux de contact), précise-la séparément.
~~~~

Attendus : Feedback précis sur passé/futur et opportunité; Ne pas demander un exercice de plus

Signaux à examiner : Félicitation automatique ou compétence acquise
