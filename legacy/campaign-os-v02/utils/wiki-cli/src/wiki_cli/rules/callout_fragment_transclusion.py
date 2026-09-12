"""W136: performative-sibling transclusion resolution (ADR-0056).

Two checks in both directions:

Forward — every ``![[slug-narration-…]]`` / ``![[slug-dialogue-…]]``
(and leftover ``![[slug-c0N]]``) transclusion resolves to an existing file.

Orphan — every ``type: narration`` / ``type: dialogue`` page (and leftover
``-c0N`` file) has at least one parent that transcludes it.

Not pure — both checks depend on other pages, not just this file's bytes.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register

_SCOPED_PREFIX = "vault/"
_FRAGMENT_FILE_RE = re.compile(r"(?:-c\d{2,}|-narration-|-dialogue-).*\.md$")
_FRAGMENT_SLUG_RE = re.compile(r"(?:-c\d{2,}|-narration-|-dialogue-)")
_PERFORMATIVE_TYPES = frozenset({"narration", "dialogue"})
_EMBED_RE = re.compile(r"!\[\[([^\]|#]+?)(?:\|[^\]]*)?\]\]")


@register
class CalloutFragmentTransclusionRule(VaultRule):
    """Forward and orphan resolution for callout-fragment (``-c0N``) embeds."""

    id = "W136"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Add the missing narration/dialogue sibling, or remove the broken transclusion "
        "that points at it. Add a ![[slug]] embed on the parent for an orphan sibling, "
        "or delete that file."
    )
    producer = "wiki"
    pure = False
    version = "2"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        transcluded: set[str] = set()

        # Forward check: scan parent pages for callout-fragment embeds
        for page in corpus.pages():
            if not page.rel_path.startswith(_SCOPED_PREFIX):
                continue
            if _FRAGMENT_FILE_RE.search(page.rel_path) or page.type in _PERFORMATIVE_TYPES:
                continue  # skip performative siblings in the forward pass
            lines = page.raw.split("\n")
            for idx, line in enumerate(lines):
                for match in _EMBED_RE.finditer(line):
                    target = match.group(1).strip()
                    if not _FRAGMENT_SLUG_RE.search(target):
                        continue  # not a callout-fragment embed
                    resolved = corpus.resolve(target)
                    if resolved is not None:
                        transcluded.add(resolved.slug.lower())
                    else:
                        yield self.finding(
                            file=page.rel_path,
                            line=idx + 1,
                            message=(
                                f"![[{target}]] transclusion cannot resolve — "
                                "no file with that slug exists "
                                "(a missing fragment renders as a blank hole at the table)"
                            ),
                        )

        # Orphan check: performative siblings with no parent transclusion
        for page in corpus.pages():
            if not page.rel_path.startswith(_SCOPED_PREFIX):
                continue
            is_performative = (
                page.type in _PERFORMATIVE_TYPES or _FRAGMENT_FILE_RE.search(page.rel_path)
            )
            if not is_performative:
                continue
            if page.slug.lower() in transcluded:
                continue
            yield self.finding(
                file=page.rel_path,
                line=1,
                message=(
                    f"{page.rel_path} is a narration/dialogue sibling with no parent "
                    "page transcluding it — orphaned, add a ![[slug]] embed "
                    "or delete the file"
                ),
            )
