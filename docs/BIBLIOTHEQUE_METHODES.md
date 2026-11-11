# Bibliothèque de méthodes · prototype expérimental 0.1

## Statut et portée

Demande du porteur du 11 novembre 2026, après la campagne transversale D-031 :
bibliothèque locale utilisable et essai de sélection contextuelle. Dix fiches
originales, majoritairement sur la relation commanditaire et les exigences,
sont dans `pedagogy/library/methodes-v0.1.json`. Chaque fiche est un **brouillon** :
aucune relecture enseignante ni validation documentaire indépendante ne lui est
attribuée. Les exemples et gabarits sont fictifs. Les correspondances avec les
onze compétences V0.3 sont proposées, non validées institutionnellement.

Les pages publiques GOV.UK, NASA, APM, PMI, AHRQ et ASQ liées dans les fiches
ont été consultées. Elles documentent des pratiques professionnelles dans leurs
propres domaines ; la transposition PTD est originale. Elles ne démontrent pas à
elles seules l'efficacité de chaque adaptation ni son adoption dans toutes les
organisations. Origine historique et fréquence d'usage non établies : non
revendiquées. ISO et les textes fermés n'ont pas été reproduits. Fiche M09 :
AHRQ traite des soins ; adaptation à une équipe d'étudiants à relire.
Les fiches sont volontairement brèves : renforcer modèles et exemples avec un
enseignant, examiner l'analyse fonctionnelle, les parties prenantes, la décision
multicritère et les risques dans une suite éventuelle.

## Utilisation locale

```sh
python3 -m ptd_coach --port 8765
```

Ouvrir `http://127.0.0.1:8765/bibliotheque` : recherche, filtres, fiches,
liens, exemples et repères tuteurs, sans session ni appel Mistral. Une navigation
par liens se trouve aussi depuis `/coach`.

Pour essayer **séparément** le coach enrichi :

```sh
python3 -m ptd_coach --port 8766 --bibliotheque-experimentale
```

La clé Mistral reste dans `.env` ignoré ou l'environnement, jamais dans le
navigateur. Avec `CHAT_PROVIDER=mock`, aucun appel payant. Cette option ouvre
`local-data/coach-library-experimental.sqlite3`, distincte de la base historique :
les fils ne sont pas migrés et les anciennes versions restent disponibles avec
la commande normale. Les mêmes contrôles du service de conversation s'appliquent.
Ces comptes ne sont pas une authentification institutionnelle ; données fictives
uniquement, et avec Mistral le fil utilisé est transmis à son API.

## Choix de recherche et limites

Comparaison de trois approches : mots-clés historiques (simples mais incapables
de prendre en compte le contexte et absents sur les cas clients), plongements
vectoriels ou classificateur LLM (coût et complexité non justifiés ici), recherche
lexicale locale TF-IDF (déterministe, sans dépendance ni appel réseau). Le MVP
combine formulations de situations, regroupements de synonymes, similarité
TF-IDF, seuil minimal et dernier message utilisateur du même fil pour certaines
continuations courtes. L'application choisit au plus une fiche et peut s'abstenir ;
les identifiants sélectionnés sont enregistrés par l'existant. Les scores et
signaux sont disponibles dans la fonction locale `select`, pas encore exposés
dans l'interface. Le contexte fourni est uniquement celui autorisé par le
service, jamais une autre conversation. Cette recherche reste lexicale : elle ne
comprend pas toutes les paraphrases, elle peut sélectionner à tort et le coach
peut ignorer ou mal utiliser la fiche. L'affichage navigateur utilise une
recherche distincte, plus large et non classée par pertinence.

## Évaluation de développement et points critiques

`python3 scripts/compare_library.py --provider mock --output-dir local-data/essai-bibliotheque-mock`
exécute 12 tours simulés. Pour l'essai payant, utiliser `--provider mistral
--allow-billable` dans un nouveau dossier. Il ouvre seulement TX05 et TX07 du
jeu transversal de développement : deux tours, trois variantes, maximum 12
appels sans reprise automatique. Réponses exactes, messages, tokens et latences
sont archivés dans `pedagogy/evaluations/bibliotheque-v01/premier-passage/` ;
la grille humaine est vierge. Le comparateur utilise c2, c2 avec une fiche
imposée, et c2 avec sélection contextuelle. Les variantes bibliothèque ajoutent
aussi un petit cadrage de citation et d'autonomie : l'effet isolé de la fiche
ne peut donc pas être conclu. Ordre fixe, un seul passage et alias de modèle
mobile limitent toute comparaison. Aucune évaluation du jeu réservé.

Constats de développement, pas jugement pédagogique indépendant :

- TX05 : le sélecteur ne choisit aucune fiche aux deux tours, malgré une demande
  de changement. La ressource imposée cite M06, mais invente des estimations
  « 2–3 jours » et « 1 jour », et des intérêts qui ne sont pas établis.
- TX07 : la sélection contextuelle injecte M03 au premier tour, puis rien au
  second. Malgré la fiche, le premier tour invente notamment conservation un an,
  budget nul et fonctionnalités ; il est tronqué. La ressource imposée invente
  notamment un délai et un seuil de 7 jours, même si certains points sont à
  discuter. Son deuxième tour ajoute identité et date de l'emprunteur. Le
  second tour contextuel ajoute une restriction aux emprunts du jour à confirmer.
- La fiche seule ne garantit donc ni autonomie ni non-invention. **Aucun gain
  pédagogique convaincant ne peut être revendiqué**. Une revue humaine et une
  correction de conception séparée sont indispensables avant usage étudiant.

Le premier passage a produit 12 réponses ; résultats par variante dans
`MESURES.json`. La comparaison ne prouve aucune efficacité d'apprentissage.
Ne pas ajuster ce système à l'aide des scénarios réservés.

## Vérifications exécutées

- Six tests dédiés : catalogue et liens, exemples de formulation, abstention,
  continuité sur le fil, contexte séparé et consultation HTTP sans fournisseur.
- `PYTHONPATH=. python3 ../../work/transversale/verify.py` : 120 tests réussis
  le 11 novembre 2026, contrôles documentaires et syntaxiques. Cette commande
  locale exclut explicitement les deux tests historiques qui ouvrent le jeu
  réservé et exclut ce fichier du contrôle documentaire. Les contrôles CI
  historiques peuvent vérifier format et empreinte sans divulguer son contenu.
- Navigation locale : recherche « le client change d’avis », ouverture de M06,
  source et modèle visibles ; navigateur sur fournisseur simulé.
- Comparaison Mistral : 12/12 réponses, 24 485 tokens totaux ;
  température 0,2 et plafond 700. V0.8 c2 : 6 897 tokens, 1 réponse tronquée ;
  fiche imposée : 9 592, aucune tronquée ; sélection : 7 996, 1 tronquée.
  Latences médianes respectives 2 164,5 ms, 2 969 ms et 2 407,5 ms.
  Ces chiffres ne mesurent pas les apprentissages.
