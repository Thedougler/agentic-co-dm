"""Shared command runtime for the read-layer CLI commands (`wiki list`,
`wiki search`, `wiki links`): loading config/index/db once and turning the
vault into `Row`s ready for `filters`/`output`.
"""

from __future__ import annotations

import sqlite3
from dataclasses import dataclass

from wiki_cli import db
from wiki_cli.config import Config, load_config
from wiki_cli.index import VaultIndex
from wiki_cli.query.filters import COMPUTED_KEYS, Row
from wiki_cli.query.pagerank import ensure_pagerank
from wiki_cli.query.schema import legal_filter_keys


@dataclass(frozen=True, slots=True)
class QueryContext:
    config: Config
    index: VaultIndex
    conn: sqlite3.Connection
    legal_keys: frozenset[str]


def load_context(needs_pagerank: bool = False) -> QueryContext:
    """Load config, build/open the vault index, connect to the cache, and
    resolve the legal `--where`/`--sort` key set. `needs_pagerank` triggers
    a (lazy, dirty-flagged) PageRank recompute before any row is built."""
    config = load_config()
    index = VaultIndex.build(config.repo_root, config.vault_root.resolve(), ())
    conn = db.connect(config.cache_path)
    legal = legal_filter_keys(config.templates_root) | COMPUTED_KEYS
    if needs_pagerank:
        ensure_pagerank(conn, weights=config.pagerank.weights)
    return QueryContext(config=config, index=index, conn=conn, legal_keys=legal)


def _templates_prefix(config: Config) -> str:
    rel = config.templates_root.resolve().relative_to(config.repo_root.resolve())
    return f"{rel}/"


def rows_for(ctx: QueryContext, include_templates: bool = False) -> list[Row]:
    """Every vault page as a `Row`, with `links-in`/`links-out`/`pagerank`
    pulled from `page_metrics` (scope `all`) and `mtime` from disk. Skips
    pages under the configured templates root unless `include_templates`."""
    templates_prefix = _templates_prefix(ctx.config)
    rows: list[Row] = []
    for page in ctx.index.pages():
        if not include_templates and page.rel_path.startswith(templates_prefix):
            continue

        metrics = ctx.conn.execute(
            "SELECT links_in, links_out, pagerank FROM page_metrics "
            "WHERE rel_path = ? AND scope = 'all'",
            (page.rel_path,),
        ).fetchone()
        links_in = metrics[0] if metrics else 0
        links_out = metrics[1] if metrics else 0
        pagerank = metrics[2] if metrics else None

        try:
            mtime = (ctx.config.repo_root / page.rel_path).stat().st_mtime
        except OSError:
            mtime = 0.0

        computed: dict[str, object] = {
            "path": page.rel_path,
            "links-in": links_in,
            "links-out": links_out,
            "pagerank": pagerank,
            "mtime": mtime,
        }
        rows.append(Row(rel_path=page.rel_path, frontmatter=dict(page.frontmatter), computed=computed))
    return rows
