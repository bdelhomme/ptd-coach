"""Offline repository checks; no application or pedagogical validation."""

import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
REQUIRED = (
    "AGENTS.md", "README.md", ".gitignore", ".env.example",
    "docs/PROJECT_STATUS.md", "docs/DECISIONS.md", "docs/OPEN_QUESTIONS.md",
    "docs/PRODUCT_SPEC.md", "docs/PEDAGOGY.md", "docs/ARCHITECTURE.md",
    "docs/DATA_MODEL.md", "docs/PRIVACY_SECURITY.md", "docs/AI_ENGINE.md",
    "docs/ROADMAP.md", "docs/DEVELOPMENT.md", "assets/SOURCE_FINGERPRINTS.md",
    "contracts/json-schemas/coach-request.schema.json",
    "contracts/json-schemas/coach-response.schema.json",
    "pedagogy/competencies/candidate-v0.3.json",
    "pedagogy/scenarios/A2-first-cycle.json", "infra/README.md", "tests/README.md",
)
PRIVATE_DIRS = {".venv", "node_modules", "local-data", "student-data",
                "private-source-documents", ".git"}
PRIVATE_SUFFIXES = {".pem", ".key", ".docx", ".sqlite", ".sqlite3", ".dump", ".bak"}
TOKEN_PATTERNS = (
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bgithub_pat_[A-Za-z0-9_]{30,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b"),
)


def tracked_files(root):
    """Read the index, including staged new files, without invoking hooks."""
    output = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
    return [Path(p.decode("utf-8")) for p in output.split(b"\0") if p]


def check_repository(root, paths):
    paths = list(paths)
    errors = []
    for name in REQUIRED:
        if Path(name) not in paths or not (root / name).is_file():
            errors.append("Missing required tracked file: " + name)
    for relative in paths:
        name = relative.as_posix()
        path = root / relative
        if (PRIVATE_DIRS.intersection(relative.parts)
                or relative.suffix.lower() in PRIVATE_SUFFIXES
                or (relative.name.startswith(".env") and relative.name != ".env.example")
                or relative.name.lower() == "credentials.json"):
            errors.append("Private/local file tracked: " + name)
            continue
        if path.is_symlink():
            errors.append("Symlink requires explicit review: " + name)
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError):
            errors.append("Unreadable/non-text file requires review: " + name)
            continue
        if any(pattern.search(content) for pattern in TOKEN_PATTERNS):
            # Never include the matched value in logs.
            errors.append("Potential credential in: " + name)
        if relative.suffix.lower() == ".json":
            try:
                json.loads(content)
            except ValueError:
                errors.append("Invalid JSON: " + name)
        if relative.suffix.lower() == ".md":
            for target in re.findall(r"\[[^\]]*\]\(([^\s)]+)\)", content):
                target = target.strip("<>")
                parts = urlsplit(target)
                if parts.scheme or parts.netloc or not parts.path:
                    continue
                resolved = (path.parent / unquote(parts.path)).resolve()
                try:
                    resolved.relative_to(root.resolve())
                except ValueError:
                    errors.append("Link outside repository in: " + name)
                    continue
                if not resolved.exists():
                    errors.append("Broken local link in: " + name + " -> " + target)
    return errors


def main():
    paths = tracked_files(ROOT)
    errors = check_repository(ROOT, paths)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("Repository checks passed ({} tracked files).".format(len(paths)))
    print("Scope: required files, JSON syntax, local link targets, local files and token patterns.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
