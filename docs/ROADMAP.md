# Feuille de route priorisée — tâches et livrables

## Tranche c2 — D-030

- [x] Consigner le retour qualitatif du porteur, sans inventer de grille notée.
- [x] Vérifier les sources et relire les exemples avant utilisation.
- [x] Contexte c2 séparé et gelé, sans toucher au moteur ni à c1.
- [x] Comparateur à trois variantes, réservé refusé avant ouverture.
- [x] Exécuter les 54 essais Mistral bornés et préparer leurs preuves/limites pour publication.
- [ ] Revue humaine de c2 ; aucun pilote ni acceptation automatique.

Le rapport c2 suit les résultats réellement obtenus. Les sections suivantes
conservent l’historique c1 et les cadrages antérieurs.

## Première tranche V0.8 — D-029

- [x] Intégrer le cadrage, distinguer principes du porteur et hypothèses.
- [x] Ajouter un contexte séparé, sélection V0.7/V0.8 par nouveau fil.
- [x] Préserver A2, candidat V0.3, corpus historique et permissions backend.
- [x] Préparer 12 scénarios de développement et 12 réservés séparés, avec gel et provenance.
- [ ] Lecture humaine comparative puis évaluation indépendante des 12 réservés.
- [ ] Gouvernance et relecture des ressources avant élargissement du corpus.

Voir [le bilan V0.8](V08_IMPLEMENTATION.md) pour les vérifications réellement
exécutées, les arbitrages et les bornes. Les sections suivantes sont historiques.

## Tranche D-026 — coach local sur données fictives

- [x] Conserver A2 et ajouter conversation/Mistral configurables séparément.
- [x] Historique multi-tours, ressources communes, tokens et export autorisé.
- [x] Interface locale privé/collectif et tests de permissions/concurrence/erreurs.
- [x] Runner V0.7 utilisant le même service ; recette API distincte des tests CI.
- [ ] Faire remplir la grille humaine et relire les défauts pédagogiques observés.
- [ ] Valider pédagogie, DSI/DPO et authentification avant tout pilote réel.

Les mentions de report D-025 ci-dessous sont historiques ; D-026 lance la
première tranche. Voir [le rapport courant](CONVERSATION_COACH_REPORT.md).


## Intégration V0.6/V0.7 — revue documentaire avant nouveau coach

Demande du 2026-11-09 : intégrer les lots dans cet ordre, puis ouvrir une PR.
**Proposition V0.6 soumise à relecture** : noyau, politique, ressources et
protocole dans [le rapport d'intégration](INTEGRATION_V06_V07.md).
Les idées des archives ne deviennent pas des décisions VALIDÉES par leur import.
Le développement du nouveau coach Mistral attend une deuxième étape demandée
par le porteur ; aucun appel distant ni modification du prototype pour ce lot.

- [x] Intégrer V0.6, puis V0.7 sans copier les cas V0.6 dans `inputs/`.
- [x] Conserver les propositions distinctes des décisions et tracer les écarts.
- [x] Ajouter un mode d'emploi des outils de recette hors réseau.
- [ ] Faire relire le noyau, la politique et R01–R03 ; enregistrer les retours.
- [ ] Après nouvelle demande seulement : discuter puis développer l'étape 2,
  [ticket 004](tickets/004-conversation-router.md) et
  [ticket 005](tickets/005-backend-boundaries.md), ADR-0006 proposé.

## Chantier de conception — cadrage du coaching (ticket 003)

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
