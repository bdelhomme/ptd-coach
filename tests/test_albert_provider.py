"""Exercise the Albert provider without sending any requests."""
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import HTTPError

from ptd_coach.chat_config import provider_from_settings, settings
from ptd_coach.chat_provider_albert import AlbertChatProvider, parse_completion
from ptd_coach.chat_service import ChatService
from ptd_coach.service import DomainError


class AlbertProviderTests(unittest.TestCase):
    model = "deepseek-v4-flash-0731"

    def test_selected_model_uses_albert_and_records_only_final_content(self):
        with tempfile.TemporaryDirectory() as tmp, patch.dict(os.environ, {
                "CHAT_PROVIDER": "albert", "ALBERT_API_KEY": "FAKE_ALBERT_KEY",
                "ALBERT_MODEL": self.model, "CHAT_MAX_TOKENS": "",
                "MISTRAL_REASONING_EFFORT": "invalid-for-mistral",
        }):
            root = Path(tmp)
            provider = provider_from_settings(settings(root, v2=True))
            self.assertEqual(provider.max_tokens, 2000)
            config = ChatService(root / "chat.sqlite3", provider).public_config()
            self.assertEqual((config["provider"], config["model"]), ("albert", self.model))
            self.assertNotIn("FAKE_ALBERT_KEY", json.dumps(config))
            with patch("ptd_coach.chat_provider_albert.build_opener") as opener:
                http = opener.return_value.open
                http.return_value.__enter__.return_value.read.return_value = json.dumps({
                    "model": self.model,
                    "choices": [{"message": {"content": "Réponse finale.", "reasoning_content": "Interne."},
                                 "finish_reason": "stop"}],
                    "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
                }).encode()
                messages = [{"role": "user", "content": "Cas fictif."}]
                result = provider.complete(messages)
                request = http.call_args.args[0]
                self.assertEqual(request.full_url, "https://albert.api.etalab.gouv.fr/v1/chat/completions")
                self.assertEqual(request.get_header("Authorization"), "Bearer FAKE_ALBERT_KEY")
                self.assertEqual(json.loads(request.data), {"model": self.model, "messages": messages,
                                                            "temperature": 0.2, "stream": False, "max_tokens": 2000})
                self.assertEqual((result.message, result.usage["total_tokens"]), ("Réponse finale.", 15))

    def test_missing_key_and_model_rejection_never_fall_back(self):
        with patch("ptd_coach.chat_provider_albert.build_opener") as opener:
            with self.assertRaises(DomainError) as missing:
                AlbertChatProvider("", self.model, 2000, 45).complete([])
            self.assertIn("ALBERT_API_KEY", missing.exception.message)
            opener.assert_not_called()
            http = opener.return_value.open
            http.side_effect = HTTPError("https://albert.api.etalab.gouv.fr", 404, "PRIVATE_BODY", {}, None)
            with self.assertRaises(DomainError) as rejected:
                AlbertChatProvider("FAKE_ALBERT_KEY", self.model, 2000, 45).complete([])
            self.assertEqual(rejected.exception.code, "albert_http_error")
            self.assertNotIn("PRIVATE_BODY", rejected.exception.message)
            http.assert_called_once()

    def test_reasoning_reaches_length_limit_before_any_final_text(self):
        with self.assertRaises(DomainError) as exhausted:
            parse_completion({"choices": [{"finish_reason": "length", "message": {
                "content": None, "reasoning_content": "Interne.",
            }}]}, 33000)
        self.assertEqual(exhausted.exception.code, "albert_output_limit")
        self.assertNotIn("Interne.", exhausted.exception.message)
