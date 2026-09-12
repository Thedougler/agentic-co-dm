"""links producer (W85): pure-Python markdown-link checking, no Node binary.

Only inline markdown links (`](...)`) and autolinks (`<https://...>`) are in
scope — this vault links almost entirely by `[[wikilink]]`, which is a
different syntax checked by the native wikilink-resolution rules, not this
producer. `.markdown-link-check.json`'s own `ignorePatterns`
(`^https?://`) excludes every external URL, so only local/relative link
resolution is ever checked here — this producer never makes a network
call, it only stats the filesystem.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit

from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, Finding, ProducerRuleDoc, Severity, Tier

FAMILY_ID = "W85"
VERSION = "1"
PURE = False
"""Uncached: a link finding turns on whether the TARGET path exists, so
another file appearing or vanishing changes this file's verdict without
changing its bytes."""

RULE_DOCS: tuple[ProducerRuleDoc, ...] = (
    ProducerRuleDoc(
        id=FAMILY_ID,
        tier=Tier.STRUCTURAL,
        severity=Severity.WARNING,
        fix=(
            "Repoint the `](target)` link at a path that exists — find it with "
            "`git ls-files | grep <basename>` — or delete the link if the target is gone. A "
            "page inside vault/ is linked as a [[wikilink]], never as a relative path."
        ),
    ),
)

_HAS_MD_LINK_RE = re.compile(r"\]\(|<https?://")
"""A file with no markdown-syntax link has no link this producer can check
— skipping it avoids scanning line-by-line for a file that carries no link
at all, same optimization as the legacy `carriesMarkdownLink`."""

_FENCE_RE = re.compile(r"^(```|~~~)")
"""Fenced code block delimiter, either flavor, any info-string after it."""

_MD_LINK_RE = re.compile(r"(?<!\\)\[([^\]]*)\]\(([^)]+)\)")
"""Inline link/image target: `[text](target)` or `![alt](target)` — the
leading `!` of an image is simply not consumed, so both shapes match
identically and a broken image path is reported the same as a broken link.
A backslash immediately before `[` marks it escaped (`\\[not a link]`),
excluded via the lookbehind."""

_AUTOLINK_RE = re.compile(r"<(https?://[^>\s]+)>")
"""Autolinks are always an absolute URL by CommonMark's own grammar, so
every match here is external and filtered out by `_is_external` — kept
only so a file containing solely `<https://...>` autolinks still passes
`_HAS_MD_LINK_RE`'s fast-path gate."""

_TARGET_RE = re.compile(r'^(\S+)(?:\s+["\'].*)?$')
"""Splits a link-destination string into its path and an optional
`"title"`/`'title'` suffix (CommonMark's inline-link title syntax)."""


def _load_link_check_config(
    repo_root: Path,
) -> tuple[list[re.Pattern[str]], list[tuple[re.Pattern[str], str]]]:
    """Read `.markdown-link-check.json`'s `ignorePatterns` and
    `replacementPatterns` so this producer excludes and rewrites link
    targets exactly as the config directs, same as the legacy binary did."""
    config_path = repo_root / ".markdown-link-check.json"
    try:
        raw = json.loads(config_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return [], []

    ignore_patterns = [re.compile(entry["pattern"]) for entry in raw.get("ignorePatterns", [])]
    replacement_patterns = [
        (re.compile(entry["pattern"]), entry["replacement"])
        for entry in raw.get("replacementPatterns", [])
    ]
    return ignore_patterns, replacement_patterns


def _non_code_lines(content: str) -> list[tuple[int, str]]:
    """(1-indexed line, text) for every line outside a fenced code block —
    a link inside a fence is sample text, not a real reference to check."""
    lines: list[tuple[int, str]] = []
    in_code = False
    for line_no, line in enumerate(content.splitlines(), start=1):
        if _FENCE_RE.match(line.lstrip()):
            in_code = not in_code
            continue
        if in_code:
            continue
        lines.append((line_no, line))
    return lines


def _iter_raw_targets(line: str) -> list[str]:
    """Every link-destination string found on one line, markdown links and
    image paths first, then URL autolinks (always external, see
    `_AUTOLINK_RE`)."""
    targets = [match.group(2) for match in _MD_LINK_RE.finditer(line)]
    targets.extend(match.group(1) for match in _AUTOLINK_RE.finditer(line))
    return targets


def _extract_target(raw: str) -> str:
    """Strip a CommonMark title suffix or `<...>` wrapper off a raw link
    destination, leaving just the path/URL."""
    raw = raw.strip()
    if raw.startswith("<"):
        end = raw.find(">")
        return raw[1:end] if end != -1 else raw[1:]
    match = _TARGET_RE.match(raw)
    return match.group(1) if match else raw


def _is_external(target: str) -> bool:
    """A scheme (`https:`, `mailto:`, ...) or a network location
    (`//host/path`) means this points off the filesystem — nothing this
    producer, which only stats local paths, can check."""
    parsed = urlsplit(target)
    return bool(parsed.scheme or parsed.netloc)


def _resolve_local_target(file_path: Path, repo_root: Path, path_part: str) -> Path:
    """Relative targets resolve against the linking file's own directory —
    matching how a browser or Obsidian resolves a relative markdown link.
    A leading `/` is repo-root-relative by convention; resolved directly
    against the file's parent instead, pathlib's `/` operator would
    discard the parent entirely and point at the filesystem root."""
    if path_part.startswith("/"):
        return repo_root / path_part.lstrip("/")
    return file_path.parent / path_part


def run(config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]:
    """Check every local/relative markdown link in `targets` for a target
    that resolves to a real file — pure filesystem `exists()` calls, no
    subprocess and no network access.

    `targets` are absolute paths under the repo. A non-`.md` target or one
    with no markdown-syntax link is skipped — neither has anything this
    producer can check. `.markdown-link-check.json`'s `ignorePatterns` and
    `replacementPatterns` are honored so this stays behaviorally aligned
    with the legacy engine's own config.
    """
    del config  # this producer's invocation is fully determined by the shared config file on disk
    if not targets:
        return []

    repo_root = corpus.repo_root
    ignore_patterns, replacement_patterns = _load_link_check_config(repo_root)

    findings: list[Finding] = []
    for target in targets:
        if target.suffix != ".md":
            continue
        try:
            content = target.read_text(encoding="utf-8")
        except OSError:
            continue
        if not _HAS_MD_LINK_RE.search(content):
            continue

        rel_path = str(target.resolve().relative_to(repo_root))
        for line_no, line in _non_code_lines(content):
            for raw in _iter_raw_targets(line):
                link_target = _extract_target(raw)
                if not link_target:
                    continue

                for pattern, replacement in replacement_patterns:
                    link_target = pattern.sub(replacement, link_target, count=1)

                if any(pattern.search(link_target) for pattern in ignore_patterns):
                    continue
                if _is_external(link_target):
                    continue

                path_part = unquote(link_target.split("#", 1)[0].strip())
                if not path_part:
                    continue  # fragment-only link (`#heading`) — nothing local to resolve

                resolved = _resolve_local_target(target, repo_root, path_part)
                if resolved.exists():
                    continue

                findings.append(
                    Finding(
                        rule_id=FAMILY_ID,
                        file=rel_path,
                        line=line_no,
                        message=f"Broken link: {link_target} (target does not exist)",
                        severity=Severity.WARNING,
                        tier=Tier.STRUCTURAL,
                        producer="links",
                        fixable=False,
                    )
                )
    return findings
