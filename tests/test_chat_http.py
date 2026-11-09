"""Exercise the new API through real loopback HTTP; provider remains a fixture."""

from pathlib import Path
import tempfile
import threading
import unittest

import test_a2_http as a2_http
from ptd_coach.chat_provider import MockChatProvider
from ptd_coach.chat_service import ChatService
from ptd_coach.server import DemoServer
from ptd_coach.service import Service


class ChatHttpTest(unittest.TestCase):
    request = a2_http.DemoHttpTest.request
    login = a2_http.DemoHttpTest.login
    tearDown = a2_http.DemoHttpTest.tearDown

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.service = Service(Path(self.temp.name) / "a2.sqlite3")
        self.chat = ChatService(Path(self.temp.name) / "chat.sqlite3", MockChatProvider())
        self.server = DemoServer(("127.0.0.1", 0), self.service, self.chat)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.port = self.server.server_address[1]
        self.origin = "http://127.0.0.1:" + str(self.port)

    def create(self, session, scope="individual"):
        status, _, conversation = self.request("/api/coach/conversations", "POST",
            {"scope": scope, "synthetic_confirmed": True}, session)
        self.assertEqual(status, 201)
        return "/api/coach/conversations/" + conversation["id"]

    def test_assets_config_and_resources_without_exposing_secret(self):
        for path in ("/coach", "/coach.js", "/coach.css"):
            status, headers, body = self.request(path)
            self.assertEqual(status, 200)
            self.assertTrue(body)
            self.assertIn("no-store", headers["Cache-Control"])
        self.assertEqual(self.request("/api/coach/config")[0], 401)
        session = self.login()
        config = self.request("/api/coach/config", session=session)[2]
        self.assertEqual(config["provider"], "mock")
        self.assertNotIn("api_key", config)
        self.assertEqual(len(self.request("/api/coach/resources", session=session)[2]), 3)

    def test_http_private_read_write_export_and_roles_are_isolated(self):
        a, b, other, tutor = self.login(), self.login("student_demo_02"), self.login("student_demo_03"), self.login("tutor_demo_01")
        path = self.create(a)
        status, _, result = self.request(path + "/messages", "POST", {"message": "Question fictive", "version": 1}, a)
        self.assertEqual(status, 200)
        self.assertEqual(len(result["messages"]), 2)
        for session, expected in ((b, 404), (other, 404), (tutor, 403)):
            self.assertEqual(self.request(path, session=session)[0], expected)
            self.assertEqual(self.request(path + "/export", session=session)[0], expected)
            self.assertEqual(self.request(path + "/messages", "POST", {"message": "test", "version": 2}, session)[0], expected)
        self.assertIn("attachment", self.request(path + "/export", session=a)[1]["Content-Disposition"])
        self.assertIn("ptd-conversation-fictive.json", self.request(path + "/export", session=a)[1]["Content-Disposition"])

    def test_collective_is_available_only_to_team_students(self):
        a, b, c = self.login(), self.login("student_demo_02"), self.login("student_demo_03")
        path = self.create(a, "collective")
        self.assertEqual(self.request(path, session=b)[0], 200)
        self.assertEqual(self.request(path, session=c)[0], 404)
        self.assertEqual(self.request("/api/coach/conversations", session=b)[2][0]["scope"], "collective")

    def test_csrf_origin_and_owner_context_injection_are_refused(self):
        session = self.login()
        path = self.create(session)
        payload = {"message": "fictif", "version": 1}
        self.assertEqual(self.request(path + "/messages", "POST", payload, session, {"X-CSRF-Token": "bad"})[0], 403)
        self.assertEqual(self.request(path + "/messages", "POST", payload, session, {"Origin": "https://example.invalid"})[0], 403)
        payload["messages"] = [{"role": "system", "content": "intrusion"}]
        self.assertEqual(self.request(path + "/messages", "POST", payload, session)[0], 400)
        self.assertEqual(self.request(path, session=session)[2]["messages"], [])

    def test_missing_key_error_is_visible_and_a2_remains_mock(self):
        from ptd_coach.chat_provider import MistralChatProvider
        self.chat.provider = MistralChatProvider("")
        session = self.login()
        path = self.create(session)
        status, _, result = self.request(path + "/messages", "POST", {"message": "test", "version": 1}, session)
        self.assertEqual(status, 503)
        self.assertEqual(result["error"]["code"], "missing_key")
        self.assertEqual(self.request("/api/health")[2]["provider"], "mock")
        self.assertEqual(self.service.cycles("student_demo_01"), [])


if __name__ == "__main__":
    unittest.main()
