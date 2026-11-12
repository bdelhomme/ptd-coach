from copy import deepcopy
import unittest

from ptd_coach.gantt import gantt_warnings, validate_gantt
from ptd_coach.service import DomainError


def task(task_id, start="2026-11-12", duration=1, predecessors=()):
    return {"id": task_id, "name": f" Tâche fictive {task_id} ", "start": start,
            "duration": duration, "predecessors": list(predecessors)}


def plan(*tasks, baseline=None):
    return {"tasks": list(tasks), "baseline": baseline}


class GanttTest(unittest.TestCase):
    def test_preserves_input_order_and_snapshot_without_aliasing(self):
        tasks = [task("lancement", predecessors=["reunion"]), task("reunion", duration=0)]
        source = plan(*tasks, baseline={"tasks": tasks})
        normalized = validate_gantt(source)
        self.assertEqual([item["id"] for item in normalized["tasks"]], ["lancement", "reunion"])
        self.assertEqual(normalized["tasks"][0]["name"], "Tâche fictive lancement")
        self.assertEqual(normalized["tasks"], normalized["baseline"]["tasks"])
        normalized["tasks"][0]["predecessors"].clear()
        self.assertEqual(normalized["baseline"]["tasks"][0]["predecessors"], ["reunion"])
        self.assertEqual(source["tasks"][0]["predecessors"], ["reunion"])

    def test_warnings_report_first_available_calendar_day_without_replanning(self):
        source = plan(task("debut", "2026-11-13", duration=3),
                      task("revue", "2026-11-15", duration=0, predecessors=["debut"]),
                      task("suite", "2026-11-15", predecessors=["revue"]),
                      task("livraison", "2026-11-16", duration=0, predecessors=["debut"]))
        normalized = validate_gantt(source)
        original = deepcopy(normalized)
        self.assertEqual(gantt_warnings(normalized), [
            {"task_id": "revue", "predecessor_id": "debut", "earliest_start": "2026-11-16"},
        ])
        self.assertEqual(normalized, original)

    def test_cycles_and_invalid_references_rejected_in_current_and_baseline(self):
        invalid = (
            [task("a"), task("a")],
            [task("a", predecessors=["absente"])],
            [task("a", predecessors=["a"])],
            [task("a", predecessors=["b"]), task("b", predecessors=["c"]), task("c", predecessors=["a"])],
            [task("a", predecessors=["b", "b"]), task("b")],
        )
        for tasks in invalid:
            for source in (plan(*tasks), plan(baseline={"tasks": tasks})):
                with self.subTest(source=source), self.assertRaises(DomainError):
                    validate_gantt(source)

    def test_shape_dates_and_duration_are_bounded(self):
        invalid_tasks = (
            task("a/b"), task("a", "2026-02-29"), task("a", "20261112"),
            task("a", "1999-12-31"), task("a", "2101-01-01"), task("a", "2100-12-31", 2),
            task("a", duration=True), task("a", duration=1.5), task("a", duration=-1), task("a", duration=3661),
            dict(task("a"), name="  "), dict(task("a"), name="x" * 121), dict(task("a"), name="\ud800"),
            dict(task("a"), predecessors="b"), dict(task("a"), predecessors=[[]]), dict(task("a"), extra=True),
        )
        for invalid in invalid_tasks:
            with self.subTest(task=invalid), self.assertRaises(DomainError):
                validate_gantt(plan(invalid))
        for invalid in (None, {}, plan(baseline=[]), plan(*[task(str(i)) for i in range(101)])):
            with self.subTest(value=invalid), self.assertRaises(DomainError):
                validate_gantt(invalid)
        boundary = validate_gantt(plan(task("a", "2100-12-31", 1), task("b", "2000-01-01", 0)))
        self.assertEqual(gantt_warnings(boundary), [])


if __name__ == "__main__":
    unittest.main()
