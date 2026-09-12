"""context-rot producer (W91): undated/expired transient markers
("TEMPORARY", "TODO:", "re-enable once X lands", "for now") in config and
script comments. Mirrors `utils/scripts/lint-context-rot.mjs`.

A comment that parks a setting as temporary is a promise to come back.
Undated, it is unfalsifiable: no later reader can tell whether the
condition that justified it still holds, so the workaround outlives its
cause and becomes the config. Dated, it becomes a checkable claim — and one
that has aged past the window is exactly the claim worth re-checking.

Scope is this repo's own fixed domain — the config surface
(`_CONFIG_TARGETS`) plus every script under `utils/scripts/**/*.mjs` — not
whatever vault pages the caller happens to be linting; that domain is
sub-second and rides every run, scoped and sweep alike.
When `targets` narrows to paths that are actually inside this domain, only
those are checked (matching the legacy module's own `run(targets)`
narrowing); an empty or entirely out-of-domain `targets` list (e.g. a
normal vault-page sweep, which never touches this producer's domain at
all) falls back to the full default scan — the caller not naming any of
this producer's own files is not a request to check nothing.

Only COMMENT lines are scanned — a marker inside a string literal or a
phrase-list constant is data, not a promise.
"""

from __future__ import annotations

import re
from datetime import UTC, datetime
from pathlib import Path

from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, Finding, ProducerRuleDoc, Severity, Tier

FAMILY_ID = "W91"
VERSION = "1"
PURE = False
"""Uncached: a transient marker expires by the calendar, so an unchanged
file's verdict changes on its own with the date."""

RULE_DOCS: tuple[ProducerRuleDoc, ...] = (
    ProducerRuleDoc(
        id=FAMILY_ID,
        tier=Tier.STRUCTURAL,
        severity=Severity.WARNING,
        fix=(
            "Re-verify the marked comment's condition now: resolved -> delete the marker and "
            "restore the setting it parks; still open -> re-date it `(YYYY-MM-DD, until <the "
            "check that ends it>)`. Softening the wording is not a fix."
        ),
    ),
)

_SELF = "utils/scripts/lint-context-rot.mjs"
"""The legacy engine's own script — excluded from its own scan domain
because its docstring cites marker phrases as illustrative examples, not
as promises. This Python port lives elsewhere, but the same legacy path
must stay excluded from the scan domain for parity: this producer scans
`utils/scripts/**/*.mjs` by SHAPE, which would otherwise pick the legacy
file back up."""

_CONFIG_TARGETS: tuple[str, ...] = (
    ".obsidian-linter.jsonc",
    ".vale.ini",
    ".vale-hard.ini",
    ".jscpd.json",
    ".oxlintrc.json",
    ".markdown-link-check.json",
    ".claude/settings.json",
    ".pre-commit-config.yaml",
    "utils/scripts/lint-rules/skills-config.jsonc",
    "utils/scripts/lint-rules/sweep-config.jsonc",
)

_DEFAULT_PHRASES: tuple[str, ...] = (
    "TEMPORARY",
    "temporarily (disabled|off|removed)",
    (
        r"(disabled|off|skip|park|hold|defer|blocked|pending|re-?enable|revisit)"
        r"[^\n]{0,40}until .{0,40}(lands|ships|migration)"
    ),
    "re-enable",
    "revisit",
    "in-flight",
    "for now",
    "TODO:",
    "FIXME",
    "disabled pending",
)
"""`utils/scripts/lint-context-rot.mjs`'s `DEFAULT_PHRASES`, verbatim. Falls
back to this until `wiki.toml` carries a `TRANSIENT_MARKER_PHRASES` key —
see `_phrases` below."""

_DEFINITION_LINE_RE = re.compile(r"PHRASES|_TERMS|_MARKER")
"""A line that DEFINES the marker vocabulary (this rule's own list, a
phrase constant, a term list) quotes the markers instead of making a
promise."""

_QUOTED_SPAN_RE = re.compile(r'"[^"\n]*"')
"""A marker inside double quotes is being CITED, not made. Quoted spans are
blanked before matching, so a bare `TODO: swap this back` on the same line
still fires."""

_ISO_DATE_RE = re.compile(r"\b(\d{4})-(\d{2})-(\d{2})\b")
_DATE_LOOKBACK_LINES = 3

_HASH_SEMI_EXTS = frozenset({".ini", ".yaml", ".yml"})
_HASH_SEMI_RE = re.compile(r"(?:^|\s)[#;](.*)$")


def _in_scope(rel: str) -> bool:
    """Path-only scope predicate, same shape the legacy module exports for
    its own orchestrator wiring to reuse."""
    if rel == _SELF:
        return False
    if rel.endswith(".test.mjs"):
        return False  # fixtures quote markers verbatim
    if rel.startswith("utils/scripts/lint-rules/config/"):
        return False  # data, not comments
    if rel in _CONFIG_TARGETS:
        return True
    return rel.startswith("utils/scripts/") and rel.endswith(".mjs")


def _walk_scripts(repo_root: Path) -> list[str]:
    scripts_root = repo_root / "utils" / "scripts"
    if not scripts_root.is_dir():
        return []
    out: list[str] = []
    for path in scripts_root.rglob("*.mjs"):
        rel = path.relative_to(repo_root)
        if any(part == "node_modules" or part.startswith(".") for part in rel.parts[:-1]):
            continue
        out.append(str(rel))
    return sorted(out)


def _default_targets(repo_root: Path) -> list[str]:
    candidates = [*_CONFIG_TARGETS, *_walk_scripts(repo_root)]
    return sorted({rel for rel in candidates if _in_scope(rel)})


_DEFAULT_MAX_AGE_DAYS = 30
"""`utils/scripts/lint-context-rot.mjs`'s own `readOptionalNumberConstant`
default — used when `wiki.toml` carries no `TRANSIENT_MARKER_MAX_AGE_DAYS`
key (or when `run` is invoked, as every producer is, through `run_lint`
against a `Config` built for an unrelated test/caller that never populated
`thresholds` at all) — this producer must never crash the whole
orchestrator run over a missing key it happens to own."""


def _phrases(config: Config) -> tuple[str, ...]:
    try:
        return tuple(config.threshold_list("TRANSIENT_MARKER_PHRASES"))
    except KeyError:
        return _DEFAULT_PHRASES


def _max_age_days(config: Config) -> int:
    try:
        return int(config.threshold("TRANSIENT_MARKER_MAX_AGE_DAYS"))
    except KeyError:
        return _DEFAULT_MAX_AGE_DAYS


def _build_matchers(phrases: tuple[str, ...]) -> list[re.Pattern[str]]:
    """Uppercase anywhere in a phrase source => the marker is an all-caps
    token, matched case-sensitively (TEMPORARY, TODO:, FIXME are all-caps
    tokens by convention — "todo" inside a word like "todos" or a
    lowercase sentence is prose, not a marker); every other source is
    matched case-insensitively. An unparseable configured source is
    skipped rather than killing the run."""
    matchers: list[re.Pattern[str]] = []
    for source in phrases:
        source = source.strip()
        if not source:
            continue
        flags = 0 if re.search(r"[A-Z]", source) else re.IGNORECASE
        try:
            matchers.append(re.compile(source, flags))
        except re.error:
            continue
    return matchers


def _comment_of_line(line: str, in_block: bool) -> tuple[str, bool]:
    """The comment text of one JS-family line, and the updated block-comment
    state — character scan rather than indexOf juggling, since a `//`
    inside a string literal is not a comment opener and only tracking
    quotes tells the two apart. Ported statement-for-statement from the
    legacy `for`-loop so every `c += 1` (block-close, comment-open) still
    lands on the same character the JS version does."""
    parts: list[str] = []
    quote: str | None = None
    c = 0
    n = len(line)
    while c < n:
        ch = line[c]
        if in_block:
            if ch == "*" and c + 1 < n and line[c + 1] == "/":
                in_block = False
                c += 1
            else:
                parts.append(ch)
            c += 1
            continue
        if quote is not None:
            if ch == "\\":
                c += 1
            elif ch == quote:
                quote = None
            c += 1
            continue
        if ch in "\"'`":
            quote = ch
            c += 1
            continue
        if ch == "/" and c + 1 < n and line[c + 1] == "/":
            parts.append(line[c + 2 :])
            break
        if ch == "/" and c + 1 < n and line[c + 1] == "*":
            in_block = True
            c += 1
        c += 1
    return "".join(parts), in_block


def _comment_lines(rel: str, lines: list[str]) -> list[str]:
    """The comment text on each line, or `""` for a line with no comment.
    Block comments carry state across lines for JS-family files; `.ini`/
    `.yaml` use `#`/`;` line comments only."""
    if Path(rel).suffix in _HASH_SEMI_EXTS:
        out = []
        for line in lines:
            match = _HASH_SEMI_RE.search(line)
            out.append(match.group(1) if match else "")
        return out

    out = []
    in_block = False
    for line in lines:
        comment, in_block = _comment_of_line(line, in_block)
        out.append(comment)
    return out


def _nearest_date(comments: list[str], index: int) -> str | None:
    """The ISO date nearest the hit line, searching it then upward."""
    i = index
    while i >= 0 and i >= index - _DATE_LOOKBACK_LINES:
        found = list(_ISO_DATE_RE.finditer(comments[i]))
        if found:
            return found[-1].group(0)
        i -= 1
    return None


def _days_between(iso_date: str, now: datetime) -> int | None:
    try:
        then = datetime.strptime(iso_date, "%Y-%m-%d").replace(tzinfo=UTC)
    except ValueError:
        return None
    today = datetime(now.year, now.month, now.day, tzinfo=UTC)
    return (today - then).days


def _check_file(
    repo_root: Path,
    rel: str,
    matchers: list[re.Pattern[str]],
    max_age_days: int,
    now: datetime,
) -> list[Finding]:
    try:
        raw = (repo_root / rel).read_text(encoding="utf-8")
    except OSError:
        return []  # a listed config this repo does not have — nothing to scan

    lines = raw.split("\n")
    comments = _comment_lines(rel, lines)
    findings: list[Finding] = []

    for i, text in enumerate(comments):
        if text.strip() == "":
            continue
        if _DEFINITION_LINE_RE.search(lines[i]):
            continue
        uncited = _QUOTED_SPAN_RE.sub(" ", text)
        if not any(matcher.search(uncited) for matcher in matchers):
            continue

        date = _nearest_date(comments, i)
        age = _days_between(date, now) if date is not None else None
        if date is not None and age is not None and age <= max_age_days:
            continue

        if date is None or age is None:
            message = (
                'Transient marker with no date — add "(TEMPORARY <YYYY-MM-DD>, resolve when: '
                '<observable condition>)" or delete the marker and the workaround with it; '
                "an undated transient can never be retired"
            )
        else:
            message = (
                f"Transient marker dated {date} is {age} days old — re-verify its condition now: "
                "resolved, delete the marker and restore the real setting; still open, re-date it "
                "with the check that ends it"
            )

        findings.append(
            Finding(
                rule_id=FAMILY_ID,
                file=rel,
                line=i + 1,
                message=message,
                severity=Severity.WARNING,
                tier=Tier.STRUCTURAL,
                producer="context-rot",
                column=1,
                fixable=False,
            )
        )

    return findings


def run(config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]:
    """Scan this producer's own fixed domain (`_default_targets`) for
    undated/expired transient markers, narrowed to `targets` only when
    `targets` actually names files inside that domain — see the module
    docstring for why an out-of-domain `targets` list (the normal case for
    a vault-page sweep) falls back to the full scan instead of scanning
    nothing.
    """
    repo_root = corpus.repo_root
    matchers = _build_matchers(_phrases(config))
    max_age_days = _max_age_days(config)
    now = datetime.now(UTC)

    all_targets = _default_targets(repo_root)

    requested: set[str] = set()
    for target in targets:
        try:
            requested.add(str(target.resolve().relative_to(repo_root)))
        except ValueError:
            continue
    narrowed = sorted(rel for rel in requested if rel in all_targets)
    scope = narrowed if narrowed else all_targets

    findings: list[Finding] = []
    for rel in scope:
        findings.extend(_check_file(repo_root, rel, matchers, max_age_days, now))
    return findings
