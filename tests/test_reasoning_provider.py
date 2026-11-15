import json
import unittest
from unittest.mock import patch
from ptd_coach.chat_provider_reasoning import MistralReasoningProvider
from ptd_coach.service import DomainError

class Response:
    def __init__(self, data): self.data = json.dumps(data).encode()
    def __enter__(self): return self
    def __exit__(self, *args): pass
    def read(self, size): return self.data

class FakeOpener:
    def __init__(self, raw): self.raw = raw; self.request = None
    def open(self, req, timeout): self.request = req; return Response(self.raw)

def raw(content, finish='stop'):
    return {'model':'mistral-large-4', 'choices':[{'message':{'content':content},'finish_reason':finish}],
            'usage':{'prompt_tokens':10,'completion_tokens':20,'total_tokens':30}}

class ReasoningTest(unittest.TestCase):
    def provider(self): return MistralReasoningProvider('test-key','mistral-large-4',700,45,'low')
    def test_drops_thinking_and_sends_effort(self):
        opener = FakeOpener(raw([{'type':'thinking','thinking':'private'}, {'type':'text','text':'Bonjour.'}]))
        with patch('ptd_coach.chat_provider_reasoning.build_opener', return_value=opener):
            result=self.provider().complete([{'role':'user','content':'bonjour'}])
        self.assertEqual(result.message,'Bonjour.')
        self.assertNotIn('private',repr(result))
        self.assertEqual(json.loads(opener.request.data)['reasoning_effort'],'low')
        self.assertEqual(result.usage['total_tokens'],30)
    def test_no_final_text_reports_reasoning_limit_without_retry(self):
        opener=FakeOpener(raw([{'type':'thinking','thinking':'private'}], 'length'))
        with patch('ptd_coach.chat_provider_reasoning.build_opener', return_value=opener) as mock:
            with self.assertRaises(DomainError) as error: self.provider().complete([])
        self.assertEqual(error.exception.code,'mistral_reasoning_limit')
        self.assertEqual(mock.call_count,1)
    def test_invalid_effort_rejected(self):
        with self.assertRaises(ValueError): MistralReasoningProvider('key','mistral-large-4',effort='none')

    def test_factory_keeps_other_models_on_historical_provider(self):
        from ptd_coach.chat_config import provider_from_settings
        from ptd_coach.chat_provider import MistralChatProvider
        config={'CHAT_PROVIDER':'mistral','MISTRAL_API_KEY':'test','MISTRAL_MODEL':'mistral-large-4',
                'CHAT_MAX_TOKENS':700,'CHAT_TIMEOUT_SECONDS':45,'MISTRAL_REASONING_EFFORT':'low'}
        self.assertIsInstance(provider_from_settings(config), MistralReasoningProvider)
        config['MISTRAL_MODEL']='mistral-small-latest'
        self.assertIs(type(provider_from_settings(config)), MistralChatProvider)

    def test_flash_config_uses_its_own_efforts_and_keeps_output_cap(self):
        from pathlib import Path
        from tempfile import TemporaryDirectory
        from ptd_coach.__main__ import apply_test_output_policy
        from ptd_coach.chat_config import provider_from_settings, settings

        config = {"CHAT_PROVIDER": "mistral", "MISTRAL_API_KEY": "test-key",
                  "MISTRAL_MODEL": "zai-glm-5-3-flash", "MISTRAL_REASONING_EFFORT": "max",
                  "CHAT_MAX_TOKENS": "2000"}
        with TemporaryDirectory() as directory, patch.dict("os.environ", config, clear=True):
            root = Path(directory)
            provider = provider_from_settings(settings(root))
            with patch.dict("os.environ", {"MISTRAL_REASONING_EFFORT": "medium"}):
                with self.assertRaises(ValueError):
                    settings(root)

        with self.assertRaises(ValueError):
            apply_test_output_policy(provider, True, True)
        response = raw([{"type": "thinking", "thinking": "private"}, {"type": "text", "text": "Bonjour."}])
        response["model"] = config["MISTRAL_MODEL"]
        opener = FakeOpener(response)
        with patch("ptd_coach.chat_provider_reasoning.build_opener", return_value=opener):
            result = provider.complete([{"role": "user", "content": "Bonjour"}])
        request = json.loads(opener.request.data)
        self.assertEqual((request["model"], request["reasoning_effort"], request["max_tokens"]),
                         (config["MISTRAL_MODEL"], "max", 2000))
        self.assertEqual(result.message, "Bonjour.")

    def test_tool_calls_rejected(self):
        data=raw([{'type':'text','text':'Réponse'}])
        data['choices'][0]['message']['tool_calls']=[{'id':'forbidden'}]
        with patch('ptd_coach.chat_provider_reasoning.build_opener', return_value=FakeOpener(data)):
            with self.assertRaises(DomainError) as error: self.provider().complete([])
        self.assertEqual(error.exception.code,'mistral_invalid_response')

    def test_experimental_none_omits_max_tokens(self):
        opener = FakeOpener(raw([{'type':'text','text':'Bonjour.'}]))
        provider = MistralReasoningProvider('test-key','mistral-large-4',None,45,'high')
        with patch('ptd_coach.chat_provider_reasoning.build_opener', return_value=opener):
            provider.complete([{'role':'user','content':'bonjour'}])
        payload = json.loads(opener.request.data)
        self.assertNotIn('max_tokens', payload)
        self.assertEqual(payload['reasoning_effort'],'high')
