"""Check the mission and stage sent by the isolated trial."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock
from uuid import uuid4

from ptd_coach.demo_v2 import PROJECTS_V2
from ptd_coach.library_v2 import SemesterWorkshopContext, WorkshopChatService, WorkshopMockProvider
from ptd_coach.project import ProjectService
from ptd_coach.student_trial import RESEARCH_MISSION, TRIAL_EXAMPLES, StudentTrialContext, StudentTrialProject


class StudentTrialTest(unittest.TestCase):
    def test_student_trial_sends_its_mission_and_stage_from_the_authenticated_team(self):
        actor = "student_demo_01"
        with TemporaryDirectory() as tmp:
            path = Path(tmp)
            standard = SemesterWorkshopContext(ProjectService(path / "standard.sqlite3", PROJECTS_V2))
            project = StudentTrialProject(path / "trial-project.sqlite3")
            context = StudentTrialContext(project)
            provider = WorkshopMockProvider()
            provider.complete = Mock(wraps=provider.complete)
            service = WorkshopChatService(path / "trial-chat.sqlite3", provider, context=context)
            thread = service.create(actor, uuid4().hex, {
                "scope": "individual", "synthetic_confirmed": True, "coach_version": context.coach_version,
            })
            reply = service.send(actor, thread["id"], uuid4().hex,
                                 {"message": "Je comprends le sujet.", "version": thread["version"]})
            system = provider.complete.call_args.args[0][0]["content"]
            data, _ = json.JSONDecoder().raw_decode(
                system.split("Données du projet accessibles pour ce tour (JSON) :\n", 1)[1])
            self.assertEqual(data["project"]["title"], RESEARCH_MISSION["title"])
            self.assertEqual(data["project"]["stage"], "Prise en main")
            self.assertEqual(data["items"], [])
            self.assertNotIn("service de reprise", system)
            self.assertIn("question ciblée", system)
            self.assertEqual(reply["invocations"][0]["prompt_version"], "conversation-ptd-v2-student-trial-0.1")

            standard.actor.set(actor)
            self.assertIn("Étudier un service de reprise", standard.system("individual"))
            self.assertNotIn(RESEARCH_MISSION["title"], standard.system("individual"))
            self.assertIn("centre", TRIAL_EXAMPLES["team_demo_01"]["excerpt"])
