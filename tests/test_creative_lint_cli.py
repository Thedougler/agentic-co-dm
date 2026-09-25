from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "wiki-lint"
FIXTURE = ROOT / "tests" / "fixtures" / "creative_lint" / "WIKI001" / "fail_missing_frontmatter.md"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([str(CLI), *args], cwd=ROOT, text=True, capture_output=True)


def test_task_json_contract_and_exit_code():
    proc = run_cli("task", "session-prep", str(FIXTURE), "--json")
    assert proc.returncode == 1
    data = json.loads(proc.stdout)
    assert data["status"] == "repair_required"
    assert data["findings"][0]["rule_id"] == "WIKI001"
    assert {"rule_id", "result", "severity", "location", "evidence", "reason", "evaluator"} <= data["findings"][0].keys()


def test_rule_human_output_and_unknown_rule():
    proc = run_cli("rule", "WIKI001")
    assert proc.returncode == 0
    assert "WIKI001" in proc.stdout and "Bundles:" in proc.stdout
    missing = run_cli("rule", "NOPE999")
    assert missing.returncode == 2
    assert "Unknown rule ID" in missing.stderr


def test_legacy_no_subcommand_is_structural_json():
    proc = run_cli("--json", "wiki")
    assert proc.returncode in (0, 1)
    data = json.loads(proc.stdout)
    assert "counts" in data and "hard_fail" in data




def test_candidate_creates_shadow_template_for_unmatched_correction():
    correction = "A completely novel moonlit cartography concern"
    slug = "a-completely-novel-moonlit-cartography-concern"
    candidate = ROOT / "rules" / "candidates" / f"{slug}.yml"
    try:
        proc = run_cli("candidate", correction, "--json")
        assert proc.returncode == 0
        data = json.loads(proc.stdout)
        assert data["lifecycle"] == "SHADOW"
        assert candidate.is_file()
        assert "lifecycle: SHADOW" in candidate.read_text(encoding="utf-8")
    finally:
        candidate.unlink(missing_ok=True)


def test_file_missing_frontmatter_reports_wiki001(tmp_path):
    page = tmp_path / "missing.md"
    page.write_text("plain output\n", encoding="utf-8")
    proc = run_cli("file", str(page), "--json")
    assert proc.returncode == 1
    data = json.loads(proc.stdout)
    finding = next(item for item in data["findings"] if item["rule_id"] == "WIKI001")
    assert finding["severity"] == "BLOCK"
    assert "frontmatter" in finding["evidence"].lower()


def test_unknown_bundle_and_invalid_severity_are_argument_errors():
    unknown = run_cli("task", "not-a-bundle", "--json")
    assert unknown.returncode == 2
    assert "available" in unknown.stderr
    invalid = run_cli("task", "session-prep", "--severity", "nope", "--json")
    assert invalid.returncode == 2
    assert "severity" in invalid.stderr


def test_consolidation_is_dry_run_until_approved():
    dry = run_cli("--consolidate", "wiki", "--json")
    assert dry.returncode == 0
    dry_data = json.loads(dry.stdout)
    assert dry_data["status"] == "dry_run"
    assert dry_data["plan"]["requires_approval"] is True
    assert dry_data["plan"]["approved"] is False
    applied = run_cli("--consolidate", "wiki", "--json", "--approve")
    assert applied.returncode == 0
    assert json.loads(applied.stdout)["status"] == "applied"
