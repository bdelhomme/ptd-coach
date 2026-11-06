# ADR-0004 — Abstraction des modèles IA
Statut : **Principe de portabilité VALIDÉ ; interface de code PROPOSÉE** · 2026-11-06

## Décision
Mistral premier fournisseur ; tous appels via contrat fournisseur indépendant. Les prompts, compétences et scénarios sont versionnés et distincts du SDK. Le modèle ne peut ni modifier la base ni octroyer des droits. Tests pédagogiques sur cas fixes après toute migration.

## Risques
Différences de schémas, tailles de contexte, outils/streaming, prix, rétention et qualité du feedback ; tests de capacité et fallback nécessaire. Souveraineté à évaluer contractuellement.
