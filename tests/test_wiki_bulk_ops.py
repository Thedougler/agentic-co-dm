from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "wiki-bulk-ops"
PYTHON = os.environ.get("PYTHON", "python3")


def run_cli(*args: str, vault: Path | None = None) -> subprocess.CompletedProcess[str]:
    command = [PYTHON, str(SCRIPT), *args]
    return subprocess.run(command, cwd=ROOT, capture_output=True, text=True, env=os.environ | ({"OBSIDIAN_VAULT_PATH": str(vault)} if vault else {}))


class VaultFixture(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory(prefix="wiki-bulk-ops-")
        self.vault = Path(self.tempdir.name)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def page(self, relative: str, text: str | bytes) -> Path:
        path = self.vault / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(text, bytes):
            path.write_bytes(text)
        else:
            path.write_text(text, encoding="utf-8")
        return path


class FoundationalCliTests(VaultFixture):
    def test_missing_vault_is_validation_error(self) -> None:
        result = run_cli("replace", "--search", "x", "--replacement", "y", "--vault", str(self.vault / "missing"))
        self.assertEqual(result.returncode, 1)
        self.assertIn("vault", result.stderr.lower())

    def test_dry_run_json_does_not_write(self) -> None:
        page = self.page("note.md", "before before\n")
        result = run_cli("replace", "--search", "before", "--replacement", "after", "--dry-run", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(page.read_text(), "before before\n")
        data = json.loads(result.stdout)
        self.assertEqual(data["files_modified"], 1)
        self.assertEqual(data["total_changes"], 2)

    def test_invalid_utf8_is_skipped_with_partial_status(self) -> None:
        self.page("good.md", "old\n")
        self.page("bad.md", b"\x80\x81\x82")
        result = run_cli("replace", "--search", "old", "--replacement", "new", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 2)
        self.assertEqual((self.vault / "good.md").read_text(), "new\n")
        data = json.loads(result.stdout)
        self.assertEqual(data["files_skipped"], 1)
        self.assertTrue(any(record["skipped"] for record in data["records"]))
    def test_scope_filters_and_excluded_directories(self) -> None:
        self.page("entities/a.md", "old\n")
        self.page("entities/nested/b.md", "old\n")
        self.page("_raw/ignored.md", "old\n")
        result = run_cli("replace", "--search", "old", "--replacement", "new", "--glob", "entities/*.md", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.vault / "entities/a.md").read_text(), "new\n")
        self.assertEqual((self.vault / "entities/nested/b.md").read_text(), "old\n")
        self.assertEqual((self.vault / "_raw/ignored.md").read_text(), "old\n")

    def test_directory_scope_limits_scan(self) -> None:
        self.page("entities/a.md", "old\n")
        self.page("journal/b.md", "old\n")
        result = run_cli("replace", "--search", "old", "--replacement", "new", "--directory", "entities", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.vault / "entities/a.md").read_text(), "new\n")
        self.assertEqual((self.vault / "journal/b.md").read_text(), "old\n")


class RenameTests(VaultFixture):
    def test_rename_rewrites_structural_links_and_preserves_display(self) -> None:
        source = self.page("entities/npc/korvash.md", "---\ntitle: Korvash\ntype: npc\n---\nKorvash in prose.\n")
        links = self.page("journal/note.md", "[[korvash]] [[korvash|the orc]] ![[korvash#portrait]] [[entities/npc/korvash.md|Korvash]] old-name-kin\n")
        result = run_cli("rename", "--old", "korvash", "--new", "korveth", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse(source.exists())
        renamed = self.vault / "entities/npc/korveth.md"
        self.assertEqual(renamed.read_text(), "---\ntitle: Korveth\ntype: npc\n---\nKorvash in prose.\n")
        self.assertIn("[[korveth]] [[korveth|the orc]] ![[korveth#portrait]] [[entities/npc/korveth.md|Korvash]] old-name-kin", links.read_text())

    def test_rename_collision_is_atomic(self) -> None:
        source = self.page("old.md", "---\ntitle: Old\n---\n")
        destination = self.page("new.md", "untouched\n")
        result = run_cli("rename", "--old", "old", "--new", "new", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 1)
        self.assertIn("collision", result.stderr.lower())
        self.assertTrue(source.exists())
        self.assertEqual(destination.read_text(), "untouched\n")
    def test_rename_dry_run_and_second_invocation(self) -> None:
        source = self.page("old.md", "---\ntitle: Old\n---\n")
        preview = run_cli("rename", "--old", "old", "--new", "new", "--dry-run", "--json", "--vault", str(self.vault))
        self.assertEqual(preview.returncode, 0, preview.stderr)
        data = json.loads(preview.stdout)
        self.assertEqual(data["files_modified"], 1)
        self.assertTrue(any(change["line"] == 0 and change["zone"] == "filename" for change in data["records"][0]["changes"]))
        self.assertTrue(source.exists())
        applied = run_cli("rename", "--old", "old", "--new", "new", "--vault", str(self.vault))
        self.assertEqual(applied.returncode, 0, applied.stderr)
        repeat = run_cli("rename", "--old", "old", "--new", "new", "--json", "--vault", str(self.vault))
        self.assertEqual(repeat.returncode, 1)


class ReplaceTests(VaultFixture):
    def test_replace_defaults_to_body_and_preserves_frontmatter_and_targets(self) -> None:
        page = self.page("note.md", "---\ntitle: old\n---\n> [!note] old\n[[old]] old\n")
        result = run_cli("replace", "--search", "old", "--replacement", "new", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(page.read_text(), "---\ntitle: old\n---\n> [!note] new\n[[old]] new\n")
        self.assertEqual(json.loads(result.stdout)["total_changes"], 2)

    def test_replace_can_include_protected_zones_and_is_idempotent(self) -> None:
        page = self.page("note.md", "---\ntitle: old\n---\n[[old]]\n")
        result = run_cli("replace", "--search", "old", "--replacement", "new", "--include-frontmatter", "--include-links", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(page.read_text(), "---\ntitle: new\n---\n[[new]]\n")
        repeat = run_cli("replace", "--search", "old", "--replacement", "new", "--include-frontmatter", "--include-links", "--json", "--vault", str(self.vault))
        self.assertEqual(repeat.returncode, 0)
        self.assertEqual(json.loads(repeat.stdout)["files_modified"], 0)
    def test_regex_replacement_reports_line_and_zone(self) -> None:
        page = self.page("note.md", "keep\nvalue 12\nvalue 34\n")
        result = run_cli("replace", "--search", r"value (\d+)", "--replacement", r"item \1", "--regex", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(page.read_text(), "keep\nitem 12\nitem 34\n")
        data = json.loads(result.stdout)
        self.assertEqual([change["line"] for change in data["records"][0]["changes"]], [2, 3])
    def test_frontmatter_validation_and_repeated_filters(self) -> None:
        page = self.page("a.md", "---\ntype: npc\nrole: ally\n---\nbody\n")
        invalid = run_cli("frontmatter", "--action", "set", "--field", "bad.key", "--value", "x", "--vault", str(self.vault))
        self.assertEqual(invalid.returncode, 1)
        missing = run_cli("frontmatter", "--action", "rename", "--field", "role", "--vault", str(self.vault))
        self.assertEqual(missing.returncode, 1)
        result = run_cli("frontmatter", "--action", "set", "--field", "reviewed", "--value", "true", "--filter", "type=npc", "--filter", "role=ally", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("reviewed: true", page.read_text())

    def test_frontmatter_dry_run_json_is_byte_preserving(self) -> None:
        page = self.page("a.md", "---\ntype: npc\n---\nbody\n")
        before = page.read_bytes()
        result = run_cli("frontmatter", "--action", "set", "--field", "reviewed", "--value", "false", "--dry-run", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(page.read_bytes(), before)
        self.assertEqual(json.loads(result.stdout)["records"][0]["changes"][0]["zone"], "frontmatter")

    def test_replace_refuses_empty_wikilink(self) -> None:
        page = self.page("note.md", "[[old]]\n")
        result = run_cli("replace", "--search", "old", "--replacement", "", "--include-links", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 1)
        self.assertEqual(page.read_text(), "[[old]]\n")


class FrontmatterTests(VaultFixture):
    def test_frontmatter_set_filters_and_preserves_body(self) -> None:
        npc = self.page("entities/npc/a.md", "---\ntype: npc\ntitle: A\n---\nbody\n")
        other = self.page("entities/npc/b.md", "---\ntype: pc\n---\nbody\n")
        result = run_cli("frontmatter", "--action", "set", "--field", "connections_reviewed", "--value", "false", "--filter", "type=npc", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("connections_reviewed: false", npc.read_text())
        self.assertEqual(other.read_text(), "---\ntype: pc\n---\nbody\n")
        self.assertTrue(npc.read_text().endswith("body\n"))

    def test_frontmatter_rename_and_remove(self) -> None:
        page = self.page("a.md", "---\ntype: npc\nrelationships: allies\nremove_me: yes\n---\nbody\n")
        renamed = run_cli("frontmatter", "--action", "rename", "--field", "relationships", "--new-field", "connections", "--vault", str(self.vault))
        self.assertEqual(renamed.returncode, 0, renamed.stderr)
        removed = run_cli("frontmatter", "--action", "remove", "--field", "remove_me", "--vault", str(self.vault))
        self.assertEqual(removed.returncode, 0, removed.stderr)
        self.assertEqual(page.read_text(), "---\ntype: npc\nconnections: allies\n---\nbody\n")


class DryRunParityTests(VaultFixture):
    def test_replace_preview_matches_apply_counts_and_bytes(self) -> None:
        page = self.page("note.md", "old old\n")
        preview = run_cli("replace", "--search", "old", "--replacement", "new", "--dry-run", "--json", "--vault", str(self.vault))
        preview_data = json.loads(preview.stdout)
        before = page.read_bytes()
        self.assertEqual(preview.returncode, 0)
        self.assertEqual(page.read_bytes(), before)
        applied = run_cli("replace", "--search", "old", "--replacement", "new", "--json", "--vault", str(self.vault))
        applied_data = json.loads(applied.stdout)
        self.assertEqual((preview_data["files_modified"], preview_data["total_changes"]), (applied_data["files_modified"], applied_data["total_changes"]))
        self.assertEqual(page.read_text(), "new new\n")

    def test_rename_preview_leaves_filename_untouched(self) -> None:
        source = self.page("old.md", "---\ntitle: Old\n---\n")
        result = run_cli("rename", "--old", "old", "--new", "new", "--dry-run", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue(source.exists())
        self.assertFalse((self.vault / "new.md").exists())

if __name__ == "__main__":
    unittest.main()
