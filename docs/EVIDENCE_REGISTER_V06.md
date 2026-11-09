# PTD Coach V0.6 — registre critique des sources

**Revue déclarée dans le lot source du 7 novembre 2026.** Lien et degré d'accès effectivement vérifiés ; ne pas transformer une référence en « preuve que le coach IA fonctionne ». Cette revue thématique n'est pas une revue systématique exhaustive de la littérature mondiale.

| Référence | Type / accès vérifié | Point solide | Ne démontre pas | Conséquence de conception |
|---|---|---|---|---|
| **IPMA ICB4**, *Individual Competence Baseline* | Cadre professionnel, présentation officielle et documentation déjà indexée dans le dépôt ; pas de relecture intégrale du manuel ici | Répertoire international de domaines de compétences projet | Que nos 11 compétences sont « validées IPMA » | Vérifier couverture management, personnes, contexte ; ne pas copier une taxonomie intacte |
| **CDIO Syllabus 3.0** | Syllabus officiel en HTML consulté intégralement pour la rubrique 3.1.1–3.1.3 | Conduites d'équipe, gestion des rôles, réunions, décisions, diversité de perspectives, réflexion et implication des parties prenantes | Efficacité de notre application | Décrire des situations et comportements dans le contexte ingénieur |
| **Salas, Sims & Burke (2005)** DOI 10.1177/1046496405277134 | Résumé éditeur consulté ; pas de revendication de lecture intégrale | Cadre des 5 composantes du travail d'équipe et mécanismes de coordination | Hiérarchie normative de nos 4 capacités E1–E4 | Ancrer coordination, entraide, adaptation, suivi mutuel, collectif |
| **Ohland et al. (2012)** DOI 10.5465/amle.2010.0177 ; **CATME** | Article complet disponible via CATME (PDF) ; **la présente vérification porte directement sur la page HTML officielle des cinq dimensions**, pas sur une nouvelle lecture page par page du PDF | Cinq dimensions : contribuer, interagir, suivre le cap, qualité, connaissances/aptitudes pertinentes | Reproduction libre des échelles, évaluation automatique des individus par LLM | Ne pas oublier qualité et savoirs, ne pas attribuer à CATME notre adaptation |
| **McEwan et al. (2017)** DOI 10.1371/journal.pone.0169604 | Texte intégral ouvert sur PLOS/PMC, résumé et résultats contrôlés | Méta-analyse 51 articles, 72 interventions, 8 439 participants ; effets moyens positifs des interventions étudiées | Qu'une modalité particulière domine les autres ni qu'un coach IA apporte cet effet | Enseigner explicitement des comportements, ne pas se contenter de « faire un projet » |
| **Keiser & Arthur (2021)** DOI 10.1037/apl0000821 | Résumé intégral indexé PubMed ; texte complet non lu | Méta-analyse 61 études, importance de l'alignement de l'AAR avec l'objet et de l'appui sur des éléments objectifs | Que des débriefs IA produisent le même effet | Débrief court centré sur une activité et des indices concrets, laisser place à l'auto-animation |
| **Tannenbaum & Cerasoli (2013)** DOI 10.1177/0018720812448394 | Résumé PubMed ; intégral non lu | 46 échantillons ; effets globaux positifs des débriefings, conditions diverses | Effet universel de toute question réflexive | Débrief structuré oui, mais non obligatoire ; étudier la qualité de mise en œuvre |
| **Edmondson (1999)** DOI 10.2307/2666999 | Résumé éditeur ; texte ouvert repéré Harvard/MIT mais non relu intégralement ici | Association sécurité psychologique / comportements d'apprentissage dans 51 équipes industrielles | Causalité simple ni généralisation automatique aux étudiants | Coach collectif non accusateur ; pas de dévoilement obligé en groupe |
| **Nicol & Macfarlane-Dick (2006)** DOI 10.1080/03075070600572090 | Résumé éditeur et manuscrit accepté accessible dépôt institutionnel ; pas de nouvelle lecture exhaustive du manuscrit ici | Feedback formatif comme appui à l'autorégulation de l'étudiant | Efficacité automatique d'un chatbot | Laisser l'étudiant se donner des critères et décider des prochaines actions |
| **Chi & Wylie (2014)** DOI 10.1080/00461520.2014.965823 | Résumé éditeur consulté ; version intégrale institutionnelle repérée | Cadre ICAP pour discuter engagement cognitif | Classement garanti de toutes interactions IA | Favoriser explication construite, mais sans questionnements systématiques |
| **Gollwitzer & Sheeran (2006)** DOI 10.1016/S0065-2601(06)38002-1 | Résumé scientifique éditeur consulté | Planification « si [situation], alors [action] » associée à l'atteinte d'objectifs dans une méta-analyse de 94 tests | Gain spécifique sur coopération d'ingénieurs ou sur une IA coach | Permettre à l'étudiant de préparer une action située ; jamais automatique |
| **Garel & Ika (2026)** *Le management de projet*, La Découverte | Notice/sommaire déclarés vérifiés dans la V0.5 (non fournie ici) ; voir aussi PROJECT_MANAGEMENT_FOUNDATIONS.md dans le dépôt ; **texte intégral non consulté** | Référence francophone panoramique potentiellement utile | Toute affirmation détaillée sur les chapitres non lus | À reprendre avec accès Cairn/PSL, ne pas bloquer le prototype |

## Liens primaires consultables

- CDIO : https://www.cdio.org/content/cdio-syllabus-30
- CATME : https://info.catme.org/features/catme-five-dimensions/
- McEwan 2017 texte intégral : https://pmc.ncbi.nlm.nih.gov/articles/PMC5234826/
- Salas 2005 (résumé éditeur) : https://journals.sagepub.com/doi/10.1177/1046496405277134
- Keiser & Arthur 2021 (résumé) : https://pubmed.ncbi.nlm.nih.gov/32852990/
- Tannenbaum & Cerasoli 2013 (résumé) : https://pubmed.ncbi.nlm.nih.gov/23516804/
- Edmondson 1999 (éditeur) : https://journals.sagepub.com/doi/10.2307/2666999
- Nicol & Macfarlane-Dick 2006 (manuscrit institutionnel) : https://strathprints.strath.ac.uk/3235/
- Chi & Wylie 2014 : https://doi.org/10.1080/00461520.2014.965823
- Gollwitzer & Sheeran 2006 : https://doi.org/10.1016/S0065-2601(06)38002-1
- IPMA ICB4 : https://ipma.world/ipma-standards-development-programme/icb4/

## Déductions justifiées et limites

**Ce que l'on peut recommander** : ressources contextualisées ; pratique dans le projet réel ; retours réflexifs courts ; possibilité de débrief collectif ; prudence sur les interprétations personnelles ; vérification de transferts hors IA.

**Ce que l'on ne peut pas affirmer** : que ces méthodes mises en œuvre par Mistral amélioreront causalement les compétences ; qu'une conversation prouve une compétence ; que les 11 catégories constituent un instrument psychométrique validé ; qu'une comparaison brute des effets publiés prouve la supériorité de jeux de rôle, cours, ateliers ou débriefings.

**Futures vérifications** : texte intégral Garel/Ika ; lecture systématique d'ICB4, d'Ohland et de Nicol ; travaux récents spécifiquement sur les tuteurs IA génératifs en apprentissage par projet et leur dépendance/surdéclaration de performance. Consigner les dates de lecture et les pages exactes à chaque approfondissement.

## Note d’intégration — 2026-11-09

Les niveaux de lecture du tableau sont ceux déclarés par les auteurs du lot ;
ils ne constituent pas une nouvelle lecture intégrale par l’assistant intégrateur.
Les lots V0.4/V0.5 évoqués ne sont pas présents dans ce dépôt ; aucune décision
supplémentaire n’en est déduite. La recherche antérieure reste consultable dans
[PROJECT_MANAGEMENT_FOUNDATIONS.md](PROJECT_MANAGEMENT_FOUNDATIONS.md).

Contrôle ciblé pendant l’intégration : notices/résumés PubMed de Tannenbaum &
Cerasoli et Keiser & Arthur, page officielle CDIO (rubriques d’équipe). Le DOI
Tannenbaum & Cerasoli transmis (`10.1177/0149206312441830`) a été corrigé en
`10.1177/0018720812448394`, celui de l’article *Human Factors* 55(1), 231–245
[identifié dans PubMed](https://pubmed.ncbi.nlm.nih.gov/23516804/).
Les autres références et accès déclarés restent à approfondir ; aucun bénéfice
causal propre à PTD Coach ou Mistral n’est établi par cette intégration.
