# ADR-0001 — Portabilité de l'application et des assistants
Statut : **PROPOSÉ, non approuvé par DSI** · 2026-11-06

## Contexte
Prototype financé/administré provisoirement par le porteur du projet ; exploitation institutionnelle souhaitée ; plusieurs assistants IA et développeurs susceptibles de se succéder.

## Décision proposée
Git comme source de vérité, Markdown + schémas JSON versionnés, conteneurs, stockage PostgreSQL et objet interopérable, fournisseurs IA en adaptateurs. Environnement de démonstration avec données fictives. Aucune plate-forme unique requise.

## Alternatives
Plate-forme no-code ou agent hébergé par un fournisseur (rapidité de prototype, moindre portabilité) ; infrastructure institutionnelle immédiate (dépendances de gouvernance avant preuve de concept).

## Conséquences
Nécessite documentation, tests et CI ; facilite hébergement cible DSI et passations. Ne garantit pas à elle seule la conformité juridique.
