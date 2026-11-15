# Bibliothèque V2 · Parcours de mise en pratique

La demande du porteur est limitée à la bibliothèque et prolonge D-040.
L’approche vise à donner plus de profondeur aux ressources : onze compétences
candidates visibles et filtrables, six ateliers rejouables du premier entretien
à la restitution, et un cas fictif commun. Ce parcours est une proposition
à éprouver, pas un nouveau référentiel ni un calendrier obligatoire.

## Ce que peut faire un étudiant

- Choisir une compétence candidate et lire un signe de progrès observable ;
  choisir ensuite une situation qu’il reconnaît ou ouvrir directement une
  fiche méthode.
- Essayer une mise en pratique, ouvrir les repères de relecture lorsqu’il le
  souhaite, puis essayer un geste analogue sur son propre PTD avec un pair.
- Ouvrir un des 18 modèles de travail : chaque outil indique son usage et un
  piège, présente un exemple distinct et télécharge un CSV vierge. Ainsi,
  le groupe peut rapidement mettre en place une matrice d’exigences, un
  registre hypothèse–preuve ou un point de reprise quand le collectif décroche.
- Approfondir avec les 15 fiches versionnées du catalogue. Les étudiants
  connectés à la démo ont aussi des raccourcis vers les sept brouillons
  d’équipe existants. Les téléchargements et les exercices fictifs sont
  consultables sans compte. La bibliothèque ne reçoit aucun travail rendu.

## Inspiration et arbitrages

Le [MOOC GdP de Rémi Bachelet](https://mooc.gestiondeprojet.pm/) combine
tronc commun, spécialisations et étude de cas. Le [GdP-Lab](https://lab.gestiondeprojet.pm/)
relie les méthodes à une pratique en équipe. Le
[cours sur la collecte de données](https://gestiondeprojet.pm/collecte-de-donnees/)
sert de point de départ pour préciser l’objectif de collecte et la feuille de
relevés. Le parcours reprend ces idées de structure et renvoie aux sources.
Les missions, exemples et modèles sont originaux ; ni supports, ni quiz ni
études de cas du MOOC n’ont été importés. Les fiches V2 conservent leurs
propres références professionnelles et leur statut. Le PTD demande en plus
un dialogue avec un commanditaire, la traçabilité du travail d’enquête, la
gestion d’un engagement qui dure et un retour réflexif individuel.

Le parcours suit des situations typiques de jeudis de PTD. Il ne déduit
aucune date de rendu et ne remplace pas le calendrier communiqué à l’équipe.
Les repères aident à relire une production ; aucun score ni déblocage
automatique. Pas de changement de modèle, de prompt, de mémoire ou de droits.

## Reprendre et vérifier

- Contenu : `pedagogy/library/bootcamp-v2.json`. Les identifiants de méthode
  et d’outil renvoient aux éléments existants. Les titres des compétences
  sont lus dans le candidat V0.3 ; les repères d’observation sont des ajouts
  propres au parcours. Garder les lignes d’exemple fictives et distinctes
  des lignes vierges. Le coach ne consomme pas ce fichier.
- Interface : `web/ptd.html`, `web/ptd.js`, `web/ptd-v2.css`. L’API
  de ressources `/api/library-v2/bootcamp` est publique en mode V2 local
  et en lecture seule. Le catalogue reste accessible si le parcours est
  indisponible. `/bibliotheque` conserve la bibliothèque historique.
- Lancer `CHAT_PROVIDER=mock .venv/bin/python -m ptd_coach --port 8802 --data-dir local-data/essai-v2-bootcamp`,
  puis ouvrir [le parcours](http://127.0.0.1:8802/bibliotheque-ptd).
- Suite à proposer : observer un groupe fictif puis, si le cadre l’autorise,
  un vrai usage pendant un jeudi. Vérifier si deux étudiants arrivent à
  choisir le bon outil, à produire une trace relisible et à transférer le
  geste sur un autre épisode, avant de multiplier les fiches.

La recette locale a passé 165 tests, hors des deux contrôles qui ouvrent le
jeu réservé. Le contrôle du dépôt a examiné 349 fichiers hors jeu réservé.
Dans le navigateur : entrée sans compte, filtrage D2, repères et exemple WBS,
action de téléchargement, recherche de la fiche Gantt, puis retour depuis
le brouillon Gantt de l’équipe fictive avec restauration du focus.
Aucun appel à un fournisseur d’IA.
