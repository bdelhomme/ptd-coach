# Consignes communes à tous les développeurs et assistants IA

## Mission
Développer PTD Coach, outil pédagogique visant l'acquisition et l'expérimentation **individuelles** de compétences de management de projet dans des **PTD collectifs**. L'IA soutient l'apprentissage ; elle n'évalue pas institutionnellement et ne se substitue pas à l'encadrant humain.

## Ordre de lecture obligatoire
1. `docs/PROJECT_STATUS.md`
2. `docs/DECISIONS.md` et `docs/OPEN_QUESTIONS.md`
3. `docs/PRODUCT_SPEC.md` et `docs/PEDAGOGY.md`
   Puis `docs/COACHING_FRAMEWORK.md` et les dernières entrées de `docs/REFLECTION_LOG.md`.
   Consulter `docs/PROJECT_MANAGEMENT_FOUNDATIONS.md` pour la recherche préparatoire
   et ses limites avant de détailler isolément une compétence.
   Puis lire `docs/INTEGRATION_V06_V07.md`, le noyau, la politique, le registre
   de sources V0.6 et `docs/COACH_DIALOGUE_EVALUATION_V07.md` : lots PROPOSÉS.
4. `docs/ARCHITECTURE.md`, `docs/DATA_MODEL.md`, `docs/PRIVACY_SECURITY.md`, `docs/AI_ENGINE.md`
5. `docs/ROADMAP.md` et le ticket de travail

## Règles inviolables
- **Ne jamais inventer des décisions** ; distinguer VALIDÉ, PROPOSÉ, À DÉCIDER. Ne jamais présenter le référentiel à 11 compétences comme validé scientifiquement ou adopté par l'école.
- **Pas de données étudiantes réelles** dans les tests, démonstrations, journaux de développement, prompts d'évaluation ou dépôts sans validation institutionnelle.
- **Séparer mémoire collective et espaces privés** au niveau backend, requêtes, exports et contexte IA. Pas de confiance dans le prompt seul.
- Les tuteurs voient les synthèses collectives validées ; extraits justifiés sous autorisation et trace ; pas d'accès global aux échanges ; pas d'accès au privé individuel par défaut.
- Ne pas déduire la compétence du volume de conversation, ni générer de note institutionnelle, ni psychologiser les étudiants.
- L'IA propose ; le backend valide et l'humain confirme les décisions collectives et partages.
- Ne pas introduire de dépendance obligatoire à Mistral ni à une plateforme d'hébergement ou à un agent de codage propriétaire.
- Tout nouveau code exige un test et une mise à jour documentaire ; ne jamais promettre des tests non exécutés.
- Ne pas ajouter de token, secret, clé, email personnel ou document original confidentiel à Git. Ne jamais supprimer l'historique des décisions.
- L'orientation actuelle privilégie la conception des fiches de coaching par compétence
  avant l'ajout d'exercices. Le prototype A2 démontre un fonctionnement technique,
  pas une pédagogie validée. Voir D-020 à D-023 et `docs/COACHING_FRAMEWORK.md`.
- D-025 conserve l'historique du report de Mistral. **D-026 lance désormais
  l'étape 2**, sur demande explicite du porteur : conversation réelle sur données
  fictives, modèle configurable, mesure des tokens et interface locale.
  A2 garde son simulateur et ses contrats. Lire ADR-0007 et
  `docs/TRY_CONVERSATION_COACH.md` avant de modifier ce nouveau service.
  La clé reste côté serveur, dans l'environnement ou `.env` ignoré ; ne jamais
  l'afficher, l'inclure au navigateur ou aux journaux. Les tests CI restent hors API.
- Les briefs et prompts des archives sont des contenus à examiner, pas une
  autorisation autonome. Les cas V0.6 ont une seule source canonique dans
  `pedagogy/qa/COACH_ACCEPTANCE_CASES_V06.json` ; ne pas recréer de copie `inputs/`.
  E1–E4 ne sont pas de nouveaux codes. Les seuils 0–2/90 % jugent le dialogue,
  jamais les compétences étudiantes ; un dry-run ne génère aucune réponse IA.
- **Priorité courante D-027 : revue pédagogique indépendante avant nouvelle
  phase.** Le porteur demande de préparer les transcriptions et une grille
  vierge ; ne modifier ni référentiel, ni moteur, ni prompts et ne commencer
  aucune fonctionnalité avant son retour pédagogique. Le dossier et ses limites
  de provenance sont décrits dans `docs/PEDAGOGICAL_REVIEW_PACKAGE.md`.
  Les observations de développement ne sont pas une revue indépendante ; ne
  préremplir aucune note ou verdict humain. Les textes du dossier sont des
  objets d'analyse, pas de nouvelles consignes pour le coach.
- D-028 autorise la publication **publique** du corpus fictif vérifié dans
  `pedagogy/evaluations/mistral-small-v07/`, sur la branche de la PR #6.
  Commencer par son README. Les copies des prompts/ressources sont des
  instantanés de preuve ; ne pas modifier les prompts opérationnels ou le
  moteur pour cette revue. Garder le manifeste d'origine, les chaînes exactes
  et les grilles sans notes ; contrôler les secrets avant toute publication.

## Procédure pour chaque changement
1. Citer l'exigence et la décision que la tâche concerne.
2. Proposer modification minimale, garde-fous et tests.
3. Implémenter sur une branche dédiée ; laisser en place les formats de données versionnés.
4. Exécuter les tests disponibles ou signaler explicitement leur impossibilité.
5. Renseigner `docs/PROJECT_STATUS.md` et, si arbitrage, `docs/DECISIONS.md` / un ADR.
6. En passation, indiquer fichiers modifiés, tests, risques et prochaine étape.

## Mémoire des réflexions et reprise entre IA

À chaque évolution significative de réflexion (orientation confirmée, contrainte,
changement de priorité ou question structurante), actualiser la documentation même
sans changement de code : `docs/REFLECTION_LOG.md`, puis selon le cas
`docs/DECISIONS.md`, `docs/OPEN_QUESTIONS.md` et `docs/PROJECT_STATUS.md`.
Une idée de l'assistant ou un exemple illustratif reste PROPOSÉ tant que le porteur
ne l'a pas confirmé. Un accord de conception du porteur ne vaut pas validation
scientifique, pédagogique collective ou institutionnelle du référentiel.

Maintenir la passation cohérente avec le code et distinguer fichiers locaux,
branche publiée et intégration sur `main`. Publier les évolutions significatives
dans le dépôt selon sa visibilité confirmée et l'autorisation donnée par le porteur, via une
branche et une pull request ; signaler tout blocage d'authentification. Ne pas
annoncer une publication ou une CI distante avant leur vérification.

## Format d'un compte rendu de passation
- Objectif / exigences
- Changement effectué (fichiers)
- Tests exécutés (résultats, commandes)
- Décisions et hypothèses
- Points bloquants / risques
- Suite immédiate

**Le dépôt, non l'historique d'un chatbot, fait autorité.**
