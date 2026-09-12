"""Ported from npm's W107 (`utils/scripts/lint-rules/w107-routing-trigger-verbatim.mjs`).

A guardrail doc's opener drifted from the CLAUDE.md routing row that sends
the model there. `_FORMAT.md` F11:

    F11. Guardrail doc shape: the first non-comment line restates the
         doc's routing-table trigger VERBATIM; ...

"Paired trigger lists must stay byte-identical because a model greps its
own draft against whichever copy it last read." A re-tensed verb or one
inserted word is a trigger that no longer fires from one of its two copies.

Reads root `CLAUDE.md` (via `corpus.repo_root`) as its reference, parsed
once into a module-level cache keyed by repo root — the routing table is
one file every check would otherwise re-read. A doc with no routing row
(TRAPS.md, CONTENT.md, _FORMAT.md, every doc reached by a Project bullet
instead) is silent: there is no second copy to drift from.

Normalization before comparison: backticks stripped, whitespace collapsed.
Nothing else — case, wording, tense and punctuation inside the trigger are
all load-bearing, which is the whole point.

Detection only, never fixable: which side is canonical is a judgment call.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.claude_pointer import resolve_at_pointer_text
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_GUARDRAIL_DOC_RE = re.compile(r"(^|/)docs/guardrails/([^/]+)\.md$")
_ROUTING_ROW_RE = re.compile(r"^\|\s*(.+?)\s*\|\s*docs/guardrails/([^/|\s]+\.md)\s*\|\s*$")
_FORMAT_DOC = "docs/guardrails/_FORMAT.md"

_table_cache: dict[str, dict[str, list[str]]] = {}


def _normalize(text: str) -> str:
    """Backticks out, whitespace collapsed — the only permitted difference."""
    return re.sub(r"\s+", " ", text.replace("`", "")).strip()


def _words(text: str) -> list[str]:
    return [w for w in text.split(" ") if w]


def _routing_table(repo_root: Path) -> dict[str, list[str]]:
    """Map<doc-basename, list of trigger texts> from root CLAUDE.md."""
    key = str(repo_root)
    cached = _table_cache.get(key)
    if cached is not None:
        return cached

    table: dict[str, list[str]] = {}
    try:
        raw = resolve_at_pointer_text((repo_root / "CLAUDE.md").read_text(encoding="utf-8"), repo_root)
        for line in raw.split("\n"):
            match = _ROUTING_ROW_RE.match(line)
            if not match:
                continue
            trigger = _normalize(match.group(1))
            if not trigger or re.fullmatch(r"-+", trigger) or trigger == "The moment you...":
                continue
            table.setdefault(match.group(2), []).append(trigger)
    except OSError:
        pass  # No root CLAUDE.md (a fixture vault, a subtree run): every doc stays silent.

    _table_cache[key] = table
    return table


def _strip_trail(word: str) -> str:
    """Sentence punctuation the doc's opener adds when it ends the sentence."""
    return re.sub(r"[.,;:]+$", "", word)


def _opener_line(lines: list[str]) -> tuple[int, str] | None:
    """First non-comment, non-blank line: (0-based index, text)."""
    for index, raw_line in enumerate(lines):
        text = raw_line.strip()
        if not text or text.startswith("<!--"):
            continue
        return index, text
    return None


def _carries_trigger(opener_words: list[str], trigger_words: list[str]) -> bool:
    """Does the opener carry the trigger as a contiguous WORD sequence? Only
    the final word tolerates trailing sentence punctuation."""
    last = len(trigger_words) - 1
    for start in range(len(opener_words) - len(trigger_words) + 1):
        matched = True
        for i, want in enumerate(trigger_words):
            mine = opener_words[start + i]
            if i == last:
                if _strip_trail(mine) != _strip_trail(want):
                    matched = False
                    break
            elif mine != want:
                matched = False
                break
        if matched:
            return True
    return False


def _first_divergence(trigger: str, opener: str) -> str:
    """First word-level divergence, for the actionable half of the message."""
    t = _words(trigger)
    o = _words(opener)

    best_start, best_matched = -1, -1
    for start in range(len(o)):
        if _strip_trail(o[start]) != _strip_trail(t[0]):
            continue
        matched = 0
        while (
            matched < len(t)
            and start + matched < len(o)
            and _strip_trail(o[start + matched]) == _strip_trail(t[matched])
        ):
            matched += 1
        if matched > best_matched:
            best_start, best_matched = start, matched

    if best_start == -1:
        return f'the row opens "{" ".join(t[:6])}", the doc opens "{" ".join(o[:6])}"'

    i = best_matched
    if i >= len(t):
        return "the doc's opener adds words inside the row's text"
    mine = o[best_start + i] if best_start + i < len(o) else None
    if mine is None:
        return f'the doc\'s opener stops before the row\'s "{" ".join(t[i : i + 4])}"'
    return f'row word {i + 1} is "{t[i]}", the doc has "{mine}"'


@register
class RoutingTriggerVerbatimRule(FileRule):
    """Ported from npm's W107 (`utils/scripts/lint-rules/w107-routing-trigger-verbatim.mjs`)."""

    id = "W107"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Make the doc's opener byte-identical to its CLAUDE.md routing-table "
        "trigger (modulo backticks/whitespace)."
    )
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        match = _GUARDRAIL_DOC_RE.search("/" + page.rel_path)
        if not match:
            return

        doc_file = f"{match.group(2)}.md"
        triggers = _routing_table(corpus.repo_root).get(doc_file)
        if not triggers:
            return

        lines = page.raw.split("\n")
        opener = _opener_line(lines)
        if opener is None:
            return
        opener_index, opener_text_raw = opener
        opener_text = _normalize(opener_text_raw)
        opener_words = _words(opener_text)

        for trigger in triggers:
            trigger_words = _words(trigger)
            if _carries_trigger(opener_words, trigger_words):
                continue
            yield self.finding(
                file=page.rel_path,
                line=opener_index + 1,
                message=(
                    f"this opener drifted from CLAUDE.md's routing row for {doc_file} — make "
                    "it byte-identical (modulo backticks/whitespace): the model greps its "
                    "draft against whichever copy it last read, so a re-tensed verb here is a "
                    f"trigger that does not fire ({_FORMAT_DOC} F11). Divergence: "
                    f"{_first_divergence(trigger, opener_text)}"
                ),
            )
