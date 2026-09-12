"""W142 — session ≥ RUN_GUIDE_SHAPE_MIN_SESSION must not use ## What's True."""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_EPISODE_DIR_RE = re.compile(r"^vault/episodes/(\d+)/")
_WHATS_TRUE_RE = re.compile(r"^## What's True\s*$")
_SOURCE = "vault/_templates/_episodes/_beat_*.md"


def _min_session() -> int:
    return int(load_config().threshold("RUN_GUIDE_SHAPE_MIN_SESSION"))


@register
class BannedHeadingRule(FileRule):
    """W142 — What's True is a junk-drawer heading; use What Happens."""

    id = "W142"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Rename ## What's True to ## What Happens. Move an NPC ask to "
        "## What they want and rolls to ## Checks "
        f"({_SOURCE})."
    )
    producer = "wiki"
    pure = True
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        match = _EPISODE_DIR_RE.match(rel)
        if match is None:
            return
        if int(match.group(1)) < _min_session():
            return

        for line_no, text in page.body_lines():
            if _WHATS_TRUE_RE.match(text):
                yield self.finding(
                    file=rel,
                    line=line_no,
                    message=(
                        'Heading "## What\'s True" is retired — write '
                        f'"## What Happens" ({_SOURCE})'
                    ),
                )
