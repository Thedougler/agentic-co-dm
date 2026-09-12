import pathlib
import subprocess

import pytest

from wiki_cli.parity import ported_rules, run_wiki_lint

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


def test_ported_rules_derive_from_registry():
    assert "W84" in ported_rules()


class _FakeCompletedProcess:
    def __init__(self, returncode: int, stdout: str, stderr: str = "") -> None:
        self.returncode = returncode
        self.stdout = stdout
        self.stderr = stderr


def test_run_wiki_lint_raises_on_unparseable_crash(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        subprocess,
        "run",
        lambda *a, **k: _FakeCompletedProcess(2, "Traceback (most recent call last):\n...\n"),
    )
    with pytest.raises(RuntimeError):
        run_wiki_lint(FIXTURES / "clean-faction.md")


def test_run_wiki_lint_parses_w84_finding(monkeypatch: pytest.MonkeyPatch) -> None:
    """wiki-cli findings use W-number ids directly — no translation needed."""
    payload = '{"rule": "W84", "path": "vault/x.md", "line": 3}\n'
    monkeypatch.setattr(subprocess, "run", lambda *a, **k: _FakeCompletedProcess(1, payload))
    assert run_wiki_lint(FIXTURES / "clean-faction.md") == {("W84", "vault/x.md", 3)}
