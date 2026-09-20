from __future__ import annotations

import json
import subprocess
from pathlib import Path


import pytest

from tools.creative_lint.bundles import BundleRegistry
from tools.creative_lint.engine import LintEngine
from tools.creative_lint.finding import Finding
from tools.creative_lint.registry import Registry, RuleDefinition
from tools.creative_lint.severity import min_severity, status_from_findings
from tools.creative_lint.shadow import ShadowRecorder
from tools.creative_lint.vale_adapter import map_vale_output
from tools.creative_lint.waivers import WaiverRegistry

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "creative_lint"


def test_registry_loads_and_exposes_stable_ids():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    assert "AGENCY001" in registry.all_ids()
    assert registry.get("AGENCY001").category == "agency"
    assert registry.by_category("agency")
    assert registry.by_evaluator("vale")
    assert not registry.validate()


def test_registry_rejects_duplicate_and_invalid_rules(tmp_path):
    path = tmp_path / "registry.yml"
    path.write_text("rules:\n  - id: BAD\n    title: bad\n    category: agency\n    scope: content\n    severity: BLOCK\n    evaluator: symbolic\n    lifecycle: ACTIVE\n    message: bad\n  - id: BAD\n    title: duplicate\n    category: agency\n    scope: content\n    severity: BLOCK\n    evaluator: symbolic\n    lifecycle: ACTIVE\n    message: duplicate\n", encoding="utf-8")
    with pytest.raises(ValueError, match="invalid rule ID|duplicate"):
        Registry.load(path)


def test_severity_order_and_status_semantics():
    assert min_severity("BLOCK", "REVIEW") == "REVIEW"
    assert min_severity("WARN", "BLOCK") == "WARN"
    assert status_from_findings([Finding("X001", "fail", "WARN", {"file": "x"}, "e", "r", "vale")]) == "clean"
    assert status_from_findings([Finding("X001", "fail", "REVIEW", {"file": "x"}, "e", "r", "vale")]) == "review_needed"
    assert status_from_findings([Finding("X001", "fail", "REPAIR", {"file": "x"}, "e", "r", "vale")]) == "repair_required"


def test_bundle_resolution_caps_diagnostics():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    resolved = dict((rule.id, severity) for rule, severity in bundles.get("session-prep").resolve(registry))
    assert resolved["AGENCY001"] == "BLOCK"
    assert resolved["SCENE001"] == "WARN"
    assert resolved["TEMP001"] == "REVIEW"
    assert "KNOW001" in resolved


def test_vale_mapping_uses_registry_metadata():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    findings = map_vale_output({"wiki/example.md": [{"Check": "CoDM.AGENCY001", "Line": 4,
        "Span": [2, 8], "Match": "You decide", "Message": "matched"}]}, registry, root=ROOT)
    assert findings[0].to_dict()["rule_id"] == "AGENCY001"
    assert findings[0].severity == "BLOCK"
    assert findings[0].location == {"file": "wiki/example.md", "line": 4, "col": 2, "end_col": 8, "text": "You decide"}


def test_vale_deprecated_output_gets_typed_repair():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    findings = map_vale_output(
        {"wiki/example.md": [{"Check": "Deprecated.DMThesis", "Line": 15,
                              "Span": [1, 12], "Match": "## DM Thesis",
                              "Message": "delete the deprecated section"}]},
        registry,
        root=ROOT,
    )
    assert findings[0].rule_id == "VALE_Deprecated.DMThesis"
    assert findings[0].severity == "REPAIR"
    assert findings[0].repair_class == "deterministic_repair"
    assert findings[0].repair_action["kind"] == "delete_section"

def test_vale_batches_merge_results(monkeypatch, tmp_path):
    from tools.creative_lint import vale_adapter

    registry = Registry.load(ROOT / "rules" / "registry.yml")
    files = [tmp_path / f"page-{index}.md" for index in range(3)]
    calls: list[tuple[str, ...]] = []

    def fake_vale(binary, root, batch, style):
        calls.append(tuple(path.name for path in batch))
        payload = {
            path.name: [{"Check": "CoDM.AGENCY001", "Line": index + 1}]
            for index, path in enumerate(batch)
        }
        return subprocess.CompletedProcess(["vale"], 1, json.dumps(payload), ""), 1

    monkeypatch.setattr(vale_adapter, "VALE_BATCH_SIZE", 2)
    monkeypatch.setattr(vale_adapter, "_resolve_vale", lambda root, executable: "vale")
    monkeypatch.setattr(vale_adapter, "_vale_json", fake_vale)
    monkeypatch.setattr("tools.creative_lint.vale_vocab.refresh_vocab", lambda root, vault: vault)

    findings, warnings = vale_adapter.run_vale(files, registry, root=tmp_path, vault=tmp_path)

    assert not warnings
    assert len(findings) == len(files)
    assert {finding.location["file"] for finding in findings} == {path.name for path in files}
    assert sorted(calls) == [("page-0.md", "page-1.md"), ("page-2.md",)]


def test_engine_finds_and_filters_agency_rule():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    engine = LintEngine(registry, bundles, root=ROOT, vault=ROOT / "wiki")
    path = FIXTURES / "AGENCY001" / "fail_authored_decision.md"
    result = engine.run(bundle="session-prep", paths=[path])
    assert result.status == "repair_required"
    assert any(f.rule_id == "AGENCY001" and f.severity == "BLOCK" for f in result.findings)
    filtered = engine.run(bundle="session-prep", paths=[path], severity_filter={"REVIEW"})
    assert all(f.severity == "REVIEW" for f in filtered.findings)


def test_fixture_fail_and_pass_regions_for_vale_rules():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    engine = LintEngine(registry, bundles, root=ROOT, vault=ROOT / "wiki")
    for rule in registry.by_evaluator("vale"):
        fail = next((FIXTURES / rule.id).glob("fail_*.md"))
        passed = next((FIXTURES / rule.id).glob("pass_*.md"))
        assert any(f.rule_id == rule.id for f in engine.run(paths=[fail], rule_ids={rule.id}).findings), rule.id
        assert not any(f.rule_id == rule.id for f in engine.run(paths=[passed], rule_ids={rule.id}).findings), rule.id


def test_waiver_suppresses_status_but_keeps_audit_record(tmp_path):
    waiver_path = tmp_path / "waivers.json"
    waiver_path.write_text(json.dumps([{"rule_id": "AGENCY001", "target": "file:tests/fixtures/creative_lint/AGENCY001/fail_authored_decision.md",
        "reason": "intentional test", "owner": "DM", "granted": "2026-09-01", "expires": "2099-01-01"}]), encoding="utf-8")
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    engine = LintEngine(registry, bundles, root=ROOT, vault=ROOT / "wiki", waivers=WaiverRegistry.load(waiver_path))
    result = engine.run(bundle="session-prep", paths=[FIXTURES / "AGENCY001" / "fail_authored_decision.md"])
    finding = next(f for f in result.findings if f.rule_id == "AGENCY001")
    assert finding.waiver and result.status == "clean" and result.summary["waived"] == 1


def test_shadow_recorder_writes_jsonl(tmp_path):
    finding = Finding("AGENCY001", "fail", "BLOCK", {"file": "x.md", "line": 1}, "e", "r", "vale")
    recorder = ShadowRecorder(tmp_path)
    paths = recorder.record([finding], run_id="test")
    assert paths[0].name == "AGENCY001.jsonl"
    assert recorder.load("AGENCY001")[0]["run_id"] == "test"


def test_repair_loop_retests_changed_surface(tmp_path):
    path = tmp_path / "output.md"
    path.write_text(
        "---\ntitle: Repair output\ncategory: test\ntags: []\nsources: []\n"
        "created: 2026-09-01\nupdated: 2026-09-16\ntype: session-prep\n"
        "lifecycle: draft\nreveal: dm\n---\n\nYou decide the risk is worth it.\n",
        encoding="utf-8",
    )
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    engine = LintEngine(registry, bundles, root=ROOT, vault=ROOT / "wiki")

    def repair(findings):
        assert findings[0].rule_id == "AGENCY001"
        path.write_text("The risk is visible and the door is open.\n", encoding="utf-8")
        return [path]

    result = engine.repair_loop(bundle="session-prep", paths=[path], repair_callback=repair)
    assert result.status == "clean"


def test_finding_from_dict_validates_contract():
    finding = Finding.from_dict({
        "rule_id": "AGENCY001", "result": "fail", "severity": "BLOCK",
        "location": {"file": "x.md", "line": 2}, "evidence": "match",
        "reason": "reason", "evaluator": "vale",
    })
    assert finding.to_dict()["location"]["line"] == 2
    with pytest.raises(ValueError, match="invalid finding severity"):
        Finding.from_dict({**finding.to_dict(), "severity": "CRITICAL"})


def test_registry_warns_on_unresolved_references(tmp_path):
    path = tmp_path / "registry.yml"
    path.write_text(
        "rules:\n"
        "  - id: TEST001\n    title: test\n    category: agency\n"
        "    scope: content\n    severity: BLOCK\n    evaluator: symbolic\n"
        "    lifecycle: ACTIVE\n    message: test\n    depends: [NOPE001]\n",
        encoding="utf-8",
    )
    registry = Registry.load(path)
    assert any("warning:" in error and "NOPE001" in error for error in registry.validate())


def test_bundle_validation_rejects_duplicate_categories(tmp_path):
    path = tmp_path / "bundles.yml"
    path.write_text(
        "bundles:\n  demo:\n    block: [agency]\n    review: [agency]\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="appears"):
        BundleRegistry.load(path)


def test_symbolic_rules_detect_dead_and_stale_entities(tmp_path):
    vault = tmp_path / "wiki"
    (vault / "entities").mkdir(parents=True)
    (vault / "journal").mkdir()
    owner = "---\ntitle: Dead NPC\ncategory: npc\ntags: []\nsources: []\ncreated: 2026-01-01\nupdated: 2026-01-01\ntype: npc\nlifecycle: rejected\nreveal: dm\n---\n"
    (vault / "entities" / "dead-npc.md").write_text(owner, encoding="utf-8")
    source = "---\ntitle: Prep\ncategory: session\ntags: []\nsources: []\ncreated: 2026-01-01\nupdated: 2026-01-01\ntype: session-prep\nlifecycle: draft\nreveal: dm\n---\n[[dead-npc]]\n"
    source_path = vault / "journal" / "prep.md"
    source_path.write_text(source, encoding="utf-8")
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    result = LintEngine(registry, bundles, root=tmp_path, vault=vault).run(
        bundle="session-prep", paths=[source_path]
    )
    assert any(f.rule_id == "CANON001" and f.evaluator == "symbolic" for f in result.findings)


def test_shadow_rules_are_excluded_from_active_result(tmp_path):
    vault = tmp_path / "wiki"
    vault.mkdir()
    page = vault / "page.md"
    page.write_text("plain output\n", encoding="utf-8")
    rule = RuleDefinition(
        id="WIKI001", title="Missing", category="wiki", scope="frontmatter",
        severity="BLOCK", evaluator="symbolic", lifecycle="SHADOW",
        message="missing", repair="add fields",
    )
    registry = Registry([rule])
    result = LintEngine(registry, root=tmp_path, vault=vault).run(paths=[page])
    assert result.findings == []
    assert result.shadow and result.shadow[0].rule_id == "WIKI001"
    assert (tmp_path / "rules" / "shadow" / "WIKI001.jsonl").is_file()


def test_expired_waiver_does_not_suppress_finding(tmp_path):
    waiver_path = tmp_path / "waivers.json"
    waiver_path.write_text(json.dumps([{
        "rule_id": "AGENCY001", "target": "*", "reason": "temporary",
        "owner": "DM", "granted": "2020-01-01", "expires": "2020-01-02",
    }]), encoding="utf-8")
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    result = LintEngine(
        registry, bundles, root=ROOT, vault=ROOT / "wiki",
        waivers=WaiverRegistry.load(waiver_path),
    ).run(bundle="session-prep", paths=[FIXTURES / "AGENCY001" / "fail_authored_decision.md"])
    finding = next(f for f in result.findings if f.rule_id == "AGENCY001")
    assert finding.waiver is None and result.status == "repair_required"


def test_fixture_families_have_fail_and_pass_cases():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    for rule in registry.active():
        if rule.id.startswith(("DIVERSITY", "CANON", "WIKI", "RETRIEVAL")):
            directory = FIXTURES / rule.id
            assert list(directory.glob("fail_*.md")), rule.id
            assert list(directory.glob("pass_*.md")), rule.id

def test_scene_applicability_exempts_redirects_and_explicit_pressure(monkeypatch):
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    files = [
        FIXTURES / "SCENE001" / "redirect_stub.md",
        FIXTURES / "SCENE001" / "pass_explicit_pressure.md",
        FIXTURES / "SCENE001" / "fail_missing_pressure.md",
    ]
    monkeypatch.setattr("tools.creative_lint.engine.run_vale", lambda *args, **kwargs: (
        [Finding("SCENE001", "fail", "WARN", {"file": str(path), "line": 1}, "match", "reason", "vale")
         for path in files], []))
    result = LintEngine(registry, bundles, root=ROOT, vault=FIXTURES).run(rule_ids={"SCENE001"}, paths=files)
    assert [Path(item.location["file"]).name for item in result.findings] == ["fail_missing_pressure.md"]


def test_state_overrides_applicability_and_lifecycle(monkeypatch, tmp_path):
    page = tmp_path / "page.md"
    page.write_text("---\ntype: faction\nlifecycle: accepted\n---\n## Narrative\nNo pressure.\n", encoding="utf-8")
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    bundles = BundleRegistry.load(ROOT / "rules" / "bundles.yml")
    monkeypatch.setattr(
        "tools.creative_lint.engine.run_vale",
        lambda *args, **kwargs: ([Finding("SCENE001", "fail", "WARN", {"file": str(page), "line": 1}, "match", "reason", "vale")], []),
    )
    engine = LintEngine(registry, bundles, root=ROOT, vault=tmp_path)
    assert engine.run(paths=[page], rule_ids={"SCENE001"}).findings
    assert not engine.run(paths=[page], rule_ids={"SCENE001"}, state={"type": "item"}).findings


def test_linear_template_flags_column_wrappers(tmp_path):
    from tools.creative_lint.template_profile import compare_page

    template = tmp_path / "creature.md"
    template.write_text(
        "---\ntitle: t\ntype: creature\n---\n# T\n\n> [!narration] Narration\n> look\n\n"
        "## Statblock\n```statblock\n```\n## Behavior\n## Tactics\n",
        encoding="utf-8",
    )
    page = tmp_path / "bear.md"
    page.write_text(
        "---\ntitle: Bear\ntype: creature\n---\n# Bear\n## Statblock\n"
        "````col\n```col-md\nflexGrow=1\n```\n## Behavior\n## Tactics\n",
        encoding="utf-8",
    )
    evidence = " ".join(item.evidence for item in compare_page(page, template, root=tmp_path))
    assert "col" in evidence


def test_bear_elk_flags_multiple_statblock_images():
    from tools.creative_lint.template_profile import template_conformance

    _, findings = template_conformance(ROOT / "wiki/entities/creature/bear-elk.md", root=ROOT)
    assert any(item.rule_id == "TMPL006" for item in findings)


def test_bloodhawk_allows_one_statblock_image():
    from tools.creative_lint.template_profile import template_conformance

    _, findings = template_conformance(ROOT / "wiki/entities/creature/bloodhawk.md", root=ROOT)
    assert not any(item.rule_id in {"TMPL006", "TMPL007"} for item in findings)


def test_creature_layout_contract_flags_multiple_statblock_images(tmp_path):
    from tools.wiki_ops.template_contracts import check_layout_conformance, load_contract

    contract = load_contract(ROOT / "wiki/templates/contracts/creature.yml")
    page = tmp_path / "creature.md"
    page.write_text(
        "## Statblock\n![[overview.jpg]]\n![[second.jpg]]\n```statblock\n```\n"
        "## Art\n### Reference\n![[extra.jpg]]\n",
        encoding="utf-8",
    )
    findings = check_layout_conformance(page, page.read_text(encoding="utf-8"), contract.layout)
    assert {item["rule_id"] for item in findings} == {"TMPL006"}

def test_creature_layout_contract_flags_misplaced_images(tmp_path):
    from tools.wiki_ops.template_contracts import check_layout_conformance, load_contract

    contract = load_contract(ROOT / "wiki/templates/contracts/creature.yml")
    page = tmp_path / "creature.md"
    page.write_text(
        "## Statblock\n```statblock\n```\n![[overview.jpg]]\n"
        "## Art\n![[extra.jpg]]\n",
        encoding="utf-8",
    )
    findings = check_layout_conformance(page, page.read_text(encoding="utf-8"), contract.layout)
    assert {item["rule_id"] for item in findings} == {"TMPL006", "TMPL007"}

def test_bloodhawk_keeps_linear_creature_layout():
    from tools.creative_lint.template_profile import template_conformance

    _, findings = template_conformance(ROOT / "wiki/entities/creature/bloodhawk.md", root=ROOT)
    assert not any("Extra formatting marker" in item.evidence for item in findings)
