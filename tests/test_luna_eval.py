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


def _luna_module():
    import importlib.util
    from importlib.machinery import SourceFileLoader

    loader = SourceFileLoader("luna_eval", str(LUNA))
    spec = importlib.util.spec_from_loader("luna_eval", loader)
    module = importlib.util.module_from_spec(spec)
    loader.exec_module(module)
    return module


def _cmd(command: str, output: str = "", exit_code: int = 0) -> dict:
    return {"type": "item.completed", "item": {
        "type": "command_execution", "command": f"/bin/zsh -lc '{command}'",
        "aggregated_output": output, "exit_code": exit_code, "status": "completed"}}


FR035 = '{"status": "error", "error": "bad path", "hint": "h", "example": "wiki lint entities/place/a.md"}'
EVENTS = [
    {"type": "thread.started", "thread_id": "t"},
    {"type": "item.completed", "item": {"type": "agent_message", "text": "hi"}},
    _cmd("cat .agents/skills/place-design/SKILL.md && cat .agents/skills/obsidian-markdown/SKILL.md", "..."),
    _cmd("sed -n 1,40p .agents/skills/place-design/SKILL.md", "..."),
    _cmd("scripts/wiki lint wiki/entities/place/a.md", FR035, 2),          # FR-035 usage error
    _cmd("scripts/wiki lint entities/place/a.md", '{"status": "ok"}', 0),
    _cmd("scripts/wiki lint --bogus", "usage: wiki lint\nwiki lint: error: unrecognized arguments", 2),
    _cmd("scripts/wiki lint --bogus", "usage: wiki lint\nwiki lint: error: unrecognized arguments", 2),  # retry
    _cmd("scripts/wiki lint entities/place/b.md", '{"status": "rejected"}', 2),  # exit 2 alone: not a usage error
    _cmd("rg Candlemere wiki", "x", 0),
    _cmd("rg Candlemere wiki", "x", 0),                                    # duplicate after success
    {"type": "item.completed", "item": {"type": "file_change", "changes": [{"path": "/o/a.md", "kind": "add"}], "status": "completed"}},
    {"type": "turn.completed", "usage": {"input_tokens": 1000, "cached_input_tokens": 400, "output_tokens": 50}},
]


def test_metrics_derive_from_events(tmp_path: Path):
    events = tmp_path / "events.jsonl"
    events.write_text("\n".join(json.dumps(e) for e in EVENTS) + "\n", encoding="utf-8")
    m = _luna_module().build_metrics(events, model="gpt-6-luna", effort="high", exit_code=0, delivered=True)
    assert set(m) == {"tool_calls", "total_tool_calls", "retries", "invocation_errors", "invocation_error_commands",
                      "duplicate_actions", "tokens", "completion_reason", "model", "effort", "skills_read"}
    assert m["tool_calls"] == {"command": 9, "file_change": 1} and m["total_tool_calls"] == 10
    assert m["retries"] == 1
    assert m["invocation_errors"] == 3
    assert m["invocation_error_commands"] == [
        "scripts/wiki lint wiki/entities/place/a.md", "scripts/wiki lint --bogus", "scripts/wiki lint --bogus"]
    assert m["duplicate_actions"] == 1
    assert m["tokens"] == {"input": 1000, "output": 50, "total": 1050}
    assert m["completion_reason"] == "ok"
    assert (m["model"], m["effort"]) == ("gpt-6-luna", "high")
    assert m["skills_read"] == [".agents/skills/place-design/SKILL.md", ".agents/skills/obsidian-markdown/SKILL.md"]


def test_metrics_record_absent_events_as_null(tmp_path: Path):
    events = tmp_path / "events.jsonl"
    events.write_text(json.dumps({"type": "thread.started"}) + "\n", encoding="utf-8")
    m = _luna_module().build_metrics(events, model="gpt-6-luna", effort="high", exit_code=1, delivered=False)
    assert m["tokens"] is None
    assert m["completion_reason"] == "error"
    assert m["skills_read"] == [] and m["total_tool_calls"] == 0


def test_skill_selected_grades_the_first_owner_skill_read():
    grade = _luna_module().grade_skill_selected
    metrics = {"skills_read": [".agents/skills/place-design/SKILL.md", ".agents/skills/city-design/SKILL.md"]}
    items = grade([{"type": "skill_selected", "text": "place-design"}, {"type": "behavior", "text": "x"}], metrics)
    assert items == [{"text": "place-design", "passed": True, "type": "skill_selected",
                      "evidence": "first SKILL.md read: .agents/skills/place-design/SKILL.md"}]
    miss = grade([{"type": "skill_selected", "text": "city-design"}], metrics)[0]
    assert miss["passed"] is False
    none = grade([{"type": "skill_selected", "text": "city-design"}], {"skills_read": []})[0]
    assert none["passed"] is False and "no SKILL.md" in none["evidence"]
