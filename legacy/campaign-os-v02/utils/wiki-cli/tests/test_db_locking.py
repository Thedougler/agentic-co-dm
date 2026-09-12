"""`connect` must tell a busy database apart from a corrupt one.

`sqlite3.OperationalError` ("database is locked") is a subclass of
`sqlite3.DatabaseError`, so a connect path that treats every `DatabaseError`
as corruption deletes a healthy cache the moment two lint processes overlap.
"""

from __future__ import annotations

import sqlite3
from pathlib import Path

import pytest

from wiki_cli import db


def _seed(db_path: Path) -> None:
    conn = db.connect(db_path)
    conn.execute("INSERT INTO claims (key, owner, expires_at) VALUES ('k', 'o', 9e9)")
    conn.close()


def test_busy_schema_migration_propagates_and_keeps_the_file(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    db_path = tmp_path / "cache.sqlite3"
    _seed(db_path)

    def always_locked(_conn: sqlite3.Connection) -> None:
        raise sqlite3.OperationalError("database is locked")

    monkeypatch.setattr(db, "_ensure_schema", always_locked)
    monkeypatch.setattr(db, "_BUSY_RETRY_DELAY_S", 0.0)

    with pytest.raises(sqlite3.OperationalError):
        db.connect(db_path)

    assert db_path.exists()
    monkeypatch.undo()
    assert db.connect(db_path).execute("SELECT key FROM claims").fetchone() == ("k",)


def test_busy_schema_migration_is_retried(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    db_path = tmp_path / "cache.sqlite3"
    real_ensure = db._ensure_schema
    attempts = {"n": 0}

    def locked_once(conn: sqlite3.Connection) -> None:
        attempts["n"] += 1
        if attempts["n"] == 1:
            raise sqlite3.OperationalError("database is locked")
        real_ensure(conn)

    monkeypatch.setattr(db, "_ensure_schema", locked_once)
    monkeypatch.setattr(db, "_BUSY_RETRY_DELAY_S", 0.0)

    conn = db.connect(db_path)
    assert attempts["n"] == 2
    assert conn.execute("SELECT COUNT(*) FROM claims").fetchone() == (0,)


def test_corrupt_file_is_still_recreated(tmp_path: Path) -> None:
    db_path = tmp_path / "cache.sqlite3"
    db_path.write_bytes(b"not a sqlite database at all, not even close")

    conn = db.connect(db_path)

    assert conn.execute("SELECT COUNT(*) FROM claims").fetchone() == (0,)
