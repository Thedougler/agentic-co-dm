"""Agent-read diagnostics: JSONL log ingestion, rolling-window rollup, and reports.

Diagnostic only — this signal never mutates search results or rankings.
"""

from __future__ import annotations

import json
import sqlite3
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wiki_cli.config import AgentAccessConfig


def _ensure_page_metrics(conn: sqlite3.Connection) -> None:
    from wiki_cli.db import PAGE_METRICS_TABLE_SQL

    conn.execute(PAGE_METRICS_TABLE_SQL)


def ingest_log(conn: sqlite3.Connection, log_path: Path) -> int:
    """Read a JSONL agent-reads log and insert rows into page_agent_access.

    Skips exact duplicates (same page + session_id + tool_type + timestamp).
    Returns the number of rows inserted."""
    if not log_path.is_file():
        return 0

    inserted = 0
    with log_path.open(encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                continue

            page = record.get("page")
            session_id = record.get("session_id")
            tool_type = record.get("tool_type")
            timestamp = record.get("timestamp")
            query_position = record.get("query_position")

            if not page or not session_id or not tool_type or not timestamp:
                continue

            existing = conn.execute(
                "SELECT 1 FROM page_agent_access "
                "WHERE page = ? AND session_id = ? AND tool_type = ? AND timestamp = ?",
                (page, session_id, tool_type, timestamp),
            ).fetchone()
            if existing is not None:
                continue

            conn.execute(
                "INSERT INTO page_agent_access (page, session_id, tool_type, query_position, timestamp) "
                "VALUES (?, ?, ?, ?, ?)",
                (page, session_id, tool_type, query_position, timestamp),
            )
            inserted += 1

    conn.commit()
    return inserted


def rollup_agent_reads(
    conn: sqlite3.Connection,
    agent_access_cfg: AgentAccessConfig,
) -> int:
    """Compute agent_reads on page_metrics as a rolling count over the last N sessions.

    Returns the number of pages updated."""
    _ensure_page_metrics(conn)

    distinct_sessions = [
        row[0]
        for row in conn.execute(
            "SELECT DISTINCT session_id FROM page_agent_access ORDER BY session_id"
        ).fetchall()
    ]

    window = agent_access_cfg.agent_reads_window
    if len(distinct_sessions) > window:
        cutoff_sessions = set(distinct_sessions[-window:])
    else:
        cutoff_sessions = set(distinct_sessions)

    if not cutoff_sessions:
        return 0

    placeholders = ",".join("?" for _ in cutoff_sessions)
    rows = conn.execute(
        f"SELECT page, COUNT(*) FROM page_agent_access "
        f"WHERE session_id IN ({placeholders}) "
        f"GROUP BY page",
        list(cutoff_sessions),
    ).fetchall()

    updated = 0
    for page, count in rows:
        conn.execute(
            "UPDATE page_metrics SET agent_reads = ? WHERE rel_path = ? AND scope = 'all'",
            (count, page),
        )
        if conn.execute("SELECT changes()").fetchone()[0] > 0:  # type: ignore[index]
            updated += 1
        else:
            conn.execute(
                "INSERT INTO page_metrics (rel_path, scope, links_in, links_out, agent_reads) "
                "VALUES (?, 'all', 0, 0, ?)",
                (page, count),
            )
            updated += 1

    conn.commit()
    return updated


@dataclass(frozen=True, slots=True)
class HotPageRow:
    page: str
    agent_reads: int
    pagerank: float | None
    gravity_tier: str | None
    player_gravity: float | None


def report_hot_pages(conn: sqlite3.Connection) -> list[HotPageRow]:
    """Pages ranked by agent_reads descending, with pagerank and gravity signals."""
    _ensure_page_metrics(conn)
    rows = conn.execute(
        "SELECT rel_path, agent_reads, pagerank, gravity_tier, player_gravity "
        "FROM page_metrics "
        "WHERE agent_reads IS NOT NULL AND agent_reads > 0 AND scope = 'all' "
        "ORDER BY agent_reads DESC"
    ).fetchall()
    return [
        HotPageRow(
            page=r[0],
            agent_reads=r[1],
            pagerank=r[2],
            gravity_tier=r[3],
            player_gravity=r[4],
        )
        for r in rows
    ]


@dataclass(frozen=True, slots=True)
class RedundantRow:
    page: str
    session_id: str
    read_count: int


def report_redundant(conn: sqlite3.Connection) -> list[RedundantRow]:
    """Pages read more than once in the same session — candidates for pre-loading."""
    rows = conn.execute(
        "SELECT page, session_id, COUNT(*) as cnt "
        "FROM page_agent_access "
        "GROUP BY page, session_id "
        "HAVING cnt > 1 "
        "ORDER BY cnt DESC"
    ).fetchall()
    return [RedundantRow(page=r[0], session_id=r[1], read_count=r[2]) for r in rows]


@dataclass(frozen=True, slots=True)
class DivergentRow:
    page: str
    agent_reads: int
    pagerank: float | None
    player_gravity: float | None
    importance_score: float


def report_divergent(conn: sqlite3.Connection) -> list[DivergentRow]:
    """Pages where agent_reads is high but pagerank × player_gravity is low."""
    _ensure_page_metrics(conn)
    rows = conn.execute(
        "SELECT rel_path, agent_reads, pagerank, player_gravity "
        "FROM page_metrics "
        "WHERE agent_reads IS NOT NULL AND agent_reads > 0 AND scope = 'all' "
        "ORDER BY agent_reads DESC"
    ).fetchall()

    results: list[DivergentRow] = []
    for r in rows:
        page, agent_reads, pagerank, player_gravity = r
        pr = pagerank if pagerank is not None else 0.0
        pg = player_gravity if player_gravity is not None else 0.0
        importance = pr * pg
        results.append(
            DivergentRow(
                page=page,
                agent_reads=agent_reads,
                pagerank=pagerank,
                player_gravity=player_gravity,
                importance_score=importance,
            )
        )

    results.sort(key=lambda row: (row.agent_reads, -row.importance_score), reverse=True)
    median_reads = _median_value([r.agent_reads for r in results])
    median_importance = _median_value([r.importance_score for r in results])
    return [
        r
        for r in results
        if r.agent_reads >= median_reads and r.importance_score <= median_importance
    ]


def _median_value(values: list[float | int]) -> float:
    if not values:
        return 0.0
    s = sorted(values)
    mid = len(s) // 2
    if len(s) % 2 == 0:
        return (s[mid - 1] + s[mid]) / 2.0
    return float(s[mid])
