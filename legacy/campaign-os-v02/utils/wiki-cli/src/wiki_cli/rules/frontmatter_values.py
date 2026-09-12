"""W135 — validate governed frontmatter field values against Pydantic models.

Complements W84 (required/allowed key presence) by checking that fields which
ARE present hold values of the correct type or enum. A page whose `type:` is
unknown or missing is silently skipped — no false positives for untyped files.
"""

from __future__ import annotations

from collections.abc import Iterable

from pydantic import ValidationError

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.frontmatter_models import model_for


@register
class FrontmatterValuesRule(FileRule):
    """Validates frontmatter field values against the per-type Pydantic model."""

    id = "W135"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Set the field to a valid value — see the page's governing template under "
        "vault/_templates/ for the allowed enum values."
    )
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        page_type = page.type
        if page_type is None:
            return

        model_cls = model_for(page_type)
        if model_cls is None:
            return

        try:
            model_cls.model_validate(dict(page.frontmatter))
        except ValidationError as exc:
            for error in exc.errors():
                loc = error.get("loc", ())
                field = str(loc[0]) if loc else "unknown"
                expected = error.get("type", "")
                input_val = error.get("input")
                msg = (
                    f'Invalid frontmatter value for "{field}": '
                    f"got {input_val!r} ({expected})"
                )
                yield self.finding(
                    file=page.rel_path,
                    line=page.line_of(field),
                    message=msg,
                )
