# Intégration pédagogique V0.6 puis V0.7 — 2026-11-09

**Statut : travail de revue sur branche ; propositions non adoptées.**
Demande du porteur : intégrer les contenus et outils fournis, préserver
l'historique et le candidat V0.3, vérifier et ouvrir une PR sans démarrer le
nouveau coach Mistral. Références : D-001/D-009/D-010/D-012/D-020 à D-024.

Base synchronisée : `efb3962c8488b9b064de0c6dd4279d9b111ab758` sur `main`.
Branche : `docs/integrate-pedagogy-v06-v07`. Deux commits d'import successifs
permettent de relire V0.6 avant V0.7 ; aucun historique réécrit.

## V0.6 — huit fichiers intégrés

- [Noyau pédagogique](PTD_PEDAGOGICAL_KERNEL_V06.md).
- [Politique de conversation](PTD_CONVERSATION_POLICY_V06.md).
- [Protocole de pilote](PTD_PILOT_PROTOCOL_V06.md).
- [Registre critique des sources](EVIDENCE_REGISTER_V06.md).
- [R01 : coordination](../pedagogy/resources/R01-coordination-et-engagements.md).
- [R02 : débrief](../pedagogy/resources/R02-debrief-factuel.md).
- [R03 : cadrage et planification](../pedagogy/resources/R03-cadrage-et-planification.md).
- [Vingt cas de recette](../pedagogy/qa/COACH_ACCEPTANCE_CASES_V06.json).

Le noyau propose une théorie d'action et une correspondance des onze codes.
E1–E4 sont une grille analytique de coopération, jamais quatre nouveaux codes.
Le dialogue souple et les sept intentions proposés complètent le cadrage du
ticket 003 ; ils ne remplacent ni la machine A2 ni les contrats API.

## Écarts et arbitrages d'intégration

- Aucun chemin de contenu V0.6 n'existait dans la base ; pas de conflit Git.
- Les README de livraison et briefs `codex/` servent à l'analyse de provenance,
  sans être recopiés comme consignes actives. La demande utilisateur actuelle
  fait autorité, notamment le report du développement Mistral et l'ouverture
  d'une PR. Les archives ne prouvent pas de nouvelles décisions validées.
- Les mentions V0.4/V0.5 restent des déclarations du lot : ces versions n'ont
  pas été fournies. Le socle déjà présent est conservé et référencé.
- V0.6 annonçait six cas critiques ; le JSON en contient **huit**, T13–T20.
  Le protocole est corrigé, sans modifier les scénarios.
- Le noyau annonçait quatre fonctions, la politique en liste **sept** ; cette
  incohérence de comptage est corrigée sans changer la politique.
- Le DOI transmis pour Tannenbaum & Cerasoli (2013) était erroné ; il est
  corrigé dans le registre et R02 selon la
  [notice PubMed](https://pubmed.ncbi.nlm.nih.gov/23516804/) :
  `10.1177/0018720812448394`. Lecture limitée à la notice/résumé.
- Les niveaux d'accès aux sources dans le registre sont attribués aux auteurs
  du lot. Aucune lecture intégrale supplémentaire ou validation scientifique
  ne leur est substituée par l'intégration.

## Préservation

`pedagogy/competencies/candidate-v0.3.json` reste identique à la base : SHA-256
`56558fec5b3005019a65b0e600b53c6c908ea157d50358e852dd5667411851d8`.
Les décisions D-001 à D-024 sont conservées ; aucune proposition du lot n'est
promue VALIDÉE. Prototype A2, schémas, scénarios d'origine et règles d'accès
restent inchangés. Aucune donnée réelle ni clé ajoutée.

## Vérification et publication

Après V0.6 : `make verify` réussi (67 fichiers suivis, 34 tests antérieurs) et
`git diff --cached --check` sans erreur. Les contrôles V0.7 seront consignés
après son import. L'import documentaire ne
constitue pas un essai de modèle, un jugement pédagogique humain, une preuve
d'apprentissage ou une recette de sécurité backend.
