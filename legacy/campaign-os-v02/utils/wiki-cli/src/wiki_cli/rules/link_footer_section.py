"""A trailing "See Also"/"Related"/"Sources"/"Further Reading" heading on a
page, ported from `utils/scripts/lint-rules/w123-link-footer-section.mjs`
(rule id `W123`, see `parity.py`) — a stale pattern per DM directive
2026-08-04 (`docs/adr/0035`), widened 2026-08-09.

The HEADING is the violation, whatever its body looks like. Every link
under one either earns a place in the page's body prose or doesn't merit
being linked at all — a footer is neither, and rewriting a link dump as a
citation sentence while keeping the heading is not a fix (that dodge is
exactly what the 2026-08-09 widening closed). A section with no body at
all is left to W38 (empty heading), which owns that defect and reports it
better.

Detection is pure text: which headings count comes from the
`LINK_FOOTER_HEADINGS` threshold alone, matched case-insensitively against
each heading's text with any trailing ATX closing sequence (`## Related
##`) stripped.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
_LEADING_HASHES_RE = re.compile(r"^#{1,6}\s+")
_TRAILING_HASHES_RE = re.compile(r"\s+#{1,6}\s*$")

_SCOPED_PREFIXES = ("vault/", "pcs/")
_EXCLUDED_PREFIXES = (
    "vault/_",
    "sys/",
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
)


def _heading_text(line: str) -> str:
    """Heading text with a trailing ATX closing sequence (`## Related ##`) stripped."""
    stripped = _LEADING_HASHES_RE.sub("", line)
    return _TRAILING_HASHES_RE.sub("", stripped).strip()


@register
class LinkFooterSectionRule(FileRule):
    """Ported from npm's W123 (`utils/scripts/lint-rules/w123-link-footer-section.mjs`)."""

    id = "W123"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        "Move each link into the sentence in the body that already talks "
        "about that thing; drop any link no sentence needs, then delete the "
        "heading. Rewriting the list as a citation sentence and keeping the "
        "heading is not a fix."
    )
    producer = "wiki"
    pure = True
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel_path = page.rel_path
        if not any(rel_path.startswith(prefix) for prefix in _SCOPED_PREFIXES):
            return
        if any(rel_path.startswith(prefix) for prefix in _EXCLUDED_PREFIXES):
            return
        if page.type == "table":
            return

        footer_headings = {
            heading.strip().lower()
            for heading in load_config().threshold("LINK_FOOTER_HEADINGS").split(",")
            if heading.strip()
        }
        if not footer_headings:
            return

        lines = page.body.splitlines()
        for index, line in enumerate(lines):
            match = _HEADING_RE.match(line)
            if not match:
                continue
            if _heading_text(line).lower() not in footer_headings:
                continue
            level = len(match.group(1))

            end = len(lines)
            for lookahead in range(index + 1, len(lines)):
                next_match = _HEADING_RE.match(lines[lookahead])
                if next_match and len(next_match.group(1)) <= level:
                    end = lookahead
                    break

            body_lines = lines[index + 1 : end]
            if not any(body_line.strip() for body_line in body_lines):
                continue  # W38 owns the empty-heading case

            yield self.finding(
                file=page.rel_path,
                line=page.body_start_line + index,
                message=(
                    f'"{_heading_text(line)}" is a link-footer section — this heading '
                    "does not belong on a page. Move each link into the sentence in the "
                    "body that already talks about that thing; drop any link no sentence "
                    "needs, then delete the heading. Rewriting the list as a citation "
                    "sentence and keeping the heading is not a fix."
                ),
            )
