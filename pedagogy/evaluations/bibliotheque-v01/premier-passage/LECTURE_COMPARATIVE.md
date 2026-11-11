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

**Variante B**

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

**Variante C**

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

### Tour 2

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

Attendus proposés · Reprendre exactement le caractère conditionnel et le périmètre export de démonstration / Signaler que les alertes et la portée de l’accord restent à clarifier

Points de vigilance · Assimiler le oui partiel à une validation complète / Prétendre enregistrer ou communiquer la décision

**Variante A**

~~~~text
Corriger

Erreur exacte : la réponse du client ne valide pas l'export comme une exigence ferme, mais comme une option conditionnelle ("si le prêt marche"). Le binôme a interprété "oui" comme une validation totale, ce qui est une surinterprétation.

Correction :
Remplacer "tout est validé" par une formulation qui reflète la condition :
*"Le client valide l'export de démonstration sous réserve que le prototype de prêt fonctionne. Les alertes restent à préciser."*

Raison : un compte rendu doit refléter fidèlement les échanges pour éviter des attentes non alignées. La condition doit être explicitement mentionnée.
~~~~

**Variante B**

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

**Variante C**

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

**Variante B**

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

**Variante C**

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

### Tour 2

~~~~text
L’agent précise qu’il lui faut repérer en fin de journée quels objets n’ont pas été rendus. Le client n’a donné aucun délai de recherche. Écris une ligne de brouillon que l’on puisse lui montrer.
~~~~

Attendus proposés · Rédiger une exigence fonctionnelle provisoire fidèle à l’usage / Proposer un contrôle observable sans seuil inventé ni solution figée

Points de vigilance · Ajouter un délai, un outil ou des données nominatives sans source / Présenter la ligne comme approuvée

**Variante A**

~~~~text
**Brouillon pour l'agent :**
*"À la fin de chaque journée, le système doit générer une liste des objets encore en prêt (non rendus), avec leur date de prêt et l’identifiant de l’emprunteur. Cette liste sera affichée dans l’interface dédiée ou exportable en PDF pour vérification manuelle."*
~~~~

**Variante B**

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

**Variante C**

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
