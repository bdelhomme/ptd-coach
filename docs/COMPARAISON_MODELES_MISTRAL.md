# Comparaison exploratoire de modèles Mistral

Demande du porteur, 11 novembre 2026 : examiner si changer de modèle améliore
l'aide pédagogique, sans déclarer un modèle défaillant sur un seul essai.
Branche issue de `feat/bibliotheque-methodes`, PR #10. Aucune modification des
prompts, moteurs, sélecteurs, fiches, corpus historiques ou référentiel. Jeu
réservé non ouvert. Aucun étudiant réel.

## Protocole

On reprend TX05 (demande de changement) et TX07 (cahier des charges), deux
tours, trois contextes (`c2`, fiche M06/M03 imposée, bibliothèque contextuelle).
Les 12 nouvelles réponses `mistral-medium-3-5` sont comparées aux 12 réponses
`mistral-small-latest` de la PR #10. À chaque paire, message utilisateur, hash
du système et identifiants de ressources sont identiques. Aux seconds tours,
l'historique contient les réponses différentes de chaque modèle : les requêtes
complètes ne sont donc pas identiques. Un seul passage par modèle, ordre fixe,
continuations prédéfinies, température 0,2 et max_tokens 700. Alias Small mobile,
comparaison non aveugle pour la lecture de développement. Ces éléments ne
permettent pas d'estimer fiabilité statistique ni apprentissage des étudiants.

Réponses et requêtes exactes, mesures, empreintes et grille vierge :
`pedagogy/evaluations/comparaison-mistral-medium35/`. Comparaison côte à côte :
`COMPARAISON.md`. La grille est destinée à une revue humaine distincte ; aucun
score étudiant et aucun verdict automatique.

## Constat de développement, à confirmer humainement

- **TX07 avec M03 imposée** : Medium énumère les inconnues plutôt que d'ajouter
  les seuils, délais et champs inventés par Small. Au second tour, sa ligne
  reprend la demande de l'agent sans ajouter le nom de l'emprunteur. C'est un
  indice favorable sur ces deux réponses, pas une preuve générale.
- **TX07 sans fiche** : Medium invente à son tour un budget nul et des critères
  chiffrés (30 à 5 minutes) ; au tour suivant, il ajoute un tri par priorité et
  d'autres champs. Le problème de substitution et d'invention persiste.
- **TX07 sélection contextuelle** : Medium cite M03 et marque un exemple comme
  fictif, mais l'expression « temps réel » ressemble au projet et peut entraîner
  une confusion ; il propose aussi des sources supposées. Au tour suivant, il
  écrit « sans délai de recherche imposé », ce qui mérite relecture : aucun délai
  n'avait été fourni, plutôt qu'une absence d'exigence décidée.
- **TX05** : avec la fiche imposée, Medium examine les impacts sans inventer
  les estimations de « 2–3 jours » et « 1 jour » apparues chez Small. En sélection
  contextuelle, il impose toutefois un faux dilemme (réduire le périmètre,
  risquer la qualité ou reporter) sans établir que ce sont les seules options.
  La sélection reste absente sur les deux tours, pour les deux modèles.

Bilan : **des réponses plus prudentes dans certains cas, mais pas de gain global
convaincant établi**. Le contexte et la ressource comptent aussi ; le modèle
seul n'explique pas tous les résultats. Aucun des deux n'est validé pour un
usage auprès d'étudiants réels.

## Mesures et disponibilité

Medium : 12 réponses, 21 563 tokens (19 300 entrée, 2 263 sortie), aucune
troncature ; médianes par contexte 1 707,5 / 2 965,5 / 1 624 ms. Small : 12
réponses, 24 485 tokens, deux troncatures, médianes 2 164,5 / 2 969 /
2 407,5 ms. Ces mesures sont descriptives, pas des scores de qualité ; elles
incluent des historiques différents. Mistral classe désormais Medium 3.5 parmi
les modèles dépréciés : ne pas en faire un choix durable sans vérifier sa date
de retrait et les conditions d'accès. Le tarif effectif de ce compte et le coût
des appels ne sont pas connus ici.

Large 4 a aussi été essayé en premier : la campagne a arrêté au premier appel
`mistral_invalid_response` sans relance. La consommation de cet appel est
inconnue. Un appel de diagnostic séparé (« Bonjour ») a réussi : 25 tokens
entrée, 245 sortie dont 232 de raisonnement, soit 270 au total. Il a renvoyé
une liste de blocs thinking/text. Cela ne prouve pas la cause précise du premier
échec ; un plafond consommé en raisonnement est une hypothèse. Aucun verbatim
de raisonnement n'a été enregistré. La documentation Mistral indique que Large
4 accepte `low`, `medium` et `high`, pas `none` ; le connecteur historique ne
configure pas ce paramètre. Une future adaptation doit être séparée et testée,
sans modifier les fichiers gelés ni masquer la verbosité par un simple plafond
plus élevé.

Sources : [catalogue Mistral et statut des modèles](https://docs.mistral.ai/models),
[raisonnement et paramètres Large 4](https://docs.mistral.ai/inference/conversations/reasoning),
[tarifs API](https://docs.mistral.ai/inference/pricing).
