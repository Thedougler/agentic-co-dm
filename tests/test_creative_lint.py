from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.creative_lint.bundles import BundleRegistry
from tools.creative_lint.engine import LintEngine
from tools.creative_lint.finding import Finding
from tools.creative_lint.registry import Registry
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
