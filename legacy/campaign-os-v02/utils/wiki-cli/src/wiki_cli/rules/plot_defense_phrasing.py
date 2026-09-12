"""Ported from npm's W71 (`utils/scripts/lint-rules/w71-plot-defense-phrasing.mjs`).

A DM directive that forbids a table outcome ("don't let a PC...", "the
party can't skip...", "nobody at the table tests it") with no stated
fallback for what actually happens if the table does it anyway reads as
railroad-by-omission — a future DM improvising at the table has no branch
to run if a player insists, tries the forbidden thing, or the "guaranteed"
outcome doesn't hold.

Same phrase-tell mechanism as W63 (invented mystery): a curated term list
flags the tell; an adjacent fallback marker within the next few lines
clears it. Scoped exactly as the legacy module — `vault/`, `pcs/`,
`sessions/`, no directory exemptions; every file under the scoped roots is
scanned, vendored/DM-only material included, because an un-fallbacked
plot-defense line is a glitch wherever it's written.

Term lists (`PLOT_DEFENSE_TELL_PHRASES` / `PLOT_DEFENSE_FALLBACK_PHRASES`)
and the lookahead window (`PLOT_DEFENSE_FALLBACK_LOOKAHEAD_LINES`) come from
`wiki.toml`'s `[thresholds]` table, mirroring the legacy
`utils/scripts/lint-rules/config/thresholds.json` values.

Detection only — the fix (write the fallback branch, or rephrase to
describe the outcome directly) is judgment.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

SCOPED_ROOTS = ("vault/", "pcs/", "sessions/")

_FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_FENCE_RE = re.compile(r"^\s*(`+|~+)\s*$")
_HTML_COMMENT_RE = re.compile(r"^<!--.*-->$")


def _fenced_flags(lines: list[str]) -> list[bool]:
    flags = [False] * len(lines)
    open_fence: tuple[str, int] | None = None
    for i, line in enumerate(lines):
        if open_fence is None:
            match = _FENCE_LINE_RE.match(line)
            if match:
                open_fence = (match.group(1)[0], len(match.group(1)))
                flags[i] = True
            continue
        flags[i] = True
        close = _CLOSING_FENCE_RE.match(line)
        if close and close.group(1)[0] == open_fence[0] and len(close.group(1)) >= open_fence[1]:
            open_fence = None
    return flags


@register
class PlotDefensePhrasingRule(FileRule):
    """Ported from npm's W71 (`w71-plot-defense-phrasing.mjs`)."""

    id = "W71"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        "Add what happens if the party/a PC actually does it (a nearby "
        '"if they do", "if a player insists", "let it happen:" branch), or '
        "rephrase to describe the outcome directly."
    )
    producer = "wiki"
    pure = True
    """Reads wiki.toml thresholds too, but those are captured by
    Config.fingerprint (part of the cache key) — unlike frontmatter_schema's
    dependency on the _templates/ file tree, a threshold-value change alone
    correctly invalidates the cache here."""
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md"):
            return
        if not any(rel.startswith(root) for root in SCOPED_ROOTS):
            return

        config = load_config()
        tell_patterns = [
            re.compile(source, re.IGNORECASE)
            for source in config.threshold_list("PLOT_DEFENSE_TELL_PHRASES")
        ]
        fallback_patterns = [
            re.compile(source, re.IGNORECASE)
            for source in config.threshold_list("PLOT_DEFENSE_FALLBACK_PHRASES")
        ]
        lookahead = int(config.threshold("PLOT_DEFENSE_FALLBACK_LOOKAHEAD_LINES"))

        body = list(page.body_lines())
        texts = [text for _, text in body]
        fenced = _fenced_flags(texts)

        for i, (line_no, text) in enumerate(body):
            if fenced[i]:
                continue
            if _HTML_COMMENT_RE.match(text.strip()):
                continue

            for pattern in tell_patterns:
                match = pattern.search(text)
                if not match:
                    continue

                window_end = min(len(texts), i + 1 + lookahead)
                window = " ".join(texts[i:window_end])
                has_fallback = any(fb.search(window) for fb in fallback_patterns)
                if has_fallback:
                    break

                yield self.finding(
                    file=rel,
                    line=line_no,
                    message=(
                        f'Plot-defense phrasing "{match.group(0)}" bans a table outcome with no '
                        "stated fallback — add what happens if the party/a PC actually does it (a "
                        'nearby "if they do", "if a player insists", "let it happen:" branch), or '
                        "rephrase to describe the outcome directly"
                    ),
                )
                break
