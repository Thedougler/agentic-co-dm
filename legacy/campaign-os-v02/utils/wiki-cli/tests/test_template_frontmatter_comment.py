"""TDD for W127 (template-frontmatter-comment).

Every fixture is a real file on disk under
`fixtures/template_frontmatter_comment/`, loaded through the real
`load_page` parser, matching `test_frontmatter_hygiene.py`'s convention.
Fixture rel_paths start with `vault/`, which the rule's own scope check
requires.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  import-for-side-effect: registers every rule
from wiki_cli.contracts import registry
from wiki_cli.markdown import load_page

FIXTURES = Path(__file__).parent / "fixtures" / "template_frontmatter_comment"


def check(fixture: str):
    rule = registry()["W127"]
    page = load_page(FIXTURES, fixture)
    return list(rule.check(page, None))


def test_flags_each_template_comment_left_in_frontmatter() -> None:
    findings = check("vault/campaigns/leaky.md")
    assert [finding.line for finding in findings] == [4, 5]


def test_finding_points_at_the_hash_column() -> None:
    tier_finding = check("vault/campaigns/leaky.md")[0]
    line = (FIXTURES / "vault/campaigns/leaky.md").read_text().splitlines()[3]
    assert line[tier_finding.column - 1] == "#"


def test_hash_inside_a_quoted_value_is_data_not_a_comment() -> None:
    assert check("vault/campaigns/clean.md") == []


def test_templates_keep_their_own_comments() -> None:
    assert check("vault/_templates/_moment.md") == []
