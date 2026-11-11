# Comparaison de développement : trois modèles

Deux scénarios fictifs ; verbatim exacts, grille humaine vierge à part. Les identités sont visibles.


## TX05 · tour 1 · c2

**Message fictif**

~~~~text
Pour notre prototype de prêt de matériel, le commanditaire ajoute des alertes et un export. Il veut garder la date de remise. On a deux jeudis. Dis-nous quoi lui répondre.
~~~~

**Small — réponse exacte**

~~~~text
Analyser

Le commanditaire ajoute deux nouvelles exigences : des alertes et un export, tout en conservant la date de remise. Ces ajouts modifient le périmètre initial du prototype.

Points à clarifier avant de répondre :
- Nature des alertes (quels événements, seuils, destinataires ?)
- Format et contenu de l'export (tableau, PDF, données brutes ?)
- Impact sur la date de remise : la conservation est-elle une contrainte ferme ou une préférence ?

Sans ces précisions, toute estimation de charge ou de planning reste incertaine. Proposer une réponse qui :
1. Reconnaît la valeur des ajouts,
2. Demande ces clarifications,
3. Indique que l'impact sur la date sera évalué une fois les détails connus.

Exemple de formulation :
*"Les alertes et l'export sont des fonctionnalités utiles pour le prototype. Pour évaluer leur impact sur la date de remise et les ressources nécessaires, pourriez-vous préciser :*
- *Quels types d'alertes sont attendus (retards, disponibilités, etc.) et à qui elles doivent être envoyées ?*
- *Quel format d'export est souhaité (excel, csv, autre) et quelles données doivent y figurer ?*
*Nous pourrons ensuite vous proposer un ajustement réaliste du planning."*
~~~~

**Medium 3.5 — réponse exacte**

~~~~text
**Analyse** : Le commanditaire demande deux ajouts (alertes + export) sans modifier la date de remise. Avec deux jeudis disponibles, il faut clarifier si ces ajouts sont prioritaires ou si la date est négociable.

**Réponse à proposer** :
*"Nous pouvons intégrer les alertes et l’export, mais cela peut impacter le périmètre ou la date. Souhaitez-vous :
1) Garder la date et réduire d’autres fonctionnalités ?
2) Accepter un report pour inclure ces éléments ?
3) Prioriser l’un des deux ajouts ?"*

*(Fonction dominante : **analyser** – évaluer les compromis sans imposer de solution.)*
~~~~

**Large 4 low — réponse exacte**

~~~~text
Deux options s'offrent à vous, à choisir selon ce que le prototype doit démontrer :

**Option A — accepter le périmètre élargi, mais négocier la date.** Répondre que alertes + export ajoutent du travail ; garder le jeudi 1 signifie livrer un prototype allégé ailleurs, ou décaler au jeudi 2. Demandez-lui lequel il préfère.

**Option B — tenir la date, délimiter le périmètre.** « On livre jeudi 1 avec les fonctions de base ; alertes et export passent en V2. » Cela protège la démonstration et montre que vous gérez les demandes de changement.

Ce qui compte dans votre réponse : ne pas dire oui aux deux sans arbitrage. Nommez le compromis explicitement, même brièvement.
~~~~


## TX05 · tour 2 · c2

**Message fictif**

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

**Small — réponse exacte**

~~~~text
Corriger

Erreur exacte : la réponse du client ne valide pas l'export comme une exigence ferme, mais comme une option conditionnelle ("si le prêt marche"). Le binôme a interprété "oui" comme une validation totale, ce qui est une surinterprétation.

Correction :
Remplacer "tout est validé" par une formulation qui reflète la condition :
*"Le client valide l'export de démonstration sous réserve que le prototype de prêt fonctionne. Les alertes restent à préciser."*

Raison : un compte rendu doit refléter fidèlement les échanges pour éviter des attentes non alignées. La condition doit être explicitement mentionnée.
~~~~

**Medium 3.5 — réponse exacte**

~~~~text
**Correction** :
Le binôme a écrit une validation totale ("tout est validé"), alors que le client a conditionné l'export à la réussite du prêt.

**Proposition de reformulation** :
*"Export de démonstration validé sous réserve que le prêt fonctionne."*

*(Fonction dominante : **corriger** – identifier l'erreur et proposer une version exacte.)*
~~~~

**Large 4 low — réponse exacte**

~~~~text
L'erreur : « tout est validé » transforme une acceptation **conditionnelle et partielle** en validation globale.

Correction proposée : « Le commanditaire accepte un export de démonstration, à condition que la fonction de prêt fonctionne. Le reste du périmètre (alertes, etc.) n'est pas validé. »

La raison : un compte rendu fidèle doit garder la condition (« si le prêt marche »), sinon l'équipe risque de croire que tout le périmètre est acté alors que seule une partie l'est, avec un critère de réussite à vérifier.
~~~~


## TX05 · tour 1 · resource_forced

**Message fictif**

~~~~text
Pour notre prototype de prêt de matériel, le commanditaire ajoute des alertes et un export. Il veut garder la date de remise. On a deux jeudis. Dis-nous quoi lui répondre.
~~~~

**Small — réponse exacte**

~~~~text
Analysons la situation avec la fiche **M06** *"Examiner une demande de changement"* :

1. **Demande** : Ajouter des alertes, un export et conserver la date de remise.
2. **Intérêt** : Améliorer la traçabilité et l’ergonomie pour les utilisateurs.
3. **Options** :
   - Intégrer les alertes et l’export dans le périmètre actuel (coût : temps de développement).
   - Reporter ces fonctionnalités à une version ultérieure (risque : insatisfaction du commanditaire).
4. **Impacts à estimer** :
   - Charge de travail pour l’équipe (ex. : 2–3 jours pour les alertes, 1 jour pour l’export).
   - Compatibilité avec les technologies existantes.
   - Priorisation : ces ajouts sont-ils critiques pour le prototype ?

**Prochaine étape** : Demander au commanditaire de prioriser ces ajouts par rapport aux autres tâches, et clarifier s’il accepte un délai ou un report. Utilisez le modèle de M06 pour structurer votre réponse :

> *"Demande : [décrivez]. Intérêt : [pourquoi]. Options : [liste]. Impacts à estimer : [charge, risques]. Décision et auteur : [à valider avec vous]."*

**Pourquoi cette approche ?**
La fiche M06 évite de répondre à la demande sans analyse, en distinguant *demande*, *impact* et *décision*. Cela responsabilise le commanditaire et protège l’équipe d’engagements non maîtrisés.
~~~~

**Medium 3.5 — réponse exacte**

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

**Large 4 low — réponse exacte**

~~~~text
La fiche **M06 « Examiner une demande de changement »** (brouillon) s’applique : avant d’accepter, rendez explicites l’intérêt, les options et les impacts à estimer — la décision revient au commanditaire et aux personnes légitimes.

Une réponse possible, à adapter par l’équipe :

> « Nous avons noté votre demande d’alertes et d’export. Pour décider sereinement, nous devons estimer le travail supplémentaire et ses effets sur les deux jeudis prévus. Quelles options privilégiez-vous : garder la date avec un périmètre réduit, ou décaler la remise pour intégrer les deux ajouts ? »

Cela pose la question sans promettre ni refuser d’emblée.
~~~~


## TX05 · tour 2 · resource_forced

**Message fictif**

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

**Small — réponse exacte**

~~~~text
**Correction** :

1. **Erreur** : Le compte rendu valide un export *sans préciser* :
   - La condition *"si le prêt marche"* (ambiguïté sur ce qui est validé).
   - La responsabilité de la démonstration (qui la réalise ? quand ?).

2. **Correction** :
   *"Export de démonstration validé **sous réserve** que le prêt fonctionne. Responsable : [nom], date limite : [JJ/MM]. Condition : validation du prêt par [nom]."*

3. **Raison** :
   Une validation floue expose à des malentendus. La fiche **M06** insiste sur la traçabilité des décisions et des conditions. Ici, la condition *"si le prêt marche"* doit être explicitée comme un critère de validation, pas une simple hypothèse.
~~~~

**Medium 3.5 — réponse exacte**

~~~~text
**Correction** :
Remplacez *"tout est validé"* par :
*"Demande notée : export de démonstration **sous condition** que la fonction de prêt soit opérationnelle. À valider après test de cette condition. Décision en attente."*

**Raison** :
- La réponse du client est **conditionnelle** (l'export dépend du bon fonctionnement du prêt).
- *"Tout est validé"* ignore cette condition et suppose un accord inconditionnel, ce qui est faux.
- La fiche **M06 – Examiner une demande de changement** (brouillon) rappelle qu’une demande doit être **explicite** sur ses critères d’acceptation. Ici, le test du prêt est un prérequis à confirmer.
~~~~

**Large 4 low — réponse exacte**

~~~~text
**Erreur** : « tout est validé » transforme une réponse conditionnelle en accord définitif.

**Correction** : « Le commanditaire accepte un export de démonstration, à condition que le prêt fonctionne. Les alertes restent en attente de décision. »

**Raison** : la fiche M06 distingue la demande, l'impact supposé et la décision. Ici, seule une partie est décidée, et sous condition — écrire « tout est validé » fait croire à un périmètre figé qui n'existe pas.
~~~~


## TX05 · tour 1 · library_contextual

**Message fictif**

~~~~text
Pour notre prototype de prêt de matériel, le commanditaire ajoute des alertes et un export. Il veut garder la date de remise. On a deux jeudis. Dis-nous quoi lui répondre.
~~~~

**Small — réponse exacte**

~~~~text
Analyser

Vous avez deux contraintes qui s’ajoutent au périmètre initial :
1. Ajouter des alertes (probablement pour les retards ou échéances).
2. Permettre un export des données (format non précisé).

La date de remise est déjà présente dans le périmètre initial, donc elle n’est pas nouvelle.

Pour répondre au commanditaire, clarifiez d’abord :
- **Nature des alertes** : retard de restitution, échéance proche, autre ?
- **Format de l’export** : CSV, PDF, Excel, API ?
- **Priorité** : les alertes et l’export sont-ils aussi urgents que le prototype initial ?

Proposez une réponse qui :
- Reconnaît l’ajout de périmètre.
- Demande des précisions pour affiner l’estimation.
- Propose un ordre de priorité ou un découpage en lots (ex : d’abord les alertes, puis l’export).

Exemple de formulation :
*« Nous prenons note de l’ajout des alertes et de l’export. Pour affiner notre estimation, pourriez-vous préciser :
- Le type d’alertes souhaité (retard, échéance, etc.) ?
- Le format de l’export (fichier, API, etc.) ?
Nous pouvons prioriser ces éléments après validation du prototype initial ou les intégrer en parallèle si le planning le permet. »*
~~~~

**Medium 3.5 — réponse exacte**

~~~~text
**Analyser** : Le commanditaire souhaite ajouter des fonctionnalités (alertes, export) tout en conservant la date de remise initiale. Avec deux jeudis disponibles, il faut clarifier si ces ajouts sont prioritaires ou négociables.

**Réponse à proposer** :
*"Pour intégrer les alertes et l’export sans repousser la date, il faudrait soit réduire le périmètre actuel (ex : simplifier une fonctionnalité existante), soit accepter un risque sur la qualité (tests limités). Sinon, la date doit être reportée. Quelle est votre priorité : livrer à temps avec un scope réduit, ou livrer complet avec un délai ajusté ?"*

*(Cela force le commanditaire à arbitrer entre scope, temps et qualité, sans imposer de solution.)*
~~~~

**Large 4 low — réponse exacte**

~~~~text
Analysons la situation : le commanditaire demande deux fonctionnalités supplémentaires (alertes, export) tout en maintenant la date — c'est un arbitrage classique périmètre/délai/qualité.

Trois pistes de réponse possibles, à choisir selon votre marge réelle :

1. **Accepter avec contrepartie** : « On intègre les alertes et l'export, mais la remise glisse au jeudi suivant » — seulement si vous avez cette marge.
2. **Refuser partiellement** : « On livre le jeudi prévu avec le périmètre initial ; alertes et export passent en V2 » — protège la date.
3. **Négocier le périmètre** : « Quel est l'indispensable entre alertes et export pour le jeudi ? L'autre suivra. »

Avant de répondre, vérifiez en interne : combien de jours de travail représentent ces deux ajouts, et quelle est la conséquence réelle d'un report ? C'est votre équipe qui décide quelle option proposer.
~~~~


## TX05 · tour 2 · library_contextual

**Message fictif**

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

**Small — réponse exacte**

~~~~text
Corriger

Erreur : **« tout est validé »** est une conclusion hâtive.
- Le client n’a validé **que l’export de démonstration**, pas l’ensemble du périmètre (alertes, date de remise, etc.).
- Le binôme a interprété une réponse partielle comme une validation globale.

Correction :
*« Le client valide l’ajout d’un export de démonstration **si le prêt fonctionne**. Les alertes et autres ajustements restent à préciser et valider. »*

Raison :
Un compte rendu doit refléter **exactement** ce qui a été validé, sans extrapolation. Cela évite les malentendus futurs et permet de prioriser les prochaines étapes (ex : tester le prêt avant de finaliser l’export).
~~~~

**Medium 3.5 — réponse exacte**

~~~~text
**Corriger** :
L'erreur est de généraliser *"tout est validé"* alors que seul **l'export de démonstration** est accepté **sous condition** (*"si le prêt marche"*).

**Correction** :
*"Validé : export de démonstration (sous réserve du bon fonctionnement du prêt). À confirmer : alertes et périmètre global."*

**Raison** : Le compte rendu doit refléter la condition et ne pas valider implicitement les autres éléments (alertes, date).
~~~~

**Large 4 low — réponse exacte**

~~~~text
L'erreur : « tout est validé » transforme une acceptation conditionnelle en validation pleine et entière.

Correction proposée : « Le commanditaire accepte un export de démonstration, à condition que le prêt fonctionne. Le reste du périmètre (alertes, etc.) n'est pas validé. »

Pourquoi : un compte rendu doit refléter exactement ce qui a été décidé, y compris les conditions. « Tout est validé » risque de faire croire à l'équipe que les alertes sont actées, alors qu'elles ne le sont pas — et de créer un écart entre ce qui est attendu et ce qui est livré.
~~~~


## TX07 · tour 1 · c2

**Message fictif**

~~~~text
Rédige notre cahier des charges. Tout ce qu’on sait, c’est que le service de prêt a des retours difficiles à retrouver et qu’on rend une maquette en fin de semestre.
~~~~

**Small — réponse exacte**

~~~~text
Voici une structure de cahier des charges adaptée à votre situation. Je vais vous proposer un cadre simple, avec des exemples concrets pour chaque section, afin que vous puissiez le compléter ensemble. L'objectif est de clarifier le périmètre, les contraintes et les attentes pour votre maquette.

---

### **Cahier des Charges – Service de Prêt**
*(Version brouillon – à affiner avec votre équipe)*

#### **1. Contexte et Objectifs**
- **Problème identifié** :
  *"Les retours de prêts (livres, équipements, etc.) sont difficiles à tracer, ce qui génère des pertes, des retards et une insatisfaction des utilisateurs."*
  → *Exemple* : Un étudiant rend un livre en retard mais le système ne le détecte pas, ou un livre est "perdu" sans historique clair.

- **Objectif principal** :
  *"Créer une maquette fonctionnelle d’un système de suivi des prêts qui permet de :*
  - *Enregistrer les prêts et retours en temps réel.*
  - *Identifier les retards et alerter les utilisateurs.*
  - *Générer des rapports simples pour le service (ex : liste des prêts en retard)."*

- **Livrable attendu** :
  Une maquette (papier, numérique ou logicielle) démontrant ces fonctionnalités, **sans obligation de développement complet** (ex : interface schématique, base de données simplifiée, ou outil comme Excel/Notion).

---

#### **2. Périmètre et Limites**
- **Fonctionnalités incluses** (à prioriser) :
  1. **Enregistrement des prêts** :
     - *Exemple* : Un utilisateur scanne un code-barres (ou saisit un identifiant) pour emprunter un livre.
     - *Données à capturer* : Date de prêt, utilisateur, ressource, durée autorisée.
  2. **Suivi des retours** :
     - *Exemple* : Un retour est enregistré avec date/heure, et le système vérifie si le délai est respecté.
  3. **Alertes pour retards** :
     - *Exemple* : Un email ou une notification (dans la maquette) est envoyé 2 jours avant la date limite.
  4. **Rapports basiques** :
     - *Exemple* : Tableau listant les 10 prêts les plus en retard.

- **Fonctionnalités exclues** (pour simplifier) :
  - Gestion des amendes financières.
  - Intégration avec un système bancaire ou un annuaire étudiant réel.
  - Historique illimité (limiter à 1 an pour la maquette).

- **Public cible** :
  - *Utilisateurs* : Étudiants et personnel du service de prêt.
  - *Bénéficiaires indirects* : Bibliothécaires (pour le suivi).

---
#### **3. Contraintes et Critères d'Acceptation**
- **Contraintes techniques** :
  - *Exemple* : La maquette doit fonctionner hors ligne (ou avec une base de données locale comme SQLite).
  - *Exemple* : Pas de dépendance à un logiciel payant (
~~~~

**Medium 3.5 — réponse exacte**

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

**Large 4 low — réponse exacte**

~~~~text
Ce que tu décris donne trois éléments : un service de prêt, un problème de recherche des retours, et une contrainte de maquette en fin de semestre. Pour rédiger un cahier des charges utile, il manque encore l'essentiel : **qui sont les utilisateurs concernés et que doit permettre concrètement la solution** (retrouver un retour en quelques clics ? notifier un retard ? autre ?) — sans ça, le document restera une liste de vœux.

Une seule question pour avancer : quels utilisateurs du service de prêt sont les plus pénalisés aujourd'hui par ces retours difficiles à retrouver ?
~~~~


## TX07 · tour 2 · c2

**Message fictif**

~~~~text
L’agent précise qu’il lui faut repérer en fin de journée quels objets n’ont pas été rendus. Le client n’a donné aucun délai de recherche. Écris une ligne de brouillon que l’on puisse lui montrer.
~~~~

**Small — réponse exacte**

~~~~text
**Brouillon pour l'agent :**
*"À la fin de chaque journée, le système doit générer une liste des objets encore en prêt (non rendus), avec leur date de prêt et l’identifiant de l’emprunteur. Cette liste sera affichée dans l’interface dédiée ou exportable en PDF pour vérification manuelle."*
~~~~

**Medium 3.5 — réponse exacte**

~~~~text
**Brouillon à valider avec l'agent :**
*"La maquette inclura un tableau de bord affichant, en fin de journée, la liste des objets non rendus (avec leur identifiant et heure de prêt), triable par priorité (ex. : objets rares en premier)."*
~~~~

**Large 4 low — réponse exacte**

~~~~text
**Brouillon — besoin exprimé :** « En fin de journée, l'agent doit pouvoir identifier rapidement quels objets prêtés n'ont pas été rendus. »
~~~~


## TX07 · tour 1 · resource_forced

**Message fictif**

~~~~text
Rédige notre cahier des charges. Tout ce qu’on sait, c’est que le service de prêt a des retours difficiles à retrouver et qu’on rend une maquette en fin de semestre.
~~~~

**Small — réponse exacte**

~~~~text
Voici une trame adaptée à votre situation, avec des exemples fictifs pour illustrer chaque section. L'objectif est de rendre visibles les informations connues et les inconnues à clarifier ensemble.

---

**Cahier des charges – Service de prêt**
*Version 0.1 – À discuter et compléter*

**1. Objectif**
Permettre aux usagers de retrouver facilement les objets empruntés et aux bibliothécaires de gérer les retards ou pertes.

**2. Périmètre**
- **Inclus** :
  - Fonctionnalité de recherche des objets empruntés (par titre, utilisateur, date).
  - Affichage des retards ou objets non rendus.
- **Exclus** :
  - Gestion des stocks physiques (hors scope de la maquette).
  - Paiement des amendes (hors scope).

**3. Besoins et sources**
- **Besoin exprimé** : "Les retours sont difficiles à retrouver" (source : retour d’expérience des bibliothécaires).
- **Inconnues** :
  - Fréquence de mise à jour des données (ex. : en temps réel ? quotidienne ?).
  - Nombre d’objets gérés (ex. : 100 ? 1000 ?).

**4. Exigences vérifiables**
| Exigence | Vérification | Statut |
|----------|-------------|--------|
| L’usager peut rechercher un objet par son titre. | Test : saisie d’un titre valide → affichage des emprunts correspondants. | À confirmer |
| Le système affiche les objets non rendus depuis plus de 7 jours. | Test : simulation d’un retard de 8 jours → objet marqué "en retard". | À discuter |

**5. Contraintes**
- **Technique** : Maquette en fin de semestre (délai : 6 semaines).
- **Humaine** : Validation par les bibliothécaires avant la maquette.

**6. Points à clarifier**
- Qui valide les exigences ? (ex. : bibliothécaires + enseignant).
- Quels objets sont concernés ? (ex. : livres uniquement ?).

---

**Pourquoi cette structure ?**
- Chaque exigence est liée à un besoin et une vérification (fiche M03).
- Les inconnues sont marquées ("à confirmer/discuter") pour éviter les décisions prématurées.

**Prochaine étape** :
- Confirmez ou ajustez les éléments ci-dessus avec les bibliothécaires.
- Priorisez les exigences pour la maquette (ex. : commencer par la recherche par titre).

*Exemple fictif de validation* :
*"Les bibliothécaires confirment que la recherche par titre suffit pour la maquette, mais insistent sur l’affichage des retards."* → Mise à jour du statut des exigences.
~~~~

**Medium 3.5 — réponse exacte**

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

**Large 4 low — réponse exacte**

~~~~text
On ne rédige pas un cahier des charges à partir de « tout ce qu’on sait » : on le construit progressivement à partir des faits recueillis, en gardant visibles les inconnues. La fiche **M03 — Construire progressivement le cahier des charges** (brouillon) propose une trame simple : objectif, périmètre, besoin avec sa source, exigence vérifiable, statut, validation.

Exemple fictif : si le besoin est « retrouver facilement un objet emprunté », on écrit l’exigence « la recherche renvoie le bon objet en moins de 3 secondes » avec le statut « à discuter », plutôt que d’inventer un délai ou une fonctionnalité.

Première application : prenez votre seul fait — « retours difficiles à retrouver » — et formulez-le comme un besoin sourcé, sans ajouter de seuil ni de solution.
~~~~


## TX07 · tour 2 · resource_forced

**Message fictif**

~~~~text
L’agent précise qu’il lui faut repérer en fin de journée quels objets n’ont pas été rendus. Le client n’a donné aucun délai de recherche. Écris une ligne de brouillon que l’on puisse lui montrer.
~~~~

**Small — réponse exacte**

~~~~text
**Ligne de brouillon à montrer au client :**

*"Exigence : Le système doit permettre à l’agent de visualiser, en fin de journée, la liste des objets non rendus, avec leur date d’emprunt et le nom de l’emprunteur. Statut : À valider par l’agent. Vérification : Affichage correct après simulation d’une journée d’emprunts (ex. : 5 objets non rendus sur 50)."*

---
**Pourquoi cette formulation ?**
- **Précision** : L’exigence cible un besoin concret (fin de journée) et un livrable (liste avec détails).
- **Flexibilité** : Pas de délai imposé (client n’a rien précisé).
- **Vérifiable** : La simulation est un test simple à réaliser sur la maquette.

*À discuter* : L’agent confirme-t-il que ces informations (date d’emprunt, nom) sont suffisantes ? Sinon, ajouter d’autres champs.
~~~~

**Medium 3.5 — réponse exacte**

~~~~text
**Exigence (brouillon)** :
*« À la fin de chaque journée, le système doit permettre à l’agent d’identifier la liste des objets non rendus (source : agent du service de prêt ; vérification : démonstration sur la maquette ; statut : à valider). »*

*Pourquoi* : La fiche **M03** souligne l’importance de lier chaque exigence à une **source**, une **vérification** et un **statut**. Ici, la source est l’agent, la vérification sera testable via la maquette, et le statut reste ouvert car le client n’a pas encore confirmé.
~~~~

**Large 4 low — réponse exacte**

~~~~text
**Besoin (source : agent du service de prêt) :** repérer en fin de journée les objets non rendus ; **exigence :** la liste des objets non rendus est disponible en fin de journée ; **délai de recherche : à discuter** (aucun délai communiqué par le client) ; **statut : brouillon, à confirmer**.
~~~~


## TX07 · tour 1 · library_contextual

**Message fictif**

~~~~text
Rédige notre cahier des charges. Tout ce qu’on sait, c’est que le service de prêt a des retours difficiles à retrouver et qu’on rend une maquette en fin de semestre.
~~~~

**Small — réponse exacte**

~~~~text
Voici une trame adaptée à ce que vous savez, avec des éléments à compléter ou à discuter. Je vous propose de la remplir ensemble en distinguant ce qui est **confirmé**, **à préciser** ou **à arbitrer**.

---

**Cahier des charges – Service de suivi des prêts**
*(Version 0 – À valider)*

**1. Objectif**
Permettre aux usagers et au personnel de retrouver facilement les objets empruntés et leur état.

**2. Périmètre**
- Fonctionnalités attendues : recherche des prêts en cours, historique des retours, signalement des objets non rendus.
- Exclusions : gestion des stocks, paiements de pénalités, interface publique (si hors scope).

**3. Besoin source**
- Constat : retours difficiles à retrouver (fait rapporté).
- À confirmer : fréquence des retours, types d’objets concernés, acteurs impliqués (bibliothécaires ? usagers ?).

**4. Exigences (à vérifier)**
- **Recherche** : système doit permettre une recherche par identifiant objet, nom d’emprunteur ou date.
  *Statut* : À discuter (exemple : "Recherche par identifiant objet validée par [nom] le [date]").
- **Historique** : conservation des données de prêt pendant au moins 1 an après retour.
  *Statut* : Inconnu (à sourcer : règlement interne ?).
- **Signalement** : alerte automatique pour les objets non rendus après X jours.
  *Statut* : Seuil X non défini.

**5. Contraintes**
- Délai : maquette livrée en fin de semestre (date exacte à préciser).
- Ressources : équipe de 7 étudiants, compétences techniques limitées (à détailler si besoin).
- Budget : aucun (à confirmer).

**6. Inconnues à lever**
- Quels objets sont concernés ? (livres, matériel, etc.)
- Qui valide les données de prêt ? (bibliothécaires uniquement ?)
- Quel est le processus actuel de signalement des retards ?

**7. Validation**
- Points à faire confirmer : périmètre, exigences, contraintes.
- Responsable validation : [nom du commanditaire ou enseignant].

---

**Prochaine étape** :
1. **Relisez** cette trame et identifiez :
   - Les éléments **confirmés** (ex : objectif, délai).
   - Les éléments **à discuter** (ex : seuils, acteurs).
2. **Ajoutez** une colonne "Source" pour chaque exigence (ex : "Règlement bibliothèque, 2023").

*Pourquoi cette structure ?*
Elle sépare les faits des hypothèses et met en évidence ce qui manque pour éviter les décisions prématurées. La fiche **M03** (Construire progressivement le cahier des charges) suggère de marquer les inconnues plutôt que de les deviner — ici, les seuils ou les acteurs.

**Exemple de formulation à éviter** :
*"Le système enverra une alerte après 7 jours de retard"* → **Problème** : 7 jours est une hypothèse non sourcée. À la place :
*"Le système en
~~~~

**Medium 3.5 — réponse exacte**

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

**Large 4 low — réponse exacte**

~~~~text
Un cahier des charges est un document évolutif qui part des faits connus et rend visibles les inconnues, plutôt qu’une liste figée de fonctionnalités.

Pour votre cas, commencez par écrire ce que vous savez : « Le service de prêt constate que les retours d’objets sont difficiles à retrouver. » Puis ajoutez une exigence vérifiable liée à ce constat, par exemple : « Un objet emprunté doit être localisable en moins de X étapes » — mais comme le seuil X n’est pas connu, inscrivez « à discuter avec le service » plutôt que d’inventer une valeur. Enfin, notez la contrainte temporelle : « Maquette livrée en fin de semestre ».

Référence : fiche **M03 — Construire progressivement le cahier des charges** (brouillon), qui insiste sur le statut visible des exigences et l’absence de seuils inventés.
~~~~


## TX07 · tour 2 · library_contextual

**Message fictif**

~~~~text
L’agent précise qu’il lui faut repérer en fin de journée quels objets n’ont pas été rendus. Le client n’a donné aucun délai de recherche. Écris une ligne de brouillon que l’on puisse lui montrer.
~~~~

**Small — réponse exacte**

~~~~text
**Brouillon – Exigence utilisateur**
*"L’agent doit pouvoir identifier, en fin de journée, la liste des objets non rendus parmi ceux empruntés ce jour-là."*

**Pourquoi cette ligne ?**
- Elle cible l’**action concrète** (repérage en fin de journée) sans imposer une solution technique.
- Elle évite les hypothèses sur les délais (le client n’en a pas donné).
- Elle reste **vérifiable** : un test simple consisterait à vérifier si la liste est disponible à l’heure demandée.

*À affiner* :
- Préciser si "fin de journée" correspond à une heure fixe (ex : 18h).
- Confirmer si la liste doit inclure uniquement les objets du jour ou aussi les retards antérieurs.
~~~~

**Medium 3.5 — réponse exacte**

~~~~text
**Exigence fonctionnelle** : *"Le système doit permettre à l’agent d’identifier, en fin de journée, la liste des objets non rendus, sans délai de recherche imposé."*
~~~~

**Large 4 low — réponse exacte**

~~~~text
Voici une ligne de brouillon à lui montrer :

**« En fin de journée, l’outil affiche la liste des objets non rendus ; le délai de recherche reste à préciser avec le service. »**

Elle traduit le besoin en exigence observable (la liste en fin de journée) tout en gardant visible l’inconnue (le délai), conformément à la fiche **M03 — Construire progressivement le cahier des charges** (brouillon).
~~~~
