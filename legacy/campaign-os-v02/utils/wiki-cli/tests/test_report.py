"""The report contract: lint output is an instruction list (ADR-0064).

`LintResult`s are built by hand throughout; no rule ever actually runs.
Three throwaway rules (`WT1`/`WT2`/`WT3`, deliberately outside the real
`W##` id space so they can never collide with a ported rule) are
registered once at import time — the inline-FIX law needs a real registry
entry to pull `fix` text from, matching `test_orchestrator.py`'s own
test-only-registered-rule pattern.
"""

from __future__ import annotations

from wiki_cli import report
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.orchestrator import LintResult, RunStats
from wiki_cli.report import render

_FILE = "vault/npcs/barnaby-rook.md"

_INTERNAL_VOCABULARY = (
    "advisory",
    "GATED",
    "gated",
    "ratchet",
    "structural",
    "content-shape",
    "prose",
    "severity",
    "warning",
    "error",
    "tier",
)
"""Tokens a scoped report must never print: a fixing agent acts on the
output without first learning the engine's internal vocabulary."""


@register
class _WT1Rule(FileRule):
    id = "WT1"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "fix WT1 by doing the WT1 thing"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> list[Finding]:
        del page, corpus
        return []


@register
class _WT2Rule(FileRule):
    id = "WT2"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "fix WT2 by doing the WT2 thing"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> list[Finding]:
        del page, corpus
        return []


@register
class _WT3Rule(FileRule):
    id = "WT3"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = "fix WT3 by doing the WT3 thing"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> list[Finding]:
        del page, corpus
        return []


def _finding(
    rule_id: str,
    *,
    file: str = _FILE,
    line: int = 1,
    message: str = "something is wrong",
    severity: Severity = Severity.WARNING,
    tier: Tier = Tier.STRUCTURAL,
) -> Finding:
    return Finding(
        rule_id=rule_id,
        file=file,
        line=line,
        message=message,
        severity=severity,
        tier=tier,
        producer="wiki",
    )


def _result(findings: list[Finding], *, files: int = 1) -> LintResult:
    return LintResult(
        findings=findings,
        stats=RunStats(files=files, rules_run=len(findings), cache_hits=0, seconds=0.4),
    )


def test_header_line_first():
    result = _result([_finding("WT1", line=1), _finding("WT2", line=2)])
    output = render(result)
    assert output.splitlines()[0] == "LINT 1 file — 2 findings"


def test_one_finding_per_line():
    result = _result(
        [
            _finding("WT1", line=1, message="no tags"),
            _finding("WT2", line=44, message="unlinked mention"),
        ]
    )
    lines = render(result).splitlines()
    assert any(
        line.startswith(f"{_FILE}:1") and "WT1" in line and "no tags" in line for line in lines
    )
    assert any(
        line.startswith(f"{_FILE}:44") and "WT2" in line and "unlinked mention" in line
        for line in lines
    )


def test_per_rule_hit_cap():
    findings = [_finding("WT1", line=i) for i in range(1, 11)]  # 10 hits, one rule
    lines = render(_result(findings)).splitlines()
    shown = [
        line for line in lines if line.startswith(_FILE) and "WT1" in line and "more" not in line
    ]
    overflow = [line for line in lines if "… 2 more WT1 (--all)" in line]
    assert len(shown) == 8
    assert len(overflow) == 1


def test_fix_prints_inline_under_the_first_occurrence_only():
    """Each rule's FIX sits directly under its FIRST finding, indented; a
    later hit of the same rule is the finding line alone."""
    result = _result(
        [
            _finding("WT1", line=1),
            _finding("WT1", line=9),
            _finding("WT2", line=12),
        ]
    )
    lines = render(result).splitlines()

    first_wt1 = next(i for i, line in enumerate(lines) if line.startswith(f"{_FILE}:1 "))
    assert lines[first_wt1 + 1] == "   FIX WT1: fix WT1 by doing the WT1 thing"

    second_wt1 = next(i for i, line in enumerate(lines) if line.startswith(f"{_FILE}:9"))
    assert not lines[second_wt1 + 1].startswith("   FIX WT1")

    first_wt2 = next(i for i, line in enumerate(lines) if line.startswith(f"{_FILE}:12"))
    assert lines[first_wt2 + 1] == "   FIX WT2: fix WT2 by doing the WT2 thing"

    assert len([line for line in lines if line.strip().startswith("FIX WT1:")]) == 1


def test_no_trailing_fix_legend():
    result = _result([_finding("WT1", line=1)])
    lines = render(result).splitlines()
    assert not [line for line in lines if line.startswith("FIX ")]


def test_a_long_message_is_never_truncated():
    """The ≤240-char cap is enforced at authoring time by the rule
    contract, so the report prints every message whole."""
    message = "x" * 240
    lines = render(_result([_finding("WT1", message=message)])).splitlines()
    assert any(message in line for line in lines)
    assert "…" not in lines[0]
    assert not [line for line in lines if line.endswith("…")]


def test_scoped_output_carries_no_internal_vocabulary():
    result = _result(
        [
            _finding("WT1", line=1, severity=Severity.ERROR),
            _finding("WT2", line=2, message="a second thing", tier=Tier.PROSE),
        ]
    )
    output = render(result, suppressed=3)
    for token in _INTERNAL_VOCABULARY:
        assert token not in output, token


def test_clean_run_is_two_lines():
    output = render(_result([]))
    assert output.splitlines() == ["LINT 1 file — clean", "NEXT: nothing — clean"]


def test_next_trailer_is_the_last_line_when_findings_exist():
    output = render(_result([_finding("WT1")]))
    assert output.splitlines()[-1] == "NEXT: fix the findings above, then re-run"


def test_next_trailer_follows_the_suppressed_pointer():
    output = render(_result([_finding("WT1")]), suppressed=42)
    lines = output.splitlines()
    assert lines[-2] == "SUPPRESSED: 42 baselined findings — run: wiki drain --over"
    assert lines[-1] == "NEXT: fix the findings above, then re-run"


def test_sweep_prints_one_line_per_dirty_file():
    findings = [
        _finding("WT1", file="vault/a.md", line=1),
        _finding("WT1", file="vault/a.md", line=2),
        _finding("WT2", file="vault/a.md", line=3),
        _finding("WT3", file="vault/b.md", line=1),
    ]
    lines = render(_result(findings, files=900), sweep=True).splitlines()

    assert lines[0] == "LINT 900 files — 4 findings"
    assert lines[1] == "vault/a.md — 3 findings (WT1, WT2)"
    assert lines[2] == "vault/b.md — 1 findings (WT3)"
    assert lines[-1] == "NEXT: fix the files above one at a time — wiki lint <path>"
    assert not [line for line in lines if line.startswith("vault/a.md:")]


def test_sweep_manifest_caps_at_forty_files():
    findings = [_finding("WT1", file=f"vault/f{i:03d}.md") for i in range(45)]
    lines = render(_result(findings, files=45), sweep=True).splitlines()
    file_lines = [line for line in lines if line.startswith("vault/f")]
    assert len(file_lines) == 40
    assert "+5 more files — narrow with wiki lint <path>" in lines


def test_json_format():
    finding = _finding("WT1", file="vault/x.md", line=5, message="oops", tier=Tier.CONTENT_SHAPE)
    payload = report.finding_to_json(finding)
    assert set(payload) == {
        "rule",
        "path",
        "line",
        "message",
        "severity",
        "tier",
        "producer",
        "fixable",
    }
    assert payload["rule"] == "WT1"
    assert payload["path"] == "vault/x.md"
    assert payload["severity"] == "warning"
    assert payload["tier"] == "content-shape"


def test_exit_codes():
    """0 clean, 1 any finding (ADR-0064). Exit 2 is the CLI's own
    usage/config/internal-error code — see `test_cli_lint.py`."""
    assert report.exit_code(_result([])) == 0
    assert report.exit_code(_result([_finding("WT1", severity=Severity.WARNING)])) == 1
    assert report.exit_code(_result([_finding("WT1", severity=Severity.ERROR)])) == 1


def test_output_cap():
    findings = [_finding(f"WT-CAP-{i}", line=i + 1, message=f"finding {i}") for i in range(50)]
    lines = render(_result(findings)).splitlines()
    assert len(lines) <= 40


def test_guide_pointer(tmp_path, monkeypatch):
    guide_dir = tmp_path / "vault" / "refs" / "lint"
    guide_dir.mkdir(parents=True)
    guide_path = guide_dir / "wt1.md"
    guide_path.write_text("guidance", encoding="utf-8")
    monkeypatch.setattr(report, "GUIDE_DIR", guide_dir)

    result = _result([_finding("WT1", line=1)], files=1)
    lines = render(result).splitlines()
    assert f"GUIDE: {guide_path}" in lines


def test_guide_pointer_absent_when_multiple_files_targeted(tmp_path, monkeypatch):
    guide_dir = tmp_path / "vault" / "refs" / "lint"
    guide_dir.mkdir(parents=True)
    (guide_dir / "wt1.md").write_text("guidance", encoding="utf-8")
    monkeypatch.setattr(report, "GUIDE_DIR", guide_dir)

    result = _result([_finding("WT1", line=1)], files=2)
    lines = render(result).splitlines()
    assert not any(line.startswith("GUIDE:") for line in lines)


def test_every_reportable_rule_id_has_fix_text() -> None:
    """No rule id the report can print falls through to the placeholder —
    registered rule classes and external-producer ids alike (the producers
    are plain functions, so their ids reach the inline FIX via
    `RULE_DOCS`)."""
    import wiki_cli.rules  # noqa: F401  — populates the registry
    from wiki_cli.contracts import all_rules
    from wiki_cli.producers import all_rule_docs

    ids = [rule.id for rule in all_rules()] + list(all_rule_docs())
    texts = {rule_id: report.fix_text(rule_id) for rule_id in ids}
    assert [rule_id for rule_id, text in texts.items() if "no fix guidance registered" in text] == []
    assert [rule_id for rule_id, text in texts.items() if len(text) < 20] == []


def test_no_fix_text_exceeds_the_inline_cap() -> None:
    """A FIX prints inline under its finding, so it stays one readable
    imperative line (ADR-0064's ≤240 chars)."""
    import wiki_cli.rules  # noqa: F401  — populates the registry
    from wiki_cli.contracts import all_rules
    from wiki_cli.producers import all_rule_docs

    ids = [rule.id for rule in all_rules()] + list(all_rule_docs())
    assert [rule_id for rule_id in ids if len(report.fix_text(rule_id)) > 240] == []


def test_fixed_block_is_capped_like_the_manifest():
    """A sweep repairs hundreds of files; the FIXED preamble caps so it
    never buries the findings it precedes."""
    fixed = {f"vault/f{i:03d}.md": 1 for i in range(45)}
    result = LintResult(
        findings=[],
        stats=RunStats(files=45, rules_run=0, cache_hits=0, seconds=0.1),
        fixed=fixed,
    )
    lines = render(result, sweep=True).splitlines()
    assert len([line for line in lines if line.startswith("FIXED vault/")]) == 40
    assert "FIXED +5 more files — see git diff" in lines
