"""A page's H2 headings against its `type:`'s required spine, ported from
`utils/scripts/lint-rules/w5-required-headings.mjs` (rule id `W5`).

A required heading may carry a `<Placeholder>` segment (angle brackets)
that a concrete page fills with its own name — `_srd/_class.md`'s
"## Core <Class> Traits" matches a real page's "## Core Wizard Traits" or
"## Core Fighter Traits" alike. Everything outside `<...>` matches
literally; `<...>` itself matches one or more characters.

The legacy rule's autofix machinery (reordering a single misplaced H2
section, `isFenceBalanced`/`findHeadingBlocks`) is not ported — this repo's
`contracts.py` has no fix-application mechanism at all yet (`fix` is a
report-legend string, never executed), so there is nothing for that
machinery to drive. Detection (missing / out-of-order) is ported in full.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli import templates
from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_EPISODE_DIR_RE = re.compile(r"^vault/episodes/(\d+)/")

_EXEMPT_PREFIXES: tuple[str, ...] = (
    "vault/_templates/",
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
    "vault/campaigns/shattered-sea/pcs/va-scripts/",
)
_EXEMPT_EXACT: frozenset[str] = frozenset({"vault/campaigns/shattered-sea/dm-voice-script.md"})

_H2_RE = re.compile(r"^## (.+)$")
_H1_RE = re.compile(r"^# (.+)$", re.MULTILINE)

# A cold open is one Hook beat whose page shape is owned by the
# writing-cold-opens skill (references/cold-open-page.md § Page skeleton),
# not by the beat template. Detected by beat_type: hook + an H1 that opens
# with "Cold Open".
_COLD_OPEN_HEADINGS: tuple[str, ...] = (
    "Purpose",
    "POV Brief",
    "Opening Frame",
    "1. <step>",
    "2. <step>",
    "3. <step>",
    "4. <step>",
    "5. <step>",
    "Final Image",
    "Carry Forward",
)
_COLD_OPEN_SPEC = ".claude/skills/writing-cold-opens/references/cold-open-page.md"
_FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
_CLOSING_FENCE_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")
_PLACEHOLDER_SPLIT_RE = re.compile(r"(<[^>]+>)")
_ESCAPE_CHARS_RE = re.compile(r"([.*+?^${}()|\[\]\\])")


def _fenced_line_flags(lines: list[str]) -> list[bool]:
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
        closing = _CLOSING_FENCE_ONLY_RE.match(line)
        if (
            closing
            and closing.group(1)[0] == open_fence[0]
            and len(closing.group(1)) >= open_fence[1]
        ):
            open_fence = None
    return flags


def _scan_h2_texts(body: str) -> list[str]:
    lines = body.splitlines()
    fenced = _fenced_line_flags(lines)
    return [
        match.group(1).strip()
        for index, line in enumerate(lines)
        if not fenced[index] and (match := _H2_RE.match(line))
    ]


def _heading_pattern(required: str) -> re.Pattern[str]:
    parts = _PLACEHOLDER_SPLIT_RE.split(required)
    escaped = "".join(
        ".+" if part.startswith("<") and part.endswith(">") else _ESCAPE_CHARS_RE.sub(r"\\\1", part)
        for part in parts
    )
    return re.compile(f"^{escaped}$")


def _find_match(required: str, actual: list[str]) -> str | None:
    pattern = _heading_pattern(required)
    for text in actual:
        if pattern.match(text):
            return text
    return None


def _index_from(items: list[str], value: str, start: int) -> int:
    """`items.index(value, start)`, JS `Array.prototype.indexOf`-style:
    -1 when not found in `items[start:]`, never a `ValueError` — the out-
    of-order check below relies on that -1 sentinel exactly like the
    legacy rule's own `actual.indexOf(text, cursor + 1)`."""
    for index in range(start, len(items)):
        if items[index] == value:
            return index
    return -1


@register
class RequiredHeadingsRule(FileRule):
    """Ported from npm's W5 (`utils/scripts/lint-rules/w5-required-headings.mjs`)."""

    id = "W5"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Add the missing ## heading(s) in the template's order, or move a "
        "misplaced section to match it — see the page's type template under "
        "vault/_templates/."
    )
    producer = "wiki"
    pure = False
    """Depends on the template catalog under vault/_templates/, not just
    this file's own bytes."""
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md") or not rel.startswith("vault/"):
            return
        if any(rel.startswith(prefix) for prefix in _EXEMPT_PREFIXES) or rel in _EXEMPT_EXACT:
            return

        episode = _EPISODE_DIR_RE.match(rel)
        if episode:
            min_session = int(load_config().threshold("RUN_GUIDE_SHAPE_MIN_SESSION"))
            if int(episode.group(1)) < min_session:
                return

        page_type = page.type
        if page_type is None:
            return  # W84's own job

        subtype_value = page.frontmatter.get("subtype")
        subtype = subtype_value if isinstance(subtype_value, str) else None
        if page_type == "beat" and subtype is None:
            beat_type_value = page.frontmatter.get("beat_type")
            subtype = beat_type_value if isinstance(beat_type_value, str) else None

        required: tuple[str, ...] | list[str]
        template_path: str
        h1 = _H1_RE.search(page.body)
        if page_type == "beat" and subtype == "hook" and h1 and h1.group(1).startswith("Cold Open"):
            required = _COLD_OPEN_HEADINGS
            template_path = _COLD_OPEN_SPEC
        else:
            entry = templates.resolve_template(load_config().templates_root, page_type, subtype)
            if entry is None or not entry.required_headings:
                return
            required = entry.required_headings
            template_path = entry.template_path

        actual = _scan_h2_texts(page.body)

        missing = [h for h in required if _find_match(h, actual) is None]
        for heading in missing:
            yield self.finding(
                file=rel,
                line=page.body_start_line,
                message=(
                    f'Missing required heading "## {heading}" for type "{page_type}" '
                    f"(see {template_path})"
                ),
            )
        if missing:
            return  # order check needs everything present first

        resolved = [_find_match(h, actual) for h in required]
        expected_order = " -> ".join(required)
        cursor = -1
        for text in resolved:
            assert text is not None  # guaranteed by the missing-check above
            idx = _index_from(actual, text, cursor + 1)
            if idx <= cursor:
                yield self.finding(
                    file=rel,
                    line=page.body_start_line,
                    message=(
                        f'Heading "## {text}" is out of order for type "{page_type}" — '
                        f"expected order: {expected_order}"
                    ),
                )
                break
            cursor = idx
