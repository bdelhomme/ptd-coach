"""V0.8 provenance, version isolation, migration and offline paired collection."""

import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import sqlite3
import sys
import tempfile
import unittest
from unittest.mock import patch
import uuid

from ptd_coach.chat_context import ChatContext
from ptd_coach.chat_context_v08 import ChatContextV08
from ptd_coach.chat_service import ChatService
from ptd_coach.service import DomainError
from test_chat import RecordingProvider
import test_chat_http as http_v07

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from compare_conversation_v08 import collect, summary, write_review, main, verify_freeze, DIMENSIONS
from run_coach_eval_v07 import cases_from_file
from run_conversation_eval import evaluate
import compare_conversation_v08 as comparison


class VersionedChatTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / "chat.sqlite3"
        self.provider = RecordingProvider()
        self.service = ChatService(self.path, self.provider)

    def tearDown(self):
        self.temp.cleanup()

    def create(self, version="v08", scope="individual", key=None):
        return self.service.create("student_demo_01", key or str(uuid.uuid4()),
                                   {"scope": scope, "synthetic_confirmed": True, "coach_version": version})

    def send(self, row, message, actor="student_demo_01", **extra):
        return self.service.send(actor, row["id"], str(uuid.uuid4()),
                                 dict(message=message, version=row["version"], **extra))

    def test_v07_hash_is_unchanged_and_new_threads_pin_versions(self):
        old = self.send(self.create("v07"), "WBS fictive")
        self.assertEqual(old["invocations"][0]["context_sha256"],
                         "c321c72fa966b1d13a0e29f1ac8fcd120daafe3859f02b75477a05682322487a")
        new = self.send(self.create(), "WBS fictive")
        self.assertEqual(new["coach_version"], "v08")
        self.assertEqual(new["invocations"][0]["prompt_version"], ChatContextV08.version)
        with self.assertRaises(DomainError):
            self.send(new, "Change de coach", coach_version="v07")
        restarted = ChatService(self.path, self.provider)
        self.assertEqual(restarted.conversation("student_demo_01", new["id"]), new)
        self.assertEqual(restarted.conversation("student_demo_01", old["id"]), old)

    def test_creation_replay_checks_version_and_bad_versions_never_call(self):
        key = str(uuid.uuid4())
        self.create(key=key)
        with self.assertRaises(DomainError) as caught:
            self.create("v07", key=key)
        self.assertEqual(caught.exception.code, "idempotency_conflict")
        for version in ("v09", {}, ["v08"], None):
            with self.assertRaises(DomainError):
                self.create(version)
        self.assertEqual(self.provider.calls, [])

    def test_v08_private_collective_exports_and_context_are_isolated(self):
        private = self.send(self.create(), "CANARI_PRIVE_FICTIF")
        collective = self.send(self.create(scope="collective"), "Coordination fictive de notre équipe")
        self.send(collective, "Complément collectif", actor="student_demo_02")
        self.assertNotIn("CANARI_PRIVE_FICTIF", json.dumps(self.provider.calls[-1]))
        for row in (private, collective):
            for actor in ("student_demo_03", "tutor_demo_01", "coordination_demo_01", "admin_demo_01"):
                with self.assertRaises(DomainError):
                    self.service.export(actor, row["id"])
                with self.assertRaises(DomainError):
                    self.send(row, "intrusion", actor)
        with self.assertRaises(DomainError):
            self.service.export("student_demo_02", private["id"])

    def test_actual_system_and_message_hashes_match_selected_resource(self):
        row = self.send(self.create(), "Explique les dépendances dans un planning fictif")
        invocation = row["invocations"][0]
        self.assertEqual(invocation["resource_ids"], ["R03"])
        call = self.provider.calls[0]
        self.assertIn("<ressource id='R03'", call[0]["content"])
        self.assertNotIn("<ressource id='R01'", call[0]["content"])
        self.assertEqual(invocation["system_sha256"], hashlib.sha256(call[0]["content"].encode()).hexdigest())
        self.assertEqual(invocation["messages_sha256"], hashlib.sha256(
            json.dumps(call, ensure_ascii=False, sort_keys=True).encode()).hexdigest())
        row = self.send(row, "Merci, c'est tout.")
        self.assertEqual(row["invocations"][-1]["resource_ids"], [])
        self.assertEqual(row["proposed_updates"], [])

    def test_migration_preserves_legacy_messages_requests_and_pending(self):
        legacy = Path(self.temp.name) / "legacy.sqlite3"
        with sqlite3.connect(legacy) as db:
            db.executescript((ROOT / "ptd_coach/chat_schema.sql").read_text())
            db.execute("INSERT INTO conversations VALUES (?,?,?,?,?,?,?,?)",
                       ("legacy", "individual", "student_demo_01", "team_demo_01", "k", 2, 1, "2026-01-01"))
            db.execute("INSERT INTO chat_messages VALUES (?,?,?,?,?,?)", (1, "legacy", "user", "Texte fictif intact", "student_demo_01", "t"))
            db.execute("INSERT INTO chat_requests VALUES (?,?,?,?,?,?,?,?)",
                       ("student_demo_01", "pending-key", "legacy", "digest", "pending", '{"usage":{}}', None, "t"))
        migrated = ChatService(legacy, self.provider)
        snapshot = migrated.conversation("student_demo_01", "legacy")
        self.assertEqual(snapshot["coach_version"], "v07")
        self.assertTrue(snapshot["pending"])
        self.assertEqual(snapshot["messages"][0]["content"], "Texte fictif intact")
        with self.assertRaises(DomainError) as caught:
            migrated.send("student_demo_01", "legacy", str(uuid.uuid4()), {"version": 2, "message": "test"})
        self.assertEqual(caught.exception.code, "call_pending")
        with sqlite3.connect(legacy) as db:
            self.assertEqual(db.execute("PRAGMA user_version").fetchone()[0], 2)
            self.assertEqual(db.execute("SELECT metadata FROM chat_requests").fetchone()[0], '{"usage":{}}')

    def test_suites_are_synthetic_balanced_and_disjoint(self):
        suites = [cases_from_file(ROOT / "pedagogy/qa" / name) for name in
                  ("COACH_DEV_CASES_V08.json", "COACH_RESERVED_CASES_V08.json")]
        ids, messages = set(), set()
        for suite in suites:
            self.assertEqual(len(suite["cases"]), 12)
            axes = [c["axis"] for c in suite["cases"]]
            self.assertEqual(len(set(axes)), 6)
            self.assertTrue(all(axes.count(a) == 2 for a in axes))
            self.assertEqual({f for c in suite["cases"] for f in c["families"]}, {"F1", "F2", "F3", "F4", "F5"})
            self.assertEqual({c["scope"] for c in suite["cases"]}, {"individual", "collective"})
            for case in suite["cases"]:
                self.assertNotIn(case["id"], ids)
                ids.add(case["id"])
                self.assertIn(len(case["turns"]), (2, 3, 4))
                for turn in case["turns"]:
                    self.assertNotIn(turn["student"], messages)
                    messages.add(turn["student"])

    def test_offline_development_and_v07_regression_never_leak_rubrics(self):
        for name in ("COACH_DEV_CASES_V08.json", "COACH_MULTI_TURN_CASES_V07.json"):
            suite = cases_from_file(ROOT / "pedagogy/qa" / name)
            suite = copy.deepcopy(suite)
            for case in suite["cases"]:
                for turn in case["turns"]:
                    turn["look_for"] = ["ORACLE_NEVER_SENT"]
            rows = list(evaluate(suite, ChatContextV08(), self.provider))
            self.assertEqual(len(rows), sum(len(c["turns"]) for c in suite["cases"]))
            self.assertNotIn("ORACLE_NEVER_SENT", json.dumps(self.provider.calls))
            self.assertTrue(all(r["coach_version"] == "v08" for r in rows))

    def test_paired_mock_records_and_human_grid_remain_unscored(self):
        suite = cases_from_file(ROOT / "pedagogy/qa/COACH_DEV_CASES_V08.json")
        rows = list(collect(suite, self.provider, {"D03", "D09"}))
        self.assertEqual(len(rows), 12)
        self.assertEqual({r["variant"] for r in rows}, {"v07", "v08"})
        self.assertEqual(summary(rows)["v08"]["usage"]["total_tokens"], 720)
        self.assertEqual(sum(len(call) == 2 for call in self.provider.calls), 4)
        folder = Path(self.temp.name)
        write_review(folder, rows, suite)
        with (folder / "GRILLE_VIERGE.csv").open() as file:
            grid = list(csv.DictReader(file))
        self.assertEqual(len(grid), 12)
        self.assertTrue(all(not r[k] for r in grid for k in DIMENSIONS))

    def test_freeze_and_paid_reserved_gates_precede_network(self):
        self.assertEqual(len(verify_freeze()), 64)
        base = ["--output-dir", str(Path(self.temp.name) / "output")]
        with patch("ptd_coach.chat_provider.build_opener") as network:
            for args in (["--provider", "mistral"],
                         ["--provider", "mistral", "--allow-billable"],
                         ["--suite", str(ROOT / "pedagogy/qa/COACH_RESERVED_CASES_V08.json")]):
                with patch("sys.stderr", new=io.StringIO()), self.assertRaises(SystemExit):
                    main(base + args)
            network.assert_not_called()
        self.assertFalse((Path(self.temp.name) / "output").exists())

    def test_freeze_refuses_a_modified_context(self):
        folder = Path(self.temp.name)
        (folder / "context.txt").write_text("modified")
        freeze = folder / "freeze.json"
        freeze.write_text(json.dumps({"files": {"context.txt": hashlib.sha256(b"original").hexdigest()}}))
        with patch.object(comparison, "ROOT", folder), patch.object(comparison, "FREEZE", freeze):
            with self.assertRaisesRegex(ValueError, "Contexte modifié"):
                verify_freeze()

    def test_archive_content_hashes_are_preserved(self):
        manifest = json.loads((ROOT / "assets/PEDAGOGY_IMPORT_V08.json").read_text())
        imported = [f for f in manifest["files"] if f["target"]]
        self.assertEqual(len(imported), 4)
        for f in imported:
            self.assertEqual(hashlib.sha256((ROOT / f["target"]).read_bytes()).hexdigest(), f["sha256"])

    def test_reserved_provenance_matches_freeze_and_suite_without_execution(self):
        provenance = json.loads((ROOT / "pedagogy/qa/V08_RESERVED_PROVENANCE.json").read_text())
        self.assertEqual(provenance["context_freeze_sha256"], verify_freeze())
        self.assertEqual(provenance["suite_sha256"], hashlib.sha256((ROOT / provenance["suite_path"]).read_bytes()).hexdigest())
        freeze = json.loads(comparison.FREEZE.read_text())
        self.assertLess(freeze["timestamp_utc"], provenance["timestamp_utc"])
        self.assertEqual(provenance["counts"]["cases"], 12)
        self.assertEqual(provenance["counts"]["student_turns"], 34)
        self.assertEqual(provenance["procedure"]["execution_status"], "not_executed_on_api")

    def test_real_development_corpus_preserves_hashes_contexts_and_blank_review(self):
        folder = ROOT / "pedagogy/evaluations/v08-c1-comparison"
        manifest = json.loads((folder / "MANIFESTE.json").read_text())
        self.assertEqual({p.name for p in folder.iterdir()}, set(manifest["files"]) | {"MANIFESTE.json"})
        for name, meta in manifest["files"].items():
            data = (folder / name).read_bytes()
            self.assertEqual(len(data), meta["bytes"])
            self.assertEqual(hashlib.sha256(data).hexdigest(), meta["sha256"])
        rows = [json.loads(l) for l in (folder / "responses.jsonl").read_text().splitlines()]
        self.assertEqual(len(rows), 12)
        self.assertEqual({r["case_id"] for r in rows}, {"D03", "D09"})
        systems = json.loads((folder / "SYSTEM_CONTEXTS.json").read_text())
        histories = {}
        markdown = (folder / "LECTURE_COMPARATIVE.md").read_text()
        labels = json.loads((folder / "CLE_VARIANTES.json").read_text())
        for r in rows:
            system = systems[r["system_sha256"]]["system_exact"]
            self.assertEqual(hashlib.sha256(system.encode()).hexdigest(), r["system_sha256"])
            history = histories.setdefault((r["variant"], r["case_id"]), [])
            user = {"role": "user", "content": r["student"]}
            messages = [{"role": "system", "content": system}] + history + [user]
            self.assertEqual(hashlib.sha256(json.dumps(messages, ensure_ascii=False, sort_keys=True).encode()).hexdigest(), r["messages_sha256"])
            history.extend([user, {"role": "assistant", "content": r["response"]}])
            self.assertIn("~~~~text\n" + r["response"] + "\n~~~~", markdown)
            self.assertEqual(r["freeze_sha256"], verify_freeze())
            self.assertEqual(r["status"], "model_called")
        with (folder / "GRILLE_VIERGE.csv").open() as file:
            grid = list(csv.DictReader(file))
        self.assertEqual(len(grid), 12)
        self.assertTrue(all(not row[k] for row in grid for k in DIMENSIONS))
        self.assertEqual({(r["case_id"], int(r["turn"]), r["label"]) for r in grid},
                         {(r["case_id"], r["turn"], labels[r["variant"]]) for r in rows})
        report = json.loads((folder / "MESURES.json").read_text())
        self.assertEqual(report["summary"], summary(rows))
        self.assertIsNone(report["pedagogical_verdict"])


class VersionedHttpTest(http_v07.ChatHttpTest):
    # Re-run all existing HTTP boundaries with explicit V0.8 creation.
    def create(self, session, scope="individual"):
        status, _, result = self.request("/api/coach/conversations", "POST",
            {"scope": scope, "synthetic_confirmed": True, "coach_version": "v08"}, session)
        self.assertEqual(status, 201)
        self.assertEqual(result["coach_version"], "v08")
        return "/api/coach/conversations/" + result["id"]


if __name__ == "__main__":
    unittest.main()
