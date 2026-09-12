"""W112 — `docs/tags.md` itself fails to parse as a well-formed tag
taxonomy. Ported from `utils/scripts/lint-rules/w112-tag-taxonomy-doc.mjs`.

Fires only on `docs/tags.md` itself — every other file's tag findings
belong to W111 (missing Domain tag) or W113 (alias, not canonical), never
this rule. Each of `wiki_cli.tags`'s parse issues (C1-C5) becomes one
finding; only C2 (an exact duplicate bullet) is mechanical enough to mark
`fixable` — C1/C3/C4/C5 are content judgments.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.tags import Taxonomy, default_taxonomy_path

if TYPE_CHECKING:
    from collections.abc import Iterable
    from pathlib import Path

_TAGS_DOC_REL_PATH = "docs/tags.md"


def _is_tags_doc(rel_path: str) -> bool:
    normalised = rel_path.replace("\\", "/")
    return normalised == _TAGS_DOC_REL_PATH or normalised.endswith(f"/{_TAGS_DOC_REL_PATH}")


@register
class TagTaxonomyDocRule(FileRule):
    """Ported from npm's W112 (`w112-tag-taxonomy-doc.mjs`)."""

    id = "W112"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Fix docs/tags.md at this line: rejoin the heading, delete the duplicate, "
        "repoint the alias, or reword the bullet."
    )
    producer = "wiki"
    fixable = True
    pure = False
    """Reads docs/tags.md from disk, independent of the checked page's own bytes."""
    version = "1"

    def __init__(self, taxonomy_path: Path | None = None) -> None:
        self._taxonomy_path_override = taxonomy_path

    def _resolve_taxonomy_path(self) -> Path:
        if self._taxonomy_path_override is not None:
            return self._taxonomy_path_override
        return default_taxonomy_path(load_config())

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if not _is_tags_doc(page.rel_path):
            return

        taxonomy = Taxonomy.load(self._resolve_taxonomy_path())
        for issue in taxonomy.issues:
            yield self.finding(
                file=page.rel_path,
                line=issue.line,
                message=issue.message,
                fixable=issue.code == "C2",
            )
