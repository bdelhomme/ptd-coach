# Mémoire sur un semestre — proposition à discuter

## État actuel

Le prototype local enregistre les messages dans la base locale de conversation
et recharge l'historique du fil autorisé pour chaque requête. Il ne rappelle pas
les autres fils, ne consolide pas l'évolution sur le semestre et ne dispose pas
d'une mémoire longitudinale de compétences. Le service refuse la suite au-delà
de 24 échanges ou 60 000 caractères d'historique utilisateur/assistant et invite
à ouvrir un nouveau fil ; ouvrir un autre fil ne transfère pas son contexte.
Les échanges sont conservés localement et envoyés à Mistral lors des requêtes.
Les comptes sont des identités de démonstration et ne garantissent pas la
confidentialité entre personnes ayant accès au Mac.

Les blocs internes de raisonnement Large ne sont ni conservés ni retransmis.
[Mistral indique](https://docs.mistral.ai/inference/conversations/reasoning)
que leur retrait peut dégrader la cohérence entre tours. Ce sont des blocs du
modèle, distincts d'une mémoire pédagogique relisible ; ils ne sauraient être
considérés comme des faits validés sur l'étudiant.

## Hypothèse de conception — non implémentée, non validée

Permettre à l'étudiant de construire et réviser une mémoire succincte, liée à
ses propres objectifs et expériences. Chaque élément affiché pourrait contenir :
une formulation courte, sa source et sa date, son statut (rapporté, hypothèse,
décision humaine confirmée), son périmètre et éventuellement une échéance de
révision. L'étudiant pourrait corriger, retirer ou refuser une proposition avant
qu'elle ne serve à un autre échange ; un résumé généré ne deviendrait pas un fait
ou une évaluation sans confirmation humaine.

Une mémoire collective distincte contiendrait seulement les éléments discutés
et explicitement validés par l'équipe ; elle ne puiserait jamais automatiquement
dans un fil privé. Les tuteurs accéderaient uniquement aux éléments collectifs
partagés selon des règles explicites. Les droits s'appliqueraient dans le serveur
avant sélection des données, pas uniquement dans les consignes au modèle.

## Arbitrages et tests nécessaires

- Quelle conservation à la fin du semestre, quelle suppression ou export, qui
  peut corriger et révoquer les éléments et quelles traces de partage garder ?
- Quelles données sont nécessaires à l'apprentissage, avec quelles autorisations
  et quelle information sur les transmissions au fournisseur IA ?
- Comment détecter un résumé inexact ou périmé et éviter qu'il s'impose comme
  diagnostic de personne, note ou jugement de compétence ?
- Comment évaluer sur des projets **fictifs** étalés dans le temps, y compris
  les changements de décision, oublis, contradictions et révocations ?
- Quelles limites de contexte, latence et coûts quand les échanges s'accumulent,
  sans présumer qu'un plus grand contexte équivaut à une mémoire fiable ?

Aucune mémoire longitudinale automatique n'est introduite dans cette tranche ;
ces points demandent une conception, des tests d'accès et une validation adaptée
avant des données réelles ou un déploiement institutionnel.
