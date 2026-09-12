"""The one markdown/frontmatter parser in this package.

Two loaders, split by direction.

READ (`parse_page`, `load_page`): libyaml's C scanner via PyYAML, which only
has to answer what a rule asks — the values, and which line each top-level key
sits on. Over this vault's 2541 frontmatter blocks it costs 0.3s against
ruamel round-trip's 6.2s, and the corpus build parses every page on every
invocation, including a one-file lint. Key lines come from `_key_lines_of_text`
rather than ruamel's `.lc` record; duplicate keys still raise, so a page that
was a parse error before is still one.

WRITE (`dump_frontmatter`, `render_page`): round-trip YAML (`ruamel.yaml`,
typ="rt"). The templates encode closed enums in trailing comments
(`subtype: building|plane|dungeon`), so a load/dump cycle that drops comments
silently destroys the schema source. Every write path goes through
`dump_frontmatter` here and nowhere else, and `render_page` re-reads the
page's own frontmatter text round-trip when handed anything else.
"""

from __future__ import annotations

import io
import re
import threading
from pathlib import Path
from typing import Any

import yaml as _pyyaml
from ruamel.yaml import YAML
from ruamel.yaml.comments import CommentedMap
from ruamel.yaml.error import YAMLError
from yaml.constructor import ConstructorError as _ConstructorError

from wiki_cli.contracts import Page

_FENCE = "---"
_WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


_YAML_LOCAL = threading.local()
"""One `YAML` instance per thread, reused across every page that thread
parses. Constructing one costs more than parsing a page's frontmatter with
it — building a fresh instance per page was ~35% of the corpus build's total
YAML time over this vault (9.4s -> 6.2s for the same 2541 blocks). Per
THREAD, not one global: `ruamel` instances carry mutable parser/scanner
state and the orchestrator runs producers on a thread pool."""


def _yaml() -> YAML:
    cached: YAML | None = getattr(_YAML_LOCAL, "instance", None)
    if cached is not None:
        return cached
    yaml = YAML(typ="rt")
    yaml.preserve_quotes = True
    yaml.width = 4096  # never re-wrap a long summary: line breaks are content
    _YAML_LOCAL.instance = yaml
    return yaml


_BASE_SAFE_LOADER = getattr(_pyyaml, "CSafeLoader", _pyyaml.SafeLoader)
"""libyaml's C scanner when the wheel carries it, PyYAML's pure-Python
SafeLoader otherwise — same accepted grammar either way, only the speed
differs, so a machine without libyaml parses the same pages to the same
values."""


class _StrictSafeLoader(_BASE_SAFE_LOADER):  # type: ignore[valid-type,misc]
    """SafeLoader that rejects a duplicate mapping key.

    PyYAML's own loaders let the last duplicate win silently; ruamel's
    round-trip loader raises. Read-path parsing must keep raising, or a page
    whose frontmatter carries `type:` twice would quietly parse to one of the
    two values instead of being recorded as a parse error."""

    def construct_mapping(self, node: Any, deep: bool = False) -> dict[Any, Any]:
        seen: set[Any] = set()
        for key_node, _value_node in node.value:
            key = self.construct_object(key_node, deep=deep)
            try:
                duplicate = key in seen
            except TypeError:
                continue  # unhashable key — super() raises its own error for it
            if duplicate:
                raise _ConstructorError(
                    "while constructing a mapping",
                    node.start_mark,
                    f"found duplicate key {key!r}",
                    key_node.start_mark,
                )
            seen.add(key)
        return super().construct_mapping(node, deep)


_TOP_LEVEL_KEY_RE = re.compile(r"^([A-Za-z_][\w-]*):(?:\s|$)")
"""A top-level frontmatter key: no leading indent. Nested keys and every
continuation line of a block scalar or a wrapped flow scalar are indented by
YAML's own grammar, so column 0 is the whole of the top level."""


def _key_lines_of_text(fm_text: str, fm_start_line: int) -> dict[str, int]:
    """Top-level key -> 1-indexed file line, read off the frontmatter text.

    Replaces ruamel's `.lc` position record, which is only available from the
    round-trip loader. First occurrence wins, matching `.lc`'s own behaviour on
    a mapping whose duplicate keys did not raise."""
    lines: dict[str, int] = {}
    for offset, line in enumerate(fm_text.split("\n")):
        match = _TOP_LEVEL_KEY_RE.match(line)
        if match and match.group(1) not in lines:
            lines[match.group(1)] = fm_start_line + offset
    return lines


def split_frontmatter(raw: str) -> tuple[str | None, str, int]:
    """(frontmatter text or None, body, 1-indexed file line the body starts on).

    A file with no leading `---` fence has no frontmatter and a body starting at
    line 1. An unterminated fence is treated the same way — the caller decides
    whether that is a finding.
    """
    if not raw.startswith(_FENCE + "\n"):
        return None, raw, 1

    lines = raw.split("\n")
    for index in range(1, len(lines)):
        if lines[index].rstrip() == _FENCE:
            fm_text = "\n".join(lines[1:index])
            body = "\n".join(lines[index + 1 :])
            return fm_text, body, index + 2
    return None, raw, 1


def parse_page(rel_path: str, raw: str) -> Page:
    """Parse one file's text. Never raises on bad frontmatter — records it."""
    fm_text, body, body_start_line = split_frontmatter(raw)
    if fm_text is None:
        return Page(
            rel_path=rel_path,
            raw=raw,
            frontmatter={},
            body=body,
            body_start_line=body_start_line,
        )

    fm_start_line = 2
    try:
        loaded = _pyyaml.load(fm_text, Loader=_StrictSafeLoader) if fm_text.strip() else None
    except (_pyyaml.YAMLError, YAMLError) as error:
        return Page(
            rel_path=rel_path,
            raw=raw,
            frontmatter={},
            body=body,
            body_start_line=body_start_line,
            parse_error=str(error).strip().splitlines()[0] if str(error).strip() else "invalid YAML",
        )

    if loaded is None:
        return Page(
            rel_path=rel_path,
            raw=raw,
            frontmatter={},
            body=body,
            body_start_line=body_start_line,
        )
    if not isinstance(loaded, dict):
        return Page(
            rel_path=rel_path,
            raw=raw,
            frontmatter={},
            body=body,
            body_start_line=body_start_line,
            parse_error="frontmatter is not a mapping",
        )

    return Page(
        rel_path=rel_path,
        raw=raw,
        frontmatter=loaded,
        body=body,
        body_start_line=body_start_line,
        frontmatter_lines=_key_lines_of_text(fm_text, fm_start_line),
    )


def load_page(repo_root: Path, rel_path: str) -> Page:
    """Read and parse one page. Undecodable bytes are recorded, not raised."""
    path = repo_root / rel_path
    try:
        raw = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as error:
        return Page(
            rel_path=rel_path,
            raw="",
            frontmatter={},
            body="",
            body_start_line=1,
            parse_error=f"not valid UTF-8: {error.reason}",
        )
    return parse_page(rel_path, raw)


def dump_frontmatter(frontmatter: CommentedMap) -> str:
    """Serialise frontmatter back to YAML text, comments and key order intact."""
    stream = io.StringIO()
    _yaml().dump(frontmatter, stream)
    return stream.getvalue()


def round_trip_frontmatter(page: Page) -> CommentedMap | None:
    """`page`'s own frontmatter re-read with the round-trip loader, comments
    and quoting intact — the write path's entry point, since `parse_page`
    reads through the fast loader and returns a plain mapping. `None` when the
    page has no frontmatter block or it does not parse."""
    fm_text, _body, _start = split_frontmatter(page.raw)
    if fm_text is None or not fm_text.strip():
        return None
    try:
        loaded = _yaml().load(fm_text)
    except YAMLError:
        return None
    return loaded if isinstance(loaded, CommentedMap) else None


def render_page(page: Page, frontmatter: CommentedMap | None = None) -> str:
    """Reassemble a page's text, optionally with replacement frontmatter.

    Given no replacement, the page's frontmatter is re-read round-trip rather
    than taken from `page.frontmatter`: the read path's plain mapping carries
    no comments, and writing it back would delete the trailing enum comments
    the templates encode their schema in."""
    source: object | None = frontmatter if frontmatter is not None else round_trip_frontmatter(page)
    if not source:
        return page.body
    if not isinstance(source, CommentedMap):
        raise TypeError("frontmatter must be a round-trip CommentedMap to preserve comments")
    return f"{_FENCE}\n{dump_frontmatter(source)}{_FENCE}\n{page.body}"


def wikilink_targets(text: str) -> list[str]:
    """Every `[[target]]` in `text`, with any `#heading` and `|display` stripped."""
    return [match.group(1).strip() for match in _WIKILINK_RE.finditer(text)]
