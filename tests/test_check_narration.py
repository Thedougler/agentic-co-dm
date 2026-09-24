import importlib.util
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check-narration.py"
spec = importlib.util.spec_from_file_location("check_narration", SCRIPT)
assert spec and spec.loader
cn = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cn)


def test_checks_only_the_narration_callout():
    raw = "> [!narration] Opening\n> The gate is shut; the road bends.\n\nArt seen: north tower, west gate\n"
    body = cn.narration_text(raw)
    assert body == "The gate is shut; the road bends."
    assert cn.check(body, []) == ["semicolon in spoken prose"]


def test_reports_copied_phrases_but_not_quoted_speech(tmp_path):
    src = tmp_path / "beat.md"
    src.write_text("A thin line hangs in the slow current. She says: stay back from the water now.")
    body = 'A thin line hangs in the slow current beside you. "Stay back from the water now," she says.'
    findings = cn.check(body, [str(src)])
    assert any("a thin line hangs in" in f for f in findings)
    assert not any("back from the water" in f for f in findings)


def test_finds_every_narration_block_on_a_beat_page():
    page = ("# Beat\n\n> [!narration] Initial Narration\n> Smoke hangs low.\n\n"
            "| Zone | Narration |\n|---|---|\n\n```col-md\n> [!narration] Exit\n> The door slams.\n```\n")
    assert [t for t, _ in cn.narration_blocks(page)] == ["Initial Narration", "Exit"]
