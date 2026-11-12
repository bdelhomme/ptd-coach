from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import stat
import tempfile
import unittest
from unittest.mock import patch
from uuid import uuid4

from ptd_coach.identities import USERS
from ptd_coach.project import ProjectService
from ptd_coach.service import DomainError


STUDENT = "student_demo_01"
TEAMMATE = "student_demo_02"
OTHER_TEAM = "student_demo_03"
TUTOR = "tutor_demo_01"


class ProjectServiceTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.path = Path(temporary.name) / "semester.sqlite3"
        self.project = ProjectService(self.path)

    def create(self, scope="collective", kind="requirement", origin="ai", content="Repère fictif à vérifier"):
        snapshot = self.project.create(STUDENT, {"scope": scope, "kind": kind, "text": content,
                                                 "source": "Essai fictif", "origin": origin})
        return next(item for item in snapshot["items"] if item["text"] == content)

    def assert_error(self, code, function, *args):
        with self.assertRaises(DomainError) as raised:
            function(*args)
        self.assertEqual(raised.exception.code, code)

    def audit(self):
        with self.project.connect() as db:
            return [dict(row) for row in db.execute("SELECT * FROM project_share_audit ORDER BY id")]

    def test_confirmation_and_share_are_separate_and_edit_retracts_both(self):
        draft = self.create()
        self.assertFalse(draft["confirmed"])
        self.assertEqual(self.project.context(STUDENT, "collective")["items"], [])
        self.assert_error("not_shareable", self.project.share, STUDENT, draft["id"], {"version": 1})
        self.assert_error("invalid_request", self.project.confirm, STUDENT, draft["id"],
                          {"version": 1, "confirmed_by": TUTOR})

        confirmed = self.project.confirm(TEAMMATE, draft["id"], {"version": 1})["items"][0]
        self.assertEqual(confirmed["origin"], "ai")
        self.assertEqual(confirmed["confirmed_by"], TEAMMATE)
        self.assertIsNotNone(confirmed["confirmed_at"])
        self.assertEqual(self.project.snapshot(TUTOR)["items"], [])
        self.assertEqual(self.project.context(STUDENT, "collective")["items"][0]["text"], draft["text"])

        shared = self.project.share(STUDENT, draft["id"], {"version": 2})["items"][0]
        self.assertTrue(shared["shared"])
        tutor_item = self.project.snapshot(TUTOR)["items"][0]
        self.assertEqual(tutor_item["id"], shared["id"])
        self.assertIsNone(tutor_item["confirmed_by"])
        self.assertNotIn("week_description", self.project.snapshot(TUTOR)["project"])
        self.assert_error("stale_version", self.project.update, STUDENT, draft["id"],
                          {"version": 2, "kind": "criterion", "text": "Modification", "source": "Essai"})
        edited = self.project.update(TEAMMATE, draft["id"],
                                     {"version": 3, "kind": "criterion", "text": "Modification",
                                      "source": "Deuxième essai fictif"})["items"][0]
        self.assertFalse(edited["confirmed"])
        self.assertFalse(edited["shared"])
        self.assertEqual(edited["origin"], "ai")
        self.assertEqual(self.project.snapshot(TUTOR)["items"], [])
        self.assertEqual(self.project.context(STUDENT, "collective")["items"], [])
        entries = self.audit()
        self.assertEqual([(row["action"], row["item_version"], row["actor_id"], row["recipient_id"])
                          for row in entries],
                         [("share", 2, STUDENT, TUTOR), ("revoke_on_edit", 3, TEAMMATE, TUTOR)])
        self.assertTrue(all(row["occurred_at"] and row["item_id"] == draft["id"] for row in entries))
        self.assertEqual(set(entries[0]), {"id", "item_id", "item_version", "actor_id", "recipient_id",
                                         "action", "occurred_at"})
        self.project.confirm(STUDENT, draft["id"], {"version": 4})
        context = self.project.context(TEAMMATE, "collective")["items"]
        self.assertEqual([item["text"] for item in context], ["Modification"])
        self.assertEqual(self.project.snapshot(TUTOR)["items"], [])

    def test_private_and_other_team_access_is_denied_in_every_mutation(self):
        private = self.create(scope="individual", kind="note")
        collective = self.create(content="Repère fictif collectif")
        self.assertEqual([item["id"] for item in self.project.snapshot(TEAMMATE)["items"]], [collective["id"]])
        self.assertEqual(self.project.snapshot(OTHER_TEAM)["items"], [])
        self.assertNotEqual(self.project.snapshot(STUDENT)["project"]["id"],
                            self.project.snapshot(OTHER_TEAM)["project"]["id"])
        self.assert_error("forbidden", self.project.snapshot, "coordination_demo_01")
        for method in (self.project.confirm, self.project.share, self.project.revoke, self.project.delete):
            self.assert_error("not_found", method, TEAMMATE, private["id"], {"version": 1})
            self.assert_error("not_found", method, OTHER_TEAM, collective["id"], {"version": 1})
            self.assert_error("forbidden", method, TUTOR, collective["id"], {"version": 1})
        self.assert_error("not_found", self.project.update, TEAMMATE, private["id"],
                          {"version": 1, "kind": "note", "text": "Fictif", "source": "Fictif"})
        self.assert_error("not_found", self.project.update, OTHER_TEAM, collective["id"],
                          {"version": 1, "kind": "note", "text": "Fictif", "source": "Fictif"})
        self.assert_error("forbidden", self.project.create, TUTOR,
                          {"scope": "collective", "kind": "note", "text": "Fictif",
                           "source": "Fictif", "origin": "human"})
        self.project.confirm(STUDENT, private["id"], {"version": 1})
        self.assert_error("not_shareable", self.project.share, STUDENT, private["id"], {"version": 2})
        self.assert_error("forbidden", self.project.context, TUTOR, "collective")
        self.assertEqual(self.project.snapshot(TUTOR)["items"], [])
        self.assertEqual(self.project.context(TEAMMATE, "individual")["items"], [])
        self.assertEqual(self.project.context(STUDENT, "collective")["items"], [])
        self.assertEqual(self.project.context(STUDENT, "individual")["items"][0]["kind"], "note")

    def test_revocation_and_deletion_remove_tutor_access(self):
        record = self.create()
        item_id = record["id"]
        self.project.confirm(STUDENT, item_id, {"version": 1})
        self.project.share(STUDENT, item_id, {"version": 2})
        with patch.dict(USERS, {"replacement_tutor_demo": {"role": "tutor", "team": "team_demo_01"}}):
            self.assertEqual(self.project.snapshot("replacement_tutor_demo")["items"], [])
        self.assert_error("stale_version", self.project.revoke, TEAMMATE, item_id, {"version": 2})
        self.project.revoke(TEAMMATE, item_id, {"version": 3})
        self.assertEqual(self.project.snapshot(TUTOR)["items"], [])
        self.assertEqual(len(self.project.context(TEAMMATE, "collective")["items"]), 1)
        self.project.share(STUDENT, item_id, {"version": 4})
        self.project.delete(TEAMMATE, item_id, {"version": 5})
        self.assertEqual(self.project.snapshot(TUTOR)["items"], [])
        self.assertEqual(self.project.context(TEAMMATE, "collective")["items"], [])
        self.assertEqual([(row["action"], row["item_version"]) for row in self.audit()],
                         [("share", 2), ("revoke", 3), ("share", 4), ("revoke_on_delete", 5)])

    def test_week_advance_preserves_confirmed_items_and_uses_revision(self):
        record = self.create(kind="review", origin="human", content="Point d’étape fictif")
        self.project.confirm(STUDENT, record["id"], {"version": 1})
        advanced = self.project.next_week(STUDENT, {"version": 1})
        self.assertEqual(advanced["project"]["current_week"], 2)
        self.assertEqual(advanced["items"][0]["week"], 1)
        self.assertEqual(self.project.snapshot(OTHER_TEAM)["project"]["current_week"], 1)
        self.assert_error("stale_version", self.project.next_week, TEAMMATE, {"version": 1})
        self.assert_error("forbidden", self.project.next_week, TUTOR, {"version": 2})
        reopened = ProjectService(self.path)
        self.assertEqual(reopened.context(TEAMMATE, "collective")["items"][0]["text"], record["text"])
        self.assertEqual(reopened.snapshot(STUDENT)["project"]["current_week"], 2)
        self.assertEqual(stat.S_IMODE(self.path.stat().st_mode), 0o600)
        for version in range(2, 6):
            reopened.next_week(STUDENT, {"version": version})
        self.assert_error("end_of_demo", reopened.next_week, STUDENT, {"version": 6})

    def test_context_is_bounded_and_excludes_drafts_and_other_scope(self):
        for i in range(10):
            item = self.project.create(STUDENT, {
                "scope": "collective", "kind": "hypothesis", "origin": "ai",
                "text": f"Hypothèse fictive {i} " + "x" * 500 + " ; à confirmer.",
                "source": "s" * 200 + " ; extrait fictif.",
            })["items"][0]
            self.project.confirm(STUDENT, item["id"], {"version": 1})
        self.create(content="Brouillon collectif fictif")
        private = self.create(scope="individual", kind="note", content="Mémoire privée fictive")
        self.project.confirm(STUDENT, private["id"], {"version": 1})

        context = self.project.context(STUDENT, "collective")
        self.assertEqual(len(context["items"]), 5)
        self.assertTrue(all(item["kind"] == "hypothesis" and item["origin"] == "ai" for item in context["items"]))
        self.assertTrue(all(item["text"].endswith("à confirmer.") and item["source"].endswith("extrait fictif.")
                            for item in context["items"]))
        self.assertNotIn("week_description", context["project"])
        self.assertEqual(self.project.context(STUDENT, "individual")["items"][0]["text"], private["text"])

    def test_concurrent_create_retry_is_idempotent_even_after_deletion(self):
        key = str(uuid4())
        payload = {"scope": "individual", "kind": "note", "origin": "human",
                   "text": "Une seule création fictive", "source": "Test fictif"}
        with ThreadPoolExecutor(max_workers=2) as pool:
            results = list(pool.map(lambda _: self.project.create(STUDENT, payload, key), range(2)))
        self.assertEqual([len(result["items"]) for result in results], [1, 1])
        self.assertEqual(results[0]["items"][0]["id"], results[1]["items"][0]["id"])
        self.assert_error("idempotency_conflict", self.project.create, STUDENT,
                          dict(payload, text="Autre contenu fictif"), key)
        self.project.delete(STUDENT, results[0]["items"][0]["id"], {"version": 1})
        self.assert_error("idempotency_conflict", self.project.create, STUDENT, payload, key)
        self.assertEqual(self.project.snapshot(STUDENT)["items"], [])
        with self.project.connect() as db:
            row = db.execute("SELECT item_id, fingerprint FROM project_create_commands").fetchone()
        self.assertIsNone(row["item_id"])
        self.assertIsNone(row["fingerprint"])

    def test_audit_schema_upgrade_preserves_records(self):
        record = self.create()
        with self.project.connect() as db:
            db.execute("DROP TABLE project_share_audit")
            db.execute("PRAGMA user_version = 1")
        reopened = ProjectService(self.path)
        self.assertEqual(reopened.snapshot(STUDENT)["items"][0]["id"], record["id"])
        self.assertEqual(self.audit(), [])
