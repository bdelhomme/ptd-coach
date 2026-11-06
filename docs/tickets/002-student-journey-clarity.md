# Ticket 002 — Rendre la séance compréhensible côté étudiant

Statut : **RÉALISÉ pour la démo locale** · 2026-11-06.

## Objectif et exigences

Retour du porteur du projet : en se mettant à la place d'un étudiant, l'entrée
et la succession des formulaires sont difficiles à comprendre.
Références : F-03/F-04, D-001/D-009/D-012. Préserver la boucle pédagogique et les
permissions ; clarifier l'interface sans créer de décision pédagogique nouvelle.

## Changements

- Entrée par une situation concrète et un bouton pour commencer l'exemple guidé.
  Le choix d'un autre compte est disponible dans un volet secondaire.
- Trois moments visibles : **ici avec le coach**, **avec mon équipe**,
  **de retour ici**. Les états et contrats backend sont conservés.
- Un appel principal à l'action par écran ; exercice et plan d'action affichés
  séparément. Situation et réponse peuvent être relues dans un volet secondaire.
- Action enregistrée affichée avant la pause. Au retour, le formulaire de bilan
  s'ouvre seulement après « J'ai testé mon action ». Ce clic ne valide aucune
  expérience en base : la déclaration explicite reste exigée lors de l'envoi.
- Leçon du retour d'expérience reprise dans le champ de bilan, éditable et
  confirmée par l'étudiant ; aucune synthèse ou compétence déduite par le système.
- Partage clairement facultatif après le bilan. Historique, exports, séances
  précédentes et référentiel candidat restent accessibles à la demande.

L'exemple guidé crée une nouvelle séance dans le compte étudiant fictif A,
puis ouvre l'explication. Les séances existantes sont conservées et accessibles.
Les comptes sont toujours librement sélectionnables ; seules des données fictives
doivent être utilisées. Le fournisseur reste un simulateur déterministe.

## Fichiers

`web/app.js`, `web/style.css`, `web/index.html`, ce ticket,
`docs/PROJECT_STATUS.md` et `docs/DEVELOPMENT.md`.

## Vérifications

- `make test` : 34 tests backend/HTTP/documentaires réussis.
- Recette navigateur : entrée guidée, exercice seul, retour du coach, ouverture
  séparée du plan, sauvegarde, pause et reprise après rechargement, ouverture
  volontaire du retour d'expérience, confirmation du bilan et fin de séance.
- Vérification de l'affichage secondaire du partage et de la conservation des
  séances précédentes. Ce contrôle manuel ne prouve pas encore la compréhension
  par des étudiants ; une relecture et un essai utilisateur restent nécessaires.

Travail initial sur `feat/student-journey-clarity`, issue de `feat/a2-local-prototype`,
ensuite publié avec la [pull request 2](https://github.com/bdelhomme/ptd-coach/pull/2).
Contrôles de publication : voir [PROJECT_STATUS.md](../PROJECT_STATUS.md).
