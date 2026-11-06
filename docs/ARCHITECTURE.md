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
- L'application n'est pas encore développée et le diagramme ci-dessus n'est pas une preuve de faisabilité validée.

Voir `docs/adr/`.
