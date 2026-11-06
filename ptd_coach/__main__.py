"""Run with python -m ptd_coach. Loopback and fictitious accounts only."""

import argparse
import os
from pathlib import Path

from .server import DemoServer
from .service import Service


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
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("Choose a port between 1024 and 65535")
    root = Path(__file__).resolve().parents[1]
    configuration(root)
    local = root / "local-data"
    local.mkdir(mode=0o700, exist_ok=True)
    service = Service(local / "a2-demo.sqlite3")
    with DemoServer(("127.0.0.1", args.port), service) as server:
        print("PTD Coach — démo fictive, coach simulé : http://127.0.0.1:{}".format(args.port), flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            print("\nDémonstration arrêtée.")


if __name__ == "__main__":
    main()
