from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts/check-agent-standards.py"


def _run(*extra: str, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--json", *extra],
        cwd=cwd or ROOT,
        capture_output=True,
        text=True,
    )


def test_agent_standards_clean_on_conforming_tree():
    proc = _run()
    assert proc.returncode == 0, proc.stdout + proc.stderr
    data = json.loads(proc.stdout)
    assert data["status"] == "clean"


def test_agent001_fails_on_work_gate_heading(tmp_path: Path):
    (tmp_path / "AGENTS.md").write_text("# x\n", encoding="utf-8")
    (tmp_path / "wiki").mkdir()
    (tmp_path / "wiki" / "AGENTS.md").write_text("# x\n", encoding="utf-8")
    skills = tmp_path / ".agents" / "skills" / "demo"
    skills.mkdir(parents=True)
    (skills / "SKILL.md").write_text("## Work gate\n\nWait.\n", encoding="utf-8")
    docs = tmp_path / "docs" / "agents"
    docs.mkdir(parents=True)
    (docs / "work.md").write_text("# work\n", encoding="utf-8")
    specs = tmp_path / "specs" / "000-demo"
    specs.mkdir(parents=True)
    (specs / "spec.md").write_text("## Requirements\n", encoding="utf-8")
    proc = _run("--root", str(tmp_path))
    assert proc.returncode != 0
    data = json.loads(proc.stdout)
    assert any(f.get("id") == "AGENT001" for f in data.get("findings", []))


def test_agent002_fails_on_adhoc_skill_path(tmp_path: Path):
    (tmp_path / "AGENTS.md").write_text("# x\n", encoding="utf-8")
    (tmp_path / "wiki").mkdir()
    (tmp_path / "wiki" / "AGENTS.md").write_text("# x\n", encoding="utf-8")
    bad = tmp_path / ".agents" / "skills" / "My Skill"
    bad.mkdir(parents=True)
    (bad / "notes.txt").write_text("notes\n", encoding="utf-8")
    (tmp_path / "docs" / "agents").mkdir(parents=True)
    (tmp_path / "specs" / "000-demo").mkdir(parents=True)
    (tmp_path / "specs" / "000-demo" / "spec.md").write_text("## Requirements\n", encoding="utf-8")
    proc = _run("--root", str(tmp_path))
    assert proc.returncode != 0
    data = json.loads(proc.stdout)
    assert any(f.get("id") == "AGENT002" for f in data.get("findings", []))


def test_agent003_fails_when_agent_facing_fr_has_no_registry_id(tmp_path: Path):
    (tmp_path / "AGENTS.md").write_text("# x\n", encoding="utf-8")
    (tmp_path / "wiki").mkdir()
    (tmp_path / "wiki" / "AGENTS.md").write_text("# x\n", encoding="utf-8")
    (tmp_path / ".agents" / "skills" / "demo").mkdir(parents=True)
    (tmp_path / ".agents" / "skills" / "demo" / "SKILL.md").write_text("# demo\n", encoding="utf-8")
    (tmp_path / "docs" / "agents").mkdir(parents=True)
    spec_dir = tmp_path / "specs" / "000-demo"
    spec_dir.mkdir(parents=True)
    (spec_dir / "spec.md").write_text(
        "## Requirements\n\n### Functional Requirements\n\n- **FR-001**: The agent-facing instruction MUST be checkable.\n",
        encoding="utf-8",
    )
    (tmp_path / "rules").mkdir()
    (tmp_path / "rules" / "registry.yml").write_text("rules:\n  - id: AGENT001\n", encoding="utf-8")
    proc = _run("--root", str(tmp_path))
    assert proc.returncode != 0
    data = json.loads(proc.stdout)
    assert any(f.get("id") == "AGENT003" for f in data.get("findings", []))
