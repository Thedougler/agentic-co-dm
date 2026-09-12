"""W102 — a GFM table whose header row has more columns than
`TABLE_MAX_COLUMNS` scrolls horizontally in Obsidian's reading pane, so the
DM loses the row he's mid-scan on. Ported from
`utils/scripts/lint-rules/w102-table-too-wide.mjs`.

Skips `type: class`/`type: subclass` pages — those vendor SRD progression
tables (spell slots, class features) whose column count is fixed by the
source material, not this vault's authoring choices. Table-row/cell
parsing follows W56's precedent: raw-line scan, frontmatter and fenced
code blocks skipped, an escaped `\\|` never counted as a delimiter.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_FENCE_MARK_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")
_TABLE_ROW_RE = re.compile(r"^\s*\|")
_DELIMITER_ROW_RE = re.compile(r"^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)*\|?\s*$")
_EXEMPT_TYPES = frozenset({"class", "subclass"})


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


def split_table_row(line: str) -> list[str]:
    """A raw table-row line's cell texts, honoring `\\|` as a literal pipe
    rather than a column delimiter. Ported 1:1 from the `.mjs` original."""
    text = line.strip()
    text = text.removeprefix("|")
    if text.endswith("|") and (len(text) < 2 or text[-2] != "\\"):
        text = text[:-1]
    cells: list[str] = []
    current = ""
    for i, char in enumerate(text):
        if char == "|" and (i == 0 or text[i - 1] != "\\"):
            cells.append(current)
            current = ""
        else:
            current += char
    cells.append(current)
    return cells


@register
class TableTooWide(FileRule):
    id = "W102"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Split the table into two, or transpose it, so its column count fits the cap."
    producer = "wiki"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if page.type in _EXEMPT_TYPES:
            return

        table_max_columns = int(load_config().threshold("TABLE_MAX_COLUMNS"))

        body = list(page.body_lines())
        texts = [text for _line, text in body]
        fenced = _fenced_flags(texts)

        for idx, (file_line, text) in enumerate(body):
            if fenced[idx]:
                continue
            if not _TABLE_ROW_RE.match(text):
                continue

            next_text = texts[idx + 1] if idx + 1 < len(texts) else ""
            if not _DELIMITER_ROW_RE.match(next_text) or not _TABLE_ROW_RE.match(next_text):
                continue

            column_count = len(split_table_row(text))
            if column_count <= table_max_columns:
                continue

            yield self.finding(
                file=page.rel_path,
                line=file_line,
                message=(
                    f"{column_count}-column table scrolls horizontally in Obsidian's reading "
                    f"pane past {table_max_columns} — split it into two tables or transpose "
                    "it so the DM keeps the row he is reading mid-scan"
                ),
            )
