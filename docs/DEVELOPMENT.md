# Environnement de développement — socle documentaire

Exigence : publier et reprendre le dépôt privé en conservant l'historique.
Références : D-010, D-011, D-018 et ADR-0001 (portabilité).
D-015 et le choix de la pile applicative restent **PROPOSÉS** ; cet outillage
ne décide ni l'hébergement, ni le framework, ni la base de données.

## Installation locale

Prérequis : Git, Python 3 avec `venv` et Make. Le socle utilise uniquement la
bibliothèque standard Python (compatible Python 3.9 et suivants ; CI en 3.12).
Aucune clé API, aucun paquet Python/JS et aucun service externe ne sont requis.

```sh
make bootstrap
make verify
```

`bootstrap` crée `.venv/` et copie `.env.example` vers `.env` seulement si ce
dernier n'existe pas. Ces deux chemins sont exclus de Git. La configuration
initiale est `APP_ENV=development`, `AI_PROVIDER=mock` ; elle ne lance pas
d'application et ne constitue pas encore un fournisseur simulé implémenté.

## Contribution

Lire `AGENTS.md` et les documents indiqués dans son ordre de lecture.
Créer une branche dédiée, puis documenter l'exigence et les décisions concernées.
Après ajout de nouveaux fichiers, les indexer pour qu'ils soient vérifiés :

```sh
git add CHEMINS_EXPLICITES
make verify
git diff --cached --check
```

`make check` contrôle les chemins indispensables, la syntaxe JSON, les cibles
des liens Markdown locaux simples et les fichiers suivis à exclure (environnement,
données locales, originaux DOCX, clés). Il recherche quelques formats connus de
jetons sans afficher leur valeur. Ce contrôle porte sur l'arbre de travail des
fichiers indexés ; il n'est ni un audit exhaustif des secrets, ni un examen
des données personnelles, ni un validateur JSON Schema, ni un test métier.
Les ancres Markdown et les liens externes ne sont pas vérifiés.

`make test` teste le contrôleur avec des fichiers synthétiques, y compris ses
cas de refus. `make verify` exécute les deux commandes. Le workflow
`.github/workflows/repository-checks.yml` les exécute sur push et pull request,
avec autorisation de lecture uniquement et actions épinglées par commit.

## Avant le développement applicatif

Le ticket 001 reste la priorité : spécification du parcours A2, puis simulateur
et tests d'isolation. L'initialisation frontend/backend/DB/conteneurs dépend de
l'arbitrage technique prévu dans `OPEN_QUESTIONS.md` et `ROADMAP.md`.
Les tests applicatifs, l'authentification et le moteur IA n'existent pas encore.
Le référentiel candidat, les scénarios et les décisions pédagogiques sont conservés.
