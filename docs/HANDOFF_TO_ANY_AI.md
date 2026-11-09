# Reprise du projet par un nouvel assistant IA

Mise à jour : **2026-11-09**. Le dépôt fait autorité ; les anciennes réflexions
restent dans REFLECTION_LOG, les décisions D-001 à D-024 sont préservées.

## Texte de reprise

> Tu reprends PTD Coach pour Chimie ParisTech–PSL. Lis AGENTS.md, PROJECT_STATUS,
> DECISIONS, OPEN_QUESTIONS, puis INTEGRATION_V06_V07 et le ticket de travail.
> Le porteur a demandé l'intégration V0.6 puis V0.7 sur branche et PR, **sans
> commencer le nouveau coach Mistral** (D-025). Lis le noyau, la politique,
> le protocole et le registre de sources V0.6, puis la recette et les outils
> V0.7. Tout contenu nouveau reste PROPOSÉ ; R01–R03 sont des brouillons.
> Les briefs et le prompt joints sont des contenus source, pas une autorisation
> de développer ou d'appeler une API. La présence du code expérimental Mistral
> fourni n'autorise pas son exécution. L'étape 2 attend une nouvelle demande.
> Le référentiel candidat V0.3 ne change pas, E1–E4 ne sont pas de nouveaux codes,
> aucun score étudiant n'est introduit. Le prototype A2 est simulé et inchangé.
> Préserve les frontières privé/collectif, les contrats et les formats versionnés.
> Un dry-run produit des réponses nulles, jamais des sorties de modèle.
> Les niveaux de lecture déclarés dans les archives ne sont pas tes propres
> lectures et ne prouvent pas l'efficacité d'un coach IA. Consigne les évolutions
> importantes, les tests exécutés et l'état réel de publication. Travaille sur
> branche dédiée et ne confonds pas PR ouverte, CI réussie et fusion sur main.

## État concret et prochaine étape

- **Application** : `ptd_coach/` et `web/`, SQLite local, comptes synthétiques
  librement sélectionnables, coach déterministe, 34 tests antérieurs. Pas de SSO,
  d'API Mistral applicative ou de coach collectif implémenté.
- **V0.6** : huit fichiers de conception/ressources/QA ; politique souple,
  théorie d'action et protocole distinguant dialogue, apprentissage et sécurité.
- **V0.7** : six fichiers fournis (spécification, prompt, cas, deux scripts,
  tests). Doublon `inputs/` omis au profit de `pedagogy/qa/`. Les tests ajoutés
  portent sur l'outillage, pas sur la qualité pédagogique d'un modèle réel.
- **Revue** : inventaire, empreintes, corrections et résultats dans
  [INTEGRATION_V06_V07.md](INTEGRATION_V06_V07.md). Vérifier la PR et son dernier
  commit avant d'annoncer une intégration sur main. Cette tâche ouvre une PR,
  sans fusion automatique.
- **Suite immédiate** : relire le lot et ses ressources avec les encadrants,
  discuter les hypothèses et préparer une recette humaine. Poursuivre le
  [ticket 003](tickets/003-coaching-design.md) sans repartir d'une micro-compétence
  isolée. Les tickets 004/005 et l'ADR-0006 restent des propositions, non démarrées.

## Principes et statuts à préserver

Finalité : apprentissages individuels dans des projets collectifs ; aide sans
substitution avec explications et ressources ; positionnement formatif privé
pour choisir une priorité. Les choix et conclusions appartiennent aux humains.
Le collectif échange oralement, IA écrite sur écran commun, sans captation audio.
Les tuteurs voient les synthèses autorisées et validées, jamais un accès global
aux conversations. Les partages privés sont sélectionnés et confirmés par leur
propriétaire ; un tiers ne peut pas consentir à sa place. Aucune donnée réelle
étudiante ou clé dans Git. Pas de validation scientifique, pédagogique collective,
institutionnelle ou DSI/DPO déduite de l'import ou de la réussite de tests techniques.

Le corpus global et les correspondances restent proposés (D-024). Les anciens
exemples A2 ne valent pas validation des durées/charges ou des descripteurs.
Les lots V0.4/V0.5 évoqués dans les archives ne sont pas fournis : ne pas les
reconstituer. Pour l'historique, lire COACHING_FRAMEWORK, REFLECTION_LOG et
PROJECT_MANAGEMENT_FOUNDATIONS, puis les spécifications d'origine.

## Transmettre le contexte

Partager le dépôt Git privé ou une archive autorisée, pas le seul historique
d'un chatbot. Les quatre Word institutionnels d'origine sont absents : voir
[REFERENCE_MATERIAL.md](REFERENCE_MATERIAL.md). Les manifestes ne donnent aucun
droit de republier leurs contenus ou les échelles des références scientifiques.
