# Développement — prototype A2 local

Références : D-001, D-009, D-010, D-011, D-012, D-018 et D-019.
La pile institutionnelle D-015 reste **PROPOSÉE** ; voir
[ADR-0005](adr/0005-local-a2-prototype.md) pour le choix provisoire de démonstration.

## Installer, vérifier et lancer

Prérequis : Git, Python 3 avec `venv`, SQLite de la bibliothèque standard et Make.
Le prototype est compatible Python 3.9 et suivants ; CI configurée en Python 3.12.
Aucun paquet externe, Node, Docker, clé API ou service distant n'est requis.

```sh
make bootstrap
make verify
make run
```

Ouvrir **http://127.0.0.1:8765**. Pour un autre port :

```sh
.venv/bin/python -m ptd_coach --port 8766
```

`bootstrap` crée `.venv/` et copie `.env.example` vers `.env` seulement si ce
dernier n'existe pas. Le programme ne démarre qu'avec `APP_ENV=development`
et `AI_PROVIDER=mock` (valeurs du fichier, surchargées par l'environnement).
Le fournisseur simulé ne facture rien et n'effectue aucun appel réseau externe.
Arrêter le serveur avec Ctrl+C. Le redémarrage conserve les données du parcours,
mais demande de sélectionner à nouveau une identité fictive.

Les restrictions de certains environnements d'exécution peuvent exiger une
autorisation réseau même pour les tests HTTP sur la boucle locale.

## Données et identités de démonstration

Les données résident dans `local-data/a2-demo.sqlite3`, exclu de Git ; elles sont
créées à la première utilisation. Ne pas y saisir de données étudiantes réelles.
Le fichier SQLite est en mode propriétaire uniquement ; il n'est pas chiffré.
Pour repartir de zéro, arrêter le serveur puis déplacer le dossier `local-data/`
vers une sauvegarde locale. Un nouveau dossier sera créé au prochain démarrage.

| Compte | Périmètre de test |
|---|---|
| Étudiant démo A / B | Même équipe fictive, espaces individuels distincts |
| Étudiant démo C | Autre équipe fictive, aucun tuteur affecté dans cette démo |
| Tuteur démo | Seulement les preuves explicitement adressées par A ou B |
| Coordination / administration démo | Aucun accès aux dialogues ou bilans privés |

Le sélecteur permet volontairement de choisir toute identité fictive : il n'est
pas un SSO ni une authentification de production. Les sessions opaques en mémoire
expirent après huit heures. Le serveur n'accepte que `127.0.0.1`, avec vérification
d'hôte, d'origine et du jeton CSRF pour les mutations ; cookies HttpOnly et
SameSite=Strict. Ne pas publier ce serveur ou l'exposer via un tunnel.

## Organisation du code

- `ptd_coach/service.py` : transitions, propriétaires, transactions, idempotence,
  partage, révocation, audit sans contenu et export personnel.
- `ptd_coach/schema.sql` : schéma local versionné (`user_version=1`). Une version
  inconnue est refusée ; les migrations ultérieures restent à développer.
- `ptd_coach/provider.py` : interface fournisseur et simulateur déterministe.
- `ptd_coach/contracts.py` : validation du vocabulaire fini utilisé par les deux
  contrats candidats existants ; aucun `$ref` ni vocabulaire inconnu accepté.
  Ce module n'est pas un validateur généraliste de JSON Schema.
- `ptd_coach/server.py` : adaptateur HTTP local, sessions et fichiers statiques
  limités à une liste explicite ; pas de journaux d'accès conversationnels.
- `web/` : interface native du navigateur, aucun composant tiers ni télémétrie.
- [Ticket 001](tickets/001-a2-local.md) : parcours, routes et périmètre détaillés.

Les commandes humaines contrôlent les transitions. Le modèle n'écrit jamais en
base ; ses propositions de mise à jour et d'état ne sont pas exécutées. Les
requêtes IA contiennent uniquement le cas fictif et les données du cycle autorisé.
Une sortie invalide annule l'opération sans perdre les données déjà enregistrées.
La preuve partagée est un texte séparément sélectionné et confirmé ; la révocation
retire l'accès futur, sans garantie de retrait d'une copie déjà consultée.

## Tests et contribution

```sh
git switch -c feat/nom-de-la-tache
git add CHEMINS_EXPLICITES
make verify
git diff --cached --check
```

Lire `AGENTS.md` avant toute modification et mettre à jour l'état du projet.
`make check` contrôle les fichiers indexés : chemins requis, syntaxe JSON,
cibles des liens Markdown locaux simples, exclusions et quelques formats de jetons
(sans leur valeur). Il ne remplace ni un audit de secrets, ni un contrôle exhaustif
des données personnelles. Les ancres et les liens externes ne sont pas contrôlés.

`make test` exécute 78 tests synthétiques : les 34 A2/documentaires (dix contrôles
documentaires, dix-sept cas domaine/contrats et sept HTTP), douze tests des outils
V0.7, deux de préservation/intégration et 24 de conversation applicative, plus quatre de fidélité du corpus publié et deux de liens verbatim. `make verify` exécute les deux
commandes. Les tests utilisent des bases temporaires distinctes des données de démo.
Le workflow GitHub Actions exécute les mêmes commandes sur push et pull request.
Le prototype et les évolutions de cadrage ont été publiés via la pull request 2 ;
voir PROJECT_STATUS.md pour la trace des contrôles vérifiés.

Les lots V0.6/V0.7 sont proposés pour revue ; les outils s'utilisent séparément,
sans modifier le serveur. Voir [EVALUATION_TOOLS_V07.md](EVALUATION_TOOLS_V07.md).
Leur import ne démarre pas le nouveau coach Mistral (D-025) ; seuls les dry-runs
et tests avec doubles locaux font partie de cette étape.

Vérification navigateur manuelle : parcours complet, reprise après rechargement,
preuve sélectionnée visible côté tuteur et révocation ; effectuer cette recette
à nouveau après changement de l'interface. L'automatisation e2e du navigateur
reste à mettre en place.

## Prochaines étapes

L'interface a été clarifiée après retour utilisateur : voir
[ticket 002](tickets/002-student-journey-clarity.md). Le bouton d'entrée guidée
ouvre une nouvelle séance fictive dans le compte étudiant A. Les autres rôles
et la reprise des séances antérieures restent accessibles à la demande.

Relire les feedbacks des trois cas avec un encadrant ; arbitrer la pile et les
conditions institutionnelles ; migrer vers une authentification et une infrastructure
appropriées. Sont hors de ce prototype : Mistral, budgets facturables, accès collectif,
synthèses validées, accès exceptionnel, SSO, restauration institutionnelle et déploiement.

## Coach conversationnel indépendant — D-026

`make run` démarre aussi `/coach` ; A2 reste simulé. Configuration locale
`CHAT_PROVIDER`, `MISTRAL_MODEL`, `MISTRAL_API_KEY`, limites de tokens/appels.
Aucune dépendance supplémentaire ; voir [le guide Mac](TRY_CONVERSATION_COACH.md)
et [le rapport](CONVERSATION_COACH_REPORT.md) pour la recette et les résultats.
Les nouveaux tests s'ajoutent aux 48 précédents sans appels externes en CI.
