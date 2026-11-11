# Ressources pour l’aide méthodologique en PTD

Audit de développement de R01 à R04 et propositions de fiches. Les ressources
existantes gardent leur statut. Les exemples ci-dessous sont des brouillons
originaux fictifs à relire par des enseignants. Leur texte reste hors des
contextes V0.7, c1 et c2 utilisés pour le comparatif.

## Ce que fournissent les quatre fiches

| Fiche | Appui utile | Lacune à traiter |
|---|---|---|
| R01 Coordination | Quatre accords sur résultat, responsabilité temporaire, interfaces et blocages. Pertinent pour un groupe de sept | Critères pour choisir entre un accord oral, un tableau d’engagements et une clarification de rôles. Retour factuel et animation d’un désaccord ordinaire |
| R02 Débrief | Repères souples pour décrire l’action, l’observation et les interprétations | Lien entre preuve et argument pour une restitution. Transposition autonome sur un cas nouveau |
| R03 Cadrage et planification | Reformulation initiale, jalons, dépendances et écart au prévu | Entretien et arbitrage client, critères d’acceptation, validation et historique d’un cahier des charges. La question sur ce qui doit être terminé illustre un type de lien de planning |
| R04 Concepts c2 | Distingue livrables, activités, liens temporels, jalon, risque et problème | Fiche centrée sur A2/A3. L’enquête sert d’exemple de WBS. Les actions à mener face à une demande vague ou contradictoire restent à développer |

La [relecture R04](V08_C2_CONCEPT_REVIEW.md) détaille ses sources et leurs limites.
Le [bilan c2](V08_C2_REPORT.md) montre que des exemples justes dans une fiche
n’assurent pas une restitution juste par le modèle.

## Sélection par mots-clés

V0.7 fournit R01, R02 et R03 dans son contexte. C1 normalise les accents du
dernier message et compte des chaînes présentes parmi trois listes, par exemple
« planning », « débrief » ou « équipe ». Elle prend au plus une fiche. Les
égalités sont tranchées par l’ordre R03, R02, R01. C2 réutilise ce choix en
remplaçant R03 par R04. L’argument historique de la méthode de sélection
n’intervient pas dans le calcul. Un mot négatif peut déclencher la sélection,
tandis qu’une paraphrase ou une allusion au tour précédent peut la faire
disparaître. Ces choix découlent du code des contextes figés.
[Sélecteur c1](../ptd_coach/chat_context_v08.py) · [Remplacement c2](../ptd_coach/chat_context_v08_c2.py)

| Domaine | Tours du nouveau jeu | C1 et c2 sans fiche | Fiche sélectionnée |
|---|---:|---:|---|
| Commanditaire | 12 | 12 | — |
| Besoin et cahier des charges | 12 | 12 | — |
| Coopération | 8 | 7 | R01 une fois |
| Pilotage et résolution | 8 | 7 | R03 en c1, R04 en c2, une fois |
| Restitution et réflexivité | 8 | 8 | — |

Mesure locale en appelant les sélecteurs sur chacun des 48 messages du jeu de
développement. Dans l’échantillon réel, le premier tour de TX14 déclenche R01
via « équipe ». Son deuxième tour s’en passe, alors qu’il poursuit le même
désaccord. Les autres cas sélectionnés ne déclenchent aucune fiche en c1/c2.
Une fiche disponible dans le contexte peut être ignorée ou mal appliquée. Les
verbatim permettent d’examiner son usage. Ces résultats justifient de comparer
la pertinence des déclenchements avant d’étendre le catalogue.

## Fiche proposée · Enquêter sur une demande et vérifier l’accord

**Quand elle aide.** Le commanditaire formule une solution ou généralise un
besoin, et l’équipe ignore la situation d’usage. En quelques minutes, relever
les mots entendus, demander un exemple récent, repérer qui vit la difficulté,
puis reformuler le but à confirmer. Si le client est indisponible, envoyer une
question de décision et préparer une hypothèse réversible. Distinguer la
reformulation envoyée, l’accord conditionnel et la validation explicite.

**Exemple fictif.** « Il faut un calendrier partagé » devient « Quand deux
associations veulent la même salle, comment apprennent-elles laquelle est
réservée ? ». Consigner l’observation et vérifier le besoin avec la personne
chargée des réservations. Une réponse d’un seul interlocuteur laisse les
autres usages à examiner. Le groupe conduit l’enquête.
[GOV.UK, Learning about users and their needs](https://www.gov.uk/service-manual/user-research/start-by-learning-user-needs)

## Fiche proposée · Construire et relire un cahier des charges court

**Quand elle aide.** L’équipe a des faits recueillis et doit passer d’un besoin
à un brouillon d’exigences. Une ligne par exigence suffit pour commencer.
Identifier la source, écrire le comportement ou résultat attendu et ses
conditions, décrire le contrôle, garder le statut à confirmer. Vérifier la
cohérence entre lignes, les contraintes et la faisabilité. Faire arbitrer les
contradictions, puis dater l’accord de la personne compétente. Vérifier une
exigence sur un prototype et confirmer que l’exigence répond au besoin sont
deux démarches complémentaires.

**Exemple fictif.** Besoin rapporté par l’atelier d’identifier une notice à
partir d’une référence. Brouillon E01. À partir d’une référence connue, un
agent retrouve la notice associée. Contrôle proposé avec un lot fictif de
références et comparaison de la notice trouvée à celle attendue. Critères
de choix du lot, délai et approbation à confirmer. L’équipe peut ensuite
choisir étiquette ou écran en fonction de l’usage et des contraintes.
[NASA, How to Write a Good Requirement](https://www.nasa.gov/reference/appendix-c-how-to-write-a-good-requirement/) · [NASA, System Design Processes](https://www.nasa.gov/reference/4-0-system-design-processes/)

## Fiche proposée · Négocier un changement

**Quand elle aide.** Une nouvelle attente touche le délai, la charge, une
exigence ou une preuve de réussite. Reformuler la demande et sa raison. Noter
les effets sur le résultat, les personnes, le temps et les essais, à partir de
ce que l’équipe sait. Présenter deux options faisables avec leurs conditions
et faire confirmer l’arbitrage. Mettre le plan et l’exigence à jour après
décision. Pour un détail réversible, quelques lignes suffisent.

**Exemple fictif.** On demande un export additionnel avant vendredi. L’équipe
estime qu’elle peut montrer un export de démonstration ou terminer le test
d’usage initial. « Quel résultat souhaitez-vous voir en priorité vendredi ? »
L’accord sur une démonstration d’export laisse sa qualité et sa disponibilité
en usage réel à vérifier.
[APM, What is change control?](https://www.apm.org.uk/resources/what-is-project-management/what-is-change-control/)

## Complément proposé à R01 et R02 · Débloquer un accord d’équipe

**Quand il aide.** Le retard vient d’un engagement ou d’une interface
incertaine. Décrire un fait et son effet, entendre l’explication, convenir de
ce qui est attendu et de qui confirme quoi. Une phrase suffit parfois. Si
l’ambiguïté se répète, proposer un tableau d’engagements à trois colonnes.
Au débrief, partir de l’effet observé et choisir un ajustement. Les outils
de débrief s’inspirent ici d’un domaine différent et demandent une adaptation
au PTD.

**Exemple fictif.** « On a deux unités différentes dans les tableaux et on
ne peut pas agréger les mesures. Est-ce qu’on confirme l’unité et la version
ensemble avant la prochaine mesure ? » Éviter de déduire un manque d’effort.
La situation d’insultes ou de mise en danger requiert un interlocuteur humain
approprié.
[AHRQ, Reviewing the Team’s Performance](https://www.ahrq.gov/teamstepps-program/curriculum/team/tools/debrief.html)

## Fiche proposée · Tester une hypothèse et défendre une conclusion

**Quand elle aide.** Plusieurs explications ou options sont plausibles, et
l’équipe doit présenter une recommandation. Nommer l’effet observé et les
hypothèses. Chercher un essai court qui les distingue. Garder les conditions
comparables, noter les limites de l’essai et les critères d’arbitrage. Pour
la restitution, associer une affirmation à une trace, une limite et une
suite. L’équipe choisit et justifie son arbitrage.

**Exemple fictif.** Une notice a été trouvée plus vite après deux modifications.
Comparer une modification à la fois à tâche et conditions constantes si
possible. Un écart ponctuel aide à formuler la suite de l’enquête. Si les
modifications interagissent, ce petit essai ne sépare pas leurs effets. En
soutenance, montrer les mesures disponibles et préciser quelles conclusions
elles autorisent.
[NIST, Glossary of DOE Terminology](https://itl.nist.gov/div898/handbook/pri/section7/pri7.htm) · [NASA GISS, Guide to Presenting Your Research](https://www.giss.nasa.gov/edu/icp/education/presentation/)

## Priorisation proposée

Relire d’abord les trois fiches sur demande, exigences et changement avec
des encadrants. Vérifier que chaque exemple permet une action faisable en
séance et indique qui valide l’information. Les compléments sur la
coopération et la preuve peuvent réutiliser R01/R02. Pour mesurer l’intérêt
du choix d’une fiche, faire comparer sur le même cas une aide directe et
une aide appuyée sur une fiche à partir du besoin diagnostiqué. Tester les
paraphrases, les tours suivants et les cas où aucune ressource n’apporte de
valeur avant d’envisager un système documentaire plus complexe.
