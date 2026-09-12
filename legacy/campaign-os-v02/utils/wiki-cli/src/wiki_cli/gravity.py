"""Player gravity pipeline: entity resolution, interaction recording, and rollup.

Entity resolution for gravity uses exact slug match + Levenshtein ≤ 2 fuzzy
match against slug and `aliases:` frontmatter. Transcription noise that
doesn't resolve cleanly is skipped.

`build_gravity` rolls up `page_interactions` into `player_gravity` and
`gravity_tier` on `page_metrics`, incrementally via a `last_gravity_session`
watermark in `schema_meta`.
"""

from __future__ import annotations

import sqlite3
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from wiki_cli.config import GravityConfig
    from wiki_cli.index import VaultIndex


def _levenshtein(a: str, b: str) -> int:
    if len(a) < len(b):
        return _levenshtein(b, a)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a):
        curr = [i + 1]
        for j, cb in enumerate(b):
            curr.append(min(prev[j + 1] + 1, curr[j] + 1, prev[j] + (ca != cb)))
        prev = curr
    return prev[-1]


def resolve_entity(name: str, corpus: VaultIndex) -> str | None:
    """Resolve a transcript entity mention to a vault page rel_path.

    Precedence: exact VaultIndex.resolve() > Levenshtein ≤ 2 fuzzy match
    against slug and aliases. Returns None for unresolvable noise."""
    page = corpus.resolve(name)
    if page is not None:
        return page.rel_path

    name_lower = name.strip().lower()
    if not name_lower:
        return None

    best_path: str | None = None
    best_dist = 3  # threshold + 1

    for page in corpus.pages():
        slug_lower = page.slug.lower()
        dist = _levenshtein(name_lower, slug_lower)
        if dist < best_dist:
            best_dist = dist
            best_path = page.rel_path

        aliases = page.frontmatter.get("aliases")
        if isinstance(aliases, list):
            for alias in aliases:
                if isinstance(alias, str):
                    dist = _levenshtein(name_lower, alias.lower())
                    if dist < best_dist:
                        best_dist = dist
                        best_path = page.rel_path

    return best_path


def record_interaction(
    conn: sqlite3.Connection,
    page: str,
    session_num: int,
    mention_count: int = 1,
) -> None:
    """Write a player-gravity interaction record to page_interactions."""
    conn.execute(
        "INSERT INTO page_interactions (page, session_num, mention_count) "
        "VALUES (?, ?, ?) "
        "ON CONFLICT(page, session_num) DO UPDATE "
        "SET mention_count = mention_count + excluded.mention_count",
        (page, session_num, mention_count),
    )


def get_watermark(conn: sqlite3.Connection) -> int | None:
    """Read the last_gravity_session watermark from schema_meta."""
    row = conn.execute(
        "SELECT last_gravity_session FROM schema_meta WHERE id = 1"
    ).fetchone()
    if row is None:
        return None
    return row[0]


def set_watermark(conn: sqlite3.Connection, session_num: int) -> None:
    """Write the last_gravity_session watermark to schema_meta."""
    conn.execute(
        "UPDATE schema_meta SET last_gravity_session = ? WHERE id = 1",
        (session_num,),
    )


def build_gravity(
    conn: sqlite3.Connection,
    gravity_cfg: GravityConfig,
    *,
    full: bool = False,
) -> tuple[int, int]:
    """Roll up page_interactions into player_gravity and gravity_tier.

    Returns (pages_updated, pages_unencountered) counts."""
    from wiki_cli.db import PAGE_METRICS_TABLE_SQL

    conn.execute(PAGE_METRICS_TABLE_SQL)
    watermark = None if full else get_watermark(conn)

    max_session_row = conn.execute(
        "SELECT MAX(session_num) FROM page_interactions"
    ).fetchone()
    max_session: int | None = max_session_row[0] if max_session_row else None
    if max_session is None:
        return (0, 0)

    active_floor = max_session - gravity_cfg.active_window + 1

    if watermark is not None:
        affected_pages = {
            row[0]
            for row in conn.execute(
                "SELECT DISTINCT page FROM page_interactions WHERE session_num > ?",
                (watermark,),
            ).fetchall()
        }
        stale_active = {
            row[0]
            for row in conn.execute(
                "SELECT rel_path FROM page_metrics "
                "WHERE gravity_tier = 'active' AND scope = 'all' "
                "AND rel_path NOT IN ("
                "  SELECT DISTINCT page FROM page_interactions WHERE session_num >= ?"
                ")",
                (active_floor,),
            ).fetchall()
        }
        affected_pages |= stale_active
        if not affected_pages:
            return (0, 0)
    else:
        affected_pages = None

    rows = conn.execute(
        "SELECT page, session_num, mention_count FROM page_interactions"
    ).fetchall()

    gravity_map: dict[str, float] = {}
    tier_map: dict[str, str] = {}
    session_map: dict[str, set[int]] = {}

    for page, session_num, mention_count in rows:
        if affected_pages is not None and page not in affected_pages:
            continue
        if page not in session_map:
            session_map[page] = set()
        session_map[page].add(session_num)

        weight = (
            gravity_cfg.active_weight
            if session_num >= active_floor
            else gravity_cfg.encountered_weight
        )
        gravity_map[page] = gravity_map.get(page, 0.0) + mention_count * weight

    for page, sessions in session_map.items():
        if any(s >= active_floor for s in sessions):
            tier_map[page] = "active"
        else:
            tier_map[page] = "encountered"

    pages_updated = 0
    for page, gravity_val in gravity_map.items():
        tier = tier_map[page]
        conn.execute(
            "INSERT INTO page_metrics (rel_path, scope, links_in, links_out, player_gravity, gravity_tier) "
            "VALUES (?, 'all', 0, 0, ?, ?) "
            "ON CONFLICT(rel_path, scope) DO UPDATE "
            "SET player_gravity = excluded.player_gravity, gravity_tier = excluded.gravity_tier",
            (page, gravity_val, tier),
        )
        pages_updated += 1

    unencountered_cursor = conn.execute(
        "UPDATE page_metrics SET gravity_tier = 'unencountered' "
        "WHERE (gravity_tier IS NULL OR gravity_tier != 'unencountered') "
        "AND rel_path NOT IN (SELECT DISTINCT page FROM page_interactions) "
        "AND scope = 'all'"
    )
    pages_unencountered = unencountered_cursor.rowcount

    set_watermark(conn, max_session)

    return (pages_updated, pages_unencountered)
