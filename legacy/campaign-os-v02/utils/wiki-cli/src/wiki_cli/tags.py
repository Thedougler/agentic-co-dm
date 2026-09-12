"""Shared `docs/tags.md` taxonomy parser, ported from `utils/scripts/
lint-rules/lib/tags.mjs` — the single parse every tag-taxonomy-family rule
(W111, W112, W113) needs.

`docs/tags.md` shape: `## Canonical tags` contains one or more group
subheadings (any heading level between `## Canonical tags` and the next H2
— the live doc mixes `###` and `####`) whose leading word names the group
(Domain, Meta, or Project), each holding `- token` bullets. `## Aliases`
then holds `- alias -> canonical` bullets. Everything past that is prose,
not tag data.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

from wiki_cli.markdown import split_frontmatter

if TYPE_CHECKING:
    from collections.abc import Mapping

    from wiki_cli.config import Config
    from wiki_cli.contracts import Page

GROUP_NAMES: tuple[str, ...] = ("Domain", "Meta", "Project")
VISIBILITY_PREFIX = "visibility/"

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_CANONICAL_BULLET_RE = re.compile(r"^- ([a-z0-9-]+)\s*$")
_ALIAS_BULLET_RE = re.compile(r"^- ([a-z0-9-]+)\s*->\s*([a-z0-9-]+)\s*$")
_BULLET_RE = re.compile(r"^-\s")
_LEADING_WORD_RE = re.compile(r"^([A-Za-z0-9]+)")

_INLINE_TAGS_RE = re.compile(r"^tags:\s*\[(.*)\]\s*$")
_BLOCK_TAGS_KEY_RE = re.compile(r"^tags:\s*$")
_BLOCK_BULLET_RE = re.compile(r"^(\s*-\s*)(['\"]?)(.*?)\2\s*$")


def _leading_word(heading_text: str) -> str:
    match = _LEADING_WORD_RE.match(heading_text)
    return match.group(1) if match else ""


def _slug_suggestion(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower())
    return slug.strip("-")


@dataclass(frozen=True, slots=True)
class TaxonomyIssue:
    """One `docs/tags.md` self-diagnostic parse defect — W112's job to
    surface. `code` is one of C1 (heading wrapped across lines, parses as
    a bogus fourth group), C2 (a token defined twice), C3 (an alias points
    at a non-canonical, non-`visibility/` target), C4 (a bullet under a
    tag section that doesn't parse as `- token` or `- alias -> target`),
    C5 (a `- token`-shaped bullet stray outside the tag sections)."""

    line: int
    code: str
    message: str


def _parse_tags_doc(
    raw: str,
) -> tuple[set[str], dict[str, str], dict[str, set[str]], list[TaxonomyIssue]]:
    canonical: set[str] = set()
    aliases: dict[str, str] = {}
    groups: dict[str, set[str]] = {name: set() for name in GROUP_NAMES}
    issues: list[TaxonomyIssue] = []
    defined_at: dict[str, int] = {}

    in_canonical_section = False
    in_aliases_section = False
    current_group: str | None = None

    for index, line in enumerate(raw.split("\n")):
        line_number = index + 1
        heading = _HEADING_RE.match(line)

        if heading:
            level = len(heading.group(1))
            text = heading.group(2)
            if level == 2:
                in_canonical_section = text == "Canonical tags"
                in_aliases_section = text == "Aliases"
                current_group = None
                continue
            if in_canonical_section:
                word = _leading_word(text)
                if word in GROUP_NAMES:
                    current_group = word
                else:
                    current_group = None
                    issues.append(
                        TaxonomyIssue(
                            line=line_number,
                            code="C1",
                            message=(
                                f'"{text}" parses as a fourth tag group — the previous '
                                "heading wrapped across source lines; join it back into "
                                'one "### <Group> (…)" heading line'
                            ),
                        )
                    )
            continue

        if not _BULLET_RE.match(line):
            continue

        # A bullet under "## Canonical tags" with no group heading above it
        # is still canonical (a minimal taxonomy may not use groups at
        # all); it just belongs to no group.
        if in_canonical_section:
            section: str | None = current_group if current_group is not None else "Canonical"
        elif in_aliases_section:
            section = "Aliases"
        else:
            section = None

        if section is None:
            stray = _CANONICAL_BULLET_RE.match(line)
            if stray:
                issues.append(
                    TaxonomyIssue(
                        line=line_number,
                        code="C5",
                        message=(
                            f'"- {stray.group(1)}" outside the tag sections matches the '
                            "tag-entry shape — wiki_cli.tags would accept it as a live "
                            "tag; reword or move it"
                        ),
                    )
                )
            continue

        canonical_match = _CANONICAL_BULLET_RE.match(line)
        alias_match = _ALIAS_BULLET_RE.match(line)

        if canonical_match:
            token = canonical_match.group(1)
            if token in defined_at:
                issues.append(
                    TaxonomyIssue(
                        line=line_number,
                        code="C2",
                        message=f'"{token}" is defined twice (line {defined_at[token]}) — '
                        "delete one",
                    )
                )
            else:
                defined_at[token] = line_number
            canonical.add(token)
            if section in GROUP_NAMES:
                groups[section].add(token)
        elif alias_match:
            alias_token, target = alias_match.group(1), alias_match.group(2)
            if alias_token in defined_at:
                issues.append(
                    TaxonomyIssue(
                        line=line_number,
                        code="C2",
                        message=f'"{alias_token}" is defined twice '
                        f"(line {defined_at[alias_token]}) — delete one",
                    )
                )
            else:
                defined_at[alias_token] = line_number
            if alias_token not in aliases:
                aliases[alias_token] = target
            if target not in canonical and not target.startswith(VISIBILITY_PREFIX):
                issues.append(
                    TaxonomyIssue(
                        line=line_number,
                        code="C3",
                        message=(
                            f'alias "{alias_token} -> {target}" points at "{target}" which '
                            "is not a canonical tag — repoint it at a tag under ### "
                            f'Domain/Meta/Project, or add "{target}" as a canonical bullet'
                        ),
                    )
                )
        else:
            text = line[2:].strip()
            suggestion = _slug_suggestion(text)
            issues.append(
                TaxonomyIssue(
                    line=line_number,
                    code="C4",
                    message=(
                        f'"- {text}" does not parse as a tag entry — every page tag using '
                        "it then fails validation; rewrite as lowercase-hyphenated "
                        f'("- {suggestion}") or as an alias line ("- <x> -> <target>")'
                    ),
                )
            )

    return canonical, aliases, groups, issues


@dataclass(frozen=True, slots=True)
class Taxonomy:
    """Parsed `docs/tags.md`: canonical tags (grouped under Domain/Meta/
    Project), the alias -> canonical map, and any self-diagnostic parse
    `issues` (C1-C5, W112's job to surface). A missing taxonomy file
    parses as empty — same shape, no crash."""

    path: Path
    _canonical: frozenset[str]
    _aliases: Mapping[str, str]
    _groups: Mapping[str, frozenset[str]]
    issues: tuple[TaxonomyIssue, ...]

    def groups(self) -> Mapping[str, frozenset[str]]:
        """Group name (Domain/Meta/Project) -> its canonical tag members."""
        return self._groups

    def canonical(self, tag: str) -> str:
        """Resolve `tag` to its canonical form: itself when already
        canonical or unrecognised, its alias target when listed."""
        return self._aliases.get(tag, tag)

    def is_alias(self, tag: str) -> bool:
        """True when `tag` is a listed alias (docs/tags.md § Aliases),
        never its own canonical form."""
        return tag in self._aliases

    @classmethod
    def load(cls, path: Path) -> Taxonomy:
        """Parse `path` (docs/tags.md's location) into a `Taxonomy`."""
        try:
            raw = path.read_text(encoding="utf-8")
        except OSError:
            return cls(
                path=path,
                _canonical=frozenset(),
                _aliases={},
                _groups={name: frozenset() for name in GROUP_NAMES},
                issues=(),
            )
        canonical, aliases, groups, issues = _parse_tags_doc(raw)
        return cls(
            path=path,
            _canonical=frozenset(canonical),
            _aliases=dict(aliases),
            _groups={name: frozenset(tags) for name, tags in groups.items()},
            issues=tuple(issues),
        )


@dataclass(frozen=True, slots=True)
class PageTag:
    """One `tags:` frontmatter value with its absolute file position —
    both authored shapes (inline array, block list) resolve to this same
    shape. Ported from `lib/pageTags.mjs`."""

    value: str
    line: int
    column: int


def _parse_inline_segment(line: str, abs_line: int) -> list[PageTag]:
    open_idx = line.find("[")
    close_idx = line.rfind("]")
    if open_idx == -1 or close_idx == -1 or close_idx < open_idx:
        return []
    inner = line[open_idx + 1 : close_idx]
    results: list[PageTag] = []
    cursor = 0
    for raw in inner.split(","):
        segment_start = cursor
        cursor += len(raw) + 1  # account for the stripped comma
        trimmed = raw.strip()
        if not trimmed:
            continue
        quote = trimmed[0] if trimmed[0] in ("'", '"') else None
        value = trimmed[1:-1] if quote else trimmed
        lead_ws = len(raw) - len(raw.lstrip())
        quote_offset = 1 if quote else 0
        value_offset_in_inner = segment_start + lead_ws + quote_offset
        column = open_idx + 1 + value_offset_in_inner + 1
        results.append(PageTag(value=value, line=abs_line, column=column))
    return results


def page_tags(page: Page) -> list[PageTag]:
    """A page's `tags:` frontmatter values with absolute file line/column
    positions — both authored shapes: inline array (`tags: [a, b]`,
    quoted or bare) and block list (`tags:` then `- a` lines). Ported from
    `lib/pageTags.mjs`.

    Re-derives frontmatter text from `page.raw` (rather than reading
    `page.frontmatter`, the parsed mapping) because only the raw text
    carries per-value line/column positions — `Page.frontmatter_lines`
    tracks only the top-level key's line.
    """
    fm_text, _body, _body_start_line = split_frontmatter(page.raw)
    if not fm_text:
        return []
    lines = fm_text.split("\n")
    results: list[PageTag] = []

    for i, line in enumerate(lines):
        abs_line = i + 2  # frontmatterRaw's own line 0 is always file line 2
        inline_match = _INLINE_TAGS_RE.match(line)
        if inline_match:
            results.extend(_parse_inline_segment(line, abs_line))
            continue
        if not _BLOCK_TAGS_KEY_RE.match(line):
            continue
        for j in range(i + 1, len(lines)):
            bullet_match = _BLOCK_BULLET_RE.match(lines[j])
            if not bullet_match:
                break
            prefix, quote, value = (
                bullet_match.group(1),
                bullet_match.group(2),
                bullet_match.group(3),
            )
            results.append(PageTag(value=value, line=j + 2, column=len(prefix) + len(quote) + 1))
        break

    return results


def default_taxonomy_path(config: Config) -> Path:
    """The real `docs/tags.md`'s location.

    `config.repo_root` is wiki-cli's OWN root (wherever `wiki.toml` lives),
    not the outer git repo — so it is not usable directly. `config.
    vault_root` is already resolved relative to the real repo root (per
    `wiki.toml`'s `vault.root`), and `docs/` is a sibling of `vault/`
    there, so `vault_root.parent` is the real repo root to derive from.
    """
    return config.vault_root.parent / "docs" / "tags.md"
