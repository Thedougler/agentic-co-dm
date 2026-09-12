"""Ported from npm's W98 (`utils/scripts/lint-rules/w98-slug-kebab-case.mjs`).

A `vault/**` page's own basename must match `^[a-z0-9]+(-[a-z0-9]+)*\\.md$`
— lowercase, hyphen-delimited, no underscores or capitals. Obsidian's
`[[bare slug]]` resolution is basename-based and case/underscore-sensitive
to the human eye but not to muscle memory: a link typed from memory in the
vault's dominant lowercase-hyphen convention silently fails to resolve
against a page whose real filename carries a capital or underscore.

Detection only — picking the exact new slug and sweeping inbound wikilinks
is this rule's suggestion, not an automatic rename.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*\.md$")
_ALLOWED_EXACT = frozenset({"CLAUDE.md", "AGENTS.md", "README.md", "GUIDE.md", "SKILL.md"})
_TRANSCRIPT_RE = re.compile(r"^transcript(\.raw)?(-.*)?\.md$")
_IGNORED_PATTERNS = (
    re.compile(r"^vault/campaigns/[^/]+/pcs/va-scripts/.*-voice-script\.md$"),
    re.compile(r"(^|/)[^/]*\.vale-fm-.*\.md$"),
    re.compile(r"(^|/)[^/]*\.vale-chunk-.*\.md$"),
    re.compile(r"(^|/)\.vale-(fm|chunk)-\d+-[^/]*/"),
)


def _suggest_slug(name: str) -> str:
    stem = re.sub(r"\.md$", "", name)
    slug = re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", stem)
    slug = slug.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", slug)
    slug = slug.strip("-")
    return f"{slug}.md"


@register
class SlugKebabCaseRule(FileRule):
    """Ported from npm's W98 (`utils/scripts/lint-rules/w98-slug-kebab-case.mjs`)."""

    id = "W98"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "Rename the file to lowercase-kebab-case and update inbound wikilinks in the same pass."
    producer = "wiki"
    pure = True
    version = "3"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus

        if not page.rel_path.startswith("vault/"):
            return

        name = Path(page.rel_path).name
        if name in _ALLOWED_EXACT:
            return
        if _TRANSCRIPT_RE.match(name):
            return
        if any(pattern.search(page.rel_path) for pattern in _IGNORED_PATTERNS):
            return
        if _SLUG_RE.match(name):
            return

        yield self.finding(
            file=page.rel_path,
            line=1,
            message=(
                f"rename this file to {_suggest_slug(name)} — Obsidian resolves "
                "[[bare slugs]] by basename and a capital or underscore here breaks "
                "links written from muscle memory; update inbound wikilinks in the "
                "same pass"
            ),
        )
