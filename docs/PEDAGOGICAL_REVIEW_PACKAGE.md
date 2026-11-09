# Dossier de revue pédagogique indépendante — 2026-11-09

Référence D-027, demande du porteur après D-026. Préparation documentaire,
sans nouvelle fonctionnalité, appel API, notation ni modification du référentiel,
du moteur ou des prompts. La prochaine évolution attend le retour pédagogique.

## Accès public sur GitHub — D-028

Sur demande explicite du porteur, le corpus est désormais versionné dans
[pedagogy/evaluations/mistral-small-v07](../pedagogy/evaluations/mistral-small-v07/README.md)
sur la branche de la PR #6. La visibilité **PUBLIC** du dépôt est vérifiée.
Le README fournit les liens GitHub et bruts vers les transcriptions principales,
le JSONL et le contexte. La PR n'est pas supposée fusionnée sur `main`.

Les 25 fichiers du ZIP vérifié sont copiés **octet pour octet**. Un README et
un manifeste de publication sont ajoutés ; le manifeste d'origine et toutes
ses empreintes sont conservés. Les 27 fichiers rendent la revue autonome sur
GitHub. Les observations restent séparées, les 26 lignes de la grille restent
vierges ; aucun résultat pédagogique n'est déduit de cette publication.

L'outillage documentaire ignore désormais les liens littéraux dans les blocs
verbatim, tout en continuant à rechercher les secrets dans ces blocs. Deux
régressions vérifient ce comportement ; quatre tests du corpus contrôlent les
manifestes, les 160 blocs exacts, les cas/critères/tokens, la grille et le contexte.
Le moteur et les prompts opérationnels n'ont pas changé.

Contrôles locaux exécutés pour cette publication : `make verify` (78 tests
réussis), puis `make check` (124 fichiers suivis) et quatre tests du corpus
rejoués après l'ajout des attributs Git de fidélité. `git diff --cached --check`
réussi ; CRLF et lignes finales des pièces originales conservés explicitement,
sans les normaliser. Les contrôles du dernier commit publié sont suivis dans
la PR #6. La lecture anonyme des liens bruts sera vérifiée après le push.

## Livrable local

`PTD_COACH_REVUE_PEDAGOGIQUE_V07.zip` : **25 fichiers**, **112 298 octets**.
SHA-256 : `25f2edb953ce97c70350887c32f185eb7a1fc1248063439b64310a34d7ee738d`.
Le ZIP et le dossier décompressé sont dans les livrables locaux `outputs/`,
à côté du checkout applicatif. Le ZIP reste hors Git ; son contenu est désormais
versionné dans le corpus public indiqué ci-dessus.
Le porteur dispose du lien de récupération dans la conversation de livraison.

## Contenu

- `00_LIRE_D_ABORD.md` : contexte et ordre de lecture, indépendance et limites.
- `01_TRANSCRIPTIONS_V1_2.md` : 12 scénarios, 26 réponses exactes, messages
  fictifs, attendus, signaux et marqueurs critiques par tour.
- `02_GRILLE_HUMAINE_VIERGE.md` et `.csv` : 26 lignes, aucun score, veto,
  commentaire ou nom de lecteur prérempli.
- `03_PARAMETRES_TOKENS_PROVENANCE.md` : compteurs, modèles/paramètres,
  versions, empreintes et limites de reproductibilité.
- `04_OBSERVATIONS_PREEXISTANTES.md` : M09/M10/M11 et affirmations trompeuses
  des premiers passages, avec citations exactes et distinction fait/hypothèse.
- `05_DEMANDE_REVUE_CRITIQUE_CHATGPT.md` : demande de revue qualitative,
  sans remplir la grille humaine ni développer de nouvelles fonctions.
- `annexes/` : transcriptions lisibles v1, v1.1 et smoke M01.
- `donnees/` : quatre JSONL originaux et suite de scénarios V0.7.
- `contexte/` : prompt source V0.7, systèmes complets v1.2 individuel/collectif,
  politique V0.6, grille V0.7 et brouillons R01–R03.
- `MANIFESTE.json` et `CONTROLES.md` : empreintes et vérifications.

Les observations préexistantes sont séparées et conseillées après une première
lecture des traces pour éviter d'en faire des verdicts d'évaluateur indépendant.
Les noms des scénarios sont fictifs ; aucun compte GitHub, chemin personnel,
clé, cookie, `.env`, base locale ou document institutionnel original n'est inclus.

## Provenance et consommation

Quatre traces déjà livrées dans `recette-conversation/` ont été récupérées,
sans appel au modèle : smoke v1 = 2 réponses/6 257 tokens ; v1 complète =
26/84 860 ; v1.1 = 26/88 004 ; v1.2 = 26/91 945. Total de ces quatre fichiers :
**80 réponses, 271 066 tokens**, hors essais du navigateur.

Dernier passage : 87 949 tokens d'entrée, 3 996 de sortie ; température 0,2,
max 700 tokens par réponse ; modèles demandé/renvoyé `mistral-small-latest`
(alias, révision immuable non fournie par l'API). Contexte :
`conversation-v1.2+v07-proposed`, SHA-256
`c321c72fa966b1d13a0e29f1ac8fcd120daafe3859f02b75477a05682322487a`.
SHA-256 du JSONL v1.2 :
`3e64f913ae685074e52b4be03f14932b334e345b99d14fb05e88d8ae57e85754`.

Les systèmes v1.2 sont reconstruits à l'identique depuis la version conservée,
empreinte vérifiée. Les anciennes empreintes v1/v1.1 ne couvraient pas leurs
compléments applicatifs ; leurs systèmes complets ne sont pas revendiqués comme
archivés. Les JSONL sont les traces disponibles, pas un archivage HTTP brut.
Le texte reproduit est exact au regard des chaînes enregistrées.

## Contrôles réellement exécutés

- 12 cas/26 tours uniques vérifiés pour chaque passage complet, smoke M01 séparé.
- Messages, scopes, attendus/signaux et marqueurs comparés au JSON canonique.
- Quatre JSONL copiés octet pour octet ; 160 blocs étudiant/réponse Markdown
  comparés aux chaînes sources ; aucune correction de sortie.
- Grille CSV : 26 lignes, textes exacts, toutes les cellules de jugement vides.
- Paramètres et sommes de tokens vérifiés ; contextes v1.2 conformes à l'empreinte.
- ZIP sans erreur CRC, 25 entrées relatives sûres, 24 empreintes du manifeste
  vérifiées, cibles des liens locaux vérifiées (hors blocs verbatim).
- Contrôle sans affichage de la clé locale : valeur exacte absente ; formats
  courants de jetons, emails/téléphones et chemins de compte absents.
- Aucun code applicatif, référentiel, ressource ou prompt modifié pour préparer
  cette revue. Les tests applicatifs n'ont pas été rejoués inutilement : le
  contrôle de cette tâche porte sur les livrables et la documentation.

## Suite

Transmettre le ZIP au réviseur choisi par le porteur. Toute analyse IA reste
distincte d'une revue humaine ; la grille doit rester vierge jusqu'à la saisie
des lecteurs. Attendre le retour avant toute nouvelle phase de développement.
Les détails techniques de la première tranche restent dans
[CONVERSATION_COACH_REPORT.md](CONVERSATION_COACH_REPORT.md).

## Synchronisation documentaire

Branche `docs/independent-pedagogical-review` publiée ;
[PR #6](https://github.com/bdelhomme/ptd-coach/pull/6) ouverte, dépendante de #5,
sans changement applicatif ni fusion automatique. Sur le commit `57550d8`,
contrôles GitHub réussis :
[pull_request](https://github.com/bdelhomme/ptd-coach/actions/runs/42666593944)
et [push](https://github.com/bdelhomme/ptd-coach/actions/runs/42666473032).
Les contrôles du dernier suivi documentaire sont visibles dans la PR.
