"""Ported from npm's W115 (`utils/scripts/lint-rules/w115-naming-substitute.mjs`).

A note telling the DM a name must never be spoken at the table ("naming
discipline", "never say X aloud") must script the table-safe substitute
beside it, quoted — otherwise the DM is left to coin one live, mid-fight
(draft-moment Hard Rule 11; docs/adr/0025). Clears when the tell's own line
or the next few lines carry BOTH a substitute marker ("substitute", "call
it", "instead", "table-safe") AND a quoted phrase.

Scoped to `vault/episodes/` only, matching the legacy module. Term lists
(`NAMING_DISCIPLINE_TELL_PHRASES` / `NAMING_SUBSTITUTE_MARKER_PHRASES`) and
the lookahead window (`NAMING_SUBSTITUTE_LOOKAHEAD_LINES`) come from
`wiki.toml`'s `[thresholds]` table.

Detection only — the substitute itself is the author's judgment.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

EPISODES_SEGMENT = re.compile(r"^vault/episodes/")
QUOTED_PHRASE = re.compile(r'["“][^"”\n]{2,60}["”]')

_FENCE_LINE_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_FENCE_RE = re.compile(r"^\s*(`+|~+)\s*$")


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
class NamingSubstituteRule(FileRule):
    """Ported from npm's W115 (`w115-naming-substitute.mjs`)."""

    id = "W115"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        'Add the quoted table-safe name beside the note (e.g. Table-safe '
        'substitute: "the Foul One") so the DM never coins one mid-fight '
        "(draft-moment Hard Rule 11)."
    )
    producer = "wiki"
    pure = True
    """Reads wiki.toml thresholds too; captured by Config.fingerprint (the
    cache key), same reasoning as plot_defense_phrasing.py."""
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md"):
            return
        if not EPISODES_SEGMENT.match(rel):
            return

        config = load_config()
        tells = [
            re.compile(source, re.IGNORECASE)
            for source in config.threshold_list("NAMING_DISCIPLINE_TELL_PHRASES")
        ]
        markers = [
            re.compile(source, re.IGNORECASE)
            for source in config.threshold_list("NAMING_SUBSTITUTE_MARKER_PHRASES")
        ]
        lookahead = int(config.threshold("NAMING_SUBSTITUTE_LOOKAHEAD_LINES"))

        body = list(page.body_lines())
        texts = [text for _, text in body]
        fenced = _fenced_flags(texts)

        for i, (line_no, text) in enumerate(body):
            if fenced[i]:
                continue
            if not any(tell.search(text) for tell in tells):
                continue

            window = "\n".join(texts[i : i + 1 + lookahead])
            if any(marker.search(window) for marker in markers) and QUOTED_PHRASE.search(window):
                continue

            yield self.finding(
                file=rel,
                line=line_no,
                message=(
                    "naming-discipline note with no scripted substitute — add the quoted "
                    'table-safe name beside it (e.g. Table-safe substitute: "the Foul One") so '
                    "the DM never coins one mid-fight (draft-moment Hard Rule 11)"
                ),
            )
