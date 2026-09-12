"""Tests for agent-read diagnostics: JSONL ingestion, rollup, and reports."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli import db
from wiki_cli.agent_access import (
    ingest_log,
    report_divergent,
    report_hot_pages,
    report_redundant,
    rollup_agent_reads,
)
from wiki_cli.cli import app
from wiki_cli.config import AgentAccessConfig

runner = CliRunner()


@pytest.fixture
def db_conn(tmp_path: Path):
    conn = db.connect(tmp_path / "cache.sqlite3")
    return conn


@pytest.fixture
def agent_cfg() -> AgentAccessConfig:
    return AgentAccessConfig(agent_reads_window=90)


@pytest.fixture
def sample_log(tmp_path: Path) -> Path:
    log_path = tmp_path / "agent-reads.jsonl"
    records = [
        {"page": "vault/npcs/barnaby-rook.md", "session_id": "sess-001", "tool_type": "Read", "query_position": None, "timestamp": "2026-08-01T10:00:00Z"},
        {"page": "vault/npcs/barnaby-rook.md", "session_id": "sess-001", "tool_type": "Read", "query_position": None, "timestamp": "2026-08-01T10:05:00Z"},
        {"page": "vault/npcs/captain-vex.md", "session_id": "sess-001", "tool_type": "Read", "query_position": None, "timestamp": "2026-08-01T10:01:00Z"},
        {"page": "vault/npcs/barnaby-rook.md", "session_id": "sess-002", "tool_type": "Read", "query_position": None, "timestamp": "2026-08-02T10:00:00Z"},
        {"page": "vault/locations/sunken-crown.md", "session_id": "sess-002", "tool_type": "Read", "query_position": None, "timestamp": "2026-08-02T10:01:00Z"},
        {"page": "vault/npcs/captain-vex.md", "session_id": "sess-003", "tool_type": "wiki_query", "query_position": 1, "timestamp": "2026-08-03T10:00:00Z"},
    ]
    log_path.write_text(
        "\n".join(json.dumps(r) for r in records) + "\n",
        encoding="utf-8",
    )
    return log_path


def test_ingest_inserts_records(db_conn, sample_log):
    inserted = ingest_log(db_conn, sample_log)
    assert inserted == 6

    rows = db_conn.execute("SELECT COUNT(*) FROM page_agent_access").fetchone()[0]
    assert rows == 6


def test_ingest_skips_duplicates(db_conn, sample_log):
    ingest_log(db_conn, sample_log)
    inserted_2 = ingest_log(db_conn, sample_log)
    assert inserted_2 == 0

    rows = db_conn.execute("SELECT COUNT(*) FROM page_agent_access").fetchone()[0]
    assert rows == 6


def test_ingest_missing_file(db_conn, tmp_path):
    inserted = ingest_log(db_conn, tmp_path / "nonexistent.jsonl")
    assert inserted == 0


def test_ingest_skips_malformed_lines(db_conn, tmp_path):
    log_path = tmp_path / "agent-reads.jsonl"
    log_path.write_text(
        "not json\n"
        '{"page": "vault/x.md"}\n'
        '{"page": "vault/x.md", "session_id": "s1", "tool_type": "Read", "timestamp": "2026-01-01T00:00:00Z"}\n',
        encoding="utf-8",
    )
    inserted = ingest_log(db_conn, log_path)
    assert inserted == 1


def test_rollup_counts_within_window(db_conn, sample_log, agent_cfg):
    from wiki_cli.agent_access import _ensure_page_metrics

    _ensure_page_metrics(db_conn)
    ingest_log(db_conn, sample_log)
    db_conn.execute(
        "INSERT INTO page_metrics (rel_path, scope, links_in, links_out) VALUES (?, 'all', 1, 1)",
        ("vault/npcs/barnaby-rook.md",),
    )
    db_conn.execute(
        "INSERT INTO page_metrics (rel_path, scope, links_in, links_out) VALUES (?, 'all', 1, 1)",
        ("vault/npcs/captain-vex.md",),
    )
    db_conn.commit()

    updated = rollup_agent_reads(db_conn, agent_cfg)
    assert updated >= 2

    row = db_conn.execute(
        "SELECT agent_reads FROM page_metrics WHERE rel_path = ? AND scope = 'all'",
        ("vault/npcs/barnaby-rook.md",),
    ).fetchone()
    assert row[0] == 3  # 2 in sess-001 + 1 in sess-002


def test_rollup_window_excludes_old_sessions(db_conn, sample_log):
    cfg = AgentAccessConfig(agent_reads_window=1)
    ingest_log(db_conn, sample_log)

    updated = rollup_agent_reads(db_conn, cfg)
    assert updated > 0

    row = db_conn.execute(
        "SELECT agent_reads FROM page_metrics WHERE rel_path = ? AND scope = 'all'",
        ("vault/npcs/captain-vex.md",),
    ).fetchone()
    # window=1 keeps only sess-003 (latest), captain-vex has 1 record there
    assert row[0] == 1


def test_report_hot_pages_ordering(db_conn, sample_log, agent_cfg):
    ingest_log(db_conn, sample_log)
    rollup_agent_reads(db_conn, agent_cfg)

    rows = report_hot_pages(db_conn)
    assert len(rows) > 0
    assert rows[0].agent_reads >= rows[-1].agent_reads
    assert rows[0].page == "vault/npcs/barnaby-rook.md"


def test_report_redundant_identifies_rereads(db_conn, sample_log, agent_cfg):
    ingest_log(db_conn, sample_log)

    rows = report_redundant(db_conn)
    assert len(rows) == 1
    assert rows[0].page == "vault/npcs/barnaby-rook.md"
    assert rows[0].session_id == "sess-001"
    assert rows[0].read_count == 2


def test_report_divergent(db_conn, sample_log, agent_cfg):
    ingest_log(db_conn, sample_log)
    rollup_agent_reads(db_conn, agent_cfg)
    db_conn.execute(
        "UPDATE page_metrics SET pagerank = 0.9, player_gravity = 10.0 "
        "WHERE rel_path = 'vault/npcs/barnaby-rook.md' AND scope = 'all'"
    )
    db_conn.execute(
        "UPDATE page_metrics SET pagerank = 0.01, player_gravity = 0.0 "
        "WHERE rel_path = 'vault/npcs/captain-vex.md' AND scope = 'all'"
    )
    db_conn.commit()

    rows = report_divergent(db_conn)
    divergent_pages = [r.page for r in rows]
    assert "vault/npcs/captain-vex.md" in divergent_pages


def test_signal_is_read_only(db_conn, sample_log, agent_cfg):
    """agent_reads never mutates search rankings — no UPDATE touches pagerank."""
    import inspect
    import re

    from wiki_cli import agent_access

    source = inspect.getsource(agent_access)
    update_stmts = re.findall(r"UPDATE\s+page_metrics\s+SET\s+[^\"']+", source)
    for stmt in update_stmts:
        assert "pagerank" not in stmt, f"UPDATE writes pagerank: {stmt}"


@pytest.fixture
def vault_cwd(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    (tmp_path / "wiki.toml").write_text(
        '[vault]\nroot = "vault"\n\n'
        "[agent_access]\nagent_reads_window = 90\n",
        encoding="utf-8",
    )
    vault = tmp_path / "vault"
    vault.mkdir()
    wiki_cli_dir = tmp_path / ".wiki-cli"
    wiki_cli_dir.mkdir()
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_cli_build_agent_access(vault_cwd, sample_log):
    import shutil

    dest = vault_cwd / ".wiki-cli" / "agent-reads.jsonl"
    shutil.copy(sample_log, dest)

    result = runner.invoke(app, ["build-agent-access"])
    assert result.exit_code == 0
    assert "6 records ingested" in result.output


def test_cli_report_hot_pages(vault_cwd, sample_log):
    import shutil

    dest = vault_cwd / ".wiki-cli" / "agent-reads.jsonl"
    shutil.copy(sample_log, dest)

    runner.invoke(app, ["build-agent-access"])
    result = runner.invoke(app, ["report-hot-pages"])
    assert result.exit_code == 0
    assert "barnaby-rook" in result.output


def test_cli_report_hot_pages_redundant(vault_cwd, sample_log):
    import shutil

    dest = vault_cwd / ".wiki-cli" / "agent-reads.jsonl"
    shutil.copy(sample_log, dest)

    runner.invoke(app, ["build-agent-access"])
    result = runner.invoke(app, ["report-hot-pages", "--redundant"])
    assert result.exit_code == 0
    assert "barnaby-rook" in result.output
    assert "sess-001" in result.output


def test_cli_report_hot_pages_divergent(vault_cwd, sample_log):
    import shutil

    dest = vault_cwd / ".wiki-cli" / "agent-reads.jsonl"
    shutil.copy(sample_log, dest)

    runner.invoke(app, ["build-agent-access"])
    result = runner.invoke(app, ["report-hot-pages", "--divergent"])
    assert result.exit_code == 0
