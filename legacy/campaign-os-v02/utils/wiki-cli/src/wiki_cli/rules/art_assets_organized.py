"""Ported from npm's `w-art-assets-organized` (no W-number;
`utils/scripts/lint-rules/w-art-assets-organized.mjs`,
`lib/looseAssets.mjs`).

An image file sitting anywhere inside `vault/**` outside the flat, top-
level `_assets/<type>/` tree is "loose" — every image belongs in
`_assets/<type>/` (`vault/_templates/CLAUDE.md`), not beside the content it
illustrates. `sessions/*/audio/**` raw recordings (a different pipeline's
own output; the audio subtree name is reused so this rule's audio sibling
can skip it uniformly, see `audio_assets_organized.py`) are the sole
carve-out. `.claude/` (and any other dot-directory) is never scanned —
skills/tooling assets are not content.

LEGACY-BUG (verified empirically 2026-08-09, `npm run lint`'s real
full-vault sweep): the npm rule's `listLooseAssetFiles` walk never excludes
`vault/_assets/**` itself, so a genuine full sweep (`CAMPAIGN_OS_LINT_ASSET_
SWEEP=1`, the env var `lint-findings.mjs` sets on exactly one markdownlint
shard of a real `npm run lint` with no path args) currently reports every
*already-organized* asset as "loose" — probed directly against
`markdownlint-obsidian` with that env var set: 400 spurious hits on a
single unrelated file, all misattributed to whichever file the module-
level `reported` guard happened to fire on first, since a whole-corpus
finding has no real per-file line to sit at. This wiki-cli port implements
the evidently-intended, bug-free behavior (exclude `_assets/` from the
walk) instead of bug-compatibly reproducing that misattribution, for two
reasons: (1) `parity.py`'s `--live` harness invokes `npm run lint` once per
single file (`files.length === 1`), which never sets `CAMPAIGN_OS_LINT_
ASSET_SWEEP` — so npm-side findings for this rule are structurally always
empty through `--live`, regardless of what this port does; (2) the bug's
exact `(file, line)` attribution is non-deterministic (depends on
markdownlint's shard/file processing order), so there is no stable target
to bug-compatibly match even in principle. Flagged for Task 32's post-
retirement fix-pass ledger. As of this port, the real vault carries zero
loose images either way (verified via direct filesystem check), so this
divergence produces no live-vault diff today.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register

_SCAN_ROOT = "vault"
_ASSETS_DIR = "_assets"
_AUDIO_PIPELINE_DIR = "audio"


def _loose_asset_files(vault_dir: Path, extensions: frozenset[str]) -> list[Path]:
    """Every file under `vault_dir` whose lowercased suffix is in
    `extensions`, skipping hidden directories, the organized `_assets/`
    tree itself (see the LEGACY-BUG note above), and any `audio/` subtree
    (a different pipeline's raw output — matches `looseAssets.mjs`'s
    `insideAudioPipeline` flag, which applies to both the image and audio
    scans alike)."""
    found: list[Path] = []

    def walk(directory: Path, inside_audio_pipeline: bool) -> None:
        try:
            entries = sorted(directory.iterdir())
        except OSError:
            return
        for entry in entries:
            if entry.name.startswith("."):
                continue
            if entry.is_dir():
                if entry.name == _ASSETS_DIR and directory == vault_dir:
                    continue
                walk(entry, inside_audio_pipeline or entry.name == _AUDIO_PIPELINE_DIR)
            elif not inside_audio_pipeline and entry.suffix.lower().lstrip(".") in extensions:
                found.append(entry)

    walk(vault_dir, False)
    return found


@register
class ArtAssetsOrganizedRule(VaultRule):
    """Ported from npm's `w-art-assets-organized`
    (`utils/scripts/lint-rules/w-art-assets-organized.mjs`)."""

    id = "w-art-assets-organized"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "Move the image into _assets/<type>/ (see vault/_templates/CLAUDE.md)."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        config = load_config()
        extensions = frozenset(
            ext.strip().lower()
            for ext in config.threshold("IMAGE_EXTENSIONS").split(",")
            if ext.strip()
        )
        asset_subfolders = [
            folder.strip()
            for folder in config.threshold("ASSET_SUBFOLDERS").split(",")
            if folder.strip()
        ]
        vault_dir = corpus.repo_root / _SCAN_ROOT
        for full in _loose_asset_files(vault_dir, extensions):
            rel = str(full.relative_to(corpus.repo_root))
            yield self.finding(
                file=rel,
                line=1,
                message=(
                    f"{rel} is a loose image sitting inside vault/** — move it into "
                    f"_assets/<type>/ ({', '.join(asset_subfolders)})"
                ),
            )
