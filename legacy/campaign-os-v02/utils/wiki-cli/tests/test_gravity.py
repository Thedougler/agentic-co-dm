"""Tests for the player gravity pipeline: entity resolution, interaction recording, and rollup."""

from __future__ import annotations

from pathlib import Path

import pytest
from typer.testing import CliRunner

from wiki_cli import db
from wiki_cli.cli import app
from wiki_cli.config import GravityConfig
from wiki_cli.gravity import (
    _levenshtein,
    build_gravity,
    get_watermark,
    record_interaction,
    resolve_entity,
    set_watermark,
)

runner = CliRunner()


@pytest.fixture
def db_conn(tmp_path: Path):
    conn = db.connect(tmp_path / "cache.sqlite3")
    return conn


@pytest.fixture
def gravity_cfg() -> GravityConfig:
    return GravityConfig(active_window=3, active_weight=2.0, encountered_weight=1.0)


@pytest.fixture
def vault_cwd(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    (tmp_path / "wiki.toml").write_text(
        '[vault]\nroot = "vault"\n\n'
        "[gravity]\nactive_window = 3\nactive_weight = 2.0\nencountered_weight = 1.0\n",
        encoding="utf-8",
    )
    vault = tmp_path / "vault"
    vault.mkdir()
    npcs = vault / "npcs"
    npcs.mkdir()
    (npcs / "barnaby-rook.md").write_text(
        "---\ntype: npc\naliases:\n  - The Rook\n  - Barnaby\n---\n# Barnaby Rook\n",
        encoding="utf-8",
    )
    (npcs / "captain-vex.md").write_text(
        "---\ntype: npc\n---\n# Captain Vex\n",
        encoding="utf-8",
    )
    (npcs / "dessa-wule.md").write_text(
        "---\ntype: npc\naliases:\n  - Dessa\n---\n# Dessa Wule\n",
        encoding="utf-8",
    )
    monkeypatch.chdir(tmp_path)
    return tmp_path


# --- Levenshtein distance ---


def test_levenshtein_identical() -> None:
    assert _levenshtein("abc", "abc") == 0


def test_levenshtein_one_insert() -> None:
    assert _levenshtein("abc", "abcd") == 1


def test_levenshtein_one_delete() -> None:
    assert _levenshtein("abcd", "abc") == 1


def test_levenshtein_one_substitute() -> None:
    assert _levenshtein("abc", "adc") == 1


def test_levenshtein_two_edits() -> None:
    assert _levenshtein("abc", "axyz") == 3


def test_levenshtein_empty() -> None:
    assert _levenshtein("", "abc") == 3
    assert _levenshtein("abc", "") == 3


# --- Entity resolution ---


def test_resolve_exact_slug(vault_cwd: Path) -> None:
    from wiki_cli.index import VaultIndex

    config_mod = __import__("wiki_cli.config", fromlist=["load_config"])
    config = config_mod.load_config()
    corpus = VaultIndex.build(config.repo_root, config.vault_root, ())
    result = resolve_entity("barnaby-rook", corpus)
    assert result == "vault/npcs/barnaby-rook.md"


def test_resolve_alias(vault_cwd: Path) -> None:
    from wiki_cli.index import VaultIndex

    config = __import__("wiki_cli.config", fromlist=["load_config"]).load_config()
    corpus = VaultIndex.build(config.repo_root, config.vault_root, ())
    result = resolve_entity("The Rook", corpus)
    assert result == "vault/npcs/barnaby-rook.md"


def test_resolve_fuzzy_typo(vault_cwd: Path) -> None:
    from wiki_cli.index import VaultIndex

    config = __import__("wiki_cli.config", fromlist=["load_config"]).load_config()
    corpus = VaultIndex.build(config.repo_root, config.vault_root, ())
    result = resolve_entity("captain-vx", corpus)
    assert result == "vault/npcs/captain-vex.md"


def test_resolve_noise_returns_none(vault_cwd: Path) -> None:
    from wiki_cli.index import VaultIndex

    config = __import__("wiki_cli.config", fromlist=["load_config"]).load_config()
    corpus = VaultIndex.build(config.repo_root, config.vault_root, ())
    result = resolve_entity("xyzzy-qqq-nonsense", corpus)
    assert result is None


def test_resolve_fuzzy_alias_typo(vault_cwd: Path) -> None:
    from wiki_cli.index import VaultIndex

    config = __import__("wiki_cli.config", fromlist=["load_config"]).load_config()
    corpus = VaultIndex.build(config.repo_root, config.vault_root, ())
    result = resolve_entity("Desssa", corpus)
    assert result == "vault/npcs/dessa-wule.md"


# --- Interaction recording ---


def test_record_interaction_insert(db_conn) -> None:
    record_interaction(db_conn, "vault/npcs/foo.md", 1, 3)
    row = db_conn.execute(
        "SELECT mention_count FROM page_interactions WHERE page='vault/npcs/foo.md' AND session_num=1"
    ).fetchone()
    assert row[0] == 3


def test_record_interaction_accumulates(db_conn) -> None:
    record_interaction(db_conn, "vault/npcs/foo.md", 1, 3)
    record_interaction(db_conn, "vault/npcs/foo.md", 1, 2)
    row = db_conn.execute(
        "SELECT mention_count FROM page_interactions WHERE page='vault/npcs/foo.md' AND session_num=1"
    ).fetchone()
    assert row[0] == 5


# --- Watermark ---


def test_watermark_none_initially(db_conn) -> None:
    wm = get_watermark(db_conn)
    assert wm is None


def test_watermark_roundtrip(db_conn) -> None:
    set_watermark(db_conn, 5)
    assert get_watermark(db_conn) == 5
    set_watermark(db_conn, 8)
    assert get_watermark(db_conn) == 8


# --- build_gravity rollup ---


def test_build_gravity_basic(db_conn, gravity_cfg: GravityConfig) -> None:
    record_interaction(db_conn, "vault/npcs/a.md", 1, 5)
    record_interaction(db_conn, "vault/npcs/a.md", 5, 3)
    record_interaction(db_conn, "vault/npcs/b.md", 1, 2)

    updated, _unencountered = build_gravity(db_conn, gravity_cfg, full=True)
    assert updated == 2

    row_a = db_conn.execute(
        "SELECT player_gravity, gravity_tier FROM page_metrics "
        "WHERE rel_path='vault/npcs/a.md' AND scope='all'"
    ).fetchone()
    assert row_a is not None
    # max_session=5, active_floor=5-3+1=3. session 1 encountered (1.0): 5*1.0;
    # session 5 active (2.0): 3*2.0 = 11.0
    assert row_a[0] == pytest.approx(11.0)
    assert row_a[1] == "active"

    row_b = db_conn.execute(
        "SELECT player_gravity, gravity_tier FROM page_metrics "
        "WHERE rel_path='vault/npcs/b.md' AND scope='all'"
    ).fetchone()
    assert row_b is not None
    # session 1 only (encountered) -> 2*1.0 = 2.0
    assert row_b[0] == pytest.approx(2.0)
    assert row_b[1] == "encountered"


def test_build_gravity_unencountered(db_conn, gravity_cfg: GravityConfig) -> None:
    from wiki_cli.db import PAGE_METRICS_TABLE_SQL

    db_conn.execute(PAGE_METRICS_TABLE_SQL)
    db_conn.execute(
        "INSERT INTO page_metrics (rel_path, scope, links_in, links_out) VALUES ('vault/npcs/c.md', 'all', 1, 0)"
    )
    record_interaction(db_conn, "vault/npcs/a.md", 1, 1)

    updated, unencountered = build_gravity(db_conn, gravity_cfg, full=True)
    assert updated == 1
    assert unencountered == 1

    row_c = db_conn.execute(
        "SELECT gravity_tier FROM page_metrics WHERE rel_path='vault/npcs/c.md' AND scope='all'"
    ).fetchone()
    assert row_c[0] == "unencountered"


def test_build_gravity_sets_watermark(db_conn, gravity_cfg: GravityConfig) -> None:
    record_interaction(db_conn, "vault/npcs/a.md", 5, 1)
    build_gravity(db_conn, gravity_cfg, full=True)
    assert get_watermark(db_conn) == 5


def test_build_gravity_no_interactions(db_conn, gravity_cfg: GravityConfig) -> None:
    updated, unencountered = build_gravity(db_conn, gravity_cfg, full=True)
    assert updated == 0
    assert unencountered == 0


def test_build_gravity_active_window_config(db_conn) -> None:
    """Active window of 1 means only the latest session counts as active."""
    cfg = GravityConfig(active_window=1, active_weight=3.0, encountered_weight=1.0)
    record_interaction(db_conn, "vault/npcs/a.md", 1, 4)
    record_interaction(db_conn, "vault/npcs/a.md", 5, 2)

    build_gravity(db_conn, cfg, full=True)
    row = db_conn.execute(
        "SELECT player_gravity, gravity_tier FROM page_metrics "
        "WHERE rel_path='vault/npcs/a.md' AND scope='all'"
    ).fetchone()
    # session 1 (encountered: 1.0) -> 4*1.0; session 5 (active: 3.0) -> 2*3.0 = 10.0
    assert row[0] == pytest.approx(10.0)
    assert row[1] == "active"


def test_build_gravity_incremental_skips_old_sessions(db_conn, gravity_cfg: GravityConfig) -> None:
    """Incremental mode only reprocesses pages with interactions newer than watermark."""
    record_interaction(db_conn, "vault/npcs/a.md", 1, 5)
    build_gravity(db_conn, gravity_cfg, full=True)
    assert get_watermark(db_conn) == 1

    record_interaction(db_conn, "vault/npcs/b.md", 2, 3)
    updated, _ = build_gravity(db_conn, gravity_cfg, full=False)
    assert updated == 1

    row_b = db_conn.execute(
        "SELECT player_gravity FROM page_metrics WHERE rel_path='vault/npcs/b.md' AND scope='all'"
    ).fetchone()
    assert row_b is not None
    assert row_b[0] > 0


def test_build_gravity_incremental_downgrades_stale_active(
    db_conn, gravity_cfg: GravityConfig,
) -> None:
    """A page active in session 1 must downgrade to encountered once the window slides past it."""
    record_interaction(db_conn, "vault/npcs/a.md", 1, 5)
    build_gravity(db_conn, gravity_cfg, full=True)
    row = db_conn.execute(
        "SELECT gravity_tier FROM page_metrics WHERE rel_path='vault/npcs/a.md' AND scope='all'"
    ).fetchone()
    assert row[0] == "active"

    record_interaction(db_conn, "vault/npcs/b.md", 5, 3)
    build_gravity(db_conn, gravity_cfg, full=False)

    row_after = db_conn.execute(
        "SELECT gravity_tier FROM page_metrics WHERE rel_path='vault/npcs/a.md' AND scope='all'"
    ).fetchone()
    assert row_after[0] == "encountered"


# --- CLI integration ---


def test_cli_build_gravity(vault_cwd: Path) -> None:
    conn = db.connect(vault_cwd / ".wiki-cli" / "cache.sqlite3")
    record_interaction(conn, "vault/npcs/barnaby-rook.md", 1, 5)
    conn.close()

    result = runner.invoke(app, ["build-gravity"])
    assert result.exit_code == 0
    assert "1 pages scored" in result.output


def test_cli_build_gravity_full(vault_cwd: Path) -> None:
    conn = db.connect(vault_cwd / ".wiki-cli" / "cache.sqlite3")
    record_interaction(conn, "vault/npcs/barnaby-rook.md", 1, 5)
    conn.close()

    result = runner.invoke(app, ["build-gravity", "--full"])
    assert result.exit_code == 0
    assert "1 pages scored" in result.output


# --- Schema migration: last_gravity_session column ---


def test_fresh_db_has_last_gravity_session_column(tmp_path: Path) -> None:
    conn = db.connect(tmp_path / "cache.sqlite3")
    cols = {row[1] for row in conn.execute("PRAGMA table_info(schema_meta)")}
    assert "last_gravity_session" in cols
