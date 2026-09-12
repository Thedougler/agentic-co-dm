"""W104 — a callout opener indented under, or doubly-quoted inside, another
block renders as an unstyled quote inside a box in Obsidian: the parser
treats the extra `>`/indent as a nested blockquote, not a second callout,
so the `[!type]` marker prints as literal text instead of getting its own
colored border. Ported from
`utils/scripts/lint-rules/w104-nested-callout.mjs`.

Never nest callouts. Not fixable — hoisting to column 0 vs. dropping the
marker is an authoring call this rule can't make. Skips fenced code
blocks: an example snippet quoting this exact syntax is documentation, not
a live defect.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_FENCE_MARK_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")
_NESTED_INDENT_RE = re.compile(r"^\s+> *\[!")
_NESTED_DOUBLE_QUOTE_RE = re.compile(r"^> *> *\[!")


def _fenced_flags(lines: list[str]) -> list[bool]:
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


@register
class NestedCallout(FileRule):
    id = "W104"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Hoist the nested callout opener to column 0 as its own top-level block."
    producer = "wiki"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        body = list(page.body_lines())
        texts = [text for _line, text in body]
        fenced = _fenced_flags(texts)

        for idx, (file_line, text) in enumerate(body):
            if fenced[idx]:
                continue
            if not _NESTED_INDENT_RE.match(text) and not _NESTED_DOUBLE_QUOTE_RE.match(text):
                continue
            yield self.finding(
                file=page.rel_path,
                line=file_line,
                message=(
                    "Obsidian renders a nested callout as an unstyled quote inside a box — "
                    "hoist it to column 0 as its own block, or drop the [!type] marker and "
                    "leave the text as an indented paragraph"
                ),
            )
