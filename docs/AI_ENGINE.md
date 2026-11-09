# Moteur conversationnel IA — contrat conceptuel

## Mise à jour applicative — étape 2, D-026

Le premier coach Mistral local est désormais développé dans un service séparé
avec historique multi-tours, ressources et mesure des tokens, sans modifier A2
ou le candidat V0.3. La demande du porteur succède au report historique D-025.
Les détails pédagogiques V0.6/V0.7 restent proposés ; aucune validation
institutionnelle n'est déduite du code. Voir [le guide d'essai](TRY_CONVERSATION_COACH.md),
[le rapport de recette](CONVERSATION_COACH_REPORT.md) et
[ADR-0007](adr/0007-local-conversation-mistral.md).
Les mentions de non-implémentation ci-dessous décrivent les cadrages antérieurs.


## V0.6/V0.7 — spécification candidate, aucun raccordement applicatif

La [politique V0.6](PTD_CONVERSATION_POLICY_V06.md) propose sept intentions
combinables ; elles ne sont pas les états du cycle A2 ci-dessous. Le prompt et
le banc de dialogue V0.7 restent isolés dans `pedagogy/` et `scripts/`.
Aucun schéma existant n'est modifié ; la réponse en texte libre du banc n'est
pas une réponse contractuelle du backend. Voir
[ADR-0006 PROPOSÉ](adr/0006-dialogue-evaluation-compatibility.md) et
[le mode d'emploi des outils](EVALUATION_TOOLS_V07.md).
Le chemin API Mistral fourni avec le lot n'est pas le futur coach et n'a pas
été exécuté. D-025 réserve son développement applicatif à une deuxième étape.

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
