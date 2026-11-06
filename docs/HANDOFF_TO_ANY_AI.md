# Reprise du projet par un nouvel assistant IA — texte prêt à copier

> Tu reprends **PTD Coach** pour Chimie ParisTech–PSL. Le dépôt fait autorité.
> Lis `AGENTS.md`, `docs/PROJECT_STATUS.md`, `docs/DECISIONS.md`,
> `docs/OPEN_QUESTIONS.md`, `docs/COACHING_FRAMEWORK.md`, `docs/REFLECTION_LOG.md`,
> puis les spécifications, la pédagogie, la confidentialité, l'architecture et la
> feuille de route. La priorité actuelle est le **ticket 003 : co-concevoir le
> coaching par compétence avant de poursuivre les exercices**. Le porteur a confirmé
> l'aide sans faire à la place, la place des ressources et l'intérêt d'un
> auto-positionnement formatif pour choisir où travailler. Les descripteurs,
> ressources, modalités, échelles et fiches restent à discuter. Le référentiel à
> onze compétences demeure candidat. Un accord du porteur n'est pas une validation
> scientifique ou institutionnelle. Un prototype A2 local existe dans `ptd_coach/`
> et `web/`, avec SQLite, comptes fictifs et coach simulé ; les 34 tests existants
> sont décrits dans `tests/README.md`. Il ne démontre pas la pertinence pédagogique
> des exercices, ne réalise pas encore le positionnement et n'utilise pas Mistral.
> Consulte l'état de publication et les résultats de contrôles dans PROJECT_STATUS ;
> n'annonce aucun test non exécuté. Préserve le privé individuel, les décisions
> pédagogiques et les formats versionnés. Ne manipule aucune donnée étudiante réelle
> sans validation institutionnelle. Commence par identifier l'exigence, les accords
> et les propositions ; fais le travail sur une branche dédiée. Consigne les
> évolutions significatives de réflexion dans les docs même sans code, et termine
> par une passation vérifiable avec fichiers, contrôles, limites et prochaine étape.

## État de référence de la passation — 2026-11-06

- Finalité : progression **individuelle** au sein de projets collectifs réels.
- Coach collectif : échanges humains oraux, IA écrite ; pas de captation audio ajoutée.
- Tuteur : synthèses validées et partages ciblés selon les autorisations prévues ;
  aucun accès global ou implicite aux dialogues privés.
- Posture et ressources : voir D-020/D-021 et le cadre de coaching ; le coach peut
  expliquer et donner un exemple sans produire à la place le raisonnement visé.
- Positionnement : principe confirmé (D-022), mise en œuvre ouverte. Distinguer
  ressenti et éléments disponibles ; l'étudiant confirme sa priorité, sans note.
- Mémoire : D-023 demande la synchronisation des évolutions significatives dans le
  dépôt privé. Le journal conserve les raisons des changements ; le registre en
  fixe les statuts. Ne pas déduire une décision d'un exemple proposé par l'IA.
- Technique : architecture locale provisoire, D-015 toujours proposée, pas de SSO,
  de coach collectif ou de validation DSI/DPO ; ne pas exposer le serveur de démo.
- Suite : discuter d'abord une fiche A2 (ticket 003), puis les dix autres compétences.

## Comment fournir le contexte

Partager le dépôt Git **privé** ou une archive du dépôt, pas une capture de nos échanges. Les quatre fichiers Word d'origine ne sont pas dans ce dépôt ; ils doivent être fournis par un canal autorisé si la tâche exige leur consultation. Leur existence et les éléments exploités sont décrits dans `docs/REFERENCE_MATERIAL.md`.

## Règle de décision

Si un nouveau modèle propose de modifier un principe de confidentialité, la finalité pédagogique, une compétence du référentiel candidat ou la pile technique, il doit proposer un ADR/une note de changement avec ses motifs. **Ne pas présumer l'accord.**
