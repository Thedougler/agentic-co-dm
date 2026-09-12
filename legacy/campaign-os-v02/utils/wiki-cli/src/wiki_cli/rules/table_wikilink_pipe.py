"""W56 — a `[[Page|Alias]]` wikilink's alias pipe is also the markdown
table column delimiter. Left unescaped inside a table cell, it splits the
row into an extra column and tears the link into a dangling `[[Page`
fragment and a bare `Alias]]` fragment. Ported from
`utils/scripts/lint-rules/w56-table-wikilink-pipe.mjs`.

No path scoping: a pure syntax defect, not a content-semantic one.
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
_TABLE_ROW_RE = re.compile(r"^\s*\|")
_WIKILINK_RE = re.compile(r"\[\[[^\]]*\]\]")


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


_UNESCAPED_PIPE_RE = re.compile(r"(?<!\\)\|")


def _escape_alias_pipes(text: str) -> str:
    """Every unescaped alias pipe inside a wikilink on a table row, escaped.

    Rewrites only the characters between `[[` and `]]`, so a real cell
    boundary keeps its meaning and an already-escaped `\\|` is left alone —
    which is also what makes a second pass a no-op.
    """
    lines = text.split("\n")
    fenced = _fenced_flags(lines)
    for index, line in enumerate(lines):
        if fenced[index] or not _TABLE_ROW_RE.match(line):
            continue
        lines[index] = _WIKILINK_RE.sub(
            lambda match: f"[[{_UNESCAPED_PIPE_RE.sub(r'\\|', match.group(0)[2:-2])}]]",
            line,
        )
    return "\n".join(lines)


@register
class TableWikilinkPipe(FileRule):
    id = "W56"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = 'Escape the alias pipe as "\\|", e.g. change [[Page|Alias]] to [[Page\\|Alias]].'
    producer = "wiki"
    pure = True
    fixable = True
    autofix = Autofix(scope="syntax", apply=_escape_alias_pipes)

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        body = list(page.body_lines())
        texts = [text for _line, text in body]
        fenced = _fenced_flags(texts)

        for idx, (file_line, text) in enumerate(body):
            if fenced[idx]:
                continue
            if not _TABLE_ROW_RE.match(text):
                continue

            for link_match in _WIKILINK_RE.finditer(text):
                link = link_match.group(0)
                start = link_match.start()
                for j in range(2, len(link) - 2):
                    if link[j] != "|":
                        continue
                    if link[j - 1] == "\\":
                        continue
                    column = start + j + 1
                    yield self.finding(
                        file=page.rel_path,
                        line=file_line,
                        message=(
                            "Unescaped `|` inside a wikilink alias breaks this table's column "
                            'count — escape as `\\|` ([[Page\\|Alias]])'
                        ),
                        column=column,
                    )
