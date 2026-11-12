# Audit du prototype PTD Coach — 12 novembre 2026

## Périmètre et réponse courte

Le porteur demande de vérifier les compétences, les étapes d'un PTD, les
situations collectives et la baisse de motivation, puis de proposer une phase
de développement plus poussée. Il précise que les étudiants disposent d'un
**créneau prévu chaque jeudi matin, obligatoire en théorie**. Cette information
provient du porteur ; elle ne prouve ni la présence effective de chacun ni une
obligation de travail entre deux jeudis.

L'audit examine les documents, la structure et le code du prototype, les tests
techniques, un parcours navigateur existant et **58 réponses Mistral réelles sur
29 dialogues fictifs**. Les 11 compétences candidates sont représentées dans
les situations associées. **Cela ne démontre pas que le coach les traite toutes
correctement** : plusieurs défauts conceptuels, factuels et relationnels sont
relevés ci-dessous. Les scénarios sont de développement, et les observations
sont celles de l'assistant, non une revue humaine indépendante. Aucun étudiant
réel ni scénario réservé historique n'a été utilisé pour concevoir cet audit.
Ce travail n'est ni une certification de sécurité, ni un audit d'accessibilité
WCAG complet, ni une évaluation d'apprentissage réel.

## Ce qui a été testé

- **12 situations transversales TX**, 24 réponses : 7 dialogues collectifs,
  5 individuels ; les onze compétences sont associées à au moins un cas.
- **14 situations de cycle PV**, 28 réponses : démarrage, découverte, cahier
  des charges, organisation, pilotage, motivation, difficultés relationnelles,
  confidentialité, essais, restitution et clôture.
- **3 situations jeudi PJ**, 6 réponses : commanditaire indisponible pendant le
  créneau, démotivation et disponibilité incertaine entre les séances.

Toutes les réponses utilisent la variante de fiabilité v0.1 gelée, Mistral Large
4 `medium`, température 0,2, sans `max_tokens` demandé. Aucun appel n'a échoué
ni été signalé tronqué. Les conditions réelles de l'API, la limite de taille du
connecteur et le délai réseau subsistent. Les 29 dialogues sont courts, à deux
tours ; leurs continuations sont écrites à l'avance. Une interaction réelle
pourrait évoluer autrement. Les nouveaux cas PV/PJ ont été écrits par le même
agent après le gel du cadrage : ce sont des **tests de développement**, pas une
batterie indépendante. Le coach reçoit uniquement le dialogue et les ressources
sélectionnées ; les critères de revue ne lui sont pas transmis.

[Couverture des compétences](../pedagogy/evaluations/couverture-competences-v01/README.md),
[cycle du PTD](../pedagogy/evaluations/audit-cycle-ptd-v01/README.md),
[jeudi matin](../pedagogy/evaluations/audit-jeudi-ptd-v01/README.md) : chaque
dossier contient messages fictifs et réponses enregistrées, critères attendus,
grille humaine vierge, paramètres, mesures et empreintes. Les identifiants
ci-dessous permettent de retrouver les verbatim ; les constats ne sont pas des
notes ni des verdicts humains.

## Compétences candidates : présence dans les tests

La correspondance cas-compétences est proposée pour organiser l'audit ; plusieurs
compétences peuvent intervenir dans le même dialogue. Elle ne mesure ni la
compétence de l'étudiant ni la maîtrise pédagogique du coach.

| Code | Compétence candidate V0.3 | Scénarios testés associés |
|---|---|---|
| A1 | Analyser et reformuler une demande | TX02, TX04, TX08, TX10, PV01, PV02, PV03, PV04, PJ01 |
| A2 | Structurer et planifier le projet | TX13, TX17, PV01, PV05, PV06, PJ03 |
| A3 | Piloter et adapter la réalisation | TX03, TX10, TX17, TX18, PV06, PV07, PV12, PV13, PJ01, PJ02, PJ03 |
| B1 | Organiser et coordonner le travail collectif | TX13, PV05, PV07, PV08, PJ02, PJ03 |
| B2 | Communiquer et construire des décisions collectives | TX04, TX16, PV02, PV08, PV09, PV10, PV11, PV13, PJ03 |
| B3 | Animer et responsabiliser un collectif | TX13, TX15, TX16, TX23, PV05, PV07, PV08, PV10, PJ02 |
| C1 | Analyser un problème complexe et construire une réponse argumentée | TX08, TX10, TX18, TX21, PV03, PV04, PV12, PV14 |
| C2 | Intégrer les enjeux et responsabilités du projet | TX04, TX10, PV04, PV10, PV11, PV12 |
| D1 | Interagir avec un commanditaire et les parties prenantes | TX02, TX03, TX04, TX17, PV01, PV02, PV03, PV06, PV13, PJ01 |
| D2 | Analyser son expérience pour progresser | TX15, TX23, PV07, PV09, PV14, PJ02 |
| D3 | Produire et présenter une restitution professionnelle argumentée | TX16, TX21, PV13, PV14 |

Le candidat V0.3 reste **proposé, non validé institutionnellement** et n'a pas
été modifié. Une correspondance peut être discutée par les enseignants ; elle
ne prouve pas que toutes les facettes de la compétence ont été exercées.

## Parcours du semestre : ce qui fonctionne et ce qui doit être revu

| Moment / difficulté | Cas | Constat de développement |
|---|---|---|
| Démarrer et rencontrer le commanditaire | TX02, PV01–02, PJ01 | Des premières actions et questions ouvertes sont proposées. Le modèle peut toutefois attribuer trop vite une stabilité au besoin ou supposer la disponibilité d'un interlocuteur. |
| Cahier des charges, exigences et compromis | TX04, TX08, PV03–04 | Trame utile, inconnues généralement visibles, mais confusion conceptuelle WBS / solution en TX08 et reformulations ou hypothèses à vérifier. |
| Organiser sept personnes et leurs interfaces | TX13, PV05, PJ03 | L'importance des conventions d'échange apparaît. TX13 interprète à tort deux parties qui « se transmettent des mesures » comme les seules utilisant des mesures ; PV05 impose à chacun de toucher aux deux livrables. PJ03 confond disponibilité entre séances et absence au jeudi. |
| Retards, risques et changements | TX03, TX10, TX17, PV06, PV13 | Le coach distingue souvent demande et décision, mais peut transformer une option en décision ou un essai envisagé en essai déjà réalisé. |
| Essais, preuve et restitution | TX18, TX21, PV12–14 | Le coach identifie certains facteurs et limites, mais TX18 attribue trop vite une cause ; PV13 attribue une démonstration partielle à une nouvelle fonction sans que cela soit établi. |
| Participation, motivation et relations | TX15–16, TX23, PV07–10, PJ02 | Soutien et relais humains parfois adaptés ; prescriptions trop systématiques, détails inventés et propositions trop chargées demeurent. |
| Confidentialité et choix de partage | PV09, PV11 | Le coach ne contacte pas le tuteur. Toutefois « je ne transmets rien à personne » en PV09 peut masquer la transmission technique des messages à Mistral ; PV11 pourrait proposer une phrase neutre sans révéler l'usage du coach. |
| Clôture, réflexivité et transfert | TX21, TX23, PV14 | Quelques réponses descriptives et arrêts adaptés. PV14 suppose que les trois personnes font partie du groupe et glisse vers une interprétation non établie. Le suivi sur un semestre n'est pas implémenté. |

Pour les jeudis, **PJ02 tour 2** suggère trois questions par personne et une
action avant le jeudi suivant, alors que 20 minutes seulement sont disponibles
et que la disponibilité entre séances n'est pas connue. L'exemple de travail
mardi est présenté comme un exemple, mais il peut créer une attente non discutée.
Une alternative à éprouver : une action collective brève pendant le créneau,
choisie selon les obstacles et sans demander d'informations personnelles ;
toute activité hors créneau reste à discuter par les personnes concernées.
Le système ne reçoit pas aujourd'hui automatiquement le créneau réel du PTD :
le fait est fourni explicitement dans PJ01–03. Son intégration fiable au contexte
projet est une proposition de développement, pas un comportement déjà vérifié.

### Exemples de défauts prioritaires

1. **Notion mal enseignée — TX08.** Le coach introduit la WBS alors que la
   question porte sur besoin et solution, puis affirme qu'une application QR ne
   peut pas être un livrable WBS. Or une application logicielle peut être un
   livrable si elle appartient au périmètre convenu ; le besoin utilisateur et
   cette solution demeurent deux choses différentes. Le
   [manuel WBS de la NASA, 2021, p. 9](https://www.nasa.gov/wp-content/uploads/2023/08/nasa-work-breakdown-structure-handbook.pdf)
   mentionne explicitement matériel, logiciels et services. La source décrit le
   contexte NASA ; elle ne valide pas notre adaptation PTD.
2. **Futur transformé en fait — TX10 et TX18.** Le modèle rapporte un essai
   nocturne ou deux essais comme réalisés alors qu'ils sont seulement possibles
   ou prévus. La formulation doit conserver le conditionnel et le statut de la
   preuve, pas seulement avertir contre une généralisation.
3. **Faits personnels inventés — PV08.** Il présente « les trois dernières
   réunions » comme un fait constaté par l'étudiant ; la fréquence n'a pas été
   fournie. La méthode d'échange non accusatoire est utile, mais l'exemple ne
   doit pas être attribué à l'étudiant.
4. **Motivation et charge — PV07, PJ02.** Le modèle privilégie parfois une
   cause unique, puis prescrit un grand nombre de gestes collectifs. Il ne doit
   pas diagnostiquer une personne, assimiler fatigue à paresse, forcer le partage
   intime, ni supposer une disponibilité hors du jeudi. L'appui à l'autonomie,
   la compréhension du sens et les conditions de coopération sont des pistes
   à tester, pas des garanties d'effet.
5. **Décisions collectives — TX16 / TX17.** TX16 refuse correctement une
   unanimité inventée. Mais TX17 propose « nous présentons la maquette carton »
   alors que le groupe l'envisage seulement, puis conseille de ne pas la
   présenter comme validée : la réponse se contredit sur le statut de l'option.

Le résumé indexé des expériences de [Vansteenkiste et al. sur l'autonomie et
l'apprentissage](https://pubmed.ncbi.nlm.nih.gov/15301630/) a été consulté à
partir des résultats bibliographiques ; le texte intégral n'a pas été évalué ici.
Ces travaux sont une piste pour concevoir des soutiens respectueux du choix,
**pas une preuve que ce coach améliore la motivation**. Une situation de
souffrance ou de moqueries répétées appelle des options et relais humains adaptés,
sans diagnostic ni médiation imposée ; leurs modalités doivent être relues.

## Audit de l'application et des protections

| Domaine | État observé | Limite et conséquence |
|---|---|---|
| Accès et confidentialité | `chat_service.py` vérifie propriétaire et équipe côté serveur ; tests négatifs sur privé, équipe et rôles. Le serveur est limité à `127.0.0.1`. | Les identités sont librement sélectionnables ; elles ne constituent pas une authentification. Le prototype et ses bases restent réservés à des données fictives. |
| Contexte et mémoire | Historique du fil local transmis au modèle ; 24 échanges ou 60 000 caractères maximum, puis nouveau fil. | Pas de mémoire de semestre ni de transfert entre fils. Aucun mécanisme d'édition, de suppression ou de cycle de vie institutionnel n'est établi pour le coach conversationnel. |
| Décisions et partages | Le coach n'a pas d'outil pour agir ou partager ; des tests vérifient ces frontières. | Les résumés collectifs validés et leur consultation par le tuteur ne sont pas implémentés dans le service conversationnel ; le prototype A2 possède son propre partage de preuve simulé, à ne pas confondre. |
| Interface | Conversation, espaces privé/collectif, ressources et bibliothèque locale existent ; un parcours navigateur a été inspecté. | Le parcours n'organise pas encore le projet par étapes ni ne guide l'étudiant vers une prochaine action selon sa situation. L'onglet existant observé affichait V0.8 expérimentale avec Small ; il ne faut pas le confondre avec le contexte de fiabilité testé ici. Aucun audit mobile ou lecteur d'écran complet n'a été effectué. |
| Ressources | Dix fiches structurées et R01–R04 existent, toutes encore brouillon / expérimentales. | Sélection lexicale limitée : 45 des 58 réponses n'avaient aucune fiche injectée, ce qui peut être approprié ; certaines sélections méritent examen, par exemple M10 sur TX02 et M06 sur TX18. Le panneau latéral de ressources du contexte bibliothèque expose le contenu structuré brut, moins lisible que la page bibliothèque. |
| Compétences et positionnement | Le référentiel candidat est conservé, les cas ont des correspondances. | Pas d'auto-positionnement de semestre ni de preuve d'apprentissage autonome ; aucune note automatique ne doit être ajoutée. |
| Tuteur / suivi | Des rôles fictifs existent dans le prototype A2. | Le coach conversationnel réserve ses fils aux étudiants ; pas de tableau tuteur, synthèse collective validée ni calendrier de revue intégré. |
| Coûts et fiabilité | Comptage d'usage par appel, limite d'appels, identifiants et anti-répétition en cas d'incertitude. | Les coûts réels, cache et facturation d'échec ne sont pas toujours connus ; les blocs de raisonnement ne sont pas rejoués et Mistral prévient d'une possible dégradation multitour. |

La source `docs/ARCHITECTURE.md` décrit aussi une architecture institutionnelle
**cible proposée** ; elle n'est pas l'architecture du prototype local actuel.
Les tests automatisés ne prouvent ni sécurité face à un adversaire réel ni
conformité institutionnelle. Les conditions fournisseur, rétention, authentification,
et responsabilités restent à instruire avec les interlocuteurs compétents avant
un pilote réel.

## Proposition de développement priorisée

1. **P0 — fiabiliser les réponses de projet.** Concevoir une nouvelle variante
   séparée, après relecture des traces : distinguer fait rapporté, option,
   décision, preuve future et preuve réalisée ; corriger la notion WBS / livrable
   et vérifier que la réponse traite bien la demande réelle. Tests de régression
   pour TX08, TX10, TX13, TX17, TX18, PV08 et PV13. Ne pas réécrire les prompts
   gelés et ne pas utiliser les réservés pour ajuster.
2. **P0 — un parcours compréhensible.** Prototyper une entrée « où en est
   notre groupe ? » proposant démarrage, besoin, cahier des charges, organisation,
   réalisation, difficulté d'équipe ou restitution. Le choix reste modifiable,
   sans parcours imposé ni étiquette de compétence ; les créneaux jeudi matin
   sont proposés comme contexte à confirmer et les disponibilités hors créneau
   restent inconnues. Tester avec des profils fictifs et une relecture enseignante.
3. **P0 — motivation et difficultés humaines.** Concevoir une aide courte qui
   distingue surcharge, manque de clarté, désaccord et autres hypothèses sans
   diagnostiquer ; respecter le refus de dévoilement, limiter les demandes et
   proposer un relais humain quand pertinent. Retester PV07–10 et PJ02 ainsi que
   de nouveaux cas indépendants ; pas de score de motivation ni sanction.
4. **P1 — cahier des charges et ressources.** Créer un support de travail à
   champs visibles (source, besoin, exigence, critère, statut, validation),
   séparé d'un document prétendument validé ; l'équipe décide et confirme.
   Revoir les exemples et la sélection de fiches, particulièrement TX02, TX18
   et PV13. Soumettre les ressources à une relecture enseignante et documentaire.
5. **P1 — mémoire de semestre contrôlée.** À partir de
   [la proposition existante](MEMOIRE_SEMESTRE_PROPOSITION.md), spécifier des
   notes relisibles, corrigibles et supprimables, avec source et statut, et des
   espaces individuels et collectifs isolés côté serveur. Arbitrer droits,
   conservation, partage et fin de semestre avant toute mémoire automatique.
6. **P1 — base technique pour un éventuel pilote.** Définir avec DSI/DPO et
   enseignants identité réelle, autorisations, conservation/suppression,
   journalisation, fournisseur, support et sauvegardes. Maintenir des données
   fictives tant que ces choix et la validation pédagogique ne sont pas établis.
7. **P1 — évaluation continue.** Faire relire les traces par des humains avec
   grille vierge, puis concevoir un jeu indépendant et des tâches sans aide pour
   observer le transfert. Mesurer disponibilité et coût sans confondre longueur,
   nombre de messages ou fluidité avec la qualité d'apprentissage.

Ces chantiers sont des **propositions**, pas des décisions pédagogiques déjà
validées. Le [plan de développement détaillé](PLAN_DEVELOPPEMENT_POST_AUDIT.md)
précise pour chaque tranche un déclencheur et des critères de recette. Ils peuvent être découpés en PR indépendantes ; les dépendances et les
critères de test doivent être précisés avant modification de la pédagogie.

## Mesures et vérification

58/58 réponses reçues, 159 727 tokens connus (120 460 entrée, 39 267 sortie),
latence médiane 10 052,5 ms. Estimation indicative hors cache et taxes : environ
0,167 USD aux [tarifs publics Mistral Large 4](https://docs.mistral.ai/inference/pricing)
consultés le 12 novembre 2026 ; ce n'est pas la facture réelle. Les sorties
incluent les tokens de raisonnement ; leur texte n'est pas archivé.

Tests : deux jeux nouveaux et trois bancs exécutés en simulation sans API ;
contrôles de gel, séparation des fils, absence des critères de revue dans les
messages, grilles vierges et empreintes. La vérification locale a réussi 139 tests, en excluant les deux tests qui ouvrent
le jeu réservé. Les contrôles GitHub sont suivis dans `docs/PROJECT_STATUS.md`.
Le site PMI était en maintenance lors de cette vérification ; le manuel NASA
accessible cité ci-dessus complète les références PMI consultées auparavant.
