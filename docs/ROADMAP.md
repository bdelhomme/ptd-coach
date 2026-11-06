# Feuille de route priorisée — tâches et livrables

## Priorité actuelle — cadrage du coaching (ticket 003)

Cette priorité précède l'ajout d'exercices ou l'extension du prototype.
Principes confirmés : D-020 à D-023 ; voir [COACHING_FRAMEWORK.md](COACHING_FRAMEWORK.md).

- [x] Consigner les orientations confirmées, propositions et questions dans les documents.
- [x] Vérifier un premier corpus de notices/sommaires/résumés sur sources primaires (lecture intégrale et choix du corpus à faire).
- [ ] Discuter le cadre global sourcé et l'articulation sources → situations PTD → apprentissages → compétences candidates.
- [ ] Co-concevoir une première fiche A2 : capacités, situations, positionnement et limites d'aide.
- [ ] Préciser les ressources utiles et leurs sources/droits/relecture.
- [ ] Construire et discuter les fiches des dix autres compétences candidates.
- [ ] Définir les modalités du positionnement formatif privé et de sa reprise après action.
- [ ] Faire relire les fiches et exemples par les encadrants ; distinguer accord du porteur et validation institutionnelle.
- [ ] Déduire les évolutions applicatives et tests du cadrage retenu, puis reprendre l'implémentation.

## P0 — Documentation fondatrice (réalisé dans le bootstrap)
- [x] Créer dossier Git versionnable, README, AGENTS, état courant.
- [x] Consigner décisions VALIDÉES et hypothèses PROPOSÉES.
- [x] Documenter planning et grilles existants sans modifier leur contenu.
- [x] Décrire acteurs, parcours, objets métier, confidentialité, IA et hypothèses de coûts.
- [ ] Faire relire les décisions aux responsables pédagogiques.

## P1 — Premier parcours individuel A2, sans données réelles

Le prototype local décrit par les tickets 001/002 fournit une base technique ;
ses exercices restent expérimentaux. Les tâches applicatives ci-dessous ne
doivent pas prendre le pas sur la priorité de conception ci-dessus.
- [ ] Définir les critères de feedback sur 3 cas de planification, validés par un encadrant.
- [x] Définir écrans et contrats API du prototype A2 local (ticket 001 ; exhaustivité institutionnelle à revoir).
- [x] Documenter une architecture provisoire pour la démonstration (ADR-0005 ; choix DSI toujours ouvert).
- [ ] Initialiser backend, frontend, DB et Docker Compose local.
- [x] Développer accès fictif et autorisations individuelles dans le prototype local.
- [x] Développer cycle d'apprentissage avec fournisseur simulé local.
- [ ] Compléter les tests : domaine/HTTP/confidentialité exécutés ; e2e navigateur manuel, automatisation à prévoir.
- [ ] Adapter Mistral, limites de consommation et suivi tokens.

## P2 — Coach collectif et tuteurs
- [ ] IA écrite sur écran partagé, discussion orale hors captation.
- [ ] Animateur tournant et validation de synthèse.
- [ ] Console tuteur : synthèses, consignes, préparation revues.
- [ ] Reproduire premier cycle 2027 et quatre jalons ; calendrier paramétrable.
- [ ] Journalisation et demandes d'extraits ciblés avec procédure approuvée.

## P3 — Coordination, preuves et pilote
- [ ] Tableau de bord transversal sans dialogues bruts.
- [ ] Ressources partagées et programme de gestion de projet.
- [ ] Portfolios sélectifs, bilans individuels, grilles formatives.
- [ ] Évaluation pilote, mesures coûts/latence, sécurisation.
- [ ] Accord DPO/DSI, information étudiants, exploitation institutionnelle.

## Modèle de ticket
`ID / Besoin / Décision de référence / Définition de terminé / Données de test fictives / Tests négatifs / Dépendances / Documents à modifier / Responsable / Statut`.
