# Sécurité, confidentialité et conformité — exigences de conception

**Non validé juridiquement.** Ce document est une liste de précautions pour la conception et le dialogue avec DPO/DSI, non une attestation de conformité.

## Matrice de visibilité par défaut
| Donnée | Étudiant concerné | Autres membres | Tuteur | Coordination | Admin technique |
|---|---|---|---|---|---|
| Ressource commune | oui | oui | oui | oui | maintenance |
| Contexte / décisions collectives validées | oui | oui (équipe) | oui via vue prévue | synthèse uniquement | maintenance sans contenu par défaut |
| Échanges bruts collectifs | oui (équipe) | oui (équipe) | **non**, sauf extrait ciblé approuvé | non | non par défaut |
| Synthèse collective validée | oui | oui (équipe) | oui | indicateurs seulement | non par défaut |
| Conversation privée individuelle | oui | non | non | non | non par défaut |
| Objectif personnel / réflexion privée | oui | non | non | non | non par défaut |
| Preuve volontairement partagée | oui | uniquement destinataires | si destinataire | si destinataire explicitement autorisé | non par défaut |
| Agrégats d'usage | données personnelles concernées si affichées | non | niveau équipe selon politique | oui, anonymisation si possible | métriques techniques minimales |

## Accès ciblé aux extraits collectifs
Procédure **à arbitrer** : partage volontaire de l'équipe ou demande motivée limitée à un extrait, soumise à règle d'autorisation, date et audit. Aucune simple justification textuelle ne doit ouvrir à elle seule un accès global. Pas de mécanisme implicite pour accéder au privé individuel.

## Obligations à examiner avant un pilote réel
- Responsable de traitement / base légale / information des étudiants / durées de conservation.
- Sous-traitance, transferts, résidence d'inférence, entraînement sur données, rétention et mesures contractuelles.
- Analyse d'impact relative à la protection des données si requise.
- Analyse juridique de la qualification et des obligations applicables en vertu du règlement UE sur l'IA : le suivi/évaluation des acquis peut créer des obligations même sans notes automatiques.
- Hébergement, SSO, sauvegardes, gestion des incidents, supervision, réversibilité, sécurité des accès.

## Tests négatifs indispensables
Étudiant A ne lit pas privé B ; tuteur ne lit pas privé A ; coordination n'obtient pas textes privés via recherche/agrégats/exports ; utilisateur ne lit pas les autres équipes ; administrateur ne contourne pas le RBAC sans procédure exceptionnelle ; contexte modèle sans données interdites ; démo sans données réelles.

## Données techniques
Ne jamais loguer prompts ou réponses privées en clair dans un outil tiers de monitoring sans décision explicite. Chiffrement TLS, secrets hors Git, sauvegardes testées, politique de vulnérabilités et rétention.

## Démo conversationnelle — D-026

Le nouveau fil privé est réservé au propriétaire ; le collectif aux étudiants
de l'équipe. Les transcriptions/export restent interdits aux tuteurs,
coordination et admin. Aucun partage/synthèse validée implémenté dans ce service.
Ressources communes seulement, pas de recherche transversale, pas de mémoire A2
ou d'un autre fil dans le contexte modèle. Sélecteur d'identités fictives :
aucune garantie de confidentialité entre personnes pouvant changer de compte
sur la même démo. Le navigateur annonce conservation locale et transmission
Mistral ; clé uniquement côté serveur. Aucune donnée réelle autorisée.

Les requêtes à Mistral contiennent le fil autorisé et les ressources, pas la
base entière. Les conditions contractuelles de rétention du fournisseur restent
à examiner pour un pilote institutionnel. Le ledger local d'usage ne copie pas
les textes et n'est pas envoyé à un monitoring externe. Voir ADR-0007 et
[le guide](TRY_CONVERSATION_COACH.md) pour les limites et erreurs de facturation.
