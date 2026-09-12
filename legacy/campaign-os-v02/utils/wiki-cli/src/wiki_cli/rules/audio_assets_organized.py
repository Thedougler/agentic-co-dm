"""Ported from npm's `w-audio-assets-organized` (no W-number;
`utils/scripts/lint-rules/w-audio-assets-organized.mjs`,
`lib/looseAssets.mjs`). Same shape as `art_assets_organized.py` (see that
module for the shared walk logic and the LEGACY-BUG note this rule
inherits verbatim — same root cause, same helper in the legacy engine)
but for audio files. `sessions/*/audio/**` raw recordings are
record-session-audio's own pipeline output and are excluded from the walk
outright (any `audio/`-named directory, anywhere, is skipped).
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register
from wiki_cli.rules.art_assets_organized import _loose_asset_files

_SCAN_ROOT = "vault"


@register
class AudioAssetsOrganizedRule(VaultRule):
    """Ported from npm's `w-audio-assets-organized`
    (`utils/scripts/lint-rules/w-audio-assets-organized.mjs`)."""

    id = "w-audio-assets-organized"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "Move the audio file into _assets/dialogue/ (see vault/_templates/CLAUDE.md)."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        config = load_config()
        extensions = frozenset(
            ext.strip().lower()
            for ext in config.threshold("AUDIO_EXTENSIONS").split(",")
            if ext.strip()
        )
        vault_dir = corpus.repo_root / _SCAN_ROOT
        for full in _loose_asset_files(vault_dir, extensions):
            rel = str(full.relative_to(corpus.repo_root))
            yield self.finding(
                file=rel,
                line=1,
                message=(
                    f"{rel} is a loose audio file sitting inside vault/** — move it into "
                    "_assets/dialogue/"
                ),
            )
