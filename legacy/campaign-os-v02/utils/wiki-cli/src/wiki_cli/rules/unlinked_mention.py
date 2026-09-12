"""Ported from npm's W25 (`utils/scripts/lint-rules/w25-unlinked-mention.mjs`),
sharing its detection engine (legacy `lib/unlinkedMentionScan.mjs`) with W122
(`narrative_unlinked_mention.py`, which imports `scan_unlinked_mentions` from
here).

Page prose names an entity that resolves via another page's slug,
frontmatter `aliases:`, or H1 title (case- and diacritic-insensitive) but
never `[[wikilinks]]` it anywhere on the page — soft, DETECTION only. The fix
is a judgment call (the `cross-linker` skill resolves the finding); this rule
never inserts a link itself.

Exclusions ported verbatim from the legacy module/scan engine:
- `vault/srd/rules/` pages with `status: srd` are excluded as scan-index
  entries (link *targets*) unless their slug is on
  `UNLINKED_MENTION_ALLOWLIST` — the SRD rules glossary titles ordinary
  English words that would false-positive on every prose use.
- `vault/ideas/` pages are pre-canon raw material, never a real cross-link
  target — nor can one shadow a landed page's own slug/alias/title in the
  existing-wikilink resolution `_ScanIndex.raw_index` uses, even though it
  still resolves normally when no landed page shares its name.
- `type: table` pages are open-ended GM prompts, not entity references.
- `UNLINKED_MENTION_STOPLIST` holds campaign-side names too generic to
  auto-flag; both lists come from `config.threshold_list(...)`, never
  hard-coded here.

Not pure — the finding depends on every other page in the corpus, not just
this file's own bytes.
"""

from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterator
from dataclasses import dataclass

from wiki_cli.config import Config
from wiki_cli.config import load_config as _load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_MIN_NAME_LEN = 4  # same substring-match floor W17 already uses
_VALE_TEMP_RE = re.compile(r"\.vale-(fm|chunk)-")
_COMBINING_MARKS_RE = re.compile("[̀-ͯ]")  # NFKD combining diacritics

_WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
_CODE_SPAN_RE = re.compile(r"`[^`]*`")
_CALLOUT_OPEN_RE = re.compile(r"^>\s*\[!")
_TABLE_SEPARATOR_RE = re.compile(r"^\s*\|[\s|:-]+\|\s*$")
_HAS_CAPITAL_RE = re.compile(r"[A-Z]")
_ADJACENT_CAPITAL_AFTER_RE = re.compile(r"^[\s-]+[A-Z]")
_ADJACENT_CAPITAL_BEFORE_RE = re.compile(r"[A-Z][a-z]*(?:['’]s)?[\s-]+$")
_H1_RE = re.compile(r"^#\s+(.+?)\s*$")


def _fold_diacritics(text: str) -> str:
    return _COMBINING_MARKS_RE.sub("", unicodedata.normalize("NFKD", text))


def _normalize(text: str) -> str:
    return _fold_diacritics(text).lower()


def _aliases_of(page: Page) -> list[str]:
    raw = page.frontmatter.get("aliases")
    if isinstance(raw, list):
        return [item for item in raw if isinstance(item, str)]
    return []


def _title_of(page: Page) -> str | None:
    fm_title = page.frontmatter.get("title")
    if isinstance(fm_title, str) and fm_title.strip():
        return fm_title.strip()
    for _, line in page.body_lines():
        match = _H1_RE.match(line)
        if match:
            return match.group(1).strip()
    return None


@dataclass(frozen=True, slots=True)
class Mention:
    line: int
    name: str
    target_rel_path: str


@dataclass(frozen=True, slots=True)
class _ScanIndex:
    regex: re.Pattern[str] | None
    by_norm_name: dict[str, tuple[str, Page]]
    raw_index: dict[str, Page]
    """legacy `loadVaultIndex()`'s own Map: every candidate name, plainly
    lowercased (unfiltered, un-deduped-by-normalization) -> its last-write
    winning page, EXCEPT a `vault/ideas/` page never overwrites a real
    (non-`vault/ideas/`) page already holding that name — matching
    `by_norm_name`'s own exclusion of `vault/ideas/` as a resolution target,
    below. An idea page with no landed collision still resolves normally.
    `by_norm_name` is a filtered *subset* derived from this, but an existing
    `[[wikilink]]`'s target must resolve through this same raw map — not
    `corpus.resolve()`'s different alias/title precedence, and not the
    filtered subset — or "is this name already linked elsewhere on the
    page" can disagree with "which page does this bare mention name," even
    though both questions are about the exact same name string."""


def _build_scan_index(corpus: Corpus, config: Config) -> _ScanIndex:
    stoplist = {
        item.strip().lower()
        for item in config.threshold_list("UNLINKED_MENTION_STOPLIST")
        if item.strip()
    }
    allowlist = {
        item.strip().lower()
        for item in config.threshold_list("UNLINKED_MENTION_ALLOWLIST")
        if item.strip()
    }

    # legacy `loadVaultIndex()` builds one Map<lowercased-name, page> via
    # plain overwrite (JS `Map.set`) over every page's
    # [slug, *aliases, title], walked in vault-relative-path order — a
    # later page's same-named candidate silently overwrites an earlier
    # one. Two pages CAN legitimately share a display name (this vault has
    # both `campaigns/shattered-sea/monsters/whip-shark.md` aliased "Whip
    # Shark" and `srd/monsters/whip-shark-statblock.md` titled "Whip
    # Shark"; both a `lore` and a `location` page alias "Antheri"), and
    # legacy's answer for "which page does that name mean" is simply
    # whichever page was walked last, not a considered precedence.
    # `corpus.pages()` iterates in the same sorted-by-relative-path order
    # `VaultIndex.build()` walks the vault in, so reproducing that exact
    # last-write-wins overwrite here — instead of trusting whichever page
    # happens to be visited first, or re-deriving a different answer via
    # `corpus.resolve()`'s own alias/title precedence — matches legacy's
    # answer for every such collision (confirmed against the real vault:
    # both examples above false-positived under a first-write-wins or a
    # `corpus.resolve()`-precedence rebuild, and only last-write-wins in
    # path order agrees with the npm engine on both) — with one exception
    # legacy never had to handle: a `vault/ideas/` page (pre-canon scratch
    # material, routinely reusing a landed page's own slug once that idea
    # ships as real content) must never win this overwrite against a real
    # page also holding the name, regardless of which sorts later in path
    # order, or an existing wikilink from the idea page can resolve to
    # itself instead of the landed page.
    raw_index: dict[str, Page] = {}
    raw_index_is_idea: dict[str, bool] = {}  # same key -> is current winner a vault/ideas/ page
    display_names: dict[str, str] = {}  # plain-lowercase name -> last-seen original casing
    for page in corpus.pages():
        if not page.rel_path.endswith(".md"):
            continue
        is_idea = page.rel_path.startswith("vault/ideas/")
        title = _title_of(page)
        for candidate in (page.slug, *_aliases_of(page), *([title] if title else [])):
            lower = candidate.lower()
            # vault/ideas/ pages are pre-canon raw material (see by_norm_name's
            # own exclusion below) — an idea page must never shadow a landed
            # page's own slug/alias/title collision here, even though it may
            # be walked later in path order. It still resolves normally when
            # it is the only page holding that name (no real collision).
            if lower in raw_index and not raw_index_is_idea[lower] and is_idea:
                continue
            raw_index[lower] = page
            raw_index_is_idea[lower] = is_idea
            display_names[lower] = candidate

    by_norm_name: dict[str, tuple[str, Page]] = {}
    for lower_name, winner in raw_index.items():
        if len(lower_name) < _MIN_NAME_LEN:
            continue
        if _VALE_TEMP_RE.search(winner.slug):
            continue
        if (
            winner.rel_path.startswith("vault/srd/rules/")
            and winner.frontmatter.get("status") == "srd"
            and winner.slug.lower() not in allowlist
        ):
            continue
        if winner.rel_path.startswith("vault/ideas/"):
            continue
        if winner.type == "table":
            continue
        if lower_name in stoplist:
            continue

        norm = _normalize(display_names[lower_name])
        if norm not in by_norm_name:
            by_norm_name[norm] = (display_names[lower_name], winner)

    if not by_norm_name:
        return _ScanIndex(regex=None, by_norm_name=by_norm_name, raw_index=raw_index)

    # Longer/more-specific names first so a shared prefix keeps its own
    # entry when the alternation matches greedily left-to-right.
    names_by_len = sorted(by_norm_name.keys(), key=len, reverse=True)
    pattern = (
        r"(?<![A-Za-z0-9])(?:"
        + "|".join(re.escape(name) for name in names_by_len)
        + r")(?![A-Za-z0-9])"
    )
    return _ScanIndex(regex=re.compile(pattern), by_norm_name=by_norm_name, raw_index=raw_index)


# Single-slot cache scoped to the most recently seen corpus — mirrors the
# legacy engine's per-process module cache. One `wiki lint` run builds one
# `VaultIndex` and reuses it for every file's `check()` call, so this hits
# on every file after the first; a different corpus (a new run, or a new
# fixture `VaultIndex` in tests) simply rebuilds once and replaces the slot.
_scan_index_cache: tuple[Corpus, _ScanIndex] | None = None


def _get_scan_index(corpus: Corpus, config: Config) -> _ScanIndex:
    global _scan_index_cache
    if _scan_index_cache is not None and _scan_index_cache[0] is corpus:
        return _scan_index_cache[1]
    built = _build_scan_index(corpus, config)
    _scan_index_cache = (corpus, built)
    return built


def scan_unlinked_mentions(page: Page, corpus: Corpus, config: Config) -> Iterator[Mention]:
    """`rel`-scoping is the caller's job (each rule gates its own path
    scope before calling in). Shared by W25 and W122."""
    index = _get_scan_index(corpus, config)
    if index.regex is None:
        return

    self_slug = page.slug
    self_norm = _normalize(self_slug)
    self_norm_spaced = _normalize(self_slug.replace("-", " "))

    linked_targets: set[str] = set()
    raw_unescaped = page.raw.replace("\\|", "|")
    for match in _WIKILINK_RE.finditer(raw_unescaped):
        target = match.group(1).split("/")[-1].strip()
        target = target.split("#", 1)[0]
        # Resolved through the same raw name index the scan candidates come
        # from (not `corpus.resolve()`'s different alias/title precedence)
        # so "already linked" and "this bare mention means page X" can
        # never disagree about the same name string.
        resolved = index.raw_index.get(_normalize(target))
        if resolved is not None:
            linked_targets.add(resolved.rel_path)

    reported_targets = set(linked_targets)

    lines = page.body.split("\n")
    in_code_fence = False
    for offset, line in enumerate(lines):
        file_line = page.body_start_line + offset
        trimmed = line.strip()

        if trimmed.startswith("```"):
            in_code_fence = not in_code_fence
            continue
        if in_code_fence:
            continue
        if trimmed.startswith("#"):
            continue
        if _CALLOUT_OPEN_RE.match(trimmed):
            continue
        next_line = lines[offset + 1] if offset + 1 < len(lines) else ""
        if trimmed.startswith("|") and _TABLE_SEPARATOR_RE.match(next_line):
            continue

        stripped = _WIKILINK_RE.sub("", line)
        stripped = _CODE_SPAN_RE.sub("", stripped)
        folded_cased = _fold_diacritics(stripped)
        folded_lower = folded_cased.lower()

        for match in index.regex.finditer(folded_lower):
            found = index.by_norm_name.get(match.group(0))
            if found is None:
                continue
            name, target_page = found
            norm_name = match.group(0)
            if norm_name in (self_norm, self_norm_spaced):
                continue
            if target_page.rel_path == page.rel_path:
                continue
            if target_page.rel_path in reported_targets:
                continue
            if target_page.rel_path.rsplit("/", 1)[-1] in ("CLAUDE.md", "AGENTS.md"):
                # Instruction files are process, never mention targets.
                continue

            matched_span = folded_cased[match.start() : match.end()]
            words = matched_span.split()
            capital_check_span = " ".join(words[1:]) if len(words) > 1 else matched_span
            if not _HAS_CAPITAL_RE.search(capital_check_span):
                continue

            after = folded_cased[match.end() :]
            before = folded_cased[: match.start()]
            if _ADJACENT_CAPITAL_AFTER_RE.match(after):
                continue
            if _ADJACENT_CAPITAL_BEFORE_RE.search(before):
                continue
            if before.rstrip().endswith("§"):
                # A "§ Heading" reference names a section of the file cited
                # beside it, not an entity.
                continue
            if f"{matched_span}: `" in _fold_diacritics(line):
                # A "Label: `path`" line labels a path reference, not an
                # entity.
                continue

            reported_targets.add(target_page.rel_path)
            yield Mention(line=file_line, name=name, target_rel_path=target_page.rel_path)


_EXEMPT_ROOTS = (
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
)
_EXEMPT_FILES = ("vault/campaigns/shattered-sea/dm-voice-script.md",)


@register
class UnlinkedMentionRule(FileRule):
    """Ported from npm's W25 (`utils/scripts/lint-rules/w25-unlinked-mention.mjs`)."""

    id = "W25"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = "Wikilink the first natural mention: [[target-slug|Display Text]]."
    producer = "wiki"
    pure = False
    version = "4"

    def check(self, page: Page, corpus: Corpus) -> Iterator[Finding]:
        rel = page.rel_path
        if not rel.startswith("vault/"):
            return
        if any(rel.startswith(root) for root in _EXEMPT_ROOTS):
            return
        if rel in _EXEMPT_FILES:
            return
        # Instruction files are process, not wiki prose — no wikilink duty.
        if rel.rsplit("/", 1)[-1] == "CLAUDE.md":
            return
        if page.type == "table":
            return

        config = _load_config()
        for mention in scan_unlinked_mentions(page, corpus, config):
            yield self.finding(
                file=rel,
                line=mention.line,
                message=(
                    f'"{mention.name}" resolves to {mention.target_rel_path} but is never '
                    "[[wikilinked]] on this page"
                ),
            )
