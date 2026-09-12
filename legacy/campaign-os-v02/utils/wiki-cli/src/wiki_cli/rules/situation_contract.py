"""W139 — `type: situation` pages carry Situation-only structure.

A Situation is a durable dramatic condition, not a table-ready beat. Its
frontmatter must name the live lifecycle, pressure, and if-ignored world change
that make it runnable later; its body must not contain a `## Next` handoff or
verbatim read-aloud box, because those belong to table-ready frames derived from
the Situation. Its body must also carry all eight Beat Chart headings
(ADR-0061) — the composition control surface DMs scan during play.

`vault/_templates/_campaigns/_situation.md` owns the page shape.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_NEXT_HEADING_RE = re.compile(r"^##\s+Next\s*$", re.MULTILINE)
_READ_ALOUD_RE = re.compile(r"^>\s*\[!read-aloud\]", re.MULTILINE)
_PRESCRIBED_PLAYER_ACTION_RE = re.compile(
    r"\b(?:the party|the players?|a pc|the pcs?)\s+must\s+\w+", re.IGNORECASE
)
_SOURCE_DOC = "vault/_templates/_campaigns/_situation.md"
_REQUIRED_FIELDS = ("lifecycle", "pressure", "if_ignored")
_BEAT_CHART_HEADINGS = (
    "Dramatic Question",
    "Player Gravity",
    "Current State",
    "Active Beat",
    "Beat Spine",
    "Live Branches",
    "Climax Readiness",
    "Unused Possibilities",
)


def _heading_re(name: str) -> re.Pattern[str]:
    return re.compile(rf"^#{{2,3}}\s+{re.escape(name)}\s*$", re.MULTILINE)


def _has_value(value: object) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return value.strip() != ""
    if isinstance(value, list | tuple | set | dict):
        return len(value) > 0
    return True


@register
class SituationContractRule(FileRule):
    """W139 — situation pages require core fields and reject moment-only content."""

    id = "W139"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Fill lifecycle:, pressure:, and if_ignored: with concrete Situation state; "
        'delete any "## Next" section or inline > [!read-aloud] box; add every '
        "missing Beat Chart heading per vault/_templates/_campaigns/_situation.md "
        "§ Beat Chart."
    )
    producer = "wiki"
    pure = True
    version = "3"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md") or not rel.startswith("vault/"):
            return
        if page.type != "situation":
            return

        for field in _REQUIRED_FIELDS:
            if _has_value(page.frontmatter.get(field)):
                continue
            yield self.finding(
                file=rel,
                line=1,
                message=(
                    f"type: situation page has no {field}: value — every Situation "
                    "must state its lifecycle, live pressure, and observable "
                    f"if-ignored change ({_SOURCE_DOC})"
                ),
            )

        for match in _NEXT_HEADING_RE.finditer(page.raw):
            line_no = page.raw.count("\n", 0, match.start()) + 1
            yield self.finding(
                file=rel,
                line=line_no,
                message=(
                    'type: situation page contains "## Next" — a Situation does not '
                    "land on the next table frame; put the handoff on the derived "
                    f"moment instead ({_SOURCE_DOC})"
                ),
            )

        for match in _READ_ALOUD_RE.finditer(page.raw):
            line_no = page.raw.count("\n", 0, match.start()) + 1
            yield self.finding(
                file=rel,
                line=line_no,
                message=(
                    "type: situation page contains a > [!read-aloud] callout — "
                    "extract to a type: narration sibling and embed it "
                    f"({_SOURCE_DOC})"
                ),
            )

        for match in _PRESCRIBED_PLAYER_ACTION_RE.finditer(page.raw):
            line_no = page.raw.count("\n", 0, match.start()) + 1
            yield self.finding(
                file=rel,
                line=line_no,
                message=(
                    f'Prescribed-player-action phrasing "{match.group(0)}" on a '
                    "type: situation page may be assigning player action; rephrase "
                    f"so the world acts and the party chooses ({_SOURCE_DOC})"
                ),
                severity=Severity.WARNING,
            )

        for heading in _BEAT_CHART_HEADINGS:
            if _heading_re(heading).search(page.raw):
                continue
            yield self.finding(
                file=rel,
                line=1,
                message=(
                    f'type: situation page has no "{heading}" heading — every '
                    "Situation carries all eight Beat Chart headings "
                    f"({_SOURCE_DOC} § Beat Chart, ADR-0061)"
                ),
            )
