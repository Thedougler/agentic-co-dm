from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CLI = ROOT / "scripts" / "wiki-lint"
FIXTURE = ROOT / "tests" / "fixtures" / "creative_lint" / "AGENCY001" / "fail_authored_decision.md"


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([str(CLI), *args], cwd=ROOT, text=True, capture_output=True)


def test_task_json_contract_and_exit_code():
    proc = run_cli("task", "session-prep", str(FIXTURE), "--json")
    assert proc.returncode == 1
    data = json.loads(proc.stdout)
    assert data["status"] == "repair_required"
    assert data["findings"][0]["rule_id"] == "AGENCY001"
    assert {"rule_id", "result", "severity", "location", "evidence", "reason", "evaluator"} <= data["findings"][0].keys()


def test_rule_human_output_and_unknown_rule():
    proc = run_cli("rule", "AGENCY001")
    assert proc.returncode == 0
    assert "AGENCY001" in proc.stdout and "Bundles:" in proc.stdout
    missing = run_cli("rule", "NOPE999")
    assert missing.returncode == 2
    assert "Unknown rule ID" in missing.stderr


def test_legacy_no_subcommand_is_structural_json():
    proc = run_cli("--json", "wiki")
    assert proc.returncode in (0, 1)
    data = json.loads(proc.stdout)
    assert "counts" in data and "hard_fail" in data


def test_candidate_routes_known_correction():
    proc = run_cli("candidate", "NPC", "meta-knowledge")
    assert proc.returncode == 0
    assert "KNOW002" in proc.stdout
