# Reprendre PTD Coach

La bibliothèque fait l’objet d’un [chantier ciblé](PTD_BIBLIOTHEQUE_PARCOURS.md).
La reprise du coach porte sur [l’essai Albert API](PTD_ALBERT_API.md).
Le porteur envisage d’observer les situations qui coincent et
les pratiques d’IA déjà présentes, notamment après un cours sur la
contextualisation des demandes et l’examen critique des réponses.

- Lire [AGENTS.md](../AGENTS.md) et [l’état du projet](PROJECT_STATUS.md).
- La branche `feat/ptd-v2-workbench` est publiée dans la
  [PR #17](https://github.com/bdelhomme/ptd-coach/pull/17), basée sur la
  branche de la PR #16.
- [Guide V2](PTD_V2.md), [place dans le dispositif](PTD_DISPOSITIF_PEDAGOGIQUE.md)
  et [pratique réflexive](PTD_PRATIQUE_REFLEXIVE.md). Les objectifs et
  propositions pédagogiques, notamment le débrief individuel et sa fréquence,
  restent à discuter et à éprouver. Le candidat V0.3 sert à concevoir la recette.
- Les [essais fictifs](../pedagogy/evaluations/ptd-v2-demo/README.md) conservent
  les protocoles et réponses exactes publiables. Le contexte du semestre
  explicite la différence entre un rendu école et un rendu commanditaire.
  La recette signale encore des propositions que le modèle reprend comme des
  actes réalisés. Les nouvelles trajectoires dérivées de thèmes de missions
  restent à jouer.

## Reproduire la démo GLM en high

Depuis le dépôt, avec une clé Mistral configurée dans `.env` local :

```sh
CHAT_PROVIDER=mistral MISTRAL_MODEL=zai-glm-5-3-flash \
  MISTRAL_REASONING_EFFORT=high CHAT_MAX_TOKENS=2000 \
  python3 -m ptd_coach --port 8798 --data-dir local-data/essai-v2-glm-high
```

Ouvrir [le coach](http://127.0.0.1:8798/coach) avec un compte fictif. Le
démarrage standard de la V2 utilise GLM Flash en `low`. La démo `high`
dispose d’un dossier de données distinct.

Le [fil d’essai individuel en high](../pedagogy/evaluations/ptd-v2-demo/essai-individuel-glm-high/README.md)
est disponible en Markdown et en JSON avec ses métadonnées. Lire la note
associée pour retrouver les points à examiner dans le verbatim. Les copies
SQLite de la démo sont dans la sauvegarde locale et servent à restaurer son
état sur le Mac.
