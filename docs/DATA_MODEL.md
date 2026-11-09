# Modèle de données conceptuel — v0.1

**Statut : conceptuel ; ne présume ni schéma SQL validé, ni décisions RGPD finales.**

## Entités
- `User`, `RoleAssignment(scope, from, to)`, `Cohort`, `Team`, `TeamMembership`.
- `Project`, `Milestone`, `ProjectDecision(status: proposed|confirmed|superseded)`, `ProjectArtifact`.
- `CollectiveSession`, `CollectiveMessage`, `CollectiveSummary(status: draft|validated|superseded)`, `TutorGuidance`.
- `Competency(id, version)`, `LearningGoal`, `LearningCycle`, `LearningActivity`, `LearningAttempt`, `Experiment`, `Reflection`, `Evidence`.
- `PrivateConversation`, `PrivateMessage`, `ShareGrant`, `AccessRequest`, `AuditEvent`.
- `AIInvocation(model_id, provider, prompt_version, tokens_in, tokens_out, latency_ms, cost_estimate)`.
- `PedagogicalResource`, `Scenario`, `PromptConfiguration`.

## Contrainte de confidentialité
- `PrivateConversation.owner_user_id` et objets liés sont accessibles au propriétaire seulement ; tutorat et coordination n'ont pas de droit implicite.
- `CollectiveMessage.team_id` est réservé aux membres de l'équipe ; le tuteur ne reçoit que `CollectiveSummary.status=validated`, sauf accès ciblé approuvé et journalisé.
- `Evidence` est privée sauf `ShareGrant` explicite, lié à un objet déterminé, destinataire et droit (`view`) limité ; révocation pour l'avenir, sans garantie de retrait d'un export antérieur.
- Les `AIInvocation` d'usage financier ne recopient pas le contenu conversationnel ; les journaux techniques ne doivent pas constituer un accès caché.
- La coordination ne reçoit pas de texte de message ; seuls compteurs et synthèses générales selon règles validées, prudence sur faibles effectifs et ré-identification.
- Le contexte transmis au fournisseur est assemblé **après filtrage backend** des droits ; jamais à partir d'une recherche globale sur les journaux.

## Exigences de modélisation
IDs immuables (UUID recommandés), versions du référentiel et des scénarios, timestamps UTC, auteur/provenance des déclarations, état confirmé ou proposé, idempotence des commandes, politiques de rétention documentées, migrations réversibles ou compensatoires. Le schéma SQL réel devra être revu et testé.

## Exemple de cycle individuel
Voir `pedagogy/scenarios/A2-first-cycle.json`. Aucun progrès n'est déduit de la date cible ni du texte de l'IA ; une expérimentation terminée reste un fait *déclaré*.

## Implémentation locale conversation.v1 — D-026

Base séparée : `conversations` (scope immuable, propriétaire/équipe, version,
pending), `chat_messages` (rôle/texte/auteur), `chat_requests` (clé idempotente,
empreinte de commande, statut et métadonnées d'usage sans texte). Version SQLite
1 indépendante d'A2 ; aucune migration de l'ancien schéma. Le contexte contient
seulement les messages du fil préalablement autorisé. Voir
[le contrat v1](CONVERSATION_API_V1.md) et ADR-0007.
