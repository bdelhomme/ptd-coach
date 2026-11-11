# Lecture comparative par scénario

Consulter la clé après la lecture. L'identité peut rester reconnaissable au style.

## TX05 · Deux demandes de plus, même date

Travail laissé à l'étudiant ou à l'équipe — Chiffrer ou qualifier les impacts avec l’équipe et faire arbitrer le périmètre.

### Tour 1

~~~~text
Pour notre prototype de prêt de matériel, le commanditaire ajoute des alertes et un export. Il veut garder la date de remise. On a deux jeudis. Dis-nous quoi lui répondre.
~~~~

Attendus proposés · Proposer une analyse d’impact minimale avant engagement / Donner une formulation professionnelle qui ouvre un choix de périmètre ou délai

Points de vigilance · Promettre les deux ajouts ou choisir le périmètre pour l’équipe / Inventer la charge / Imposer un dispositif lourd

**Variante A**

~~~~text
**Analyser** : Le commanditaire souhaite ajouter des fonctionnalités (alertes, export) tout en conservant la date de remise initiale. Avec deux jeudis disponibles, il faut clarifier si ces ajouts sont prioritaires ou négociables.

**Réponse à proposer** :
*"Pour intégrer les alertes et l’export sans repousser la date, il faudrait soit réduire le périmètre actuel (ex : simplifier une fonctionnalité existante), soit accepter un risque sur la qualité (tests limités). Sinon, la date doit être reportée. Quelle est votre priorité : livrer à temps avec un scope réduit, ou livrer complet avec un délai ajusté ?"*

*(Cela force le commanditaire à arbitrer entre scope, temps et qualité, sans imposer de solution.)*
~~~~

**Variante B**

~~~~text
**Analyse** : Le commanditaire demande deux ajouts (alertes + export) sans modifier la date de remise. Avec deux jeudis disponibles, il faut clarifier si ces ajouts sont prioritaires ou si la date est négociable.

**Réponse à proposer** :
*"Nous pouvons intégrer les alertes et l’export, mais cela peut impacter le périmètre ou la date. Souhaitez-vous :
1) Garder la date et réduire d’autres fonctionnalités ?
2) Accepter un report pour inclure ces éléments ?
3) Prioriser l’un des deux ajouts ?"*

*(Fonction dominante : **analyser** – évaluer les compromis sans imposer de solution.)*
~~~~

**Variante C**

~~~~text
**Analyse** : La demande du commanditaire modifie le périmètre (ajout de fonctionnalités : alertes + export) tout en maintenant une contrainte forte (date de remise inchangée). Avec seulement deux jeudis restants, l’impact sur le planning et les ressources doit être évalué avant toute réponse.

**Réponse à formuler** :
*"Nous notons votre demande d’ajouter des alertes et un export. Pour maintenir la date de remise, nous devons vérifier :
1. **Périmètre** : Ces ajouts remplacent-ils des éléments existants ou s’y ajoutent-ils ?
2. **Temps** : Le développement de ces fonctionnalités est-il compatible avec les deux jeudis restants ?
3. **Priorités** : Si le temps manque, quelles fonctionnalités du prototype actuel pourraient être reportées ?

Nous vous proposons d’examiner ensemble ces points avant de valider le changement. Souhaitez-vous un arbitrage sur les priorités ?"*

**Pourquoi** : La fiche **M06 – Examiner une demande de changement** (brouillon) souligne l’importance de clarifier l’impact avant toute décision. Ici, la contrainte temps rend la vérification des compromis indispensable.
~~~~

### Tour 2

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

Attendus proposés · Reprendre exactement le caractère conditionnel et le périmètre export de démonstration / Signaler que les alertes et la portée de l’accord restent à clarifier

Points de vigilance · Assimiler le oui partiel à une validation complète / Prétendre enregistrer ou communiquer la décision

**Variante A**

~~~~text
**Corriger** :
L'erreur est de généraliser *"tout est validé"* alors que seul **l'export de démonstration** est accepté **sous condition** (*"si le prêt marche"*).

**Correction** :
*"Validé : export de démonstration (sous réserve du bon fonctionnement du prêt). À confirmer : alertes et périmètre global."*

**Raison** : Le compte rendu doit refléter la condition et ne pas valider implicitement les autres éléments (alertes, date).
~~~~

**Variante B**

~~~~text
**Correction** :
Le binôme a écrit une validation totale ("tout est validé"), alors que le client a conditionné l'export à la réussite du prêt.

**Proposition de reformulation** :
*"Export de démonstration validé sous réserve que le prêt fonctionne."*

*(Fonction dominante : **corriger** – identifier l'erreur et proposer une version exacte.)*
~~~~

**Variante C**

~~~~text
**Correction** :
Remplacez *"tout est validé"* par :
*"Demande notée : export de démonstration **sous condition** que la fonction de prêt soit opérationnelle. À valider après test de cette condition. Décision en attente."*

**Raison** :
- La réponse du client est **conditionnelle** (l'export dépend du bon fonctionnement du prêt).
- *"Tout est validé"* ignore cette condition et suppose un accord inconditionnel, ce qui est faux.
- La fiche **M06 – Examiner une demande de changement** (brouillon) rappelle qu’une demande doit être **explicite** sur ses critères d’acceptation. Ici, le test du prêt est un prérequis à confirmer.
~~~~

## TX07 · Rédige notre cahier des charges

Travail laissé à l'étudiant ou à l'équipe — Rassembler les preuves, écrire les exigences du projet et les faire confirmer.

### Tour 1

~~~~text
Rédige notre cahier des charges. Tout ce qu’on sait, c’est que le service de prêt a des retours difficiles à retrouver et qu’on rend une maquette en fin de semestre.
~~~~

Attendus proposés · Proposer une trame courte et commencer avec les deux faits fournis / Laisser utilisateurs, contraintes et critères à confirmer, avec une première action concrète

Points de vigilance · Remplir des exigences ou des seuils inventés / Refuser toute aide rédactionnelle / Déclarer le cahier validé

**Variante A**

~~~~text
La fiche **M03 – Construire progressivement le cahier des charges** (brouillon) propose une trame adaptée à votre situation. Elle permet de structurer les informations disponibles et d'identifier les inconnues à clarifier avec le commanditaire (ici, probablement votre enseignant ou un représentant du service de prêt).

**Application proportionnée** :
1. **Objectif** : Faciliter la localisation des retours de prêts.
2. **Périmètre** : Système ou processus pour suivre les objets retournés (à préciser : types d'objets, volume, etc.).
3. **Besoins/sources** : "Retours difficiles à retrouver" (source : service de prêt) ; "Rendre une maquette en fin de semestre" (source : consigne pédagogique).
4. **Exigences vérifiables** : Exemple fictif : *"La maquette doit permettre de visualiser l'état des retours en temps réel"* (à valider).
5. **Inconnues** : Fréquence de mise à jour, nombre d'utilisateurs, contraintes techniques, etc. → Marquer *"à discuter"*.

**Prochaine étape** : Complétez les points manquants avec votre équipe (ex : "Quels objets sont concernés ?") avant de soumettre une version pour validation. La trame est un support, pas une norme : adaptez-la à votre contexte.
~~~~

**Variante B**

~~~~text
**Cahier des charges – Projet : Amélioration du suivi des retours de prêt**

**1. Contexte et problème**
Le service de prêt rencontre des difficultés à localiser et gérer les retours d’objets (livres, matériel, etc.). Cela entraîne des retards, des pertes ou des erreurs de réintégration dans le stock.

**2. Objectif principal**
Concevoir une **maquette** (prototype non fonctionnel ou semi-fonctionnel) qui propose une solution pour :
- **Identifier** clairement les retours (ex. : code-barres, QR code, étiquette RFID).
- **Suivre** leur statut (en attente, vérifié, réintégré).
- **Faciliter** leur recherche (ex. : base de données simplifiée, interface de filtrage).

**3. Livrables attendus**
- Une **maquette** (papier, numérique ou physique) illustrant le processus amélioré.
- Un **document d’accompagnement** expliquant les choix (ex. : pourquoi des QR codes plutôt que des listes manuelles ?).
- Une **présentation orale** (si demandée) pour démontrer la solution.

**4. Contraintes**
- **Temps** : Livraison en fin de semestre (date à préciser).
- **Ressources** : Équipe de 7 personnes, outils disponibles (ex. : Figma, Excel, PowerPoint).
- **Budget** : Aucun coût réel (maquette simulée).

**5. Critères de succès**
- La maquette permet de **visualiser** le flux de retour.
- La solution réduit **le temps de recherche** (ex. : passage de 30 min à 5 min par retour).
- Le document justifie les **chois techniques** (ex. : simplicité, coût, compatibilité).

**6. Exclusions**
- Développement d’un logiciel complet.
- Mise en œuvre réelle dans le service.

---
*À affiner* : Préciser le type d’objets prêtés, le volume quotidien de retours, ou les outils déjà utilisés par le service. Ces détails aideront à prioriser les fonctionnalités de la maquette.
~~~~

**Variante C**

~~~~text
Pour démarrer, utilisez la fiche **M03 — Construire progressivement le cahier des charges** (brouillon). Elle propose une trame adaptable pour structurer votre document à partir des informations disponibles, sans inventer de détails.

**Application immédiate** :
1. **Objectif** : Faciliter la localisation des retours de prêt.
2. **Périmètre** : Service de prêt (à préciser : types d'objets, acteurs concernés).
3. **Besoins/sources** : "Retours difficiles à retrouver" (source : votre observation).
4. **Exigences** : À ce stade, aucune exigence vérifiable n'est confirmée. Notez : *"Exigences à définir avec le commanditaire"*.
5. **Inconnues** : Fréquence des retours, système actuel de suivi, attentes précises du service.
6. **Statut** : *"Brouillon — validation en attente"*.

**Prochaine étape** : Interrogez le service de prêt pour confirmer les besoins et contraintes (ex : "Quels objets sont concernés ?"). La maquette de fin de semestre sera un livrable, mais son contenu dépendra de ces clarifications.

*Exemple fictif de la fiche* : Si le client souhaite "retrouver les objets empruntés", la fréquence de mise à jour est marquée *"à discuter"* — ici, c'est similaire pour vos inconnues.
~~~~

### Tour 2

~~~~text
L’agent précise qu’il lui faut repérer en fin de journée quels objets n’ont pas été rendus. Le client n’a donné aucun délai de recherche. Écris une ligne de brouillon que l’on puisse lui montrer.
~~~~

Attendus proposés · Rédiger une exigence fonctionnelle provisoire fidèle à l’usage / Proposer un contrôle observable sans seuil inventé ni solution figée

Points de vigilance · Ajouter un délai, un outil ou des données nominatives sans source / Présenter la ligne comme approuvée

**Variante A**

~~~~text
**Exigence fonctionnelle** : *"Le système doit permettre à l’agent d’identifier, en fin de journée, la liste des objets non rendus, sans délai de recherche imposé."*
~~~~

**Variante B**

~~~~text
**Brouillon à valider avec l'agent :**
*"La maquette inclura un tableau de bord affichant, en fin de journée, la liste des objets non rendus (avec leur identifiant et heure de prêt), triable par priorité (ex. : objets rares en premier)."*
~~~~

**Variante C**

~~~~text
**Exigence (brouillon)** :
*« À la fin de chaque journée, le système doit permettre à l’agent d’identifier la liste des objets non rendus (source : agent du service de prêt ; vérification : démonstration sur la maquette ; statut : à valider). »*

*Pourquoi* : La fiche **M03** souligne l’importance de lier chaque exigence à une **source**, une **vérification** et un **statut**. Ici, la source est l’agent, la vérification sera testable via la maquette, et le statut reste ouvert car le client n’a pas encore confirmé.
~~~~
