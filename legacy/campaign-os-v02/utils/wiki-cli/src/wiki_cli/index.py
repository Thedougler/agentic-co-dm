"""SQLite-cached `Corpus` (contracts.py) implementation over a vault directory."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import TYPE_CHECKING

from wiki_cli import db
from wiki_cli.config import load_config
from wiki_cli.markdown import load_page

if TYPE_CHECKING:
    import sqlite3
    from collections.abc import Sequence

    from wiki_cli.contracts import Page

_VALE_TEMP_RE = re.compile(r"\.vale-(?:fm|chunk)-\d+-")
"""Same ephemeral prose-tooling copies `orchestrator.py` filters out of target
discovery (`<stem>.vale-fm-<pid>-<uuid>.md`, `utils/scripts/lib/prose-scope.mjs`).
The index walks the whole vault rather than a target list, so it needs the
filter independently: under concurrent agents this walk enumerates another
run's copy microseconds before that run deletes it, and `load_page` then
raises a fatal `FileNotFoundError` that aborts the entire lint."""

_LINK_TARGET_RE = re.compile(r"!?\[\[([^\]|]+?)(?:\|[^\]]*)?\]\]")
_HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$")
_H1_RE = re.compile(r"^#\s+(.*)$")

_TYPED_FM_KEYS: dict[str, str] = {
    "within": "CONTAINS",
    "location": "LOCATED_AT",
    "factions": "MEMBER_OF",
    "owner": "OWNED_BY",
    "origin": "ORIGINATES_FROM",
    "episode": "CANON_IN",
}


def _fm_target_name(value: str) -> str:
    """Normalize a frontmatter wikilink value to a raw target name.

    Strips [[...]] brackets and display-name aliases (|...), keeping any
    #heading anchor. Returns '' for blank/whitespace-only input."""
    text = value.strip()
    if text.startswith("[[") and text.endswith("]]"):
        text = text[2:-2]
    return text.split("|", 1)[0].strip()


def _typed_fm_edges_of(page: Page) -> list[tuple[str, str, str]]:
    """Return (raw_target, fm_key, link_type) for each non-empty typed
    frontmatter relationship on `page`.

    Values may be scalars or lists (e.g. `factions:`); each resolves to one
    edge row. Empty/whitespace values are skipped — they produce no edge."""
    results: list[tuple[str, str, str]] = []
    for fm_key, link_type in _TYPED_FM_KEYS.items():
        raw = page.frontmatter.get(fm_key)
        if raw is None:
            continue
        if isinstance(raw, list):
            values: list[str] = [v for v in raw if isinstance(v, str)]
        elif isinstance(raw, str):
            values = [raw]
        else:
            continue
        for value in values:
            target = _fm_target_name(value)
            if target:
                results.append((target, fm_key, link_type))
    return results

_PAGES_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS pages (
    rel_path TEXT PRIMARY KEY,
    mtime_ns INTEGER NOT NULL,
    content_hash TEXT NOT NULL,
    type TEXT,
    slug TEXT NOT NULL,
    aliases_json TEXT NOT NULL,
    links_json TEXT NOT NULL,
    headings_json TEXT NOT NULL,
    uid TEXT,
    "unique" INTEGER DEFAULT NULL
)
"""

_LINKS_TABLE_SQL = """
CREATE TABLE IF NOT EXISTS links (
    source TEXT NOT NULL,
    target TEXT,
    raw_target TEXT NOT NULL,
    section TEXT NOT NULL DEFAULT '',
    count INTEGER NOT NULL DEFAULT 1,
    link_type TEXT,
    PRIMARY KEY (source, raw_target, section)
)
"""

_LINKS_TARGET_IDX_SQL = "CREATE INDEX IF NOT EXISTS links_target_idx ON links (target)"



def _strip_md(value: str) -> str:
    return value.removesuffix(".md")


def _aliases_of(page: Page) -> list[str]:
    raw = page.frontmatter.get("aliases")
    if isinstance(raw, list):
        return [item for item in raw if isinstance(item, str)]
    return []


def _links_of(page: Page) -> list[str]:
    return [match.group(1).strip() for match in _LINK_TARGET_RE.finditer(page.body)]


def _headings_of(page: Page) -> list[str]:
    return [
        match.group(1).strip()
        for _, line in page.body_lines()
        if (match := _HEADING_RE.match(line))
    ]


def links_with_sections(page: Page) -> list[tuple[str, str]]:
    """`(raw_target, section)` per wikilink occurrence in `page`'s body —
    `section` is the nearest preceding heading text, or `''` before the
    first heading."""
    results: list[tuple[str, str]] = []
    section = ""
    for _, line in page.body_lines():
        heading_match = _HEADING_RE.match(line)
        if heading_match:
            section = heading_match.group(1).strip()
            continue
        for link_match in _LINK_TARGET_RE.finditer(line):
            results.append((link_match.group(1).strip(), section))
    return results


def _title_of(page: Page) -> str | None:
    """Frontmatter `title:`, else the first `# H1` in the body. Always
    computed live — there is no cached column for it, unlike aliases/links/
    headings, which the SQLite row skips recomputing on an unchanged mtime."""
    fm_title = page.frontmatter.get("title")
    if isinstance(fm_title, str) and fm_title.strip():
        return fm_title.strip()
    for _, line in page.body_lines():
        match = _H1_RE.match(line)
        if match:
            return match.group(1).strip()
    return None


class VaultIndex:
    """`Corpus` over one vault directory, backed by a SQLite page-row cache
    keyed on file mtime — a page's aliases/links/headings re-derive only
    when its `mtime_ns` changes; unchanged pages read the cached row."""

    def __init__(
        self,
        repo_root: Path,
        pages: list[Page],
        derived: dict[str, tuple[list[str], list[str], list[str]]],
        parses_performed: int,
        content_hashes: dict[str, str],
        corpus_fingerprint: str,
        link_data: dict[str, list[tuple[str, str]]],
    ) -> None:
        self.repo_root = repo_root
        self.parses_performed = parses_performed
        self.corpus_fingerprint = corpus_fingerprint
        self._pages = pages
        self._content_hashes = content_hashes
        self._link_data = link_data
        self._pages_by_path: dict[str, Page] = {}
        self._by_type: dict[str, list[Page]] = {}
        self._by_rel_path: dict[str, Page] = {}
        self._by_basename: dict[str, list[Page]] = {}
        self._by_alias: dict[str, Page] = {}
        self._by_title: dict[str, Page] = {}
        self._links_from: dict[str, list[str]] = {}

        for page in pages:
            self._pages_by_path[page.rel_path] = page
            self._by_rel_path[_strip_md(page.rel_path).lower()] = page
            self._by_basename.setdefault(page.slug.lower(), []).append(page)
            if page.type is not None:
                self._by_type.setdefault(page.type, []).append(page)

            aliases, links, _ = derived[page.rel_path]
            self._links_from[page.rel_path] = links
            for alias in aliases:
                self._by_alias.setdefault(alias.lower(), page)

            title = _title_of(page)
            if title:
                self._by_title.setdefault(title.lower(), page)

        self._links_to: dict[str, list[str]] = {}
        for page in pages:
            for target in self._links_from.get(page.rel_path, []):
                base_target = target.split("#", 1)[0]
                resolved = self.resolve(base_target)
                if resolved is not None:
                    self._links_to.setdefault(resolved.rel_path, []).append(page.rel_path)

    @classmethod
    def build(cls, repo_root: Path, vault_root: Path, scoped_roots: tuple[str, ...]) -> VaultIndex:
        """Build the FULL index over `vault_root` — corpus rules need the
        whole graph even on a scoped run, so `scoped_roots` (which rules a
        given invocation gates on) never narrows what gets indexed here."""
        del scoped_roots  # accepted for interface parity; the index is never partial.

        config = load_config(repo_root)
        conn = db.connect(config.cache_path)
        conn.execute(_PAGES_TABLE_SQL)
        conn.execute(_LINKS_TABLE_SQL)
        conn.execute(_LINKS_TARGET_IDX_SQL)
        conn.execute(db.PAGE_METRICS_TABLE_SQL)

        pages: list[Page] = []
        derived: dict[str, tuple[list[str], list[str], list[str]]] = {}
        content_hashes: dict[str, str] = {}
        link_data: dict[str, list[tuple[str, str]]] = {}
        parses_performed = 0

        for path in sorted(vault_root.rglob("*.md")):
            # Skill/agent trees (vault/**/.claude/) and vendored packages
            # (node_modules) under the vault are not wiki pages — indexing
            # them turns names like "SKILL"/"AGENTS" into W25 link-target
            # candidates (same skip set as producers/context_rot.py).
            if any(
                part == "node_modules" or part.startswith(".")
                for part in path.relative_to(vault_root).parts[:-1]
            ):
                continue
            if _VALE_TEMP_RE.search(path.name):
                continue
            rel_path = str(path.relative_to(repo_root))
            page = load_page(repo_root, rel_path)
            pages.append(page)
            link_data[rel_path] = links_with_sections(page)

            mtime_ns = path.stat().st_mtime_ns
            row = conn.execute(
                "SELECT mtime_ns, content_hash, aliases_json, links_json, headings_json "
                "FROM pages WHERE rel_path = ?",
                (rel_path,),
            ).fetchone()

            reparsed = row is None or row[0] != mtime_ns

            if not reparsed:
                assert row is not None
                content_hashes[rel_path] = row[1]
                derived[rel_path] = (json.loads(row[2]), json.loads(row[3]), json.loads(row[4]))
            else:
                parses_performed += 1
                aliases = _aliases_of(page)
                links = _links_of(page)
                headings = _headings_of(page)
                derived[rel_path] = (aliases, links, headings)

                ch = hashlib.sha256(page.raw.encode("utf-8")).hexdigest()
                content_hashes[rel_path] = ch

                unique_val: int | None
                if page.type == "item":
                    unique_val = 1 if page.frontmatter.get("unique") is True else 0
                else:
                    unique_val = None

                conn.execute(
                    "INSERT INTO pages (rel_path, mtime_ns, content_hash, type, slug, "
                    'aliases_json, links_json, headings_json, "unique") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?) '
                    "ON CONFLICT (rel_path) DO UPDATE SET "
                    "mtime_ns = excluded.mtime_ns, content_hash = excluded.content_hash, "
                    "type = excluded.type, slug = excluded.slug, "
                    'aliases_json = excluded.aliases_json, links_json = excluded.links_json, '
                    'headings_json = excluded.headings_json, "unique" = excluded."unique"',
                    (
                        rel_path,
                        mtime_ns,
                        ch,
                        page.type,
                        page.slug,
                        json.dumps(aliases),
                        json.dumps(links),
                        json.dumps(headings),
                        unique_val,
                    ),
                )

            has_links_rows = (
                conn.execute(
                    "SELECT 1 FROM links WHERE source = ? LIMIT 1", (rel_path,)
                ).fetchone()
                is not None
            )
            if reparsed or not has_links_rows:
                conn.execute("DELETE FROM links WHERE source = ?", (rel_path,))
                counts: dict[tuple[str, str], int] = {}
                for raw_target, section in link_data[rel_path]:
                    counts[(raw_target, section)] = counts.get((raw_target, section), 0) + 1
                for (raw_target, section), count in counts.items():
                    conn.execute(
                        "INSERT INTO links (source, target, raw_target, section, count) "
                        "VALUES (?, NULL, ?, ?, ?)",
                        (rel_path, raw_target, section, count),
                    )
                for raw_target, fm_key, link_type in _typed_fm_edges_of(page):
                    conn.execute(
                        "INSERT OR IGNORE INTO links "
                        "(source, target, raw_target, section, count, link_type) "
                        "VALUES (?, NULL, ?, ?, 1, ?)",
                        (rel_path, raw_target, fm_key, link_type),
                    )

        corpus_fp = hashlib.sha256(
            "\x00".join(
                f"{rp}\x01{content_hashes[rp]}"
                for rp in sorted(content_hashes)
            ).encode("utf-8")
        ).hexdigest()[:16]

        index = cls(repo_root, pages, derived, parses_performed, content_hashes, corpus_fp, link_data)
        index._persist_graph(conn)
        return index

    def _persist_graph(self, conn: sqlite3.Connection) -> None:
        """Refresh resolved link targets, drop rows for pages no longer in
        the corpus, and upsert `page_metrics` in/out counts — called once at
        the end of `build()`, after the full in-memory index (and therefore
        `resolve`) is available."""
        for rowid, raw_target in conn.execute("SELECT rowid, raw_target FROM links").fetchall():
            resolved = self.resolve(raw_target.split("#", 1)[0])
            target = resolved.rel_path if resolved is not None else None
            conn.execute("UPDATE links SET target = ? WHERE rowid = ?", (target, rowid))

        existing = {page.rel_path for page in self._pages}

        stale_link_sources = [
            row[0]
            for row in conn.execute("SELECT DISTINCT source FROM links").fetchall()
            if row[0] not in existing
        ]
        for source in stale_link_sources:
            conn.execute("DELETE FROM links WHERE source = ?", (source,))

        stale_metrics = [
            row[0]
            for row in conn.execute("SELECT DISTINCT rel_path FROM page_metrics").fetchall()
            if row[0] not in existing
        ]
        for rel_path in stale_metrics:
            conn.execute("DELETE FROM page_metrics WHERE rel_path = ?", (rel_path,))

        for page in self._pages:
            links_out = len(self._links_from.get(page.rel_path, []))
            links_in = len(self._links_to.get(page.rel_path, []))
            row = conn.execute(
                "SELECT links_in, links_out FROM page_metrics WHERE rel_path = ? AND scope = 'all'",
                (page.rel_path,),
            ).fetchone()
            dirty = 1 if row is None or row[0] != links_in or row[1] != links_out else 0
            conn.execute(
                "INSERT INTO page_metrics (rel_path, scope, links_in, links_out, pagerank, dirty) "
                "VALUES (?, 'all', ?, ?, NULL, ?) "
                "ON CONFLICT (rel_path, scope) DO UPDATE SET "
                "links_in = excluded.links_in, links_out = excluded.links_out, "
                "dirty = CASE WHEN page_metrics.links_in != excluded.links_in "
                "OR page_metrics.links_out != excluded.links_out THEN 1 ELSE page_metrics.dirty END",
                (page.rel_path, links_in, links_out, dirty),
            )

    def get_page(self, rel_path: str) -> Page | None:
        """Return the loaded Page for an exact rel_path, or None."""
        return self._pages_by_path.get(rel_path)

    def content_hash(self, rel_path: str) -> str | None:
        """Return the content hash for a rel_path, or None."""
        return self._content_hashes.get(rel_path)

    def pages(self) -> Sequence[Page]:
        return list(self._pages)

    def resolve(self, name: str) -> Page | None:
        """Case-insensitive, Obsidian-style precedence: exact rel-path >
        unique basename > alias > title."""
        key = name.strip()
        if not key:
            return None
        key_lower = _strip_md(key).lower()

        exact = self._by_rel_path.get(key_lower)
        if exact is not None:
            return exact

        candidates = self._by_basename.get(key_lower)
        if candidates is not None and len(candidates) == 1:
            return candidates[0]

        alias = self._by_alias.get(key_lower)
        if alias is not None:
            return alias

        return self._by_title.get(key_lower)

    def by_type(self, page_type: str) -> Sequence[Page]:
        return list(self._by_type.get(page_type, []))

    def links_from(self, rel_path: str) -> Sequence[str]:
        return list(self._links_from.get(rel_path, []))

    def links_to(self, rel_path: str) -> Sequence[str]:
        return list(self._links_to.get(rel_path, []))

    def links_detail(self, rel_path: str) -> list[tuple[str | None, str, str, int]]:
        """`(target, raw_target, section, count)` per distinct link occurrence
        from `rel_path`, read from the in-memory graph (never the DB)."""
        counts: dict[tuple[str, str], int] = {}
        for raw_target, section in self._link_data.get(rel_path, []):
            counts[(raw_target, section)] = counts.get((raw_target, section), 0) + 1
        detail: list[tuple[str | None, str, str, int]] = []
        for (raw_target, section), count in counts.items():
            resolved = self.resolve(raw_target.split("#", 1)[0])
            target = resolved.rel_path if resolved is not None else None
            detail.append((target, raw_target, section, count))
        return detail

    def ambiguous(self, name: str) -> list[str]:
        """Every rel_path sharing `name`'s basename, case-insensitively."""
        return sorted(page.rel_path for page in self._by_basename.get(name.strip().lower(), []))
