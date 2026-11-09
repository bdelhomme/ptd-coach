# Vérifications du dossier

- Trois passages complets : 12 scénarios / 26 réponses chacun ; smoke M01 : 2 réponses.
- Dernier passage conforme à la suite V0.7, 26 couples scénario/tour uniques.
- Messages, scopes, attendus, signaux et marqueurs comparés au JSON source.
- JSONL copiés octet pour octet ; SHA-256 final conforme au rapport de recette.
- Les 160 blocs étudiant/réponse des documents Markdown correspondent exactement
  aux chaînes des 80 enregistrements JSONL, sans retouche.
- Grille CSV : 26 lignes, textes identiques au passage final ; lecteur, cinq
  notes, veto et commentaires intégralement vides.
- Contextes système v1.2 : empreinte reconstruite conforme à celle des traces.
- Manifestes et archive contrôlés après génération : intégrité ZIP, noms de
  chemins relatifs, absence de liens cassés vers des fichiers et empreintes.
- Contrôle de contenu avant livraison : pas de clé locale exacte, formats
  courants de jetons, email, téléphone, chemins personnels ou fichiers locaux
  confidentiels. Les noms présents dans les scénarios sont fictifs.

Ces contrôles vérifient la préparation du dossier, pas la qualité pédagogique
des réponses. Aucune nouvelle requête API, notation ou correction du coach.
