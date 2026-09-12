"""New rule (no npm parity) — wiki-lint migration plan Task 29.

Notices vault pages that have been edited since `qmd`'s search index was
last refreshed, so a `qmd search`/`qmd query` risks serving a stale
snapshot of those pages.

The real `qmd` cache is machine-wide, not scoped to this repo, so this rule
does not read it directly. `utils/scripts/qmd-sync.mjs` (the `search:sync`
npm script) only splices this repo's collection *definitions* into
`~/.config/qmd/index.yml` — the actual content index is a separate SQLite
DB (its path is printed by `qmd status`, e.g. `~/.cache/qmd/index.sqlite`),
keyed by collection name in a `documents(collection, path, hash,
modified_at)` table. That DB is shared across every project on the machine
that runs `qmd`, and collection names are not namespaced per repo — this
repo's own `wiki`/`content` collections were found (2026-08-09, empirically:
`sqlite3 ~/.cache/qmd/index.sqlite "SELECT path FROM documents WHERE
collection='wiki'"`) to contain paths from an unrelated project, because
that project's last `qmd update` happened to run under the same collection
name. Reading that table would attribute another project's re-index time to
this vault's own pages, so there is no reliable *queryable* per-repo index
state — this is exactly the "no queryable index state" case the migration
plan's Task 29 spec calls out, and its named fallback is used instead:

A page counts as drifted when its on-disk mtime is newer than
`~/.config/qmd/index.yml`'s own mtime — the one artifact `npm run
search:sync` actually writes on this repo's behalf, and therefore the best
available proxy for "when this repo was last synced". `WIKI_CLI_QMD_SYNC_
MARKER` overrides the marker path, for tests.

A `VaultRule`: producing a single corpus-wide stale count needs every
page's mtime in one pass, not a per-page judgment.

Not pure — depends on filesystem mtimes outside any page's own bytes.
"""

from __future__ import annotations

import os
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register

_MARKER_ENV = "WIKI_CLI_QMD_SYNC_MARKER"
"""Overrides the sync-marker path (module docstring). Unset in production —
tests point it at a fixture file so marker/page mtimes are controllable."""

_DEFAULT_MARKER = Path.home() / ".config" / "qmd" / "index.yml"


def _marker_path() -> Path:
    override = os.environ.get(_MARKER_ENV, "").strip()
    return Path(override) if override else _DEFAULT_MARKER


def _marker_mtime(marker: Path) -> float:
    """0.0 (epoch) when `search:sync` has never run for this repo — every
    existing page then counts as modified since it, correctly: nothing has
    ever told qmd about them."""
    try:
        return marker.stat().st_mtime
    except OSError:
        return 0.0


@register
class IndexDriftRule(VaultRule):
    """New rule (wiki-lint migration plan Task 29, no npm parity)."""

    id = "wiki/index-drift"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Run `npm run search:sync` to rebuild qmd's index over the listed pages — "
        "`npm run search:content` answers from the index, so until it is re-synced a query "
        "reads their pre-edit text. Touching the pages again without re-syncing is not a fix."
    )
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        marker = _marker_path()
        marker_mtime = _marker_mtime(marker)

        stale: list[str] = []
        for page in corpus.pages():
            try:
                page_mtime = (corpus.repo_root / page.rel_path).stat().st_mtime
            except OSError:
                continue
            if page_mtime > marker_mtime:
                stale.append(page.rel_path)

        if not stale:
            return

        stale.sort()
        yield self.finding(
            file=stale[0],
            line=1,
            message=(
                f"{len(stale)} vault page(s) modified since qmd's search index was "
                f"last synced ({marker}) — qmd's own index state is a machine-wide "
                "cache shared across projects, not reliably queryable per-repo, so "
                "staleness here is measured as page mtime against the last "
                "`search:sync`. FIX: run npm run search:sync"
            ),
        )
