# ADR-0007 — Premier coach conversationnel local, sans migration d'A2

Statut : **IMPLÉMENTÉ POUR EXPÉRIMENTATION FICTIVE, non validé DSI** · 2026-11-09.
Exigences F-01/F-03/F-04/F-05/F-11/F-12/F-14 ; D-009/D-010/D-012/D-026.

## Choix et compatibilité

La nouvelle demande du porteur lance l'étape 2 différée par D-025. Le prototype
A2 et son simulateur demeurent sur leurs routes, contrats et base d'origine.
Un service de conversation indépendant utilise Python standard, SQLite séparé
et une interface `/coach`. Cette extension du socle provisoire ADR-0005 ne
tranche pas la pile institutionnelle D-015.

L'ADR-0006 reste la proposition historique de compatibilité. Cette première
implémentation choisit un contrat distinct `conversation.v1`, décrit dans
[CONVERSATION_API_V1.md](../CONVERSATION_API_V1.md), plutôt qu'une migration
des états A2. Le dialogue n'a pas de parcours obligatoire ni d'action métier
proposée/exécutée : `proposed_updates` est toujours vide. Les sept intentions
de V0.6 guident le texte via le prompt V0.7, sans classificateur imposé ou
déduction automatique de compétence. L'étudiant choisit son besoin librement.

## Fournisseur et contexte

Interface minimale `complete(messages) -> Completion` : texte, modèle renvoyé,
usage, latence et motif d'arrêt. Mistral réel ou mock explicite. Endpoint HTTPS
fixe, sans outils, sans redirection d'authentification ni retry automatique ;
modèle par défaut `mistral-small-latest`, configurable côté serveur.
La clé est lue depuis l'environnement ou `.env` ignoré, jamais depuis le
navigateur. Les erreurs de service sont nettoyées, sans contenu API brut.

Le prompt V0.7 et les ressources R01–R03 restent inchangés et PROPOSÉS. Un
complément décrit le scope autorisé et l'absence d'outils. Une empreinte SHA-256
du prompt et des ressources, la version du complément, les paramètres et les
modèles demandé/renvoyé sont associés à chaque invocation. Un alias renvoyé
tel quel par l'API n'identifie pas nécessairement une révision immuable.

## Permissions, mémoire et confirmations

Scope fixé à la création : privé = propriétaire seul ; collectif = étudiants
de la même équipe seulement. Tuteur, coordination et admin n'ont pas accès aux
transcriptions ou exports, même collectifs. Aucun index global, récupération de
traces A2 ou copie de privé dans le collectif. Le contexte du modèle contient
uniquement le fil autorisé, jamais les autres fils, même du propriétaire.

L'interface annonce stockage local et transmission API puis exige une
confirmation de données fictives à la création. Cette conservation du fil
conversationnel ne crée pas de mémoire de compétences, de décision, de planning,
de partage ou de synthèse validée. Ces fonctionnalités restent absentes.

## Facturation et concurrence

Réservation persistante de la clé de commande et verrou du fil avant l'appel,
hors transaction réseau. Une réponse connue est rejouée sans nouvel appel ;
une erreur connue est rejouée comme erreur. Un appel interrompu reste marqué
incertain/en attente après redémarrage et n'est jamais relancé automatiquement.
Une nouvelle tentative après erreur connue doit être explicitement initiée.
Les usages manquants/erreurs sont « non mesurés », jamais annoncés gratuits.

Limites : 3 appels simultanés par processus, 24 tours et 60 000 caractères
d'historique par fil, sortie 700 tokens par défaut, 100 réservations d'appel par
base de démo par défaut (y compris échecs). Ces bornes sont techniques et ne
constituent pas une norme pédagogique ou un plafond financier contractuel.

## Conséquences et limites

Tests de permissions, contexte, idempotence, erreurs, HTTP et QA V0.7 via le
service réel avec fournisseur factice ; recette API distincte. Pas de déploiement,
SSO, validation institutionnelle, monitoring externe ou données réelles.
Le texte du LLM reste susceptible de défauts pédagogiques ; il n'est pas rendu
fiable par les seules garanties de permissions. Les grilles restent humaines.
