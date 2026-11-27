"""Text conversation via the official Albert API endpoint."""

import json
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener

from .chat_provider import Completion, NoRedirect
from .service import DomainError


ENDPOINT = "https://albert.api.etalab.gouv.fr/v1/chat/completions"
DEFAULT_MODEL = "openai/gpt-oss-120b"


class AlbertChatProvider:
    name = "albert"

    def __init__(self, api_key, model, max_tokens, timeout):
        self._api_key = api_key
        self.model, self.max_tokens, self.timeout = model, max_tokens, timeout

    @property
    def configured(self):
        return bool(self._api_key)

    def complete(self, messages):
        if not self.configured:
            raise DomainError(503, "missing_key", "Ajoutez ALBERT_API_KEY dans .env puis redémarrez le serveur.")
        payload = {"model": self.model, "messages": messages, "temperature": 0.2,
                   "max_tokens": self.max_tokens, "stream": False}
        request = Request(ENDPOINT, data=json.dumps(payload, ensure_ascii=False).encode(),
                          headers={"Authorization": "Bearer " + self._api_key,
                                   "Content-Type": "application/json"}, method="POST")
        started = time.monotonic()
        try:
            with build_opener(NoRedirect()).open(request, timeout=self.timeout) as response:
                content = response.read(2_000_001)
            if len(content) > 2_000_000:
                raise ValueError("oversized")
            return parse_completion(json.loads(content), round(1000 * (time.monotonic() - started)))
        except HTTPError as error:
            status = error.code
            if error.fp is not None:
                error.close()
            if status in (401, 403):
                message = "Albert API refuse la clé ou les droits. Vérifiez la configuration locale."
            elif status == 429:
                message = "Quota ou limite Albert API atteinte. Aucun nouvel essai automatique."
            elif status in (404, 422):
                message = "Modèle ou paramètres refusés par Albert API. Vérifiez ALBERT_MODEL et le catalogue du compte."
            else:
                message = "Albert API est indisponible ou refuse la requête. Aucun nouvel essai automatique."
            raise DomainError(502, "albert_http_error", message) from None
        except (URLError, OSError):
            raise DomainError(504, "albert_network_error",
                              "L’appel à Albert API n’a pas abouti. Aucun nouvel essai automatique.") from None
        except (ValueError, KeyError, IndexError, TypeError, AttributeError):
            raise DomainError(502, "albert_invalid_response",
                              "Réponse Albert API inexploitable. Aucun nouvel essai automatique.") from None


def parse_completion(raw, latency_ms):
    choice = raw["choices"][0]
    message = choice["message"]
    if message.get("tool_calls") or message.get("function_call"):
        raise ValueError("unexpected tool call")
    answer = message.get("content")
    finish = choice.get("finish_reason") or "unknown"
    if finish == "length" and (answer is None or isinstance(answer, str) and not answer.strip()):
        raise DomainError(502, "albert_output_limit",
                          "Albert API a atteint le plafond sans produire de réponse finale.")
    model = raw.get("model")
    if not isinstance(answer, str) or not answer.strip() or len(answer) > 30000 or not isinstance(model, str) or not model:
        raise ValueError("missing or invalid text/model")
    source_usage = raw.get("usage") or {}
    usage = {key: source_usage.get(key) for key in ("prompt_tokens", "completion_tokens", "total_tokens")}
    if any(value is not None and (type(value) is not int or value < 0) for value in usage.values()):
        raise ValueError("invalid usage")
    return Completion(answer.strip(), model, usage, latency_ms, finish)
