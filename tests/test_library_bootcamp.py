"""Verify public, read-only practice material and its catalogue links."""

import json
import re
import threading
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen

from ptd_coach.library_v2 import catalogue_v2
from ptd_coach.server import DemoServer, WEB
from ptd_coach.workbench import VALIDATORS


class BootcampTests(unittest.TestCase):
    def test_anonymous_practice_resources_reference_existing_catalogue_and_tools(self):
        with DemoServer(("127.0.0.1", 0), None, project=object(), workbench=object()) as server:
            thread = threading.Thread(target=server.serve_forever, daemon=True)
            thread.start()
            base = f"http://127.0.0.1:{server.server_port}"
            try:
                with urlopen(base + "/bibliotheque-ptd") as response:
                    self.assertIn(b'id="boot-competences"', response.read())
                with urlopen(base + "/api/library-v2/bootcamp") as response:
                    bootcamp = json.load(response)
                    self.assertNotIn("Set-Cookie", response.headers)
                with self.assertRaises(HTTPError) as caught:
                    urlopen(Request(base + "/api/library-v2/bootcamp", method="POST", data=b"{}"))
                self.assertIn(caught.exception.code, (401, 403, 404, 405))
                with self.assertRaises(HTTPError) as caught:
                    urlopen(base + "/api/workbench/gantt")
                self.assertEqual(caught.exception.code, 401)
            finally:
                server.shutdown()
                thread.join()

        ref = WEB.parent / "pedagogy/competencies/candidate-v0.3.json"
        self.assertEqual(bootcamp["competences"], json.loads(ref.read_text(encoding="utf-8"))["competencies"])
        competences = {item["id"] for item in bootcamp["competences"]}
        self.assertEqual(set(bootcamp["reperes"]), competences)
        self.assertTrue(all(bootcamp["reperes"].values()))
        catalogue = {item["id"] for item in catalogue_v2()["methodes"]}
        seen_tools, seen_codes, seen_workbench = set(), set(), set()
        self.assertEqual(len(bootcamp["modules"]), len({item["id"] for item in bootcamp["modules"]}))
        for module in bootcamp["modules"]:
            self.assertTrue(module["mission"] and module["cas"] and module["relecture"] and module["transfert"])
            self.assertTrue(set(module["methode"]) <= catalogue)
            seen_workbench.update(module["atelier"])
            for tool in module["outils"]:
                self.assertRegex(tool["id"], r"^[a-z0-9-]+$")
                self.assertNotIn(tool["id"], seen_tools)
                seen_tools.add(tool["id"])
                self.assertEqual(len(tool["colonnes"]), len(tool["exemple"]))
                self.assertTrue(all(tool["colonnes"]) and all(tool["exemple"]))
                self.assertFalse(any(re.match(r"^[=+@\-\t\r\n]", cell) for cell in tool["colonnes"]))
                self.assertTrue(tool["competences"])
                seen_codes.update(tool["competences"])
        self.assertEqual(seen_codes, competences)
        self.assertEqual(seen_workbench, set(VALIDATORS))
