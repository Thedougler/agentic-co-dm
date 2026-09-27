from __future__ import annotations

import json
import os
import subprocess
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = os.environ.get("PYTHON", str(ROOT / ".venv/bin/python"))


def run_cli(vault: Path, *args: str, extra_env: dict[str, str] | None = None, traces: Path | None = None):
    env = os.environ | {"OBSIDIAN_VAULT_PATH": str(vault)} | (extra_env or {})
    env.pop("CI", None)
    tracker = vault / "_tracker"
    tracker.mkdir(exist_ok=True)
    env.setdefault("WIKI_TRACKER_ROOT", str(tracker))
    env.setdefault("WIKI_EFFICIENCY_TRACE", str(traces or (tracker / "traces.jsonl")))
    return subprocess.run(
        [PYTHON, str(ROOT / "scripts/wiki"), *args],
        cwd=ROOT,
        capture_output=True,
        text=True,
        env=env,
    )


def page(vault: Path, relative: str, *, title: str = "Page") -> None:
    path = vault / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        f"---\ntitle: {title}\n---\n\n# {title}\n\nBody.\n",
        encoding="utf-8",
    )


def payload(result):
    assert result.stdout.strip(), result.stderr
    return json.loads(result.stdout)


def test_render_lint_issues_uses_fields_and_expands_pages():
    from tools.wiki_ops.pretty import render_lint_issues

    text = render_lint_issues({
        "findings": {
            "missing_frontmatter": [{"page": "a.md", "missing": ["summary"], "line": 1}],
            "duplicate_titles": [{"title": "Harbor", "pages": ["a.md", "b.md"], "lines": [2, 3]}],
        }
    })
    assert "a.md:1: missing_frontmatter: missing=summary" in text
    assert "a.md:2: duplicate_titles: title=Harbor" in text
    assert "b.md:3: duplicate_titles: title=Harbor" in text



def test_render_lint_issues_prints_next_path():
    from tools.wiki_ops.pretty import render_lint_issues

    text = render_lint_issues({
        "files": [{"file": "a.md", "findings": [{
            "rule": "TMPL_missing_job", "file": "a.md", "line": 12, "message": "Required Wants is missing",
            "repair_class": "agent_repair",
            "repair_target": "Add required Wants from wiki/templates/faction.md; fill it from page facts.",
        }]}],
        "next": {"path": "a.md", "action": "wiki lint a.md"},
    })
    assert text.endswith("next: a.md")
    assert "fix: Add required Wants from wiki/templates/faction.md; fill it from page facts." in text


def test_lint_default_prints_file_line_issue(tmp_path: Path):
    target = tmp_path / "page.md"
    target.write_text(
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
    result = run_cli(tmp_path, "lint", "page.md")
    assert result.returncode == 1, result.stderr
    assert "page.md:14:" in result.stdout, result.stdout
    assert "broken_links" in result.stdout
    assert "next: page.md" in result.stdout
    assert not result.stdout.lstrip().startswith("{")

    data = payload(run_cli(tmp_path, "lint", "page.md", "--json"))
    broken = [item for group in data["files"] for item in group["findings"] if item["rule"] == "broken_links"]
    assert broken and broken[0]["line"] == 14


def test_lint_default_is_full_and_actionable(tmp_path: Path):
    page(tmp_path, "entities/npc/large.md", title="Large")
    page(tmp_path, "entities/npc/small.md", title="Small")
    (tmp_path / "entities/npc/large.md").write_text(
        (tmp_path / "entities/npc/large.md").read_text(encoding="utf-8") + ("x" * 200),
        encoding="utf-8",
    )
    bulk = run_cli(tmp_path, "lint", "--json")
    assert bulk.returncode in (0, 1), bulk.stderr
    data = payload(bulk)
    required = {
        "status", "counts", "hard_fail", "finding_total", "affected_pages",
        "next_page", "next", "cache", "files_checked", "scope", "ledger", "timing",
        "unique", "backlog", "files",
    }
    assert required <= data.keys()
    assert data["timing"]["command"] == "lint"
    assert data["scope"]["paths"] == []
    assert data["next"]["path"] == "entities/npc/small.md"
    assert data["next"]["bytes"] < (tmp_path / "entities/npc/large.md").stat().st_size
    base_keys = {"rule", "file", "line", "severity", "message"}
    assert all(
        base_keys <= set(item)
        for group in data["files"]
        for item in group["findings"]
    )



def test_multi_path_lint_includes_grouped_findings(tmp_path: Path):
    page(tmp_path, "a.md")
    page(tmp_path, "b.md")
    result = payload(run_cli(tmp_path, "lint", "a.md", "b.md", "--json"))
    assert {item["file"] for item in result["files"]} == {"a.md", "b.md"}

def test_default_lint_includes_soft_and_vale_findings(tmp_path: Path):
    target = tmp_path / "npc.md"
    target.write_text(
        "---\n"
        "title: Vale fixture\n"
        "category: test\n"
        "tags: []\n"
        "sources: []\n"
        "created: 2026-09-01\n"
        "updated: 2026-09-19\n"
        "type: npc\n"
        "reveal: dm\n"
        "---\n\n"
        "# Vale fixture\n\n"
        "## Narrative\n\n"
        "You decide the risk is worth it.\n\n"
        "| **snake_case** |\n",
        encoding="utf-8",
    )
    result = run_cli(tmp_path, "lint", "npc.md", "--json")
    assert result.returncode == 1, result.stderr
    data = payload(result)
    assert "snake_case_labels" in set(data["counts"])
    findings = [item for group in data["files"] for item in group["findings"]]
    assert any(item["rule"] == "snake_case_labels" for item in findings)



    suppressed = run_cli(tmp_path, "lint", "npc.md", "--no-vale")
    assert suppressed.returncode == 2


def test_two_named_files_are_separate_default_blocks(tmp_path: Path):
    page(tmp_path, "entities/npc/one.md", title="One")
    page(tmp_path, "entities/npc/two.md", title="Two")
    result = run_cli(
        tmp_path,
        "lint",
        "entities/npc/two.md",
        "entities/npc/one.md",
        "--json",
    )
    data = payload(result)
    files = [group["file"] for group in data["files"]]
    if len(files) >= 2:
        assert files.index("entities/npc/two.md") < files.index("entities/npc/one.md")


def test_unknown_path_is_structured_error_without_scan(tmp_path: Path):
    page(tmp_path, "entities/npc/one.md")
    started = time.monotonic()
    result = run_cli(tmp_path, "lint", "entities/npcs")
    elapsed = time.monotonic() - started
    assert result.returncode == 2
    assert result.stdout == ""
    assert "path not found in vault: 'entities/npcs'" in result.stderr
    assert elapsed < 1
    data = payload(run_cli(tmp_path, "lint", "entities/npcs", "--json"))
    assert data["error"] == "path not found in vault: 'entities/npcs'" and data["status"] == "error"
    assert data["hint"] and data["example"] and data["list_valid"]



def test_cache_hits_and_byte_change(tmp_path: Path):
    page(tmp_path, "one.md")
    run_cli(tmp_path, "lint")
    second_result = run_cli(tmp_path, "lint", "--json")
    second = payload(second_result)
    assert second_result.returncode in (0, 1)
    assert second["cache"]["hits"] > 0
    assert second["cache"]["vale_skipped"] >= second["cache"]["hits"]
    (tmp_path / "one.md").write_text((tmp_path / "one.md").read_text(encoding="utf-8") + "x", encoding="utf-8")
    changed = payload(run_cli(tmp_path, "lint", "--json"))
    assert changed["cache"]["misses"] >= 1
    unchanged = payload(run_cli(tmp_path, "lint", "--json"))
    assert unchanged["cache"]["hits"] >= 1
    assert unchanged["cache"]["misses"] == 0


def test_scoped_lint_keeps_other_cache_entries(tmp_path: Path):
    page(tmp_path, "a.md")
    page(tmp_path, "b.md")
    run_cli(tmp_path, "lint", "a.md")
    run_cli(tmp_path, "lint", "b.md")
    again = payload(run_cli(tmp_path, "lint", "a.md", "--json"))
    assert again["cache"]["hits"] >= 1


def test_default_lint_is_issues_and_json_is_worklist(tmp_path: Path):
    page(tmp_path, "one.md")
    default = run_cli(tmp_path, "lint")
    worklist = run_cli(tmp_path, "lint", "--json")
    assert not default.stdout.lstrip().startswith("{")
    assert json.loads(worklist.stdout)
    assert "next:" in default.stdout or default.stdout.strip() == "clean"



def test_health_default_matches_lint_shape(tmp_path: Path):
    page(tmp_path, "journal/_index.md", title="Journal Index")
    page(tmp_path, "entities/npc/real.md", title="Real")
    (tmp_path / "journal/_index.md").write_text(
        "---\ntitle: Journal Index\n---\n\n# Journal Index\n\n",
        encoding="utf-8",
    )
    default = run_cli(tmp_path, "health")
    assert default.returncode in (0, 1), default.stderr
    assert not default.stdout.lstrip().startswith("{"), default.stdout[:200]
    assert "journal/_index.md" not in default.stdout
    data = payload(run_cli(tmp_path, "health", "--json"))
    nxt = data.get("next") or {}
    assert not str(nxt.get("path") or "").endswith("_index.md")
    if nxt.get("path"):
        assert nxt["action"].startswith("wiki lint ")
    assert "identity" not in data
    assert "scope" not in (data.get("lint") or {})




def test_health_help_has_copyable_examples():
    result = _bare("health", "--help")
    assert result.returncode == 0, result.stderr
    assert "Examples:" in result.stdout
    assert "wiki health --json" in result.stdout


def test_lint_skips_generated_index(tmp_path: Path):
    page(tmp_path, "journal/_index.md", title="Journal Index")
    page(tmp_path, "entities/npc/real.md", title="Real")
    data = payload(run_cli(tmp_path, "lint", "--json"))
    files = {item["file"] for item in data.get("files") or []}
    assert "journal/_index.md" not in files
    assert "journal/_index.md" not in {row["page"] for row in data.get("backlog") or []}


def test_health_regenerates_moc_without_linting_it(tmp_path: Path):
    page(tmp_path, "entities/npc/alpha.md", title="Alpha")
    page(tmp_path, "entities/npc/bravo.md", title="Bravo")
    index = tmp_path / "entities/npc/_index.md"
    assert not index.exists()
    result = run_cli(tmp_path, "health")
    assert result.returncode in (0, 1), result.stderr
    assert index.is_file()
    data = payload(run_cli(tmp_path, "lint", "--json"))
    files = {item["file"] for item in data.get("files") or []}
    assert "entities/npc/_index.md" not in files





def test_rules_digest_changes_when_styles_change(tmp_path: Path):
    from tools.wiki_ops.lint_cache import digest_rules

    (tmp_path / "styles").mkdir()
    style = tmp_path / "styles" / "Rule.yml"
    style.write_text("a: 1\n", encoding="utf-8")
    (tmp_path / "tools").mkdir()
    (tmp_path / "tools" / "lint_wiki.py").write_text("print(1)\n", encoding="utf-8")
    creative = tmp_path / "tools" / "creative_lint"
    creative.mkdir()
    (creative / "engine.py").write_text("x = 1\n", encoding="utf-8")
    ops = tmp_path / "tools" / "wiki_ops"
    ops.mkdir()
    contracts = ops / "template_contracts.py"
    contracts.write_text("a = 1\n", encoding="utf-8")
    first = digest_rules(tmp_path, extra={"vale": True})
    style.write_text("a: 2\n", encoding="utf-8")
    second = digest_rules(tmp_path, extra={"vale": True})
    contracts.write_text("a = 2\n", encoding="utf-8")
    ops_changed = digest_rules(tmp_path, extra={"vale": True})
    third = digest_rules(tmp_path, extra={"vale": False})
    pyc = creative / "__pycache__"
    pyc.mkdir()
    (pyc / "engine.cpython-314.pyc").write_text("bytecode", encoding="utf-8")
    assert first != second
    assert ops_changed != second
    assert second != third
    assert digest_rules(tmp_path, extra={"vale": False}) == third



def test_lint_fix_deletes_registered_redirect_stub_and_is_idempotent(tmp_path: Path):
    stub = tmp_path / "entities/npc/legacy.md"
    stub.parent.mkdir(parents=True, exist_ok=True)
    stub.write_text(
        "---\n"
        "title: Legacy\n"
        "type: npc\n"
        "redirects_to: entities/npc/current.md\n"
        "---\n\n"
        "# Legacy\n\nUse the canonical page.\n",
        encoding="utf-8",
    )
    first = run_cli(tmp_path, "lint", "fix", "--json", "entities/npc/legacy.md")
    assert first.returncode in (0, 1), first.stderr
    data = payload(first)
    assert data["status"] in {"clean", "findings"}
    assert data["changed_files"] == ["entities/npc/legacy.md"]
    assert any(item["status"] == "applied" for item in data["applied"])
    assert not stub.exists()
    second = run_cli(tmp_path, "lint", "fix", "--json", "entities/npc/legacy.md")
    assert second.returncode == 2
    assert payload(second)["status"] == "error"

def test_lint_fix_reports_same_scope_progress_delta(tmp_path: Path):
    target = tmp_path / "entities/npc/target.md"
    other = tmp_path / "entities/npc/other.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    redirect = (
        "---\n"
        "title: Target\n"
        "type: npc\n"
        "redirects_to: entities/npc/current.md\n"
        "---\n\n"
        "# Target\n\nUse the canonical page.\n"
    )
    target.write_text(redirect, encoding="utf-8")
    other.write_text(redirect.replace("Target", "Other"), encoding="utf-8")

    result = payload(run_cli(tmp_path, "lint", "fix", "--json", "entities/npc/target.md"))
    progress = result["progress"]

    assert result["scope"]["paths"] == ["entities/npc/target.md"]
    assert progress["before_total"] >= progress["after_total"]
    assert progress["changed_files"] == ["entities/npc/target.md"]
    assert progress["state_changed"] is True
    assert isinstance(progress["resolved"], list)
    assert isinstance(progress["next_changed"], bool)
    assert other.exists()


def test_lint_fix_uses_contract_skip_reason_for_unsupported_fixer(tmp_path: Path):
    target = tmp_path / "entities/npc/Bob.md"
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("---\ntitle: Bob\n---\n\n# Bob\n", encoding="utf-8")

    result = payload(run_cli(tmp_path, "lint", "fix", "--json", "entities/npc/Bob.md"))
    reasons = {item["reason"] for item in result["skipped"]}

    assert reasons <= {"unsupported", "unsafe", "conflict", "precondition"}


def _vale_scratch(tmp_path: Path, config_root: Path = ROOT) -> str:
    import shutil

    import pytest

    vale = shutil.which("vale") or str(ROOT / ".venv/bin/vale")
    if not Path(vale).is_file():
        pytest.skip("vale binary is absent")
    scratch = tmp_path / "scratch.md"
    scratch.write_text("# Scratch\n\nThe DM Thesis section names the villain.\n", encoding="utf-8")
    proc = subprocess.run(
        [vale, "--output=line", f"--config={config_root / '.vale.ini'}", str(scratch)],
        cwd=config_root,
        capture_output=True,
        text=True,
    )
    return proc.stdout + proc.stderr


def test_vale_config_loads_without_e100(tmp_path: Path):
    output = _vale_scratch(tmp_path)
    assert "E100" not in output, output


def test_vale_deprecated_dmthesis_fires_with_live_vocabulary(tmp_path: Path):
    import shutil

    from tools.creative_lint.vale_vocab import VOCAB_RELATIVE, render_vocab

    config_root = tmp_path / "config"
    shutil.copytree(ROOT / "styles", config_root / "styles")
    shutil.copy(ROOT / ".vale.ini", config_root / ".vale.ini")
    (config_root / VOCAB_RELATIVE).write_text(render_vocab(ROOT / "wiki"), encoding="utf-8")
    output = _vale_scratch(tmp_path, config_root)
    assert "E100" not in output, output
    assert "Deprecated.DMThesis" in output, output


def test_lint_fix_escapes_table_wikilink_pipes(tmp_path: Path):
    page(tmp_path, "entities/npc/keeper.md", title="Keeper")
    table = tmp_path / "entities/npc/table.md"
    table.write_text(
        "---\ntitle: Table\n---\n\n| Who |\n| --- |\n| [[keeper|The Keeper]] |\n\n[[keeper|prose link]]\n",
        encoding="utf-8",
    )
    before = payload(run_cli(tmp_path, "lint", "entities/npc/table.md", "--json"))
    rules = {item["rule"] for group in before["files"] for item in group["findings"]}
    assert "table_wikilink_unescaped_pipe" in rules
    fixed = run_cli(tmp_path, "lint", "fix", "--json", "entities/npc/table.md")
    assert fixed.returncode in (0, 1), fixed.stderr
    assert "| [[keeper\\|The Keeper]] |" in table.read_text(encoding="utf-8")
    assert "[[keeper|prose link]]" in table.read_text(encoding="utf-8")
    after = payload(run_cli(tmp_path, "lint", "entities/npc/table.md", "--json"))
    rules = {item["rule"] for group in after["files"] for item in group["findings"]}
    assert "table_wikilink_unescaped_pipe" not in rules
    assert "broken_links" not in rules


# --- FR-027–FR-039 contract (contracts/wiki-cli.md), one test per rule class ---

WIKI = [PYTHON, str(ROOT / "scripts/wiki")]


def _bare(*args: str, cwd: Path = ROOT, env: dict[str, str] | None = None, stdin: str | None = None):
    base = os.environ | (env or {})
    base.pop("CI", None)
    return subprocess.run([*WIKI, *args], cwd=cwd, capture_output=True, text=True, env=base,
                          input=stdin if stdin is not None else "", timeout=120)


def _error(result, *, needle: str) -> dict:
    assert result.returncode == 2, result.stdout + result.stderr
    data = payload(result)
    assert {"status", "error", "hint", "example", "list_valid"} <= set(data), data
    assert data["status"] == "error" and needle in data["error"], data
    assert data["error"] in result.stderr
    return data


def test_discovery_from_any_cwd_and_vault_precedence(tmp_path: Path):
    from tools.wiki_ops.cli import repo_root, resolve_vault

    assert repo_root() == ROOT
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    one, two = tmp_path / "one", tmp_path / "two"
    for vault in (one, two):
        page(vault, "a.md")
    env = os.environ | {"OBSIDIAN_VAULT_PATH": str(one)}
    old = os.environ.get("OBSIDIAN_VAULT_PATH")
    try:
        os.environ["OBSIDIAN_VAULT_PATH"] = str(one)
        assert resolve_vault(None) == one.resolve()
        assert resolve_vault(str(two)) == two.resolve()
        del os.environ["OBSIDIAN_VAULT_PATH"]
        assert resolve_vault(None) == (ROOT / "wiki").resolve() or (ROOT / ".env").is_file()
    finally:
        if old is not None:
            os.environ["OBSIDIAN_VAULT_PATH"] = old
    result = run_cli(one, "lint", "a.md", "--vault", str(two), "--json")
    assert payload(result)["vault"] == str(two.resolve())
    result = _bare("lint", "a.md", "--json", cwd=elsewhere, env={"OBSIDIAN_VAULT_PATH": str(one), "WIKI_TRACKER_ROOT": str(elsewhere)})
    assert payload(result)["vault"] == str(one.resolve())


def test_stdin_and_paths_only(tmp_path: Path):
    page(tmp_path, "a.md")
    page(tmp_path, "b.md")
    result = run_cli_stdin(tmp_path, "a.md\nb.md\n", "lint", "--stdin", "--json")
    assert payload(result)["files_checked"] == 2
    paths = run_cli_stdin(tmp_path, "a.md\n", "lint", "--stdin", "--paths-only")
    assert paths.stdout.split() == ["a.md"] or paths.stdout.split() == []


def run_cli_stdin(vault: Path, stdin: str, *args: str):
    env = {"OBSIDIAN_VAULT_PATH": str(vault), "WIKI_TRACKER_ROOT": str(vault / "_tracker")}
    (vault / "_tracker").mkdir(exist_ok=True)
    return _bare(*args, env=env, stdin=stdin)


def test_dry_run_plans_and_repeat_is_already_done(tmp_path: Path):
    stub = tmp_path / "entities/npc/legacy.md"
    stub.parent.mkdir(parents=True, exist_ok=True)
    stub.write_text("---\ntitle: Legacy\ntype: npc\nredirects_to: entities/npc/current.md\n---\n\n# Legacy\n", encoding="utf-8")
    page(tmp_path, "entities/npc/current.md", title="Current")
    planned = payload(run_cli(tmp_path, "lint", "fix", "--json", "dir:entities/npc", "--dry-run"))
    assert planned["status"] == "planned" and planned["planned"] and stub.exists()
    again = payload(run_cli(tmp_path, "lint", "fix", "--json", "dir:entities/npc", "--dry-run"))
    assert again["planned"] == planned["planned"]
    applied = payload(run_cli(tmp_path, "lint", "fix", "--json", "dir:entities/npc"))
    assert applied["changed"] == ["entities/npc/legacy.md"]
    repeat = payload(run_cli(tmp_path, "lint", "fix", "--json", "dir:entities/npc"))
    assert repeat["status"] == "already_done" and repeat["changed"] == []
    op = json.dumps({"kind": "add_tag", "target": "entities/npc/current.md", "selector": {}, "payload": {"tag": "x"}})
    first = payload(run_cli_stdin(tmp_path, op, "mutate", "--stdin"))
    assert first["changed"] == ["entities/npc/current.md"], first
    second = payload(run_cli_stdin(tmp_path, op, "mutate", "--stdin"))
    assert second["status"] == "already_done" and second["changed"] == []
    plan = json.dumps({"actions": [{"target": "entities/npc/current.md", "mutation": {
        "kind": "add_tag", "target": "entities/npc/current.md", "selector": {}, "payload": {"tag": "y"}}}]})
    preview = payload(run_cli_stdin(tmp_path, plan, "repair", "--stdin", "--dry-run"))
    assert preview["status"] == "planned" and preview["changed"] == []
    repaired = payload(run_cli_stdin(tmp_path, plan, "repair", "--stdin"))
    assert repaired["changed"] == ["entities/npc/current.md"], repaired
    again = payload(run_cli_stdin(tmp_path, plan, "repair", "--stdin"))
    assert again["status"] == "already_done" and again["changed"] == [], again


def test_lint_fix_renames_noncanonical_basename_and_rewrites_backlinks(tmp_path: Path):
    page(tmp_path, "entities/place/Belumara.md", title="Belumara")
    (tmp_path / "entities/place/harbor.md").write_text("---\ntitle: harbor\n---\n\nSee [[Belumara]].\n", encoding="utf-8")
    first = payload(run_cli(tmp_path, "lint", "fix", "--json", "dir:entities/place"))
    assert "entities/place/belumara.md" in first["changed"], first
    assert "belumara.md" in os.listdir(tmp_path / "entities/place")  # case-only rename kept the page
    assert "[[belumara]]" in (tmp_path / "entities/place/harbor.md").read_text(encoding="utf-8")
    repeat = payload(run_cli(tmp_path, "lint", "fix", "--json", "dir:entities/place"))
    assert repeat["status"] == "already_done" and repeat["changed"] == []



def _put(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


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


def test_wrong_heading_level_cli_fix_is_idempotent(tmp_path: Path):
    _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    rel = "entities/faction/red-sails.md"
    _put(
        tmp_path / rel,
        "---\ntitle: Red Sails\ntype: faction\nstatus: active\n---\n\n"
        "# Red Sails\n\n**Wants.** Coin.\n\n**Next move.** Bribe.\n\n### Log\n\n- Session 1 — they moved.\n",
    )
    shown = run_cli(tmp_path, "lint", rel)
    assert "TMPL_wrong_level" in shown.stdout
    assert f"fix: wiki lint fix {rel}" in shown.stdout
    first = payload(run_cli(tmp_path, "lint", "fix", "--json", rel))
    text = (tmp_path / rel).read_text(encoding="utf-8")
    assert "\n## Log\n" in text and "### Log" not in text
    assert text.count("## Log") == 1
    second = payload(run_cli(tmp_path, "lint", "fix", "--json", rel))
    assert second["status"] == "already_done"
    assert first["changed_files"] == [rel] or first["changed"] == [rel]



def test_lint_fix_default_prints_remaining_issues(tmp_path: Path):
    _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    rel = "entities/faction/red-sails.md"
    _put(
        tmp_path / rel,
        "---\ntitle: Red Sails\ntype: faction\nstatus: active\n---\n\n"
        "# Red Sails\n\n**Wants.** Coin.\n\n**Next move.** Bribe.\n\n### Log\n\n- Session 1 — they moved.\n",
    )
    result = run_cli(tmp_path, "lint", "fix", rel)
    assert not result.stdout.lstrip().startswith("{")
    assert "next: " in result.stdout


def test_missing_wants_fix_adds_nothing(tmp_path: Path):
    _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    rel = "entities/faction/red-sails.md"
    original = (
        "---\ntitle: Red Sails\ntype: faction\nstatus: active\n---\n\n"
        "# Red Sails\n\n## Log\n\n- Session 1 — they moved.\n"
    )
    path = _put(tmp_path / rel, original)
    shown = run_cli(tmp_path, "lint", rel)
    assert "TMPL_missing_job" in shown.stdout
    run_cli(tmp_path, "lint", "fix", "--json", rel)
    assert path.read_text(encoding="utf-8") == original
    assert "**Wants.**" not in path.read_text(encoding="utf-8")
    assert "[!narration]" not in path.read_text(encoding="utf-8")


def test_missing_optional_narration_is_silent(tmp_path: Path):
    _put(tmp_path / "templates" / "faction.md", _FACTION_TEMPLATE)
    rel = "entities/faction/red-sails.md"
    original = (
        "---\ntitle: Red Sails\ntype: faction\nstatus: active\n---\n\n"
        "# Red Sails\n\n**Wants.** Coin.\n\n**Next move.** Bribe.\n\n## Log\n\n- Session 1 — they moved.\n"
    )
    path = _put(tmp_path / rel, original)
    shown = run_cli(tmp_path, "lint", rel)
    assert "First meeting" not in shown.stdout
    run_cli(tmp_path, "lint", "fix", "--json", rel)
    assert path.read_text(encoding="utf-8") == original


def test_missing_npc_role_is_agent_repair(tmp_path: Path):
    _put(tmp_path / "templates" / "npc.md", _NPC_TEMPLATE)
    rel = "entities/npc/harbour-master.md"
    original = (
        "---\ntitle: Harbour Master\ncategory: entities\ntags: []\nsources: []\n"
        "created: 2026-01-01\nupdated: 2026-01-01\ntype: npc\nreveal: unrevealed\n---\n\n"
        "# Harbour Master\n\n## Statblock\n\n## Log\n"
    )
    path = _put(tmp_path / rel, original)
    data = payload(run_cli(tmp_path, "lint", rel, "--json"))
    findings = [item for group in data["files"] for item in group["findings"]]
    role = [
        item for item in findings
        if item["rule"] in {"missing_frontmatter", "TMPL_missing_frontmatter"}
        and "role" in str(item.get("missing", item))
    ]
    assert role
    assert role[0]["repair_class"] == "agent_repair"
    run_cli(tmp_path, "lint", "fix", "--json", rel)
    assert "role:" not in path.read_text(encoding="utf-8")

