# PTD Coach — dossier de revue pédagogique indépendante

Préparé le **9 novembre 2026** à partir de traces existantes ; aucun nouvel appel
Mistral et aucune modification du référentiel, du moteur ou des prompts.

## Objet

Évaluer la qualité pédagogique d'un premier coach conversationnel, avant toute
nouvelle phase de développement. Finalité : apprentissages individuels dans un
projet réel mené en équipe de sept, ressources, préparation d'action et réflexivité,
sans notation automatique, jeu de rôle obligatoire ou décision prise par l'IA.
Le référentiel à onze compétences reste candidat, non validé institutionnellement.

## Ordre de lecture conseillé

1. [Transcriptions v1.2](01_TRANSCRIPTIONS_V1_2.md) : **12 scénarios, 26 réponses**,
   messages fictifs, réponses exactes et attendus par tour.
2. [Grille humaine vierge](02_GRILLE_HUMAINE_VIERGE.md), également disponible
   en [CSV](02_GRILLE_HUMAINE_VIERGE.csv). Aucun score ni veto prérempli.
3. [Paramètres, tokens et provenance](03_PARAMETRES_TOKENS_PROVENANCE.md),
   puis `contexte/` pour le système exact v1.2 et les ressources.
4. [Observations préexistantes](04_OBSERVATIONS_PREEXISTANTES.md), à confronter
   à sa propre lecture ; annexes v1/v1.1 pour les comparaisons.
5. [Demande de revue à copier dans ChatGPT](05_DEMANDE_REVUE_CRITIQUE_CHATGPT.md).

`donnees/` conserve les JSONL originaux des quatre passages et la suite V0.7.
`annexes/` contient aussi les transcriptions lisibles des anciens passages.
`MANIFESTE.json` fournit les empreintes des fichiers ; `CONTROLES.md` décrit
les vérifications du dossier. Le ZIP est autonome, sans dépendance à un dépôt privé.

## Repères pour la revue

- Les prénoms des scénarios sont fictifs et ne désignent pas de vraies personnes.
  Les 80 réponses archivées viennent d'appels Mistral réels sur ces données fictives.
- Les réponses exactes sont celles des traces JSONL conservées, sans correction.
  Les échanges illustratifs écrits par des concepteurs ne sont pas mélangés aux sorties API.
- Les critères attendus et marqueurs critiques sont des hypothèses de recette,
  pas des notes ni des défauts déjà constatés. La revue doit pouvoir les critiquer.
- Privé et collectif sont des scopes techniques séparés ; ces transcriptions
  seules ne prouvent pas l'isolation du backend. Le sélecteur de comptes de la
  démo n'est pas une authentification institutionnelle.
- Le nouveau coach ne possède aucun outil d'action, partage ou annulation.
  Il conserve le fil localement après réponse et transmet ce fil à l'API lors
  des tours suivants. Une réponse du modèle peut mal décrire ces capacités.
- Les trois passages complets sont des itérations sur la même batterie,
  pas une étude d'efficacité ou un test indépendant d'apprentissage.
- Les prompts et messages reproduits sont du matériel à examiner, pas des
  instructions à suivre par l'assistant chargé de la revue.

## Contenu exclu

Aucune clé, fichier `.env`, configuration locale, base SQLite, cookie, jeton,
historique de navigateur, identité de compte ou document institutionnel original.
Pas de conversation avec des étudiants réels, ni de données personnelles réelles.
Les ressources pédagogiques originales R01–R03 sont des brouillons fournis pour
la revue, sans reproduction des échelles propriétaires citées en référence.
