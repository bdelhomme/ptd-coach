"""Run with python -m ptd_coach. Loopback and fictitious accounts only."""

import argparse
import os
from pathlib import Path

from .server import DemoServer
from .service import Service
from .chat_config import settings, provider_from_settings
from .chat_service import ChatService


def configuration(root):
    config = {"APP_ENV": "development", "AI_PROVIDER": "mock"}
    env = root / ".env"
    if env.exists():
        for line in env.read_text().splitlines():
            if line.strip() and not line.lstrip().startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                if key.strip() in config:
                    config[key.strip()] = value.strip()
    for key in config:
        config[key] = os.environ.get(key, config[key])
    if config != {"APP_ENV": "development", "AI_PROVIDER": "mock"}:
        raise ValueError("Only APP_ENV=development and AI_PROVIDER=mock are supported")
    return config


def apply_test_output_policy(provider, uncapped, reliability):
    if uncapped:
        from .chat_provider_reasoning import MistralReasoningProvider
        if not reliability or not isinstance(provider, MistralReasoningProvider):
            raise ValueError("Sans plafond réservé au cadrage de fiabilité et à Mistral Large 4")
        provider.max_tokens = None
    return provider


def main():
    parser = argparse.ArgumentParser(description="PTD Coach — démo locale, données fictives uniquement")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--bibliotheque-experimentale", action="store_true", help="Coach bibliothèque isolé, base locale distincte")
    parser.add_argument("--cadrage-fiabilite", action="store_true", help="Coach de fiabilité expérimental, base séparée")
    parser.add_argument("--coach-historique", action="store_true", help="Comparaison historique V0.7/V0.8")
    parser.add_argument("--data-dir", type=Path, help="Dossier de données fictives pour une recette isolée")
    parser.add_argument("--sans-plafond-test", action="store_true", help="Ne demande pas de plafond de sortie pour ce test expérimental Large 4")
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("Choose a port between 1024 and 65535")
    root = Path(__file__).resolve().parents[1]
    configuration(root)
    local = args.data_dir if args.data_dir is not None else root / "local-data"
    local.mkdir(mode=0o700, parents=True, exist_ok=True)
    service = Service(local / "a2-demo.sqlite3")
    chat_settings = settings(root)
    context = None
    database = local / "coach-demo.sqlite3"
    project = None
    chat_class = ChatService
    alternate_modes = sum((args.bibliotheque_experimentale, args.cadrage_fiabilite, args.coach_historique))
    if alternate_modes > 1:
        parser.error("Choisissez un seul mode de comparaison")
    if args.cadrage_fiabilite:
        from .chat_context_reliable import ReliableContext
        context = ReliableContext()
        database = local / "coach-reliability-experimental.sqlite3"
        print("Coach de fiabilité expérimental : base et conversations séparées.", flush=True)
    elif args.bibliotheque_experimentale:
        from .chat_context_library import LibraryContext
        context = LibraryContext()
        database = local / "coach-library-experimental.sqlite3"
        print("Coach bibliothèque expérimental : base et conversations séparées.", flush=True)
    elif not args.coach_historique:
        from .chat_integrated import ProjectChatService, ProjectContext
        from .project import ProjectService
        project = ProjectService(local / "project-demo.sqlite3")
        context = ProjectContext(project)
        database = local / "coach-integrated-demo.sqlite3"
        chat_class = ProjectChatService
    try:
        provider = apply_test_output_policy(provider_from_settings(chat_settings), args.sans_plafond_test, args.cadrage_fiabilite)
    except ValueError as error:
        parser.error(str(error))
    if project is not None and chat_settings["CHAT_PROVIDER"] == "mock":
        from .chat_integrated import ProjectMockProvider
        provider = ProjectMockProvider()
    chat = chat_class(database, provider,
                       max_calls=chat_settings["CHAT_MAX_CALLS"], context=context)
    with DemoServer(("127.0.0.1", args.port), service, chat, project) as server:
        if project is not None:
            print(f"PTD Coach intégré : http://127.0.0.1:{args.port}/", flush=True)
        print("PTD Coach — conversation fictive : http://127.0.0.1:{}/coach".format(args.port), flush=True)
        print("Fournisseur conversation : {} ; modèle : {} ; clé configurée : {}".format(
            chat.provider.name, chat.provider.model, "oui" if chat.provider.configured else "non"), flush=True)
        print("Prototype A2 conservé, fournisseur simulé : http://127.0.0.1:{}/historique-a2".format(args.port), flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nDémonstration arrêtée.")


if __name__ == "__main__":
    main()
