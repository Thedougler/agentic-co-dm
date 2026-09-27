from __future__ import annotations

from pathlib import Path


import pytest

from tools.creative_lint.bundles import BundleRegistry
from tools.creative_lint.engine import LintEngine
from tools.creative_lint.finding import Finding
from tools.creative_lint.registry import Registry, RuleDefinition
from tools.creative_lint.severity import min_severity, status_from_findings
from tools.creative_lint.vale_adapter import map_vale_output

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "tests" / "fixtures" / "creative_lint"


def test_registry_loads_and_exposes_stable_ids():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    assert registry.all_ids()
    assert registry.by_category("wiki")
    assert registry.by_evaluator("symbolic")
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
    assert set(resolved) == {"WIKI001", "WIKI002", "RETRIEVAL001", "DIVERSITY001"}


def test_vale_repo_local_style_is_agent_repair(tmp_path):
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    findings = map_vale_output(
        {"wiki/example.md": [{"Check": "Deprecated.DMThesis", "Line": 15,
                              "Span": [1, 12], "Match": "## DM Thesis",
                              "Message": "DM Thesis is deprecated"}]},
        registry,
        root=ROOT,
    )
    assert findings[0].rule_id == "VALE_Deprecated.DMThesis"
    assert findings[0].severity == "REPAIR"
    assert findings[0].repair_class == "agent_repair"
    assert findings[0].repair_action is None

    from tools.wiki_ops.repair_plans import build_safe_fix_plan

    (tmp_path / "example.md").write_text("# Example\n\n## DM Thesis\n", encoding="utf-8")
    finding = findings[0].to_dict() | {"file": "example.md"}
    operations, skipped = build_safe_fix_plan(tmp_path, [finding], scope={"paths": ["example.md"]})
    assert operations == []
    assert skipped == []


def test_finding_from_dict_validates_contract():
    finding = Finding.from_dict({
        "rule_id": "TEST001", "result": "fail", "severity": "BLOCK",
        "location": {"file": "x.md", "line": 2}, "evidence": "match",
        "reason": "reason", "evaluator": "symbolic",
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


def test_fixture_families_have_fail_and_pass_cases():
    registry = Registry.load(ROOT / "rules" / "registry.yml")
    for rule in registry.active():
        if rule.id.startswith(("DIVERSITY", "WIKI", "RETRIEVAL")):
            directory = FIXTURES / rule.id
            assert list(directory.glob("fail_*.md")), rule.id
            assert list(directory.glob("pass_*.md")), rule.id


def test_generated_vale_vocab_keeps_rule_tokens_active(tmp_path: Path):
    import shutil
    import subprocess

    from tools.creative_lint.vale_vocab import VOCAB_RELATIVE, render_vocab

    root = Path(__file__).resolve().parents[1]
    vocab = render_vocab(root / "wiki")
    assert "DM" not in vocab.splitlines()

    vale = shutil.which("vale") or str(root / ".venv/bin/vale")
    if not Path(vale).is_file():
        pytest.skip("vale binary is absent")
    config_root = tmp_path / "config"
    shutil.copytree(root / "styles", config_root / "styles")
    shutil.copy(root / ".vale.ini", config_root / ".vale.ini")
    (config_root / VOCAB_RELATIVE).write_text(vocab, encoding="utf-8")
    scratch = tmp_path / "scratch.md"
    scratch.write_text(
        "# Scratch\n\nThe DM Thesis section names the villain.\n\nTrack the faction clock here.\n",
        encoding="utf-8",
    )
    proc = subprocess.run(
        [vale, "--output=line", f"--config={config_root / '.vale.ini'}", str(scratch)],
        cwd=config_root,
        capture_output=True,
        text=True,
    )
    output = proc.stdout + proc.stderr
    assert "Deprecated.DMThesis" in output, output
    assert "Deprecated.FactionClock" in output, output


def test_linting_a_temp_vault_leaves_the_tracked_vocabulary_alone(tmp_path: Path):
    from tools.creative_lint.vale_adapter import run_vale
    from tools.creative_lint.vale_vocab import VOCAB_RELATIVE

    root = Path(__file__).resolve().parents[1]
    tracked = root / VOCAB_RELATIVE
    before = tracked.read_bytes()
    vault = tmp_path / "vault"
    (vault / "entities/npc").mkdir(parents=True)
    page = vault / "entities/npc/zorblax-quennifer.md"
    page.write_text("---\ntitle: Zorblax Quennifer\ntype: npc\n---\n\n# Zorblax Quennifer\n", encoding="utf-8")
    run_vale([page], Registry.load(root / "rules/registry.yml"), root=root, vault=vault)
    assert tracked.read_bytes() == before
