"""V2 catalogue, workbench permissions and the boundary of coach requests."""

from pathlib import Path
import json
import tempfile
import threading
import unittest

import test_a2_http as a2_http
from ptd_coach.demo_v2 import DEMOS, PROJECTS_V2
from ptd_coach.library_v2 import WorkshopChatService, WorkshopContext, WorkshopMockProvider, catalogue_v2, projection, select_v2
from ptd_coach.project import ProjectService
from ptd_coach.server import DemoServer
from ptd_coach.service import Service
from ptd_coach.workbench import DEFAULTS, VALIDATORS, Workbench


class CatalogueV2Test(unittest.TestCase):
    def test_canonical_fiches_cover_candidate_competencies(self):
        catalogue = catalogue_v2()
        methods = catalogue["methodes"]
        self.assertEqual([m["id"] for m in methods], [f"M{i:02}" for i in range(1, 16)])
        self.assertEqual(set().union(*(set(m["competences"]) for m in methods)),
                         set("A1 A2 A3 B1 B2 B3 C1 C2 D1 D2 D3".split()))
        ids = {m["id"] for m in methods}
        for method in methods:
            with self.subTest(method=method["id"]):
                self.assertIn("Brouillon", method["statut"])
                self.assertTrue(set(method["liens"]) < ids)
                self.assertTrue(method["references"])
                self.assertTrue(all(ref["url"].startswith("https://") for ref in method["references"]))
                self.assertTrue(method["outil"] is None or method["outil"] in VALIDATORS)
                self.assertGreaterEqual(len(method["exemple"]["lignes"]), 2)
                for table in (method["exemple"], method["modele"]):
                    self.assertTrue(all(len(row) == len(table["colonnes"]) for row in table["lignes"]))
                brief = json.loads(projection(method)["content"])
                self.assertEqual(brief["version"], method["version"])
                self.assertNotIn("modele", brief)
                self.assertNotIn("lignes", brief["exemple"])
                self.assertNotIn("tuteur", brief)
                self.assertLess(len(projection(method)["content"]), 2300)

    def test_contextual_selection_and_abstention(self):
        methods = catalogue_v2()["methodes"]
        for message, expected in [
            ("On a fait un questionnaire avec des répondants volontaires.", "M14"),
            ("Nous devons répartir les rôles, qui fait quoi ?", "M11"),
            ("Le recrutement prend du retard, comment faire un planning ?", "M08"),
            ("Notre matrice de décision change suivant la pondération.", "M13"),
        ]:
            self.assertEqual(select_v2(methods, message)["id"], expected)
        self.assertIsNone(select_v2(methods, "Je suis arrivé à la salle."))
        self.assertEqual(select_v2(methods, "Et un exemple ?", [
            {"role": "user", "content": "Peux-tu expliquer la WBS ?"},
        ])["id"], "M07")

    def test_fictional_examples_validate(self):
        for team, demo in DEMOS.items():
            self.assertTrue(demo["excerpt"])
            self.assertGreater(len(PROJECTS_V2[team]["weeks"]), 6)
            for tool, example in demo.items():
                if tool in VALIDATORS:
                    self.assertEqual(VALIDATORS[tool](example), example)


class Capture(WorkshopMockProvider):
    def complete(self, messages):
        self.last_request = messages
        return super().complete(messages)


class WorkbenchV2HTTPTest(unittest.TestCase):
    request = a2_http.DemoHttpTest.request
    login = a2_http.DemoHttpTest.login
    tearDown = a2_http.DemoHttpTest.tearDown

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        project = ProjectService(root / "project.sqlite3", PROJECTS_V2)
        self.provider = Capture()
        self.chat = WorkshopChatService(root / "chat.sqlite3", self.provider, context=WorkshopContext(project))
        self.workbench = Workbench(project, DEMOS)
        self.server = DemoServer(("127.0.0.1", 0), Service(root / "a2.sqlite3"), self.chat, project, self.workbench)
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()
        self.port = self.server.server_address[1]
        self.origin = f"http://127.0.0.1:{self.port}"

    def test_two_missions_and_team_only_tools(self):
        a, b = self.login(), self.login("student_demo_02")
        c, tutor = self.login("student_demo_03"), self.login("tutor_demo_01")
        self.assertEqual(len(self.request("/api/library-v2")[2]["methodes"]), 15)
        path = "/api/workbench/gantt"
        self.assertEqual(self.request(path)[0], 401)
        self.assertEqual(self.request(path, session=tutor)[0], 403)
        self.assertEqual(self.request("/api/workbench/examples", session=tutor)[0], 403)
        example = self.request("/api/workbench/examples", session=a)[2]
        second = self.request("/api/workbench/examples", session=c)[2]
        self.assertNotEqual(example["excerpt"], second["excerpt"])
        command = {"version": 0, "data": example["gantt"]}
        self.assertEqual(self.request(path, "POST", command, tutor)[0], 403)
        self.assertEqual(self.request(path, "POST", command, a, {"X-CSRF-Token": "bad"})[0], 403)
        for _ in range(2):
            status, _, result = self.request(path, "POST", command, a)
            self.assertEqual(status, 200, result)
            self.assertEqual(result["version"], 1)
        self.assertEqual(self.request(path, session=b)[2]["data"], example["gantt"])
        self.assertEqual(self.request(path, session=c)[2]["data"], DEFAULTS["gantt"])
        different = {"version": 0, "data": second["gantt"]}
        self.assertEqual(self.request(path, "POST", different, b)[0], 409)
        self.assertEqual(self.request(path, "POST", different, c)[0], 200)

    def test_reference_and_reported_decision_require_explicit_provenance(self):
        a = self.login()
        path = "/api/workbench/specification"
        spec = DEMOS["team_demo_01"]["specification"]
        versioned = {"sections": spec["sections"], "reference": {"sections": spec["sections"], "source": "Relecture fictive du jeudi"}}
        result = self.request(path, "POST", {"version": 0, "data": versioned}, a)
        self.assertEqual(result[0], 200, result[2])
        self.assertEqual(self.request(path, "POST", {"version": 1, "data": spec}, a)[0], 409)
        evolved = {**versioned, "sections": {**versioned["sections"], "scope": "Périmètre à renégocier"}}
        self.assertEqual(self.request(path, "POST", {"version": 1, "data": evolved}, a)[0], 200)
        self.assertEqual(self.request(path, session=a)[2]["data"]["reference"], versioned["reference"])
        draft = {"rows": [{"type": "Prise", "statement": "Déployer", "rationale": "", "authority": "", "source": "", "next": ""}]}
        self.assertEqual(self.request("/api/workbench/decisions", "POST", {"version": 0, "data": draft}, a)[0], 400)

    def test_submitted_excerpt_enters_only_its_authorized_thread(self):
        a, b = self.login(), self.login("student_demo_02")
        calendar = {"start": "", "end": "", "sessions": "TEXTE ATELIER NON TRANSMIS"}
        self.assertEqual(self.request("/api/workbench/calendar", "POST", {"version": 0, "data": calendar}, a)[0], 200)
        status, _, thread = self.request("/api/coach/conversations", "POST", {
            "scope": "individual", "synthetic_confirmed": True, "coach_version": "v08",
        }, a)
        self.assertEqual(status, 201, thread)
        path = "/api/coach/conversations/" + thread["id"]
        excerpt = "Notre questionnaire serait représentatif."
        command = {"excerpt": excerpt, "version": thread["version"], "kind": "Méthode d’enquête"}
        self.assertEqual(self.request(path + "/review", "POST", command, a)[0], 400)
        self.assertFalse(hasattr(self.provider, "last_request"))
        command["synthetic_confirmed"] = True
        self.assertEqual(self.request(path + "/review", "POST", command, b)[0], 404)
        status, _, reply = self.request(path + "/review", "POST", command, a)
        self.assertEqual(status, 200, reply)
        self.assertEqual(reply["invocations"][0]["resource_ids"], ["M14"])
        self.assertEqual(reply["invocations"][0]["prompt_version"], "review-ptd-v2-experimental-0.3")
        self.assertIn(excerpt, self.provider.last_request[-1]["content"])
        self.assertNotIn(calendar["sessions"], str(self.provider.last_request))
        self.assertEqual(self.request(path, session=b)[0], 404)
        self.assertEqual(self.request(path + "/export", session=self.login("tutor_demo_01"))[0], 403)

    def test_invalid_workbench_input_does_not_persist(self):
        a = self.login()
        path = "/api/workbench/calendar"
        raw = b'{"version":0,"data":{"start":"","end":"","sessions":"\\ud800"}}'
        self.assertEqual(self.request(path, "POST", session=a, raw=raw)[0], 400)
        self.assertEqual(self.request(path, session=a)[2]["version"], 0)
