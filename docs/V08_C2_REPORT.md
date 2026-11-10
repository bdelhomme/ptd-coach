# Candidate 2 — rapport de développement et passation

11 novembre 2026 · D-030 · branche `feat/v08-candidate2`, basée sur #7
(`d01b56a2bba42c375edde422a38f617e84fe65da`). Les PR #4–#7 restent ouvertes au
départ. PR distincte vers #7, aucune fusion automatique.

## Exigences et périmètre

Le porteur transmet sa revue qualitative D03/D09 : **c1 non validée**. Ce retour
ne vaut ni grille notée ni preuve d’apprentissage. C2 vise justesse conceptuelle,
intervention dominante (enseigner/corriger/vérifier/analyser/conclure), vérification
ciblée, feedback et arrêt après reformulation correcte ; pas seulement raccourcir.
Les familles savoir/outils, jugement, incertitude, interaction et réflexivité
restent combinables. Les modalités c2 sont expérimentales, pas une méthode validée.

Aucune nouvelle fonctionnalité, mémoire, note, donnée réelle ou déploiement.
Moteur, schéma, fournisseurs, ressources historiques, interface et anciens fils
restent inchangés. C2 est injectée via le paramètre `context` déjà disponible,
dans les bases isolées du banc d’essai. **Le navigateur conserve V0.7/c1**.
Cette tranche ne prétend pas proposer un nouveau sélecteur c2 dans l’application.

## Sources et exemples avant usage

[Relecture conceptuelle](V08_C2_CONCEPT_REVIEW.md) : sources publiques ciblées PMI,
Microsoft et APM, limites de lecture déclarées, nouveaux exemples fictifs courts.
R04 corrige les confusions livrables/activités/planning et rattachement des
responsabilités, dépendances au-delà de fin-début, jalon/activité, risque/problème.
Aucun manuel ou clause précise non consultée invoqué. La relecture est celle de
l’assistant intégrateur, **pas une approbation indépendante humaine**.

Nouveaux fichiers : `pedagogy/prompts/COACH_SYSTEM_V08_C2.md`,
`pedagogy/resources/R04-concepts-projet-c2.md`, `ptd_coach/chat_context_v08_c2.py`.
R03 originale reste inchangée ; la sélection c1 est réutilisée avec remplacement
versionné R03 → R04 uniquement pour c2. Un rappel conceptuel court dans c2 évite
que sa justesse dépende d’un mot-clé présent au dernier tour.

## Protocole figé

[Gel c2](../pedagogy/qa/V08_C2_FREEZE.json) avant tout appel : contexte, prompt,
fiche, relecture d’exemples, cas de développement, nouveau comparateur et ancien
gel c1. Le gel c1 vérifie aussi son moteur d’origine. **Aucun message ou attendu
réservé n’est lu par l’assistant de conception ni transmis au modèle.** L’exécuteur
c2 n’a pas d’option d’ouverture de la réserve ; il accepte uniquement les chemins
canoniques développement/concepts/non-régression, avant lecture du fichier.
Les anciens tests CI font des contrôles génériques de formats/empreintes du réservé,
sans l’afficher, le faire répondre ou en dériver une consigne.

Comparaison contemporaine des trois contextes ; même fournisseur/configuration,
température 0,2, plafond 700 tokens, pas de streaming/outil/retry. Modèle initial
configurable `mistral-small-latest` ; alias mouvant, révision immuable non garantie.
Ordre des variantes tournant entre les cas sélectionnés et répétitions ; histoires
isolées par cas/variante. Les continuations d’étudiants restent préécrites, les
historiques de réponses divergent. Mesurer une réponse n’établit aucun transfert.

Premier passage prévu : D03/D09 × trois tours × trois variantes = **18 appels**.
Puis, si le passage réussit techniquement, trois sondes conceptuelles de
**développement** (P01–P03, 18 appels comparatifs), garde-fous V0.7 M06–M11 sur c2
(12 appels) et une répétition D03/D09 c2 (6 appels) : **budget total maximal 54**.
Arrêt en cas d’erreur ; pas de dépenses pour « remplir » ce budget. Pas d’essai
réservé. Aucune révision du contexte c2 après gel : les défauts seront conservés.

Les nombres de points d’interrogation sont des indices de ponctuation, pas des
nombres de sollicitations pédagogiques. La grille vierge comporte le nombre de
sollicitations **à compter par le lecteur**, leurs citations et la qualité
conceptuelle. Les observations de développement de l’assistant restent séparées
et ne préremplissent aucun verdict humain.

## Commandes reproductibles

```bash
make verify
.venv/bin/python scripts/compare_conversation_c2.py --provider dry-run --output-dir local-data/c2-dry-new
.venv/bin/python scripts/compare_conversation_c2.py --provider mock --output-dir local-data/c2-mock-new
.venv/bin/python scripts/compare_conversation_c2.py --provider mistral --allow-billable --case D03 --case D09 --max-calls 18 --output-dir local-data/c2-first-new
```

La clé reste dans `.env` ignoré/env serveur ; aucune clé envoyée dans les messages,
exports ou rapports. Chaque passage crée un dossier neuf sans écrasement : JSONL
avec messages système/historiques exacts, mesures, lecture A/B/C, clé séparée,
grille CSV vierge. Pas de copie brute des en-têtes HTTP. Usage réel mesuré par API,
coût monétaire non estimé faute de tarif vérifié. CI sans API payante.

## Vérifications déjà exécutées avant API

Socle : **96 tests réussis**. Lot c2 : **13 tests techniques réussis** : anciennes
empreintes, sélection de la fiche, isolation des histoires/oracles, gel, refus du
réservé avant ouverture, limites payantes, arrêt au premier échec, grille vierge,
permissions HTTP existantes rejouées sous c2. Dry-run complet : **96 lignes sans
réponse**. Mock complet : **96 réponses fixes**, aucune qualité pédagogique testée.

## Résultats API et arbitrages après exécution

Les quatre passages prévus ont été exécutés : **54 réponses réelles, zéro erreur
API, 132 977 tokens** (118 253 entrée, 14 724 sortie), aucun cas réservé. Temps UTC
le 10 novembre 23 h, donc le **11 novembre en heure de Paris**. Même alias demandé
et retourné, aucun plafond augmenté, aucun retry. Les JSONL et messages complets
sont publiés dans [le dossier de revue](../pedagogy/evaluations/v08-c2-comparison/README.md).

Premier passage D03/D09 :

| Variante | Entrée | Sortie | Total tokens | Caractères | Médiane latence | Tronquées |
|---|---:|---:|---:|---:|---:|---:|
| V0.7 | 21 666 | 1 711 | 23 377 | 6 136 | 2 706 ms | 0/6 |
| c1 | 13 891 | 3 755 | 17 646 | 13 139 | 4 492 ms | 3/6 |
| c2 | 11 419 | 1 919 | 13 338 | 6 640 | 2 622 ms | 0/6 |

C2 est plus courte que c1 mais reste plus longue que V0.7 ici. Elle échoue encore
sur des exemples WBS (activités sous des lots), les étiquettes de fonction
apparaissent malgré la consigne et D09-T03 déclenche une nouvelle sollicitation
après reformulation. La répétition c2 reproduit les ambiguïtés WBS. Les sondes
jalon/risque donnent des réponses localement plus pertinentes, avec des nuances
encore nécessaires sur les relations temporelles et l’acceptation.

Les garde-fous révèlent des régressions préoccupantes : M08 propose une cause
probable du harcèlement sans preuve et une réponse de gestion d’incident projet ;
M09 nie un passé absent du fil ; M10 revient à la présentation d’une méthode à
l’équipe ; M11 affirme « le partage est annulé » alors qu’aucun outil ne le permet.
Le backend n’a exécuté aucun partage/action ni traversé les espaces privés. La
qualité du texte constitue un problème distinct des autorisations techniques.

**Conclusion de développement : aucun gain convaincant au regard du critère
complet ; c2 non retenue pour adoption.** Cette conclusion ne remplace pas le
jugement indépendant, et les grilles humaines restent toutes vierges. Le
[comptage des sollicitations](../pedagogy/evaluations/v08-c2-comparison/SOLLICITATIONS_DEVELOPPEMENT.csv)
porte seulement sur les 18 réponses initiales : codage assistant descriptif,
conventions explicites et bornes sur cas ambigus ; pas un compteur de « ? » ni
une note d’étudiant. Voir [les observations détaillées](../pedagogy/evaluations/v08-c2-comparison/OBSERVATIONS.md).

Arbitrage : ne pas brancher c2 dans le navigateur ni modifier le défaut applicatif.
Conserver le gel, les défauts et les résultats. Une future candidate distincte
pourrait éprouver des exemples WBS plus fidèles, une clôture explicite après
reformulation et les réponses sensibles, sur développement seulement. Aucun
nouveau prompt n’est ajouté pour masquer l’échec de la candidate demandée.
Les 54 tentatives épuisent le budget annoncé ; aucune dépense supplémentaire.

Vérification finale : `make verify` réussi : **111 tests**, 181 fichiers suivis
contrôlés ; fidélité des nouveaux corpus et des 54 lignes de grilles vierges,
diff sans erreur. [Journal d’exécution](V08_C2_RUN_LOG.md) pour les commandes
complètes, acteurs, empreintes et contrôles. La CI du dernier commit est suivie
dans la PR. Aucune fusion.

## Reprise autonome

Les nouveaux travaux autorisés sont des vérifications et corrections justifiées
par les résultats, sans nouvelles fonctions ni altération de la réserve. Conserver
les défauts des essais, versionner toute future candidate, ne jamais réécrire un
verbatim. Publier l’état et les limites, ne pas promettre un service autonome actif
après la fin d’une session. Le dépôt conserve la mémoire transmissible ; aucun
contenu de raisonnement interne n’est requis, seulement décisions et justifications
techniques/pédagogiques utiles au repreneur.
