# PTD Coach V0.6 — protocole de validation et de pilote

**Statut : PROPOSÉ.** Ce document est une feuille de recherche-développement, pas une autorisation de traiter des données réelles. Les grilles 2026 tuteur/rapporteur/client restent distinctes de cette évaluation formative et ne sont pas modifiées.

## A. Deux questions à ne jamais confondre

**Q1, qualité du coach (pré-déploiement)** : ses réponses sont-elles justes, pertinentes, proportionnées, sécurisées et conformes au cadre pédagogique ? Peut-on s'en assurer sans données étudiantes ? **Oui :** scénarios synthétiques, double revue humaine et cas négatifs.

**Q2, effet sur les apprentissages (pilote autorisé)** : l'accompagnement améliore-t-il le raisonnement, l'action et l'analyse de l'expérience des étudiants au-delà de leur progression ordinaire ? **Pas déductible** de la qualité des réponses IA : prétest/post-test sans IA et, si possible, comparaison entre groupes.

## B. Phase 0 — recette hors étudiants

Corpus V0.6 : 20 scénarios JSON synthétiques, comprenant 8 cas porteurs d’un veto critique (T13–T20). Tester sur mock, puis éventuellement sur Mistral après sélection technique. Pour chaque scénario, évaluer : adéquation à l'intention, justesse, autonomie, distinction fait/hypothèse, longueur et sécurité. Deux évaluateurs humains sur un échantillon, discussion des désaccords. Toute fuite, note automatique ou validation d'une décision par IA bloque le passage au pilote.

**Indicateurs internes de conception** proposés : au moins 90 % des réponses « adéquates » par jugement humain et **zéro** défaut critique sur le corpus. Ce sont des **seuils de recette proposés**, non des seuils scientifiques, à durcir avec scénarios adversariaux et itérations ; ils ne prouvent pas la sécurité en production.

## C. Phase 1 — utilisateurs volontaires sur données fictives

Test bref du parcours : « comprendre », « m'aider à avancer », « faire le point ». Observer si les testeurs trouvent une information en moins de 2–3 échanges, comprennent le statut du chat individuel privé et ne confondent pas brouillon collectif et décision. Nombre de participants à calibrer ; un essai d'ergonomie ne démontre pas un gain de compétence.

## D. Phase 2 — pilote pédagogique dans le PTD (après autorisation)

### Résultats à observer

| Objet | Mesure possible | Ce qu'elle n'est pas |
|---|---|---|
| Raisonnement en gestion de projet | Cas inédit sans IA, argumentation sur dépendances, risques, choix et justification | Une note produite par LLM |
| Coopération individuelle | Retour sur situation + indices d'actions provenant de traces et/ou d'observations humaines | Inférence depuis un journal de chat |
| Autorégulation | Capacité à choisir un objectif, repérer une occasion d'action et discuter résultat | Nombre d'objectifs créés |
| Qualité du groupe | Revues de processus et retours du tuteur, éventuellement indicateurs descriptifs collectifs | Classement des personnes |
| Acceptabilité | Temps perçu, non-usage, utilité, réticences, confiance, charge et incidents | Efficacité d'apprentissage |

### Design minimal recommandé
1. **Janvier prétest**, réalisé individuellement sans IA sur un cas de management de projet et un cas de coordination ; correction humaine avec rubriques descriptives préétablies.
2. **Pendant le semestre**, permettre des aides souples (pas de quota de conversations ni obligation uniforme), recueillir commentaires sur bénéfices/effets inattendus selon base légale autorisée.
3. **Juin post-test** : cas différents mais de difficulté équivalente, sans IA ; correcteurs aveugles de la condition si possible, contrôle de fidélité inter-juges.
4. **Transfert différé** : courte situation nouvelle ou retour d'expérience ailleurs si faisable ; ne pas substituer cette mesure à un examen de situation réelle.
5. **Groupe de comparaison** si effectifs, organisation et avis éthique/juridique le permettent : assignation **par équipe** pour limiter la contamination dans chaque équipe de sept, tutorat identique ; transparence des limites dues à l'auto-sélection et à la petite taille d'échantillon.

### Grille descriptive de qualité du raisonnement — à expérimenter, non psychométrique

Chaque correcteur relève sur un cas sans IA, par rubriques séparées (non destinées à certifier la compétence de l'étudiant) :
- **Description exacte du problème** : faits et contraintes déterminants identifiés ;
- **Analyse causale/alternative** : hypothèses distinctes des données et alternatives pertinentes ;
- **Choix justifié** : cohérence avec les objectifs, dépendances et parties prenantes ;
- **Contrôle de l'action** : anticipation d'indicateurs/retours et possibilité d'ajuster ;
- **Coopération** : prise en compte des interactions, responsabilités partagées et qualité du travail collectif.

Relever explicitement « non observé / insuffisamment documenté » plutôt que rabattre sur la valeur basse. Les rubriques et seuils ne valent pas échelle validée. Former évaluateurs sur cas d'ancrage avant toute utilisation.

## E. Risques et règles d'arrêt

- Données réelles : aucune avant validation DSI/DPO, authentification forte, analyse de finalité, conservation, droits des personnes et vérification du cadre UE IA applicable **au cas d'usage effectivement retenu**.
- Sensibilité des échanges individuels : ne pas exporter ni partager des récits de tensions nominatives dans les rapports de recherche ; faire valider les voies d'escalade vers tutorat.
- Non-usage : ne pas supposer une faiblesse de motivation ou de compétence.
- Biais : différenciation selon aisance rédactionnelle, handicaps et accès numérique ; vérifier accessibilité iPhone PWA si retenue, sans présumer la conformité.
- Dépendance à l'IA : détecter les réponses apprises mais non comprises et le besoin de ressources à chaque tâche ; enquêter qualitativement.
- Charge enseignant : coût de relecture des ressources, suivi d'incidents, collecte de données proportionnée.

## F. Décisions à obtenir avant le pilote

- Qui relit/approuve les ressources et les réponses test ? Qui arbitre les désaccords entre correcteurs ?
- Quelles données peuvent servir d'indices de contribution individuelle sans transformer le coach en outil de surveillance ?
- Quel rôle des tuteurs dans le recrutement et les observations, et quelle séparation avec la note du PTD ?
- Quelles modalités d'absence de consentement/non-usage sans pression sur l'étudiant ?
- Quelle méthode comparative réalisable compte tenu du nombre réel d'équipes et des contraintes de programme ?

**Ne pas annoncer de preuve causale** sur la base d'un simple pré/post, d'avis favorables ou du nombre de conversations.
