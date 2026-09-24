from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "wiki-bulk-ops"
PYTHON = os.environ.get("PYTHON", "python3")


def run_cli(*args: str, vault: Path | None = None, extra_env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    command = [PYTHON, str(SCRIPT), *args]
    environment = os.environ | (extra_env or {})
    if vault:
        environment["OBSIDIAN_VAULT_PATH"] = str(vault)
    return subprocess.run(command, cwd=ROOT, capture_output=True, text=True, env=environment)


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

class LinkRepairTests(VaultFixture):
    def test_link_repair_resolves_mapping_alias_and_fuzzy_and_reports_ambiguity(self) -> None:
        self.page("current.md", "---\naliases: [old-page]\n---\ncurrent\n")
        self.page("new-page.md", "new\n")
        self.page("read.md", "read\n")
        self.page("cot.md", "cot\n")
        self.page("cut.md", "cut\n")
        source = self.page("source.md", "[[old-page|alias]] [[mapped-page]] [[red]] [[cat]] [[zzzz]]\n")
        mapping = self.page("mapping.tsv", "mapped-page\tnew-page\n")
        preview = run_cli("link-repair", "--mapping", str(mapping), "--fuzzy-threshold", "1", "--dry-run", "--json", "--vault", str(self.vault))
        self.assertEqual(preview.returncode, 0, preview.stderr)
        data = json.loads(preview.stdout)
        self.assertEqual(data["files_modified"], 1)
        self.assertIn("resolution", data["records"][0])
        self.assertIn("cat", data["details"]["ambiguous"])
        self.assertIn("zzzz", data["details"]["unresolved"])
        self.assertEqual(source.read_text(), "[[old-page|alias]] [[mapped-page]] [[red]] [[cat]] [[zzzz]]\n")
        applied = run_cli("link-repair", "--mapping", str(mapping), "--fuzzy-threshold", "1", "--vault", str(self.vault))
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertEqual(source.read_text(), "[[current|alias]] [[new-page]] [[read]] [[cat]] [[zzzz]]\n")
        repeat = run_cli("link-repair", "--mapping", str(mapping), "--fuzzy-threshold", "1", "--json", "--vault", str(self.vault))
        self.assertEqual(repeat.returncode, 0, repeat.stderr)
        self.assertEqual(json.loads(repeat.stdout)["files_modified"], 0)

    def test_link_repair_flags_and_mapping_warnings(self) -> None:
        self.page("current.md", "---\naliases: [old-page]\n---\n")
        source = self.page("source.md", "[[old-page]] [[newp]]\n")
        mapping = self.page("mapping.tsv", "bad-line\nnewp\tcurrent\textra\n")
        disabled = run_cli("link-repair", "--mapping", str(mapping), "--no-aliases", "--no-fuzzy", "--no-git", "--json", "--vault", str(self.vault))
        self.assertEqual(disabled.returncode, 0, disabled.stderr)
        self.assertEqual(source.read_text(), "[[old-page]] [[newp]]\n")
        self.assertIn("mapping", disabled.stderr.lower())
        invalid = run_cli("link-repair", "--fuzzy-threshold", "6", "--vault", str(self.vault))
        self.assertEqual(invalid.returncode, 1)

    def test_link_repair_uses_git_renames_and_reports_bad_encoding(self) -> None:
        self.page("old.md", "old\n")
        source = self.page("nested/source.md", "[[old]]\n")
        self.page("bad.md", b"\x80\x81")
        subprocess.run(["git", "init", "-q"], cwd=self.vault, check=True)
        subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=self.vault, check=True)
        subprocess.run(["git", "config", "user.name", "Test"], cwd=self.vault, check=True)
        subprocess.run(["git", "add", "."], cwd=self.vault, check=True)
        subprocess.run(["git", "commit", "-qm", "old"], cwd=self.vault, check=True)
        subprocess.run(["git", "mv", "old.md", "new.md"], cwd=self.vault, check=True)
        subprocess.run(["git", "commit", "-qm", "rename"], cwd=self.vault, check=True)
        scoped = run_cli("link-repair", "--directory", "nested", "--json", "--vault", str(self.vault))
        self.assertEqual(scoped.returncode, 0, scoped.stderr)
        self.assertEqual(source.read_text(), "[[new]]\n")
        result = run_cli("link-repair", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 2, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data["files_skipped"], 1)


class TagNormalizeTests(VaultFixture):
    def setUp(self) -> None:
        super().setUp()
        self.taxonomy = self.page("taxonomy.md", "# Taxonomy\n## Canonical\n- npc\n- creature\n## Aliases\n- monster -> creature\n")

    def test_tag_normalize_aliases_duplicates_unknowns_and_body(self) -> None:
        page = self.page("a.md", "---\ntags: [monster, npc, npc, unknown]\n---\nbody\n")
        preview = run_cli("tag-normalize", "--taxonomy", str(self.taxonomy), "--dry-run", "--json", "--vault", str(self.vault))
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertEqual(page.read_text(), "---\ntags: [monster, npc, npc, unknown]\n---\nbody\n")
        data = json.loads(preview.stdout)
        self.assertEqual(data["files_modified"], 1)
        self.assertEqual(data["details"]["unknown_tags"], ["unknown"])
        applied = run_cli("tag-normalize", "--taxonomy", str(self.taxonomy), "--vault", str(self.vault))
        self.assertEqual(applied.returncode, 0, applied.stderr)
        self.assertEqual(page.read_text(), "---\ntags: [creature, npc, unknown]\n---\nbody\n")
        removed = run_cli("tag-normalize", "--taxonomy", str(self.taxonomy), "--remove-unknown", "--vault", str(self.vault))
        self.assertEqual(removed.returncode, 0, removed.stderr)
        self.assertEqual(page.read_text(), "---\ntags: [creature, npc]\n---\nbody\n")
        repeat = run_cli("tag-normalize", "--taxonomy", str(self.taxonomy), "--remove-unknown", "--json", "--vault", str(self.vault))
        self.assertEqual(json.loads(repeat.stdout)["files_modified"], 0)

    def test_tag_normalize_block_tags_and_missing_taxonomy(self) -> None:
        page = self.page("nested/a.md", "---\ntags:\n  - monster\n  - npc\n---\nbody\n")
        result = run_cli("tag-normalize", "--taxonomy", str(self.taxonomy), "--directory", "nested", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(page.read_text(), "---\ntags:\n  - creature\n  - npc\n---\nbody\n")
        self.page("bad.md", b"\x80\x81")
        partial = run_cli("tag-normalize", "--taxonomy", str(self.taxonomy), "--json", "--vault", str(self.vault))
        self.assertEqual(partial.returncode, 2, partial.stderr)
        self.assertEqual(json.loads(partial.stdout)["files_skipped"], 1)
        missing = run_cli("tag-normalize", "--taxonomy", str(self.vault / "missing.md"), "--vault", str(self.vault))
        self.assertEqual(missing.returncode, 1)


class OrphanReportTests(VaultFixture):
    def test_orphan_report_lists_only_unlinked_pages_without_writing(self) -> None:
        self.page("index.md", "[[linked]]\n")
        self.page("log.md", "log\n")
        self.page("hot.md", "hot\n")
        linked = self.page("linked.md", "linked\n")
        orphan = self.page("orphan.md", "orphan\n")
        before = {path: path.read_bytes() for path in (linked, orphan)}
        result = run_cli("orphan-report", "--json", "--vault", str(self.vault))
        self.assertEqual(result.returncode, 0, result.stderr)
        data = json.loads(result.stdout)
        self.assertEqual(data["files_modified"], 0)
        self.assertIn("orphan.md", data["details"]["orphans"])
        self.assertNotIn("linked.md", data["details"]["orphans"])
        self.assertFalse(any(name in data["details"]["orphans"] for name in ("index.md", "log.md", "hot.md")))
        self.assertEqual({path: path.read_bytes() for path in (linked, orphan)}, before)

    def test_dry_run_parity_for_report_and_repair(self) -> None:
        self.page("target.md", "target\n")
        source = self.page("source.md", "[[old-target]]\n")
        mapping = self.page("mapping.tsv", "old-target\ttarget\n")
        preview = json.loads(run_cli("link-repair", "--mapping", str(mapping), "--dry-run", "--json", "--vault", str(self.vault)).stdout)
        applied_result = run_cli("link-repair", "--mapping", str(mapping), "--json", "--vault", str(self.vault))
        applied = json.loads(applied_result.stdout)
        self.assertEqual((preview["files_modified"], preview["total_changes"]), (applied["files_modified"], applied["total_changes"]))
        report_preview = json.loads(run_cli("orphan-report", "--dry-run", "--json", "--vault", str(self.vault)).stdout)
        report_live = json.loads(run_cli("orphan-report", "--json", "--vault", str(self.vault)).stdout)
        self.assertEqual(report_preview["details"], report_live["details"])
        self.assertEqual(report_preview["files_modified"], report_live["files_modified"])
        self.assertEqual(report_preview["total_changes"], report_live["total_changes"])
        self.assertEqual(source.read_text(), "[[target]]\n")

class MocGenerationTests(VaultFixture):
    def setUp(self) -> None:
        super().setUp()
        self.page("entities/npc/zara.md", "---\ntitle: Zara Vale\n---\nnpc\n")
        self.page("entities/npc/alpha.md", "---\ntitle: Alpha\n---\npc\n")
        self.page("entities/place/harbor.md", "---\ntitle: Harbor\ntags: [campaign, place]\n---\nplace\n")
        self.page("entities/place/cove.md", "---\ntitle: Cove\n---\nplace\n")
        self.page("entities/creature/a.md", "---\ntitle: A\n---\ncreature\n")
        self.page("entities/creature/b.md", "---\ntitle: B\n---\ncreature\n")
        self.page("index.md", "## Entities\n\n- [[old]] — Old entry. ( #campaign #place)\n")
        self.page("_raw/ignored.md", "raw\n")
        self.page("_meta/ignored.md", "meta\n")
        self.page("attachments/ignored.md", "attachment\n")

    def test_moc_generation_orders_links_excludes_infrastructure_and_is_idempotent(self) -> None:
        stale = self.page("entities/place/place-index.md", "---\ntitle: Places\n---\nstale\n")
        legacy = self.page("entities/npc/npc-index.md", "---\ntitle: Legacy\n---\nstale\n")
        preview = run_cli("moc-generate", "--dry-run", "--json", "--vault", str(self.vault))
        self.assertEqual(preview.returncode, 0, preview.stderr)
        self.assertFalse((self.vault / "entities/entities-index.md").exists())
        self.assertFalse((self.vault / "entities/_index.md").exists())
        self.assertFalse((self.vault / "_raw/_index.md").exists())
        self.assertTrue(stale.exists())
        self.assertTrue(legacy.exists())
        data = json.loads(preview.stdout)
        self.assertGreaterEqual(data["files_modified"], 4)

        applied = run_cli("moc-generate", "--json", "--vault", str(self.vault))
        self.assertEqual(applied.returncode, 0, applied.stderr)
        entities = (self.vault / "entities/_index.md").read_text()
        npc = (self.vault / "entities/npc/_index.md").read_text()
        place = (self.vault / "entities/place/_index.md").read_text()
        creature = (self.vault / "entities/creature/_index.md").read_text()
        self.assertFalse((self.vault / "entities/entities-index.md").exists())
        self.assertFalse((self.vault / "entities/npc/npc-index.md").exists())
        self.assertFalse((self.vault / "entities/place/place-index.md").exists())
        self.assertIn("title: Entities Index", entities)
        self.assertIn("title: Non-Player Characters Index", npc)
        self.assertIn("title: Places Index", place)
        self.assertIn("title: Creature Index", creature)
        self.assertNotIn("#campaign", place)
        self.assertNotIn("#place", place)
        self.assertIn("type: lore", entities)
        self.assertNotIn("lifecycle:", entities)
        self.assertIn("reveal: unrevealed", entities)
        self.assertNotIn("base_confidence:", entities)
        self.assertIn("- [[entities/npc/_index|Non-Player Characters Index]]", entities)
        self.assertIn("- [[entities/npc/alpha|Alpha]]", npc)
        self.assertLess(npc.index("Alpha"), npc.index("Zara Vale"))
        root = (self.vault / "index.md").read_text()
        self.assertIn("- [[entities/_index|Entities Index]]", root)
        self.assertIn("- [[entities/npc/_index|Non-Player Characters Index]]", root)
        self.assertIn("- [[old]] — Old entry.", root)
        self.assertNotIn("#campaign", root)
        self.assertNotIn("#place", root)
        self.assertFalse((self.vault / "_meta/_index.md").exists())
        self.assertFalse((self.vault / "_raw/_index.md").exists())
        repeat = run_cli("moc-generate", "--json", "--vault", str(self.vault))
        self.assertEqual(repeat.returncode, 0, repeat.stderr)
        self.assertEqual(json.loads(repeat.stdout)["files_modified"], 0)

class RawIngestIndexTests(VaultFixture):
    def test_raw_ingest_does_not_append_tags_to_index_entries(self) -> None:
        self.page("index.md", "## Entities\n")
        (self.vault / "entities").mkdir()
        self.page("log.md", "")
        self.page("hot.md", "")
        self.page(".manifest.json", "{}\n")
        source = self.page(
            "_raw/harbor.md",
            "---\ntitle: Harbor\ntype: place\ntags: [campaign, place]\n---\nbody\n",
        )
        result = subprocess.run(
            [PYTHON, str(ROOT / "scripts" / "ingest-raw.py"), "--skip-qmd", "--wiki", str(self.vault), str(source)],
            cwd=ROOT,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        index = (self.vault / "index.md").read_text()
        self.assertIn("- [[harbor]] — Ingested campaign entity.", index)
        self.assertNotIn("#campaign", index)
        self.assertNotIn("#place", index)


class PerformanceSmokeTests(VaultFixture):
    def test_rename_scans_1565_files_under_five_seconds(self) -> None:
        for number in range(782):
            self.page(f"pages/page-{number}.md", f"page {number}\n")
        self.page("old.md", "---\ntitle: Old\n---\n")
        for number in range(782):
            self.page(f"refs/ref-{number}.md", "[[old]]\n")
        started = time.perf_counter()
        result = run_cli("rename", "--old", "old", "--new", "new", "--json", "--vault", str(self.vault))
        elapsed = time.perf_counter() - started
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertLess(elapsed, 5.0)
        self.assertEqual(json.loads(result.stdout)["files_scanned"], 1565)
if __name__ == "__main__":
    unittest.main()
