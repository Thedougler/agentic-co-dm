from __future__ import annotations

import json
import os
import stat
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
    required = {"pages", "bytes", "tokens", "lint", "trends", "focus", "next", "timing", "waste", "staging", "remorph", "policy"}
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
