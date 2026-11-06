# Modèle de coûts d'inférence — hypothèses auditées, pas devis

## Pourquoi le mesurer
La facturation du fournisseur IA doit pouvoir passer du compte de démonstration à un compte institutionnel sans changement de code. Le coût total inclut aussi **hébergement, maintenance, conformité et encadrement humain**.

## Variables
- `T` équipes, `S` séances collectives / équipe, `R_c` réponses du modèle par séance.
- `N` étudiants, `I` sessions individuelles / étudiant, `R_i` réponses / session.
- `Cin_c`, `Cout_c` tokens entrants/sortants **par requête collective**, notamment les prompts, mémoires, ressources.
- `Cin_i`, `Cout_i` tokens par requête individuelle.
- `f` coefficient pour appels annexes ; `p_in`, `p_out` tarifs du modèle / million ; `m` surcoût optionnel régional.

**Formules** :

`In = f × (T × S × R_c × Cin_c + N × I × R_i × Cin_i)`  
`Out = f × (T × S × R_c × Cout_c + N × I × R_i × Cout_i)`  
`Cost = m × (In × p_in + Out × p_out) / 1_000_000`

## Scénario exploratoire (non validé)
14 équipes × 7 étudiants ; 17 séances collectives, 8 réponses/ séance ; 10 sessions individuelles / étudiant, 8 réponses / session ; 5000 tokens entrants et 400 sortants par collectif ; 4500 entrants et 450 sortants par individuel ; `f=1.2`. **Résultat calculé : 53 760 000 entrants, 5 147 520 sortants.**

Ces volumes sont **des hypothèses**, non des mesures. Le contexte pourrait être réduit via la mémoire structurée, mais il ne faut pas présumer d'économie avant mesures. La tarification des modèles, des endpoints et des caches change : **relever les prix officiels et horodater** avant toute demande de budget.

## Journal par appel
`invocation_id`, date, type d'activité, modèle exact, région si applicable, prompt version, usage retourné par fournisseur, coût estimé selon table de tarifs horodatée, latence, statut de succès et code d'erreur. Ne pas inclure les textes privés dans la comptabilité.

## Règles
Budget global et quotas par étudiant/groupe, alertes de seuils, plafonds par activité, circuit de validation des dépassements, suivi des requêtes simultanées du jeudi. Tester les coûts en petits lots avant extension. Le budget de capacité ne doit pas devenir un classement des étudiants.
