"""Ported from npm's `w-orphan-art-assets` (no W-number;
`utils/scripts/lint-rules/w-orphan-art-assets.mjs`).

A file inside `_assets/banners/` or `_assets/portraits/` whose slug
(filename minus a `-banner`/`-banner-alt`/`-portrait`/`-portrait-alt`
suffix) doesn't match any markdown page anywhere under `vault/` has no
owning page — not just "not embedded" (`art_asset_linked.py`'s job),
genuinely orphaned art that may be lost/unused. Scoped to banners/portraits
only (`SLUG_SUBFOLDERS`) — battlemaps/layouts/scene-art don't follow a 1:1
slug-to-page convention.

Uses the already-built `Corpus.pages()` page index for the slug set rather
than a second, independent filesystem walk (the legacy module's own
`vaultPageSlugs` re-walks `vault/` from scratch) — the one behavioral
difference this introduces is that a page under a dot-directory (e.g.
`.claude/`), which the legacy walk explicitly skips, would count as a valid
slug owner here. That only ever makes this check *more* lenient (fewer
false "orphan" hits, never more), and produces no live-vault diff — no
dot-directory page shares a slug with any real banner/portrait asset today.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register

_ASSETS_ROOT = "_assets"
_SUFFIXES = ("-banner-alt", "-banner", "-portrait-alt", "-portrait")


def _derive_slug(filename: str) -> str:
    base = filename.rsplit(".", 1)[0] if "." in filename else filename
    lowered = base.lower()
    for suffix in _SUFFIXES:
        if lowered.endswith(suffix):
            return lowered[: -len(suffix)]
    return lowered


@register
class OrphanArtAssetsRule(VaultRule):
    """Ported from npm's `w-orphan-art-assets`
    (`utils/scripts/lint-rules/w-orphan-art-assets.mjs`)."""

    id = "w-orphan-art-assets"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "Delete the orphaned asset, or add the page it belongs to."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        config = load_config()
        slug_subfolders = [
            folder.strip()
            for folder in config.threshold("SLUG_SUBFOLDERS").split(",")
            if folder.strip()
        ]
        page_slugs = {page.slug.lower() for page in corpus.pages()}

        for subfolder in slug_subfolders:
            directory = corpus.repo_root / "vault" / _ASSETS_ROOT / subfolder
            try:
                names = sorted(entry.name for entry in Path(directory).iterdir() if entry.is_file())
            except OSError:
                continue
            for name in names:
                slug = _derive_slug(name)
                if slug in page_slugs:
                    continue
                rel = f"vault/{_ASSETS_ROOT}/{subfolder}/{name}"
                yield self.finding(
                    file=rel,
                    line=1,
                    message=(
                        f"{rel} has no matching page anywhere under vault/ (derived slug "
                        f'"{slug}") — orphaned art, may be lost/unused'
                    ),
                )
