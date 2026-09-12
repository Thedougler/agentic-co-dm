"""Backlog-wave workflow on top of `db.py`'s findings cache and claim/lease
(Task 24 of the wiki-lint migration plan, ADR-0042).

`wiki drain` turns the findings cache — already populated by whatever
`wiki sweep` last ran — into a dispatch queue: one line per file,
worst offenders first. The cache being stale is fine here; the queue is
something an orchestrator hands to fixing agents, never a gate (that job
stays `wiki lint`'s). Only `pure=True` `FileRule` findings
ever reach the cache (`orchestrator.py`), so a drain queue reflects native
rule findings, not external producers or `VaultRule`s.

`--claim N` layers the TTL lease (`db.claim`/`db.release`/`db.active_claims`)
on top: it walks the same sorted drain queue and atomically claims each file
in turn until `N` succeed, printing only the claimed `rel_path`s so a
fixing agent's brief never has to know claims exist at all (ADR-0041:
"adding no extra effort to the fixing agent's own task").
"""

from __future__ import annotations

import fnmatch
import json
import sqlite3
import time
import tomllib
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path

from wiki_cli import db
from wiki_cli.config import CONFIG_FILENAME, ConfigError
from wiki_cli.contracts import Finding

DEFAULT_CLAIM_TTL_SECONDS = 1800
"""30 minutes — the plan's stated default lease when `wiki.toml` sets none."""

_TOP_RULE_IDS_CAP = 3
"""How many distinct rule ids the drain queue line names per file, most-frequent
first — enough to tell a dispatching agent what kind of fix it is without
reprinting every finding."""


@dataclass(frozen=True, slots=True)
class DrainEntry:
    """One file's standing in the queue: how many (filtered) findings it
    carries and which rules fire most on it."""

    rel_path: str
    count: int
    top_rule_ids: list[str]


def load_claim_ttl_seconds(repo_root: Path) -> int:
    """`[claim] ttl_seconds` from `wiki.toml`, or `DEFAULT_CLAIM_TTL_SECONDS`
    when the file or the key is absent. Reads `wiki.toml` directly (the same
    `tomllib` parse `config.py` does) rather than through `Config`, whose
    dataclass has no claim-ttl field."""
    config_path = repo_root / CONFIG_FILENAME
    if not config_path.is_file():
        return DEFAULT_CLAIM_TTL_SECONDS

    try:
        data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    except (tomllib.TOMLDecodeError, UnicodeDecodeError) as error:
        raise ConfigError(f"{config_path}: {error}") from error

    claim_table = data.get("claim", {})
    if not isinstance(claim_table, dict):
        raise ConfigError(f"{config_path}: [claim] must be a table")

    ttl_seconds = claim_table.get("ttl_seconds", DEFAULT_CLAIM_TTL_SECONDS)
    if not isinstance(ttl_seconds, int) or isinstance(ttl_seconds, bool) or ttl_seconds < 1:
        raise ConfigError(f"{config_path}: claim.ttl_seconds must be a positive integer")
    return ttl_seconds


def _current_findings_by_file(conn: sqlite3.Connection) -> dict[str, list[Finding]]:
    """Every cached finding, per file, from ONLY that file's most-recently
    updated content hash — a file with stale rows left behind by an older
    sweep (a rule ported since, a file edited since without a re-lint of
    every rule) never mixes two generations of findings into one count."""
    rows = conn.execute(
        "SELECT rel_path, content_hash, findings_json, updated_at FROM findings_cache"
    ).fetchall()

    latest_hash: dict[str, tuple[str, float]] = {}
    for rel_path, content_hash, _findings_json, updated_at in rows:
        current = latest_hash.get(rel_path)
        if current is None or updated_at > current[1]:
            latest_hash[rel_path] = (content_hash, updated_at)

    findings_by_file: dict[str, list[Finding]] = defaultdict(list)
    for rel_path, content_hash, findings_json, _updated_at in rows:
        if latest_hash[rel_path][0] != content_hash:
            continue
        # `db._finding_from_dict` is the same JSON->Finding decode
        # `get_cached` uses; reused here rather than re-implemented so the
        # two never drift, even though this is a bulk scan `get_cached`'s
        # exact-key lookup does not support.
        for item in json.loads(findings_json):
            findings_by_file[rel_path].append(db._finding_from_dict(item))
    return dict(findings_by_file)


def cache_age_seconds(conn: sqlite3.Connection) -> float | None:
    """Seconds since the most recently written cache row, or `None` when the
    cache is empty (no sweep has run yet)."""
    row = conn.execute("SELECT MAX(updated_at) FROM findings_cache").fetchone()
    if row is None or row[0] is None:
        return None
    return max(0.0, time.time() - float(row[0]))


def build_queue(
    conn: sqlite3.Connection,
    *,
    rules: list[str] | None = None,
    path_glob: str | None = None,
    limit: int | None = None,
) -> list[DrainEntry]:
    """Every file with at least one cached finding matching the filters,
    sorted by finding count descending (rel_path breaks ties), capped at
    `limit` when given. `rules` matches rule ids case-insensitively — the
    one vocabulary the CLI still speaks (ADR-0064)."""
    wanted_rules = {rule_id.upper() for rule_id in rules} if rules else None
    entries: list[DrainEntry] = []
    for rel_path, findings in _current_findings_by_file(conn).items():
        if path_glob is not None and not fnmatch.fnmatch(rel_path, path_glob):
            continue
        filtered = findings
        if wanted_rules is not None:
            filtered = [f for f in filtered if f.rule_id.upper() in wanted_rules]
        if not filtered:
            continue
        rule_counts = Counter(f.rule_id for f in filtered)
        top_rule_ids = [rule_id for rule_id, _count in rule_counts.most_common(_TOP_RULE_IDS_CAP)]
        entries.append(DrainEntry(rel_path=rel_path, count=len(filtered), top_rule_ids=top_rule_ids))

    entries.sort(key=lambda e: (-e.count, e.rel_path))
    if limit is not None:
        entries = entries[:limit]
    return entries


def claim_top_n(
    conn: sqlite3.Connection,
    n: int,
    agent_id: str,
    ttl_seconds: int,
    *,
    rules: list[str] | None = None,
    path_glob: str | None = None,
) -> list[str]:
    """Atomically claim the top `n` unclaimed files off the (filtered)
    drain queue, in order. A file already leased by another owner and not yet
    expired is skipped — `db.claim`'s own atomic `INSERT ... ON CONFLICT`
    decides that, never a read-then-write here. Returns only the rel_paths
    that were actually claimed, which may be fewer than `n`."""
    candidates = build_queue(conn, rules=rules, path_glob=path_glob, limit=None)
    claimed: list[str] = []
    for entry in candidates:
        if len(claimed) >= n:
            break
        if db.claim(conn, entry.rel_path, agent_id, ttl_seconds):
            claimed.append(entry.rel_path)
    return claimed


def list_active_claims(conn: sqlite3.Connection) -> list[tuple[str, str, float]]:
    """Claims not yet expired — `db.active_claims`'s raw dump, filtered here
    per that function's own contract (callers decide "active")."""
    now = time.time()
    return [claim_row for claim_row in db.active_claims(conn) if claim_row[2] > now]


def release_claim(conn: sqlite3.Connection, key: str, *, agent_id: str | None) -> bool:
    """Release one claim. With `agent_id`, only releases when that agent
    currently holds it (`db.release`'s owner-matched delete). Without one,
    force-releases regardless of owner — the orchestrator/admin path for
    freeing a claim whose owning agent is gone."""
    if agent_id is not None:
        return db.release(conn, key, agent_id)
    cursor = conn.execute("DELETE FROM claims WHERE key = ?", (key,))
    return cursor.rowcount > 0


def release_all(conn: sqlite3.Connection, *, agent_id: str | None) -> int:
    """Release every claim, or (with `agent_id`) only those that agent
    holds. Returns the count released."""
    if agent_id is not None:
        released = 0
        for key, owner, _expires_at in db.active_claims(conn):
            if owner == agent_id and db.release(conn, key, agent_id):
                released += 1
        return released
    cursor = conn.execute("DELETE FROM claims")
    return cursor.rowcount


def _format_age(seconds: float | None) -> str:
    if seconds is None:
        return "no cache data"
    if seconds < 60:
        return "just now"
    minutes = int(seconds // 60)
    if minutes < 60:
        return f"{minutes}m ago"
    hours, minutes = divmod(minutes, 60)
    return f"{hours}h {minutes}m ago"


def format_queue(entries: list[DrainEntry], *, cache_age_seconds: float | None) -> str:
    """One line per entry: `<rel_path>  <n> findings  <top rule ids>`,
    already sorted by `build_queue`. Header names the cache age so a
    reader knows how stale the queue might be."""
    header = f"DRAIN — cache {_format_age(cache_age_seconds)} · {len(entries)} files"
    if not entries:
        return header
    lines = [header]
    for entry in entries:
        top = ", ".join(entry.top_rule_ids)
        lines.append(f"{entry.rel_path}  {entry.count} findings  {top}")
    return "\n".join(lines)
