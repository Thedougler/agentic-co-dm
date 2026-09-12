"""TDD for the context-rot producer (W91).

Uses a throwaway `tmp_path` repo shaped like the real one (a
`utils/scripts/*.mjs` file, one config target) rather than this repo's own
tree — the producer's scan domain is path-SHAPE-driven
(`utils/scripts/**/*.mjs` + a fixed config list), and touching the real
`utils/scripts/` tree from a test would be exactly the kind of drive-by
mutation CLAUDE.md forbids.
"""

from __future__ import annotations

from datetime import UTC, datetime
from pathlib import Path

from wiki_cli.config import Config
from wiki_cli.contracts import Page
from wiki_cli.producers import all_producers
from wiki_cli.producers.context_rot import FAMILY_ID, run


class _StubCorpus:
    def __init__(self, repo_root: Path) -> None:
        self.repo_root = repo_root

    def pages(self) -> list[Page]:
        raise NotImplementedError

    def resolve(self, name: str) -> Page | None:
        raise NotImplementedError

    def by_type(self, page_type: str) -> list[Page]:
        raise NotImplementedError

    def links_from(self, rel_path: str) -> list[str]:
        raise NotImplementedError

    def links_to(self, rel_path: str) -> list[str]:
        raise NotImplementedError


def _config(repo_root: Path, *, max_age_days: str = "30") -> Config:
    return Config(
        repo_root=repo_root,
        vault_root=repo_root / "vault",
        templates_root=repo_root / "vault" / "_templates",
        cache_path=repo_root / ".wiki-cli-test-cache.sqlite3",
        scoped_roots=("vault",),
        report_cap=50,
        fingerprint="test-fingerprint",
        _thresholds={"TRANSIENT_MARKER_MAX_AGE_DAYS": max_age_days},
    )


def _write(repo_root: Path, rel: str, content: str) -> Path:
    path = repo_root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_family_id_is_w91() -> None:
    assert FAMILY_ID == "W91"


def test_registers_in_producers_registry() -> None:
    assert all_producers()["W91"] is run


def test_undated_marker_fires(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "utils/scripts/sample.mjs",
        "// TEMPORARY: skip this check for now\nexport const x = 1;\n",
    )
    findings = run(_config(tmp_path), [], _StubCorpus(tmp_path))

    assert len(findings) == 1
    finding = findings[0]
    assert finding.rule_id == "W91"
    assert finding.producer == "context-rot"
    assert finding.tier.value == "structural"
    assert finding.severity.value == "warning"
    assert finding.file == "utils/scripts/sample.mjs"
    assert finding.line == 1
    assert "no date" in finding.message


def test_recently_dated_marker_does_not_fire(tmp_path: Path) -> None:
    today = datetime.now(UTC).strftime("%Y-%m-%d")
    _write(
        tmp_path,
        "utils/scripts/sample.mjs",
        f"// TEMPORARY ({today}): skip this check\nexport const x = 1;\n",
    )
    findings = run(_config(tmp_path, max_age_days="30"), [], _StubCorpus(tmp_path))

    assert findings == []


def test_expired_dated_marker_fires(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "utils/scripts/sample.mjs",
        "// TEMPORARY (2020-01-01): skip this check\nexport const x = 1;\n",
    )
    findings = run(_config(tmp_path, max_age_days="30"), [], _StubCorpus(tmp_path))

    assert len(findings) == 1
    assert "days old" in findings[0].message
    assert "2020-01-01" in findings[0].message


def test_definition_line_never_fires(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "utils/scripts/sample.mjs",
        '// DEFAULT_PHRASES lists TEMPORARY, TODO:, and FIXME as markers\n'
        "export const x = 1;\n",
    )
    findings = run(_config(tmp_path), [], _StubCorpus(tmp_path))

    assert findings == []


def test_quoted_citation_never_fires(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "utils/scripts/sample.mjs",
        '// a comment noting "TODO:" is a marker phrase, not making one\n'
        "export const x = 1;\n",
    )
    findings = run(_config(tmp_path), [], _StubCorpus(tmp_path))

    assert findings == []


def test_config_target_ini_comment_fires(tmp_path: Path) -> None:
    _write(
        tmp_path,
        ".vale.ini",
        "; TODO: re-enable this style once the false positives are fixed\n"
        "[*.md]\n",
    )
    findings = run(_config(tmp_path), [], _StubCorpus(tmp_path))

    assert len(findings) == 1
    assert findings[0].file == ".vale.ini"


def test_legacy_self_path_excluded(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "utils/scripts/lint-context-rot.mjs",
        "// for now, this file cites TODO: as an example marker\n",
    )
    findings = run(_config(tmp_path), [], _StubCorpus(tmp_path))

    assert findings == []


def test_narrowed_targets_scope_to_named_file_only(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "utils/scripts/sample.mjs",
        "// TEMPORARY: skip this check\nexport const x = 1;\n",
    )
    _write(
        tmp_path,
        "utils/scripts/other.mjs",
        "// TEMPORARY: another undated marker\nexport const y = 2;\n",
    )

    findings = run(
        _config(tmp_path), [tmp_path / "utils/scripts/sample.mjs"], _StubCorpus(tmp_path)
    )

    assert len(findings) == 1
    assert findings[0].file == "utils/scripts/sample.mjs"


def test_out_of_domain_targets_fall_back_to_full_default_scan(tmp_path: Path) -> None:
    """A caller linting only vault pages (this producer's domain never
    intersects that) still gets the full sub-second scan — matching "rides
    every sweep", not silently skipped."""
    _write(
        tmp_path,
        "utils/scripts/sample.mjs",
        "// TEMPORARY: skip this check\nexport const x = 1;\n",
    )
    _write(tmp_path, "vault/note.md", "---\ntype: note\n---\n\nbody\n")

    findings = run(_config(tmp_path), [tmp_path / "vault/note.md"], _StubCorpus(tmp_path))

    assert len(findings) == 1
    assert findings[0].file == "utils/scripts/sample.mjs"


def test_clean_file_yields_no_findings(tmp_path: Path) -> None:
    _write(
        tmp_path,
        "utils/scripts/sample.mjs",
        "// a perfectly ordinary comment\nexport const x = 1;\n",
    )
    findings = run(_config(tmp_path), [], _StubCorpus(tmp_path))

    assert findings == []
