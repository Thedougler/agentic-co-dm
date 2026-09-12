"""Shared `vault/_templates/` reader — W5's required-heading spine and
W55's governed-frontmatter spine, ported from `utils/scripts/lint-rules/
lib/templates.mjs` (`loadTemplateSchema`/`resolveEntry`/`scanH2Headings`
for the former, `loadDefaultSpine` for the latter).

Template resolution is `wiki_cli.query.schema.resolve_template`, shared with
W84: a filename-stem match first (`templates_root/**/_<type>*.md`, exact
`_<type>_<subtype>` stem preferred over the bare `_<type>` stem), falling
back to the template's own declared `type:`/`subtype:` frontmatter for the
files whose stem doesn't carry it (`_session_history.md` declares
`type: session-log`).

Every function here takes `templates_root` explicitly rather than reading
`wiki_cli.config` itself — callers (a rule's `check()`) pass
`load_config().templates_root` in production and a fixture directory in
tests, so this module stays a pure reader with no config dependency of its
own.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from wiki_cli.markdown import split_frontmatter
from wiki_cli.query.schema import resolve_template as schema_resolve_template

_H2_RE = re.compile(r"^## (.+)$")
_KEY_RE = re.compile(r"^([A-Za-z_]+):")
_OPTIONAL_FIRST_LINE_RE = re.compile(r"^OPTIONAL\b", re.IGNORECASE)
_FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
_CLOSING_FENCE_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")


def _fenced_line_flags(lines: list[str]) -> list[bool]:
    """Same CommonMark-correct fence tracker duplicated across this port
    (`dead_weight.py`, `template_boilerplate_leak.py`) — a `## `-looking
    line inside a fenced code block must never read as a real heading."""
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


def _required_h2_headings(body: str) -> list[str]:
    """A template's H2 headings, in file order, excluding any whose first
    non-blank body line starts with `OPTIONAL` (case-insensitive) — the
    same convention `vault/_templates/CLAUDE.md` documents and
    `scanH2Headings` in the legacy module implements."""
    lines = body.splitlines()
    fenced = _fenced_line_flags(lines)
    headings: list[str] = []
    for index, line in enumerate(lines):
        if fenced[index]:
            continue
        match = _H2_RE.match(line)
        if not match:
            continue
        cursor = index + 1
        while cursor < len(lines) and lines[cursor].strip() == "":
            cursor += 1
        optional = cursor < len(lines) and bool(
            _OPTIONAL_FIRST_LINE_RE.match(lines[cursor].strip())
        )
        if not optional:
            headings.append(match.group(1).strip())
    return headings


def _display_path(templates_root: Path, template_path: Path) -> str:
    """A repo-root-relative-looking path for messages, e.g.
    `vault/_templates/_srd/_monster.md` — best-effort, never load-bearing
    for detection (parity compares `(rule, path, line)`, never message text)."""
    try:
        return str(template_path.relative_to(templates_root.parent.parent))
    except ValueError:
        try:
            return str(template_path.relative_to(templates_root.parent))
        except ValueError:
            return str(template_path)


def _all_templates(templates_root: Path) -> list[Path]:
    return sorted(templates_root.rglob("_*.md")) if templates_root.is_dir() else []


def _resolve_template_file(
    templates_root: Path, type_name: str, subtype: str | None
) -> Path | None:
    """Exact `_<type>_<subtype>` stem preferred, else the bare `_<type>`
    stem, else the template declaring that `type:` in its own frontmatter."""
    return schema_resolve_template(
        templates_root, type_name, subtype, _all_templates(templates_root)
    )


@dataclass(frozen=True, slots=True)
class ResolvedTemplate:
    """One `_<type>[_<subtype>].md` template's required H2 spine (W5)."""

    template_path: str
    required_headings: tuple[str, ...]


def resolve_template(
    templates_root: Path, type_name: str, subtype: str | None
) -> ResolvedTemplate | None:
    """The template governing `type_name`/`subtype`, or `None` when no
    template resolves — an unmapped type never gets a required-heading
    check (matches legacy: W5 stays silent, W84 already owns "no such
    type")."""
    path = _resolve_template_file(templates_root, type_name, subtype)
    if path is None:
        return None
    raw = path.read_text(encoding="utf-8")
    _fm_text, body, _body_start = split_frontmatter(raw)
    return ResolvedTemplate(
        template_path=_display_path(templates_root, path),
        required_headings=tuple(_required_h2_headings(body)),
    )


@dataclass(frozen=True, slots=True)
class DefaultSpine:
    """`_refs/_ref.md`'s governed frontmatter key spine, in file order
    (W55) — the authority every per-type template's own spine is checked
    against."""

    template_path: str
    spine_keys: tuple[str, ...]


def default_spine(templates_root: Path) -> DefaultSpine | None:
    """`vault/_templates/_refs/_ref.md` — `None` when the file is missing."""
    path = templates_root / "_refs" / "_ref.md"
    if not path.is_file():
        return None
    raw = path.read_text(encoding="utf-8")
    fm_text, _body, _body_start = split_frontmatter(raw)
    if not fm_text:
        return None
    spine_keys = [match.group(1) for line in fm_text.splitlines() if (match := _KEY_RE.match(line))]
    return DefaultSpine(
        template_path=_display_path(templates_root, path),
        spine_keys=tuple(spine_keys),
    )
