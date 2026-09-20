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


def test_lint_prefix_dump_and_full_noop(tmp_path: Path):
    page(tmp_path, "entities/npc/one.md", title="One")
    page(tmp_path, "entities/npc/two.md", title="Two")
    bulk = run_cli(tmp_path, "lint", "entities/npc")
    assert bulk.returncode in (0, 1), bulk.stderr
    data = payload(bulk)
    required = {
        "status", "counts", "hard_fail", "unique", "backlog", "next_page",
        "cache", "files_checked", "scope", "files", "timing",
    }
    assert required <= data.keys()
    assert "findings" not in data
    assert "findings_by_file" not in data
    assert data["timing"]["command"] == "lint"
    assert data["scope"]["paths"] == ["entities/npc"]
    for group in data["files"]:
        assert group["findings"]
        assert all(isinstance(item["line"], int) and item["line"] >= 1 for item in group["findings"])
        assert all(set(item) == {"rule", "file", "line", "severity", "message"} for item in group["findings"])
    full = payload(run_cli(tmp_path, "lint", "entities/npc", "--full"))
    assert set(full) == set(data)
    assert full["files"] == data["files"]
    assert full["counts"] == data["counts"]


def test_two_named_files_are_separate_blocks(tmp_path: Path):
    page(tmp_path, "entities/npc/one.md", title="One")
    page(tmp_path, "entities/npc/two.md", title="Two")
    result = run_cli(tmp_path, "lint", "entities/npc/two.md", "entities/npc/one.md")
    assert result.returncode in (0, 1), result.stderr
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
    assert payload(result) == {"error": "path not found in vault: 'entities/npcs'", "status": "error"}
    assert elapsed < 1
    pretty = run_cli(tmp_path, "lint", "entities/npcs", "--pretty")
    assert pretty.returncode == 2
    assert pretty.stdout == ""
    assert pretty.stderr.strip().startswith("error:")


def test_cache_hits_byte_change_and_config_miss(tmp_path: Path):
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
    flagged = payload(run_cli(tmp_path, "lint", "--no-vale"))
    assert flagged["cache"]["misses"] >= 1


def test_scoped_lint_keeps_other_cache_entries(tmp_path: Path):
    page(tmp_path, "a.md")
    page(tmp_path, "b.md")
    run_cli(tmp_path, "lint", "a.md")
    run_cli(tmp_path, "lint", "b.md")
    again = payload(run_cli(tmp_path, "lint", "a.md"))
    assert again["cache"]["hits"] >= 1


def test_pretty_default_json_and_full_same_list(tmp_path: Path):
    page(tmp_path, "one.md")
    default = run_cli(tmp_path, "lint")
    pretty = run_cli(tmp_path, "lint", "--pretty")
    pretty_full = run_cli(tmp_path, "lint", "--pretty", "--full")
    assert json.loads(default.stdout)
    assert pretty.stdout.strip()
    assert not pretty.stdout.lstrip().startswith("{")
    assert pretty.stdout == pretty_full.stdout


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



def test_lint_open_ledger_is_not_clean(tmp_path: Path):
    page(tmp_path, "one.md")
    tracker = tmp_path / "_tracker"
    tracker.mkdir(exist_ok=True)
    (tracker / "errors.md").write_text(
        "# Error ledger\n\n"
        + json.dumps({
            "cause": "open operational failure",
            "cause_fixed": False,
            "id": "e-1",
            "sitting": "test",
            "status": "open",
        })
        + "\n",
        encoding="utf-8",
    )
    result = run_cli(tmp_path, "lint", "one.md")
    data = payload(result)
    assert data["ledger"]["open"] == 1
    assert data["ledger"]["ids"] == ["e-1"]
    assert data["status"] == "findings"
    assert result.returncode == 1


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
