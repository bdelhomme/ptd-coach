# Tests du dépôt et du prototype A2

V0.8 (D-029) : `make verify` exécuté avec **96 tests réussis**, sans API payante.
Le lot couvre également migration/version par fil, isolation V0.8, gel et
provenance des corpus. Recette réelle distincte : 12 réponses sur deux cas de
développement ; réservé non exécuté. Voir [le bilan V0.8](../docs/V08_IMPLEMENTATION.md).

`make verify` exécute les contrôles du dépôt et 78 tests sur données synthétiques :

- Douze tests du contrôleur documentaire, dont liens verbatim et maintien du contrôle des secrets.
- Dix-sept tests de domaine/contrats : cycle complet, persistance après reprise,
  isolation entre étudiants et rôles, version optimiste, idempotence, sortie IA
  invalide, propositions non exécutées, contexte filtré, partage explicite,
  révocation, métadonnées d'audit et export propriétaire.
- Sept tests HTTP : session, cookie, origine/CSRF/hôte, statiques, validation des
  entrées, accès aux cycles/exports, refus d'exposition réseau et configuration.
- Douze tests des outils V0.7 (six fournis, six supplémentaires) : cas/tours,
  dry-run sans appel, isolation des historiques et exclusion des rubriques du
  contexte de test, erreur simulée sans suite inventée, sélection, refus des
  données non synthétiques, grilles humaines incomplètes, seuil et veto.
- Deux tests d'intégration : empreinte inchangée du candidat V0.3 et inventaire
  des 14 fichiers importés sans deuxième copie des cas V0.6.

Les suites pédagogiques JSON contiennent **20 cas à un tour** (huit marqués
critiques) et **12 cas à plusieurs tours** (26 tours), soit 46 réponses potentielles.
Ces cas ne sont pas 46 tests de modèle réussis : les dry-runs produisent
uniquement `response: null` / `status: not_called`. Les doubles de fonction
utilisés par les tests n'appellent aucun modèle. Voir
[le mode d'emploi](../docs/EVALUATION_TOOLS_V07.md).

Voir [l'environnement](../docs/DEVELOPMENT.md), [le ticket 001](../docs/tickets/001-a2-local.md)
et [les critères de recette](../docs/ACCEPTANCE_TESTS.md).

Couverture initiale de T-01/T-02/T-03/T-07/T-08/T-09/T-11/T-12/T-14/T-15 limitée
au simulateur local et à l'export, sans restauration institutionnelle. Aucun test
de SSO, Mistral, budget réel, coach collectif ou environnement de production.
Les tests du mock ne valident pas la qualité pédagogique d'un modèle réel.
Le navigateur est vérifié manuellement ; ses tests e2e automatisés restent à écrire.

## Conversation applicative — 24 tests supplémentaires

`test_chat.py` : 19 tests (domaine, fournisseurs, configuration, reprise,
isolation des contextes, concurrence et ledger, limites, comptage réel/factice,
rejeu des 46 tours V0.6/V0.7 à travers le service avec fournisseur de test).
`test_chat_http.py` : cinq tests des nouvelles routes, rôles/CSRF, ressources,
export et erreurs de clé. Tous restent hors API externe ; la CI n'a pas de clé.
Les résultats API réels et la recette navigateur sont séparés dans
[CONVERSATION_COACH_REPORT.md](../docs/CONVERSATION_COACH_REPORT.md).

## Corpus public de revue — quatre tests de fidélité supplémentaires

`test_published_evaluations.py` vérifie les 27 fichiers et leurs manifestes,
les 80 réponses et 160 blocs verbatim, les critères/scopes/tokens, les grilles
vierges et l'empreinte des contextes. Il ne contacte pas Mistral et ne note pas
le coach. Les deux nouveaux tests du contrôleur restent documentaires.
