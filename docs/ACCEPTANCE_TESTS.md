# Recette initiale — à convertir en tests automatisés

Chaque test doit être exécuté avec **données fictives** et être identifié par une exigence produit.

| ID | Scénario | Résultat attendu |
|---|---|---|
| T-01 | Student-A commence A2 et revient après interruption | État et réponses persistés ; aucune action perdue |
| T-02 | Student-B appelle `GET` sur parcours privé de A | Refus au niveau API et base requêtée par domaine d'accès |
| T-03 | Tuteur appelle l'API conversation privée de A | Refus, même si tuteur de l'équipe |
| T-04 | Tuteur charge la synthèse validée de son équipe | Accès au résumé seulement |
| T-05 | Tuteur tente de charger messages bruts collectifs | Refus, sauf autorisation ciblée approuvée et tracée |
| T-06 | Coordination charge son tableau de bord | Aucun contenu privé ; agrégats définis |
| T-07 | A partage un objet Evidence avec tuteur | Seul objet explicitement sélectionné visible ; journalisation |
| T-08 | Modèle renvoie JSON invalide | Erreur contrôlée ; pas de transition d'état ni perte de données |
| T-09 | Modèle tente d'écrire « compétence acquise » | Aucun niveau validé automatiquement |
| T-10 | Seuil budget dépassé | Pas d'appel facturable sans décision ; message utilisateur adapté |
| T-11 | Fournisseur Mistral remplacé par mock | Contrat respecté et scénario exécutable |
| T-12 | Instruction malveillante dans ressource | Ne contourne pas RBAC, pas de partage ni d'appel non autorisé |
| T-13 | Équipe refuse/corrige résumé | Tuteur ne voit pas version non validée |
| T-14 | Étudiant débriefe une expérience non observée | IA distingue récit, interprétation et preuve |
| T-15 | Import/export/restauration sur nouvel environnement | Seules données autorisées, IDs et versions conservés |

En complément : banc de cas pédagogiques pour A1/A2/B1, calibrage du feedback par des encadrants, tests de non-régression après changement de modèle.
