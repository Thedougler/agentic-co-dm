"""TDD for `wiki/backlink-symmetry` (wiki-lint migration plan Task 30) — a
new VaultRule with no npm parity. Fixtures live under
`tests/fixtures/backlink_symmetry/vault/`, built through a real `VaultIndex`
so every case exercises actual corpus link resolution.
"""

from __future__ import annotations

from pathlib import Path

import wiki_cli.rules  # noqa: F401  side-effect: registers every rule
from wiki_cli.contracts import Finding, registry
from wiki_cli.index import VaultIndex

FIXTURES = Path(__file__).parent / "fixtures" / "backlink_symmetry"

RULE_ID = "wiki/backlink-symmetry"


def _corpus() -> VaultIndex:
    return VaultIndex.build(FIXTURES, FIXTURES / "vault", ("vault",))


def _findings() -> list[Finding]:
    rule = registry()[RULE_ID]
    return list(rule.check(_corpus()))


def test_within_with_backlink_stays_silent() -> None:
    findings = [f for f in _findings() if f.file == "vault/container-linked.md"]
    assert findings == []


def test_parent_without_backlink_fires_on_the_container() -> None:
    findings = [f for f in _findings() if f.file == "vault/container-unlinked-parent.md"]

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == RULE_ID
    assert finding.severity == "warning"
    assert "[[child-parent-unlinked]]" in finding.message
    assert "parent:" in finding.message
    assert "never links back" in finding.message


def test_within_without_backlink_fires_on_the_container() -> None:
    findings = [f for f in _findings() if f.file == "vault/container-unlinked-within.md"]

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == RULE_ID
    assert "[[child-within-unlinked]]" in finding.message
    assert "within:" in finding.message


def test_missing_target_page_stays_silent() -> None:
    # child-missing-target.md declares parent: [[no-such-page]], which does
    # not resolve to any page in the corpus — nothing to check symmetry
    # against, so no finding should fire for it anywhere.
    findings = [f for f in _findings() if "child-missing-target" in f.message]
    assert findings == []


def test_rule_is_registered_warning_content_shape() -> None:
    rule = registry()[RULE_ID]
    assert rule.severity == "warning"
    assert rule.tier == "content-shape"
    assert rule.pure is False
