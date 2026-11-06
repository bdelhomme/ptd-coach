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

## Principe de mise à jour
Pour toute modification de décision VALIDÉE : renseigner une nouvelle ligne citant l'ancienne et le motif ; ne jamais réécrire silencieusement l'historique. Enregistrer les décisions techniques dans `docs/adr/`.
