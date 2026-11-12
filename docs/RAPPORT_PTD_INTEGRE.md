# Première tranche de PTD Coach intégré

Branche `feat/ptd-integrated` ([PR #16](https://github.com/bdelhomme/ptd-coach/pull/16)),
issue de la [PR #15](https://github.com/bdelhomme/ptd-coach/pull/15)
au commit `5d18364966074f8915d98762f69f88ca8c816e2b`. Le [guide de recette](DEMO_PTD_INTEGREE.md)
permet de reprendre le scénario. Les conditions du pilote figurent dans une
[checklist séparée](CHECKLIST_PILOTE_PTD.md).

## Mise en œuvre

| Écran | Composants réutilisés et nouveau travail |
| --- | --- |
| Parler au coach | Service de conversation, budgets, erreurs et fournisseurs existants. Fils individuels ou d’équipe, accès à la fiche associée à un tour et retour au même fil. |
| Bibliothèque | Les dix fiches et leurs sources, exemples, modèles et repères tuteurs. Recherche locale, statut de brouillon visible. |
| Notre projet | Atelier avec types, origine humaine ou IA, source, semaine, brouillon et confirmation. Correction, suppression, partage au tuteur désigné et retrait. |
| Faire le point | Situation fictive du jeudi, repères de la semaine précédente, bilan modifiable, obstacles et prochaine action. Avancement explicite, avec six semaines simulées. |

`ptd_coach/project.py` isole la persistance et les autorisations. `server.py`
identifie le compte depuis la session, applique le CSRF et vérifie aussi un
jeton présenté sur un GET. Les instances locales intégrées utilisent des
cookies nommés par port pour les comparaisons sur le même navigateur. La
création de brouillon réutilise sa clé d’idempotence lors d’une reprise après
résultat incertain. Les écritures utilisent une version attendue. La semaine
de confirmation est distincte de la semaine de création. Les repères confirmés
avant l’ajout de ce champ gardent leur date, avec une semaine de confirmation
inconnue. Les deux bases de la démonstration sont distinctes du coach historique
et d’A2.

`ptd_coach/chat_integrated.py` ajoute le contexte versionné
`conversation-v08-ptd-integrated-experimental-0.1` au cadrage de fiabilité.
Le service lie le compte au seul assemblage du contexte après contrôle des
droits du fil. Le nouveau fil reçoit au plus cinq repères entiers, récents et
confirmés, de son périmètre. Le coach peut fournir un exemple ou un brouillon.
La copie dans l’atelier requiert un clic et conserve le périmètre et l’origine.
Confirmation et partage restent des actes humains distincts. Les données du
projet sont traitées comme du contenu et l’appel au fournisseur n’a aucun
outil d’écriture. Les anciens contextes, corpus, empreintes et le référentiel
V0.3 sont conservés. Les scénarios réservés sont exclus de la conception.

## Revue indépendante et corrections

- L’agent de stockage a développé les opérations de mémoire, les autorisations
  et leurs tests. L’agent d’interface a relié les écrans au service HTTP.
- Un agent indépendant utilisant GPT-6 Astra a relu l’architecture puis les
  chemins mémoire, partage, suppression, session et tuteur. Il a demandé de
  conserver les repères entiers pour préserver les nuances, d’ajouter un
  journal de partage sans texte ni source et de tester les modifications,
  révocations et refus entre équipes. Ces corrections sont intégrées.
- Sa relecture de l’interface a relevé deux défauts. La reprise de création
  pouvait dupliquer un brouillon, et une session devenue invalide pouvait
  laisser des éléments privés affichés. Un agent léger a finalisé les
  corrections ciblées. Les tests HTTP vérifient le rejeu et le rejet d’un
  ancien jeton, et la recette navigateur a vérifié la purge après changement
  de compte dans un deuxième onglet. La revue statique a retrouvé les garde-fous
  pédagogiques prévus. Leur efficacité reste à évaluer sur des réponses réelles.

## Recette exécutée

- Contrôle documentaire et syntaxique du dépôt, puis 151 tests locaux réussis.
  Les deux contrôles de provenance qui ouvrent le jeu réservé sont exclus de
  cette exécution locale. Aucun appel Mistral dans cette suite.
- En HTTP sans API, cinq tests traversent l’interface de service. Ils vérifient
  M03, la création et la confirmation, l’avancement, le contexte de séance, le
  partage et le retrait, la suppression, les refus par rôle et équipe, les
  sessions et l’isolation de deux appels privés concurrents. Sept tests du
  domaine exercent notamment l’édition d’un repère partagé, la revalidation,
  le rejeu après suppression, les écritures périmées et la migration du journal.
- Dans le navigateur, l’étudiant A a demandé de l’aide, consulté M03 puis
  retrouvé le même fil. Le brouillon d’origine IA a été reformulé et confirmé.
  Le bilan confirmé était visible le jeudi suivant. Le tuteur a vu la question
  partagée, puis la question a disparu après retrait du partage. À 390 × 844 px,
  le point d’étape s’affichait sans débordement horizontal. La bibliothèque et
  l’envoi d’un message privé ont été exercés à cette taille. Il s’agit d’une
  émulation dans le navigateur, avec une recette mobile physique encore à faire.

## Conversation Mistral fictive

Deux tours dans le navigateur avec `mistral-small-latest`, le contexte intégré,
une sortie plafonnée à 700 tokens, un délai de 45 s et un budget de quatre
appels pour la recette. Le premier tour demande un
exemple de cahier des charges à partir de « un système simple ». Mistral
associe la fiche M03 et distingue plusieurs statuts, mais invente la date
`2026-11-10` pour la demande. Le second tour lui signale que ni la date ni un
critère validé n’ont été communiqués. La date est retirée et les critères
restent des pistes. Cette erreur confirme le besoin de revue des sources,
y compris sur une réponse par ailleurs exploitable.

| Tour | Tokens totaux API | Latence |
| --- | ---: | ---: |
| Exemple de départ | 3 245 | 3 623 ms |
| Correction demandée | 2 891 | 1 679 ms |
| Total | 6 136 | 5 302 ms |

Cette recette vérifie la connexion et le multitour. L’[audit précédent](AUDIT_GLOBAL_PTD_2026_11_12.md)
donne la couverture des onze compétences candidates. Une évaluation de
l’apprentissage et une nouvelle campagne réelle sur l’ensemble des compétences
restent nécessaires pour juger du contexte intégré. Les résultats de ces deux
tours ne justifient aucun changement de modèle par défaut.

## Limites et reprise

La démonstration repose sur des identités fictives librement sélectionnables,
six jeudis scénarisés et une confirmation par un membre de l’équipe. L’atelier
ne déduit aucun engagement à partir d’une conversation. Le point d’étape est
rédigé par l’équipe, éventuellement avec l’aide du coach. Les notes corrigées
ou supprimées cessent d’alimenter la mémoire projet, tandis que les fils et
envois antérieurs au fournisseur ont leur propre cycle de vie. Un onglet
ancien détecte un changement de session lors de sa prochaine requête. La
recette navigateur est manuelle et les tests automatisés passent par HTTP.
