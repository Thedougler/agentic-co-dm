from __future__ import annotations

import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VALE = ROOT / ".venv" / "bin" / "vale"
FIXTURES = ROOT / "tests" / "fixtures" / "vale" / "emdash"


def _vale(path: Path) -> dict:
    result = subprocess.run(
        [str(VALE), "--config", str(ROOT / ".vale.ini"), "--output", "JSON", str(path)],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode in (0, 1), result.stderr
    return json.loads(result.stdout or "{}")


def _emdash_alerts(payload: dict) -> list[dict]:
    alerts = []
    for findings in payload.values():
        for item in findings:
            if item.get("Check") == "ai-tells.EmDashUsage":
                alerts.append(item)
    return alerts


def test_required_check_token_is_vale_clean():
    alerts = _emdash_alerts(_vale(FIXTURES / "pass_check_token.md"))
    assert alerts == []


def test_prose_emdash_still_fails_emdash_usage():
    alerts = _emdash_alerts(_vale(FIXTURES / "fail_prose_emdash.md"))
    assert alerts
