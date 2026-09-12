"""W144 — depiction camera: no player state on non-session narration.

Entity and Situation portraits (ADR-0056) name the thing, never the party.
Moment files and ``mode: recap`` may address the table.

`.claude/skills/narration/references/depiction.md` owns the contract.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_YOU_RE = re.compile(r"\b(you|your)\b", re.IGNORECASE)
_PACING_RE = re.compile(
    r"What do you do\?|How do you (?:get past it|stay ahead of it)\?",
    re.IGNORECASE,
)
_SOURCE = ".claude/skills/narration/references/depiction.md"


def _session_local(page: Page) -> bool:
    mode = page.frontmatter.get("mode")
    if isinstance(mode, str) and mode.strip() == "recap":
        return True
    parent = page.frontmatter.get("parent")
    return isinstance(parent, str) and (
        "moment-" in parent or "sequence-" in parent or "beat-" in parent
    )


@register
class NarrationCameraRule(FileRule):
    """W144 — depiction narration does not use you/your or a pacing prompt."""

    id = "W144"
    version = "2"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.ERROR
    fix = (
        "Rewrite as a subject-focused picture of the thing. Drop you/your "
        f"and any pacing prompt ({_SOURCE})."
    )
    producer = "wiki"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        if page.type != "narration":
            return
        if _session_local(page):
            return

        for file_line, text in page.body_lines():
            if _YOU_RE.search(text) or _PACING_RE.search(text):
                yield self.finding(
                    file=page.rel_path,
                    line=file_line,
                    message=(
                        "depiction narration names the party (you/your or a "
                        "pacing prompt) — keep the thing as the subject "
                        f"({_SOURCE})"
                    ),
                )
