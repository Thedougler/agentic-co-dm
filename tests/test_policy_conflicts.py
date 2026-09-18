from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]


def test_policy_registry_is_clean():
    proc = subprocess.run([sys.executable, str(ROOT / "scripts/check-policy-conflicts"), "--json"], cwd=ROOT, capture_output=True, text=True)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    data = json.loads(proc.stdout)
    assert data["status"] == "clean"
    assert data["policies"] >= 5


def test_policy_checker_reports_missing_consumer(tmp_path: Path):
    registry = tmp_path / "policy.yml"
    registry.write_text(
        "policies:\n  demo:\n    owner: docs/owner.md\n    consumers: [docs/missing.md]\n",
        encoding="utf-8",
    )
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "owner.md").write_text("demo owner\n", encoding="utf-8")
    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check-policy-conflicts"), "--registry", str(registry), "--root", str(tmp_path), "--json"],
        cwd=ROOT, capture_output=True, text=True,
    )
    assert proc.returncode == 1
    assert json.loads(proc.stdout)["conflicts"][0]["reason"] == "consumer_not_found"
