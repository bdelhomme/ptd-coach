# Infrastructure — à construire

Ne pas présenter ce répertoire comme un environnement Docker opérationnel. Les futures configurations `compose.yaml`, Dockerfiles, devcontainer, migrations, CI applicative, sauvegardes et scripts de déploiement seront ajoutés après l'arbitrage de la pile et des exigences DSI.

Un socle documentaire local et une CI de contrôle du dépôt sont disponibles :
voir [DEVELOPMENT.md](../docs/DEVELOPMENT.md). Ils ne constituent pas
l'environnement applicatif ou de déploiement décrit ci-dessus.

Critère de réussite : un développeur tiers déploie le même code avec données fictives en local puis sur serveur Linux, sans connaître l'auteur initial.
