from typer.testing import CliRunner

from wiki_cli.cli import app

runner = CliRunner()


def test_help_exits_zero():
    result = runner.invoke(app, ["help"])
    assert result.exit_code == 0


def test_help_contains_commands():
    result = runner.invoke(app, ["help"])
    for cmd in ("wiki lint", "wiki sweep", "wiki drain", "wiki explain", "wiki debt", "wiki bench"):
        assert cmd in result.output


def test_help_contains_flags():
    result = runner.invoke(app, ["help"])
    for flag in ("--only", "--quiet", "--json", "--over", "--claim"):
        assert flag in result.output


def test_help_names_no_retired_command_or_flag():
    """ADR-0064 cull: the surface an agent reads names nothing it cannot
    run — no severity/producer display filters, no ratchet-exit, and no
    worklist/claims/release/baseline commands drain and debt absorbed."""
    result = runner.invoke(app, ["help"])
    for retired in (
        "--severity",
        "--producer",
        "--ratchet-exit",
        "wiki worklist",
        "wiki claims",
        "wiki release",
        "wiki baseline",
    ):
        assert retired not in result.output


def test_help_contains_read_layer_commands():
    result = runner.invoke(app, ["help"])
    for cmd in ("wiki list", "wiki search", "wiki links spread"):
        assert cmd in result.output
