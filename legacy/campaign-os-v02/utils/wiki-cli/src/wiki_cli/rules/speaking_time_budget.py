"""W145 — speaking-time band on player-facing spoken prose (ADR-0028 amend).

140 wpm. Warning, not error. Floor and ceiling.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import FileRule, Finding, Page, Severity, Tier, register

_SOURCE = ".claude/skills/narration/references/checklist.md"
_WORD_RE = re.compile(r"[A-Za-z0-9']+")
_CALLOUT_RE = re.compile(r"^>\s*(?:\[![\w-]+\]\s*)?")
_WIKILINK_RE = re.compile(
    r"(?:!)?\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|([^\]]+))?\]\]"
)
_RECAP_HEADING_RE = re.compile(r"^## Recap\s*$", re.MULTILINE)
_NEXT_H2_RE = re.compile(r"^## ", re.MULTILINE)

# (lo, hi) inclusive word band. Ceilings sit high: specificity wins
# over brevity (DM ruling 2026-08-15) — the floor catches thin prose,
# the ceiling only catches runaway padding.
_ESTABLISH = (90, 320)
_CONTINUE = (60, 240)
_LAST_TIME = (240, 700)
_DIALOGUE = (1, 100)
_RECAP = (900, 1600)


def _spoken_wikilink(match: re.Match[str]) -> str:
    display = match.group(2)
    if display:
        return display
    slug = match.group(1).rsplit("/", 1)[-1]
    return slug.replace("-", " ")


def _words(text: str) -> int:
    stripped = "\n".join(
        _CALLOUT_RE.sub("", line).replace("*", "").replace("_", "")
        for line in text.splitlines()
        if line.strip() and not line.strip().startswith("```")
    )
    spoken = _WIKILINK_RE.sub(_spoken_wikilink, stripped)
    return len(_WORD_RE.findall(spoken))


def _recap_section(body: str) -> str | None:
    match = _RECAP_HEADING_RE.search(body)
    if not match:
        return None
    rest = body[match.end() :]
    nxt = _NEXT_H2_RE.search(rest)
    return rest[: nxt.start()] if nxt else rest


def _band(page: Page) -> tuple[int, int] | None:
    if page.rel_path.startswith("vault/_templates/"):
        return None
    if page.type == "narration":
        mode = page.frontmatter.get("mode")
        if mode == "recap":
            return _LAST_TIME
        if mode in ("continue", "transition"):
            return _CONTINUE
        return _ESTABLISH
    if page.type == "dialogue":
        return _DIALOGUE
    if page.type == "session" and page.frontmatter.get("subtype") == "recap":
        return _RECAP
    return None


@register
class SpeakingTimeBudgetRule(FileRule):
    """W145 — player-facing spoken prose sits in its speaking-time band."""

    id = "W145"
    version = "1"
    tier = Tier.PROSE
    severity = Severity.WARNING
    fix = (
        "Hook by sentence two, then spend the band: cut padding if over, "
        f"add a concrete image if under ({_SOURCE})."
    )
    producer = "wiki"
    pure = True

    def check(self, page: Page, corpus: object) -> Iterable[Finding]:
        del corpus
        band = _band(page)
        if band is None:
            return
        lo, hi = band
        text = page.body
        if page.type == "session":
            section = _recap_section(page.body)
            if section is None:
                return
            text = section
        count = _words(text)
        if lo <= count <= hi:
            return
        yield self.finding(
            file=page.rel_path,
            line=page.body_start_line,
            message=(
                f"spoken prose is {count} words; band is {lo}–{hi} "
                f"(~140 wpm, {_SOURCE})"
            ),
        )
