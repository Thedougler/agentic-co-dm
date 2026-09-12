"""Ported from npm's W78 (`utils/scripts/lint-rules/w78-unsourced-session-log.mjs`).

A `## Session Log` heading whose body cites zero real sessions is not a
legitimate section, just placeholder narration in disguise
(`vault/_templates/CLAUDE.md` § Session Log sections: the section is born
only when a real entry lands; an absent section already records "no
appearances yet"). W38 (dead-weight) only catches a literally empty
section — this one has non-blank body text (an HTML comment or a vague "no
evidence" sentence) but zero real session citations.

A real citation is either a raw transcript/prep path
(`vault/campaigns/<season>/episodes/NNN/...`) or a prose form real pages
actually use ("Session 03", "**Session 02**", "Pre-Session-01", "s04:") —
matching only the path form previously flagged pages that DO record play,
and since the rule's own stated fix is to delete the section, that false
positive would destroy canon session history rather than merely nag.

Detection-only by design: the fix (delete the heading + its body down to
the next heading/EOF) is a multi-line deletion outside this rule's scope.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

SCOPED_ROOTS = ("vault",)
# A citation is a transcript/prep path OR the prose forms real pages actually
# use: "Session 03", "**Session 02**", "Pre-Session-01", "s04:".
SESSION_CITATION_RE = re.compile(
    r"\b(?:sessions|episodes)/|\bpre-session[\s-]?\d{1,3}\b|\bsessions?[\s-]?\d{1,3}\b|\bs\d{2}\b",
    re.IGNORECASE,
)
_HEADING_RE = re.compile(r"^(#{1,6})\s+(.+)$")
_FENCE_TOGGLE_RE = re.compile(r"^\s*(```|~~~)")
_FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_FENCE_RE = re.compile(r"^\s*(`+|~+)\s*$")


def _fenced_flags(lines: list[str]) -> list[bool]:
    flags = [False] * len(lines)
    open_fence: tuple[str, int] | None = None
    for i, line in enumerate(lines):
        if open_fence is None:
            match = _FENCE_LINE_RE.match(line)
            if match:
                open_fence = (match.group(1)[0], len(match.group(1)))
                flags[i] = True
            continue
        flags[i] = True
        close = _CLOSING_FENCE_RE.match(line)
        if close and close.group(1)[0] == open_fence[0] and len(close.group(1)) >= open_fence[1]:
            open_fence = None
    return flags


@register
class UnsourcedSessionLogRule(FileRule):
    """Ported from npm's W78 (`w78-unsourced-session-log.mjs`)."""

    id = "W78"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        'Delete the "## Session Log" heading and its body down to the next '
        'heading (or EOF); an absent section already records "no '
        'appearances yet". Never write a placeholder sentence or comment instead.'
    )
    producer = "wiki"
    pure = True
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md"):
            return
        if not any(rel == root or rel.startswith(f"{root}/") for root in SCOPED_ROOTS):
            return

        lines = page.raw.split("\n")
        fenced = _fenced_flags(lines)

        for i, line in enumerate(lines):
            if fenced[i]:
                continue

            heading = _HEADING_RE.match(line)
            if not heading or heading.group(2).strip() != "Session Log":
                continue
            level = len(heading.group(1))

            body_in_fence = False
            cited = False
            j = i + 1
            while j < len(lines):
                body_line = lines[j]
                if _FENCE_TOGGLE_RE.match(body_line):
                    body_in_fence = not body_in_fence
                    j += 1
                    continue
                if body_in_fence:
                    j += 1
                    continue

                sub_heading = _HEADING_RE.match(body_line)
                if sub_heading and len(sub_heading.group(1)) <= level:
                    break

                if SESSION_CITATION_RE.search(body_line):
                    cited = True
                j += 1

            if not cited:
                yield self.finding(
                    file=rel,
                    line=i + 1,
                    message=(
                        '"## Session Log" cites no real session — delete the heading and its '
                        "body down to the next heading (or EOF); an absent section already "
                        'records "no appearances yet" (vault/_templates/CLAUDE.md § Session '
                        "Log sections). Never write a placeholder sentence or comment to say "
                        "there is no evidence."
                    ),
                )
