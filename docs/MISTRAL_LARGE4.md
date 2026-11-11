# Mistral Large 4 : diagnostic, correction et comparaison exploratoire

## Cause technique reproduite

Le 11 novembre 2026, reproduction sur TX05 c2, température 0,2 et plafond
700 tokens : avec le réglage de raisonnement implicite, l'API a terminé avec
`finish_reason=length`, 700 tokens de sortie dont 699 de raisonnement et un
seul bloc `thinking`, sans texte final. Le connecteur historique signale alors
une réponse inexploitable. C'est une reproduction cohérente avec le premier
échec, mais l'utilisation détaillée de cet appel historique n'avait pas été
conservée : sa cause exacte ne peut être prouvée rétroactivement.

Sur le même message et le même contexte, `reasoning_effort=low` avec le même
plafond a renvoyé une réponse finale (332 tokens de sortie dont 209 de
raisonnement). Les deux réponses ont été diagnostiquées uniquement par leur
structure et leurs compteurs, sans enregistrer le texte de raisonnement :
`pedagogy/evaluations/comparaison-mistral-large4-low/DIAGNOSTIC.json`.

## Correction

`MistralReasoningProvider` est un nouveau fournisseur séparé, activé pour
`mistral-large-4` et `mistral-large-4-0`. Il fixe par défaut `low`, configurable
par `MISTRAL_REASONING_EFFORT=low|medium|high`, accepte les blocs de texte,
ignore les blocs de raisonnement, interdit les appels d'outils et fournit
l'erreur explicite `mistral_reasoning_limit` si la limite est atteinte avant
la réponse finale. Pas de retry automatique. Le modèle par défaut reste Small,
le fournisseur historique et les fichiers gelés sont intacts.

L'application ne conserve et ne retransmet que le texte final dans l'historique.
[Mistral recommande de conserver les blocs de raisonnement pour les échanges
multitours](https://docs.mistral.ai/inference/conversations/reasoning) et avertit
que leur retrait peut réduire la qualité. Ici on ne les conserve pas pour éviter
une nouvelle mémoire opaque ; la qualité multitour peut donc être dégradée.
C'est une limite importante à réévaluer avant tout usage au-delà du prototype.
La limite 700 comprend raisonnement et réponse ; un raisonnement long peut
encore laisser peu ou pas de texte final. Le prix des appels échoués sans usage
récupéré reste inconnu.

Pour essayer uniquement sur données fictives :

```sh
MISTRAL_MODEL=mistral-large-4 MISTRAL_REASONING_EFFORT=low python3 -m ptd_coach --port 8780 --bibliotheque-experimentale
```

La clé reste locale dans `.env` ignoré ou l'environnement. L'option conserve
la base expérimentale séparée ; changer de modèle ne change pas les droits.

## Comparaison et prix

Même corpus de développement TX05/TX07, deux tours, trois contextes ; 12 réponses
par modèle. Les systèmes, messages fictifs et ressources sont identiques à
chaque paire ; les historiques divergent aux deuxièmes tours. Small est un alias
mobile ; Medium 3.5 est déprécié ; Large utilise `low` alors que les autres
utilisaient leurs réglages implicites. Les réponses n'ont pas été évaluées en
aveugle ; une seule répétition et deux scénarios ne mesurent pas la robustesse.
Les textes exacts et la grille humaine vierge se trouvent dans
`pedagogy/evaluations/comparaison-mistral-large4-low/`.

| Modèle | Entrée | Sortie | Total | Réponses tronquées | Prix indicatif |
|---|---:|---:|---:|---:|---|
| Small, alias historique | 20 588 | 3 897 | 24 485 | 2/12 | env. 0,0054 $ si l'alias correspond à Small 4 aux tarifs actuels |
| Medium 3.5 | 19 300 | 2 263 | 21 563 | 0/12 | tarif actuel non établi, modèle déprécié |
| Large 4, low | 17 462 | 3 521 | 20 983 | 0/12 | env. 0,0196 $ sans réduction de cache |

Estimation, pas facture : tarifs publics standard consultés le 11 novembre 2026
[chez Mistral](https://docs.mistral.ai/inference/pricing), par million de tokens :
Small 4 : 0,15 $ entrée / 0,60 $ sortie ; Large 4 : 0,70 $ entrée / 2,10 $ sortie.
L'alias Small retourné ne permet pas d'établir sa version exacte historique ;
le calcul Small 4 est donc une hypothèse, pas son coût constaté. Les tokens
cachés, taxes et conditions du compte ne sont pas disponibles par appel dans
les corpus ; le coût réel peut différer. Ne comprend pas les diagnostics ni
l'appel historique en échec. Les tokens de raisonnement sont compris dans la
sortie et facturables, sans détail par appel dans le corpus de comparaison.

## Observations de développement, à confirmer en revue humaine

- **TX05** : Large conserve la condition de l'accord au second tour. Sans fiche,
  il introduit des dates « jeudi 1/2 » et suggère un report au jeudi suivant qui
  ne figure pas dans la demande. Avec M06, il ne promet pas immédiatement, mais
  réduit les options proposées à deux sans examen de leur faisabilité.
- **TX07 sans fiche** : Large n'invente pas tout un cahier des charges comme
  les deux autres, mais demande surtout une précision, alors que l'étudiant a
  demandé une aide concrète. Au tour suivant, il ajoute « rapidement » bien que
  le délai n'ait pas été donné.
- **TX07 avec M03** : Large illustre un seuil fictif de trois secondes puis dit
  paradoxalement éviter d'inventer un délai ; ce chiffre peut contaminer le
  projet. Dans l'autre contexte, il remplace le seuil par X à discuter et
  indique correctement que le délai est à préciser au tour suivant.

**Conclusion provisoire :** Large fonctionne techniquement en low et paraît
plus prudent dans certaines réponses, mais il invente encore des informations
ou des seuils et n'apporte pas toujours l'aide demandée. Cet échantillon ne
prouve aucun gain global ni un apprentissage supérieur. Le choix d'un modèle
pour des étudiants réels exige une revue indépendante et d'autres situations.

## Contrôles

Tests dédiés hors réseau : blocs thinking/text, limite sans texte et sans retry,
refus d'outils, validation du niveau, sélection du fournisseur. Le protocole
mock de 12 réponses et les tests historiques hors jeu réservé ont été exécutés.
Le premier passage réel a donné 12/12 réponses, aucun échec ni troncature.

`PYTHONPATH=. python3 ../../work/transversale/verify.py` : **125 tests réussis**
le 11 novembre 2026. Cette vérification locale exclut les deux tests qui ouvrent
le jeu réservé. Le texte final conservé par l'application est celui qui figure
dans les verbatim ; les blocs de raisonnement ne sont pas archivés.
