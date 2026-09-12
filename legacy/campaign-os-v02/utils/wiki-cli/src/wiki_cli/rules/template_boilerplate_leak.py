"""A `vault/**` page's body reproduces a line of its own type template
verbatim, ported from `utils/scripts/lint-rules/w90-template-boilerplate-leak.mjs`
(rule id `W90`, see `parity.py`).

`vault/_templates/CLAUDE.md`'s "Templates own layout only" makes a
template's plain-prose section spec (an OPTIONAL condition, a structural
note) instructional scaffolding, not a fact about any one page — a page
that still carries that sentence unedited never replaced it with real
content. Short structural recurrence (a heading, a table row, a callout
marker, a shared line under `MIN_LEAK_WORDS` words) is expected and
excluded; only a longer sentence lifted unchanged counts as a leak.
`class`/`subclass`/`spell`/`monster` pages quote SRD mechanical text
against their own template's worked example by design, so they're exempt
by default (`TEMPLATE_LEAK_EXEMPT_TYPES`).

Template resolution mirrors `FrontmatterSchemaRule`'s (`_templates_root/
_<type>*.md`, exact `_<type>_<subtype>` preferred over the bare
`_<type>`) — duplicated here rather than imported, since that logic lives
as private methods on the other rule's class and this port must not modify
that file.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.markdown import split_frontmatter

_MIN_LEAK_WORDS = 8

# Copied by design, not an unedited leak — mirrors the legacy rule's
# KNOWN_BOILERPLATE exemption (itself mirroring lint-duplication.mjs's
# KNOWN_BOILERPLATE pattern).
_KNOWN_BOILERPLATE: tuple[str, ...] = (
    "How to read this page: [[reading-conventions|Reading These Pages]]",
    "Draft fiction, not canon. Canon lives on the wiki. Derived pages:",
)

_HEADING_RE = re.compile(r"^#{1,6}\s")
_WHITESPACE_RE = re.compile(r"\s+")
_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
_CLOSING_FENCE_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")


def _fenced_line_flags(lines: list[str]) -> list[bool]:
    """Same CommonMark-correct semantics as the legacy `fences.mjs` tracker:
    a fence opened with N backticks/tildes closes only on a line using the
    SAME character, with a run of at least N, and nothing but whitespace
    after it — a naive open/close toggle gets this wrong for a fence
    wrapping a shorter same-character inner example."""
    flags = [False] * len(lines)
    open_fence: tuple[str, int] | None = None

    for index, line in enumerate(lines):
        if open_fence is None:
            match = _FENCE_RE.match(line)
            if match:
                marker = match.group(1)
                open_fence = (marker[0], len(marker))
                flags[index] = True
            continue

        flags[index] = True
        close = _CLOSING_FENCE_ONLY_RE.match(line)
        if close and close.group(1)[0] == open_fence[0] and len(close.group(1)) >= open_fence[1]:
            open_fence = None

    return flags


def _is_structural_line(line: str) -> bool:
    """Heading, table row, or callout marker — never a candidate leak line
    on either side of the comparison."""
    trimmed = line.strip()
    return trimmed == "" or bool(_HEADING_RE.match(trimmed)) or trimmed.startswith(("|", ">"))


def _word_count(line: str) -> int:
    trimmed = line.strip()
    return 0 if trimmed == "" else len(trimmed.split())


def _normalize(line: str) -> str:
    return _WHITESPACE_RE.sub(" ", line.strip())


def _collect_template_lines(template_raw: str) -> frozenset[str]:
    """Qualifying template body lines (>= MIN_LEAK_WORDS words, not
    heading/table/callout, frontmatter and fenced blocks excluded), as a
    frozenset of whitespace-normalized text."""
    _fm_text, body, _body_start = split_frontmatter(template_raw)
    lines = body.splitlines()
    fenced = _fenced_line_flags(lines)
    qualifying: set[str] = set()
    for index, line in enumerate(lines):
        if fenced[index]:
            continue
        if _is_structural_line(line):
            continue
        if _word_count(line) < _MIN_LEAK_WORDS:
            continue
        qualifying.add(_normalize(line))
    return frozenset(qualifying)


@register
class TemplateBoilerplateLeakRule(FileRule):
    """Ported from npm's W90 (`utils/scripts/lint-rules/w90-template-boilerplate-leak.mjs`)."""

    id = "W90"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        "Delete the line — it is scaffolding prose from the page's own type "
        "template, not a fact about this page. The instruction belongs in "
        "the owning skill or a vault/refs/ runbook, not the page body."
    )
    producer = "wiki"
    pure = False
    """Depends on the template catalog under vault/_templates/, not just this file's own bytes."""
    version = "1"

    def __init__(self) -> None:
        self._templates_cache: tuple[Path, list[Path]] | None = None
        self._lines_cache: dict[Path, frozenset[str]] = {}

    def _all_templates(self, templates_root: Path) -> list[Path]:
        if self._templates_cache is not None and self._templates_cache[0] == templates_root:
            return self._templates_cache[1]
        found = sorted(templates_root.rglob("_*.md")) if templates_root.is_dir() else []
        self._templates_cache = (templates_root, found)
        return found

    def _resolve_template(
        self, templates_root: Path, page_type: str, subtype: str | None
    ) -> Path | None:
        bare_stem = f"_{page_type}"
        prefix = f"{bare_stem}_"
        candidates = [
            path
            for path in self._all_templates(templates_root)
            if path.stem == bare_stem or path.stem.startswith(prefix)
        ]
        if not candidates:
            return None
        if subtype:
            exact_stem = f"{bare_stem}_{subtype}"
            for path in candidates:
                if path.stem == exact_stem:
                    return path
        for path in candidates:
            if path.stem == bare_stem:
                return path
        return candidates[0] if len(candidates) == 1 else None

    def _template_lines(self, template_path: Path) -> frozenset[str]:
        cached = self._lines_cache.get(template_path)
        if cached is not None:
            return cached
        raw = template_path.read_text(encoding="utf-8")
        result = _collect_template_lines(raw)
        self._lines_cache[template_path] = result
        return result

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        page_type = page.type
        if page_type is None:
            return  # W84 already flags a missing type

        exempt_types = {
            entry.strip()
            for entry in load_config().threshold("TEMPLATE_LEAK_EXEMPT_TYPES").split("|")
            if entry.strip()
        }
        if page_type in exempt_types:
            return

        subtype_value = page.frontmatter.get("subtype")
        subtype = subtype_value if isinstance(subtype_value, str) else None

        templates_root = load_config().templates_root
        template_path = self._resolve_template(templates_root, page_type, subtype)
        if template_path is None:
            return

        template_lines = self._template_lines(template_path)
        if not template_lines:
            return

        body_lines = page.body.splitlines()
        fenced = _fenced_line_flags(body_lines)
        for offset, raw_line in enumerate(body_lines):
            if fenced[offset]:
                continue
            if _is_structural_line(raw_line):
                continue
            if _word_count(raw_line) < _MIN_LEAK_WORDS:
                continue

            normalized = _normalize(raw_line)
            if normalized not in template_lines:
                continue
            if any(signature in raw_line for signature in _KNOWN_BOILERPLATE):
                continue

            yield self.finding(
                file=page.rel_path,
                line=page.body_start_line + offset,
                message=(
                    f"This line is verbatim {template_path} scaffolding prose, not a "
                    "fact about this page — delete it; the instruction belongs in the "
                    "owning skill or a vault/refs/runbooks/ page "
                    "(vault/_templates/CLAUDE.md)"
                ),
            )
