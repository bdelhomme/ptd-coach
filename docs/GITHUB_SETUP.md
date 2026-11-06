# Publier le dépôt Git **privé** sur GitHub

## État actuel — 2026-11-06

Le dépôt [bdelhomme/ptd-coach](https://github.com/bdelhomme/ptd-coach) existe et est
privé. `origin` est configuré, la branche par défaut est `main` et les commits
initiaux ont été conservés. Ne pas recréer le dépôt. Voir PROJECT_STATUS.md pour
les branches synchronisées et les contrôles réellement exécutés.

La protection de `main` a été refusée par l'API avec HTTP 403, l'offre actuelle
exigeant GitHub Pro pour ce dépôt privé. Garder le dépôt privé et passer par des
branches et pull requests. Aucun changement d'offre ou de visibilité n'est présumé.

## Mettre à jour le dépôt existant

Après une évolution significative, actualiser les docs pertinentes selon AGENTS.md,
indexer explicitement les fichiers, puis exécuter `make check` et
`git diff --cached --check`. Pour du code, exécuter également les tests appropriés.
Créer un commit, pousser la branche puis ouvrir une pull request vers `main`.
Vérifier la CI et le résultat de l'intégration avant d'annoncer la synchronisation.
Ne jamais committer des identifiants de connexion, fichiers d'environnement réels
ou données étudiantes ; toute authentification reste extérieure au dépôt.

## Procédure historique du bootstrap — à réutiliser seulement pour une nouvelle copie sans distant

Le bootstrap initial contenait un dépôt `.git` local sans distant. Les options
ci-dessous décrivent sa première publication ; elles ne sont plus à exécuter
pour le dépôt existant. Ne pas ajouter les documents sources institutionnels
avant autorisation.

## Option A — Avec GitHub CLI (recommandée)
1. Installer GitHub CLI sur le Mac : `brew install gh` (Homebrew installé au préalable).
2. Dans le Terminal : `gh auth login` et suivre l'authentification GitHub.
3. Décompresser l'archive reçue puis `cd ptd-coach`.
4. Exécuter : `gh repo create ptd-coach --private --source=. --remote=origin --push`.
5. Vérifier sur github.com que le dépôt est **Private** et que les fichiers y figurent.

## Option B — Depuis l'interface GitHub
1. Aller sur https://github.com/new et créer `ptd-coach` en mode **Private**.
2. **Ne pas** cocher initialisation README, .gitignore ou licence (ils existent déjà ou sont volontairement laissés ouverts).
3. Copier l'URL SSH ou HTTPS du dépôt vide.
4. Dans le dossier extrait :

```bash
git remote add origin URL_DU_DEPOT
git push -u origin main
```

Une authentification GitHub valide est nécessaire. En cas d'échec, ne pas ajouter de clé API ou mot de passe dans l'historique Git.

## Après publication
- Activer la protection de `main` et, lorsqu'il y a plusieurs contributeurs, privilégier les pull requests.
- Définir les autorisations des collaborateurs et les comptes de service avec le minimum de privilèges.
- Vérifier le `.gitignore`, les protections de secrets, et les droits sur les documents originaux.
- Ouvrir un ticket « Tranche A2 » à partir de `docs/ROADMAP.md`.
- Planifier la clarification de la licence/propriété avant ouverture publique.

Aide officielle : https://docs.github.com/en/migrations/importing-source-code/using-the-command-line-to-import-source-code/adding-locally-hosted-code-to-github
