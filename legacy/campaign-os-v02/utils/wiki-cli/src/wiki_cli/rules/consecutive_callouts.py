"""W101 — two callout blocks of the SAME type in a row, separated only by
blank lines, read as one interrupted block in Obsidian's rendered view (the
fold/border resets between them but the reader's eye treats them as one
continuous box). Ported from
`utils/scripts/lint-rules/w101-consecutive-callouts.mjs`.

Scoped to `vault/` and to `CONSECUTIVE_CALLOUT_TYPES` only — `[!check]`,
`[!read-aloud]`, and `[!dialogue]` are atomic by design (a read-aloud/
dialogue box is one spoken unit, a check box is one resolvable prompt), so
two of either in a row are two distinct beats, not a false split. Not
fixable — merging is a prose-judgment call this rule can't make safely.

Boundary: more than 2 blank lines between the two blocks, or any non-blank
line between them, both mean the blocks were deliberately separated —
silent.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_FENCE_MARK_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")
_CALLOUT_OPENER_RE = re.compile(r"^>\s*\[!([A-Za-z][A-Za-z0-9-]*)\][-+]?\s*(.*)$")
_SCOPED_ROOTS = ("vault/",)
_MAX_GAP_BLANK_LINES = 2


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


def _parse_callouts(
    body: list[tuple[int, str]], fenced: list[bool]
) -> list[tuple[str, int, int]]:
    """[(type, opener_line, end_line)] for every top-level (column 0)
    callout, in document order. `end_line` is the last contiguous
    `>`-prefixed body line the block consumed (== opener_line for a
    one-line opener with no body)."""
    callouts: list[tuple[str, int, int]] = []
    i = 0
    n = len(body)
    while i < n:
        file_line, text = body[i]
        if fenced[i]:
            i += 1
            continue
        match = _CALLOUT_OPENER_RE.match(text)
        if match is None:
            i += 1
            continue
        call_type = match.group(1).lower()
        end_line = file_line
        j = i + 1
        while j < n and not fenced[j]:
            _next_line, next_text = body[j]
            if not next_text.startswith(">") or _CALLOUT_OPENER_RE.match(next_text):
                break
            end_line = body[j][0]
            j += 1
        callouts.append((call_type, file_line, end_line))
        i = j
    return callouts


@register
class ConsecutiveCallouts(FileRule):
    id = "W101"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Merge the two callouts if tight, put prose between them, or retype the second."
    producer = "wiki"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path.replace("\\", "/")
        if not rel.endswith(".md"):
            return
        if not any(rel.startswith(root) for root in _SCOPED_ROOTS):
            return

        config = load_config()
        consecutive_types = {
            item.lower() for item in config.threshold_list("CONSECUTIVE_CALLOUT_TYPES")
        }
        dm_max = config.threshold("DM_MAX_SENTENCES")
        mechanic_max = config.threshold("MECHANIC_MAX_LINES")
        cap_clause = f"{dm_max} sentences / {mechanic_max} lines"

        body = list(page.body_lines())
        fenced = _fenced_flags([text for _line, text in body])
        line_by_num = {file_line: text for file_line, text in body}
        callouts = _parse_callouts(body, fenced)

        for i in range(1, len(callouts)):
            prev_type, _prev_start, prev_end = callouts[i - 1]
            curr_type, curr_start, _curr_end = callouts[i]
            if prev_type != curr_type or curr_type not in consecutive_types:
                continue

            gap_start = prev_end + 1
            gap_end = curr_start - 1
            gap_lines = (
                [line_by_num[num] for num in range(gap_start, gap_end + 1)]
                if gap_end >= gap_start
                else []
            )
            if len(gap_lines) > _MAX_GAP_BLANK_LINES:
                continue
            if not all(line.strip() == "" for line in gap_lines):
                continue

            yield self.finding(
                file=page.rel_path,
                line=curr_start,
                message=(
                    f"two [!{curr_type}] blocks in a row read as one interrupted block in "
                    f"Obsidian — merge them if the combined body stays reasonably tight "
                    f"(roughly {cap_clause}), else put the prose separating their two jobs "
                    "between them, or retype the second"
                ),
            )
