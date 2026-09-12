"""Ported from npm's W114 (`utils/scripts/lint-rules/w114-operative-transclusion.mjs`).

A session scene (`scene-<N>-<slug>.md`) or moment (`moment-<N>-<slug>.md`,
ADR-0026) that references a sibling `type: encounter` page must
`![[page#Heading]]`-embed every operative heading that page carries, so the
beat runs cold with no mid-round lookup hop (vault/refs/runbook-wiki.md §
Operative-mechanics ownership; ADR-0025). The operative-heading list is
`OPERATIVE_HEADINGS` (`wiki.toml` `[thresholds]`); only headings the
encounter page actually carries are required. Detection only — placing
each embed where the beat spends those numbers is judgment (draft-moment
Hard Rule 7).

Not pure — resolving a sibling encounter page needs the corpus.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_EPISODES_SEGMENT_RE = re.compile(r"^vault/episodes/[^/]+/")
_AT_TABLE_BASENAME_RE = re.compile(r"^(scene|moment)-\d+-.+\.md$")
_WIKILINK_RE = re.compile(r"(!?)\[\[([^\]|#]+)(?:#([^\]|]+))?(?:\|[^\]]*)?\]\]")
_SOURCE_DOC = "vault/refs/runbook-wiki.md § Operative-mechanics ownership"


def _h2_headings(page: Page) -> list[str]:
    return [text[3:].strip() for _, text in page.body_lines() if text.startswith("## ")]


@register
class OperativeTransclusionRule(FileRule):
    """Ported from npm's W114 (`w114-operative-transclusion.mjs`)."""

    id = "W114"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.ERROR
    fix = (
        "Add ![[<encounter-page>#<Heading>]] embedding every operative heading the "
        "sibling encounter page carries, where the beat spends those numbers."
    )
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path
        if not _EPISODES_SEGMENT_RE.match(rel):
            return
        if not _AT_TABLE_BASENAME_RE.match(rel.rsplit("/", 1)[-1]):
            return

        operative = [
            h.strip() for h in load_config().threshold_list("OPERATIVE_HEADINGS") if h.strip()
        ]
        if not operative:
            return

        directory = rel.rsplit("/", 1)[0]
        own_base = page.slug
        pages_by_path = {p.rel_path: p for p in corpus.pages()}

        siblings: dict[str, Page] = {}
        first_ref_line: dict[str, int] = {}
        embedded: dict[str, set[str]] = {}

        lines = page.raw.split("\n")
        for i, line in enumerate(lines):
            for match in _WIKILINK_RE.finditer(line):
                bang, target, heading = match.group(1), match.group(2).strip(), match.group(3)
                base = target.rsplit("/", 1)[-1]
                if not base or base == own_base:
                    continue

                sibling = siblings.get(base)
                if sibling is None:
                    candidate = pages_by_path.get(f"{directory}/{base}.md")
                    if candidate is None or candidate.type != "encounter":
                        continue
                    siblings[base] = candidate

                if base not in first_ref_line:
                    first_ref_line[base] = i + 1
                if bang == "!" and heading:
                    embedded.setdefault(base, set()).add(heading.strip().lower())

        for base, sibling in siblings.items():
            page_headings = _h2_headings(sibling)
            required = [
                h for h in operative if any(ph.lower() == h.lower() for ph in page_headings)
            ]
            have = embedded.get(base, set())
            for heading in required:
                if heading.lower() in have:
                    continue
                yield self.finding(
                    file=rel,
                    line=first_ref_line[base],
                    message=(
                        f'references sibling encounter page "{base}" but never embeds its § '
                        f"{heading} — add ![[{base}#{heading}]] where the beat spends those "
                        f"numbers ({_SOURCE_DOC})"
                    ),
                )
