"""Ported from npm's `w-audio-asset-linked` (no W-number;
`utils/scripts/lint-rules/w-audio-asset-linked.mjs`). Same sibling-matching
shape as `art_asset_linked.py` (reused from that module — see it for the
`_TYPE_SUBFOLDERS`/session-scoping/more-specific-owner logic and the
bug-compatibility note on both) but for audio siblings (`stuff.md` matches
`stuff.mp3`, `stuff-clip.wav`, ...), no Leaflet `image:` exemption (the
legacy module has none), and never autofixable — the legacy source ships
no fix for this one.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.rules.art_asset_linked import _TEMPLATES_PREFIX, _sibling_assets


def _is_embedded(raw: str, filename: str) -> bool:
    escaped = re.escape(filename)
    embed_re = re.compile(rf"!\[\[[^\]]*{escaped}[^\]]*\]\]", re.IGNORECASE)
    return bool(embed_re.search(raw))


@register
class AudioAssetLinkedRule(FileRule):
    """Ported from npm's `w-audio-asset-linked`
    (`utils/scripts/lint-rules/w-audio-asset-linked.mjs`)."""

    id = "w-audio-asset-linked"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Embed the sibling asset in the page body: add ![[<path/to/asset>]]."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if not page.rel_path.startswith("vault/"):
            return
        if page.rel_path.startswith(_TEMPLATES_PREFIX):
            return

        config = load_config()
        extensions = frozenset(
            ext.strip().lower()
            for ext in config.threshold("AUDIO_EXTENSIONS").split(",")
            if ext.strip()
        )

        for name, _directory in _sibling_assets(page, extensions, corpus):
            if _is_embedded(page.raw, name):
                continue
            yield self.finding(
                file=page.rel_path,
                line=page.body_start_line,
                message=(
                    f'Sibling audio asset "{name}" exists but isn\'t embedded anywhere in this '
                    f"page — add ![[{name}]]"
                ),
            )
