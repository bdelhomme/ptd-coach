"""Synthetic fixtures for the repository checker, without application data."""

from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from scripts.check_repository import check_repository


class RepositoryChecksTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.required_patch = patch("scripts.check_repository.REQUIRED", ())
        self.required_patch.start()
        self.addCleanup(self.required_patch.stop)

    def write(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return Path(name)

    def test_valid_json_and_relative_link(self):
        paths = [self.write("docs/a.md", "[data](../data.json)"),
                 self.write("data.json", '{"synthetic": true}')]
        self.assertEqual(check_repository(self.root, paths), [])

    def test_invalid_json_is_rejected(self):
        paths = [self.write("bad.json", "{")]
        self.assertIn("Invalid JSON: bad.json", check_repository(self.root, paths))

    def test_missing_link_is_rejected(self):
        paths = [self.write("a.md", "[missing](missing.md)")]
        self.assertTrue(any("Broken local link" in e for e in check_repository(self.root, paths)))

    def test_verbatim_links_are_not_navigation_but_real_links_are_checked(self):
        for fence in ("```", "~~~", "````"):
            with self.subTest(fence=fence):
                content = fence + "text\n[R01](id='R01') [outside](../private.md)\n" + fence + "\n"
                paths = [self.write("quoted.md", content)]
                self.assertEqual(check_repository(self.root, paths), [])
                self.write("quoted.md", content + "[missing](missing.md)")
                errors = check_repository(self.root, paths)
                self.assertEqual(len(errors), 1)
                self.assertIn("Broken local link", errors[0])

    def test_nested_short_fence_does_not_end_verbatim_and_secrets_still_fail(self):
        paths = [self.write("quoted.md", "````text\n```\n[quoted](missing.md)\n````\n")]
        self.assertEqual(check_repository(self.root, paths), [])
        self.write("quoted.md", "~~~text\n" + "ghp_" + "x" * 36 + "\n~~~\n")
        self.assertEqual(check_repository(self.root, paths), ["Potential credential in: quoted.md"])

    def test_external_links_and_anchors_are_offline(self):
        paths = [self.write("a.md", "[web](https://example.invalid) [anchor](#section)")]
        self.assertEqual(check_repository(self.root, paths), [])

    def test_link_outside_repository_is_rejected(self):
        paths = [self.write("a.md", "[outside](../outside.md)")]
        self.assertTrue(any("Link outside" in e for e in check_repository(self.root, paths)))

    def test_local_files_and_originals_are_rejected(self):
        for name in (".env", ".env.local", "student-data/demo.json", "source.docx"):
            with self.subTest(name=name):
                paths = [self.write(name, "synthetic")]
                self.assertIn("Private/local file tracked: " + name,
                              check_repository(self.root, paths))

    def test_env_example_is_allowed(self):
        paths = [self.write(".env.example", "AI_PROVIDER=mock\n")]
        self.assertEqual(check_repository(self.root, paths), [])

    def test_synthetic_token_is_rejected_without_logging_value(self):
        synthetic = "ghp_" + "x" * 36
        paths = [self.write("sample.txt", synthetic)]
        errors = check_repository(self.root, paths)
        self.assertEqual(errors, ["Potential credential in: sample.txt"])
        self.assertNotIn(synthetic, "\n".join(errors))

    def test_symlink_is_rejected(self):
        self.write("target.txt", "synthetic")
        (self.root / "link.txt").symlink_to("target.txt")
        self.assertIn("Symlink requires explicit review: link.txt",
                      check_repository(self.root, [Path("link.txt")]))

    def test_required_file_must_be_tracked(self):
        self.write("required.md", "synthetic")
        with patch("scripts.check_repository.REQUIRED", ("required.md",)):
            self.assertEqual(check_repository(self.root, []),
                             ["Missing required tracked file: required.md"])


if __name__ == "__main__":
    unittest.main()
