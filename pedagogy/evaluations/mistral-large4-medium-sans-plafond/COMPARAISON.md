# Comparaison des réponses de développement

Huit tours comparables, quatre variantes : les identités restent visibles. Les réponses sont celles enregistrées par le connecteur. Les grilles sont vierges.


## TX05 · tour 1 · c2

**Message fictif**

~~~~text
Pour notre prototype de prêt de matériel, le commanditaire ajoute des alertes et un export. Il veut garder la date de remise. On a deux jeudis. Dis-nous quoi lui répondre.
~~~~

**Small historique**

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

**Medium 3.5 historique**

~~~~text
**Analyse** : Le commanditaire demande deux ajouts (alertes + export) sans modifier la date de remise. Avec deux jeudis disponibles, il faut clarifier si ces ajouts sont prioritaires ou si la date est négociable.

**Réponse à proposer** :
*"Nous pouvons intégrer les alertes et l’export, mais cela peut impacter le périmètre ou la date. Souhaitez-vous :
1) Garder la date et réduire d’autres fonctionnalités ?
2) Accepter un report pour inclure ces éléments ?
3) Prioriser l’un des deux ajouts ?"*

*(Fonction dominante : **analyser** – évaluer les compromis sans imposer de solution.)*
~~~~

**Large low 700**

~~~~text
Deux options s'offrent à vous, à choisir selon ce que le prototype doit démontrer :

**Option A — accepter le périmètre élargi, mais négocier la date.** Répondre que alertes + export ajoutent du travail ; garder le jeudi 1 signifie livrer un prototype allégé ailleurs, ou décaler au jeudi 2. Demandez-lui lequel il préfère.

**Option B — tenir la date, délimiter le périmètre.** « On livre jeudi 1 avec les fonctions de base ; alertes et export passent en V2. » Cela protège la démonstration et montre que vous gérez les demandes de changement.

Ce qui compte dans votre réponse : ne pas dire oui aux deux sans arbitrage. Nommez le compromis explicitement, même brièvement.
~~~~

**Large medium sans plafond**

~~~~text
Voici une piste de réponse qui pose le choix sans décider à sa place :

« Merci pour ces ajouts. Les alertes et l’export demandent du développement et des tests supplémentaires. Pour tenir la remise au jeudi prévu, on peut soit livrer le prototype sans ces deux fonctions d’abord, soit décaler la date. Quelle option préférez-vous, ou souhaitez-vous qu’on évalue le délai exact de ces ajouts avant de décider ? »

Cela nomme l’impact concret, rappelle la contrainte de date, et renvoie la décision au commanditaire sur la base d’éléments factuels.
~~~~


## TX05 · tour 2 · c2

**Message fictif**

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

**Small historique**

~~~~text
Corriger

Erreur exacte : la réponse du client ne valide pas l'export comme une exigence ferme, mais comme une option conditionnelle ("si le prêt marche"). Le binôme a interprété "oui" comme une validation totale, ce qui est une surinterprétation.

Correction :
Remplacer "tout est validé" par une formulation qui reflète la condition :
*"Le client valide l'export de démonstration sous réserve que le prototype de prêt fonctionne. Les alertes restent à préciser."*

Raison : un compte rendu doit refléter fidèlement les échanges pour éviter des attentes non alignées. La condition doit être explicitement mentionnée.
~~~~

**Medium 3.5 historique**

~~~~text
**Correction** :
Le binôme a écrit une validation totale ("tout est validé"), alors que le client a conditionné l'export à la réussite du prêt.

**Proposition de reformulation** :
*"Export de démonstration validé sous réserve que le prêt fonctionne."*

*(Fonction dominante : **corriger** – identifier l'erreur et proposer une version exacte.)*
~~~~

**Large low 700**

~~~~text
L'erreur : « tout est validé » transforme une acceptation **conditionnelle et partielle** en validation globale.

Correction proposée : « Le commanditaire accepte un export de démonstration, à condition que la fonction de prêt fonctionne. Le reste du périmètre (alertes, etc.) n'est pas validé. »

La raison : un compte rendu fidèle doit garder la condition (« si le prêt marche »), sinon l'équipe risque de croire que tout le périmètre est acté alors que seule une partie l'est, avec un critère de réussite à vérifier.
~~~~

**Large medium sans plafond**

~~~~text
L’erreur est « tout est validé » : la réponse du client n’est ni globale ni inconditionnelle. Il accepte un **export de démonstration**, et seulement **si le prêt fonctionne**.

Correction proposée pour le compte rendu : « Le client accepte un export de démonstration, sous condition que le prêt soit fonctionnel. Le reste du périmètre n’est pas encore validé. »

Pourquoi : un compte rendu doit refléter fidèlement la décision réelle, y compris ses conditions et ses limites, pour éviter qu’on croie plus tard que tout était figé.
~~~~


## TX05 · tour 1 · resource_forced

**Message fictif**

~~~~text
Pour notre prototype de prêt de matériel, le commanditaire ajoute des alertes et un export. Il veut garder la date de remise. On a deux jeudis. Dis-nous quoi lui répondre.
~~~~

**Small historique**

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

**Medium 3.5 historique**

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

**Large low 700**

~~~~text
La fiche **M06 « Examiner une demande de changement »** (brouillon) s’applique : avant d’accepter, rendez explicites l’intérêt, les options et les impacts à estimer — la décision revient au commanditaire et aux personnes légitimes.

Une réponse possible, à adapter par l’équipe :

> « Nous avons noté votre demande d’alertes et d’export. Pour décider sereinement, nous devons estimer le travail supplémentaire et ses effets sur les deux jeudis prévus. Quelles options privilégiez-vous : garder la date avec un périmètre réduit, ou décaler la remise pour intégrer les deux ajouts ? »

Cela pose la question sans promettre ni refuser d’emblée.
~~~~

**Large medium sans plafond**

~~~~text
La fiche **M06 « Examiner une demande de changement »** (brouillon) s’applique ici : avant d’accepter ou refuser, il faut rendre explicite l’intérêt de la demande et ses impacts sur le délai.

Voici un exemple de ce que vous pouvez lui répondre :

> « Nous avons bien noté votre demande d’ajout d’alertes et d’un export. Pour tenir la date de remise prévue, nous devons d’abord évaluer le travail supplémentaire que cela représente et voir quelles options s’offrent à nous : décaler une autre fonctionnalité, accepter un délai, ou trouver une solution intermédiaire. Pouvons-nous faire le point jeudi pour décider ensemble de la meilleure option ? »

Cela montre que vous prenez la demande au sérieux sans promettre automatiquement, et vous gardez la décision entre les mains des personnes légitimes.
~~~~


## TX05 · tour 2 · resource_forced

**Message fictif**

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

**Small historique**

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

**Medium 3.5 historique**

~~~~text
**Correction** :
Remplacez *"tout est validé"* par :
*"Demande notée : export de démonstration **sous condition** que la fonction de prêt soit opérationnelle. À valider après test de cette condition. Décision en attente."*

**Raison** :
- La réponse du client est **conditionnelle** (l'export dépend du bon fonctionnement du prêt).
- *"Tout est validé"* ignore cette condition et suppose un accord inconditionnel, ce qui est faux.
- La fiche **M06 – Examiner une demande de changement** (brouillon) rappelle qu’une demande doit être **explicite** sur ses critères d’acceptation. Ici, le test du prêt est un prérequis à confirmer.
~~~~

**Large low 700**

~~~~text
**Erreur** : « tout est validé » transforme une réponse conditionnelle en accord définitif.

**Correction** : « Le commanditaire accepte un export de démonstration, à condition que le prêt fonctionne. Les alertes restent en attente de décision. »

**Raison** : la fiche M06 distingue la demande, l'impact supposé et la décision. Ici, seule une partie est décidée, et sous condition — écrire « tout est validé » fait croire à un périmètre figé qui n'existe pas.
~~~~

**Large medium sans plafond**

~~~~text
L’erreur : « tout est validé » transforme une acceptation **partielle et conditionnelle** en une validation globale. Or le client n’a accepté qu’un **export de démonstration**, et seulement **si le prêt fonctionne** — les alertes et l’export complet ne sont pas retenus, et la condition reste à vérifier.

Correction proposée pour le compte rendu :

> « Le commanditaire accepte l’ajout d’un export de démonstration, à condition que le prêt fonctionne. Les alertes ne sont pas retenues pour l’instant. La date de remise reste à confirmer selon l’impact estimé. »

Pourquoi : un compte rendu doit refléter la décision réelle, avec sa condition et son auteur, sinon l’équipe risque de développer ce qui n’a pas été décidé — ou de croire le périmètre figé alors qu’il ne l’est pas. C’est exactement ce que la fiche **M06 « Examiner une demande de changement »** (brouillon) demande de tracer : la décision et qui la prend, pas un « validé » générique.
~~~~


## TX05 · tour 1 · library_contextual

**Message fictif**

~~~~text
Pour notre prototype de prêt de matériel, le commanditaire ajoute des alertes et un export. Il veut garder la date de remise. On a deux jeudis. Dis-nous quoi lui répondre.
~~~~

**Small historique**

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

**Medium 3.5 historique**

~~~~text
**Analyser** : Le commanditaire souhaite ajouter des fonctionnalités (alertes, export) tout en conservant la date de remise initiale. Avec deux jeudis disponibles, il faut clarifier si ces ajouts sont prioritaires ou négociables.

**Réponse à proposer** :
*"Pour intégrer les alertes et l’export sans repousser la date, il faudrait soit réduire le périmètre actuel (ex : simplifier une fonctionnalité existante), soit accepter un risque sur la qualité (tests limités). Sinon, la date doit être reportée. Quelle est votre priorité : livrer à temps avec un scope réduit, ou livrer complet avec un délai ajusté ?"*

*(Cela force le commanditaire à arbitrer entre scope, temps et qualité, sans imposer de solution.)*
~~~~

**Large low 700**

~~~~text
Analysons la situation : le commanditaire demande deux fonctionnalités supplémentaires (alertes, export) tout en maintenant la date — c'est un arbitrage classique périmètre/délai/qualité.

Trois pistes de réponse possibles, à choisir selon votre marge réelle :

1. **Accepter avec contrepartie** : « On intègre les alertes et l'export, mais la remise glisse au jeudi suivant » — seulement si vous avez cette marge.
2. **Refuser partiellement** : « On livre le jeudi prévu avec le périmètre initial ; alertes et export passent en V2 » — protège la date.
3. **Négocier le périmètre** : « Quel est l'indispensable entre alertes et export pour le jeudi ? L'autre suivra. »

Avant de répondre, vérifiez en interne : combien de jours de travail représentent ces deux ajouts, et quelle est la conséquence réelle d'un report ? C'est votre équipe qui décide quelle option proposer.
~~~~

**Large medium sans plafond**

~~~~text
Ajouter alertes et export, c’est augmenter le périmètre alors que le délai est bloqué. Avec deux jeudis, vous avez trois leviers : réduire ailleurs, décaler la date, ou livrer en deux temps (prototype fonctionnel d’abord, alertes/export ensuite).

Demandez-lui ce qui est indispensable pour le premier usage : si les alertes servent à l’adoption, intégrez-les et retirez autre chose ; si l’export sert à la démonstration, priorisez-le. Proposez-lui ce choix explicite plutôt qu’un « oui » qui mènerait à un livrable bâclé.
~~~~


## TX05 · tour 2 · library_contextual

**Message fictif**

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

**Small historique**

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

**Medium 3.5 historique**

~~~~text
**Corriger** :
L'erreur est de généraliser *"tout est validé"* alors que seul **l'export de démonstration** est accepté **sous condition** (*"si le prêt marche"*).

**Correction** :
*"Validé : export de démonstration (sous réserve du bon fonctionnement du prêt). À confirmer : alertes et périmètre global."*

**Raison** : Le compte rendu doit refléter la condition et ne pas valider implicitement les autres éléments (alertes, date).
~~~~

**Large low 700**

~~~~text
L'erreur : « tout est validé » transforme une acceptation conditionnelle en validation pleine et entière.

Correction proposée : « Le commanditaire accepte un export de démonstration, à condition que le prêt fonctionne. Le reste du périmètre (alertes, etc.) n'est pas validé. »

Pourquoi : un compte rendu doit refléter exactement ce qui a été décidé, y compris les conditions. « Tout est validé » risque de faire croire à l'équipe que les alertes sont actées, alors qu'elles ne le sont pas — et de créer un écart entre ce qui est attendu et ce qui est livré.
~~~~

**Large medium sans plafond**

~~~~text
L’erreur : « tout est validé » transforme une réponse partielle et conditionnelle en accord global. Le client n’a validé que l’export de démonstration, et seulement si le prêt fonctionne. Les alertes restent non retenues, et la date de remise reste inchangée.

Correction proposée pour le compte rendu : « Le commanditaire accepte un export de démonstration, conditionné au bon fonctionnement du prêt. Les alertes ne sont pas retenues pour cette remise. La date du jeudi reste maintenue. »

Cette formulation garde la trace de ce qui est réellement décidé, de la condition posée, et de ce qui reste en suspens — utile si le prêt ne marche pas ou si quelqu’un relit le CR plus tard.
~~~~


## TX07 · tour 1 · resource_forced

**Message fictif**

~~~~text
Rédige notre cahier des charges. Tout ce qu’on sait, c’est que le service de prêt a des retours difficiles à retrouver et qu’on rend une maquette en fin de semestre.
~~~~

**Small historique**

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

**Medium 3.5 historique**

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

**Large low 700**

~~~~text
On ne rédige pas un cahier des charges à partir de « tout ce qu’on sait » : on le construit progressivement à partir des faits recueillis, en gardant visibles les inconnues. La fiche **M03 — Construire progressivement le cahier des charges** (brouillon) propose une trame simple : objectif, périmètre, besoin avec sa source, exigence vérifiable, statut, validation.

Exemple fictif : si le besoin est « retrouver facilement un objet emprunté », on écrit l’exigence « la recherche renvoie le bon objet en moins de 3 secondes » avec le statut « à discuter », plutôt que d’inventer un délai ou une fonctionnalité.

Première application : prenez votre seul fait — « retours difficiles à retrouver » — et formulez-le comme un besoin sourcé, sans ajouter de seuil ni de solution.
~~~~

**Large medium sans plafond**

~~~~text
La fiche **M03 « Construire progressivement le cahier des charges »** (statut brouillon) est pertinente : elle propose de partir des faits recueillis, de formuler le besoin, puis de marquer les inconnues plutôt que d’inventer des détails.

Voici comment démarrer avec vos deux éléments :

**Objectif** : permettre au service de prêt de retrouver facilement les objets empruntés.
**Périmètre** : maquette à rendre en fin de semestre (date exacte à préciser).
**Besoin/source** : « retours difficiles à retrouver » (constat du service).
**Exigence** : … (à définir avec l’équipe, ex. : chaque retour est enregistré avec un identifiant).
**Vérification** : … (comment vérifier que l’objet est bien retrouvé ?).
**Statut** : brouillon — fréquence de mise à jour « à discuter », format de la maquette « à confirmer ».

Cette trame vous permet de lister ce qui est connu et ce qui reste à arbitrer, sans décider à la place des personnes concernées.
~~~~


## TX07 · tour 2 · resource_forced

**Message fictif**

~~~~text
L’agent précise qu’il lui faut repérer en fin de journée quels objets n’ont pas été rendus. Le client n’a donné aucun délai de recherche. Écris une ligne de brouillon que l’on puisse lui montrer.
~~~~

**Small historique**

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

**Medium 3.5 historique**

~~~~text
**Exigence (brouillon)** :
*« À la fin de chaque journée, le système doit permettre à l’agent d’identifier la liste des objets non rendus (source : agent du service de prêt ; vérification : démonstration sur la maquette ; statut : à valider). »*

*Pourquoi* : La fiche **M03** souligne l’importance de lier chaque exigence à une **source**, une **vérification** et un **statut**. Ici, la source est l’agent, la vérification sera testable via la maquette, et le statut reste ouvert car le client n’a pas encore confirmé.
~~~~

**Large low 700**

~~~~text
**Besoin (source : agent du service de prêt) :** repérer en fin de journée les objets non rendus ; **exigence :** la liste des objets non rendus est disponible en fin de journée ; **délai de recherche : à discuter** (aucun délai communiqué par le client) ; **statut : brouillon, à confirmer**.
~~~~

**Large medium sans plafond**

~~~~text
Selon la fiche **M03 « Construire progressivement le cahier des charges »** (brouillon), une exigence doit rester vérifiable et son statut visible, sans inventer de délai.

Voici une ligne de brouillon montrable :

> **Exigence** : en fin de journée, l’agent repère la liste des objets non rendus. **Source** : demande de l’agent. **Vérification** : affichage de la liste des emprunts en cours à la fermeture. **Statut** : délai de recherche non précisé par le client — *à discuter*.

Cette formulation garde l’inconnue explicite plutôt que de décider un délai arbitraire, ce qui permet au client de confirmer ou de préciser lors de la discussion.
~~~~
