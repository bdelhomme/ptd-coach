# Architecture cible — proposition

## Principe
Application web **auto-hébergeable**. Le code pédagogique, les données et les permissions ne dépendent pas d'une plateforme de modèle ou d'hébergement.

```text
Browser étudiants / tuteurs / coordination
              |
       Frontend (Next.js proposé)
              |
       API métier (FastAPI proposé)
         |         |          |
  RBAC/ABAC   PostgreSQL   Ressources / objet
         |
    Orchestrateur pédagogique
         |
  Interface interne AIProvider
        / | \
   Mistral Mock Autres modèles
```

## Frontières strictes
1. **API métier** : identité, permissions, règles de partage, transitions d'état, confirmation des décisions.
2. **Moteur pédagogique** : états, scénarios, compétences, ressources et stratégie de feedback. Aucun accès privilégié.
3. **Adaptateur IA** : traduit requête/réponse structurées et métriques. Aucun droit direct d'écriture dans la base.
4. **Persistance** : PostgreSQL, ressources documentaires dans un stockage interchangeable ; backups et migrations.
5. **Infogérance** : dev local → démonstration VPS → infrastructure DSI selon validations. Infrastructure sous conteneurs ; choix final soumis à la DSI.

## Déploiement
- `.env` hors Git, exemple documenté ; secrets sur gestionnaire approprié en institution.
- Configurer fournisseurs, URLs, comptes, SSO, CORS, stockage, SMTP et observabilité par environnement.
- Migrations SQL versionnées et exports standards pour transférer les seules données autorisées.
- Authentification locale fictive uniquement en développement ; SSO institutionnel à définir.
- Images conteneurs reproductibles avec dépendances verrouillées ; CI et tests de permission avant release.

## Limitations / décisions ouvertes
- Docker Compose dev n'implique pas que la DSI accepte Compose en prod.
- Un stockage « en France » ne garantit pas à lui seul confidentialité, conformité ou souveraineté.
- Les changements de modèle exigent une comparaison pédagogique, pas seulement un test technique.
- Le prototype local A2 existe (ADR-0005) ; la pile cible ci-dessus reste proposée. Les outils de recette V0.7 en sont séparés (ADR-0006 proposé) et ne changent aucun service applicatif.

Voir `docs/adr/`.

## Extension locale de conversation — D-026

Le serveur existant sert `/coach` et les routes `conversation.v1` ; service,
fournisseur textuel et base `coach-demo.sqlite3` séparés d'A2. Mistral/Mock
interchangeables, contexte préparé après vérification SQL des droits. Aucune
récupération des traces privées A2 ou des autres conversations. Le choix reste
provisoire et décrit par [ADR-0007](adr/0007-local-conversation-mistral.md),
sans adoption de la pile institutionnelle proposée ci-dessus.
