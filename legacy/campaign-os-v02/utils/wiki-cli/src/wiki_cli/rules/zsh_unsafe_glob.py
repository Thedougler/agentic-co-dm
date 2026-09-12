"""W46 — an unquoted glob token (containing `*`) passed to a file-taking
shell command inside a fenced shell code block aborts the whole command in
zsh when it matches zero files ("no matches found"), before the command
itself ever runs. Ported from
`utils/scripts/lint-rules/w46-zsh-unsafe-glob.mjs`.

Fenced blocks only (`SHELL_FENCE_LANGS` or no info string) — never inline
backticks. `SHELL_FENCE_LANGS`/`SHELL_GLOB_COMMANDS` are comma-delimited in
`wiki.toml`, unlike this package's other `;;`/` | `-delimited threshold
lists, so this module splits them locally rather than via
`Config.threshold_list`.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.autofix import current_context
from wiki_cli.config import load_config
from wiki_cli.contracts import (
    Autofix,
    Corpus,
    FileRule,
    Finding,
    Page,
    Severity,
    Tier,
    register,
)

_SCOPED_ROOTS = ("docs/", ".claude/skills/", "pcs/.claude/skills/", "sys/")
_FENCE_START_RE = re.compile(r"^\s*(```|~~~)\s*([A-Za-z]*)\s*$")
_FENCE_END_RE = re.compile(r"^\s*(```|~~~)\s*$")
_SEGMENT_SPLIT_RE = re.compile(r"(\|\||&&|\||;)")
_SEGMENT_DELIM_RE = re.compile(r"^(\|\||&&|\||;)$")
_COMMAND_PREFIX_RE = re.compile(r"^.*/")


def _comma_list(raw: str) -> list[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def _is_skipped_token(token: str) -> bool:
    if token.startswith(("--include=", "--exclude=")):
        return True
    if token.startswith('"') and token.endswith('"') and len(token) >= 2:
        return True
    return bool(token.startswith("'") and token.endswith("'") and len(token) >= 2)


def _check_line(text: str, commands: set[str]) -> list[tuple[str, int]]:
    findings: list[tuple[str, int]] = []
    trimmed = text.strip()
    if trimmed.startswith("#") or trimmed == "":
        return findings

    segments = [s for s in _SEGMENT_SPLIT_RE.split(text) if not _SEGMENT_DELIM_RE.match(s)]
    search_from = 0
    for segment in segments:
        seg_start = text.index(segment, search_from)
        search_from = seg_start + len(segment)

        tokens = [t for t in re.split(r"\s+", segment) if t]
        if not tokens:
            continue
        command_word = _COMMAND_PREFIX_RE.sub("", tokens[0])
        if command_word not in commands:
            continue

        cursor = seg_start
        for token in tokens:
            token_index = text.index(token, cursor)
            cursor = token_index + len(token)
            if token == tokens[0]:
                continue
            if "*" not in token:
                continue
            if _is_skipped_token(token):
                continue
            findings.append((token, token_index + 1))
    return findings


def _quote_globs(text: str) -> str:
    """Every unquoted glob token inside a shell fence wrapped in `"`.

    `_check_line` locates the tokens, so the fix quotes exactly what the
    rule reports and nothing else. A token already carrying a `"` is left
    alone — the rule marks it unfixable for the same reason, and it is what
    makes the second pass a no-op. Replacements run right-to-left so an
    earlier one never shifts a later column.
    """
    context = current_context()
    if context is None:
        return text
    rel = context.rel_path.replace("\\", "/")
    if not rel.endswith(".md") or not rel.startswith(_SCOPED_ROOTS):
        return text

    try:
        config = load_config()
        shell_langs = set(_comma_list(config.threshold("SHELL_FENCE_LANGS"))) | {""}
        commands = set(_comma_list(config.threshold("SHELL_GLOB_COMMANDS")))
    except (OSError, KeyError, ValueError):
        return text

    lines = text.split("\n")
    in_fence = False
    fence_is_shell = False
    for index, line in enumerate(lines):
        if not in_fence:
            start = _FENCE_START_RE.match(line)
            if start:
                in_fence = True
                fence_is_shell = start.group(2).lower() in shell_langs
            continue
        if _FENCE_END_RE.match(line):
            in_fence = False
            fence_is_shell = False
            continue
        if not fence_is_shell:
            continue

        hits = [hit for hit in _check_line(line, commands) if '"' not in hit[0]]
        for token, column in sorted(hits, key=lambda hit: hit[1], reverse=True):
            start_at = column - 1
            line = line[:start_at] + f'"{token}"' + line[start_at + len(token) :]
        lines[index] = line
    return "\n".join(lines)


@register
class ZshUnsafeGlob(FileRule):
    id = "W46"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = 'Quote the glob token, e.g. change *.md to "*.md", so zsh doesn\'t abort on no match.'
    producer = "wiki"
    pure = True
    fixable = True
    autofix = Autofix(scope="syntax", apply=_quote_globs)

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path.replace("\\", "/")
        if not rel.endswith(".md"):
            return
        if not any(rel.startswith(root) for root in _SCOPED_ROOTS):
            return

        config = load_config()
        shell_langs = set(_comma_list(config.threshold("SHELL_FENCE_LANGS"))) | {""}
        commands = set(_comma_list(config.threshold("SHELL_GLOB_COMMANDS")))

        in_fence = False
        fence_is_shell = False
        for file_line, text in page.body_lines():
            if not in_fence:
                start = _FENCE_START_RE.match(text)
                if start:
                    in_fence = True
                    fence_is_shell = start.group(2).lower() in shell_langs
                continue
            if _FENCE_END_RE.match(text):
                in_fence = False
                fence_is_shell = False
                continue
            if not fence_is_shell:
                continue

            for token, column in _check_line(text, commands):
                can_quote = '"' not in token
                yield self.finding(
                    file=page.rel_path,
                    line=file_line,
                    message=(
                        f'unquoted glob `{token}` aborts the whole command in zsh when it '
                        "matches nothing — quote the pattern or use grep -r "
                        '--include="*.md" <dir> / find instead'
                    ),
                    column=column,
                    fixable=can_quote,
                )
