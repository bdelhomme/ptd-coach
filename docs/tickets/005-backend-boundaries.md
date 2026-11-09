# Ticket 005 — Vérifier les frontières backend du futur coach

**Statut : PROPOSÉ, NON DÉMARRÉ.** Dépend des futures routes/contrats et de
l'étape 2. Références : F-01/F-04/F-06/F-09/F-13/F-14, D-007/D-009/D-012/D-025.

## Existant à préserver

Les tests A2 contrôlent déjà privé interutilisateurs/interéquipes, rôles tuteur,
coordination et admin, contexte filtré, partage ciblé/révocation, export
propriétaire, idempotence et refus des propositions d'écriture du modèle.
Ils ne couvrent pas un futur coach collectif ou un index de recherche inexistant.

## Matrice à couvrir avant extension

- Deux membres d'une même équipe, un autre étudiant d'une autre équipe,
  tuteur, coordination et admin : refus de lecture/écriture privée à tous les
  points d'entrée, contexte IA compris.
- Synthèses collectives : brouillon invisible au tuteur ; validation humaine
  requise, corrections/refus sans diffusion ; aucune validation par le modèle.
- Partage : objet et destinataire explicites, confirmation par la personne
  autorisée ; refus d'un consentement rapporté par un tiers, retrait avant
  confirmation, révocation d'accès futur, portée limitée de l'export.
- Recherche, cache, exports, sauvegardes et logs : aucun chemin détourné vers
  le privé ; tests uniquement si ces capacités sont implémentées, sinon les
  marquer non disponibles. Journaux sans verbatims privés ni secrets.
- Écritures : proposition séparée, version/idempotence contrôlées, rollback en
  cas d'erreur, aucun succès d'enregistrement inventé.

## Recette attendue

Tests négatifs exécutables avec identités synthétiques et assertions côté
service/persistance/HTTP, hors confiance dans le prompt. Un refus LLM dans
V0.6/V0.7 ne prouve pas l'isolation du système. Mettre à jour le modèle de données,
la confidentialité et les limites de couverture lors de l'implémentation.
