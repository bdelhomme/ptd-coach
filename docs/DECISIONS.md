# Registre des décisions

**Convention :** `VALIDÉ` = explicitement choisi au cours du cadrage ; `PROPOSÉ` = recommandation non arbitrée ; `OUVERT` = doit être décidé. La date est celle de la mise en registre, pas forcément celle du dialogue initial.

| ID | Statut | Décision / position | Motif | Conséquence |
|---|---|---|---|---|
| D-001 | VALIDÉ | Finalité prioritaire : développement **individuel** des compétences de management de projet | Ne pas réduire l'outil à un tableau de bord | Parcours individuels complets |
| D-002 | VALIDÉ | Un espace collectif par équipe, tous les membres impliqués dans les différentes parties | Éviter les silos artificiels | Mémoire et décisions collectives |
| D-003 | VALIDÉ | Coach collectif : étudiants discutent **oralement**, IA **par écrit** sur écran partagé | Préserver l'interaction humaine | Pas d'enregistrement audio requis |
| D-004 | VALIDÉ | Fonctionnement collectif hybride : un animateur conduit, tous participent | Rotation des rôles, inclusion | Animateur ≠ chef de projet nécessairement |
| D-005 | VALIDÉ | Coaching collectif guidé sur temps PTD et libre entre séances | Cadence + autonomie | Scénarios contextuels |
| D-006 | VALIDÉ | Chaque équipe a un encadrant-coach humain qui peut orienter l'IA | Rôle pédagogique du tuteur | Console tuteur + consignes |
| D-007 | VALIDÉ | Le tuteur consulte synthèses et **extraits ciblés justifiés**, pas l'historique entier | Proportionnalité et confiance | Procédure d'accès encore à préciser |
| D-008 | VALIDÉ | Deux coordinateurs ont une **vue synthétique** de toutes les équipes, peuvent diffuser apports de cours | Pilotage transversal | Pas de vue de détail par défaut |
| D-009 | VALIDÉ | Coach individuel privé : apprendre, s'entraîner, agir, débriefer et sélectionner preuves | Progression individuelle | Séparation stricte des données |
| D-010 | VALIDÉ | Mistral est le fournisseur IA **initial privilégié**, sans dépendance obligatoire | IA française + portabilité | Interface fournisseur abstraite |
| D-011 | VALIDÉ | Prototype personnel puis hébergement et paiement API institutionnels visés | Démontrer avant déploiement | Déploiement portable ; validation DSI/DPO |
| D-012 | VALIDÉ | Pas de notation institutionnelle automatique | Responsabilité humaine et validité | Évaluation formative seulement |
| D-013 | VALIDÉ | Les 17 matinées / quatre cycles du calendrier 2027 sont la base du parcours, **sous réserve de validation** | Alignement au PTD | Ne pas inventer 24 séances |
| D-014 | PROPOSÉ | Dix puis onze compétences candidates (version 0.3) | Alignement syllabus/grilles/IPMA/CDIO | Validation encadrants requise |
| D-015 | PROPOSÉ | Pile Next.js + FastAPI + PostgreSQL, conteneurs Docker | Portabilité, accessibilité | Avis DSI requis |
| D-016 | PROPOSÉ | Deux objectifs individuels actifs par étudiant | Limiter la charge cognitive | Tester en pilote |
| D-017 | PROPOSÉ | Coaching collectif ~10–15 min ; bilans individuels ponctuels | Ne pas concurrencer tutorat humain | Affiner avec calendrier réel |
| D-018 | PROPOSÉ | Dépôt Git privé, docs Markdown, AGENTS.md et ADR | Passation multi-IA | Premier dépôt local prêt |
| D-019 | PROPOSÉ | Prototype A2 local en Python standard, SQLite et interface HTML/CSS/JS, comptes fictifs et coach simulé | Éprouver le parcours et ses frontières de données sans dépendance externe | Mise en œuvre de démonstration décrite par ADR-0005 ; ne remplace pas D-015 ni l'avis DSI |
| D-020 | VALIDÉ | Définir, compétence par compétence, la progression visée et la posture du coach avant de poursuivre l'ajout d'exercices | Le porteur remet en question la pertinence pédagogique du premier parcours et confirme la nécessité de ce cadrage | Priorité au ticket 003 et aux fiches de coaching ; exercices existants considérés comme expérimentaux |
| D-021 | VALIDÉ | Accompagner sans faire à la place ; donner aussi des explications et des ressources pour aider à comprendre et agir | Le porteur confirme le principe « aider, sans faire » et la nécessité de ressources | Expliciter les formes et limites d'aide ; l'étudiant garde les choix, actions et conclusions ; modalités détaillées proposées dans COACHING_FRAMEWORK.md |
| D-022 | VALIDÉ | Aider l'étudiant à se positionner sur les compétences pour choisir où travailler et revoir sa progression | Le porteur propose cette fonction puis confirme son intérêt | Concevoir un auto-positionnement formatif et privé ; descripteurs, questions, échelles et modalités restent à discuter, sans notation automatique |
| D-023 | VALIDÉ | Maintenir dans le dépôt privé la mémoire des évolutions significatives de réflexion, afin de permettre la reprise par toute IA | Demande explicite du porteur le 2026-11-06 | Journal de réflexion, décisions, état et passation actualisés lorsque pertinent ; publication GitHub vérifiée |
| D-024 | PROPOSÉ | Établir un cadre global sourcé du management de projet et une matrice d'alignement avec les situations PTD avant de détailler les fiches | Le porteur demande des livres/travaux et questionne l'atomisation autour d'A2 | Corpus préparatoire vérifié sur sources primaires ; choix des références, correspondances et périmètre encore à discuter ; aucun référentiel adopté |
| D-025 | VALIDÉ | Intégrer les lots V0.6 puis V0.7 pour revue sur branche dédiée et PR ; différer le développement du nouveau coach Mistral à une deuxième étape | Demande explicite du porteur le 2026-11-09 | Préserver l'historique et le candidat V0.3, dédupliquer les fichiers, intégrer l'outillage expérimental sans appel IA ni raccordement applicatif ; les propositions pédagogiques des lots ne sont pas validées par leur import |
| D-026 | VALIDÉ | Lancer l'étape 2 : premier coach conversationnel réel via API Mistral, modèle initial mistral-small-latest configurable, conversation souple, ressources, tokens, séparation privée/collective et interface locale fictive | Nouvelle demande explicite du porteur le 2026-11-09, après D-025 | Autorise l'implémentation et les essais synthétiques, sur nouvelle branche et PR ; A2/simulateur et candidat V0.3 préservés ; ne vaut pas validation scientifique/institutionnelle ou autorisation de données réelles |

Pour D-020 à D-023, **VALIDÉ désigne un accord de conception du porteur dans les
échanges du 2026-11-06**. Il ne vaut pas validation du référentiel par l'école,
consensus des encadrants, validation scientifique, accord DSI/DPO ou approbation
de tous les exemples et modalités proposés. Voir [le journal de réflexion](REFLECTION_LOG.md).

D-025 autorise le travail d'intégration et en fixe les limites ; ce n'est pas
une adoption pédagogique ou institutionnelle de V0.6/V0.7. Les décisions
D-001 à D-024 sont conservées sans modification de statut.

D-026 succède explicitement au report de D-025, qui reste dans l'historique.
Il autorise le développement demandé et les appels de recette fictifs avec la
clé locale configurée par le porteur, sans modifier les décisions pédagogiques.

## Principe de mise à jour
Pour toute modification de décision VALIDÉE : renseigner une nouvelle ligne citant l'ancienne et le motif ; ne jamais réécrire silencieusement l'historique. Enregistrer les décisions techniques dans `docs/adr/`.
