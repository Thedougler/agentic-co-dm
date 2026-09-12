"""TDD for `VaultIndex` — the SQLite-cached `Corpus` implementation."""

from __future__ import annotations

import shutil
import sqlite3
from pathlib import Path

import pytest

from wiki_cli import db
from wiki_cli.index import VaultIndex

FIXTURES = Path(__file__).parent / "fixtures" / "index"


@pytest.fixture
def vault(tmp_path: Path) -> Path:
    shutil.copytree(FIXTURES, tmp_path, dirs_exist_ok=True)
    return tmp_path


@pytest.fixture
def index(vault: Path) -> VaultIndex:
    return VaultIndex.build(vault, vault, scoped_roots=())


def test_resolve_by_slug(index: VaultIndex) -> None:
    page = index.resolve("the-rook")
    assert page is not None
    assert page.rel_path == "npcs/the-rook.md"


def test_resolve_by_alias(index: VaultIndex) -> None:
    page = index.resolve("The Rook")
    assert page is not None
    assert page.rel_path == "npcs/the-rook.md"


def test_ambiguous_basename(index: VaultIndex) -> None:
    assert index.ambiguous("guide") == ["factions/guide.md", "guides/guide.md"]


def test_links_from(index: VaultIndex) -> None:
    targets = index.links_from("npcs/barnaby-rook.md")
    assert "the-rook" in targets
    assert "guide#Setup" in targets


def test_links_to(index: VaultIndex) -> None:
    linkers = index.links_to("npcs/the-rook.md")
    assert "npcs/barnaby-rook.md" in linkers


def test_by_type(index: VaultIndex) -> None:
    pages = index.by_type("npc")
    assert {page.rel_path for page in pages} == {
        "npcs/the-rook.md",
        "npcs/barnaby-rook.md",
        "npcs/section-links.md",
    }


def test_cache_second_build_zero_parses(vault: Path) -> None:
    VaultIndex.build(vault, vault, scoped_roots=())
    second = VaultIndex.build(vault, vault, scoped_roots=())
    assert second.parses_performed == 0


def test_links_table_persisted(vault: Path, index: VaultIndex) -> None:
    conn = sqlite3.connect(vault / ".wiki-cli" / "cache.sqlite3")
    rows = conn.execute(
        "SELECT target, raw_target, section, count FROM links WHERE source = ?",
        ("npcs/barnaby-rook.md",),
    ).fetchall()
    by_raw = {(r[1], r[2]): (r[0], r[3]) for r in rows}
    assert by_raw[("the-rook", "Ties")] == ("npcs/the-rook.md", 2)


def test_page_metrics_counts(vault: Path, index: VaultIndex) -> None:
    conn = sqlite3.connect(vault / ".wiki-cli" / "cache.sqlite3")
    row = conn.execute(
        "SELECT links_in, links_out FROM page_metrics WHERE rel_path = ? AND scope = 'all'",
        ("guides/lonely.md",),
    ).fetchone()
    assert row == (0, 0)


def test_links_detail_in_memory(index: VaultIndex) -> None:
    detail = index.links_detail("npcs/barnaby-rook.md")
    assert ("npcs/the-rook.md", "the-rook", "Ties", 2) in detail


def test_stale_links_rows_removed(vault: Path) -> None:
    VaultIndex.build(vault, vault, scoped_roots=())
    (vault / "guides" / "lonely.md").unlink()
    VaultIndex.build(vault, vault, scoped_roots=())
    conn = sqlite3.connect(vault / ".wiki-cli" / "cache.sqlite3")
    assert conn.execute(
        "SELECT COUNT(*) FROM page_metrics WHERE rel_path = 'guides/lonely.md'"
    ).fetchone() == (0,)


@pytest.fixture
def built_vault(vault: Path) -> Path:
    VaultIndex.build(vault, vault, scoped_roots=())
    return vault


def _unique_col(vault: Path, rel_path: str) -> int | None:
    conn = sqlite3.connect(vault / ".wiki-cli" / "cache.sqlite3")
    row = conn.execute(
        'SELECT "unique" FROM pages WHERE rel_path = ?', (rel_path,)
    ).fetchone()
    assert row is not None, f"no pages row for {rel_path}"
    return row[0]


def test_unique_true_item(built_vault: Path) -> None:
    assert _unique_col(built_vault, "items/magic-sword.md") == 1


def test_unique_false_item(built_vault: Path) -> None:
    assert _unique_col(built_vault, "items/rope.md") == 0


def test_unique_absent_item(built_vault: Path) -> None:
    assert _unique_col(built_vault, "items/torch.md") == 0


def test_unique_null_for_non_item(built_vault: Path) -> None:
    assert _unique_col(built_vault, "npcs/the-rook.md") is None


def test_unique_column_present_after_migration(tmp_path: Path) -> None:
    """A v2 DB gains the unique column when connect() migrates to v3."""
    db_path = tmp_path / "cache.sqlite3"
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS schema_meta (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            version INTEGER NOT NULL,
            last_gravity_session INTEGER
        )
    """)
    conn.execute("INSERT INTO schema_meta (id, version) VALUES (1, 2)")
    conn.execute("""
        CREATE TABLE IF NOT EXISTS pages (
            rel_path TEXT PRIMARY KEY,
            mtime_ns INTEGER NOT NULL,
            content_hash TEXT NOT NULL,
            type TEXT,
            slug TEXT NOT NULL,
            aliases_json TEXT NOT NULL,
            links_json TEXT NOT NULL,
            headings_json TEXT NOT NULL,
            uid TEXT
        )
    """)
    conn.commit()
    conn.close()

    migrated = db.connect(db_path)
    cols = {row[1] for row in migrated.execute("PRAGMA table_info(pages)")}
    assert "unique" in cols
