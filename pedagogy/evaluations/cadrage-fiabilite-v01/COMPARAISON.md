# Comparaison de développement : cadrage existant et fiabilité

Les identités sont affichées ; pour une lecture partiellement aveugle, voir `premier-passage/LECTURE_COMPARATIVE.md`. Réponses telles qu’enregistrées, aucune notation automatique.

## TX05 · tour 1

**Message étudiant fictif**

~~~~text
Pour notre prototype de prêt de matériel, le commanditaire ajoute des alertes et un export. Il veut garder la date de remise. On a deux jeudis. Dis-nous quoi lui répondre.
~~~~

**Cadrage bibliothèque existant**

~~~~text
Quand on ajoute du périmètre en cours de route avec un délai fixe, il faut choisir ce qu’on ajuste : la date, la qualité, ou une autre fonctionnalité. Dire « oui » aux alertes et à l’export tout en gardant le jeudi, c’est promettre quelque chose qui risque de déraper.

Tu peux lui répondre ceci : *« On peut intégrer les alertes et l’export, mais avec la remise prévue jeudi dans deux semaines, il faudra soit alléger une autre partie du prototype, soit les livrer en version suivante. Qu’est-ce qui compte le plus pour vous à cette date ? »*

Ça ouvre la décision sans t’engager seul sur un délai intenable.
~~~~

**Cadrage de fiabilité expérimental**

~~~~text
Ce que rapporte l’échange : le commanditaire demande d’ajouter deux éléments (alertes et export) tout en maintenant la date de remise, avec deux jeudis restants. Avec un délai fixe, augmenter le périmètre signifie qu’un autre élément devra céder : une autre fonctionnalité reportée, une livraison en deux temps, ou un risque accepté sur la qualité.

Tu peux lui répondre ainsi : « Vous souhaitez intégrer les alertes et l’export en conservant la date de remise prévue. Avec deux jeudis disponibles, quelles priorités retenez-vous pour ces ajouts, et que décale-t-on ou livre-t-on dans une version suivante ? » Cela formule sa demande sans déduire d’accord sur la méthode, et ouvre l’arbitrage à lui.
~~~~

## TX05 · tour 2

**Message étudiant fictif**

~~~~text
Le client répond « oui pour un export de démonstration si le prêt marche ». Notre binôme écrit « tout est validé ». Aide-nous à corriger le compte rendu.
~~~~

**Cadrage bibliothèque existant**

~~~~text
**L’erreur :** « tout est validé » transforme une acceptation partielle et conditionnelle en validation globale. Le client a accepté un export de démonstration, et seulement si le prêt fonctionne — ce n’est ni « tout », ni inconditionnel.

**Correction proposée pour le compte rendu :** *« Le commanditaire accepte un export de démonstration, à condition que le prêt de matériel fonctionne. Les alertes restent hors périmètre pour la remise du jeudi. »*

**Pourquoi :** un compte rendu fidèle note ce qui est accepté, sa condition et ce qui reste exclu. « Tout est validé » ferait croire à une validation sans réserve et masquerait la condition de fonctionnement — ce qui posera problème si le prêt échoue.
~~~~

**Cadrage de fiabilité expérimental**

~~~~text
L’erreur est de transformer un accord partiel et conditionnel en validation globale. Le client a dit oui à **un export de démonstration**, et seulement **si le prêt marche** : ce n’est ni un accord sur les alertes, ni une validation de tout le périmètre, ni une levée de la contrainte de date.

Formulation fidèle possible : « Le client accepte un export de démonstration, sous réserve que le prêt fonctionne. Les alertes et le maintien de la date de remise restent à arbitrer. »
~~~~

## TX07 · tour 1

**Message étudiant fictif**

~~~~text
Rédige notre cahier des charges. Tout ce qu’on sait, c’est que le service de prêt a des retours difficiles à retrouver et qu’on rend une maquette en fin de semestre.
~~~~

**Cadrage bibliothèque existant**

~~~~text
La fiche **M03 « Construire progressivement le cahier des charges »** (statut : brouillon) propose de partir des faits recueillis pour formuler un besoin vérifiable, en marquant explicitement ce qui reste inconnu plutôt que d’inventer des seuils.

Avec vos deux éléments : « retours difficiles à retrouver » se traduit en besoin de traçabilité (ex. : chaque retour enregistré avec date et emprunteur), et « maquette en fin de semestre » devient une contrainte de délai. Pour l’instant, inscrivez « à discuter » pour la fréquence de mise à jour ou le format exact des enregistrements.

Première application : rédigez trois lignes — **Objectif** (retrouver facilement les retours du service de prêt), **Périmètre** (service de prêt uniquement), **Contrainte** (livraison d’une maquette en fin de semestre) — puis ajoutez une exigence vérifiable du type « chaque retour est horodaté à la restitution » avec le statut « proposé, à confirmer ».
~~~~

**Cadrage de fiabilité expérimental**

~~~~text
Voici une trame inspirée de la fiche **M03 « Construire progressivement le cahier des charges »** (statut : brouillon), à compléter avec vos faits réels :

**Objectif** : Permettre au service de prêt de retrouver facilement les objets empruntés.
**Périmètre** : À préciser (quels types d’objets ? quels utilisateurs concernés ?).
**Besoin / source** : « Le service de prêt rencontre des difficultés pour retrouver les retours » (votre constat).
**Exigences** : À formuler avec le service (ex. : « retrouver un retour en moins de X étapes » — seuil à discuter, non fixé ici).
**Vérification** : Comment le service confirmera-t-il que c’est résolu ? (test utilisateur, démonstration…).
**Statut** : Brouillon — maquette prévue en fin de semestre (contrainte de calendrier connue, date exacte à confirmer).
**Validation par** : Personnes du service de prêt et commanditaire à identifier.

Les seuils, la technologie et les critères de « facilité » restent à discuter avec les personnes concernées ; ne les remplissez pas seuls.
~~~~

## TX07 · tour 2

**Message étudiant fictif**

~~~~text
L’agent précise qu’il lui faut repérer en fin de journée quels objets n’ont pas été rendus. Le client n’a donné aucun délai de recherche. Écris une ligne de brouillon que l’on puisse lui montrer.
~~~~

**Cadrage bibliothèque existant**

~~~~text
Voici une ligne conforme à la fiche **M03 « Construire progressivement le cahier des charges »** (brouillon), qui vise des besoins vérifiables :

**« En fin de journée, l’agent peut afficher la liste des objets empruntés et non restitués. »**

Elle précise le moment (fin de journée), l’action (afficher) et l’objet (objets non rendus), ce qui la rend testable sans inventer de délai de recherche.
~~~~

**Cadrage de fiabilité expérimental**

~~~~text
**Brouillon à montrer :**

> « En fin de journée, le service de prêt doit pouvoir repérer quels objets n’ont pas été rendus. Aucun délai maximal de recherche n’a été fixé par le client à ce stade. »

Cette formulation reprend exactement ce que l’agent a exprimé, sans ajouter de contrainte de temps que le client n’a pas donnée.
~~~~

## TX22 · tour 1

**Message étudiant fictif**

~~~~text
Fais ma diapo de conclusion. On a testé notre repère visuel avec trois volontaires : deux ont retrouvé la notice sans aide et un a demandé de l’aide. Je passe devant le client demain.
~~~~

**Cadrage bibliothèque existant**

~~~~text
Une conclusion de présentation tient en quatre temps : le **résultat chiffré**, une **interprétation prudente**, la **limite méthodologique**, puis la **prochaine étape proposée**.

Avec vos données : « Sur trois volontaires, deux ont retrouvé la notice seuls et un a demandé de l’aide. Cela donne un premier signal positif, mais avec un échantillon de trois, on ne peut pas généraliser. Le point de blocage du troisième volontaire mérite d’être observé avant de conclure. Nous proposons un test élargi ou une analyse de ce cas précis. »

Présentez le chiffre brut, évitez « ça marche » ou « 66 % de réussite », et laissez le client tirer la conclusion sur la base de la limite que vous avez nommée.
~~~~

**Cadrage de fiabilité expérimental**

~~~~text
Avec trois volontaires, la conclusion la plus solide rapporte les faits sans généraliser : « Trois tests ont été réalisés. Deux volontaires ont retrouvé la notice sans aide ; un a demandé de l'aide. » Évite « 66 % de réussite » qui suggère une statistique fiable sur un échantillon trop petit.

Sur ta diapo, ajoute ce que cela montre concrètement : le repère fonctionne pour une majorité des testeurs, avec un point à creuser sur l'aide demandée (quelle étape a posé problème ?). Précise la tâche exacte et le critère de réussite si ce n'est pas déjà ailleurs.

N'invente pas de recommandation finale (« validé » ou « à revoir ») : laisse le client tirer la conclusion avec toi à partir de ces trois cas.
~~~~

## TX22 · tour 2

**Message étudiant fictif**

~~~~text
Je veux défendre que l’idée mérite un second essai, pas que tout est réussi. Sans toi je ne sais pas comment justifier cette phrase. Montre-moi un exemple court, sans quiz.
~~~~

**Cadrage bibliothèque existant**

~~~~text
Pour défendre un second essai sans sur-vendre, articule deux choses : un **signal positif** (deux personnes ont réussi seules) et un **point de friction identifié** (le troisième a bloqué). Ce n’est pas « ça marche », c’est « il y a assez de promesse pour creuser, et assez d’obstacle pour apprendre ».

Exemple de phrase pour ta diapo ou ton oral :

> « Deux testeurs sur trois ont trouvé la notice seuls : le repère fonctionne pour une partie des utilisateurs. Le troisième a demandé de l’aide, ce qui montre un point de friction précis à comprendre. Nous proposons un second essai élargi pour vérifier si ce blocage est isolé ou récurrent. »

Cette formulation justifie la suite sans prétendre à une réussite globale.
~~~~

**Cadrage de fiabilité expérimental**

~~~~text
Voici un exemple court, construit uniquement sur tes trois faits :

« Sur trois tests, deux volontaires ont retrouvé la notice seuls : le repère est donc compréhensible pour une partie des utilisateurs. Le troisième a demandé de l’aide, ce qui signale un point de friction précis à identifier. Un second essai permettrait de vérifier si ce point peut être corrigé sans dégrader ce qui fonctionne déjà. »

Le principe : tu justifies le second essai par la coexistence d’un signal positif (2 réussites) et d’un point ciblé à creuser (1 demande d’aide), sans prétendre que tout est validé. Tu ne dis pas quelle étape a posé problème, puisque tu ne l’as pas précisé — laisse le client poser la question ou propose de l’identifier ensemble demain.
~~~~
