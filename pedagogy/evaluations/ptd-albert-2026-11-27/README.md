# Premier essai Albert API

Le 27 novembre 2026, trois appels de coaching sur la trajectoire fictive
SEM-A et un appel de diagnostic ont porté sur le premier entretien et un
arbitrage en cours de projet. Le [journal JSONL](comparaison.jsonl) contient
les réponses textuelles et le statut de l’appel interrompu. L’[essai de
référence](../ptd-v2-demo/semestre-v2.jsonl) utilise GLM Flash en `low` sur
Mistral. Les réponses de lancement ci-dessous ont la même empreinte de
message système V2 0.2, la même température de 0,2 et le même plafond
de 2 000 tokens. Les fournisseurs et réglages de raisonnement diffèrent.

| Lancement | Entrée | Sortie | Total | Latence | Arrêt |
| --- | ---: | ---: | ---: | ---: | --- |
| GLM Flash sur Mistral | 3 173 | 376 | 3 549 | 4,18 s | stop |
| DeepSeek V4 Flash 0731 sur Albert | 3 322 | 1 574 | 4 896 | 33,01 s | stop |
| GPT-OSS 120B sur Albert | 2 860 | 457 | 3 317 | 13,43 s | stop |

DeepSeek laisse toute l’équipe entendre la demande, donne des rôles simples
et distingue les traces d’école des attentes du commanditaire. GPT-OSS
propose une répartition concrète, mais organise la rencontre autour de la
présentation d’un plan. Il décrit quatre rôles puis « Les 2 autres membres »
alors que l’équipe annonce sept membres. Il fixe aussi un agenda de quinze
minutes sans durée fournie. Sur ce tour, la réponse DeepSeek est plus adaptée
à l’écoute du commanditaire.

Au deuxième tour, DeepSeek a renvoyé une réponse inexploitable. Le diagnostic
a rejoué exactement les mêmes messages, dont la réponse DeepSeek du premier
tour. La passerelle a renvoyé `finish_reason=length`, 3 614 tokens d’entrée
et 2 000 tokens de sortie, soit 5 614 au total, avec un champ de raisonnement
et aucun texte final. Le contenu de raisonnement a été écarté. Ce diagnostic
explique le blocage observé sur le rejeu. Le fournisseur distingue désormais
ce cas avec le code `albert_output_limit`. Le deuxième scénario de semestre
n’a pas été exécuté en réel. GPT-OSS n’a été essayé que sur le lancement.

Ces mesures sont ponctuelles. Les nombres de tokens et la latence dépendent
de la tokenisation, du raisonnement et de l’infrastructure. Les coûts réels
et l’efficacité pédagogique sur le semestre n’ont pas été mesurés.
[Reproduire l’essai](../../../docs/PTD_ALBERT_API.md).
