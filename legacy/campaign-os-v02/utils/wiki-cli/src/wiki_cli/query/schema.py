"""Free functions for parsing a page type's governing template's
frontmatter schema — extracted from `rules/frontmatter_schema.py` (W84) so
other read-layer callers (e.g. the query CLI) can reuse the same template
resolution and key parsing without depending on the lint rule class.
"""

from __future__ import annotations

import re
from functools import cache
from pathlib import Path

from wiki_cli.markdown import split_frontmatter

_KEY_RE = re.compile(r"^([A-Za-z_]+):")
_OPTIONAL_RE = re.compile(r"#\s*OPTIONAL", re.IGNORECASE)
_DECLARED_RE = re.compile(r"^(type|subtype):\s*([^#\n]*)")


def template_keys(fm_text: str) -> tuple[frozenset[str], frozenset[str]]:
    """(required, allowed) top-level keys declared by one template's
    frontmatter text. A key is required unless `# OPTIONAL`."""
    required: set[str] = set()
    allowed: set[str] = set()
    for line in fm_text.splitlines():
        match = _KEY_RE.match(line)
        if not match:
            continue
        key = match.group(1)
        allowed.add(key)
        if not _OPTIONAL_RE.search(line):
            required.add(key)
    return frozenset(required), frozenset(allowed)


def all_templates(templates_root: Path) -> list[Path]:
    """Every template file under `templates_root`, or `[]` if it doesn't
    exist as a directory."""
    return sorted(templates_root.rglob("_*.md")) if templates_root.is_dir() else []


def resolve_template(
    templates_root: Path,
    page_type: str,
    subtype: str | None,
    templates: list[Path] | None = None,
) -> Path | None:
    """The template governing `page_type`/`subtype`, or `None` if none
    resolves. `templates` may be passed pre-computed (e.g. memoized by a
    caller); otherwise `all_templates(templates_root)` is called directly."""
    if templates is None:
        templates = all_templates(templates_root)
    # Template stems use underscores where type: values use hyphens
    # (`type: agent-guidance` -> `_agent_guidance.md`).
    bare_stem = f"_{page_type.replace('-', '_')}"
    prefix = f"{bare_stem}_"
    candidates = [
        path for path in templates if path.stem == bare_stem or path.stem.startswith(prefix)
    ]
    if not candidates:
        return _resolve_by_declared_type(templates, page_type, subtype)
    if subtype:
        exact_stem = f"{bare_stem}_{subtype.replace('-', '_')}"
        for path in candidates:
            if path.stem == exact_stem:
                return path
    for path in candidates:
        if path.stem == bare_stem:
            return path
    if len(candidates) == 1:
        return candidates[0]
    return _resolve_by_declared_type(templates, page_type, subtype)


@cache
def _declared(path: Path, _mtime_ns: int) -> tuple[str | None, str | None]:
    """One template's own declared `type:`/`subtype:` values. Keyed on mtime
    so an edited template is re-read."""
    fm_text, _body, _body_start = split_frontmatter(path.read_text(encoding="utf-8"))
    declared: dict[str, str | None] = {"type": None, "subtype": None}
    for line in (fm_text or "").splitlines():
        match = _DECLARED_RE.match(line)
        if match is None:
            continue
        key = match.group(1)
        if declared[key] is None:
            declared[key] = match.group(2).strip().strip("\"'") or None
    return declared["type"], declared["subtype"]


def _resolve_by_declared_type(
    templates: list[Path], page_type: str, subtype: str | None
) -> Path | None:
    """Fallback for templates whose filename stem doesn't encode their type
    (`_session_history.md` declares `type: session-log`). Consulted only
    after stem matching finds nothing, so it never changes an existing
    mapping."""
    matches: list[tuple[Path, str | None]] = []
    for path in templates:
        try:
            declared_type, declared_subtype = _declared(path, path.stat().st_mtime_ns)
        except OSError:
            continue
        if declared_type == page_type:
            matches.append((path, declared_subtype))
    if not matches:
        return None
    if subtype:
        for path, declared_subtype in matches:
            if declared_subtype == subtype:
                return path
    for path, declared_subtype in matches:
        if declared_subtype is None:
            return path
    return matches[0][0] if len(matches) == 1 else None


def legal_filter_keys(templates_root: Path) -> frozenset[str]:
    """The union of every template's allowed frontmatter keys under
    `templates_root` — the set of keys a query filter may legally target."""
    keys: set[str] = set()
    for template_path in all_templates(templates_root):
        raw = template_path.read_text(encoding="utf-8")
        fm_text, _body, _body_start = split_frontmatter(raw)
        _required, allowed = template_keys(fm_text or "")
        keys |= allowed
    return frozenset(keys)
