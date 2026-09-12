"""W22 — a callout type must be lowercase as written (`> [!dm]`, never
`> [!DM]`). Ported from `utils/scripts/lint-rules/w22-callout-lowercase.mjs`.

Taxonomy-by-path (does this type belong on this page family) is W23's job;
this rule owns case only. Fenced code blocks are skipped — an example
snippet demonstrating callout syntax with the wrong case is documentation,
not a live defect (same rationale W104 states for nested callouts).
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import (
    Autofix,
    Corpus,
    FileRule,
    Finding,
    Page,
    Severity,
    Tier,
    register,
)

_FENCE_MARK_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")
_CALLOUT_OPENER_RE = re.compile(r"^>\s*\[![A-Za-z][A-Za-z0-9-]*\]")
_TYPE_TOKEN_RE = re.compile(r"\[!([A-Za-z][A-Za-z0-9-]*)\]")


def _fenced_flags(lines: list[str]) -> list[bool]:
    """Same-length flags: True where a line is inside (or delimits) a
    fenced code block. CommonMark-correct: a fence opened with N backticks
    (or tildes) closes only on a line with the SAME character, run of at
    least N, and nothing else — mirrors `lib/fences.mjs`'s `fencedLineFlags`."""
    flags = [False] * len(lines)
    open_char: str | None = None
    open_len = 0
    for i, line in enumerate(lines):
        if open_char is None:
            match = _FENCE_MARK_RE.match(line)
            if match:
                open_char = match.group(1)[0]
                open_len = len(match.group(1))
                flags[i] = True
            continue
        flags[i] = True
        close = _CLOSING_ONLY_RE.match(line)
        if close and close.group(1)[0] == open_char and len(close.group(1)) >= open_len:
            open_char = None
            open_len = 0
    return flags


def _lowercase_callout_types(text: str) -> str:
    """Every callout opener's type token, lowercased in place.

    Only the token inside `[!...]` on an opener line changes, so the line's
    title, the callout's body, and every fenced example are untouched.
    """
    lines = text.split("\n")
    fenced = _fenced_flags(lines)
    for index, line in enumerate(lines):
        if fenced[index] or not _CALLOUT_OPENER_RE.match(line):
            continue
        match = _TYPE_TOKEN_RE.search(line)
        if match is None or match.group(1) == match.group(1).lower():
            continue
        lines[index] = line[: match.start(1)] + match.group(1).lower() + line[match.end(1) :]
    return "\n".join(lines)


@register
class CalloutLowercase(FileRule):
    id = "W22"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = 'Lowercase the callout type token, e.g. change "[!DM]" to "[!dm]".'
    producer = "wiki"
    pure = True
    fixable = True
    autofix = Autofix(scope="syntax", apply=_lowercase_callout_types)

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        body = list(page.body_lines())
        texts = [text for _line, text in body]
        fenced = _fenced_flags(texts)

        for idx, (file_line, text) in enumerate(body):
            if fenced[idx]:
                continue
            if not _CALLOUT_OPENER_RE.match(text):
                continue
            match = _TYPE_TOKEN_RE.search(text)
            if match is None:
                continue
            token = match.group(1)
            if token == token.lower():
                continue
            yield self.finding(
                file=page.rel_path,
                line=file_line,
                message=f'Callout type "[!{token}]" must be lowercase: "[!{token.lower()}]"',
                column=match.start() + 1,
            )
