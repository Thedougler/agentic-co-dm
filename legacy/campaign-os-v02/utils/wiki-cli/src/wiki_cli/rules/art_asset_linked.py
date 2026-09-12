"""Ported from npm's `w-art-asset-linked` (no W-number;
`utils/scripts/lint-rules/w-art-asset-linked.mjs`, sibling-matching logic
in `lib/siblingAssets.mjs`).

If a markdown page has a sibling art asset (same slug, optionally a
`-suffix`: `stuff.md` matches `stuff.png`, `stuff-portrait.png`,
`stuff-banner.png`, ... but never `stuffed.png`), the page body must
reference it via a real Obsidian embed (`![[filename]]` / `![[filename|
alt]]`) or, on a page using the Leaflet plugin, an `image:` parameter
inside a ```leaflet block — both are genuine, plugin-rendered usage, not an
orphaned asset. When two pages' slugs both prefix-match one asset (e.g.
`hcs-surety-layout-galley.webp` matches both `hcs-surety` and
`hcs-surety-layout`), only the longer (more specific) slug's page owns it.

`_TYPE_SUBFOLDERS` is the legacy module's own hardcoded asset-subfolder
list (`lib/siblingAssets.mjs`), not the `ASSET_SUBFOLDERS` threshold (which
additionally lists `reference` and is used only for *message* text
elsewhere in this cluster) — copied verbatim rather than read from config
to match detection logic exactly, per the port's bug-compatibility rule;
it was never threshold-driven in the legacy source either. Same for the
session-number regex (`^sessions/(\\d{2})`): it is ported byte-for-byte
even though the real vault uses `vault/episodes/NN/` rather than a
top-level `sessions/` root, so it never actually matches any real page —
dead code inherited from the legacy source, not "fixed" here, since a rule
module's job is detection parity, not correcting a stale convention.

Not `pure` — resolving siblings needs the real `_assets/` filesystem and
every other page's slug (to defer to a more specific owner), not just this
page's own bytes.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_TEMPLATES_PREFIX = "vault/_templates/"
_ASSETS_ROOT = "_assets"
_TYPE_SUBFOLDERS = (
    "banners",
    "portraits",
    "layouts",
    "maps",
    "battlemaps",
    "scene-art",
    "dialogue",
    "audio",
    "misc",
    "character-sheets",
)
_SESSION_SCOPED_TYPES = frozenset({"scene-art", "battlemaps"})
_SESSION_NUMBER_RE = re.compile(r"^sessions/(\d{2})")


# Both caches below are keyed on `corpus` object identity, the same
# single-slot-scoped-to-the-run pattern `unlinked_mention.py`'s
# `_scan_index_cache` uses: one `wiki lint` run builds one `VaultIndex` and
# calls `_sibling_assets` once per page (twice counting `audio_asset_linked.
# py`'s reuse), so without this every `_TYPE_SUBFOLDERS` directory got
# re-`iterdir()`'d and every other page's slug re-listed on every single
# page — the dominant cost of a full-vault sweep (measured: ~17s of a ~65s
# `wiki` producer total across 2547 pages). A different corpus (a new run,
# or a new fixture `VaultIndex` in tests) simply rebuilds once.
_dir_listing_cache: tuple[Corpus, dict[Path, tuple[str, ...]]] | None = None
_all_slugs_cache: tuple[Corpus, list[str]] | None = None


def _dir_names(directory: Path, corpus: Corpus) -> tuple[str, ...]:
    global _dir_listing_cache
    if _dir_listing_cache is None or _dir_listing_cache[0] is not corpus:
        _dir_listing_cache = (corpus, {})
    cache = _dir_listing_cache[1]
    cached = cache.get(directory)
    if cached is not None:
        return cached
    try:
        names = tuple(sorted(entry.name for entry in directory.iterdir() if entry.is_file()))
    except OSError:
        names = ()
    cache[directory] = names
    return names


def _all_slugs(corpus: Corpus) -> list[str]:
    global _all_slugs_cache
    if _all_slugs_cache is not None and _all_slugs_cache[0] is corpus:
        return _all_slugs_cache[1]
    slugs = [page.slug for page in corpus.pages()]
    _all_slugs_cache = (corpus, slugs)
    return slugs


def _matching_files(
    directory: Path, slug: str, extensions: frozenset[str], corpus: Corpus
) -> list[str]:
    names = _dir_names(directory, corpus)
    matches = []
    for name in names:
        dot = name.rfind(".")
        if dot == -1:
            continue
        if name[dot + 1 :].lower() not in extensions:
            continue
        base = name[:dot]
        if base == slug or base.startswith(f"{slug}-"):
            matches.append(name)
    return matches


def _sibling_assets(
    page: Page, extensions: frozenset[str], corpus: Corpus
) -> list[tuple[str, Path]]:
    """`[(filename, containing_dir), ...]` — every sibling asset this page
    owns (not deferred to a more specific same-prefix page)."""
    slug = page.slug
    session_match = _SESSION_NUMBER_RE.match(page.rel_path)
    session_number = session_match.group(1) if session_match else None
    # Every OTHER page's slug, per the docstring above — but `page`'s own
    # slug can never satisfy `len(other) > len(slug)` below (equal length),
    # so it's safe (and, via `_all_slugs`, far cheaper) to pass the full
    # corpus list unfiltered rather than rebuilding a self-excluded one on
    # every call.
    other_slugs = _all_slugs(corpus)

    found: list[tuple[str, Path]] = []
    for subfolder in _TYPE_SUBFOLDERS:
        type_dir = corpus.repo_root / "vault" / _ASSETS_ROOT / subfolder
        found.extend(
            (name, type_dir) for name in _matching_files(type_dir, slug, extensions, corpus)
        )
        if session_number and subfolder in _SESSION_SCOPED_TYPES:
            session_dir = type_dir / f"session-{session_number}"
            found.extend(
                (name, session_dir)
                for name in _matching_files(session_dir, slug, extensions, corpus)
            )

    owned: list[tuple[str, Path]] = []
    for name, directory in found:
        dot = name.rfind(".")
        base = name[:dot] if dot != -1 else name
        more_specific_owner_exists = any(
            len(other) > len(slug) and (base == other or base.startswith(f"{other}-"))
            for other in other_slugs
        )
        if not more_specific_owner_exists:
            owned.append((name, directory))
    return owned


def _is_embedded(raw: str, filename: str) -> bool:
    escaped = re.escape(filename)
    embed_re = re.compile(rf"!\[\[[^\]]*{escaped}[^\]]*\]\]", re.IGNORECASE)
    if embed_re.search(raw):
        return True
    # W128 autofix strips path-qualified embeds to bare slugs (no extension),
    # so also match ![[stem]] / ![[stem|alt]] / ![[stem#heading]].
    stem = Path(filename).stem
    stem_escaped = re.escape(stem)
    stem_re = re.compile(rf"!\[\[{stem_escaped}(?:[#|][^\]]*?)?\]\]", re.IGNORECASE)
    if stem_re.search(raw):
        return True
    leaflet_image_re = re.compile(
        rf"image:\s*(?:\n\s*-\s*)?\[\[[^\]]*{escaped}[^\]]*\]\]", re.IGNORECASE
    )
    return bool(leaflet_image_re.search(raw))


@register
class ArtAssetLinkedRule(FileRule):
    """Ported from npm's `w-art-asset-linked`
    (`utils/scripts/lint-rules/w-art-asset-linked.mjs`)."""

    id = "w-art-asset-linked"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Embed the sibling asset in the page body: add ![[<path/to/asset>]] near the top."
    producer = "wiki"
    pure = False
    fixable = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if not page.rel_path.startswith("vault/"):
            return
        if page.rel_path.startswith(_TEMPLATES_PREFIX):
            return

        config = load_config()
        extensions = frozenset(
            ext.strip().lower()
            for ext in config.threshold("IMAGE_EXTENSIONS").split(",")
            if ext.strip()
        )

        for name, directory in _sibling_assets(page, extensions, corpus):
            if _is_embedded(page.raw, name):
                continue
            embed_path = str((directory / name).relative_to(corpus.repo_root))
            yield self.finding(
                file=page.rel_path,
                line=page.body_start_line,
                message=(
                    f'Sibling art asset "{name}" exists but isn\'t embedded anywhere in this '
                    f"page — add ![[{embed_path}]]"
                ),
            )
