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
| D-027 | VALIDÉ | Préparer une revue pédagogique indépendante du coach à partir des traces V0.7, avec archive lisible et grille humaine vierge ; attendre le retour pédagogique avant toute nouvelle fonctionnalité ou modification du référentiel, moteur ou prompts | Demande explicite du porteur le 2026-11-09 après la première tranche D-026 | Dossier local sans secret ni donnée réelle, transcriptions exactes et observations historiques séparées ; aucune note ni validation pédagogique attribuée automatiquement ; aucune nouvelle requête Mistral pour préparer la revue |
| D-028 | VALIDÉ | Publier le dossier fictif de revue V0.7 directement dans pedagogy/evaluations/mistral-small-v07/ sur la branche de la PR #6, en tenant compte du dépôt désormais public | Demande explicite du porteur le 2026-11-09 ; visibilité PUBLIC vérifiée sur GitHub | Réponses exactes, anciens passages, critères, contexte, tokens, empreintes et grilles vierges consultables ; aucun secret/donnée réelle, aucune modification du moteur ou des prompts ; D-027 reste applicable |

| D-029 | VALIDÉ | Lancer une première V0.8 expérimentale depuis la branche de la PR #6, avec enseignement explicite, vérification formative dosée, correction précise, bienveillance exigeante et adaptation à la nature de l’apprentissage sans routage hard/soft | Nouvelle demande explicite du porteur et archive de cadrage du 2026-11-10, après la revue V0.7 ; succède au gel D-027 pour cette tranche | Conserver candidat V0.3, contexte et corpus V0.7, A2, permissions et fournisseur configurable ; 12 cas de développement et 12 réservés séparés, contexte gelé avant jeu réservé, tests sans API puis comparaison bornée fictive ; aucune mémoire longitudinale automatique, notation, RAG complexe, donnée réelle, déploiement ou fusion automatique ; familles F1–F5, dosage et heuristique restent PROPOSÉS |

| D-030 | VALIDÉ | Préparer c2 après revue qualitative D03/D09 : c1 non validée, concepts professionnels vérifiés, intervention dominante, vérification ciblée, feedback et arrêt après reformulation correcte | Retour explicite du porteur le 2026-11-11 | Nouvelle branche/PR sur #7, contexte c2 séparé, comparaison V0.7/c1/c2 bornée, gel avant API/réservé ; anciennes versions/empreintes conservées, aucun usage des réservés pour conception, aucune nouvelle fonctionnalité/mémoire/notation/donnée réelle/fusion ; autonomie pour corrections et tests justifiés, passation GitHub documentée |

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

D-027 fixait la priorité et le gel des évolutions jusqu'au retour du
porteur. Il ne revient pas sur les appels déjà réalisés ni ne valide les réponses.

## Principe de mise à jour
Pour toute modification de décision VALIDÉE : renseigner une nouvelle ligne citant l'ancienne et le motif ; ne jamais réécrire silencieusement l'historique. Enregistrer les décisions techniques dans `docs/adr/`.

D-029 autorise désormais la tranche V0.8 demandée par le porteur. Elle ne vaut
ni validation pédagogique des réponses, ni adoption institutionnelle. Le cadrage
validé et les modalités expérimentales sont distingués dans
[V08_IMPLEMENTATION.md](V08_IMPLEMENTATION.md). Les versions antérieures restent
des preuves historiques, sans réécriture de leurs décisions.
