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


def _omp_copy(tmp_path: Path, memory_block: str) -> Path:
    import shutil

    shutil.copytree(ROOT / ".omp", tmp_path / ".omp")
    (tmp_path / ".specify").mkdir()
    shutil.copy(ROOT / ".specify/integration.json", tmp_path / ".specify/integration.json")
    shutil.copy(ROOT / "AGENTS.md", tmp_path / "AGENTS.md")
    config = tmp_path / ".omp/config.yml"
    lines = config.read_text(encoding="utf-8").splitlines()
    start = lines.index("memory:")
    end = start + 1
    while end < len(lines) and lines[end].startswith((" ", "\t")):
        end += 1
    config.write_text("\n".join(lines[:start] + memory_block.splitlines() + lines[end:]) + "\n", encoding="utf-8")
    return tmp_path


def _omp_check(root: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["bash", str(ROOT / "scripts/check-omp-baseline.sh")], cwd=root, capture_output=True, text=True)


def test_omp_baseline_accepts_disabled_memory_backends(tmp_path: Path):
    for index, value in enumerate(("false", '"false"', "off", '"off"')):
        proc = _omp_check(_omp_copy(tmp_path / str(index), f"memory:\n  backend: {value}"))
        assert proc.returncode == 0, (value, proc.stderr)
        assert "omp-speckit-baseline: pass" in proc.stdout


def test_omp_baseline_rejects_enabled_or_missing_memory(tmp_path: Path):
    proc = _omp_check(_omp_copy(tmp_path / "enabled", "memory:\n  backend: mnemopi"))
    assert proc.returncode == 1
    assert "memory enabled: backend=mnemopi" in proc.stderr
    proc = _omp_check(_omp_copy(tmp_path / "no-block", ""))
    assert proc.returncode == 1
    assert "memory key missing" in proc.stderr
    proc = _omp_check(_omp_copy(tmp_path / "no-line", "memory:\n  scoping: none"))
    assert proc.returncode == 1
    assert "memory key missing" in proc.stderr


def test_feature_026_docs_cite_only_existing_paths(tmp_path: Path):
    import re

    spec_dir = "specs/026-agent-autonomy-scope"
    seeded = tmp_path / spec_dir
    seeded.mkdir(parents=True)
    (seeded / "plan.md").write_text("Run `tests/test_missing_surface.py` and `scripts/check-current-commands`.\n", encoding="utf-8")
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts/check-current-commands").write_text("", encoding="utf-8")
    seeded_proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check-current-commands"), "--json", "--root", str(tmp_path)],
        capture_output=True, text=True,
    )
    seeded_hits = json.loads(seeded_proc.stdout)["hits"]
    assert [(hit["path"], hit["command"]) for hit in seeded_hits] == [
        (f"{spec_dir}/plan.md", "tests/test_missing_surface.py")
    ], seeded_hits

    proc = subprocess.run(
        [sys.executable, str(ROOT / "scripts/check-current-commands"), "--json"],
        cwd=ROOT, capture_output=True, text=True,
    )
    hits = [hit for hit in json.loads(proc.stdout)["hits"] if hit["path"].startswith(spec_dir + "/")]
    assert hits == []

    retired = [
        f"{path.relative_to(ROOT)}:{number}"
        for path in sorted((ROOT / spec_dir).rglob("*.md"))
        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1)
        if re.search(r"AGENT00[1-3]", line)
    ]
    assert retired == []
