# V0.8 expérimentale — tranche minimale et arbitrages

Date : 10 novembre 2026. Décision du porteur D-029 ; **pas de validation
institutionnelle ni d'acceptation pédagogique**. Base vérifiée : branche de la
PR #6, commit `32248cc2202145eb1cfa3a64b58f52221f368137`. Branche dédiée
`feat/v08-adaptive-coach`, PR vers `docs/independent-pedagogical-review`, dans la
chaîne #4 → #5 → #6 encore ouverte au départ. Aucune fusion automatique.

## Cadrage et lecture préalable

L'archive V0.8 complète est lue (cinq fichiers). Ses quatre documents de contenu
sont intégrés **octet pour octet** :

- [Contrat pédagogique](PTD_V08_CONTRAT_PEDAGOGIQUE.md).
- [Matrice des onze compétences candidates](../pedagogy/competencies/V08_MATRICE_APPRENTISSAGES.md).
- [Plan de recette proposé](V08_PLAN_DE_RECETTE.md).
- [Ticket source 006](tickets/006-v08-coach-adaptatif.md).

Le README de livraison reste une pièce de provenance recensée dans le
[manifeste d'import](../assets/PEDAGOGY_IMPORT_V08.json), pas un remplacement du
README courant. Son « sans changement de code » décrit ce paquet ; la nouvelle
demande du porteur autorise explicitement le développement. Le statut source
« À DÉVELOPPER » du ticket est conservé, le présent rapport décrit l'avancement.

Lecture croisée des décisions, du noyau/politique V0.6 et des 26 réponses v1.2
V0.7 avec leurs observations historiques. Points conservés : appropriation sans
IA (M10), prudence face à un passé absent (M09), aucune fausse action (M11) ni
fausse promesse sur le stockage. La revue n'a pas produit de notes humaines.
[Le corpus V0.7](../pedagogy/evaluations/mistral-small-v07/README.md) reste inchangé.

**VALIDÉ par le porteur** : enseignement explicite, vérification formative dosée,
feedback précis et exigeant, adaptation situationnelle, autonomie, espaces séparés,
absence de réduction hard/soft et conservation du candidat V0.3.
**PROPOSÉ / expérimental** : familles F1–F5 combinables, règles de dosage,
sélection des fiches, formulation du contexte et modalités de recette.
**OUVERT** : efficacité pédagogique, ressources approuvées et leurs responsables,
durée des vérifications, conservation et gouvernance institutionnelles.

## Ce qui est implémenté

- [Prompt V0.8 séparé](../pedagogy/prompts/COACH_SYSTEM_EXPERIMENTAL_V08.md) et
  [assembleur dédié](../ptd_coach/chat_context_v08.py), version
  `conversation-v08-experimental-c1`. Le prompt et l'assembleur V0.7 sont conservés.
- Même fournisseur/configuration Mistral, modèle initial `mistral-small-latest`,
  température 0,2, maximum 700 tokens par défaut, sortie non streamée, sans outil
  ni réessai automatique. Le modèle et les bornes restent configurables localement.
- Sélection V0.7/V0.8 à la création du fil, version immuable et visible, reprise
  et exports autorisés. Anciens fils migrés en V0.7, ledger/pending/messages intacts.
  Extension additive de `conversation.v1` et migration SQLite 1 → 2, sans toucher A2.
- V0.8 n'envoie qu'une fiche au plus, par correspondances lexicales sur le message
  **courant autorisé**. Aucun classement des compétences/personnes, recherche dans
  les autres fils ou embedding. Une demande sans correspondance n'envoie aucune
  fiche ; le modèle peut alors expliquer des connaissances générales sans inventer
  de citation vérifiée. Le catalogue R01–R03 entier reste consultable sans IA.
- Empreintes du bundle complet, du système effectivement envoyé et des messages,
  version, fiches, modèles demandé/retourné, tokens et latence par appel. Les
  empreintes seules ne permettent pas de reconstruire un texte absent : les
  recueils fictifs conservent aussi les verbatim.

Les fiches existantes restent en **brouillon**, sans nouvelle approbation ou
reproduction d'ouvrages. Leur enrichissement complet selon le contrat de
métadonnées V0.8 est différé ; pas de fausse mention « relu » ou « validé ».

## Arbitrages testables

1. « Une sollicitation principale » est un repère de charge cognitive : pas de
   quota de points d'interrogation, de rejet automatique ou de relance obligatoire.
   Alternative testable : une explication directe pour l'urgence, une application
   volontaire pour l'apprentissage substantiel, un feedback avant la suite.
2. Vérifier régulièrement ne signifie pas interroger à chaque tour. Respecter le
   refus/l'arrêt ; une réponse erronée appelle d'abord correction et étayage.
3. F1–F5 guident le modèle à chaque tour, sans routage par compétence ou stockage
   d'un profil. La même coordination peut appeler explication, choix ou dialogue.
4. La sélection lexicale de ressources peut manquer une paraphrase ou choisir une
   fiche moins pertinente. Ce défaut est rendu traçable par `resource_ids`, sans
   ajouter de RAG complexe. Si aucun gain, simplifier ou proposer un choix manuel.
5. Pas de mémoire longitudinale automatique : le stockage technique du fil n'est
   ni un bilan de compétences ni une décision collective. Les permissions restent
   SQL/backend ; le modèle n'a toujours aucun outil d'action ou de partage.

## Développement et réserve

[12 cas de développement](../pedagogy/qa/COACH_DEV_CASES_V08.json), **32 tours**,
2 cas par axe de recette, couvrent F1–F5, privé/collectif, débutant/expérimenté,
erreurs, demandes directes, correction, refus et arrêt. Leurs attentes restent
hors du contexte envoyé au modèle.

Le [gel du contexte c1](../pedagogy/qa/V08_CONTEXT_FREEZE.json) précède la création
du jeu réservé : dix fichiers et leurs SHA-256, dont contextes, prompts,
fournisseur, service, ressources et jeu de développement. L'exécuteur refuse
une comparaison si un de ces fichiers a changé. Le porteur a explicitement
autorisé un assistant distinct pour créer les douze réservés, sans lecture du
prompt V0.8 ni du jeu de développement. Les [12 réservés](../pedagogy/qa/COACH_RESERVED_CASES_V08.json) comportent
34 tours ; [leur provenance](../pedagogy/qa/V08_RESERVED_PROVENANCE.json)
consigne les empreintes, la création séparée et ses limites.
Leur contenu et leurs résultats ne servent à aucun ajustement du contexte c1.

La réserve est une séparation de procédure, **pas un secret** dans ce dépôt
public. Les auteurs artificiels peuvent partager des biais ; le style peut
révéler une variante malgré les labels A/B. Une première évaluation externe et,
idéalement, une double lecture restent à organiser. Après exposition au réservé,
une révision exige une nouvelle version et un nouveau jeu indépendant.

## Commandes de comparaison

Depuis la racine du dépôt, après `make bootstrap` :

```bash
make verify
.venv/bin/python scripts/compare_conversation_v08.py --provider dry-run --output-dir local-data/v08-dry
.venv/bin/python scripts/compare_conversation_v08.py --provider mock --output-dir local-data/v08-mock
```

Un dry-run ne génère rien, le mock renvoie un texte fixe, ni l'un ni l'autre ne
mesure la qualité pédagogique. Exemple de comparaison API bornée sur **deux cas
de développement, six tours chacun pour les deux versions, douze appels** :

```bash
.venv/bin/python scripts/compare_conversation_v08.py --provider mistral --allow-billable --case D03 --case D09 --max-calls 12 --output-dir local-data/v08-api-comparison
```

Même instance fournisseur et réglages pour les deux contextes, conversations
isolées, ordre alterné par cas ; pas de retry. Le plafond est vérifié avant le
premier appel. Les erreurs stoppent tout le passage et restent tracées. Un dossier
existant n'est jamais écrasé. La facturation d'un échec réseau peut rester inconnue.
Les sorties comprennent JSONL exact, mesures JSON, lecture A/B, clé séparée et
grille CSV **entièrement vierge**. Lire d'abord `LECTURE_COMPARATIVE.md`, puis la
clé et les paramètres. La grille juge les réponses, jamais les étudiants.

Pour le jeu réservé, l'exécuteur demande en plus `--unlock-reserved` et un budget
explicite suffisant ; ne pas lancer ce passage pour modifier le prompt. Les
conditions d'acceptation et éventuels veto sont à arrêter par les lecteurs humains
**avant** cette première exécution pédagogique. Pas de seuil validé inventé.

## Résultats exécutés et limites

Socle avant modification : `make verify`, **78 tests réussis**. Premier lot V0.8 :
**12 tests ciblés réussis**, incluant permissions HTTP en V0.8, migration/pending,
versions immuables, contexte exact, isolation et oracles non transmis.
Vérification complète intermédiaire : `make verify`, **92 tests réussis**, contrôle
sur 138 fichiers suivis, puis `git diff --cached --check` réussi. Les contrôles de
provenance/publication ajoutés ensuite sont inclus dans la vérification finale.
Aucune API dans ces tests. Dry-run complet : **64 lignes sans réponse** ; mock
complet : **64 réponses fixes**, 12 cas et 32 tours par variante.
La suite V0.7 entière est rejouée avec un fournisseur de test sous contexte V0.8 ;
cela vérifie le passage technique, pas le respect pédagogique des garde-fous
M06–M11 par Mistral V0.8. Aucun passage API complet de non-régression n’est revendiqué.
Aucune requête ni réponse Mistral sur le jeu réservé ; seuls ses formats, comptes
et empreintes sont contrôlés automatiquement, sans afficher ses attentes.

Dépendances vérifiées : Python **3.9.6** local, SQLite et bibliothèque standard,
aucun paquet supplémentaire. Compilation Python réussie avec
`PYTHONPYCACHEPREFIX=local-data/pycache` : la première tentative d’écriture du
cache macOS hors workspace était refusée, puis corrigée par ce répertoire local.
Recette navigateur sur `http://127.0.0.1:8767/coach` : choix V0.7/V0.8, création
de deux fils privés fictifs, affichage des versions, reprise du fil V0.8 et clé
configurée vérifiés ; **aucun appel payant supplémentaire** depuis le navigateur.

### Passage réel du 10 novembre — développement seulement

[Corpus exact, mesures et grille vierge](../pedagogy/evaluations/v08-c1-comparison/README.md) :
D03 et D09, trois tours chacun, deux versions, **12 réponses**, aucune erreur API.
Même fournisseur et paramètres, modèle demandé et retourné `mistral-small-latest`.

| Variante | Entrée | Sortie | Total tokens | Médiane latence | Réponses tronquées |
|---|---:|---:|---:|---:|---:|
| V0.7 | 21 383 | 1 566 | 22 949 | 2 295 ms | 0/6 |
| V0.8 c1 | 13 479 | 3 271 | 16 750 | 3 896,5 ms | 1/6 |

Total du passage : **39 699 tokens**. Les deux scénarios ne représentent pas la
batterie complète. L'entrée baisse, mais la sortie double et la latence augmente
sur cet échantillon. D03-T01 V0.8 atteint le plafond 700 ; D09-T01 cumule plusieurs
sollicitations et les relances persistent ensuite. Ce comportement contredit
l'objectif de dosage, sans justifier un verdict automatique global. La distinction
livrable/activité (WBS) et les définitions restrictives de dépendance dans les deux
variantes sont aussi à relire. Les erreurs/troncatures restent exactes dans le
corpus ; **aucune retouche du contexte gelé c1** à partir de ces sorties.

**Arbitrage** : livrer la candidate expérimentale sélectionnable pour l'essai du
porteur, conserver V0.7 accessible, ne pas annoncer de gain pédagogique démontré.
La future alternative testable est une consigne/structure plus courte sur le jeu
de développement et une seule vérification pertinente ; cela ferait une autre
candidate, à discuter après votre retour. Ne pas augmenter le plafond de sortie
pour masquer le sur-guidage ni optimiser sur les scénarios réservés.

Les observations de développement sont séparées de la grille humaine. Toutes
les cases de jugement restent vides. Les systèmes exacts et les empreintes des
messages sont vérifiés contre les JSONL. Les huit fichiers de ce nouveau corpus
sont préparés pour publication publique avec contrôles de secrets et de fidélité.

Les comparaisons réelles doivent être contemporaines : ne pas traiter les anciennes
réponses du 9 novembre comme un contrôle identique du modèle d'aujourd'hui.
`mistral-small-latest` est un alias ; même nom retourné ne prouve pas une révision
immuable. Les historiques divergent après les réponses des deux contextes : les
messages étudiants sont identiques, les réponses antérieures ne le sont pas.
L'effet testé combine consignes et sélection de ressources, sans attribution
causale à une seule règle. Petit effectif, une répétition, aucune preuve de
transfert, d'apprentissage ou de sûreté absolue du modèle. Tokens et latence
restent des mesures techniques ; pas de tarif monétaire vérifié, donc aucun coût
en euros inventé. Une facture éventuelle fait autorité sur la dépense.

## Essai personnel et suite

[Guide Mac et choix de version](TRY_CONVERSATION_COACH.md). Données fictives
uniquement, comptes de démonstration librement sélectionnables ; pas de SSO ni
confidentialité réelle entre personnes partageant ce Mac. Aucune mémoire
longitudinale, scoring, partage nouveau ou déploiement institutionnel.

Prochaine décision : retour personnel du porteur et lecture comparative humaine,
puis évaluation réservée indépendante. Ne pas confondre une PR ouverte ou une CI
verte avec l'acceptation pédagogique de la V0.8. Ne fusionner aucune PR automatiquement.

## Vérification finale avant publication

`make verify` réussi : **146 fichiers suivis contrôlés, 96 tests réussis**,
API payante exclue. `git diff --cached --check` réussi. Tests supplémentaires :
import exact des quatre documents, gel antérieur à la création réservée, refus
après modification d’un contexte, fidélité des douze réponses/contextes/empreintes,
grille non notée et absence de confusion entre versions. Aucun conflit Git
rencontré ; la PR dédiée conserve les dépendances et ne sera pas fusionnée.

## Publication vérifiée

[PR #7](https://github.com/bdelhomme/ptd-coach/pull/7), ouverte vers la branche
de #6, sans conflit déclaré et sans auto-merge. Commit code/corpus `62b2ad4` :
CI réussie sur [pull_request](https://github.com/bdelhomme/ptd-coach/actions/runs/42786533789)
et [push](https://github.com/bdelhomme/ptd-coach/actions/runs/42786429965).
Les huit fichiers du corpus comparatif sont lisibles sans authentification, avec
identité SHA-256 des octets publics/locaux vérifiée. La clé locale exacte est
absente de tous les fichiers suivis ; contrôles de formats courants de secrets,
coordonnées et chemins locaux sans signal dans les changements. Cela ne constitue
pas un audit exhaustif. Les 42 fichiers historiques contrôlés (dont candidat,
V0.7, ressources, contrats et A2) et lignes de décisions D-001 à D-028 sont préservés.

Le connecteur GitHub permet la lecture mais refuse la création de PR (403,
`Resource not accessible by integration`) ; création réussie avec GitHub CLI déjà
autorisé, sans nouveau secret ni changement de permissions du dépôt.
Cette dernière mise à jour documentaire consigne les contrôles du commit
applicatif ; les contrôles de son propre commit sont visibles dans la PR.
Aucune fusion ni modification de la visibilité du dépôt n’a été effectuée.
