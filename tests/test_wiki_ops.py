from __future__ import annotations

import json
import os
import pytest
import re
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.wiki_ops.index_ops import insert_index_entry, remove_index_entry, replace_index_entry
from tools.wiki_ops.identity import resolve_identity, scan_identities
from tools.wiki_ops.manifest_ops import ManifestTransition, apply_transition
from tools.wiki_ops.mutations import MutationOp, apply_mutation, parse_sections, section_hash
from tools.wiki_ops.repair_plans import build_plan
from tools.wiki_ops.scope import parse_scope
from tools.wiki_ops.transactions import Transaction


ROOT = Path(__file__).resolve().parents[1]
PYTHON = os.environ.get("PYTHON", "python3")


def run_cli(
    script: str | Path,
    *args: str,
    vault: Path | None = None,
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run a repository script with the same isolated-vault setup as bulk ops."""
    script_path = Path(script)
    if not script_path.is_absolute():
        script_path = ROOT / script_path if script_path.parts[:1] == ("scripts",) else ROOT / "scripts" / script_path
    command = [PYTHON, str(script_path), *args]
    environment = os.environ | (extra_env or {})
    if vault is not None:
        environment["OBSIDIAN_VAULT_PATH"] = str(vault)
    return subprocess.run(command, cwd=ROOT, capture_output=True, text=True, env=environment)


def assert_json(result: subprocess.CompletedProcess[str], *, returncode: int = 0) -> dict:
    """Assert a command's public exit/JSON contract and return its object payload."""
    assert result.returncode == returncode, result.stderr or result.stdout
    assert result.stdout.strip(), result.stderr or "command produced no JSON"
    payload = json.loads(result.stdout)
    assert isinstance(payload, dict)
    return payload


def assert_status(
    result: subprocess.CompletedProcess[str],
    status: str,
    *,
    returncode: int = 0,
) -> dict:
    payload = assert_json(result, returncode=returncode)
    assert payload.get("status") == status, payload
    return payload


def assert_file(path: Path, *, text: str | None = None, exists: bool = True) -> None:
    """Assert observable file existence and, when provided, its complete text."""
    assert path.exists() is exists, path
    if exists and text is not None:
        assert path.read_text(encoding="utf-8") == text


class VaultFixture(unittest.TestCase):
    """Temporary vault and public-outcome assertions for subprocess stories."""

    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory(prefix="wiki-ops-")
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

    def assert_json(self, result: subprocess.CompletedProcess[str], *, returncode: int = 0) -> dict:
        return assert_json(result, returncode=returncode)

    def assert_status(
        self,
        result: subprocess.CompletedProcess[str],
        status: str,
        *,
        returncode: int = 0,
    ) -> dict:
        return assert_status(result, status, returncode=returncode)

    def assert_file(self, path: Path, *, text: str | None = None, exists: bool = True) -> None:
        assert_file(path, text=text, exists=exists)


FIXTURE = Path(__file__).parent / "fixtures" / "wiki_ops"


def test_wiki_lint_identity_block_reports_ambiguous_status(tmp_path: Path):
    import shutil

    vault = tmp_path / "vault"
    shutil.copytree(FIXTURE, vault)
    result = run_cli(
        "scripts/wiki-lint", "--json", "--no-vale", "--no-template",
        "--scope", "files:fisks-captains.md,fisks-fleet.md", vault=vault,
    )
    assert result.stdout.strip(), result.stderr
    identity = json.loads(result.stdout)["identity"]
    assert identity["status"] == "ambiguous"
    assert len(identity["ambiguous"]) == 2
    assert identity["scanned"] == 2
    assert identity["compared"] >= 2
    assert set(identity["index"]) == {"hits", "misses"}
    assert (vault / "_meta" / "identity-index.json").is_file()


def test_scope_and_semantic_sections():
    scope = parse_scope("files:fisks-fleet.md")
    assert scope and scope.resolve(FIXTURE).resolved_files == ["fisks-fleet.md"]
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    assert section_hash(section.content) == section.hash


def test_index_and_manifest_corruption_are_rejected_without_partial_state(tmp_path: Path):
    with pytest.raises(ValueError):
        from tools.wiki_ops.index_ops import parse_index
        parse_index("- [[same]]\n- [[same]]\n")
    transition = ManifestTransition("page.md", "merged_into", "canonical.md")
    assert apply_transition({"sources": {}, "page_identity_transitions": []}, transition)["page_identity_transitions"]
    with pytest.raises(ValueError):
        ManifestTransition("../escape.md", "archived").validate()
def test_scoped_lint_uses_full_vault_for_backlinks_and_index(tmp_path: Path):
    # Build fixture from the vault template so it stays in sync with the contract
    template = (ROOT / "wiki" / "templates" / "faction.md").read_text(encoding="utf-8")
    target = template.replace("{{title}}", "Target Faction")
    target = re.sub(r"\[\[([^\]]+)\]\]", r"\1", target)  # strip placeholder wikilinks
    (tmp_path / "entities/faction").mkdir(parents=True)
    (tmp_path / "entities/faction/target-faction.md").write_text(target, encoding="utf-8")
    (tmp_path / "index.md").write_text("- [[target-faction]]\n", encoding="utf-8")
    (tmp_path / "source.md").write_text("[[target-faction]]\n", encoding="utf-8")

    report = assert_json(
        run_cli(
            "scripts/wiki-lint",
            "--json",
            "--scope",
            "files:entities/faction/target-faction.md",
            "--vault",
            tmp_path,
        ),
        returncode=1,
    )
    assert report["findings"].get("orphan_pages", []) == []
    assert report["findings"].get("index_issues", {}).get("missing_from_index", []) == []

def test_default_lint_output_includes_source_line_numbers(tmp_path: Path):
    page = tmp_path / "page.md"
    page.write_text(
        "---\n"
        "title: Line fixture\n"
        "category: test\n"
        "tags: []\n"
        "sources: []\n"
        "created: 2026-09-01\n"
        "updated: 2026-09-17\n"
        "type: session-prep\n"
        "reveal: dm\n"
        "---\n\n"
        "# Line fixture\n\n"
        "A broken edge: [[missing-owner]].\n",
        encoding="utf-8",
    )
    result = run_cli(
        "scripts/wiki-lint",
        "--no-vale",
        "--no-template",
        "--all",
        "--scope",
        "files:page.md",
        "--vault",
        tmp_path,
    )
    assert result.returncode == 1, result.stderr
    assert "page.md:14:" in result.stdout, result.stdout
    assert "broken_links" in result.stdout
    report = assert_json(
        run_cli(
            "scripts/wiki-lint",
            "--json",
            "--no-vale",
            "--no-template",
            "--all",
            "--scope",
            "files:page.md",
            "--vault",
            tmp_path,
        ),
        returncode=1,
    )
    broken = report["findings"]["broken_links"][0]
    assert broken["page"] == "page.md"
    assert broken["line"] == 14
    grouped = report["findings_by_file"]["page.md"]
    assert any(item["rule"] == "broken_links" and item["line"] == 14 for item in grouped)
    assert report["status"] == "findings"
    assert report["findings"]["orphan_pages"] == [{"page": "page.md", "line": 1}]

    verbose = run_cli(
        "scripts/wiki-lint",
        "--json",
        "--verbose",
        "--no-vale",
        "--no-template",
        "--all",
        "--scope",
        "files:page.md",
        "--vault",
        tmp_path,
    )
    verbose_report = assert_json(verbose, returncode=1)
    assert verbose_report["findings"]["orphan_pages"] == [{"page": "page.md", "line": 1}]
    assert verbose_report["counts"]["orphan_pages"] == 1
    clean = tmp_path / "clean.md"
    clean.write_text(
        "---\n"
        "title: Clean fixture\n"
        "category: test\n"
        "tags: []\n"
        "sources: []\n"
        "summary: Clean fixture.\n"
        "created: 2026-09-17\n"
        "updated: 2026-09-17\n"
        "type: session-prep\n"
        "reveal: dm\n"
        "campaign: test\n"
        "session: 1\n"
        "visibility: dm\n"
        "status: draft\n"
        "card: hook\n"
        "---\n\n"
        "# Clean fixture\n",
        encoding="utf-8",
    )
    (tmp_path / "index.md").write_text("- [[clean]]\n", encoding="utf-8")
    clean_result = run_cli(
        "scripts/wiki-lint",
        "--json",
        "--no-vale",
        "--no-template",
        "--all",
        "--scope",
        "files:clean.md",
        "--vault",
        tmp_path,
    )
    clean_report = assert_json(clean_result, returncode=0)
    assert clean_report["status"] == "clean"
    assert clean_report["findings"] == {}
    assert clean_report["counts"] == {}


def test_scoped_lint_keeps_default_vale_in_acceptance_gate(tmp_path: Path):
    page = tmp_path / "page.md"
    page.write_text(
        "---\n"
        "title: Vale gate fixture\n"
        "category: test\n"
        "tags: []\n"
        "sources: []\n"
        "created: 2026-09-01\n"
        "updated: 2026-09-16\n"
        "type: session-prep\n"
        "reveal: dm\n"
        "---\n\n"
        "You decide the risk is worth it.\n",
        encoding="utf-8",
    )
    default = run_cli(
        "scripts/wiki-lint",
        "--json",
        "--scope",
        "files:page.md",
        "--vault",
        tmp_path,
    )
    default_report = assert_json(default, returncode=1)
    assert default_report["hard_fail"] is True
    assert any(rule.startswith("VALE_") for rule in default_report["counts"])
    vale_items = [
        item
        for rule, items in default_report["findings"].items()
        if rule.startswith("VALE_")
        for item in items
    ]
    assert vale_items and all(item["line"] >= 1 for item in vale_items)

    structural_only = run_cli(
        "scripts/wiki-lint",
        "--json",
        "--no-vale",
        "--scope",
        "files:page.md",
        "--vault",
        tmp_path,
    )
    structural_report = assert_json(structural_only, returncode=1)
    assert structural_report["status"] == "findings"
    assert structural_report["counts"]

def test_mutation_hash_and_dry_run():
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    op = MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "Changed\n"})
    preview = apply_mutation(FIXTURE, op, dry_run=True)
    assert preview["status"] == "dry_run"
    assert "Changed" not in (FIXTURE / "fisks-fleet.md").read_text()
    bad = apply_mutation(FIXTURE, MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": "bad"}, {"content": "x"}), dry_run=True)
    assert bad["status"] == "rejected"


def test_index_and_manifest_are_structured():
    text = (FIXTURE / "index.md").read_text()
    text = replace_index_entry(text, "fisks-fleet", "- [[fisks-fleet|Fisk's Fleet]]")
    text = insert_index_entry(text, "- [[another-page]]")
    assert "Fisk's Fleet" in text
    assert "another-page" in text
    assert "fisks-captains" not in remove_index_entry(text, "fisks-captains")
    data = apply_transition({}, ManifestTransition("old.md", "merged_into", "new.md"))
    assert data["page_identity_transitions"][0]["target"] == "new.md"


def test_transaction_rejects_overlapping_mutations():
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    tx = Transaction(FIXTURE)
    tx.add(MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "a"}))
    tx.add(MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "b"}))
    assert tx.commit()["status"] == "rejected"

def test_transaction_finalizes_once_and_retains_committed_files_on_qmd_failure(tmp_path: Path):
    page = tmp_path / "page.md"
    page.write_text("---\ntitle: Page\n---\n# Page\n\nOld\n", encoding="utf-8")
    calls = []
    tx = Transaction(tmp_path, qmd_runner=lambda: calls.append("qmd") or 7)
    content_hash = section_hash(parse_sections(page.read_text(encoding="utf-8")).find(["Page"]).content)
    tx.add(MutationOp("replace_section", "page.md", {"heading_path": ["Page"], "content_hash": content_hash}, {"content": "New"}))
    assert tx.commit()["status"] == "committed"
    first = tx.finalize()
    second = tx.finalize()
    assert first["error"] == "finalization_failed"
    assert second["status"] == "committed"
    assert calls == ["qmd"]
    assert "New" in page.read_text(encoding="utf-8")


def test_identity_fixture_is_deterministic():
    results = scan_identities(FIXTURE)
    assert [result.path for result in results] == sorted(result.path for result in results)
    assert resolve_identity(FIXTURE, "fisks-fleet.md").status == "ambiguous"
    assert resolve_identity(FIXTURE, "fisks-fleet.md").candidates

def test_identity_scan_matches_individual_resolution():
    scanned = {result.path: result.to_dict() for result in scan_identities(FIXTURE)}
    expected = {
        path: resolve_identity(FIXTURE, path).to_dict()
        for path in scanned
    }
    assert scanned == expected

def test_identity_only_compares_same_type(tmp_path: Path):
    base = (FIXTURE / "fisks-fleet.md").read_text()
    (tmp_path / "faction.md").write_text(base, encoding="utf-8")
    (tmp_path / "place.md").write_text(base.replace("type: faction", "type: place").replace("title: Fisk's Fleet", "title: Fisk's Harbor"), encoding="utf-8")
    assert resolve_identity(tmp_path, "faction.md").status == "resolved"

def test_identity_redirect_resolves_without_candidates(tmp_path: Path):
    page = (FIXTURE / "fisks-fleet.md").read_text()
    (tmp_path / "canonical.md").write_text(page.replace("title: Fisk's Fleet", "title: Canonical Fleet"), encoding="utf-8")
    (tmp_path / "redirect.md").write_text(
        page.replace("title: Fisk's Fleet", "title: Redirect Fleet")
        .replace("aliases:", "redirects_to: canonical.md\naliases:", 1),
        encoding="utf-8",
    )
    resolved = resolve_identity(tmp_path, "redirect.md")
    assert resolved.status == "resolved"
    assert resolved.signals["redirect_match"] is True

def test_typed_frontmatter_tag_and_link_mutations_preserve_document_shape(tmp_path: Path):
    page = tmp_path / "page.md"
    page.write_text(
        "---\ntitle: Page\ntags: [old]\n---\n# Page\n\nSee [[old-page]] and ![[old-page.png]].\n",
        encoding="utf-8",
    )
    (tmp_path / "new-page.md").write_text("---\ntitle: New Page\n---\n# New Page\n", encoding="utf-8")
    assert apply_mutation(tmp_path, MutationOp("add_tag", "page.md", payload={"tag": "new"}))["accepted"]
    assert apply_mutation(
        tmp_path,
        MutationOp("set_frontmatter", "page.md", selector={"field": "status"}, payload={"value": "active"}),
    )["accepted"]
    apply_mutation(
        tmp_path,
        MutationOp(
            "repair_links",
            "page.md",
            payload={
                "mapping": [
                    {"old_target": "old-page", "new_target": "new-page"},
                    {"old_target": "old-page.png", "new_target": "new-page.png"},
                ]
            },
        ),
    )
    text = page.read_text(encoding="utf-8")
    assert "tags: [old, new]" in text
    assert "status: active" in text
    assert "[[new-page]]" in text and "![[new-page.png]]" in text


def test_link_repair_rejects_missing_or_ambiguous_page_target(tmp_path: Path):
    page = tmp_path / "page.md"
    page.write_text("---\ntitle: Page\n---\nSee [[old-page]].\n", encoding="utf-8")
    missing = apply_mutation(
        tmp_path,
        MutationOp("repair_links", "page.md", payload={"old_target": "old-page", "new_target": "guessed-page"}),
    )
    assert missing["error"] == "target_not_found"
    assert "[[old-page]]" in page.read_text(encoding="utf-8")


def test_page_rename_supports_case_only_names(tmp_path: Path):
    source = tmp_path / "Page.md"
    destination = tmp_path / "page.md"
    source.write_text("---\ntitle: Page\n---\n# Page\n", encoding="utf-8")
    destination_alias = destination.exists()
    result = apply_mutation(tmp_path, MutationOp("rename_page", "Page.md", payload={"new_target": "page.md"}))
    assert result["accepted"]
    assert destination.read_text(encoding="utf-8").startswith("---")
    if not destination_alias:
        assert not source.exists()


def test_typed_mutation_rejects_invalid_selector_without_writing(tmp_path: Path):
    page = tmp_path / "page.md"
    original = "---\ntitle: Page\n---\n# Page\n"
    page.write_text(original, encoding="utf-8")
    result = apply_mutation(
        tmp_path,
        MutationOp("replace_section", "page.md", selector={"heading_path": ["Missing"]}, payload={"content": "x"}),
    )
    assert result["status"] == "rejected"
    assert page.read_text(encoding="utf-8") == original


def test_scope_and_cli_pipeline_resolve_typed_surface(tmp_path: Path):
    (tmp_path / "entities").mkdir()
    page = tmp_path / "entities" / "guard.md"
    page.write_text("---\ntitle: Guard\ntype: npc\n---\n# Guard\n", encoding="utf-8")
    directory = parse_scope("dir:entities").resolve(tmp_path)
    assert directory.resolved_files == ["entities/guard.md"]
    typed = parse_scope("type:npc").resolve(tmp_path)
    assert typed.resolved_files == ["entities/guard.md"]
    assert resolve_identity(tmp_path, "entities/guard.md").status == "resolved"

def _fake_qmd(path: Path, body: str) -> Path:
    script = path / "qmd"
    script.write_text("#!/bin/sh\nset -eu\n" + body, encoding="utf-8")
    script.chmod(0o755)
    return script


def test_repair_plan_contains_only_allowlisted_deterministic_actions(tmp_path: Path):
    page = tmp_path / "old.md"
    page.write_text("---\ntitle: Old\nredirects_to: new\n---\n# Old\n", encoding="utf-8")
    plan = build_plan(
        tmp_path,
        {"findings": {"templates": [
            {"file": "old.md", "repair_class": "deterministic_repair", "repair_action": "delete_redirect_stub", "target": "new"},
            {"file": "old.md", "repair_class": "agent_repair", "repair_action": "invent_canon"},
        ]}},
    )
    assert [item["action"] for item in plan["actions"]] == ["delete_redirect_stub"]
    assert plan["requires_approval"] is True


def test_repair_plan_skips_dict_vale_actions(tmp_path: Path):
    plan = build_plan(
        tmp_path,
        {"findings": {"VALE_Deprecated.DMThesis": [
            {
                "file": "page.md",
                "repair_class": "deterministic_repair",
                "repair_action": {"kind": "delete_section", "target": "page.md", "selector": {"line": 4}},
            },
        ]}},
    )
    assert plan["actions"] == []


def test_misplaced_entity_is_hard_and_skips_wrong_template(tmp_path: Path):
    page = tmp_path / "entities" / "item" / "snakewood.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\n"
        "title: Snakewood\n"
        "category: entities\n"
        "tags: []\n"
        "sources: []\n"
        "created: 2026-09-01\n"
        "updated: 2026-09-17\n"
        "type: creature\n"
        "reveal: dm\n"
        "---\n\n"
        "# Snakewood\n",
        encoding="utf-8",
    )
    result = run_cli(
        "scripts/wiki-lint",
        "--json",
        "--no-vale",
        "--scope",
        "files:entities/item/snakewood.md",
        "--vault",
        tmp_path,
    )
    report = assert_json(result, returncode=1)
    hits = report["findings"]["misplaced_entity"]
    assert hits[0]["page"] == "entities/item/snakewood.md"
    assert hits[0]["expected"] == "entities/creature/snakewood.md"


def test_moc_is_not_reported_as_misplaced_entity(tmp_path: Path):
    page = tmp_path / "entities" / "creature" / "_index.md"
    page.parent.mkdir(parents=True)
    page.write_text(
        "---\n"
        "title: Creature Index\n"
        "category: entities\n"
        "tags: []\n"
        "sources: []\n"
        "created: 2026-09-17\n"
        "updated: 2026-09-17\n"
        "type: lore\n"
        "reveal: unrevealed\n"
        "---\n\n"
        "- [[entities/creature/bloodhawk|Bloodhawk]]\n",
        encoding="utf-8",
    )
    result = run_cli(
        "scripts/wiki-lint",
        "--json",
        "--no-vale",
        "--scope",
        "files:entities/creature/_index.md",
        "--vault",
        tmp_path,
    )
    report = assert_json(result, returncode=1)
    assert report["findings"].get("misplaced_entity", []) == []



def _run_qmd_hook(temp: Path, *, body: str, extra_env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    _fake_qmd(temp, body)
    env = os.environ | {
        "PATH": f"{temp}:{os.environ['PATH']}",
        "QMD_HOOK_LOCK_DIR": str(temp / "lock"),
    } | (extra_env or {})
    return subprocess.run(
        [str(ROOT / "scripts/qmd-hook.sh")],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=env,
    )


def test_identity_uses_manifest_and_content_signals(tmp_path: Path):
    (tmp_path / "a.md").write_text(
        "---\ntitle: Harbor Guard\ntype: faction\n---\n# Harbor Guard\n\nShared report.\n",
        encoding="utf-8",
    )
    (tmp_path / "b.md").write_text(
        "---\ntitle: Harbor Guard Auxiliary\ntype: faction\n---\n# Harbor Guard\n\nShared report.\n",
        encoding="utf-8",
    )
    (tmp_path / ".manifest.json").write_text(
        json.dumps({"sources": {"source.md": {"pages_produced": ["a.md", "b.md"]}}}),
        encoding="utf-8",
    )
    result = resolve_identity(tmp_path, "a.md")
    assert result.status == "ambiguous"
    assert result.signals["manifest_provenance"] is True
    assert 0 <= result.signals["qmd_content_similarity"] <= 1


def test_identity_raw_drop_is_distinct_and_redirect_is_not_candidate(tmp_path: Path):
    raw = tmp_path / "_raw" / "drop.md"
    raw.parent.mkdir()
    raw.write_text("# Raw drop\n", encoding="utf-8")
    (tmp_path / "canonical.md").write_text(
        "---\ntitle: Canonical\ntype: faction\n---\n# Canonical\n",
        encoding="utf-8",
    )
    (tmp_path / "redirect.md").write_text(
        "---\ntitle: Old Name\ntype: faction\nredirects_to: canonical\n---\n# Old Name\n",
        encoding="utf-8",
    )
    assert resolve_identity(tmp_path, "_raw/drop.md").status == "distinct"
    result = resolve_identity(tmp_path, "canonical.md")
    assert all(item["path"] != "redirect.md" for item in result.candidates)


def test_osset_owner_wins_over_alias(tmp_path: Path):
    npc = tmp_path / "entities" / "npc"
    npc.mkdir(parents=True)
    front = (
        "category: entities\n"
        "tags: []\n"
        "sources: []\n"
        "created: 2026-09-18\n"
        "updated: 2026-09-18\n"
        "type: npc\n"
        "reveal: dm\n"
        "summary: Fixture.\n"
    )
    (npc / "Osset.md").write_text(
        f"---\ntitle: Osset\n{front}---\n\n# Osset\n",
        encoding="utf-8",
    )
    (npc / "talon-vantyrus.md").write_text(
        f"---\ntitle: Talon Vantyrus\naliases: [Osset]\n{front}---\n\n# Talon Vantyrus\n",
        encoding="utf-8",
    )
    (tmp_path / "source.md").write_text("See [[Osset]] and [[talon-vantyrus|Osset]].\n", encoding="utf-8")
    (tmp_path / "index.md").write_text("- [[Osset]]\n- [[talon-vantyrus]]\n- [[source]]\n", encoding="utf-8")
    report = assert_json(
        run_cli("scripts/wiki-lint", "--json", "--no-vale", "--no-template", "--all", "--vault", tmp_path),
        returncode=1,
    )
    orphans = {item["page"] for item in report["findings"].get("orphan_pages", [])}
    missing = {item["page"] for item in report["findings"].get("index_issues", {}).get("missing_from_index", [])}
    assert "entities/npc/Osset.md" not in orphans
    assert "entities/npc/Osset.md" not in missing
    assert "entities/npc/talon-vantyrus.md" not in orphans


def test_named_missing_owner_cannot_be_removed(tmp_path: Path):
    (tmp_path / "page.md").write_text(
        "---\n"
        "title: Page\n"
        "category: test\n"
        "tags: []\n"
        "sources: []\n"
        "created: 2026-09-18\n"
        "updated: 2026-09-18\n"
        "type: lore\n"
        "reveal: dm\n"
        "summary: Fixture.\n"
        "---\n\n"
        "Travel to [[Named Place]]. Ignore [[foo_bar]].\n",
        encoding="utf-8",
    )
    report = assert_json(
        run_cli(
            "scripts/wiki-lint",
            "--json",
            "--no-vale",
            "--no-template",
            "--all",
            "--scope",
            "files:page.md",
            "--vault",
            tmp_path,
        ),
        returncode=1,
    )
    by_target = {item["target"]: item for item in report["findings"]["broken_links"]}
    assert by_target["Named Place"]["repair"] == "mint_owner"
    assert by_target["Named Place"]["class"] == "missing_owner"
    assert by_target["foo_bar"]["repair"] == "remove"
    owners = {item["target"] for item in report["findings"]["missing_owner"]}
    assert "Named Place" in owners
    assert "foo_bar" not in owners
    assert report["next_page"] == "page.md"


def test_lint_reports_noncanonical_basenames_and_slug_collisions(tmp_path: Path):
    def write_page(relative: str, title: str, page_type: str) -> None:
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            "---\n"
            f"title: {title}\n"
            "category: entities\n"
            "tags: []\n"
            "sources: []\n"
            "created: 2026-09-19\n"
            "updated: 2026-09-19\n"
            f"type: {page_type}\n"
                "reveal: unrevealed\n"
            "summary: Fixture.\n"
            "---\n",
            encoding="utf-8",
        )

    write_page("entities/npc/Alice_Name.md", "Alice Name", "npc")
    write_page("entities/npc/alice-name.md", "Alice Name", "npc")
    write_page("entities/faction/Alice_Name.md", "Alice Name", "faction")
    write_page("entities/faction/Bob.md", "Bob", "faction")
    write_page("entities/place/old_port.md", "Old Port", "place")
    write_page("entities/region/old-port.md", "Old Port", "region")

    report = assert_json(
        run_cli(
            "scripts/wiki-lint",
            "--json",
            "--no-vale",
            "--no-template",
            "--all",
            "--vault",
            tmp_path,
        ),
        returncode=1,
    )
    basename_findings = {
        item["page"]: item for item in report["findings"]["noncanonical_basename"]
    }
    assert basename_findings["entities/faction/Bob.md"]["expected"] == "entities/faction/bob.md"
    assert basename_findings["entities/faction/Bob.md"]["repair_class"] == "deterministic_repair"
    assert basename_findings["entities/npc/Alice_Name.md"]["collision"] is True
    assert basename_findings["entities/npc/Alice_Name.md"]["repair_class"] == "agent_repair"
    assert basename_findings["entities/npc/Alice_Name.md"]["repair_action"] is None

    stem_collision = report["findings"]["duplicate_stems"][0]
    assert stem_collision["pages"] == ["entities/faction/Alice_Name.md", "entities/npc/Alice_Name.md"]
    slug_collision = next(
        item for item in report["findings"]["duplicate_slugs"] if item["slug"] == "old-port"
    )
    assert slug_collision["pages"] == ["entities/place/old_port.md", "entities/region/old-port.md"]
    assert slug_collision["repair_class"] == "agent_repair"


def test_lint_wiki_reports_folded_obsidian_markdown_rules(tmp_path: Path):
    vault = tmp_path / "wiki"
    (tmp_path / "concepts").mkdir()
    front = (
        "---\ntitle: {title}\ncategory: test\ntags: []\nsources: []\ncreated: 2026-09-01\n"
        "updated: 2026-09-01\ntype: {type}\nreveal: dm\n---\n\n"
    )

    def write(relative: str, text: str) -> None:
        path = vault / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    write(
        "entities/place/harbor.md",
        front.format(title="Harbor", type="place")
        + "See [the quay](quay.md).\n\n"
        + "![[attachments/missing-map.png]]\n\n"
        + "| Who | Link |\n| --- | --- |\n| Keeper | [[harbor|The Harbor]] |\n| Fine | [[harbor\\|Escaped]] |\n\n"
        + "A literal \\n in a non-session page is not flagged.\n",
    )
    write("attachments/present.png", "png")
    write("journal/notes.md", "---\ntitle: Notes\ncreated: 2026-09-01\n---\n\nBody [[harbor]].\n")
    write(
        "journal/sessions/c/01/beats.md",
        front.format(title="Beats", type="session-prep").replace("reveal: dm\n", "reveal: dm\nsummary: a\\nb\n")
        + "> [!narration]\n> The lock needs a DC 15 check.\n\n"
        + "Prose with a literal \\n token.\n\n"
        + "```statblock\nname: x\\ny\n```\n\n![[present.png]]\n",
    )
    proc = subprocess.run(
        [PYTHON, str(ROOT / "tools/lint_wiki.py"), "--json", str(vault)],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 1, proc.stderr
    findings = json.loads(proc.stdout)["findings"]

    def only(rule: str) -> list[dict]:
        return findings.get(rule, [])

    assert [item["page"] for item in only("md_internal_link")] == ["entities/place/harbor.md"]
    assert [item["page"] for item in only("title_only_frontmatter")] == ["journal/notes.md"]
    assert [item["page"] for item in only("dc_in_narration")] == ["journal/sessions/c/01/beats.md"]
    assert [(item["page"], item["target"]) for item in only("broken_image_link")] == [
        ("entities/place/harbor.md", "attachments/missing-map.png")
    ]
    pipes = only("table_wikilink_unescaped_pipe")
    assert [(item["page"], item["line"]) for item in pipes] == [("entities/place/harbor.md", 18)]
    assert [item["tree"] for item in only("forbidden_tree")] == ["concepts/"]
    newlines = only("literal_newline")
    assert [(item["page"], item["line"]) for item in newlines] == [("journal/sessions/c/01/beats.md", 16)]

    assert pipes[0]["repair_class"] == "deterministic_repair"
    assert pipes[0]["repair_action"]["kind"] == "escape_table_wikilink_pipe"
    for rule in ("md_internal_link", "title_only_frontmatter", "dc_in_narration", "broken_image_link", "forbidden_tree", "literal_newline"):
        assert all(item["repair_class"] == "agent_repair" for item in only(rule)), rule


def _identity_vault(root: Path) -> Path:
    """Build a small typed vault: one near-duplicate pair plus unrelated pages."""
    def page(relative: str, title: str, body: str, page_type: str = "npc") -> None:
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(f"---\ntitle: {title}\ntype: {page_type}\n---\n{body}\n", encoding="utf-8")

    shared = "The harbour master keeps a ledger of every hull that enters the strait. " * 4
    page("entities/npc/harbour-master.md", "Harbour Master", shared)
    page("entities/npc/harbour-keeper.md", "Harbour Keeper", shared + "She hates fog.")
    for index, letter in enumerate("qwxzv"):
        page(f"entities/npc/unrelated-{index}.md", f"Unrelated {index}", letter * (40 + index * 17))
    page("entities/place/quay.md", "Quay", shared, page_type="place")
    page("entities/npc/_index.md", "NPC Index", "Index page.")
    return root


def _identity_dicts(vault: Path, **kwargs) -> list[dict]:
    return [item.to_dict() for item in scan_identities(vault, **kwargs)]


def test_identity_index_cold_warm_and_edit_refresh(tmp_path: Path):
    from tools.wiki_ops.identity import scan_identity_report
    from tools.wiki_ops.lint_cache import identity_index_path

    vault = _identity_vault(tmp_path / "vault")
    cold, cold_stats = scan_identity_report(vault, persist=True)
    assert identity_index_path(vault).is_file()
    warm, warm_stats = scan_identity_report(vault, persist=True)
    assert [item.to_dict() for item in warm] == [item.to_dict() for item in cold]  # (a)
    assert warm_stats["index"] == {"hits": 8, "misses": 0}
    assert cold_stats["index"]["misses"] == 8

    edited = vault / "entities/npc/unrelated-0.md"  # (b)
    edited.write_text(edited.read_text(encoding="utf-8") + "More q.\n", encoding="utf-8")
    after, stats = scan_identity_report(vault, persist=True)
    assert stats["index"] == {"hits": 7, "misses": 1}
    fresh = tmp_path / "fresh"
    import shutil
    shutil.copytree(vault, fresh)
    identity_index_path(fresh).unlink()
    assert [item.to_dict() for item in after] == _identity_dicts(fresh)
    row = json.loads(identity_index_path(vault).read_text(encoding="utf-8"))["rows"]["entities/npc/unrelated-0.md"]
    assert row["size"] == edited.stat().st_size and row["mtime_ns"] == edited.stat().st_mtime_ns
    assert "lifecycle" not in row


def test_identity_index_rebuilds_on_corruption_or_version(tmp_path: Path):
    from tools.wiki_ops.identity import scan_identity_report
    from tools.wiki_ops.lint_cache import identity_index_path

    vault = _identity_vault(tmp_path)
    expected = _identity_dicts(vault)
    scan_identity_report(vault, persist=True)
    path = identity_index_path(vault)
    for broken in ("{", json.dumps({**json.loads(path.read_text(encoding="utf-8")), "version": 99})):  # (c)
        path.write_text(broken, encoding="utf-8")
        results, stats = scan_identity_report(vault, persist=True)
        assert [item.to_dict() for item in results] == expected
        assert stats["index"] == {"hits": 0, "misses": 8}
        assert json.loads(path.read_text(encoding="utf-8"))["version"] == 1


def test_identity_index_drops_deleted_rows_and_prunes_pairs(tmp_path: Path):
    from tools.wiki_ops.identity import scan_identity_report
    from tools.wiki_ops.lint_cache import identity_index_path

    vault = _identity_vault(tmp_path)
    scan_identity_report(vault, persist=True)
    before = json.loads(identity_index_path(vault).read_text(encoding="utf-8"))
    gone = before["rows"]["entities/npc/harbour-keeper.md"]["content_sha256"]
    assert any(gone in key for key in before["pairs"])
    (vault / "entities/npc/harbour-keeper.md").unlink()  # (d)
    scan_identity_report(vault, persist=True)
    after = json.loads(identity_index_path(vault).read_text(encoding="utf-8"))
    assert "entities/npc/harbour-keeper.md" not in after["rows"]
    assert not any(gone in key for key in after["pairs"])


def test_identity_scoped_run_compares_selected_and_candidates_only(tmp_path: Path):
    from tools.wiki_ops.identity import scan_identity_report

    vault = _identity_vault(tmp_path)
    scope = parse_scope("files:entities/npc/harbour-master.md").resolve(vault)
    results, stats = scan_identity_report(vault, scope=scope)  # (e)
    assert [item.path for item in results] == ["entities/npc/harbour-master.md"]
    assert stats["scanned"] == 1
    assert stats["compared"] == 2 < 8


def test_identity_index_resolution_matches_cold_walk(tmp_path: Path):
    from tools.wiki_ops.identity import _path_for, scan_identity_report
    from tools.wiki_ops.lint_cache import identity_index_path

    vault = _identity_vault(tmp_path).resolve()
    cold = {raw: resolve_identity(vault, raw).to_dict() for raw in ("harbour-master", "entities/npc/unrelated-2.md", "_index")}
    cold_paths = {raw: _path_for(vault, raw) for raw in ("harbour-keeper", "_index", "entities/place/quay.md")}
    scan_identity_report(vault, persist=True)  # (f)
    assert identity_index_path(vault).is_file()
    assert {raw: resolve_identity(vault, raw).to_dict() for raw in cold} == cold
    assert {raw: _path_for(vault, raw) for raw in cold_paths} == cold_paths


def test_rules_digest_change_keeps_identity_index(tmp_path: Path):
    from tools.wiki_ops import lint_cache
    from tools.wiki_ops.identity import scan_identity_report

    vault = _identity_vault(tmp_path)
    cache = lint_cache.load_cache(vault)
    lint_cache.update_entry(cache, vault, "entities/place/quay.md", "digest-1", {}, {})
    lint_cache.save_cache(vault, cache)
    scan_identity_report(vault, persist=True)
    pairs = json.loads(lint_cache.identity_index_path(vault).read_text(encoding="utf-8"))["pairs"]
    assert lint_cache.lookup_entry(lint_cache.load_cache(vault), vault, "entities/place/quay.md", "digest-2") is None  # (g)
    _, stats = scan_identity_report(vault, persist=True)
    assert stats["index"]["misses"] == 0
    assert json.loads(lint_cache.identity_index_path(vault).read_text(encoding="utf-8"))["pairs"] == pairs


def test_identity_threshold_lists_candidates_without_choosing(tmp_path: Path):
    vault = _identity_vault(tmp_path)
    results = {item.path: item for item in scan_identities(vault)}  # (h)
    master = results["entities/npc/harbour-master.md"]
    keeper = results["entities/npc/harbour-keeper.md"]
    assert master.status == keeper.status == "ambiguous"
    assert [item["path"] for item in master.candidates] == ["entities/npc/harbour-keeper.md"]
    assert [item["path"] for item in keeper.candidates] == ["entities/npc/harbour-master.md"]
    assert "canonical_path" not in master.signals and "canonical_path" not in keeper.signals
    assert all(item.status == "resolved" for path, item in results.items() if "unrelated" in path)


def _put(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def _rules(findings: list[dict]) -> list[str]:
    return [str(item.get("rule_id") or item.get("rule")) for item in findings]


_FACTION_TEMPLATE = """\
---
title: "{{title}}"
type: faction
status: active
---

# {{title}}

*Smuggling ring*

<!-- Required when status is active. -->

**Wants.** The concrete change they are after.

**Next move.** What they attempt next.

> [!narration] First meeting
> <!-- Optional: the moment the party first meets them. -->

## Log

<!-- Required. -->

- **[[Session]]** — what changed.
"""

_NPC_TEMPLATE = """\
---
title: "{{title}}"
type: npc
role: ""
---

# {{title}}

## Statblock

## Log
"""


def _faction_page(*, status: str, wants: bool = False, log: str | None = "## Log") -> str:
    wants_block = "**Wants.** Coin on the quay.\n\n**Next move.** Bribe the clerk.\n\n" if wants else ""
    log_block = f"\n{log}\n\n- Session 1 — they moved.\n" if log else ""
    return (
        "---\n"
        "title: Red Sails\n"
        "type: faction\n"
        f"status: {status}\n"
        "---\n\n"
        "# Red Sails\n\n"
        f"{wants_block}"
        f"{log_block}"
    )


def test_required_body_job_tracks_template_comment(tmp_path: Path):
    from tools.wiki_ops.template_contracts import check_conformance, derive_contract

    template = _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    active = _faction_page(status="active", wants=False)
    dormant = _faction_page(status="dormant", wants=False)
    contract = derive_contract(template)
    active_findings = check_conformance("entities/faction/red-sails.md", active, contract)
    assert "TMPL_missing_job" in _rules(active_findings)
    wants = [item for item in active_findings if item.get("rule_id") == "TMPL_missing_job"]
    assert any("Wants" in str(item.get("repair_target", "")) or "Wants" in str(item.get("reason", "")) for item in wants)
    dormant_findings = check_conformance("entities/faction/red-sails.md", dormant, contract)
    assert not any(
        item.get("rule_id") == "TMPL_missing_job" and "Wants" in str(item)
        for item in dormant_findings
    )

    template.write_text(_FACTION_TEMPLATE.replace("Required when status is active.", "Required."), encoding="utf-8")
    required = derive_contract(template)
    now_required = check_conformance("entities/faction/red-sails.md", dormant, required)
    assert any(
        item.get("rule_id") == "TMPL_missing_job" and "Wants" in str(item)
        for item in now_required
    )


def test_placeholder_heading_is_not_extra(tmp_path: Path):
    from tools.wiki_ops.repair_plans import build_safe_fix_plan
    from tools.wiki_ops.template_contracts import check_conformance, derive_contract

    template = _put(
        tmp_path / "templates" / "place.md",
        "---\ntitle: \"{{title}}\"\ntype: place\n---\n\n# {{title}}\n\n## {Area}\n",
    )
    page = (
        "---\ntitle: Keep\ntype: place\n---\n\n"
        "# Keep\n\n## Gatehouse\n\nGuards.\n\n## Cellar\n\nStores.\n"
    )
    findings = check_conformance("entities/place/keep.md", page, derive_contract(template))
    assert "TMPL002" not in _rules(findings)
    _put(tmp_path / "entities/place/keep.md", page)
    ops, _skipped = build_safe_fix_plan(tmp_path, findings, scope={"paths": ["entities/place/keep.md"]})
    for operation in ops:
        apply_mutation(tmp_path, operation)
    text = (tmp_path / "entities/place/keep.md").read_text(encoding="utf-8")
    assert "{Area}" not in text
    assert text.count("## ") == 2


def test_improvised_heading_names_template_slots(tmp_path: Path):
    from tools.wiki_ops.template_contracts import check_conformance, derive_contract

    template = _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    page = (
        "---\ntitle: Red Sails\ntype: faction\nstatus: active\n---\n\n"
        "# Red Sails\n\n**Wants.** Coin.\n\n**Next move.** Bribe.\n\n"
        "# Notes\n\nAside.\n\n## Agenda\n\nThey buy the quay.\n\n## Log\n\n- Session 1 — they moved.\n"
    )
    extras = [
        item for item in check_conformance("entities/faction/red-sails.md", page, derive_contract(template))
        if item.get("rule_id") == "TMPL002"
    ]
    names = {item["section"] for item in extras}
    assert names == {"Notes", "Agenda"}
    extra = extras[0]
    assert extra["repair_class"] == "agent_repair"
    assert extra["reason"].startswith("Heading '")
    assert extra["reason"].endswith("is not in wiki/templates/faction.md")
    target = extra["repair_target"]
    assert target == "Conform headings to wiki/templates/faction.md; keep page facts."
    assert "**Wants.**" not in target
    assert "## Log" not in target





def test_wrong_heading_level_is_deterministic_fix(tmp_path: Path):
    from tools.wiki_ops.repair_plans import apply_safe_fix_plan, build_safe_fix_plan
    from tools.wiki_ops.template_contracts import check_conformance, derive_contract

    template = _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    rel = "entities/faction/red-sails.md"
    page = _faction_page(status="active", wants=True, log="### Log")
    _put(tmp_path / rel, page)
    findings = check_conformance(rel, page, derive_contract(template))
    level = next(item for item in findings if item.get("rule_id") == "TMPL_wrong_level")
    assert level["repair_class"] == "deterministic_repair"
    action = level["repair_action"]
    assert (action.get("kind") if isinstance(action, dict) else action) == "set_heading_level"
    ops, _skipped = build_safe_fix_plan(tmp_path, findings, scope={"paths": [rel]})
    assert ops
    applied, _failed = apply_safe_fix_plan(tmp_path, ops)
    assert applied
    text = (tmp_path / rel).read_text(encoding="utf-8")
    assert "\n## Log\n" in text
    assert "### Log" not in text
    assert text.count("## Log") == 1
    again, _skipped = build_safe_fix_plan(
        tmp_path,
        check_conformance(rel, text, derive_contract(template)),
        scope={"paths": [rel]},
    )
    assert again == []


def test_section_reorder_is_deterministic_when_permutation(tmp_path: Path):
    from tools.wiki_ops.repair_plans import apply_safe_fix_plan, build_safe_fix_plan
    from tools.wiki_ops.template_contracts import check_conformance, derive_contract

    template = _put(tmp_path / "templates" / "npc.md", _NPC_TEMPLATE)
    rel = "entities/npc/harbour-master.md"
    page = (
        "---\ntitle: Harbour Master\ntype: npc\nrole: face\n---\n\n"
        "# Harbour Master\n\n## Log\n\n- Session 1 — spoke.\n\n## Statblock\n\nAC 12.\n"
    )
    _put(tmp_path / rel, page)
    findings = check_conformance(rel, page, derive_contract(template))
    order = next(item for item in findings if item.get("rule_id") == "TMPL003")
    assert order["repair_class"] == "deterministic_repair"
    ops, _skipped = build_safe_fix_plan(tmp_path, findings, scope={"paths": [rel]})
    apply_safe_fix_plan(tmp_path, ops)
    text = (tmp_path / rel).read_text(encoding="utf-8")
    assert text.index("## Statblock") < text.index("## Log")
    assert "# Harbour Master" in text
    assert text.count("## Statblock") == 1 and text.count("## Log") == 1


def test_missing_required_is_agent_repair_and_fix_adds_nothing(tmp_path: Path):
    from tools.wiki_ops.repair_plans import apply_safe_fix_plan, build_safe_fix_plan
    from tools.wiki_ops.template_contracts import check_conformance, derive_contract

    template = _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    rel = "entities/faction/red-sails.md"
    page = _faction_page(status="active", wants=True, log=None)
    path = _put(tmp_path / rel, page)
    before = path.read_bytes()
    findings = check_conformance(rel, page, derive_contract(template))
    missing = next(item for item in findings if item.get("rule_id") == "TMPL_missing_required")
    assert missing["repair_class"] == "agent_repair"
    assert "wiki/templates/faction.md" in str(missing.get("repair_target", ""))
    ops, _skipped = build_safe_fix_plan(tmp_path, findings, scope={"paths": [rel]})
    apply_safe_fix_plan(tmp_path, ops)
    assert path.read_bytes() == before
    assert "## Log" not in path.read_text(encoding="utf-8")


def test_missing_optional_is_not_a_finding_and_fix_adds_nothing(tmp_path: Path):
    from tools.wiki_ops.repair_plans import apply_safe_fix_plan, build_safe_fix_plan
    from tools.wiki_ops.template_contracts import check_conformance, derive_contract

    template = _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    rel = "entities/faction/red-sails.md"
    page = _faction_page(status="active", wants=True)
    path = _put(tmp_path / rel, page)
    before = path.read_bytes()
    findings = check_conformance(rel, page, derive_contract(template))
    blob = " ".join(str(item) for item in findings)
    assert "First meeting" not in blob
    ops, _skipped = build_safe_fix_plan(tmp_path, findings, scope={"paths": [rel]})
    apply_safe_fix_plan(tmp_path, ops)
    assert path.read_bytes() == before
    assert "[!narration] First meeting" not in path.read_text(encoding="utf-8")


def test_template_frontmatter_keys_are_agent_repair(tmp_path: Path):
    from tools.wiki_ops.repair_plans import apply_safe_fix_plan, build_safe_fix_plan

    _put(tmp_path / "templates" / "npc.md", _NPC_TEMPLATE)
    rel = "entities/npc/harbour-master.md"
    page = (
        "---\ntitle: Harbour Master\ncategory: entities\ntags: []\nsources: []\n"
        "created: 2026-01-01\nupdated: 2026-01-01\ntype: npc\nreveal: unrevealed\n---\n\n"
        "# Harbour Master\n\n## Statblock\n\n## Log\n"
    )
    path = _put(tmp_path / rel, page)
    report = assert_json(
        run_cli("scripts/wiki-lint", "--json", "--no-vale", "--scope", f"files:{rel}", "--vault", tmp_path),
        returncode=1,
    )
    missing = report["findings"].get("missing_frontmatter") or []
    if not missing:
        files = report.get("findings_by_file", {}).get(rel, [])
        missing = [item for item in files if item.get("rule") in {"missing_frontmatter", "TMPL_missing_frontmatter"}]
    assert missing
    record = missing[0]
    assert record.get("repair_class") == "agent_repair"
    target = str(record.get("repair_target", ""))
    assert "role" in str(record.get("missing", record)) or "role" in target
    assert "wiki/templates/npc.md" in target
    findings = []
    for items in (report.get("findings") or {}).values():
        if isinstance(items, list):
            findings.extend(item for item in items if isinstance(item, dict))
    ops, _skipped = build_safe_fix_plan(tmp_path, findings, scope={"paths": [rel]})
    apply_safe_fix_plan(tmp_path, ops)
    assert "role:" not in path.read_text(encoding="utf-8")


def test_fix_hint_prints_repair_target():
    from tools.wiki_ops.pretty import render_lint_issues

    text = render_lint_issues({
        "files": [{
            "file": "entities/faction/red-sails.md",
            "findings": [{
                "rule": "TMPL_missing_job",
                "file": "entities/faction/red-sails.md",
                "line": 12,
                "message": "Required Wants is missing",
                "repair_class": "agent_repair",
                "repair_target": "Add required Wants from wiki/templates/faction.md; fill it from page facts.",
            }],
        }],
    })
    assert "fix: Add required Wants from wiki/templates/faction.md; fill it from page facts." in text



def test_next_action_skips_fix_when_only_agent_repair():
    from tools.wiki_ops.worklist import build_worklist

    result = build_worklist(
        [{"rule": "TMPL_missing_job", "file": "a.md", "line": 1, "repair_class": "agent_repair",
          "repair_target": "Add required Wants from wiki/templates/faction.md; fill it from page facts."}],
        files_checked=1,
        page_bytes={"a.md": 12},
        full=True,
    )
    assert result["next"]["path"] == "a.md"
    assert result["next"]["action"] == "wiki lint a.md"


def test_next_action_names_fix_when_deterministic():
    from tools.wiki_ops.worklist import build_worklist

    result = build_worklist(
        [{"rule": "TMPL_wrong_level", "file": "a.md", "line": 4, "repair_class": "deterministic_repair",
          "repair_action": {"kind": "set_heading_level"}}],
        files_checked=1,
        page_bytes={"a.md": 12},
        full=True,
    )
    assert result["next"]["action"] == "wiki lint fix a.md, then wiki lint a.md"

