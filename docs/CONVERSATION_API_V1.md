# Contrat conversation.v1 — démo locale

## Extension additive V0.8 — D-029

`POST /api/coach/conversations` accepte le champ facultatif `coach_version`
(`v07` ou `v08`). L’absence garde `v07` pour les appelants existants ; l’interface
propose explicitement `v08`. Scope et version du coach sont immuables. Réutiliser
une clé de création avec un autre coach produit 409. Aucun champ de version du
coach n’est accepté lors de l’envoi des messages. Liste, snapshot et export
incluent `coach_version`. Le format `conversation.v1` reste additif.

Config expose `coach_versions`, `prompt_versions` et `default_coach_version`.
Chaque appel conserve version, empreinte du bundle, `system_sha256` du système
réel, `messages_sha256` des messages sérialisés (`ensure_ascii=False, sort_keys=True`),
identifiants des fiches, modèle, tokens et latence. Ces empreintes ne remplacent
pas une archive des textes fictifs pour la recette ; aucun message privé ne
rejoint le corpus commun. Anciennes métadonnées conservées sans réécriture.

Le contrat s'ajoute aux contrats A2 sans les modifier. Référence :
[ADR-0007](adr/0007-local-conversation-mistral.md), D-026.

## Authentification et entrée

Même session fictive, cookie HttpOnly/SameSite, validation Host/Origin et CSRF
que le prototype. Les identités restent sélectionnables, sans sécurité SSO.
Toutes les routes de conversation nécessitent un compte étudiant, y compris
configuration/ressources. Créations/envois nécessitent `Idempotency-Key` UUID.
Les corps sont des objets JSON dont les champs supplémentaires sont refusés.

| Route | Corps / résultat |
|---|---|
| `GET /api/coach/config` | Fournisseur, modèle configuré, présence de clé (booléen), limites, empreinte/version du contexte ; jamais la clé |
| `GET /api/coach/resources` | Trois brouillons communs : id, titre, statut, contenu |
| `GET /api/coach/conversations` | Métadonnées des seuls fils accessibles |
| `POST /api/coach/conversations` | `{scope: individual\|collective, synthetic_confirmed: true}` ; scope fixé, aucun appel IA |
| `GET /api/coach/conversations/{id}` | Snapshot autorisé `conversation.v1` |
| `POST /api/coach/conversations/{id}/messages` | `{message: texte, version: entier}` ; réponse après appel, aucun retry automatique |
| `GET /api/coach/conversations/{id}/export` | Export `ptd-coach-conversation-export.v1` de ce seul fil autorisé |

Le message contient 1–4 000 caractères. Le client ne fournit jamais `role`,
identité, équipe, historique, contexte, modèle, droits ou instruction système.
Le modèle est configuré uniquement côté serveur ; commencer un nouveau fil
pour une comparaison claire après changement de modèle.

## Snapshot

Champs : `format`, `id`, `scope`, `version`, `pending`, `messages`, `invocations`,
`usage`, `proposed_updates` (tableau vide). Messages : rôle utilisateur/assistant,
texte, auteur synthétique et date UTC. Invocations : statut pending/succeeded/
failed, fournisseur, modèles demandé/renvoyé, paramètres, empreinte/version du
contexte, usage, latence et motif d'arrêt. Aucun prompt, clé ou copie du texte
dans les métadonnées d'invocation.

`usage.known_tokens` somme les compteurs API disponibles (entrée/sortie/total),
en incluant les historiques retransmis ; `unmeasured_calls` signale les usages
inconnus, mocks et appels interrompus. Une somme connue de zéro n'est pas une
estimation de coût nul. Pas de conversion en euros ni de barème codé en dur.

## Erreurs et concurrence

Erreurs : `{error: {code, message}}`, jamais corps d'erreur API ou secret.
400 entrée/clé invalide ; 401 session ; 403 rôle/CSRF/origine ; 404 fil absent
ou inaccessible ; 409 version périmée, appel en cours/incertain, limite du fil,
réutilisation incompatible de clé ; 429 concurrence/plafond ; 502 réponse/API
inexploitable ; 503 clé absente ; 504 réseau/timeout. Le code HTTP est une
catégorie locale ; les détails privés du fournisseur ne sont pas exposés.

Rejouer une commande réussie donne le snapshot actuel du fil sans répéter son
effet. Rejouer un échec connu retourne la même erreur. Après une interruption
locale, conserver la même clé ; après une erreur connue, un nouvel envoi manuel
peut créer une nouvelle tentative. Aucun retry en boucle. Un fil resté pending
après arrêt du processus nécessite vérification manuelle ; il n'est pas débloqué
en supposant l'absence de facture. Les autres fils restent utilisables.

## Frontières

Les filtres SQL sont appliqués avant lecture, export ou préparation du contexte.
Aucune route de partage, modification de scope, validation collective, changement
de compétence ou modification de planning. Une réponse textuelle qui prétendrait
effectuer une telle action ne l'effectue pas ; c'est un défaut à signaler dans la
recette V0.7, jamais une preuve de persistance métier.
