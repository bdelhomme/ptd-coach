"""Local-only settings; secrets are never part of public configuration."""

import os
import re

from .chat_provider import MistralChatProvider, MockChatProvider
from .chat_provider_albert import DEFAULT_MODEL as ALBERT_DEFAULT_MODEL, AlbertChatProvider


REASONING_EFFORTS = {
    "mistral-large-4": ("low", "medium", "high"),
    "mistral-large-4-0": ("low", "medium", "high"),
    "zai-glm-5-3-flash": ("low", "high", "max"),
}


def settings(root, *, v2=False, provider_override=None):
    default_model = "zai-glm-5-3-flash" if v2 else "mistral-small-latest"
    values = {"CHAT_PROVIDER": "mistral", "MISTRAL_API_KEY": "",
              "ALBERT_API_KEY": "", "ALBERT_MODEL": ALBERT_DEFAULT_MODEL,
              "MISTRAL_MODEL": default_model, "CHAT_MAX_TOKENS": "",
              "CHAT_TIMEOUT_SECONDS": "45", "CHAT_MAX_CALLS": "100",
              "MISTRAL_REASONING_EFFORT": "low"}
    path = root / ".env"
    if path.exists():
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.lstrip().startswith("#") and "=" in line:
                key, value = line.split("=", 1)
                if key.strip() in values:
                    values[key.strip()] = value.strip().strip("\"'")
    for key in values:
        values[key] = os.environ.get(key, values[key])
    if provider_override is not None:
        values["CHAT_PROVIDER"] = provider_override
    if not values["CHAT_MAX_TOKENS"]:
        extended = values["CHAT_PROVIDER"] == "albert" or (v2 and values["MISTRAL_MODEL"] == default_model)
        values["CHAT_MAX_TOKENS"] = "2000" if extended else "700"
    provider = values["CHAT_PROVIDER"]
    if provider not in ("mock", "mistral", "albert"):
        raise ValueError("CHAT_PROVIDER doit être mock, mistral ou albert")
    model_key = "ALBERT_MODEL" if provider == "albert" else "MISTRAL_MODEL"
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.:/-]{0,119}", values[model_key]):
        raise ValueError(model_key + " invalide")
    if provider != "albert":
        efforts = REASONING_EFFORTS.get(values["MISTRAL_MODEL"], ("low", "medium", "high"))
        if values["MISTRAL_REASONING_EFFORT"] not in efforts:
            raise ValueError("MISTRAL_REASONING_EFFORT doit être " + ", ".join(efforts) + " pour ce modèle")
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
    if values["CHAT_PROVIDER"] == "albert":
        return AlbertChatProvider(values["ALBERT_API_KEY"], values["ALBERT_MODEL"],
                                  values["CHAT_MAX_TOKENS"], values["CHAT_TIMEOUT_SECONDS"])
    if values["MISTRAL_MODEL"] in REASONING_EFFORTS:
        from .chat_provider_reasoning import MistralReasoningProvider
        return MistralReasoningProvider(values["MISTRAL_API_KEY"], values["MISTRAL_MODEL"],
                                        values["CHAT_MAX_TOKENS"], values["CHAT_TIMEOUT_SECONDS"],
                                        values["MISTRAL_REASONING_EFFORT"])
    return MistralChatProvider(values["MISTRAL_API_KEY"], values["MISTRAL_MODEL"],
                               values["CHAT_MAX_TOKENS"], values["CHAT_TIMEOUT_SECONDS"])
