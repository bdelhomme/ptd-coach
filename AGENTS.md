# Consignes communes à tous les développeurs et assistants IA

## Mission
Développer PTD Coach, outil pédagogique visant l'acquisition et l'expérimentation **individuelles** de compétences de management de projet dans des **PTD collectifs**. L'IA soutient l'apprentissage ; elle n'évalue pas institutionnellement et ne se substitue pas à l'encadrant humain.

## Ordre de lecture obligatoire
1. `docs/PROJECT_STATUS.md`
2. `docs/DECISIONS.md` et `docs/OPEN_QUESTIONS.md`
3. `docs/PRODUCT_SPEC.md` et `docs/PEDAGOGY.md`
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

## Procédure pour chaque changement
1. Citer l'exigence et la décision que la tâche concerne.
2. Proposer modification minimale, garde-fous et tests.
3. Implémenter sur une branche dédiée ; laisser en place les formats de données versionnés.
4. Exécuter les tests disponibles ou signaler explicitement leur impossibilité.
5. Renseigner `docs/PROJECT_STATUS.md` et, si arbitrage, `docs/DECISIONS.md` / un ADR.
6. En passation, indiquer fichiers modifiés, tests, risques et prochaine étape.

## Format d'un compte rendu de passation
- Objectif / exigences
- Changement effectué (fichiers)
- Tests exécutés (résultats, commandes)
- Décisions et hypothèses
- Points bloquants / risques
- Suite immédiate

**Le dépôt, non l'historique d'un chatbot, fait autorité.**
