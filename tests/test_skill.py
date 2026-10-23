"""Smoke tests for a skill repo. Standard library only. Run: python3 -m unittest discover -s tests -v"""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP = {".git", "node_modules", ".venv", "dist", "__pycache__", "templates"}
SECRET_PATTERNS = [r"AKIA[0-9A-Z]{16}", r"ghp_[A-Za-z0-9]{30,}", r"-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----",
                   r"xox[baprs]-[A-Za-z0-9-]{10,}"]


def files(suffix):
    return [p for p in ROOT.rglob(f"*{suffix}") if not (set(p.relative_to(ROOT).parts) & SKIP)]


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    out = {}
    for line in (m.group(1).split("\n") if m else []):
        kv = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if kv:
            out[kv.group(1)] = kv.group(2).strip()
    return out


class SkillTests(unittest.TestCase):
    def test_there_is_a_skill_or_a_plugin(self):
        is_plugin = (ROOT / ".claude-plugin" / "plugin.json").is_file()
        self.assertTrue(files("SKILL.md") or is_plugin, "no SKILL.md found and no plugin manifest")

    def test_frontmatter(self):
        for p in files("SKILL.md"):
            fm = frontmatter(p.read_text(encoding="utf-8"))
            self.assertTrue(re.match(r"^[a-z0-9][a-z0-9-]{0,63}$", fm.get("name", "")), f"{p}: bad or missing name")
            self.assertTrue(fm.get("description"), f"{p}: missing description")
            self.assertLessEqual(len(fm["description"]), 1024, f"{p}: description over 1024 characters")

    def test_relative_links_resolve(self):
        """Only the documents this repo maintains for readers. Old plans and notes under docs/ are not checked."""
        managed = [p for p in files(".md") if p.parent == ROOT or "setup" in p.relative_to(ROOT).parts[:2]]
        for p in managed:
            for target in re.findall(r"\]\(([^)#\s]+)(?:#[^)]*)?\)", p.read_text(encoding="utf-8")):
                if re.match(r"^[a-z]+:", target) or target.startswith("#"):
                    continue
                self.assertTrue((p.parent / target).exists(), f"{p.relative_to(ROOT)}: broken link {target}")

    def test_no_secrets(self):
        """Tests, fixtures and docs are skipped on purpose: redaction tests and old plans hold fake example keys. The CI secret scan covers the rest."""
        for p in ROOT.rglob("*"):
            if p.is_file() and not (set(p.relative_to(ROOT).parts) & (SKIP | {"tests", "fixtures", "docs"})) and p.stat().st_size < 1_000_000:
                text = p.read_text(encoding="utf-8", errors="ignore")
                for pat in SECRET_PATTERNS:
                    self.assertIsNone(re.search(pat, text), f"{p.relative_to(ROOT)}: looks like a secret ({pat})")

    def test_scripts_are_executable(self):
        for p in list(ROOT.glob("**/scripts/*.sh")) + list(ROOT.glob("**/bin/*")):
            if p.is_file() and not (set(p.relative_to(ROOT).parts) & SKIP):
                self.assertTrue(p.stat().st_mode & 0o111, f"{p.relative_to(ROOT)} is not executable")


if __name__ == "__main__":
    unittest.main()
