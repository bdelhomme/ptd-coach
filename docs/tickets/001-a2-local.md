# Ticket 001 — Première tranche verticale A2

Statut : **RÉALISÉ pour le périmètre du prototype local** · 2026-11-06.
Relecture pédagogique et validation institutionnelle toujours ouvertes.

## Besoin et références

Un étudiant fictif anticipe les dépendances, s'entraîne, prépare une expérimentation,
rapporte son expérience et conserve un bilan privé. Il peut partager une preuve
qu'il choisit avec son tuteur. D-001/D-009/D-010/D-012 ; F-01/F-03/F-04/F-09/F-12/F-13/F-14.
Architecture provisoire : [ADR-0005](../adr/0005-local-a2-prototype.md).

## Parcours et écrans

1. Entrée explicite dans un compte fictif ; rappel du périmètre de démonstration.
2. Choix de l'objectif A2 et d'un des trois cas proposés (retard client, ressource
   partagée, tâches dépendantes), sans changement du référentiel candidat.
3. Explication puis exercice ; réponses et feedback de simulation persistés.
4. Plan d'action : action, occasion prévue et observation recherchée.
5. Attente d'expérience ; aucun débrief déduit du temps écoulé.
6. Déclaration explicite de l'expérience ; faits rapportés, interprétation et leçon.
7. Bilan personnel rédigé et sauvegardé ; clôture facultative sans niveau attribué.
8. Saisie d'une preuve sélectionnée, aperçu du destinataire et confirmation explicite ;
   révocation possible. Le tuteur reçoit seulement cette preuve, jamais le dialogue.

Les libellés de feedback sont **PROPOSÉS**, à valider par un encadrant.
Le scénario `A2-first-cycle.json` version 0.1 et le référentiel candidat restent inchangés.

## Définition de terminé pour le prototype

- Interface exécutable en local ; reprise d'un parcours après interruption.
- Isolation backend entre étudiants, tuteur, coordination et administrateur.
- Fournisseur simulé remplaçable ; entrée filtrée et sortie validée avant écriture.
- Transitions explicites, contrôle de version et commandes idempotentes.
- Partage d'un objet sélectionné, révocation et export personnel.
- Tests automatisés et parcours navigateur exécutés ; documentation et état actualisés.

Les tests du prototype ne valident ni le SSO, ni l'infrastructure institutionnelle,
ni la pédagogie, ni le déploiement réel. Les critères de feedback sur trois cas
restent à relire ; T-04/T-05/T-06/T-10/T-13 et migration institutionnelle hors périmètre.

## Contrat HTTP v0.1 du prototype

JSON uniquement pour `/api/*`, erreurs `{error: {code, message}}` sans contenu privé.
Cookie HttpOnly/SameSite=Strict, `X-CSRF-Token` et origine identique pour les mutations.
Les commandes de domaine exigent `Idempotency-Key` (UUID). Un même identifiant
avec un autre contenu est refusé ; une reprise identique restitue le résultat
enregistré. `version` est obligatoire pour modifier un cycle ou une preuve.

| Méthode / chemin | Entrée / sortie | Autorisation |
|---|---|---|
| GET `/api/demo-users` | Comptes fictifs | Démo locale |
| POST `/api/demo-session` | `user_id` → utilisateur et jeton CSRF | Démo locale, origine contrôlée |
| DELETE `/api/demo-session` | Fermeture de session | Session + CSRF |
| GET `/api/me` | Utilisateur courant, jeton CSRF | Session |
| GET `/api/cases` | Trois cas A2 proposés | Session |
| GET `/api/cycles` | Cycles du propriétaire | Étudiant |
| POST `/api/cycles` | `case_id` → cycle initial | Étudiant |
| GET `/api/cycles/{id}` | Cycle et messages privés | Propriétaire étudiant |
| POST `/api/cycles/{id}/actions` | `action`, `version`, `fields` → cycle | Propriétaire étudiant |
| GET `/api/cycles/{id}/export` | Export JSON versionné | Propriétaire étudiant |
| POST `/api/cycles/{id}/shares` | `version`, `text`, `recipient_id`, `confirmed` | Propriétaire étudiant |
| GET `/api/shares` | Preuves émises / reçues explicitement | Étudiant propriétaire / tuteur destinataire |
| DELETE `/api/shares/{id}` | `version` → révocation | Propriétaire étudiant |

`actions` : `learn`, `practice`, `answer`, `plan`, `start_experience`, `report`,
`review`, `close`. La transition et les champs permis dépendent de l'état ; le
client ne transmet aucun rôle, propriétaire, contexte autorisé ou état cible.
Les versions du scénario et du référentiel sont attachées au cycle et à l'export.

## Vérification exécutée

- `make test` : 34 tests réussis, dont 24 tests applicatifs/HTTP/contrats.
- Navigateur : objectif → explication → exercice et feedback → plan d'action →
  attente → expérience déclarée → bilan privé → clôture ; reprise après rechargement.
- Navigateur : seul le texte sélectionné apparaît chez le tuteur ; après révocation,
  son écran affiche « Aucune preuve reçue ».
- Redémarrage réel du serveur effectué ; les données locales sont conservées et
  les sessions en mémoire doivent être rouvertes.
- Travail initial sur `feat/a2-local-prototype`, ensuite publié avec la
  [pull request 2](https://github.com/bdelhomme/ptd-coach/pull/2).
  Contrôles de publication : voir [PROJECT_STATUS.md](../PROJECT_STATUS.md).
