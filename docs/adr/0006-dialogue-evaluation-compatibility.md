# ADR-0006 — Compatibilité des expériences de dialogue V0.6/V0.7

Statut : **PROPOSÉ, aucune migration implémentée** · 2026-11-09.
Références : D-009/D-010/D-012/D-019/D-020 à D-025.

## Contexte

Le prototype A2 utilise des transitions et des schémas versionnés, validés côté
backend. V0.6 propose sept intentions combinables selon le besoin ; V0.7 fournit
un prompt et un banc de conversations fictives en texte libre. Une intention
conversationnelle n'est ni un état métier ni un niveau de compétence.

## Proposition

Conserver ces outils hors de `ptd_coach/` et `web/`. Ils ne lisent pas la base
du prototype, ne s'authentifient pas comme étudiants et ne persistent aucun
objet métier. Leurs JSONL de recette ne sont pas des réponses conformes au
contrat API applicatif et ne doivent pas y être injectés comme telles.

Avant toute future intégration applicative, versionner explicitement le contrat,
définir la correspondance intentions / commandes humaines / transitions, les
sorties rejetées, l'idempotence et une migration compatible avec les anciens
cycles. Les propositions de mémoire restent séparées des écritures confirmées.
Le candidat V0.3 et les anciens scénarios restent lisibles sans conversion.

## Frontières et suite

Un prompt ne contrôle pas les droits. L'assemblage du contexte, les exports,
la mémoire et les partages restent filtrés par le backend, avec confirmation
humaine et provenance. La recette des sorties LLM et les tests d'isolation du
backend sont distincts. Voir [ticket 004](../tickets/004-conversation-router.md)
et [ticket 005](../tickets/005-backend-boundaries.md).

L'import de V0.7 conserve le chemin API expérimental fourni, sans le développer
en coach applicatif ni l'exécuter. D-025 réserve ce développement à une étape 2.
Le dry-run n'est pas un simulateur pédagogique : il produit des réponses nulles.
