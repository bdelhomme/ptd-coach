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


def main():
    parser = argparse.ArgumentParser(description="PTD Coach — démo locale, données fictives uniquement")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--bibliotheque-experimentale", action="store_true", help="Coach bibliothèque isolé, base locale distincte")
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("Choose a port between 1024 and 65535")
    root = Path(__file__).resolve().parents[1]
    configuration(root)
    local = root / "local-data"
    local.mkdir(mode=0o700, exist_ok=True)
    service = Service(local / "a2-demo.sqlite3")
    chat_settings = settings(root)
    context = None
    database = local / "coach-demo.sqlite3"
    if args.bibliotheque_experimentale:
        from .chat_context_library import LibraryContext
        context = LibraryContext()
        database = local / "coach-library-experimental.sqlite3"
        print("Coach bibliothèque expérimental : base et conversations séparées.", flush=True)
    chat = ChatService(database, provider_from_settings(chat_settings),
                       max_calls=chat_settings["CHAT_MAX_CALLS"], context=context)
    with DemoServer(("127.0.0.1", args.port), service, chat) as server:
        print("PTD Coach — conversation fictive : http://127.0.0.1:{}/coach".format(args.port), flush=True)
        print("Fournisseur conversation : {} ; modèle : {} ; clé configurée : {}".format(
            chat.provider.name, chat.provider.model, "oui" if chat.provider.configured else "non"), flush=True)
        print("Prototype A2 conservé, fournisseur simulé : http://127.0.0.1:{}".format(args.port), flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nDémonstration arrêtée.")


if __name__ == "__main__":
    main()
