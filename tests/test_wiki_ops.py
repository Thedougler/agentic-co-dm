from __future__ import annotations

from pathlib import Path


from tools.wiki_ops.index_ops import insert_index_entry, remove_index_entry, replace_index_entry
from tools.wiki_ops.identity import resolve_identity, scan_identities
from tools.wiki_ops.manifest_ops import ManifestTransition, apply_transition
from tools.wiki_ops.mutations import MutationOp, apply_mutation, parse_sections, section_hash
from tools.wiki_ops.template_contracts import check_conformance, load_contract
from tools.wiki_ops.scope import parse_scope
from tools.wiki_ops.transactions import Transaction

FIXTURE = Path(__file__).parent / "fixtures" / "wiki_ops"


def test_scope_and_semantic_sections():
    scope = parse_scope("files:fisks-fleet.md")
    assert scope and scope.resolve(FIXTURE).resolved_files == ["fisks-fleet.md"]
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    assert section_hash(section.content) == section.hash


def test_mutation_hash_and_dry_run():
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    op = MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "Changed\n"})
    preview = apply_mutation(FIXTURE, op, dry_run=True)
    assert preview["status"] == "dry_run"
    assert "Changed" not in (FIXTURE / "fisks-fleet.md").read_text()
    bad = apply_mutation(FIXTURE, MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": "bad"}, {"content": "x"}), dry_run=True)
    assert bad["status"] == "rejected"


def test_index_and_manifest_are_structured():
    text = (FIXTURE / "index.md").read_text()
    text = replace_index_entry(text, "fisks-fleet", "- [[fisks-fleet|Fisk's Fleet]]")
    text = insert_index_entry(text, "- [[another-page]]")
    assert "Fisk's Fleet" in text
    assert "another-page" in text
    assert "fisks-captains" not in remove_index_entry(text, "fisks-captains")
    data = apply_transition({}, ManifestTransition("old.md", "merged_into", "new.md"))
    assert data["page_identity_transitions"][0]["target"] == "new.md"


def test_transaction_rejects_overlapping_mutations():
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    tx = Transaction(FIXTURE)
    tx.add(MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "a"}))
    tx.add(MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "b"}))
    assert tx.commit()["status"] == "rejected"


def test_identity_fixture_is_deterministic():
    results = scan_identities(FIXTURE)
    assert [result.path for result in results] == sorted(result.path for result in results)
    assert resolve_identity(FIXTURE, "fisks-fleet.md").status == "resolved"


def test_template_contract_reports_required_sections():
    contract = load_contract(Path(__file__).parents[1] / "wiki/templates/contracts/faction.yml")
    page = "---\ntitle: Test\ntype: faction\nlifecycle: active\n---\n# Test\n"
    findings = check_conformance("test.md", page, contract)
    assert any(item["rule_id"] == "TMPL_missing_required" for item in findings)
