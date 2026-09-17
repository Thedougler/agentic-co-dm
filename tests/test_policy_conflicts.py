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
