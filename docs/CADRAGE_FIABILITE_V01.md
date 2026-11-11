# Cadrage de fiabilité v0.1 — expérimental

## Objectif et diagnostic

À la demande du porteur, étudier comment améliorer le cadrage existant, sans
présenter les travaux précédents comme inexistants. Les essais D-031 à D-035
montrent que la candidate c2 interdit déjà les inventions mais transforme
parfois une condition en accord global ou une absence de décision en refus,
crée des dates et seuils, ou attribue une conclusion trop générale à de petits
échantillons. Un bon cadrage ne garantit pas qu'un modèle le respecte.

## Changement proposé

`pedagogy/prompts/COACH_CADRAGE_FIABILITE_V01.md` ajoute au contexte c2 +
bibliothèque des repères sur la provenance, le statut d'un souhait, d'un accord
conditionnel, d'une hypothèse et d'une inconnue. Trois exemples fictifs courts
illustrent leur utilisation. Une aide concrète demeure possible et peut être
rédigée à partir des faits ; aucune trame ou vérification n'est obligatoire.
Il ne s'agit ni d'un score, ni d'un routage rigide, ni d'une décision à la place
des personnes. Le contexte `ReliableContext` est distinct et possède sa propre
empreinte ; il réutilise la sélection de ressources de la bibliothèque sans
l'améliorer. Les anciens prompts, ressources, référentiel et données demeurent
identiques. Aucune mémoire de semestre n'est créée.

**Limite de méthode :** les exemples ont été écrits à partir des défauts connus,
notamment TX05 et TX07 ; même avec des exemples différents, cela peut favoriser
ces cas. TX22 est un cas supplémentaire de développement, non une évaluation
indépendante. Une nouvelle batterie aveugle et une relecture humaine sont
nécessaires avant de conclure à un transfert.

## Essai et résultat

Le gel `pedagogy/qa/RELIABILITY_CONTEXT_FREEZE.json` a été écrit avant l'appel et
vérifié par `scripts/compare_reliable_context.py`. L'essai compare la bibliothèque
existante à la variante de fiabilité, avec le même modèle `mistral-large-4`,
raisonnement medium, température 0,2, sans `max_tokens` demandé : TX05, TX07,
TX22, deux tours et deux contextes, 12 appels maximum. Les mêmes fiches sont
sélectionnées pour les messages comparables ; les réponses différentes changent
les historiques au second tour. Les limites du fournisseur, du connecteur et de
la connexion subsistent ; les blocs thinking ne sont pas conservés. Aucun scénario
réservé ni donnée réelle n'a été lu ou utilisé.

Les 12 appels ont produit une réponse, aucune troncature signalée. Les requêtes,
verbatim, grilles de revue vierges et empreintes sont dans
`pedagogy/evaluations/cadrage-fiabilite-v01/`. La comparaison affichée identifie
les variantes ; une autre lecture avec labels est fournie, sans garantir que le
style ne les trahisse pas.

### Observations de développement à discuter, pas verdict humain

- **TX05 tour 2** : la référence affirme à tort que les alertes sont hors
  périmètre. La variante conserve l'accord partiel et conditionnel, sans attribuer
  un refus des alertes. Au premier tour, elle présente toutefois comme nécessaire
  qu'un autre élément « cède », alors que la capacité n'est pas estimée. Elle
  ne restitue pas explicitement que le client souhaite conserver la date dans
  sa proposition de second tour. Le cadrage ne garantit pas la fidélité complète.
- **TX07** : la variante fournit une trame, laisse les paramètres à discuter et,
  au second tour, formule le besoin sans créer de délai maximal. La référence
  propose en premier tour des données et un horodatage ; elle les marque à
  confirmer, mais leur reprise comme exigences de projet reste un risque.
  La variante évoque également un objectif reformulé à vérifier avec le service.
- **TX22** : les deux variantes rapportent les trois observations mais concluent
  que le repère fonctionne ou est compréhensible pour une partie des utilisateurs,
  ce que ces seuls résultats ne permettent pas d'attribuer avec certitude au
  repère. Elles évoquent un « point de friction précis » sans connaître l'étape.
  La variante conseille aussi d'éviter « 66 % » : un pourcentage descriptif
  calculé sur trois personnes n'est pas faux en soi ; c'est sa généralisation
  qui serait trompeuse. Ces réponses exigent une relecture conceptuelle.

**Conclusion :** amélioration ponctuelle plausible sur le statut d'un accord,
mais pas de gain pédagogique général établi ; la variante reste un brouillon.
Les exemples étant proches de deux cas étudiés, l'écart observé ne démontre pas
un transfert. Une revue indépendante des verbatim est requise.

### Mesures, non scores

| Contexte | Réponses | Tokens entrée | Tokens sortie | Total | Latence médiane | Estimation |
|---|---:|---:|---:|---:|---:|---:|
| Bibliothèque existante | 6 | 8 635 | 4 324 | 12 959 | 8 300,5 ms | ~0,0151 $ |
| Fiabilité v0.1 | 6 | 12 911 | 4 197 | 17 108 | 10 388,5 ms | ~0,0179 $ |

Estimations sans cache, taxes ou conditions de compte, aux tarifs standard
[publiés par Mistral](https://docs.mistral.ai/inference/pricing) : 0,70 $ par
million de tokens d'entrée et 2,10 $ de sortie pour Large 4. Les tokens de
raisonnement sont comptés dans la sortie. Ces montants ne sont pas la facture.
La différence de longueur du contexte, les historiques et la variabilité du
modèle limitent la comparaison ; la longueur ne démontre pas la qualité.

## Essayer localement

Depuis la racine du dépôt, avec une clé dans `.env` ignoré :

```sh
MISTRAL_MODEL=mistral-large-4 MISTRAL_REASONING_EFFORT=medium CHAT_TIMEOUT_SECONDS=90 python3 -m ptd_coach --port 8783 --cadrage-fiabilite --sans-plafond-test
```

Ouvrir `http://127.0.0.1:8783/coach`. Comptes et situations fictifs uniquement.
Le paramètre de limite de sortie n'est pas envoyé dans ce mode explicitement
activé ; les limites de Mistral et du connecteur subsistent, et les appels sont
facturables. La base locale `coach-reliability-experimental.sqlite3` est séparée.
Sans l'option, le fonctionnement habituel conserve son plafond configuré. Les
échanges privés et collectifs restent soumis aux contrôles du service existant.

## Passation et contrôles

Tests dédiés : séparation des contextes, empreinte, sélection des ressources,
isolation d'un fil privé, comparaison mock et grille vierge, et limitation du
mode sans plafond explicite au contexte de fiabilité Large 4. Vérification HTTP
en mode simulé puis configuration HTTP du serveur Mistral sans envoi de message.
Voir `docs/PROJECT_STATUS.md` pour les résultats des tests globaux et la PR.
Suite proposée : revue humaine des cas, nouveau jeu indépendant sans accès au
jeu réservé historique ; traiter la sélection des fiches et une représentation
fiable des statuts comme hypothèses séparées, avant toute mémoire longitudinale.
