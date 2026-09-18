from __future__ import annotations

import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path

from tools.wiki_ops.index_ops import insert_index_entry, remove_index_entry, replace_index_entry
from tools.wiki_ops.identity import resolve_identity, scan_identities
from tools.wiki_ops.manifest_ops import ManifestTransition, apply_transition
from tools.wiki_ops.mutations import MutationOp, apply_mutation, parse_sections, section_hash
from tools.wiki_ops.template_contracts import check_conformance, load_contract
from tools.wiki_ops.scope import parse_scope
from tools.wiki_ops.transactions import Transaction



ROOT = Path(__file__).resolve().parents[1]
PYTHON = os.environ.get("PYTHON", "python3")


def run_cli(
    script: str | Path,
    *args: str,
    vault: Path | None = None,
    extra_env: dict[str, str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run a repository script with the same isolated-vault setup as bulk ops."""
    script_path = Path(script)
    if not script_path.is_absolute():
        script_path = ROOT / script_path if script_path.parts[:1] == ("scripts",) else ROOT / "scripts" / script_path
    command = [PYTHON, str(script_path), *args]
    environment = os.environ | (extra_env or {})
    if vault is not None:
        environment["OBSIDIAN_VAULT_PATH"] = str(vault)
    return subprocess.run(command, cwd=ROOT, capture_output=True, text=True, env=environment)


def assert_json(result: subprocess.CompletedProcess[str], *, returncode: int = 0) -> dict:
    """Assert a command's public exit/JSON contract and return its object payload."""
    assert result.returncode == returncode, result.stderr or result.stdout
    assert result.stdout.strip(), result.stderr or "command produced no JSON"
    payload = json.loads(result.stdout)
    assert isinstance(payload, dict)
    return payload


def assert_status(
    result: subprocess.CompletedProcess[str],
    status: str,
    *,
    returncode: int = 0,
) -> dict:
    payload = assert_json(result, returncode=returncode)
    assert payload.get("status") == status, payload
    return payload


def assert_file(path: Path, *, text: str | None = None, exists: bool = True) -> None:
    """Assert observable file existence and, when provided, its complete text."""
    assert path.exists() is exists, path
    if exists and text is not None:
        assert path.read_text(encoding="utf-8") == text


class VaultFixture(unittest.TestCase):
    """Temporary vault and public-outcome assertions for subprocess stories."""

    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory(prefix="wiki-ops-")
        self.vault = Path(self.tempdir.name)

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def page(self, relative: str, text: str | bytes) -> Path:
        path = self.vault / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(text, bytes):
            path.write_bytes(text)
        else:
            path.write_text(text, encoding="utf-8")
        return path

    def assert_json(self, result: subprocess.CompletedProcess[str], *, returncode: int = 0) -> dict:
        return assert_json(result, returncode=returncode)

    def assert_status(
        self,
        result: subprocess.CompletedProcess[str],
        status: str,
        *,
        returncode: int = 0,
    ) -> dict:
        return assert_status(result, status, returncode=returncode)

    def assert_file(self, path: Path, *, text: str | None = None, exists: bool = True) -> None:
        assert_file(path, text=text, exists=exists)


FIXTURE = Path(__file__).parent / "fixtures" / "wiki_ops"

def test_cli_contracts_and_environment_discovery():
    for script in ("scripts/wiki-bulk-ops", "scripts/wiki-lint", "scripts/wiki-identity"):
        result = run_cli(script, "--help")
        assert result.returncode == 0
        assert "usage:" in result.stdout

def test_identity_cli_json_and_ambiguous_status():
    result = run_cli("scripts/wiki-identity", "scan", "--json", vault=FIXTURE)
    payload = assert_json(result, returncode=2)
    assert payload["ambiguous"] == 2
    assert payload["scanned"] == 2


def test_scope_and_semantic_sections():
    scope = parse_scope("files:fisks-fleet.md")
    assert scope and scope.resolve(FIXTURE).resolved_files == ["fisks-fleet.md"]
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    assert section_hash(section.content) == section.hash


def test_mutation_hash_and_dry_run():
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    op = MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "Changed\n"})
    preview = apply_mutation(FIXTURE, op, dry_run=True)
    assert preview["status"] == "dry_run"
    assert "Changed" not in (FIXTURE / "fisks-fleet.md").read_text()
    bad = apply_mutation(FIXTURE, MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": "bad"}, {"content": "x"}), dry_run=True)
    assert bad["status"] == "rejected"


def test_index_and_manifest_are_structured():
    text = (FIXTURE / "index.md").read_text()
    text = replace_index_entry(text, "fisks-fleet", "- [[fisks-fleet|Fisk's Fleet]]")
    text = insert_index_entry(text, "- [[another-page]]")
    assert "Fisk's Fleet" in text
    assert "another-page" in text
    assert "fisks-captains" not in remove_index_entry(text, "fisks-captains")
    data = apply_transition({}, ManifestTransition("old.md", "merged_into", "new.md"))
    assert data["page_identity_transitions"][0]["target"] == "new.md"


def test_transaction_rejects_overlapping_mutations():
    page = (FIXTURE / "fisks-fleet.md").read_text()
    section = parse_sections(page).find(["Overview"])
    tx = Transaction(FIXTURE)
    tx.add(MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "a"}))
    tx.add(MutationOp("replace_section", "fisks-fleet.md", {"heading_path": ["Overview"], "content_hash": section.hash}, {"content": "b"}))
    assert tx.commit()["status"] == "rejected"


def test_identity_fixture_is_deterministic():
    results = scan_identities(FIXTURE)
    assert [result.path for result in results] == sorted(result.path for result in results)
    assert resolve_identity(FIXTURE, "fisks-fleet.md").status == "ambiguous"
    assert resolve_identity(FIXTURE, "fisks-fleet.md").candidates

def test_identity_only_compares_same_type(tmp_path: Path):
    base = (FIXTURE / "fisks-fleet.md").read_text()
    (tmp_path / "faction.md").write_text(base, encoding="utf-8")
    (tmp_path / "place.md").write_text(base.replace("type: faction", "type: place").replace("title: Fisk's Fleet", "title: Fisk's Harbor"), encoding="utf-8")
    assert resolve_identity(tmp_path, "faction.md").status == "resolved"

def test_identity_redirect_resolves_without_candidates(tmp_path: Path):
    page = (FIXTURE / "fisks-fleet.md").read_text()
    (tmp_path / "canonical.md").write_text(page.replace("title: Fisk's Fleet", "title: Canonical Fleet"), encoding="utf-8")
    (tmp_path / "redirect.md").write_text(
        page.replace("title: Fisk's Fleet", "title: Redirect Fleet")
        .replace("aliases:", "redirects_to: canonical.md\naliases:", 1),
        encoding="utf-8",
    )
    resolved = resolve_identity(tmp_path, "redirect.md")
    assert resolved.status == "resolved"
    assert resolved.signals["redirect_match"] is True


def test_template_contract_reports_required_sections():
    contract = load_contract(Path(__file__).parents[1] / "wiki/templates/contracts/faction.yml")
    page = "---\ntitle: Test\ntype: faction\nlifecycle: active\n---\n# Test\n"
    findings = check_conformance("test.md", page, contract)
    assert any(item["rule_id"] == "TMPL_missing_required" for item in findings)
