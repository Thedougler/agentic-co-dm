from __future__ import annotations

import json
import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = os.environ.get("PYTHON", str(ROOT / ".venv/bin/python"))


def run_cli(vault: Path, *args: str, extra_env: dict[str, str] | None = None):
    env = os.environ | {"OBSIDIAN_VAULT_PATH": str(vault)} | (extra_env or {})
    return subprocess.run(
        [PYTHON, str(ROOT / "scripts/wiki"), *args],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
    )


def page(vault: Path, relative: str, *, title: str = "Page") -> None:
    path = vault / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "---\n"
        f"title: {title}\n"
        "category: concept\n"
        "tags: []\n"
        "sources: []\n"
        "created: 2026-09-19\n"
        "updated: 2026-09-19\n"
        "---\n\n# " + title + "\n",
        encoding="utf-8",
    )


def payload(result):
    assert result.stdout.strip(), result.stderr
    return json.loads(result.stdout)


def test_lint_worklist_and_single_file_contract(tmp_path: Path):
    page(tmp_path, "entities/npc/one.md", title="One")
    bulk = run_cli(tmp_path, "lint", "entities/npc")
    assert bulk.returncode in (0, 1), bulk.stderr
    data = payload(bulk)
    assert {"status", "counts", "hard_fail", "unique", "backlog", "next_page", "cache", "files_checked", "scope"} <= data.keys()
    assert "findings" not in data and "findings_by_file" not in data

    single = run_cli(tmp_path, "lint", "entities/npc/one.md")
    assert single.returncode in (0, 1), single.stderr
    data = payload(single)
    assert all(isinstance(item["line"], int) and item["line"] >= 1 for item in data.get("findings", []))


def test_unknown_path_is_structured_error_without_scan(tmp_path: Path):
    result = run_cli(tmp_path, "lint", "entities/npcs")
    assert result.returncode == 2
    assert payload(result) == {"error": "path not found in vault: 'entities/npcs'", "status": "error"}


def test_cache_reuses_unchanged_pages_and_json_is_noop(tmp_path: Path):
    page(tmp_path, "one.md")
    first = payload(run_cli(tmp_path, "lint"))
    second_result = run_cli(tmp_path, "lint", "--json")
    second = payload(second_result)
    assert second_result.returncode in (0, 1)
    assert second["cache"]["hits"] >= first["cache"]["hits"]
    assert len(second_result.stdout) < 8192


def test_pretty_is_explicit(tmp_path: Path):
    page(tmp_path, "one.md")
    default = run_cli(tmp_path, "lint")
    pretty = run_cli(tmp_path, "lint", "--pretty")
    assert json.loads(default.stdout)
    assert pretty.stdout.strip()
    assert not pretty.stdout.lstrip().startswith("{")


def test_health_contains_focus_and_alias(tmp_path: Path):
    page(tmp_path, "one.md")
    health = run_cli(tmp_path, "health")
    env = os.environ | {"OBSIDIAN_VAULT_PATH": str(tmp_path)}
    alias = subprocess.run(
        [PYTHON, str(ROOT / "scripts/wiki-maintain"), "--report"],
        cwd=ROOT,
        env=env,
        capture_output=True,
        text=True,
    )
    assert health.returncode in (0, 1)
    data = payload(health)
    assert {"pages", "bytes", "tokens", "lint", "trends", "focus", "next"} <= data.keys()
    assert len(data["focus"]) <= 5
    assert data["next"] == (data["focus"][0] if data["focus"] else None)
    assert alias.returncode == health.returncode
    assert payload(alias) == data
