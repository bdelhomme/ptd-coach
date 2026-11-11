# Essais sans plafond de tokens demandé et mémoire de semestre

## Demande et périmètre

Le 11 novembre 2026, le porteur demande de retirer le plafond de tokens
**pendant les tests**, de rechercher un modèle pertinent même si les essais
coûtent davantage, et souligne l'enjeu de mémoire sur le semestre. Ce passage
utilise les seuls cas fictifs de développement TX05 et TX07 ; aucun cas réservé,
aucune donnée étudiante réelle. Les prompts, ressources, référentiel et corpus
historiques restent inchangés.

Le nouveau banc `scripts/compare_large_uncapped.py` omet le champ `max_tokens`
dans les requêtes réelles et configure `mistral-large-4` avec `reasoning_effort`
explicite. Cela ne garantit pas une génération infinie : Mistral peut appliquer
ses propres limites ; le connecteur conserve une limite de réponse de 30 000
caractères et une taille de corps de 2 Mo, ainsi qu'un délai réseau. Le mode
ordinaire de l'application conserve ses réglages. Pas de retry automatique en
cas d'erreur ; 12 appels au maximum par passage. Le fournisseur ne conserve ni
ne retransmet les blocs de raisonnement, ce qui peut affecter la qualité
multitour selon la [documentation Mistral](https://docs.mistral.ai/inference/conversations/reasoning).

## Essais réellement exécutés

- Passage `high` : un premier appel TX05 sans plafond demandé n'a fourni aucun
  résultat après plus de 19 minutes ; interrompu manuellement. Aucune mesure de
  tokens ni facture connue, aucune réponse à évaluer, aucune relance automatique.
- Passage `medium`, sans plafond demandé : six réponses TX05, puis erreur réseau
  sur le premier appel TX07 après le délai configuré ; arrêt sans relance. La
  cause précise, les tokens et l'éventuelle facturation de l'appel en erreur sont
  inconnus. Les cinq appels suivants du plan n'ont pas été lancés.
- Passage séparé `medium` sur TX07 avec la fiche M03 imposée : deux réponses,
  sans plafond demandé ; il s'agit d'une variante distincte de l'appel c2 en
  erreur, pas d'une répétition automatique de celui-ci.

Au total, huit réponses Large medium sur neuf appels Mistral terminés (dont un
échec réseau), plus l'appel high interrompu. Les huit réponses sont complètes
(`finish_reason=stop`). La simulation et les tests techniques n'effectuent
aucun appel payant. Chaque tour garde le contexte de son propre fil ; les blocs
de raisonnement ne sont pas conservés dans les requêtes suivantes.

## Lecture pédagogique de développement

- **TX05** : les réponses identifient bien la condition posée par le client,
  mais deux comptes rendus disent que les alertes « ne sont pas retenues » :
  le client n'a pas dit cela. Une réponse transforme le souhait de garder la
  date en décision déjà actée. Ce sont des erreurs de statut et d'attribution
  qui peuvent modifier la décision collective.
- **TX07 avec fiche** : la première réponse propose une trame avec des inconnues
  visibles ; elle donne aussi un identifiant comme exemple à discuter, et
  appelle « périmètre » la maquette à rendre : formulation à examiner. Au
  second tour, elle reformule la demande de l'agent en indiquant que le délai
  de recherche reste à discuter, sans fixer de seuil numérique.
- Ces observations concernent seulement huit sorties d'une seule répétition.
  L'effort de raisonnement et le plafond changent en même temps par rapport au
  passage low historique ; on ne peut attribuer une différence à l'un ou l'autre.
  **Aucune amélioration globale ni validation pédagogique ne sont démontrées.**
  La grille humaine reste vierge.

Réponses exactes côte à côte, quatre variantes et huit tours, grilles vierges et
empreintes dans `pedagogy/evaluations/mistral-large4-medium-sans-plafond/`.
Les deux passages indépendants gardent leurs requêtes et sorties telles
qu'enregistrées. Les grilles ne notent ni les personnes ni leurs compétences.

## Coûts indicatifs des huit tours communs

| Variante | Tokens entrée | Tokens sortie | Total | Latence médiane | Estimation |
|---|---:|---:|---:|---:|---:|
| Large 4 low, ancien plafond 700 | 12 043 | 2 051 | 14 094 | 3,48 s | 0,0127 $ |
| Large 4 medium, plafond omis | 12 014 | 5 083 | 17 097 | 6,29 s | 0,0191 $ |

Estimations hors cache, taxes et diagnostics, et **sans l'appel en erreur ni
l'appel interrompu dont les consommations sont inconnues**. Tarifs standard
[publiés par Mistral](https://docs.mistral.ai/inference/pricing) le 11 novembre
2026 : 0,70 $ par million de tokens d'entrée et 2,10 $ par million de tokens
sortie. Les tokens de raisonnement font partie de la sortie. Les différences de
réponses aux premiers tours modifient les historiques des seconds tours ; il ne
s'agit ni de la facture réelle ni d'un test de performance statistique.

## Mémoire sur le semestre

Le fil actuel conserve localement les échanges et retransmet son historique à
Mistral, avec arrêt après 24 échanges ou 60 000 caractères. Un nouveau fil ne
récupère pas les anciens. Il n'existe donc pas encore de mémoire de semestre.
La [proposition de mémoire](MEMOIRE_SEMESTRE_PROPOSITION.md) précise les questions
à trancher : mémoire relisible et corrigeable par l'étudiant, provenance, statut
et suppression, séparation stricte individuel/collectif, consentement et partage,
stockage, fin de semestre, tests de révocation et protection contre les faux
souvenirs. Elle n'est pas implémentée ni validée. Conserver plus de tokens ne
remplace pas cette conception.

## Contrôles

Test unitaire : quand `max_tokens=None`, le paramètre est absent de la requête,
et le réglage `high` est transmis ; tests des réponses structurées et refus des
outils. Deux simulations hors réseau ont été exécutées (plan complet et sélection
TX07). Les tests historiques ont été lancés sans ouvrir le jeu réservé.
