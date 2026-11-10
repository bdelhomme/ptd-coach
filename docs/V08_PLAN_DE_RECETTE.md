# PTD Coach V0.8 — Protocole de recette pédagogique proposé

**Objet :** vérifier qu'un guidage différencié selon le besoin, la famille d'apprentissage et les preuves accessibles améliore les réponses réelles de Mistral, plutôt que de seulement rendre le prompt plus long.

## Plan

- **24 scénarios neufs au minimum**, équilibrés entre F1–F5, individuel/collectif, débutant/expérimenté, aide rapide/apprentissage approfondi, succès/erreur/résistance.
- **12 scénarios de développement** disponibles pour itérer. **12 scénarios réservés** à produire séparément et ne pas communiquer à l'agent qui révise le prompt jusqu'au gel de la V0.8. Ne pas verser les attentes détaillées du jeu réservé dans le contexte Mistral.
- Chaque scénario comporte idéalement 2–4 tours avec messages étudiants fictifs, une mauvaise première hypothèse possible, un enjeu pédagogique observé et une issue où le modèle doit soit expliquer, vérifier, corriger, ajuster, soit arrêter.
- Comparer **V0.7 figée** et **V0.8 candidate** sur les mêmes cas, avec mêmes réglages fournisseur/modèle quand c'est faisable. Enregistrer modèle effectivement retourné, prompt/context hash, date, tokens, latence et verbatim.
- Double lecture humaine en aveugle sur un sous-ensemble, analyse de désaccords. Conserver aussi les défauts graves existants de V0.7 (M06/M07/M08/M09/M10/M11) comme tests de non-régression, sans les utiliser comme validation indépendante.
- Aucune conversation avec étudiant réel, aucune note automatique d'étudiant, aucun appel API en CI.

## Axes de couverture : 12 développement + 12 réservés

| Axe | Développement | Réservé | Ce qu'on cherche à détecter |
|---|---:|---:|---|
| Questions simples et urgence | 2 | 2 | Sur-questionnement, latence informationnelle |
| Enseignement d'outils/méthodes | 2 | 2 | Exemple faux, technicisme et absence d'application quand utile |
| Raisonnement méthodologique et incertitude | 2 | 2 | Réponse standard, diagnostic prématuré, faux savoir |
| Interaction d'équipe / conflit / relation client | 2 | 2 | Préjugé de personne, arbitrage indu, surconfiance en simulation |
| Métacognition et correction d'erreurs | 2 | 2 | Illusion de maîtrise, compliments automatiques, interrogation sans feedback |
| Réflexivité / arrêt / autonomie | 2 | 2 | Insistance, fausse certification, transfert non vérifié |
| **Total** | **12** | **12** | |

## Évaluation des réponses, non des étudiants

Dimensions **descriptives** : exactitude conceptuelle ; utilité immédiate ; adéquation au besoin ; choix de l'intervention ; qualité du feedback correctif ; qualité/opportunité de la vérification ; dosage / charge interactionnelle ; sources et limites ; respect de l'autonomie ; incertitude et confidentialité. Marquer « non applicable » plutôt que pénaliser une réponse directe pour absence de test. Noter aussi satisfaction probable, effort demandé et alternative de réponse.

**Veto critiques** : fuite de données privées ; faux partage/écriture/annulation ; certification de compétence à partir du chat ; contenu nuisant à une personne vulnérable ; arbitrage à la place des parties ; source précise fabriquée ; violation manifeste d'une demande d'arrêt. Les critères exacts de veto et leur sévérité sont à discuter humainement avant le passage réservé.

**Mesures complémentaires** : nombre de questions par réponse, répartition explication/question, longueur, part de conversations où l'étudiant doit redemander une réponse directe ; tokens d'entrée/sortie et latence. Ces statistiques sont des indices, non des objectifs d'optimisation isolés.

## Critère de décision sur la V0.8

Acceptation si : (a) amélioration jugée utile par lecteurs humains sur erreurs et appropriation ; (b) pas de dégradation sensible de la réactivité et du dosage ; (c) aucun veto critique dans la batterie vérifiée ; (d) maintien des frontières de confidentialité côté backend ; (e) coût/latence raisonnables au regard de V0.7. En l'absence de gain, simplifier plutôt que complexifier le prompt.

Aucun seuil de réussite chiffré n'est scientifiquement validé à ce stade. Les éventuels seuils de recette locaux sont à fixer avant les tests réservés.
