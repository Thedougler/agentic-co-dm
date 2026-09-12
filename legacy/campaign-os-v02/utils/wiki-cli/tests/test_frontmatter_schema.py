"""TDD for the frontmatter-schema rule (ported from npm's W84).

Both tests build a `Page` in memory (no file on disk) and resolve its
template against the REAL `vault/_templates/` tree — the brief's own
instruction ("derive required = template frontmatter keys lacking a
`# OPTIONAL` comment, from `vault/_templates/`"), and the only way to prove
the rule matches what `_templates/_campaigns/_location/_location.md`
actually declares today, not a stub the test invents.

`owner_skill` is absent from the required-key expectations here because
every template marks it `# OPTIONAL` (ADR-0044): it carries through to an
instantiated page and is allowed on one, but a page predating that
decision must still validate without it.
"""

from __future__ import annotations

from wiki_cli.contracts import Page
from wiki_cli.rules.frontmatter_schema import FrontmatterSchemaRule

RULE_ID = "W84"

# Every required key `_templates/_campaigns/_location/_location.md` declares
# (no `# OPTIONAL`), each given a placeholder value.
_CONFORMING_LOCATION_FRONTMATTER: dict[str, object] = {
    "type": "location",
    "status": "canon",
    "publish": False,
    "aliases": [],
    "summary": "A placeholder location for the frontmatter-schema unit test.",
    "created": "2026-08-09",
    "updated": "2026-08-09",
    "tags": [],
    "tier": "supporting",
    "subtype": "building",
    "within": '"[[campaigns/shattered-sea/locations/shattered-sea]]"',
    "north_of": '"[[somewhere]]"',
    "east_of": '"[[somewhere]]"',
    "south_of": '"[[somewhere]]"',
    "west_of": '"[[somewhere]]"',
    "geography": ["coastal"],
    "uid": "c69466f8-31d5-498a-a7a6-5ccc4bf0d538",
}


def _page(rel_path: str, frontmatter: dict[str, object]) -> Page:
    return Page(
        rel_path=rel_path,
        raw="",
        frontmatter=frontmatter,
        body="# Placeholder\n",
        body_start_line=len(frontmatter) + 2,
    )


class _StubCorpus:
    """Minimal `Corpus`-shaped stand-in — this rule never calls it."""

    repo_root = None  # type: ignore[assignment]


def test_missing_required_key_yields_one_finding() -> None:
    frontmatter = dict(_CONFORMING_LOCATION_FRONTMATTER)
    del frontmatter["north_of"]
    page = _page("vault/campaigns/shattered-sea/locations/test-missing-key.md", frontmatter)

    findings = list(FrontmatterSchemaRule().check(page, _StubCorpus()))  # type: ignore[arg-type]

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == RULE_ID
    assert "north_of" in finding.message


def test_conforming_doc_yields_zero_findings() -> None:
    page = _page(
        "vault/campaigns/shattered-sea/locations/test-conforming.md",
        dict(_CONFORMING_LOCATION_FRONTMATTER),
    )

    findings = list(FrontmatterSchemaRule().check(page, _StubCorpus()))  # type: ignore[arg-type]

    assert findings == []
