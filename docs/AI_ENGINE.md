# Moteur conversationnel IA — contrat conceptuel

## Requête au modèle
L'appelant autorisé fournit : `mode` (individual/collective), `activity`, `pedagogical_state`, `competency_ids`, `authorized_context`, `student_message`, `prompt_version` et un identifiant d'appel. Le backend constitue le contexte autorisé ; le modèle ne sélectionne pas les droits.

## Réponse attendue
`message`, `pedagogical_intent`, `suggested_next_state?`, `proposed_updates[]`, `needs_human_support`. Validation du schéma obligatoire. **Aucune écriture directe sur les données métier par le modèle.**

Les schémas candidats sont dans `contracts/json-schemas/` : ils devront être ajustés et couverts par des tests.

## Machine à états (cycle individuel)
`OBJECTIVE_SELECTED -> LEARNING -> PRACTICING -> EXPERIMENT_PLANNED -> AWAITING_EXPERIENCE -> REFLECTING -> REVIEWED -> CLOSED`.

Chaque transition doit être explicitement permise, journalisée et idempotente. Le moteur peut demander un retour en phase antérieure ou une sortie, selon les règles métier. Le temps écoulé seul ne permet pas de déclarer une expérience accomplie.

## Style pédagogique

La prochaine évolution du moteur doit être conçue à partir des fiches de coaching
du [cadre de conception](COACHING_FRAMEWORK.md) et du ticket 003, conformément à
D-020/D-021/D-022. Les points ci-dessous restent des exigences de conception ;
le simulateur actuel ne réalise pas encore ce coaching adaptatif ni le positionnement.

- Aider à expliciter et examiner un choix ; laisser à l'étudiant les décisions,
  actions et conclusions qui constituent l'apprentissage visé.
- Fournir une explication ou une ressource utile lorsque le besoin apparaît,
  sans exiger systématiquement une réponse préalable à des questions.
- Choisir le mode d'aide en fonction du besoin ; ne pas imposer un exercice ou
  un formulaire complet pour toute interaction.
- Pour le futur positionnement, distinguer ressenti et éléments disponibles ;
  proposer une priorité à confirmer plutôt que décider d'un niveau ou d'un objectif.
- Clarifier le besoin puis intervenir par **question principale à la fois**, sauf demande contraire.
- Alterner guidage et explication : ne pas transformer toutes les demandes en interrogatoire.
- Pour les simulations, jouer un interlocuteur fictif et donner feedback sur les interventions *observées dans le chat* ; ne pas inventer des comportements en réunion réelle.
- Relier l'exercice à une expérimentation dans le PTD, puis à un débrief.
- Documenter ce qui est rapporté par l'étudiant et ce qui est confirmé par des pièces, sans confusion.
- Face à une demande de livrable à faire entièrement, privilégier aide à la structuration, critique et méthode, sans interdire toute assistance rédactionnelle légitime.

## Robustesse
- Timeouts, retries bornés avec idempotence, coupure de budget, erreurs de parsing remontées, « mock provider » pour exécution hors réseau.
- Tests d'injection de prompt, fuite de contexte et demandes de notes ou d'informations privées.
- Journal d'appels minimisé : modèle exact, modèle/pricing version, tokens et coût, latence, succès/erreurs ; éviter texte de la conversation dans les logs d'observabilité.

## Portabilité
Il ne suffit pas d'avoir une classe `AIProvider` : documenter les capacités réellement utilisées (sortie structurée, taille de contexte, streaming éventuel, limites, cache, coût, modèle européen, rétention). Une capacité non disponible doit être détectée et traitée, pas simulée silencieusement.
