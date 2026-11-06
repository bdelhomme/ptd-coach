# ADR-0005 — Prototype local du parcours A2

Statut : **PROVISOIRE, limité à la démonstration fictive, non validé DSI** · 2026-11-06.

## Exigence

Suite à la demande de poursuivre le développement, réaliser le ticket 001 :
parcours individuel A2 exécutable, fournisseur simulé et tests d'isolation.
Références : F-01/F-03/F-04/F-09/F-12/F-13/F-14, D-001/D-009/D-010/D-012.

## Choix de prototype

Utiliser Python standard pour le serveur HTTP local et le domaine, SQLite pour
la persistance locale et HTML/CSS/JavaScript sans dépendance pour l'interface.
Ce socle est exécutable avec les outils disponibles ; il ne remplace pas
l'arbitrage Next.js/FastAPI/PostgreSQL/conteneurs proposé dans D-015.
Les formats pédagogiques existants restent inchangés et versionnés.

Le serveur écoute uniquement sur la boucle locale. Les identités sélectionnables
sont toutes fictives ; ce sélecteur n'est pas une authentification institutionnelle.
Un cookie de session opaque, le contrôle d'origine, une protection CSRF et des
requêtes SQL filtrées par propriétaire permettent de tester les règles métier
dans ce périmètre. Le choix libre d'un compte de démo n'offre aucune garantie
de confidentialité entre personnes ayant accès à cette même démo.

Les textes du coach sont déterministes et portent explicitement le statut de
simulation. Les critères de feedback sont des propositions à relire par un
encadrant. Pas de note, de niveau de compétence, d'appel Mistral ou de transmission
à un service externe.

## Garde-fous et vérification

Transitions autorisées par le backend, version optimiste et clés d'idempotence ;
validation des contrats ; transaction annulée si fournisseur invalide ; partage
explicite d'un texte sélectionné vers le tuteur de l'équipe, révocable ; journal
d'événements sans contenu conversationnel ; exports limités au propriétaire.
Tests de persistance, accès interutilisateurs et rôles, contexte du fournisseur,
injection, partage/révocation, validation et chemins HTTP.

## Limites et migration

Pas de déploiement réseau, données réelles, SSO, Docker, PostgreSQL, coach collectif,
console institutionnelle ou validation scientifique. Les sessions sont en mémoire
et expirent après huit heures ; les données locales persistent après redémarrage.
Séparer le domaine, la persistance, le fournisseur et l'interface facilitera leur
remplacement après avis DSI. Aucun principe pédagogique validé n'est modifié.
