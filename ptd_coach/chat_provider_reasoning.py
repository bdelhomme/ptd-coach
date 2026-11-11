"""Opt-in Large 4 provider; preserves the frozen legacy provider unchanged."""
import json
import socket
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, build_opener

from .chat_provider import Completion, ENDPOINT, MistralChatProvider, NoRedirect
from .service import DomainError


class MistralReasoningProvider(MistralChatProvider):
    def __init__(self, api_key, model, max_tokens=700, timeout=45, effort='low'):
        super().__init__(api_key, model, max_tokens, timeout)
        if effort not in ('low', 'medium', 'high'):
            raise ValueError('MISTRAL_REASONING_EFFORT doit être low, medium ou high')
        self.effort = effort

    def complete(self, messages):
        if not self.configured:
            raise DomainError(503, 'missing_key', 'Ajoutez MISTRAL_API_KEY dans .env local.')
        payload = {'model': self.model, 'messages': messages, 'temperature': 0.2,
                   'stream': False, 'tool_choice': 'none', 'reasoning_effort': self.effort}
        # None is reserved for explicitly authorized experiments: omit the parameter.
        if self.max_tokens is not None:
            payload['max_tokens'] = self.max_tokens
        request = Request(ENDPOINT, data=json.dumps(payload, ensure_ascii=False).encode(),
                          headers={'Authorization': 'Bearer ' + self._api_key,
                                   'Content-Type': 'application/json'}, method='POST')
        started = time.monotonic()
        try:
            with build_opener(NoRedirect()).open(request, timeout=self.timeout) as response:
                content = response.read(2_000_001)
            if len(content) > 2_000_000:
                raise ValueError('oversized')
            raw = json.loads(content); choice = raw['choices'][0]; msg = choice['message']
            if msg.get('tool_calls'):
                raise ValueError('tools forbidden')
            answer = msg.get('content')
            if isinstance(answer, list):
                answer = ''.join(c.get('text', '') for c in answer if isinstance(c, dict) and c.get('type') == 'text')
            if not isinstance(answer, str) or not answer.strip():
                if choice.get('finish_reason') == 'length':
                    raise DomainError(502, 'mistral_reasoning_limit', 'La limite de sortie a été atteinte avant la réponse finale. Aucun nouvel appel automatique.')
                raise ValueError('missing answer')
            if len(answer) > 30000 or not isinstance(raw.get('model'), str) or not raw['model']:
                raise ValueError('invalid model or answer')
            usage = {}
            for key in ('prompt_tokens', 'completion_tokens', 'total_tokens'):
                value = (raw.get('usage') or {}).get(key)
                if value is not None and (type(value) is not int or value < 0):
                    raise ValueError('invalid usage')
                usage[key] = value
            # Reasoning blocks are deliberately discarded: only final text enters history.
            return Completion(answer.strip(), raw['model'], usage,
                              round(1000 * (time.monotonic() - started)), choice.get('finish_reason', 'unknown'))
        except HTTPError as error:
            if error.code in (401, 403):
                message = 'Mistral refuse la clé ou les droits API. Vérifiez la configuration locale.'
            elif error.code == 429:
                message = 'Quota ou limite Mistral atteinte. Aucun nouvel essai automatique.'
            else:
                message = 'Mistral est indisponible ou refuse la requête. Aucun nouvel essai automatique.'
            raise DomainError(502, 'mistral_http_error', message) from None
        except (TimeoutError, socket.timeout, URLError, OSError):
            raise DomainError(504, 'mistral_network_error', 'Appel Mistral interrompu ; facturation inconnue. Aucun nouvel essai automatique.') from None
        except (ValueError, KeyError, IndexError, TypeError, AttributeError):
            raise DomainError(502, 'mistral_invalid_response', 'Réponse Mistral inexploitable ; aucun nouvel essai automatique.') from None
