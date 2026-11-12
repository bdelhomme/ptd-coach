# Essayer PTD Coach sur plusieurs semaines

Depuis la racine du dépôt, lancez la démo avec une base de recette isolée.

```sh
make bootstrap
CHAT_PROVIDER=mock .venv/bin/python -m ptd_coach --port 8765 --data-dir local-data/recette-ptd
```

Ouvrez [PTD Coach](http://127.0.0.1:8765/). Les sept étudiants de l’équipe
principale travaillent pour l’Atelier des Arts fictif. Une seconde équipe et un
second tuteur permettent de vérifier les droits. Le projet présente six
situations de jeudi matin, de la première demande à la restitution. L’équipe
peut avancer dans la simulation depuis **Faire le point**.

1. Ouvrez le compte **Étudiant démo A** et confirmez l’usage de données fictives.
   Dans **Coach**, choisissez l’espace **Équipe**, créez un fil et demandez
   « Comment construire notre cahier des charges ? ».
2. Ouvrez la fiche M03 proposée avec la réponse, puis revenez à la conversation.
   Dans **Notre projet**, rédigez une question, une exigence provisoire et un
   critère de vérification. Précisez leur source et l’origine de la formulation.
3. Confirmez les éléments relus par l’équipe. Dans **Faire le point**, ajoutez
   un bilan et une prochaine action. Confirmez-les dans le point d’étape,
   cliquez sur **Simuler le jeudi suivant** et ouvrez un nouveau fil collectif.
   Les éléments confirmés de l’équipe font partie du contexte de ce fil.
4. Partagez explicitement une question ou un bilan confirmé. Changez de compte
   et ouvrez le **Tuteur démo**. Il retrouve les éléments partagés de son équipe
   et les repères de la bibliothèque. Retirez le partage depuis un compte
   étudiant de l’équipe et vérifiez la disparition dans la vue tuteur.
5. Testez une note individuelle avec le compte A. Confirmez-la puis ouvrez
   un nouveau fil privé. Un autre compte et les fils collectifs de A
   gardent chacun leur propre périmètre.

Pour la recette mobile, répétez les étapes avec une fenêtre de 390 px de
largeur ou un téléphone sur un environnement de recette approuvé. Vérifiez le
retour au fil, l’accès au formulaire et l’absence de défilement horizontal.
La démo locale écoute sur le Mac et le test à 390 px ne nécessite aucune mise
en réseau du serveur.

Le simulateur produit un exemple de navigation et permet de vérifier le cycle
sans API. Pour une réponse du modèle, renseignez `MISTRAL_API_KEY` dans le
fichier local `.env` ignoré par Git, puis lancez la commande avec
`CHAT_PROVIDER=mistral` et le modèle choisi dans `MISTRAL_MODEL`. La taille
des réponses, le délai réseau et le nombre d’appels sont réglables avec
`CHAT_MAX_TOKENS`, `CHAT_TIMEOUT_SECONDS` et `CHAT_MAX_CALLS`. Un appel
transmet le fil, la fiche éventuellement sélectionnée et le contexte autorisé.

## Règles du prototype

- Les comptes fictifs sont librement sélectionnables sur ce Mac. Le serveur
  écoute sur la boucle locale. Pour la préparation institutionnelle, consulter
  la [checklist du pilote](CHECKLIST_PILOTE_PTD.md).
- Une confirmation atteste une action humaine sur la formulation affichée.
  Une hypothèse confirmée garde son type. La source indique ce qu’a confirmé
  le commanditaire lorsque cette information est établie.
- Modifier une formulation retire sa confirmation et son partage. Le tuteur
  voit uniquement les éléments collectifs confirmés et partagés avec son
  compte. Les modifications simultanées s’appuient sur la version de l’élément.
- Les repères confirmés sont relus à chaque nouvel appel. Le contexte modèle
  prend jusqu’à cinq repères récents, entiers, dans le périmètre du fil. Une
  confirmation est effectuée par un membre de l’équipe, sans quorum. Le journal
  de partage enregistre l’action, la date, la version et les comptes concernés,
  sans conserver le texte ni sa source. Une révocation affecte les prochaines
  consultations du tuteur. Les échanges et transmissions déjà effectués, ainsi
  que les copies exportées, ont leur propre cycle de vie.
- Le prototype utilise une base SQLite pour le projet et une base séparée pour
  le coach intégré. Le mode historique du coach se lance avec
  `--coach-historique`. Le parcours simulé A2 est accessible sur
  [Historique A2](http://127.0.0.1:8765/historique-a2).

Les quatre espaces sont expérimentaux. Les scénarios transversaux couvrent les
onze compétences candidates et la revue humaine reste nécessaire. Les erreurs
documentées sur les faits, les décisions et la substitution guident la recette.
[Audit transversal](AUDIT_GLOBAL_PTD_2026_11_12.md).
