"""A `vault/**` page's frontmatter still carries its type template's
instructional comments (rule id `W127`).

`vault/_templates/` comments tell an author what a key means and which
values are legal (`# OPTIONAL — true | false; true when the session ends
here`). They are instantiation scaffolding: once the key holds a real
value the comment states nothing about this page, and every later reader
and every agent Read pays for it. W90 catches the same leak in the body;
frontmatter is this rule's half.

Templates themselves are the source of those comments, so `_templates/`
is exempt.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.autofix import current_context
from wiki_cli.contracts import (
    Autofix,
    Corpus,
    FileRule,
    Finding,
    Page,
    Severity,
    Tier,
    register,
)
from wiki_cli.markdown import split_frontmatter

_QUOTED_RE = re.compile(r"'[^']*'|\"[^\"]*\"")
"""Quoted scalars are masked before the comment scan: a `#` inside a value
(`summary: "the #1 rule"`, a `tags:` entry) is data, never a comment."""

_COMMENT_RE = re.compile(r"(?:^|\s)#")


def _comment_column(line: str) -> int | None:
    """1-indexed column of the line's YAML comment marker, or None.

    Quoted spans are blanked (length preserved) so the column still points
    at the real character in the original line.
    """
    masked = _QUOTED_RE.sub(lambda match: " " * len(match.group(0)), line)
    found = _COMMENT_RE.search(masked)
    if found is None:
        return None
    return masked.index("#", found.start()) + 1


def _strip_frontmatter_comments(text: str) -> str:
    """Every YAML comment cut from the frontmatter block.

    A line left with only its key and value keeps that value; a line that
    was nothing but a comment goes entirely. The body is never read, and
    `_comment_column`'s quote masking is what keeps a `#` inside a value
    (`summary: "the #1 rule"`) out of reach.
    """
    context = current_context()
    if context is None:
        return text
    rel_path = context.rel_path
    if not rel_path.startswith("vault/") or "_templates/" in rel_path:
        return text

    fm_text, _body, body_start_line = split_frontmatter(text)
    if fm_text is None or body_start_line <= 1:
        return text

    lines = text.split("\n")
    kept: list[str] = []
    for index, line in enumerate(lines):
        if index >= body_start_line - 1:
            kept.append(line)
            continue
        column = _comment_column(line)
        if column is None:
            kept.append(line)
            continue
        remainder = line[: column - 1].rstrip()
        if remainder:
            kept.append(remainder)
    return "\n".join(kept)


@register
class TemplateFrontmatterCommentRule(FileRule):
    """Instructional template comments left in a real page's frontmatter."""

    id = "W127"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Delete the comment from the frontmatter line — it is template "
        "scaffolding explaining the key, not a fact about this page. The "
        "explanation stays in vault/_templates/, which is where an author "
        "reads it."
    )
    producer = "wiki"
    pure = True
    fixable = True
    version = "1"
    autofix = Autofix(scope="frontmatter", apply=_strip_frontmatter_comments)

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus

        if not page.rel_path.startswith("vault/"):
            return
        if "_templates/" in page.rel_path:
            return
        if page.body_start_line <= 1:
            return  # no frontmatter block

        # Frontmatter occupies lines 1 .. body_start_line - 1, opening and
        # closing `---` included; both are skipped by the comment scan.
        frontmatter_lines = page.raw.splitlines()[: page.body_start_line - 1]

        for offset, line in enumerate(frontmatter_lines):
            column = _comment_column(line)
            if column is None:
                continue
            yield self.finding(
                file=page.rel_path,
                line=offset + 1,
                column=column,
                message=(
                    "Template comment left in frontmatter — delete it; the key's "
                    "explanation belongs in vault/_templates/, not on a page a DM "
                    "reads"
                ),
            )
