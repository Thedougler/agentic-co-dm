from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
LUNA = ROOT / "scripts" / "luna-eval"
EVAL_FILES = sorted((ROOT / ".agents" / "skills").glob("*/evals/evals.json"))


def _record(**overrides) -> dict:
    record = {"id": 1, "prompt": "Add a place.", "assertions": [{"type": "behavior", "text": "Writes the page"}]}
    record.update(overrides)
    return record


def _run_bad(tmp_path: Path, payload: dict, skill_dir: str = "demo-skill") -> subprocess.CompletedProcess[str]:
    skill = tmp_path / skill_dir
    (skill / "evals").mkdir(parents=True)
    (skill / "evals" / "evals.json").write_text(json.dumps(payload), encoding="utf-8")
    env = {**os.environ, "PATH": str(tmp_path / "no-codex")}  # a subject run would fail loudly
    return subprocess.run(
        [sys.executable, str(LUNA), "--skill", str(skill), "--eval", "1", "--out", str(tmp_path / "out")],
        cwd=tmp_path, capture_output=True, text=True, env=env,
    )


def test_all_skill_eval_files_pass_the_schema_check():
    assert len(EVAL_FILES) == 60
    import importlib.util
    from importlib.machinery import SourceFileLoader

    loader = SourceFileLoader("luna_eval", str(LUNA))
    spec = importlib.util.spec_from_loader("luna_eval", loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    problems = [problem for path in EVAL_FILES for problem in module.validate_evals(path)]
    assert problems == []


@pytest.mark.parametrize(
    "payload, needle",
    [
        ({"evals": [_record()]}, "skill_name"),
        ({"skill_name": "other-skill", "evals": [_record()]}, "skill_name"),
        ({"skill_name": "demo-skill", "evals": [_record(assertions=[])]}, "assertions"),
        ({"skill_name": "demo-skill", "evals": [{"id": 1, "prompt": "x"}]}, "assertions"),
        ({"skill_name": "demo-skill", "evals": [_record(expectations=["old"])]}, "expectations"),
        ({"skill_name": "demo-skill", "evals": [_record(assertions=[{"type": "qualitative", "text": "x"}])]}, "type"),
        (
            {"skill_name": "demo-skill", "evals": [_record(assertions=[{"type": "skill_selected", "text": "no-such-skill"}])]},
            "skill_selected",
        ),
    ],
)
def test_schema_check_rejects_bad_records_before_any_subject_run(tmp_path: Path, payload: dict, needle: str):
    proc = _run_bad(tmp_path, payload)
    assert proc.returncode == 2, proc.stdout + proc.stderr
    error = json.loads(proc.stdout)
    assert error["status"] == "error"
    assert error["hint"] == "see data-model §2"
    assert "example" in error
    assert re.match(r".+evals\.json: eval \S+: .+", error["error"]), error["error"]
    assert needle in error["error"]
    assert not (tmp_path / "out").exists()


def test_no_eval_assertion_uses_work_gate_wording():
    pattern = re.compile(r"work gate|chat proposal|approval before write", re.I)
    offenders = []
    for path in EVAL_FILES:
        for record in json.loads(path.read_text(encoding="utf-8")).get("evals", []):
            for item in record.get("assertions", []) or []:
                text = item.get("text", "") if isinstance(item, dict) else str(item)
                if pattern.search(text):
                    offenders.append(f"{path.parent.parent.name}:{record.get('id')}: {text[:80]}")
    assert offenders == []


def test_rerun_skips_a_completed_run(tmp_path: Path):
    payload = {"skill_name": "demo-skill", "evals": [_record()]}
    out = tmp_path / "out"
    done = out / "1" / "with_skill" / "run-1"
    done.mkdir(parents=True)
    (done / "timing.json").write_text(json.dumps({"duration_ms": 1000, "total_duration_seconds": 1, "exit": 0}), encoding="utf-8")
    proc = _run_bad(tmp_path, payload)
    assert proc.returncode == 0, proc.stdout + proc.stderr
    assert "skip" in proc.stdout
    assert json.loads((done / "timing.json").read_text(encoding="utf-8"))["exit"] == 0


def test_help_shows_examples_and_missing_flag_exits_2_with_example(tmp_path: Path):
    helped = subprocess.run([sys.executable, str(LUNA), "--help"], capture_output=True, text=True)
    assert helped.returncode == 0
    assert "Examples:" in helped.stdout
    example = "scripts/luna-eval --skill .agents/skills/place-design --eval 1 --out /tmp/pd/iteration-1"
    assert example in helped.stdout
    missing = subprocess.run(
        [sys.executable, str(LUNA), "--skill", ".agents/skills/place-design", "--eval", "1"],
        cwd=tmp_path, capture_output=True, text=True,
    )
    assert missing.returncode == 2
    payload = json.loads(missing.stdout)
    assert payload["status"] == "error" and "--out" in payload["error"]
    assert payload["example"] == example
    assert payload["hint"]
    assert "--out" in missing.stderr
