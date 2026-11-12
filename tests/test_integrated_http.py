"""Exercise a whole fictional semester slice through the application HTTP API."""

from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import tempfile
import threading
import unittest
import uuid

import test_a2_http as a2_http
from ptd_coach.chat_integrated import ProjectChatService, ProjectContext, ProjectMockProvider
from ptd_coach.project import ProjectService
from ptd_coach.server import DemoServer
from ptd_coach.service import Service


class CapturingProvider(ProjectMockProvider):
    def __init__(self):
        self.requests = []

    def complete(self, messages):
        self.requests.append(messages)
        return super().complete(messages)


class IntegratedHttpTest(unittest.TestCase):
    request = a2_http.DemoHttpTest.request
    login = a2_http.DemoHttpTest.login
    tearDown = a2_http.DemoHttpTest.tearDown

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.project = ProjectService(root / "project.sqlite3")
        self.provider = CapturingProvider()
        self.chat = ProjectChatService(root / "chat.sqlite3", self.provider,
                                       context=ProjectContext(self.project))
        self.server = DemoServer(("127.0.0.1", 0), Service(root / "a2.sqlite3"), self.chat, self.project)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.port = self.server.server_address[1]
        self.origin = f"http://127.0.0.1:{self.port}"

    def create_item(self, session, content, scope="collective", kind="requirement", origin="human"):
        status, _, data = self.request("/api/project", "POST", {
            "scope": scope, "kind": kind, "text": content, "source": "Atelier fictif du jeudi",
            "origin": origin,
        }, session)
        self.assertEqual(status, 201, data)
        return next(row for row in data["items"] if row["text"] == content)

    def mutate(self, session, row, action, **fields):
        return self.request(f"/api/project/items/{row['id']}/{action}", "POST",
                            {"version": row["version"], **fields}, session)

    def change(self, session, row, action, **fields):
        status, _, result = self.mutate(session, row, action, **fields)
        self.assertEqual(status, 200, result)
        return next((item for item in result["items"] if item["id"] == row["id"]), None)

    def conversation(self, session, scope, question):
        status, _, thread = self.request("/api/coach/conversations", "POST", {
            "scope": scope, "synthetic_confirmed": True, "coach_version": "v08",
        }, session)
        self.assertEqual(status, 201, thread)
        path = "/api/coach/conversations/" + thread["id"]
        status, _, response = self.request(path + "/messages", "POST",
                                           {"message": question, "version": thread["version"]}, session)
        self.assertEqual(status, 200, response)
        request = next(messages for messages in self.provider.requests if messages[-1]["content"] == question)
        return path, response, request[0]["content"]

    def test_project_from_question_to_method_to_next_week_to_tutor(self):
        self.assertIn("/ptd.js", self.request("/")[2])
        self.assertIn("/ptd.js", self.request("/coach")[2])
        self.assertEqual(self.request("/historique-a2")[0], 200)
        resources = self.request("/api/library")[2]
        self.assertEqual(len(resources), 10)
        student = self.login()
        peer = self.login("student_demo_08")
        tutor = self.login("tutor_demo_01")
        self.assertEqual(student["cookie"].split("=", 1)[0], f"ptd_demo_{self.port}")
        _, reply, _ = self.conversation(student, "collective", "Comment rédiger le cahier des charges ?")
        self.assertIn("M03", reply["invocations"][0]["resource_ids"])
        self.assertIn("M03", {resource["id"] for resource in resources})
        text = "Confirmer avec l’atelier la durée autorisée d’un prêt fictif."
        item = self.create_item(student, text, origin="ai")
        self.assertFalse(item["confirmed"])
        self.assertNotEqual(self.mutate(student, item, "share")[0], 200)
        item = self.change(peer, item, "confirm")
        self.assertTrue(item["confirmed"])
        self.assertEqual(item["confirmed_by"], "student_demo_08")
        review = self.create_item(student, "Point fictif : la question sur la durée est prête.", kind="review")
        review = self.change(student, review, "confirm")
        previous = self.request("/api/project", session=peer)[2]["project"]
        status, _, after = self.request("/api/project/next-week", "POST", {"version": previous["version"]}, peer)
        self.assertEqual(status, 200, after)
        self.assertEqual(after["project"]["current_week"], previous["current_week"] + 1)
        self.assertIn(review["id"], {r["id"] for r in after["items"]})
        _, _, context = self.conversation(peer, "collective", "Que savons-nous pour la prochaine séance ?")
        self.assertIn(text, context)
        self.assertNotIn(item["id"], {r["id"] for r in self.request("/api/project", session=tutor)[2]["items"]})
        item = self.change(student, item, "share")
        self.assertIn(item["id"], {r["id"] for r in self.request("/api/project", session=tutor)[2]["items"]})
        item = self.change(peer, item, "revoke")
        self.assertNotIn(item["id"], {r["id"] for r in self.request("/api/project", session=tutor)[2]["items"]})
        item = self.change(peer, item, "update", kind=item["kind"], text="Durée fictive corrigée", source=item["source"])
        self.assertFalse(item["confirmed"])
        _, _, context = self.conversation(student, "collective", "La durée est-elle décidée ?")
        self.assertNotIn(text, context)
        self.assertNotIn("Durée fictive corrigée", context)
        self.change(peer, item, "delete")

    def test_memory_context_and_writes_enforce_actor_scope(self):
        student = self.login()
        peer = self.login("student_demo_02")
        tutor = self.login("tutor_demo_01")
        outsiders = [self.login("student_demo_03"), self.login("tutor_demo_02"),
                     self.login("coordination_demo_01"), self.login("admin_demo_01")]
        private = self.create_item(student, "Signal privé fictif unique", scope="individual", kind="note")
        private = self.change(student, private, "confirm")
        self.assertNotEqual(self.mutate(student, private, "share")[0], 200)
        for session in [peer, tutor, *outsiders]:
            self.assertNotEqual(self.mutate(session, private, "delete")[0], 200)
            snapshot = self.request("/api/project", session=session)[2]
            self.assertNotIn(private["text"], str(snapshot))
        _, _, collective_context = self.conversation(student, "collective", "Préparer le jeudi")
        self.assertNotIn(private["text"], collective_context)
        path, _, private_context = self.conversation(student, "individual", "Reprendre ma note")
        self.assertIn(private["text"], private_context)
        self.assertEqual(self.request(path + "/export", session=tutor)[0], 403)
        self.assertEqual(self.request(path, session=peer)[0], 404)
        self.change(student, private, "delete")
        _, _, private_context = self.conversation(student, "individual", "Reprendre ma note après suppression")
        self.assertNotIn(private["text"], private_context)

    def test_concurrent_private_context_stays_with_each_student(self):
        students = [self.login(), self.login("student_demo_02")]
        markers = ["Repère privé fictif Zéphyr", "Repère privé fictif Mistral"]
        for student, marker in zip(students, markers):
            item = self.create_item(student, marker, scope="individual", kind="note")
            self.change(student, item, "confirm")

        with ThreadPoolExecutor(max_workers=2) as executor:
            first = executor.submit(self.conversation, students[0], "individual", "Préparer le premier retour")
            second = executor.submit(self.conversation, students[1], "individual", "Préparer le second retour")
        self.assertIn(markers[0], first.result()[2])
        self.assertNotIn(markers[1], first.result()[2])
        self.assertIn(markers[1], second.result()[2])
        self.assertNotIn(markers[0], second.result()[2])

    def test_get_rejects_cookie_from_another_tab_with_old_session_token(self):
        student = self.login()
        tutor = self.login("tutor_demo_01")
        status, _, error = self.request("/api/project", session=tutor, extra={"X-CSRF-Token": student["csrf"]})
        self.assertEqual(status, 403)
        self.assertEqual(error["error"]["code"], "csrf_forbidden")
        self.assertEqual(self.request("/api/project", extra={"Cookie": tutor["cookie"]})[0], 200)

    def test_create_requires_session_and_csrf_and_replays_once(self):
        self.assertEqual(self.request("/api/project")[0], 401)
        student = self.login()
        payload = {"scope": "collective", "kind": "question", "text": "Question fictive unique",
                   "source": "Séance fictive", "origin": "human"}
        self.assertEqual(self.request("/api/project", "POST", payload, student,
                                      {"X-CSRF-Token": "wrong"})[0], 403)
        self.assertEqual(self.request("/api/project", "POST", {**payload, "confirmed": True}, student)[0], 400)
        key = {"Idempotency-Key": str(uuid.uuid4())}
        for _ in range(2):
            status, _, data = self.request("/api/project", "POST", payload, student, key)
            self.assertEqual(status, 201, data)
            self.assertEqual(sum(row["text"] == payload["text"] for row in data["items"]), 1)
