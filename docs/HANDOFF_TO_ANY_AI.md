# Reprise du projet par un nouvel assistant IA

## Reprise c2 — D-030

Lire [le rapport c2](V08_C2_REPORT.md), le gel `pedagogy/qa/V08_C2_FREEZE.json`
et la relecture conceptuelle. C1 n’est pas validée ; ne pas ouvrir le réservé
pour corriger c2. Le contexte c2 est testé via le service existant, sans nouvelle
fonctionnalité applicative ni modification des anciens fils. Les mesures de
longueur et ponctuation ne sont pas des verdicts pédagogiques.

## Reprise courante V0.8 — D-029

Commencer par `AGENTS.md`, [V08_IMPLEMENTATION.md](V08_IMPLEMENTATION.md) et
le contrat V0.8. Le gel D-027 est historique ; la demande D-029 autorise cette
tranche minimale. Ne pas réutiliser le jeu réservé pour ajuster le prompt.
Le contexte V0.8 c1 est figé par manifeste, les anciennes preuves restent exactes.
La première lecture réservée et l’acceptation pédagogique restent humaines.

Mise à jour : **2026-11-09**. Le dépôt fait autorité ; les anciennes réflexions
restent dans REFLECTION_LOG, les décisions D-001 à D-024 sont préservées.

## Texte de reprise

> Lis AGENTS.md, PROJECT_STATUS, DECISIONS, puis le rapport CONVERSATION_COACH_REPORT,
> le guide TRY_CONVERSATION_COACH, le contrat CONVERSATION_API_V1 et ADR-0007.
> D-026 autorise désormais le premier coach Mistral : le report D-025 demeure
> historique, il ne bloque plus ce développement. Service et base séparés d'A2,
> qui conserve ses états, schémas et simulateur. Le candidat V0.3 ne change pas.
> Le modèle initial mistral-small-latest est configurable côté serveur. La clé
> reste dans env/.env ignoré, jamais dans le navigateur ou les traces.
> La conversation a deux scopes isolés par SQL : privé propriétaire seul,
> collectif étudiants de l'équipe. Aucun accès tuteur/coordination/admin aux
> transcriptions ; aucun transfert automatique d'un autre fil dans le contexte.
> Le modèle n'a aucun outil d'écriture/partage/décision. Le stockage explicite
> du fil n'est pas une validation de compétence ou une synthèse collective.
> Le prompt V0.7 et R01–R03 restent proposés ; le complément applicatif est versionné.
> Les erreurs de recette et les itérations sont conservées, aucune note humaine
> n'est inventée. Vérifie le rapport, la PR et la CI avant d'annoncer leurs résultats.

## État concret et suite

- Application A2 : `ptd_coach/service.py`, fournisseur simulé, `web/app.js`,
  base d'origine intacte. Conversation : `chat_service.py`, `chat_provider.py`,
  `chat_context.py`, `chat_config.py`, `chat_schema.sql`, `web/coach.*`.
- Lancement : `make run`, puis `/coach`. `AI_PROVIDER=mock` reste requis pour A2,
  `CHAT_PROVIDER=mistral` pour le nouveau service ; mode conversation mock possible.
- QA : les 48 tests précédents sont conservés ; nouveaux tests de contexte,
  permissions, idempotence, tokens, erreurs et HTTP. Le nouveau runner
  `scripts/run_conversation_eval.py` rejoue V0.6/V0.7 via le service applicatif.
- Reprise après erreur : pas de retry automatique, ni d'effacement du ledger
  de facturation. Un appel pending après arrêt reste incertain ; ne jamais
  le déclarer gratuit ou le relancer silencieusement.
- Suite : revue humaine des réponses V0.7, compréhension et utilité, ressources
  et confidentialité ; pas de données réelles avant validations institutionnelles.
  Les tickets 004/005 décrivent la tranche réalisée et le travail restant.
- Base de branche : PR #4 encore ouverte au départ ; le nouveau développement
  en dépend, ne pas annoncer une fusion sur main sans vérifier GitHub.

## Principes et statuts à préserver

Finalité : apprentissages individuels dans des projets collectifs ; aide sans
substitution avec explications et ressources ; positionnement formatif privé
pour choisir une priorité. Les choix et conclusions appartiennent aux humains.
Le collectif échange oralement, IA écrite sur écran commun, sans captation audio.
Les tuteurs voient les synthèses autorisées et validées, jamais un accès global
aux conversations. Les partages privés sont sélectionnés et confirmés par leur
propriétaire ; un tiers ne peut pas consentir à sa place. Aucune donnée réelle
étudiante ou clé dans Git. Pas de validation scientifique, pédagogique collective,
institutionnelle ou DSI/DPO déduite de l'import ou de la réussite de tests techniques.

Le corpus global et les correspondances restent proposés (D-024). Les anciens
exemples A2 ne valent pas validation des durées/charges ou des descripteurs.
Les lots V0.4/V0.5 évoqués dans les archives ne sont pas fournis : ne pas les
reconstituer. Pour l'historique, lire COACHING_FRAMEWORK, REFLECTION_LOG et
PROJECT_MANAGEMENT_FOUNDATIONS, puis les spécifications d'origine.

## Transmettre le contexte

Partager le dépôt Git privé ou une archive autorisée, pas le seul historique
d'un chatbot. Les quatre Word institutionnels d'origine sont absents : voir
[REFERENCE_MATERIAL.md](REFERENCE_MATERIAL.md). Les manifestes ne donnent aucun
droit de republier leurs contenus ou les échelles des références scientifiques.
