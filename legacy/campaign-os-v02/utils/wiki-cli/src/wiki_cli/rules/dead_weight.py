"""Ported from npm's W38 (`utils/scripts/lint-rules/w38-dead-weight.mjs`).

Pure context cost with zero content payoff: (1) an empty H2/H3 section — a
heading with no body before the next same-or-higher heading or EOF, where
a table/callout/any non-blank line right after the heading counts as body;
(2) a surviving `<!-- AGENT: ... -->` scaffolding comment on a non-template
page (every template's own AGENT comment says to remove it once done — a
`vault/` page carrying one is unfinished instantiation).

The leftover-AGENT-comment check stays unfixed: the fix is "do what the
comment says" (author real content), not a mechanical deletion.
"""

from __future__ import annotations

import re
from collections.abc import Iterable, Sequence

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SCOPED_PREFIXES = ("vault/", "sys/")
_SCOPED_EXACT = ("vault", "sys")

_HEADING_RE = re.compile(r"^(#{1,3})\s+(.+)$")
_AGENT_COMMENT_RE = re.compile(r"<!--\s*AGENT:")
_CODE_SPAN_RE = re.compile(r"`[^`]*`")

_FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")


def _fenced_line_flags(lines: Sequence[str]) -> list[bool]:
    """Same CommonMark-correct fence tracker as `lib/fences.mjs`'s
    `fencedLineFlags` — see `unsummarized_page.py`'s own copy for the same
    reasoning; duplicated rather than shared since each rule stays a single
    self-contained, `pure` file."""
    flags = [False] * len(lines)
    open_fence: tuple[str, int] | None = None
    for index, line in enumerate(lines):
        if open_fence is None:
            match = _FENCE_LINE_RE.match(line)
            if match:
                marker = match.group(1)
                open_fence = (marker[0], len(marker))
                flags[index] = True
            continue
        flags[index] = True
        closing = _CLOSING_ONLY_RE.match(line)
        if closing and closing.group(1)[0] == open_fence[0] and len(closing.group(1)) >= open_fence[1]:
            open_fence = None
    return flags


def _has_body_content(lines: Sequence[str], fenced: Sequence[bool], start: int, level: int) -> bool:
    for index in range(start, len(lines)):
        if fenced[index]:
            return True  # a fenced block right under the heading is body content
        match = _HEADING_RE.match(lines[index])
        if match and len(match.group(1)) <= level:
            return False  # hit the next same-or-higher heading first
        if lines[index].strip() != "":
            return True
    return False


@register
class DeadWeightRule(FileRule):
    """Ported from npm's W38 (`utils/scripts/lint-rules/w38-dead-weight.mjs`)."""

    id = "W38"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Delete the empty heading (add it back only with real content), or resolve "
        "the leftover AGENT comment and delete it."
    )
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus

        in_scope = page.rel_path in _SCOPED_EXACT or page.rel_path.startswith(_SCOPED_PREFIXES)
        if not in_scope:
            return

        numbered = list(page.body_lines())
        body_lines = [text for _, text in numbered]
        line_numbers = [line for line, _ in numbered]
        fenced = _fenced_line_flags(body_lines)

        for index, line in enumerate(body_lines):
            if fenced[index]:
                continue
            match = _HEADING_RE.match(line)
            if not match or len(match.group(1)) == 1:
                continue  # only H2/H3 — H1 is the page title
            level = len(match.group(1))
            heading = match.group(2).strip()
            if not _has_body_content(body_lines, fenced, index + 1, level):
                yield self.finding(
                    file=page.rel_path,
                    line=line_numbers[index],
                    message=(
                        f'Empty "{match.group(1)} {heading}" — delete the heading; add '
                        "it back only with real, sourced content."
                    ),
                )

        for index, line in enumerate(body_lines):
            stripped = _CODE_SPAN_RE.sub("", line)
            if _AGENT_COMMENT_RE.search(stripped):
                yield self.finding(
                    file=page.rel_path,
                    line=line_numbers[index],
                    message="Leftover AGENT scaffolding comment — do what it says, then delete it.",
                )
