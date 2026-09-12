"""A session run guide or beat with no session story in the episode folder —
the first rule ported after W84 (ADR-0041), matching
`utils/scripts/lint-rules/w47-story-first-gate.mjs`'s real rule id (`W47`,
see `parity.py`).

Session prep is story-first (`vault/refs/runbook-session.md` step 2): the
flowing chapter at `vault/episodes/NNN/session-NN-*.md` is written and
approved before the guide — or any `type: beat` page — is derived from it.
Episodes numbered below `STORY_GATE_MIN_SESSION` predate the gate and are
exempt — matching the legacy rule's `readOptionalNumberConstant(vaultRoot,
"STORY_GATE_MIN_SESSION", 7)` fallback.

Session directories are zero-padded to 3 (`vault/episodes/008/`); story
files to 2 (`session-08-*.md`) — normalised through the parsed session
number, not the raw regex capture, exactly as the legacy rule does.

`corpus.repo_root` (not `load_config()`) is the source of the filesystem
root this rule walks — unlike `FrontmatterSchemaRule`'s always-real
`vault/_templates/` lookup, this rule's episode-folder listing must be
swappable per-corpus for the rule to be testable against a fixture tree
instead of the real vault.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_GUIDE_RE = re.compile(
    r"^vault/episodes/(\d+)/((?:e\d+-)?run-guide(?:-[a-z0-9]+)*|e\d+-overview)\.md$"
)
_BEAT_RE = re.compile(r"^vault/episodes/(\d+)/beat-.+\.md$")
_EPISODES_DIR = "vault/episodes"


@register
class StoryFirstGateRule(FileRule):
    """Ported from npm's W47 (`utils/scripts/lint-rules/w47-story-first-gate.mjs`)."""

    id = "W47"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Write the session story at vault/episodes/NNN/session-NN-*.md with "
        "the draft-story skill first, then derive this run guide or beat from "
        "it (vault/refs/runbook-session.md step 2)."
    )
    producer = "wiki"
    pure = False
    """Depends on the episode folder's directory listing, not just this file's own bytes."""
    version = "3"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        match = _GUIDE_RE.match(page.rel_path) or _BEAT_RE.match(page.rel_path)
        if not match:
            return

        session_num = int(match.group(1))
        min_session = int(load_config().threshold("STORY_GATE_MIN_SESSION"))
        if session_num < min_session:
            return

        prefix = f"session-{session_num:02d}-"
        episode_dir = corpus.repo_root / _EPISODES_DIR / f"{session_num:03d}"
        has_story = episode_dir.is_dir() and any(
            entry.name.startswith(prefix) and entry.name.endswith(".md")
            for entry in episode_dir.iterdir()
        )
        if has_story:
            return

        yield self.finding(
            file=page.rel_path,
            line=page.body_start_line,
            message=(
                f"No session story at {_EPISODES_DIR}/{session_num:03d}/{prefix}*.md"
                " — write it first with the draft-story skill, then derive this "
                "guide or beat from it (vault/refs/runbook-session.md step 2)"
            ),
        )
