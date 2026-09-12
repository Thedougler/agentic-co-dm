"""Tests for schema v2 migration and wiki assign-uids."""

from __future__ import annotations

import shutil
import sqlite3
from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli import db
from wiki_cli.cli import app

FIXTURES = Path(__file__).parent / "fixtures" / "index"

runner = CliRunner()


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    shutil.copytree(FIXTURES, tmp_path, dirs_exist_ok=True)
    return tmp_path


@pytest.fixture
def db_path(tmp_path: Path) -> Path:
    return tmp_path / "cache.sqlite3"


def _column_names(conn: sqlite3.Connection, table: str) -> set[str]:
    return {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}


# --- Schema migration tests ---


def test_fresh_db_schema_version_is_current(db_path: Path) -> None:
    conn = db.connect(db_path)
    row = conn.execute("SELECT version FROM schema_meta WHERE id = 1").fetchone()
    assert row is not None
    assert row[0] == db.SCHEMA_VERSION


def test_fresh_db_has_page_interactions_table(db_path: Path) -> None:
    conn = db.connect(db_path)
    tables = {
        row[0]
        for row in conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
    }
    assert "page_interactions" in tables
    assert "page_agent_access" in tables


def test_v1_to_v2_migration_preserves_claims(tmp_path: Path) -> None:
    """A v1 DB with a live claim must keep that row after upgrading to v2."""
    db_path = tmp_path / "cache.sqlite3"

    # Manually create a v1 schema.
    raw = sqlite3.connect(str(db_path))
    raw.execute("PRAGMA journal_mode=WAL")
    raw.execute("CREATE TABLE schema_meta (id INTEGER PRIMARY KEY CHECK (id=1), version INTEGER NOT NULL)")
    raw.execute("INSERT INTO schema_meta (id, version) VALUES (1, 1)")
    raw.execute(
        "CREATE TABLE claims (key TEXT PRIMARY KEY, owner TEXT NOT NULL, expires_at REAL NOT NULL)"
    )
    raw.execute("INSERT INTO claims (key, owner, expires_at) VALUES ('k', 'o', 9e9)")
    raw.execute(
        "CREATE TABLE findings_cache (rel_path TEXT, content_hash TEXT, rule_id TEXT, "
        "rule_version TEXT, config_fingerprint TEXT, findings_json TEXT, updated_at REAL, "
        "PRIMARY KEY (rel_path, content_hash, rule_id, rule_version, config_fingerprint))"
    )
    raw.execute(
        "CREATE TABLE producer_timing_per_target (family_id TEXT PRIMARY KEY, seconds REAL NOT NULL, updated_at REAL NOT NULL)"
    )
    raw.commit()
    raw.close()

    conn = db.connect(db_path)
    # Schema upgraded.
    version = conn.execute("SELECT version FROM schema_meta WHERE id=1").fetchone()[0]
    assert version == db.SCHEMA_VERSION
    # Claims row preserved.
    row = conn.execute("SELECT key FROM claims").fetchone()
    assert row == ("k",)


def test_v1_to_v2_migration_adds_columns_to_index_tables(tmp_path: Path) -> None:
    """Migration adds uid/link_type/player_gravity/gravity_tier/agent_reads to existing tables."""
    db_path = tmp_path / "cache.sqlite3"

    raw = sqlite3.connect(str(db_path))
    raw.execute("PRAGMA journal_mode=WAL")
    raw.execute("CREATE TABLE schema_meta (id INTEGER PRIMARY KEY CHECK (id=1), version INTEGER NOT NULL)")
    raw.execute("INSERT INTO schema_meta (id, version) VALUES (1, 1)")
    raw.execute(
        "CREATE TABLE claims (key TEXT PRIMARY KEY, owner TEXT NOT NULL, expires_at REAL NOT NULL)"
    )
    raw.execute(
        "CREATE TABLE findings_cache (rel_path TEXT, content_hash TEXT, rule_id TEXT, "
        "rule_version TEXT, config_fingerprint TEXT, findings_json TEXT, updated_at REAL, "
        "PRIMARY KEY (rel_path, content_hash, rule_id, rule_version, config_fingerprint))"
    )
    raw.execute(
        "CREATE TABLE producer_timing_per_target (family_id TEXT PRIMARY KEY, seconds REAL NOT NULL, updated_at REAL NOT NULL)"
    )
    # v1 index tables — no new columns yet.
    raw.execute(
        "CREATE TABLE pages (rel_path TEXT PRIMARY KEY, mtime_ns INTEGER NOT NULL, "
        "content_hash TEXT NOT NULL, type TEXT, slug TEXT NOT NULL, "
        "aliases_json TEXT NOT NULL, links_json TEXT NOT NULL, headings_json TEXT NOT NULL)"
    )
    raw.execute("INSERT INTO pages VALUES ('a.md', 1, 'h', 'npc', 'a', '[]', '[]', '[]')")
    raw.execute(
        "CREATE TABLE links (source TEXT NOT NULL, target TEXT, raw_target TEXT NOT NULL, "
        "section TEXT NOT NULL DEFAULT '', count INTEGER NOT NULL DEFAULT 1, "
        "PRIMARY KEY (source, raw_target, section))"
    )
    raw.execute(
        "CREATE TABLE page_metrics (rel_path TEXT NOT NULL, scope TEXT NOT NULL DEFAULT 'all', "
        "links_in INTEGER NOT NULL, links_out INTEGER NOT NULL, pagerank REAL, "
        "dirty INTEGER NOT NULL DEFAULT 1, PRIMARY KEY (rel_path, scope))"
    )
    raw.execute("INSERT INTO page_metrics VALUES ('a.md', 'all', 3, 2, 0.5, 0)")
    raw.commit()
    raw.close()

    conn = db.connect(db_path)

    assert "uid" in _column_names(conn, "pages")
    assert "link_type" in _column_names(conn, "links")
    metrics_cols = _column_names(conn, "page_metrics")
    assert "player_gravity" in metrics_cols
    assert "gravity_tier" in metrics_cols
    assert "agent_reads" in metrics_cols

    # Existing row data preserved.
    row = conn.execute("SELECT rel_path, links_in FROM page_metrics WHERE rel_path='a.md'").fetchone()
    assert row == ("a.md", 3)
    row2 = conn.execute("SELECT rel_path FROM pages WHERE rel_path='a.md'").fetchone()
    assert row2 == ("a.md",)

    tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
    assert "page_interactions" in tables
    assert "page_agent_access" in tables


def test_vault_index_build_succeeds_on_freshly_migrated_db(tmp_path: Path) -> None:
    """wiki build (VaultIndex.build) must complete without error on a v2 DB.

    Simulates the acceptance criterion: fresh migration → build completes."""
    from wiki_cli.index import VaultIndex

    vault = tmp_path / "vault"
    vault.mkdir()
    (vault / "page.md").write_text("---\ntype: npc\n---\nBody\n", encoding="utf-8")
    (tmp_path / "wiki.toml").write_text("", encoding="utf-8")

    # Trigger migration (fresh DB → v2).
    db_path = tmp_path / ".wiki-cli" / "cache.sqlite3"
    db_path.parent.mkdir()
    db.connect(db_path)

    # Build the index against the freshly migrated DB — must not raise.
    index = VaultIndex.build(tmp_path, vault, scoped_roots=())
    assert len(list(index.pages())) == 1


# --- assign-uids tests ---


def _setup_vault(root: Path, pages: dict[str, str]) -> None:
    """Create vault/ with given pages and a minimal wiki.toml."""
    vault = root / "vault"
    vault.mkdir(parents=True, exist_ok=True)
    for name, content in pages.items():
        (vault / name).write_text(content, encoding="utf-8")
    (root / "wiki.toml").write_text("", encoding="utf-8")


def test_assign_uids_writes_uid_to_frontmatter(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _setup_vault(
        tmp_path,
        {
            "a.md": "---\ntype: npc\n---\nBody A\n",
            "b.md": "---\ntype: location\n---\nBody B\n",
        },
    )
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["assign-uids"], catch_exceptions=False)
    assert result.exit_code == 0, result.output

    for name in ("a.md", "b.md"):
        text = (tmp_path / "vault" / name).read_text(encoding="utf-8")
        assert "uid:" in text


def test_assign_uids_records_uid_in_db(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _setup_vault(
        tmp_path,
        {
            "a.md": "---\ntype: npc\n---\nBody A\n",
            "b.md": "---\ntype: location\n---\nBody B\n",
        },
    )
    monkeypatch.chdir(tmp_path)
    runner.invoke(app, ["assign-uids"], catch_exceptions=False)

    db_path = tmp_path / ".wiki-cli" / "cache.sqlite3"
    conn = sqlite3.connect(str(db_path))
    rows = conn.execute("SELECT rel_path, uid FROM pages").fetchall()
    assert len(rows) == 2
    for rel_path, uid in rows:
        assert uid is not None and len(uid) == 36, f"page {rel_path!r} missing uid in DB"


def test_assign_uids_idempotent(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    _setup_vault(tmp_path, {"a.md": "---\ntype: npc\n---\nBody\n"})
    monkeypatch.chdir(tmp_path)

    runner.invoke(app, ["assign-uids"], catch_exceptions=False)
    uid_after_first = (tmp_path / "vault" / "a.md").read_text(encoding="utf-8")

    runner.invoke(app, ["assign-uids"], catch_exceptions=False)
    uid_after_second = (tmp_path / "vault" / "a.md").read_text(encoding="utf-8")

    assert uid_after_first == uid_after_second


def test_assign_uids_skips_pages_with_existing_uid(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    preset_uid = "12345678-1234-1234-1234-123456789abc"
    _setup_vault(
        tmp_path,
        {
            "a.md": f"---\ntype: npc\nuid: {preset_uid}\n---\nBody\n",
            "b.md": "---\ntype: npc\n---\nBody B\n",
        },
    )
    monkeypatch.chdir(tmp_path)
    result = runner.invoke(app, ["assign-uids"], catch_exceptions=False)
    assert result.exit_code == 0
    assert "1 assigned, 1 skipped" in result.output

    text = (tmp_path / "vault" / "a.md").read_text(encoding="utf-8")
    assert preset_uid in text
