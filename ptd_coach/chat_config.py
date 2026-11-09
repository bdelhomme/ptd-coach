"""Local-only settings; secrets are never part of public configuration."""

import os
import re

from .chat_provider import MistralChatProvider, MockChatProvider


def settings(root):
    values = {"CHAT_PROVIDER": "mistral", "MISTRAL_API_KEY": "",
              "MISTRAL_MODEL": "mistral-small-latest", "CHAT_MAX_TOKENS": "700",
              "CHAT_TIMEOUT_SECONDS": "45", "CHAT_MAX_CALLS": "100"}
    path = root / ".env"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.lstrip().startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                if key.strip() in values:
                    values[key.strip()] = value.strip().strip("\"'")
    for key in values:
        values[key] = os.environ.get(key, values[key])
    if values["CHAT_PROVIDER"] not in ("mock", "mistral"):
        raise ValueError("CHAT_PROVIDER doit être mock ou mistral")
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:/-]{0,119}", values["MISTRAL_MODEL"]):
        raise ValueError("MISTRAL_MODEL invalide")
    for key, lower, upper in (("CHAT_MAX_TOKENS", 128, 2048), ("CHAT_TIMEOUT_SECONDS", 5, 90),
                              ("CHAT_MAX_CALLS", 1, 10000)):
        try:
            values[key] = int(values[key])
            if not lower <= values[key] <= upper:
                raise ValueError()
        except ValueError:
            raise ValueError(key + " hors limites") from None
    return values


def provider_from_settings(values):
    if values["CHAT_PROVIDER"] == "mock":
        return MockChatProvider()
    return MistralChatProvider(values["MISTRAL_API_KEY"], values["MISTRAL_MODEL"],
                               values["CHAT_MAX_TOKENS"], values["CHAT_TIMEOUT_SECONDS"])
