"""Ported from npm's W80 (`utils/scripts/lint-rules/w80-skill-trigger-overlap.mjs`).

Two skill descriptions whose significant (non-stopword) tokens overlap
heavily are very likely the same trigger branch spelled out twice across
two skill files — a router or the model itself can't reliably pick between
them, and every duplicated word bills context load twice for one decision
(writing-for-agents's "One trigger per branch. Synonyms that rename a
single branch are duplication — collapse them; keep only genuinely
distinct branches").

A `VaultRule`: the comparison needs every reachable SKILL.md at once, not
one page at a time, and a skill can live anywhere under the repo
(`.claude/skills/`, `vault/**/.claude/skills/`, `utils/wiki-cli/.claude/
skills/`), not only under the vault-scoped page index — so this rule walks
`corpus.repo_root` directly, the same `IGNORE_DIRS`-skipping walk the
legacy module runs, independent of `corpus.pages()`.

Threshold tuned against this repo's real skill corpus (legacy module
docstring, 2026-08-01): Jaccard similarity of description tokens showed a
clean break between genuine near-duplicates and adjacent-but-distinct
skills at 0.35, with a minimum-shared-token floor of 12 to keep two short,
generically-worded descriptions from tripping the threshold on coincidence.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register
from wiki_cli.markdown import load_page

_SKILL_PATH_RE = re.compile(r"(^|/)\.claude/skills/[^/]+/SKILL\.md$")
_IGNORE_DIRS = frozenset({"node_modules", ".git", ".obsidian", "raw", "inbox", "utils"})

_STOPWORDS_SOURCE = (
    "the a an and or but if when to for of in on at by from with as is are "
    "was were be been being this that these those it its it's you your use "
    "uses used using want wants asks asked mentions mentioned names named "
    "not never always about into over under between across per own other "
    "another same each every any all no yes do does did done also so such "
    "will campaign os repo present content skill skills task tasks file "
    "files page pages agent agents"
)
_STOPWORDS = frozenset(_STOPWORDS_SOURCE.split())

_TOKEN_STRIP_RE = re.compile(r"[`*_()\[\]{}]")
_TOKEN_SPLIT_RE = re.compile(r"[^a-z0-9-]+")


def _tokenize(description: str) -> frozenset[str]:
    cleaned = _TOKEN_STRIP_RE.sub(" ", description.lower())
    return frozenset(
        word
        for word in _TOKEN_SPLIT_RE.split(cleaned)
        if len(word) >= 3 and word not in _STOPWORDS
    )


def _walk_skills(repo_root: Path) -> list[str]:
    """Every `.claude/skills/<name>/SKILL.md` reachable from `repo_root`
    (repo-root-relative paths), skipping `_IGNORE_DIRS` and any dotdir
    other than `.claude` — same walk as the legacy module's `walk()`."""
    found: list[str] = []

    def _walk(directory: Path) -> None:
        try:
            entries = sorted(directory.iterdir())
        except OSError:
            return
        for entry in entries:
            name = entry.name
            if name.startswith(".") and name != ".claude":
                continue
            if name in _IGNORE_DIRS:
                continue
            if entry.is_dir():
                _walk(entry)
            elif name == "SKILL.md":
                rel = str(entry.relative_to(repo_root))
                if _SKILL_PATH_RE.search("/" + rel):
                    found.append(rel)

    _walk(repo_root)
    return found


def _build_index(repo_root: Path) -> dict[str, tuple[frozenset[str], int]]:
    """rel_path -> (trigger tokens, the description key's file line)."""
    index: dict[str, tuple[frozenset[str], int]] = {}
    for rel in _walk_skills(repo_root):
        page = load_page(repo_root, rel)
        description = page.frontmatter.get("description")
        if not isinstance(description, str):
            continue
        tokens = _tokenize(description)
        if tokens:
            index[rel] = (tokens, page.line_of("description"))
    return index


def _jaccard(a: frozenset[str], b: frozenset[str]) -> tuple[float, int]:
    intersection = len(a & b)
    union = len(a) + len(b) - intersection
    return (0.0 if union == 0 else intersection / union, intersection)


@register
class SkillTriggerOverlapRule(VaultRule):
    """Ported from npm's W80 (`utils/scripts/lint-rules/w80-skill-trigger-overlap.mjs`)."""

    id = "W80"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Collapse to one skill's branch, or diverge the wording to the "
        "concrete case each skill actually owns "
        '(writing-for-agents\'s "One trigger per branch").'
    )
    producer = "wiki"
    pure = False
    """Depends on every other skill in the repo, not just this file's own
    bytes."""
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        index = _build_index(corpus.repo_root)
        if not index:
            return

        config = load_config()
        threshold = float(config.threshold("SKILL_TRIGGER_OVERLAP_THRESHOLD"))
        min_shared = int(config.threshold("SKILL_TRIGGER_OVERLAP_MIN_SHARED"))

        for rel_path in sorted(index):
            own_tokens, line = index[rel_path]
            for other_rel, (other_tokens, _other_line) in index.items():
                if other_rel == rel_path:
                    continue
                similarity, intersection = _jaccard(own_tokens, other_tokens)
                if similarity < threshold or intersection < min_shared:
                    continue

                yield self.finding(
                    file=rel_path,
                    line=line,
                    message=(
                        f"description shares {intersection} trigger tokens with "
                        f"{other_rel} (similarity {similarity:.2f}, threshold "
                        f"{threshold:g}) — near-duplicate phrasing across two "
                        "skills means a router or the model can't reliably tell "
                        "the branches apart; collapse to one skill's branch or "
                        "diverge the wording to the concrete case each skill "
                        "actually owns, per `~/.claude/skills/writing-for-agents/"
                        'SKILL.md` (§ Context pointers: "One trigger per branch") '
                        "(threshold: wiki.toml [thresholds] "
                        "SKILL_TRIGGER_OVERLAP_THRESHOLD)"
                    ),
                )
