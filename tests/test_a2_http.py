"""HTTP integration with independent fictitious sessions and a temporary DB."""

import http.client
import json
from pathlib import Path
import tempfile
import threading
import unittest
import uuid
from unittest.mock import patch

from ptd_coach.__main__ import configuration
from ptd_coach.server import DemoServer
from ptd_coach.service import Service


class DemoHttpTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.service = Service(Path(self.temp.name) / "http.sqlite3")
        self.server = DemoServer(("127.0.0.1", 0), self.service)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.port = self.server.server_address[1]
        self.origin = "http://127.0.0.1:" + str(self.port)

    def tearDown(self):
        self.server.shutdown()
        self.server.server_close()
        self.thread.join(timeout=2)
        self.temp.cleanup()

    def request(self, path, method="GET", payload=None, session=None, extra=None, raw=None):
        headers = {}
        if method != "GET":
            headers.update({"Content-Type": "application/json", "Origin": self.origin,
                            "Idempotency-Key": str(uuid.uuid4())})
        if session:
            headers.update({"Cookie": session["cookie"], "X-CSRF-Token": session["csrf"]})
        headers.update(extra or {})
        body = raw if raw is not None else json.dumps(payload).encode() if payload is not None else None
        connection = http.client.HTTPConnection("127.0.0.1", self.port, timeout=5)
        connection.request(method, path, body=body, headers=headers)
        response = connection.getresponse()
        status, result_headers, content = response.status, dict(response.getheaders()), response.read()
        connection.close()
        value = json.loads(content) if result_headers.get("Content-Type", "").startswith("application/json") else content.decode()
        return status, result_headers, value

    def login(self, user="student_demo_01"):
        status, headers, data = self.request("/api/demo-session", "POST", {"user_id": user})
        self.assertEqual(status, 200)
        return {"cookie": headers["Set-Cookie"].split(";")[0], "csrf": data["csrf"]}

    def test_health_static_assets_and_private_routes_require_session(self):
        self.assertEqual(self.request("/api/health")[2]["provider"], "mock")
        for asset in ["/", "/style.css", "/app.js"]:
            status, headers, content = self.request(asset)
            self.assertEqual(status, 200)
            self.assertTrue(content)
            self.assertIn("frame-ancestors 'none'", headers["Content-Security-Policy"])
        self.assertEqual(self.request("/api/cycles")[0], 401)
        self.assertEqual(self.request("/.git/config")[0], 401)

    def test_cookie_session_creation_and_logout(self):
        status, headers, result = self.request("/api/demo-session", "POST", {"user_id": "student_demo_01"})
        self.assertIn("HttpOnly", headers["Set-Cookie"])
        self.assertIn("SameSite=Strict", headers["Set-Cookie"])
        session = {"cookie": headers["Set-Cookie"].split(";")[0], "csrf": result["csrf"]}
        self.assertEqual(self.request("/api/me", session=session)[2]["user"]["id"], "student_demo_01")
        self.assertEqual(self.request("/api/demo-session", "DELETE", session=session)[0], 200)
        self.assertEqual(self.request("/api/me", session=session)[0], 401)

    def test_cross_origin_wrong_host_and_csrf_are_rejected(self):
        self.assertEqual(self.request("/api/demo-session", "POST", {"user_id": "student_demo_01"}, extra={"Origin": "https://example.invalid"})[0], 403)
        self.assertEqual(self.request("/api/health", extra={"Host": "example.invalid"})[0], 403)
        session = self.login()
        self.assertEqual(self.request("/api/cycles", "POST", {"case_id": "client-delay"}, session, {"X-CSRF-Token": "wrong"})[0], 403)
        self.assertEqual(self.service.cycles("student_demo_01"), [])

    def test_http_student_and_tutor_isolation_including_export(self):
        a, b, tutor = self.login(), self.login("student_demo_02"), self.login("tutor_demo_01")
        status, headers, cycle = self.request("/api/cycles", "POST", {"case_id": "client-delay"}, a)
        self.assertEqual(status, 201)
        path = "/api/cycles/" + cycle["id"]
        self.assertEqual(self.request(path, session=a)[0], 200)
        self.assertEqual(self.request(path, session=b)[0], 404)
        self.assertEqual(self.request(path + "/export", session=tutor)[0], 403)
        self.assertEqual(self.request(path + "/actions", "POST", {"action": "learn", "version": 1, "fields": {}}, tutor)[0], 403)
        self.assertEqual(self.request("/api/shares", session=tutor)[2], [])
        self.assertIn("attachment", self.request(path + "/export", session=a)[1]["Content-Disposition"])

    def test_malformed_and_oversized_requests_are_controlled(self):
        session = self.login()
        self.assertEqual(self.request("/api/cycles", "POST", session=session, raw=b"{")[0], 400)
        self.assertEqual(self.request("/api/cycles", "POST", session=session, raw=b"[]")[0], 400)
        self.assertEqual(self.request("/api/cycles", "POST", {"case_id": "client-delay"}, session, {"Content-Type": "text/plain"})[0], 415)
        self.assertEqual(self.request("/api/cycles", "POST", session=session, raw=b" " * 32001)[0], 413)

    def test_fictitious_login_rejects_unknown_identity_and_privilege_injection(self):
        self.assertEqual(self.request("/api/demo-session", "POST", {"user_id": "unknown"})[0], 400)
        self.assertEqual(self.request("/api/demo-session", "POST", {"user_id": "student_demo_01", "role": "admin"})[0], 400)
        with self.assertRaises(ValueError):
            DemoServer(("0.0.0.0", 0), self.service)

    def test_configuration_refuses_non_demo_or_real_provider(self):
        root = Path(self.temp.name)
        with patch.dict("os.environ", {"APP_ENV": "development", "AI_PROVIDER": "mock"}):
            self.assertEqual(configuration(root)["AI_PROVIDER"], "mock")
        for overrides in [{"APP_ENV": "production"}, {"AI_PROVIDER": "mistral"}]:
            with patch.dict("os.environ", overrides):
                with self.assertRaises(ValueError):
                    configuration(root)


if __name__ == "__main__":
    unittest.main()
