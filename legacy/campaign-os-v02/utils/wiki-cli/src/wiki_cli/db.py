"""SQLite layer: findings cache and TTL claim/lease, both WAL-mode.

Two independent responsibilities share one connection type:

1. A findings cache keyed on `(rel_path, content_hash, rule_id, rule_version,
   config_fingerprint)`. Every one of those five fields can change
   independently of the others — the file's bytes, the rule's own logic
   (`BaseRule.version`), or `wiki.toml` (`Config.fingerprint`) — and a cache
   keyed on anything less than the full tuple silently serves a stale
   verdict. `Finding` round-trips through JSON with enums serialised by
   value, so the cache is portable across processes without importing
   `wiki_cli.contracts` enum identity.

2. A TTL claim/lease so concurrent fixing agents never step on the same
   finding. Acquisition is a single atomic `INSERT ... ON CONFLICT` — never
   read-then-write, which would race between two connections.

Disposable tables (findings_cache, claims) live under `schema_version` and
are dropped and recreated on mismatch. Non-disposable index tables (pages,
links, page_metrics) are migrated additively via ALTER TABLE so existing rows
are preserved across version bumps.
"""

from __future__ import annotations

import json
import sqlite3
import time
from collections.abc import Callable
from pathlib import Path

from wiki_cli.contracts import Finding, Severity, Tier

SCHEMA_VERSION = 4
"""Bump on any change to the table shapes below.

v1 → v2: additive migration — disposable tables (findings_cache, claims) are
still dropped and recreated on mismatch; the non-disposable index tables
(pages, links, page_metrics) gain new columns via ALTER TABLE, and two new
tables are created, preserving all existing rows.
v2 → v3: pages.unique INTEGER DEFAULT NULL — opt-in flag for item pages.
v3 → v4: the producer-timing tables are dropped — the budget gate they fed
is gone; a slow producer is cached now (`orchestrator.py`)."""

_BUSY_TIMEOUT_MS = 5_000
_BUSY_RETRY_ATTEMPTS = 5
_BUSY_RETRY_DELAY_S = 0.1

_SCHEMA_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS schema_meta (
    id INTEGER PRIMARY KEY CHECK (id = 1),
    version INTEGER NOT NULL,
    last_gravity_session INTEGER
)
"""

_CACHE_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS findings_cache (
    rel_path TEXT NOT NULL,
    content_hash TEXT NOT NULL,
    rule_id TEXT NOT NULL,
    rule_version TEXT NOT NULL,
    config_fingerprint TEXT NOT NULL,
    findings_json TEXT NOT NULL,
    updated_at REAL NOT NULL,
    PRIMARY KEY (rel_path, content_hash, rule_id, rule_version, config_fingerprint)
)
"""

_CLAIMS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS claims (
    key TEXT PRIMARY KEY,
    owner TEXT NOT NULL,
    expires_at REAL NOT NULL
)
"""

_DROP_PRODUCER_TIMING_SQL: tuple[str, ...] = (
    "DROP TABLE IF EXISTS producer_timing",
    "DROP TABLE IF EXISTS producer_timing_per_target",
)
"""Both tables fed a producer budget gate that no longer exists: a slow
producer is cached now, never skipped, so no timing is stored between runs.
Dropped on every connect so an existing cache file sheds them."""

_CACHE_GC_INDEX_SQL = """
CREATE INDEX IF NOT EXISTS findings_cache_gc
ON findings_cache (rel_path, rule_id, updated_at)
"""
"""Covers `gc`'s own generation ranking — it partitions by
`(rel_path, rule_id)` and orders by `updated_at`."""

_PAGE_INTERACTIONS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS page_interactions (
    page TEXT NOT NULL,
    session_num INTEGER NOT NULL,
    mention_count INTEGER NOT NULL DEFAULT 1,
    PRIMARY KEY (page, session_num)
)
"""

PAGE_METRICS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS page_metrics (
    rel_path TEXT NOT NULL,
    scope TEXT NOT NULL DEFAULT 'all',
    links_in INTEGER NOT NULL,
    links_out INTEGER NOT NULL,
    pagerank REAL,
    dirty INTEGER NOT NULL DEFAULT 1,
    player_gravity REAL,
    gravity_tier TEXT,
    agent_reads INTEGER,
    PRIMARY KEY (rel_path, scope)
)
"""

_PAGE_AGENT_ACCESS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS page_agent_access (
    page TEXT NOT NULL,
    session_id TEXT NOT NULL,
    tool_type TEXT NOT NULL,
    query_position INTEGER,
    timestamp TEXT NOT NULL
)
"""


def _table_exists(conn: sqlite3.Connection, table: str) -> bool:
    row = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table,)
    ).fetchone()
    return row is not None


def _column_exists(conn: sqlite3.Connection, table: str, column: str) -> bool:
    cols = {row[1] for row in conn.execute(f"PRAGMA table_info({table})")}
    return column in cols


def _migrate_v1_to_v2(conn: sqlite3.Connection) -> None:
    """Additive migration: add new columns to existing index tables; preserve rows.

    New tables (page_interactions, page_agent_access) are created by the
    unconditional tail of _ensure_schema — no need to create them here."""
    if _table_exists(conn, "pages") and not _column_exists(conn, "pages", "uid"):
        conn.execute("ALTER TABLE pages ADD COLUMN uid TEXT")
    if _table_exists(conn, "links") and not _column_exists(conn, "links", "link_type"):
        conn.execute("ALTER TABLE links ADD COLUMN link_type TEXT")
    if _table_exists(conn, "page_metrics"):
        if not _column_exists(conn, "page_metrics", "player_gravity"):
            conn.execute("ALTER TABLE page_metrics ADD COLUMN player_gravity REAL")
        if not _column_exists(conn, "page_metrics", "gravity_tier"):
            conn.execute("ALTER TABLE page_metrics ADD COLUMN gravity_tier TEXT")
        if not _column_exists(conn, "page_metrics", "agent_reads"):
            conn.execute("ALTER TABLE page_metrics ADD COLUMN agent_reads INTEGER")


def _migrate_v2_to_v3(conn: sqlite3.Connection) -> None:
    """Additive migration: pages.unique for item graph opt-in."""
    if _table_exists(conn, "pages") and not _column_exists(conn, "pages", "unique"):
        conn.execute('ALTER TABLE pages ADD COLUMN "unique" INTEGER DEFAULT NULL')


def connect(db_path: Path) -> sqlite3.Connection:
    """Open (creating parent dirs as needed) a WAL-mode connection, migrated
    to the current schema.

    Handles two failure modes rather than letting either crash a lint run:

    - A locked database (another process mid-write): `sqlite3.connect`'s
      `timeout` plus WAL mode makes `SQLITE_BUSY` self-resolve in the common
      case; `_with_retry` below covers the rest for individual statements.
    - A corrupt or otherwise unreadable database file: caught here and the
      file is replaced with a fresh one rather than propagating.
    """
    db_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        conn = _open(db_path)
        _with_retry(conn, lambda: _ensure_schema(conn))
    except sqlite3.DatabaseError as error:
        if _is_busy(error):
            # Lock contention that outlived busy_timeout and every retry.
            # `OperationalError` is a `DatabaseError`, so without this the
            # branch below would read a healthy-but-busy file as corrupt and
            # delete the cache out from under the process holding the lock.
            raise
        # Corrupt file (bad header, malformed page, etc.) — the cache is
        # disposable, so recreate it rather than taking down the whole run.
        try:
            conn.close()
        except UnboundLocalError:
            pass
        db_path.unlink(missing_ok=True)
        for suffix in ("-wal", "-shm"):
            Path(f"{db_path}{suffix}").unlink(missing_ok=True)
        conn = _open(db_path)
        _ensure_schema(conn)
    return conn


def _open(db_path: Path) -> sqlite3.Connection:
    conn = sqlite3.connect(str(db_path), timeout=_BUSY_TIMEOUT_MS / 1000, isolation_level=None)
    conn.execute(f"PRAGMA busy_timeout = {_BUSY_TIMEOUT_MS}")
    conn.execute("PRAGMA journal_mode = WAL")
    conn.execute("PRAGMA synchronous = NORMAL")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def _is_busy(error: sqlite3.Error) -> bool:
    """A lock/contention failure, not a damaged file. SQLite reports both
    `SQLITE_BUSY` and `SQLITE_LOCKED` through `OperationalError`, whose only
    distinguishing signal is the message text."""
    text = str(error).lower()
    return "locked" in text or "busy" in text


def _with_retry(conn: sqlite3.Connection, fn: Callable[[], None]) -> None:
    """Retry a write a few times on SQLITE_BUSY beyond what busy_timeout covers
    (e.g. contention on the initial schema migration itself)."""
    last_error: sqlite3.OperationalError | None = None
    for attempt in range(_BUSY_RETRY_ATTEMPTS):
        try:
            fn()
            return
        except sqlite3.OperationalError as error:
            if not _is_busy(error):
                raise
            last_error = error
            if attempt < _BUSY_RETRY_ATTEMPTS - 1:
                time.sleep(_BUSY_RETRY_DELAY_S * (attempt + 1))
    assert last_error is not None
    raise last_error


def _ensure_schema(conn: sqlite3.Connection) -> None:
    conn.execute(_SCHEMA_TABLE_SQL)
    row = conn.execute("SELECT version FROM schema_meta WHERE id = 1").fetchone()
    stored_version: int | None = row[0] if row is not None else None

    if stored_version != SCHEMA_VERSION:
        if stored_version is not None and stored_version < SCHEMA_VERSION:
            # Additive migration: preserve index data, drop only disposable tables.
            _migrate_v1_to_v2(conn)
            _migrate_v2_to_v3(conn)
        else:
            # Fresh DB or future-version downgrade: drop disposable tables.
            conn.execute("DROP TABLE IF EXISTS findings_cache")
            conn.execute("DROP TABLE IF EXISTS claims")
        conn.execute(
            "INSERT INTO schema_meta (id, version) VALUES (1, ?) "
            "ON CONFLICT (id) DO UPDATE SET version = excluded.version",
            (SCHEMA_VERSION,),
        )

    if not _column_exists(conn, "schema_meta", "last_gravity_session"):
        conn.execute("ALTER TABLE schema_meta ADD COLUMN last_gravity_session INTEGER")

    conn.execute(_CACHE_TABLE_SQL)
    conn.execute(_CACHE_GC_INDEX_SQL)
    conn.execute(_CLAIMS_TABLE_SQL)
    for statement in _DROP_PRODUCER_TIMING_SQL:
        conn.execute(statement)
    conn.execute(_PAGE_INTERACTIONS_TABLE_SQL)
    conn.execute(_PAGE_AGENT_ACCESS_TABLE_SQL)


def _finding_to_dict(finding: Finding) -> dict[str, object]:
    return {
        "rule_id": finding.rule_id,
        "file": finding.file,
        "line": finding.line,
        "message": finding.message,
        "severity": finding.severity.value,
        "tier": finding.tier.value,
        "producer": finding.producer,
        "column": finding.column,
        "fixable": finding.fixable,
    }


def _severity_of(value: object) -> Severity:
    """A cache row written before ADR-0064 can carry the retired `advisory`
    severity. It reads back as a plain warning — the tier it became — so an
    old cache generation stays usable instead of raising mid-sweep."""
    try:
        return Severity(value)
    except ValueError:
        return Severity.WARNING


def _finding_from_dict(data: dict[str, object]) -> Finding:
    return Finding(
        rule_id=str(data["rule_id"]),
        file=str(data["file"]),
        line=int(data["line"]),  # type: ignore[call-overload]
        message=str(data["message"]),
        severity=_severity_of(data["severity"]),
        tier=Tier(data["tier"]),
        producer=str(data["producer"]),
        column=int(data["column"]),  # type: ignore[call-overload]
        fixable=bool(data["fixable"]),
    )


def get_cached(
    conn: sqlite3.Connection,
    *,
    rel_path: str,
    content_hash: str,
    rule_id: str,
    rule_version: str,
    config_fingerprint: str,
) -> list[Finding] | None:
    """Look up a cached result. `None` means "no cache entry" — never confused
    with an empty list of findings, which is a legitimate cached verdict."""
    row = conn.execute(
        "SELECT findings_json FROM findings_cache "
        "WHERE rel_path = ? AND content_hash = ? AND rule_id = ? "
        "AND rule_version = ? AND config_fingerprint = ?",
        (rel_path, content_hash, rule_id, rule_version, config_fingerprint),
    ).fetchone()
    if row is None:
        return None
    payload: list[dict[str, object]] = json.loads(row[0])
    return [_finding_from_dict(item) for item in payload]


def set_cached(
    conn: sqlite3.Connection,
    *,
    rel_path: str,
    content_hash: str,
    rule_id: str,
    rule_version: str,
    config_fingerprint: str,
    findings: list[Finding],
) -> None:
    payload = json.dumps([_finding_to_dict(f) for f in findings])
    now = time.time()

    def _write() -> None:
        conn.execute(
            "INSERT INTO findings_cache "
            "(rel_path, content_hash, rule_id, rule_version, config_fingerprint, "
            "findings_json, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?) "
            "ON CONFLICT (rel_path, content_hash, rule_id, rule_version, config_fingerprint) "
            "DO UPDATE SET findings_json = excluded.findings_json, "
            "updated_at = excluded.updated_at",
            (rel_path, content_hash, rule_id, rule_version, config_fingerprint, payload, now),
        )

    _with_retry(conn, _write)


def gc(conn: sqlite3.Connection, *, keep: int = 3) -> int:
    """Keep the newest `keep` rows per `(rel_path, rule_id)`; delete the
    rest. Returns the count deleted so callers can report it.

    A row is superseded the moment the file's bytes, the rule's version, or
    the config fingerprint moves — the old row is then dead forever, but a
    time window keeps it for another two weeks anyway, which is how the
    cache reached 1M rows. Counting generations instead bounds the table by
    the corpus size, not by edit frequency: `keep` covers a revert or a
    branch switch back to a recent content hash, which a window sized in
    days does not.

    VACUUM follows when the delete freed a real share of the file — SQLite
    keeps freed pages on its own free list otherwise, so the 428MB on disk
    would survive a delete of every row.
    """
    cursor = conn.execute(
        "DELETE FROM findings_cache WHERE rowid NOT IN ("
        "  SELECT rowid FROM ("
        "    SELECT rowid, ROW_NUMBER() OVER ("
        "      PARTITION BY rel_path, rule_id ORDER BY updated_at DESC"
        "    ) AS generation FROM findings_cache"
        "  ) WHERE generation <= ?"
        ")",
        (keep,),
    )
    deleted = cursor.rowcount
    if deleted > 0:
        _vacuum_if_slack(conn)
    return deleted


_VACUUM_SLACK_SHARE = 0.25
"""Fraction of the file that must be free pages before a VACUUM earns its
cost — a full rewrite of the database file is far more expensive than the
delete that preceded it."""


def _vacuum_if_slack(conn: sqlite3.Connection) -> None:
    """VACUUM when free pages are a big enough share of the file. Best
    effort: a VACUUM cannot run while another connection holds the
    database, which is normal under concurrent agents and is not a lint
    failure — the next sweep reclaims the space instead."""
    page_count = conn.execute("PRAGMA page_count").fetchone()
    free_count = conn.execute("PRAGMA freelist_count").fetchone()
    if not page_count or not free_count or not page_count[0]:
        return
    if free_count[0] / page_count[0] < _VACUUM_SLACK_SHARE:
        return
    try:
        conn.execute("VACUUM")
    except sqlite3.OperationalError:
        return


def claim(conn: sqlite3.Connection, key: str, owner: str, ttl_seconds: int) -> bool:
    """Try to acquire the lease on `key` for `owner`.

    Single atomic statement: insert if no row exists, or steal an expired
    row, in one `INSERT ... ON CONFLICT` — never a separate read followed by
    a write, which would leave a window for two connections to both believe
    they hold the lease.
    """
    now = time.time()
    expires_at = now + ttl_seconds
    result_holder: list[bool] = []

    def _write() -> None:
        cursor = conn.execute(
            "INSERT INTO claims (key, owner, expires_at) VALUES (?, ?, ?) "
            "ON CONFLICT (key) DO UPDATE SET owner = excluded.owner, "
            "expires_at = excluded.expires_at "
            "WHERE claims.expires_at < ?",
            (key, owner, expires_at, now),
        )
        if cursor.rowcount > 0:
            result_holder.append(True)
            return
        row = conn.execute("SELECT owner FROM claims WHERE key = ?", (key,)).fetchone()
        result_holder.append(row is not None and row[0] == owner and expires_at >= now)

    _with_retry(conn, _write)
    return result_holder[0]


def release(conn: sqlite3.Connection, key: str, owner: str) -> bool:
    """Release `key`, only if `owner` currently holds it (expired or not)."""

    def _write() -> None:
        cursor = conn.execute(
            "DELETE FROM claims WHERE key = ? AND owner = ?",
            (key, owner),
        )
        _rowcounts.append(cursor.rowcount)

    _rowcounts: list[int] = []
    _with_retry(conn, _write)
    return _rowcounts[0] > 0


def active_claims(conn: sqlite3.Connection) -> list[tuple[str, str, float]]:
    """All claims currently on file, expired or not — `(key, owner,
    expires_at)`. Callers filter for "active" (`expires_at > now`)
    themselves; this is a raw dump for inspection/debugging."""
    rows = conn.execute("SELECT key, owner, expires_at FROM claims").fetchall()
    return [(str(key), str(owner), float(expires_at)) for key, owner, expires_at in rows]


def set_page_uid(conn: sqlite3.Connection, rel_path: str, uid: str) -> bool:
    """Write `uid` into the pages row for `rel_path`.

    Returns True when the row was found and updated, False when no pages row
    exists yet for `rel_path` (assign-uids caller can log a warning). Wraps
    _with_retry so SQLITE_BUSY under concurrent writes does not silently
    drop the update."""
    rowcounts: list[int] = []

    def _write() -> None:
        cursor = conn.execute(
            "UPDATE pages SET uid = ? WHERE rel_path = ?",
            (uid, rel_path),
        )
        rowcounts.append(cursor.rowcount)

    _with_retry(conn, _write)
    return rowcounts[0] > 0
