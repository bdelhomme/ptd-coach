"""Text-only conversational providers. No tools, writes or automatic retries."""

from dataclasses import dataclass
import json
import socket
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener, HTTPRedirectHandler

from .service import DomainError


ENDPOINT = "https://api.mistral.ai/v1/chat/completions"


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        # Never forward the Authorization header to a redirected host.
        return None


@dataclass(frozen=True)
class Completion:
    message: str
    model_returned: str
    usage: dict
    latency_ms: int = 0
    finish_reason: str = "stop"


class MistralChatProvider:
    name = "mistral"

    def __init__(self, api_key, model="mistral-small-latest", max_tokens=700, timeout=45):
        self._api_key = api_key
        self.model, self.max_tokens, self.timeout = model, max_tokens, timeout

    @property
    def configured(self):
        return bool(self._api_key)

    def complete(self, messages):
        if not self.configured:
            raise DomainError(503, "missing_key", "Ajoutez MISTRAL_API_KEY dans le fichier .env local, puis redémarrez le serveur.")
        payload = {"model": self.model, "messages": messages, "temperature": 0.2,
                   "max_tokens": self.max_tokens, "stream": False, "tool_choice": "none"}
        request = Request(ENDPOINT, data=json.dumps(payload, ensure_ascii=False).encode(),
                          headers={"Authorization": "Bearer " + self._api_key,
                                   "Content-Type": "application/json"}, method="POST")
        started = time.monotonic()
        try:
            with build_opener(NoRedirect()).open(request, timeout=self.timeout) as response:
                content = response.read(2_000_001)
            if len(content) > 2_000_000:
                raise ValueError("oversized")
            raw = json.loads(content)
            choice = raw["choices"][0]
            answer = choice["message"].get("content")
            if isinstance(answer, list):
                answer = "\n".join(chunk["text"] for chunk in answer
                                   if isinstance(chunk, dict) and chunk.get("type") == "text")
            if not isinstance(answer, str) or not answer.strip() or len(answer) > 30000:
                raise ValueError("invalid answer")
            if choice["message"].get("tool_calls"):
                raise ValueError("tools forbidden")
            model = raw.get("model")
            if not isinstance(model, str) or not model:
                raise ValueError("missing model")
            source_usage = raw.get("usage") or {}
            usage = {}
            for key in ("prompt_tokens", "completion_tokens", "total_tokens"):
                value = source_usage.get(key)
                if value is not None and (type(value) is not int or value < 0):
                    raise ValueError("invalid usage")
                usage[key] = value
            return Completion(answer.strip(), model, usage,
                              round(1000 * (time.monotonic() - started)),
                              choice.get("finish_reason", "unknown"))
        except HTTPError as error:
            if error.code in (401, 403):
                message = "Mistral refuse la clé ou les droits API. Vérifiez la configuration locale."
            elif error.code == 429:
                message = "Quota ou limite Mistral atteinte. Aucun nouvel essai automatique."
            else:
                message = "Mistral est indisponible ou refuse la requête. Aucun nouvel essai automatique."
            raise DomainError(502, "mistral_http_error", message) from None
        except (TimeoutError, socket.timeout, URLError, OSError):
            raise DomainError(504, "mistral_network_error", "L'appel Mistral n'a pas abouti. La facturation peut être inconnue ; aucun nouvel essai automatique.") from None
        except (ValueError, KeyError, IndexError, TypeError, AttributeError):
            raise DomainError(502, "mistral_invalid_response", "Réponse Mistral inexploitable ; aucun nouvel essai automatique.") from None


class MockChatProvider:
    name = "mock"
    model = "mock-conversation-v1"
    max_tokens = 0
    configured = True

    def complete(self, messages):
        return Completion(
            "[Simulation hors réseau] Je peux vous aider à clarifier une méthode, préparer une action ou examiner une expérience. "
            "Les ressources R01–R03 sont disponibles ci-dessous. Cette réponse fixe ne permet pas d'évaluer la pertinence de Mistral.",
            self.model, {"prompt_tokens": None, "completion_tokens": None, "total_tokens": None})
