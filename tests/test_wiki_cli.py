from __future__ import annotations

import json
import os
import stat
import subprocess
import time
from pathlib import Path

from tools.wiki_ops.timing import HEARTBEAT_INTERVAL_S, ProgressHeartbeat
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



def test_unified_mutation_uses_configured_vault_and_relative_paths(tmp_path: Path):
    page(tmp_path, "page.md")
    result = run_cli(tmp_path, "mutate", "add_tag", "--file", "page.md", "--tag", "new")
    assert result.returncode == 0, result.stderr
    data = payload(result)
    assert data["status"] == "applied"
    assert "tags: [new]" in (tmp_path / "page.md").read_text(encoding="utf-8")

def test_lint_default_is_full_and_actionable(tmp_path: Path):
    page(tmp_path, "entities/npc/large.md", title="Large")
    page(tmp_path, "entities/npc/small.md", title="Small")
    (tmp_path / "entities/npc/large.md").write_text(
        (tmp_path / "entities/npc/large.md").read_text(encoding="utf-8") + ("x" * 200),
        encoding="utf-8",
    )
    bulk = run_cli(tmp_path, "lint")
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

    compatibility = payload(run_cli(tmp_path, "lint", "--full"))
    assert compatibility["finding_total"] == data["finding_total"]
    assert compatibility["files"]

def test_multi_path_lint_includes_grouped_findings(tmp_path: Path):
    page(tmp_path, "a.md")
    page(tmp_path, "b.md")
    result = payload(run_cli(tmp_path, "lint", "a.md", "b.md"))
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
    result = run_cli(tmp_path, "lint", "npc.md")
    assert result.returncode == 1, result.stderr
    data = payload(result)
    assert "snake_case_labels" in set(data["counts"])
    findings = [item for group in data["files"] for item in group["findings"]]
    assert any(item["rule"] == "snake_case_labels" for item in findings)

    compatibility = payload(run_cli(tmp_path, "lint", "npc.md", "--full"))
    compatibility_findings = [item for group in compatibility["files"] for item in group["findings"]]
    assert any(item["rule"] == "snake_case_labels" for item in compatibility_findings)

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
    data = payload(result)
    assert data["error"] == "path not found in vault: 'entities/npcs'" and data["status"] == "error"
    assert data["hint"] and data["example"] and data["list_valid"]
    assert elapsed < 1
    pretty = run_cli(tmp_path, "lint", "entities/npcs", "--pretty")
    assert pretty.returncode == 2
    assert pretty.stdout == ""
    assert pretty.stderr.strip().startswith("error:")


def test_cache_hits_and_byte_change(tmp_path: Path):
    page(tmp_path, "one.md")
    run_cli(tmp_path, "lint")
    second_result = run_cli(tmp_path, "lint", "--json")
    second = payload(second_result)
    assert second_result.returncode in (0, 1)
    assert second["cache"]["hits"] > 0
    assert second["cache"]["vale_skipped"] >= second["cache"]["hits"]
    (tmp_path / "one.md").write_text((tmp_path / "one.md").read_text(encoding="utf-8") + "x", encoding="utf-8")
    changed = payload(run_cli(tmp_path, "lint"))
    assert changed["cache"]["misses"] >= 1
    unchanged = payload(run_cli(tmp_path, "lint"))
    assert unchanged["cache"]["hits"] >= 1
    assert unchanged["cache"]["misses"] == 0

def test_cache_version_and_mapped_template_invalidation(tmp_path: Path, monkeypatch):
    from tools.wiki_ops import lint_cache

    page_file = tmp_path / "page.md"
    page_file.write_text("---\ntype: npc\n---\npage\n", encoding="utf-8")
    template_dir = tmp_path / "repo" / "wiki" / "templates"
    template_dir.mkdir(parents=True)
    template = template_dir / "npc.md"
    template.write_text("template-v1\n", encoding="utf-8")
    unrelated = template_dir / "item.md"
    unrelated.write_text("unrelated-v1\n", encoding="utf-8")
    monkeypatch.setattr(lint_cache, "_REPO_ROOT", tmp_path / "repo")
    cache = lint_cache.load_cache(tmp_path)
    entry = lint_cache.update_entry(cache, tmp_path, "page.md", "rules-v1", {}, {})
    assert cache["version"] == lint_cache.CACHE_VERSION
    assert entry["template_sha256"] == lint_cache.sha256_file(template)
    lint_cache.save_cache(tmp_path, cache)
    assert lint_cache.lookup_entry(lint_cache.load_cache(tmp_path), tmp_path, "page.md", "rules-v1")

    unrelated.write_text("unrelated-v2\n", encoding="utf-8")
    assert lint_cache.lookup_entry(lint_cache.load_cache(tmp_path), tmp_path, "page.md", "rules-v1")
    template.write_text("template-v2\n", encoding="utf-8")
    assert lint_cache.lookup_entry(lint_cache.load_cache(tmp_path), tmp_path, "page.md", "rules-v1") is None

    raw = json.loads(lint_cache.cache_path(tmp_path).read_text(encoding="utf-8"))
    raw["version"] = lint_cache.CACHE_VERSION - 1
    lint_cache.cache_path(tmp_path).write_text(json.dumps(raw), encoding="utf-8")
    fresh = lint_cache.load_cache(tmp_path)
    assert fresh["version"] == lint_cache.CACHE_VERSION
    assert fresh["entries"] == {}



def test_scoped_lint_keeps_other_cache_entries(tmp_path: Path):
    page(tmp_path, "a.md")
    page(tmp_path, "b.md")
    run_cli(tmp_path, "lint", "a.md")
    run_cli(tmp_path, "lint", "b.md")
    again = payload(run_cli(tmp_path, "lint", "a.md"))
    assert again["cache"]["hits"] >= 1


def test_pretty_default_lists_findings_and_full_is_compatible(tmp_path: Path):
    page(tmp_path, "one.md")
    default = run_cli(tmp_path, "lint")
    pretty = run_cli(tmp_path, "lint", "--pretty")
    pretty_full = run_cli(tmp_path, "lint", "--pretty", "--full")
    assert json.loads(default.stdout)
    assert pretty.stdout.strip()
    assert not pretty.stdout.lstrip().startswith("{")
    assert "Next page:" in pretty.stdout
    assert pretty_full.stdout == pretty.stdout


def test_query_compact_hits_and_backend_failure(tmp_path: Path):
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    qmd = bin_dir / "qmd"
    qmd.write_text(
        "#!/bin/sh\nprintf '%s\\n' '{\"results\":[{\"title\":\"Known\",\"path\":\"entities/npc/one.md\",\"id\":\"#abc\"}]}'\n",
        encoding="utf-8",
    )
    qmd.chmod(qmd.stat().st_mode | stat.S_IXUSR)
    env = {"PATH": str(bin_dir) + os.pathsep + os.environ.get("PATH", ""), "CI": "true"}
    result = run_cli(tmp_path, "query", "Known", extra_env=env)
    assert result.returncode == 0, result.stderr
    data = payload(result)
    assert data["status"] == "ok"
    assert data["collection"] == "wiki"
    assert data["hits"] == [{"title": "Known", "path": "entities/npc/one.md", "id": "#abc"}]
    assert data["timing"]["command"] == "query"
    assert "snippets" not in data

    broken = bin_dir / "qmd"
    broken.write_text("#!/bin/sh\necho fail >&2\nexit 1\n", encoding="utf-8")
    broken.chmod(broken.stat().st_mode | stat.S_IXUSR)
    failed = run_cli(tmp_path, "query", "Known", extra_env=env)
    assert failed.returncode == 2
    error = payload(failed)
    assert error["status"] == "error"
    assert "hits" not in error


def test_health_alias_trends_focus_and_empty_trackers(tmp_path: Path):
    page(tmp_path, "one.md")
    traces = tmp_path / "_tracker" / "traces.jsonl"
    health = run_cli(tmp_path, "health", traces=traces)
    env = os.environ | {
        "OBSIDIAN_VAULT_PATH": str(tmp_path),
        "WIKI_TRACKER_ROOT": str(tmp_path / "_tracker"),
        "WIKI_EFFICIENCY_TRACE": str(traces),
    }
    alias = subprocess.run(
        [PYTHON, str(ROOT / "scripts/wiki-maintain"), "--report"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
    )
    assert health.returncode in (0, 1), health.stderr
    data = payload(health)
    required = {"pages", "bytes", "tokens", "lint", "trends", "focus", "next", "timing", "waste", "staging", "remorph", "policy", "context"}
    assert required <= data.keys()
    assert "files" not in data
    assert "files" not in data["lint"]
    assert len(data["focus"]) <= 5
    assert data["next"] == (data["focus"][0] if data["focus"] else None)
    trends = data["trends"]
    assert {"sittings", "skills", "errors", "efficiency", "slowest_commands", "token_heaviest"} <= trends.keys()
    assert trends["sittings"]["count"] == 0
    assert "skill_eval" not in data and "evals" not in trends
    assert alias.returncode == health.returncode, alias.stderr
    alias_data = payload(alias)
    assert set(alias_data) == set(data)
    assert alias_data["pages"] == data["pages"]
    assert alias_data["next"] == data["next"]
    assert "files" not in alias_data

    run_cli(tmp_path, "lint", traces=traces)
    run_cli(tmp_path, "query", "x", extra_env={"PATH": tmp_path.as_posix()}, traces=traces)
    later = payload(run_cli(tmp_path, "health", traces=traces))
    commands = [row["command"] for row in later["trends"]["slowest_commands"]]
    assert "lint" in commands or "health" in commands

    sitting = {
        "sitting_class": "prep",
        "kind": "prep",
        "job": "heavy",
        "trajectory": {"request": 10, "final_work": 90},
    }
    traces.write_text(traces.read_text(encoding="utf-8") + json.dumps(sitting) + "\n", encoding="utf-8")
    heavy = payload(run_cli(tmp_path, "health", traces=traces))
    assert heavy["trends"]["token_heaviest"]
    assert heavy["trends"]["token_heaviest"][0]["tokens"] >= 100


def test_health_explains_blockers_and_small_error_ledger():
    from tools.wiki_ops.health import build_health_snapshot, build_trends

    snapshot = build_health_snapshot(
        status="findings",
        pages=827,
        bytes=0,
        tokens=None,
        lint={
            "status": "findings",
            "counts": {"template_conformance": 5475},
            "hard_fail": True,
            "backlog": [{"page": f"page-{index}.md", "findings": 1, "bytes": index} for index in range(827)],
        },
        waste=None,
        staging=None,
        remorph=None,
        policy=None,
        trends=build_trends(
            None,
            {"entries": [{"id": f"e-{index}", "cause": f"cause-{index}", "source": "scripts/wiki",
                          "evidence": [{"sitting": "lint: a", "detail": f"cause-{index}"}]} for index in range(5)],
             "recurrence": {"total": 0, "by_sitting": {}}, "missing_sources": []},
            None,
        ),
        focus=[{"path": "page-0.md", "reason": "template_conformance lint findings", "source": "lint"}],
        context={"act": ["Repair hot.md: snapshot is oversized."]},
    )

    lint = snapshot["lint"]
    assert lint["finding_total"] == 5475
    assert lint["affected_pages"] == 827
    assert lint["blocking"] == [{"rule": "template_conformance", "findings": 5475}]
    assert "blocking lint findings" in lint["meaning"]
    assert lint["action"].startswith("Repair")
    assert snapshot["next"]["action"].endswith("rerun wiki health.")
    assert len(snapshot["trends"]["errors"]["entries"]) == 5
    assert "core" not in snapshot["context"]

def test_context_load_ranks_files_skills_and_trend(tmp_path: Path):
    from tools.wiki_ops.health import build_context_load

    (tmp_path / ".omp").mkdir()
    (tmp_path / ".omp" / "AGENTS.md").write_text("first-turn " * 80, encoding="utf-8")
    (tmp_path / "AGENTS.md").write_text("repo", encoding="utf-8")
    vault = tmp_path / "wiki"
    vault.mkdir()
    (vault / "AGENTS.md").write_text("vault agents", encoding="utf-8")
    (vault / "hot.md").write_text("hot", encoding="utf-8")
    big = tmp_path / ".agents" / "skills" / "heavy"
    small = tmp_path / ".agents" / "skills" / "light"
    big.mkdir(parents=True)
    small.mkdir(parents=True)
    (big / "SKILL.md").write_text("skill body " * 40, encoding="utf-8")
    (small / "SKILL.md").write_text("tiny", encoding="utf-8")
    evals = big / "evals"
    evals.mkdir()
    (evals / "evals.json").write_text(
        json.dumps({
            "skill_name": "heavy",
            "evals": [{
                "id": 1,
                "prompt": "Use wiki/hot.md",
                "expected_output": "ok",
                "assertions": [{"text": "Cites wiki/hot.md", "type": "process"}],
            }],
        }),
        encoding="utf-8",
    )

    first = build_context_load(root=tmp_path, vault=vault, traces=[])
    assert first["first_turn"]["files"][0]["path"] == ".omp/AGENTS.md"
    assert first["skills"][0]["name"] == "heavy"
    assert first["skills"][0]["coverage"] == "with"
    assert first["skills"][0]["evals"] == 1
    assert first["skills"][0]["criteria"] >= 1
    assert first["skills"][1]["name"] == "light"
    assert first["skills"][1]["coverage"] == "without"
    assert first["eval_coverage"] == {"with": 1, "without": 1}
    assert first["efficiency"]["trend"] == "new"
    assert any("Add eval criteria for light" in step for step in first["act"])
    assert "skill_eval" not in first

    grown = build_context_load(
        root=tmp_path,
        vault=vault,
        traces=[{"record_kind": "command", "command": "health", "first_turn_tokens": 1}],
    )
    assert grown["efficiency"]["trend"] == "up"
    assert grown["efficiency"]["delta_tokens"] == grown["first_turn"]["total_tokens"] - 1


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
    first = digest_rules(tmp_path, extra={"vale": True})
    style.write_text("a: 2\n", encoding="utf-8")
    second = digest_rules(tmp_path, extra={"vale": True})
    third = digest_rules(tmp_path, extra={"vale": False})
    pyc = creative / "__pycache__"
    pyc.mkdir()
    (pyc / "engine.cpython-314.pyc").write_text("bytecode", encoding="utf-8")
    assert first != second
    assert second != third
    assert digest_rules(tmp_path, extra={"vale": False}) == third



def test_lint_reports_open_ledger_separately(tmp_path: Path):
    page(tmp_path, "one.md")
    baseline = run_cli(tmp_path, "lint", "one.md")
    baseline_data = payload(baseline)
    tracker = tmp_path / "_tracker"
    tracker.mkdir(exist_ok=True)
    (tracker / "errors.md").write_text(
        "# Error ledger\n\n"
        + json.dumps({
            "cause": "open operational failure",
            "evidence": [{"detail": "open operational failure", "sitting": "test"}],
            "id": "e-1",
            "source": "scripts/wiki",
        }, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )
    result = run_cli(tmp_path, "lint", "one.md")
    data = payload(result)
    assert data["ledger"]["open"] == 1
    assert data["ledger"]["ids"] == ["e-1"]
    assert data["status"] == baseline_data["status"]
    assert data["counts"] == baseline_data["counts"]
    assert result.returncode == baseline.returncode


def test_health_flags_llm_wiki_core_files(tmp_path: Path):
    from tools.wiki_ops.health import build_core_files

    (tmp_path / "index.md").write_text("- [[alpha]] — page\n", encoding="utf-8")
    (tmp_path / "log.md").write_text("- [2026-09-19T00:00:00Z] INGEST source=x\n", encoding="utf-8")
    (tmp_path / "AGENTS.md").write_text("# Conventions\n\nOwner rules.\n", encoding="utf-8")
    (tmp_path / "hot.md").write_text(
        "word " * 501
        + "\n- [[alpha]] — page\n- [[beta]] — page\n- [[gamma]] — page\n"
        + "- [[delta]] — page\n- [[epsilon]] — page\n- [[zeta]] — page\n"
        + "- [[eta]] — page\n- [[theta]] — page\n- [[iota]] — page\n"
        + "- [2026-09-19T00:00:00Z] INGEST source=x\n"
        + "- [2026-09-18T00:00:00Z] UPDATE pages=y\n"
        + "- [2026-09-17T00:00:00Z] LINT issues=0\n"
        + "- [2026-09-16T00:00:00Z] CREATE pages=z\n",
        encoding="utf-8",
    )
    core = build_core_files(tmp_path)
    kinds = {item["kind"] for item in core["issues"]}
    paths = {item["path"] for item in core["issues"]}
    assert "oversized" in kinds
    assert "cohesion" in kinds
    assert "hot.md" in paths
    assert core["act"]



def test_progress_heartbeat_emits_every_interval():
    assert HEARTBEAT_INTERVAL_S == 10
    lines: list[str] = []
    with ProgressHeartbeat("lint", interval=0.05, emit=lines.append):
        time.sleep(0.16)
    beats = [line for line in lines if line.startswith("wiki lint:") and "still=1" in line and "elapsed_s=" in line]
    assert len(beats) >= 2


def test_progress_heartbeat_covers_health_command():
    lines: list[str] = []
    with ProgressHeartbeat("health", interval=0.05, emit=lines.append):
        time.sleep(0.12)
    assert any(line.startswith("wiki health:") and "still=1" in line for line in lines)


def test_lint_and_health_main_install_heartbeat(tmp_path: Path, monkeypatch):
    import importlib.machinery
    import importlib.util

    loader = importlib.machinery.SourceFileLoader("wiki_cli_heartbeat", str(ROOT / "scripts/wiki"))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    seen: list[str] = []

    class Probe:
        def __init__(self, command: str, *args, **kwargs):
            seen.append(command)

        def __enter__(self):
            return self

        def __exit__(self, *exc):
            return False

    monkeypatch.setattr(module, "ProgressHeartbeat", Probe)
    monkeypatch.setattr(module, "_lint", lambda *args, **kwargs: 0)
    monkeypatch.setattr(module, "_health", lambda *args, **kwargs: 0)
    monkeypatch.setattr(module, "configured_vault", lambda: tmp_path)
    monkeypatch.setattr(module, "resolve_vault", lambda vault: Path(vault))
    assert module.main(["lint"]) == 0
    assert module.main(["health"]) == 0
    assert seen == ["lint", "health"]


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
    first = run_cli(tmp_path, "lint", "fix", "entities/npc/legacy.md")
    assert first.returncode in (0, 1), first.stderr
    data = payload(first)
    assert data["status"] in {"clean", "findings"}
    assert data["changed_files"] == ["entities/npc/legacy.md"]
    assert any(item["status"] == "applied" for item in data["applied"])
    assert not stub.exists()
    second = run_cli(tmp_path, "lint", "fix", "entities/npc/legacy.md")
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

    result = payload(run_cli(tmp_path, "lint", "fix", "entities/npc/target.md"))
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

    result = payload(run_cli(tmp_path, "lint", "fix", "entities/npc/Bob.md"))
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
    before = payload(run_cli(tmp_path, "lint", "entities/npc/table.md"))
    rules = {item["rule"] for group in before["files"] for item in group["findings"]}
    assert "table_wikilink_unescaped_pipe" in rules
    fixed = run_cli(tmp_path, "lint", "fix", "entities/npc/table.md")
    assert fixed.returncode in (0, 1), fixed.stderr
    assert "| [[keeper\\|The Keeper]] |" in table.read_text(encoding="utf-8")
    assert "[[keeper|prose link]]" in table.read_text(encoding="utf-8")
    after = payload(run_cli(tmp_path, "lint", "entities/npc/table.md"))
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
    result = run_cli(one, "lint", "a.md", "--vault", str(two))
    assert payload(result)["vault"] == str(two.resolve())
    result = _bare("lint", "a.md", cwd=elsewhere, env={"OBSIDIAN_VAULT_PATH": str(one), "WIKI_TRACKER_ROOT": str(elsewhere)})
    assert payload(result)["vault"] == str(one.resolve())


def test_bare_wiki_lists_subcommands_only():
    result = _bare()
    assert result.returncode == 0
    names = [line.split()[0] + (" fix" if line.split()[:2] == ["lint", "fix"] else "") for line in result.stdout.splitlines() if line.strip()]
    assert names == ["lint", "lint fix", "query", "health", "mutate", "repair"]


def test_subcommand_help_is_scoped_with_examples():
    for sub, example in (("lint", "wiki lint entities/place/Belumara.md"), ("query", 'wiki query "Belumara" -n 5'),
                         ("health", "wiki health"), ("mutate", "wiki mutate --stdin --dry-run < op.json")):
        helped = _bare(sub, "--help")
        assert helped.returncode == 0 and "Examples:" in helped.stdout and example in helped.stdout, sub
        others = {"query", "health", "mutate", "repair"} - {sub}
        assert not any(f"wiki {o}" in helped.stdout for o in others), sub
    fix = _bare("lint", "fix", "--help")
    assert "wiki lint fix dir:entities/place --dry-run" in fix.stdout
    legacy = subprocess.run([PYTHON, str(ROOT / "scripts/wiki-lint"), "--help"], capture_output=True, text=True)
    assert "wiki lint --help" in legacy.stdout


def test_no_prompts_with_stdin_closed(tmp_path: Path):
    page(tmp_path, "a.md")
    result = subprocess.run([*WIKI, "lint", "a.md"], cwd=ROOT, capture_output=True, text=True, stdin=subprocess.DEVNULL,
                            env=os.environ | {"OBSIDIAN_VAULT_PATH": str(tmp_path), "WIKI_TRACKER_ROOT": str(tmp_path)},
                            timeout=120)
    assert result.returncode in (0, 1)
    missing = _bare("query", env={"OBSIDIAN_VAULT_PATH": str(tmp_path)})
    _error(missing, needle="phrase")


def test_stdin_and_paths_only(tmp_path: Path):
    page(tmp_path, "a.md")
    page(tmp_path, "b.md")
    result = run_cli_stdin(tmp_path, "a.md\nb.md\n", "lint", "--stdin")
    assert payload(result)["files_checked"] == 2
    paths = run_cli_stdin(tmp_path, "a.md\n", "lint", "--stdin", "--paths-only")
    assert paths.stdout.split() == ["a.md"] or paths.stdout.split() == []


def run_cli_stdin(vault: Path, stdin: str, *args: str):
    env = {"OBSIDIAN_VAULT_PATH": str(vault), "WIKI_TRACKER_ROOT": str(vault / "_tracker")}
    (vault / "_tracker").mkdir(exist_ok=True)
    return _bare(*args, env=env, stdin=stdin)


def test_options_before_or_after_positionals(tmp_path: Path):
    page(tmp_path, "a.md")
    before = payload(run_cli(tmp_path, "lint", "--json", "a.md"))
    after = payload(run_cli(tmp_path, "lint", "a.md", "--json"))
    assert before["files_checked"] == after["files_checked"] == 1


def test_bare_fix_token_is_rejected(tmp_path: Path):
    page(tmp_path, "entities/place/Belumara.md")
    result = run_cli(tmp_path, "lint", "entities/place/Belumara.md", "fix")
    data = _error(result, needle="'fix' is not a lint path")
    assert data["hint"] == "lint fix is a subcommand"
    assert data["example"] == "wiki lint fix entities/place/Belumara.md"
    assert not (tmp_path / "_meta" / "lint-cache.json").exists()


def test_invalid_inputs_give_the_error_object(tmp_path: Path):
    page(tmp_path, "entities/place/Belumara.md")
    _error(run_cli(tmp_path, "lint", "entities/place/Nowhere.md"), needle="path not found")
    prefixed = _error(run_cli(tmp_path, "lint", "wiki/entities/place/Belumara.md"), needle="path not found")
    assert prefixed["example"] == "wiki lint entities/place/Belumara.md"
    _error(run_cli(tmp_path, "lint", "--scope", "dir"), needle="kind:value")
    kinds = _error(run_cli(tmp_path, "lint", "folder:entities"), needle="unknown scope kind")
    assert "files|directory(dir)|entity_type(type)|identity_set|changed|bundle" in kinds["list_valid"]
    _error(run_cli(tmp_path, "lint", "--bogus"), needle="--bogus")


def test_dry_run_plans_and_repeat_is_already_done(tmp_path: Path):
    stub = tmp_path / "entities/npc/legacy.md"
    stub.parent.mkdir(parents=True, exist_ok=True)
    stub.write_text("---\ntitle: Legacy\ntype: npc\nredirects_to: entities/npc/current.md\n---\n\n# Legacy\n", encoding="utf-8")
    page(tmp_path, "entities/npc/current.md", title="Current")
    planned = payload(run_cli(tmp_path, "lint", "fix", "dir:entities/npc", "--dry-run"))
    assert planned["status"] == "planned" and planned["planned"] and stub.exists()
    again = payload(run_cli(tmp_path, "lint", "fix", "dir:entities/npc", "--dry-run"))
    assert again["planned"] == planned["planned"]
    applied = payload(run_cli(tmp_path, "lint", "fix", "dir:entities/npc"))
    assert applied["changed"] == ["entities/npc/legacy.md"]
    repeat = payload(run_cli(tmp_path, "lint", "fix", "dir:entities/npc"))
    assert repeat["status"] == "already_done" and repeat["changed"] == []
    op = json.dumps({"kind": "add_tag", "target": "entities/npc/current.md", "selector": {}, "payload": {"tag": "x"}})
    first = payload(run_cli_stdin(tmp_path, op, "mutate", "--stdin"))
    assert first["changed"] == ["entities/npc/current.md"], first
    second = payload(run_cli_stdin(tmp_path, op, "mutate", "--stdin"))
    assert second["status"] == "already_done" and second["changed"] == []


def test_success_keys_and_health_next(tmp_path: Path):
    page(tmp_path, "a.md")
    for args in (("lint", "a.md"), ("lint", "fix", "a.md"), ("health",)):
        data = payload(run_cli(tmp_path, *args))
        assert {"status", "vault", "changed", "counts", "timing", "next"} <= set(data), (args, sorted(data))
        assert "duration_ms" in data["timing"]
    health = payload(run_cli(tmp_path, "health"))
    assert health["next"] == (health["focus"][0] if health["focus"] else None)


def test_slow_checker_notice_is_a_plain_report(tmp_path: Path, capsys):
    import importlib.machinery
    import importlib.util

    loader = importlib.machinery.SourceFileLoader("wiki_cli", str(ROOT / "scripts/wiki"))
    spec = importlib.util.spec_from_loader(loader.name, loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    module._tune("lint", [("scripts/wiki-lint:vale", 4000), ("scripts/wiki-lint:template", 900)])
    assert capsys.readouterr().err.strip() == (
        "wiki lint: slowest checker scripts/wiki-lint:vale 4000 ms; next scripts/wiki-lint:template 900 ms")
