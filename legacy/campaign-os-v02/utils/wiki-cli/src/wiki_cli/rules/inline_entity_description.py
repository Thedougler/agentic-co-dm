"""Ported from npm's W77
(`utils/scripts/lint-rules/w77-inline-entity-description.mjs`).

A page narrates a distinct atomic entity — its personality, backstory,
motivation — in depth, instead of that entity getting its own `vault/<type>/`
page and being wikilinked/embedded back
(`vault/.claude/skills/obsidian-markdown/references/dry-content-patterns.md`).
Confirmed shape: a ship page describing its captain's personality and
backstory inline instead of the captain having a `type: npc` page.

Detection only, heuristic — expect false positives (severity: warning). The
fix is a judgment call, never this rule's: extract every fact the flagged
span states about the entity, create its page via the matching `*-prep`
skill, then replace the inline prose with a wikilink or section embed. This
rule never creates a page or inserts a link itself — same division of labor
as W25/W122 (cross-linker resolves it).

`SIGNAL_SETS` is keyed by candidate atomic type so a new type is a data
addition, never a rewrite of the detection logic below. Each entry names: a
human label, the owning `*-prep` skill/guide, the template it instantiates,
and the personality/backstory/motivation/dialogue keyword vocabulary that
marks prose as "about a distinct entity's inner life" rather than mechanical
or descriptive prose about the host page's own subject.

Documented exclusions (ported verbatim): `vault/campaigns/shattered-sea/pcs/`
(player-authored, different rules), `vault/refs/` (GM-methodology reference —
its prose discusses spells/items/abilities as subject matter, never as
campaign entities needing their own page), and `status: srd` pages (vendored
upstream RAW text — a cross-reference is sourced wording, not inline
authorship).

Not pure — resolution against the corpus (`corpus.resolve`) decides the
message wording (and the legacy engine's keyword-hit threshold), though not
whether a finding fires at all.
"""

from __future__ import annotations

import re
from collections.abc import Iterator
from dataclasses import dataclass

from wiki_cli.config import Config
from wiki_cli.config import load_config as _load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SCOPED_ROOT = "vault/"


@dataclass(frozen=True, slots=True)
class _SignalSet:
    label: str
    guide: str
    template_path: str
    keywords: tuple[str, ...]


SIGNAL_SETS: dict[str, _SignalSet] = {
    "npc": _SignalSet(
        label="an NPC",
        guide="vault/refs/vault/npc/GUIDE.md",
        template_path="vault/_templates/_campaigns/_npcs/_npc.md",
        keywords=(
            "personality",
            "temperament",
            "demeanor",
            "demeanour",
            "backstory",
            "motivation",
            "motivations",
            "grew up",
            "childhood",
            "vowed",
            "swore",
            "secretly",
            "in truth",
            "resents",
            "resentment",
            "grudge",
            "vendetta",
            "revenge",
            "redemption",
            "atone",
            "atonement",
            "trauma",
            "traumatized",
            "traumatised",
            "haunted",
            "obsessed",
            "obsession",
            "believes",
            "convinced that",
            "distrusts",
            "trusts no one",
            "dreams of",
            "hopes to",
            "wants nothing more",
            "only fear",
            "never forgiven",
            "never forgave",
            "driven by",
            "his goal",
            "her goal",
            "their goal",
            "his wish",
            "her wish",
            "forgiven",
            "forgave",
            "his past",
            "her past",
        ),
    ),
    "faction": _SignalSet(
        label="a faction",
        guide="the faction-prep skill",
        template_path="vault/_templates/_srd/_faction.md",
        keywords=(
            "founded",
            "founding",
            "their ranks",
            "its ranks",
            "members swear",
            "membership",
            "initiates",
            "initiation",
            "hierarchy",
            "chapters",
            "their creed",
            "its creed",
            "doctrine",
            "sworn to",
            "their charter",
            "its charter",
            "their goal",
            "its goal",
            "their agenda",
            "its agenda",
            "seeks to control",
            "seeks to overthrow",
            "recruit",
            "recruits",
            "recruiting",
            "loyal to",
            "answer to",
            "answers to",
            "their leader",
            "its leader",
            "splinter",
            "schism",
            "rival faction",
            "front for",
        ),
    ),
    "location": _SignalSet(
        label="a location",
        guide="the location-prep skill",
        template_path="_templates/location.md",
        keywords=(
            "settlement of",
            "village of",
            "port of",
            "district of",
            "built on",
            "built into",
            "built atop",
            "its harbor",
            "its harbour",
            "its streets",
            "its docks",
            "its market",
            "population",
            "inhabitants",
            "the locals",
            "founded on",
            "ruins of",
            "once a",
            "its walls",
            "its gates",
            "landmark",
            "overlooks",
            "nestled",
            "sprawls",
            "its taverns",
            "governed by",
            "ruled from",
            "trade hub",
            "its economy",
        ),
    ),
    "item": _SignalSet(
        label="an item",
        guide="the item-prep skill",
        template_path="_templates/item.md",
        keywords=(
            "forged by",
            "forged in",
            "crafted by",
            "crafted from",
            "enchanted by",
            "its wielder",
            "the wielder",
            "its blade",
            "its hilt",
            "its pages",
            "its previous owner",
            "last owner",
            "passed down",
            "heirloom",
            "relic of",
            "artifact of",
            "artefact of",
            "its power wanes",
            "when unsheathed",
        ),
    ),
}

LEADING_STOPWORDS = frozenset(
    {
        "the",
        "this",
        "that",
        "these",
        "those",
        "his",
        "her",
        "their",
        "our",
        "your",
        "my",
        "a",
        "an",
        "its",
    }
)

# Two consecutive Title Case words — the shape a personal name takes. Hyphens
# allowed inside a word so a hyphenated name ("Jean-Claude") is captured
# whole, not truncated at the hyphen.
_NAME_PATTERN = re.compile(r"\b([A-Z][a-zA-Z'’-]+)\s+([A-Z][a-zA-Z'’-]+)\b")

_H1_RE = re.compile(r"^#\s+(.+?)\s*$")
_HEADING_ANY_RE = re.compile(r"^#{1,6}\s+(.+?)\s*$", re.MULTILINE)
_BOLD_SPAN_RE = re.compile(r"\*\*([^*\n]+?)\*\*")
_MARKUP_STRIP_RE = re.compile(r"[*_]")
_TRAILING_PUNCT_RE = re.compile(r"[.:]$")
_CALLOUT_OPEN_RE = re.compile(r"^>\s*\[!")

_OPEN_QUOTES = frozenset({'"', "“", "‘", "«"})
_CLOSE_QUOTES = frozenset({'"', "”", "’", "»"})

# A candidate is sentence-initial at an occurrence if nothing but optional
# `**`/list/quote markers separate it from a preceding paragraph-start, blank
# line, or `.`/`!`/`?` + whitespace.
_SENTENCE_INITIAL_RE = re.compile(r"""(^|[.!?])[*_]*\s+[*"'“‘«]*$""")

_MIN_OCCURRENCES_DEFAULT = 2
_MIN_HITS_UNRESOLVED_DEFAULT = 2
_MIN_HITS_RESOLVED_DEFAULT = 4


def _threshold_int(config: Config, key: str, default: int) -> int:
    try:
        raw = config.threshold(key)
    except KeyError:
        return default
    try:
        return int(raw)
    except ValueError:
        return default


def _title_words(page: Page) -> set[str]:
    words = {page.slug.replace("-", " ").lower()}
    for _, line in page.body_lines():
        match = _H1_RE.match(line)
        if match:
            words.add(_MARKUP_STRIP_RE.sub("", match.group(1)).strip().lower())
            break
    return words


def _structural_labels(page: Page) -> set[str]:
    """Every `## Heading` and `**bold span**` on the page, lowercased — a
    name candidate that's really a cross-referenced section label or a
    bold-label paragraph opener is page structure, not a person."""
    labels: set[str] = set()
    for match in _HEADING_ANY_RE.finditer(page.raw):
        labels.add(_MARKUP_STRIP_RE.sub("", match.group(1)).strip().lower())
    for match in _BOLD_SPAN_RE.finditer(page.raw):
        labels.add(_TRAILING_PUNCT_RE.sub("", match.group(1)).strip().lower())
    return labels


def _is_quote_wrapped(text: str, start: int, end: int) -> bool:
    before = text[start - 1] if start > 0 else ""
    after = text[end] if end < len(text) else ""
    return before in _OPEN_QUOTES and after in _CLOSE_QUOTES


def _is_sentence_initial(text: str, start_idx: int) -> bool:
    before = text[max(0, start_idx - 10) : start_idx]
    return bool(_SENTENCE_INITIAL_RE.search(before))


@dataclass(frozen=True, slots=True)
class _Paragraph:
    text: str
    start_line: int


def _extract_paragraphs(page: Page) -> list[_Paragraph]:
    """Prose paragraphs — code fences, headings, table rows, and callout
    opener lines excluded, matching W25's non-prose skips. Blockquote
    prefixes (`> `) are stripped so a callout body's prose still counts."""
    paragraphs: list[_Paragraph] = []
    current_text: list[str] = []
    current_start: int | None = None
    in_code_fence = False

    def flush() -> None:
        nonlocal current_text, current_start
        if current_start is not None and "".join(current_text).strip():
            paragraphs.append(_Paragraph(text="".join(current_text), start_line=current_start))
        current_text = []
        current_start = None

    for file_line, line in page.body_lines():
        trimmed = line.strip()
        if trimmed.startswith("```"):
            in_code_fence = not in_code_fence
            flush()
            continue
        if in_code_fence:
            continue
        if not trimmed:
            flush()
            continue
        if trimmed.startswith("#"):
            flush()
            continue
        if trimmed.startswith("|"):
            flush()
            continue
        if _CALLOUT_OPEN_RE.match(trimmed):
            flush()
            continue

        if current_start is None:
            current_start = file_line
        current_text.append(re.sub(r"^>\s?", "", line) + "\n")
    flush()
    return paragraphs


def _count_keyword_hits(text: str, keywords: tuple[str, ...]) -> int:
    lower = text.lower()
    return sum(lower.count(keyword) for keyword in keywords)


@dataclass(slots=True)
class _NameEntry:
    count: int
    first_line: int
    keyword_hits: int
    all_sentence_initial: bool


@register
class InlineEntityDescriptionRule(FileRule):
    """Ported from npm's W77
    (`utils/scripts/lint-rules/w77-inline-entity-description.mjs`)."""

    id = "W77"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        "Extract the flagged entity's facts onto its own page via the matching "
        "*-prep skill, then replace this prose with a [[wikilink]] or section embed."
    )
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterator[Finding]:
        rel = page.rel_path
        if not rel.startswith(_SCOPED_ROOT):
            return
        if rel.startswith("vault/campaigns/shattered-sea/pcs/"):
            return
        if rel.startswith("vault/refs/"):
            return
        # Agent-guidance trees (skills, rules) are not wiki entity pages.
        if "/.claude/" in rel:
            return
        if page.frontmatter.get("status") == "srd":
            return

        page_type = page.type
        title_words = _title_words(page)
        structural_labels = _structural_labels(page)
        paragraphs = _extract_paragraphs(page)
        if not paragraphs:
            return

        config = _load_config()
        min_occurrences = _threshold_int(
            config, "ATOMICITY_MIN_NAME_OCCURRENCES", _MIN_OCCURRENCES_DEFAULT
        )
        min_hits_unresolved = _threshold_int(
            config, "ATOMICITY_MIN_KEYWORD_HITS_UNRESOLVED", _MIN_HITS_UNRESOLVED_DEFAULT
        )
        min_hits_resolved = _threshold_int(
            config, "ATOMICITY_MIN_KEYWORD_HITS_RESOLVED", _MIN_HITS_RESOLVED_DEFAULT
        )

        for candidate_type, signals in SIGNAL_SETS.items():
            if page_type == candidate_type:
                continue  # never self-flag

            names: dict[str, _NameEntry] = {}
            for para in paragraphs:
                seen_in_para: set[str] = set()
                for match in _NAME_PATTERN.finditer(para.text):
                    full = f"{match.group(1)} {match.group(2)}"
                    first_word_lower = match.group(1).lower()
                    if first_word_lower in LEADING_STOPWORDS:
                        continue
                    if full.lower() in title_words:
                        continue
                    if full.lower() in structural_labels:
                        continue
                    if _is_quote_wrapped(para.text, match.start(), match.end()):
                        continue

                    seen_in_para.add(full)
                    entry = names.get(full)
                    if entry is None:
                        entry = _NameEntry(
                            count=0,
                            first_line=para.start_line,
                            keyword_hits=0,
                            all_sentence_initial=True,
                        )
                        names[full] = entry
                    entry.count += 1
                    entry.all_sentence_initial = (
                        entry.all_sentence_initial
                        and _is_sentence_initial(para.text, match.start())
                    )

                if not seen_in_para:
                    continue
                para_hits = _count_keyword_hits(para.text, signals.keywords)
                for full in seen_in_para:
                    names[full].keyword_hits += para_hits

            for name, entry in names.items():
                if entry.count < min_occurrences:
                    continue
                if entry.all_sentence_initial:
                    continue

                resolved = corpus.resolve(name) is not None
                threshold = min_hits_resolved if resolved else min_hits_unresolved
                if entry.keyword_hits < threshold:
                    continue

                existence = (
                    "and a page already exists for it elsewhere in the vault"
                    if resolved
                    else "and no page exists for it anywhere in the vault"
                )
                yield self.finding(
                    file=rel,
                    line=entry.first_line,
                    message=(
                        f'"{name}" reads like inline description of {signals.label} — '
                        f"{entry.count} mention(s), {entry.keyword_hits} personality/backstory "
                        f"keyword hit(s) in the surrounding prose, {existence}. Extract every "
                        f'fact this page states about "{name}" into a proper page via '
                        f"{signals.guide} ({signals.template_path}), then replace the inline "
                        "prose here with a [[wikilink]] or section embed."
                    ),
                )
