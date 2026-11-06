# Tests du dépôt et du prototype A2

`make verify` exécute les contrôles du dépôt et 34 tests sur données synthétiques :

- Dix tests du contrôleur documentaire.
- Dix-sept tests de domaine/contrats : cycle complet, persistance après reprise,
  isolation entre étudiants et rôles, version optimiste, idempotence, sortie IA
  invalide, propositions non exécutées, contexte filtré, partage explicite,
  révocation, métadonnées d'audit et export propriétaire.
- Sept tests HTTP : session, cookie, origine/CSRF/hôte, statiques, validation des
  entrées, accès aux cycles/exports, refus d'exposition réseau et configuration.

Voir [l'environnement](../docs/DEVELOPMENT.md), [le ticket 001](../docs/tickets/001-a2-local.md)
et [les critères de recette](../docs/ACCEPTANCE_TESTS.md).

Couverture initiale de T-01/T-02/T-03/T-07/T-08/T-09/T-11/T-12/T-14/T-15 limitée
au simulateur local et à l'export, sans restauration institutionnelle. Aucun test
de SSO, Mistral, budget réel, coach collectif ou environnement de production.
Les tests du mock ne valident pas la qualité pédagogique d'un modèle réel.
Le navigateur est vérifié manuellement ; ses tests e2e automatisés restent à écrire.
