from __future__ import annotations

import hashlib
import json
import os
import stat
import subprocess
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PYTHON = os.environ.get("PYTHON", "python3")


def run(command: list[str], *, cwd: Path = ROOT, env: dict[str, str] | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=cwd, env=env, capture_output=True, text=True)


class LintScopeTests(unittest.TestCase):
    def test_all_lint_clis_accept_both_scope_forms_and_reject_conflicts(self) -> None:
        with tempfile.TemporaryDirectory(prefix=".ledger-lint-", dir=ROOT) as raw:
            temp = Path(raw)
            scope = temp / "scope"
            scope.mkdir()
            note = scope / "note.md"
            note.write_text(
                "---\n"
                "title: Note\n"
                "category: journal\n"
                "tags: []\n"
                "sources: []\n"
                "created: 2026-09-16\n"
                "updated: 2026-09-16\n"
                "type: session\n"
                "reveal: unrevealed\n"
                "---\n\n# Note\n",
                encoding="utf-8",
            )
            other = temp / "other.md"
            other.write_text(note.read_text(encoding="utf-8"), encoding="utf-8")

            env = os.environ | {"OBSIDIAN_VAULT_PATH": str(temp), "WIKI_TRACKER_ROOT": str(temp)}
            env.pop("CI", None)
            with self.subTest(script="scripts/wiki lint", form="positional-file"):
                result = run([str(ROOT / "scripts/wiki"), "lint", "scope/note.md"], env=env)
                self.assertIn(result.returncode, (0, 1), result.stderr)
                self.assertEqual(json.loads(result.stdout)["files_checked"], 1)
            with self.subTest(script="scripts/wiki lint", form="missing"):
                result = run([str(ROOT / "scripts/wiki"), "lint", "missing.md"], env=env)
                self.assertEqual(result.returncode, 2)
                self.assertIn("path not found", result.stdout)


class ManifestRecordTests(unittest.TestCase):
    def test_record_is_canonical_and_idempotent_across_path_forms(self) -> None:
        with tempfile.TemporaryDirectory(prefix=".ledger-manifest-", dir=ROOT) as raw:
            vault = Path(raw)
            source_dir = vault / "_raw"
            source_dir.mkdir()
            source = source_dir / "source.md"
            source.write_text("source content\n", encoding="utf-8")
            manifest = {
                "version": 1,
                "sources": {
                    "_raw/source.md": {
                        "content_hash": "sha256:old",
                        "last_ingested": "2026-09-15T00:00:00Z",
                        "pages_produced": ["entities/old.md"],
                    }
                },
            }
            (vault / ".manifest.json").write_text(json.dumps(manifest), encoding="utf-8")
            first = run(
                [
                    PYTHON,
                    str(ROOT / "scripts/manifest.py"),
                    "record",
                    str(vault),
                    str(source),
                    "--pages",
                    str(vault / "entities/new.md"),
                    "entities/old.md",
                ]
            )
            self.assertEqual(first.returncode, 0, first.stderr)

            second = run(
                [
                    PYTHON,
                    str(ROOT / "scripts/manifest.py"),
                    "record",
                    str(vault),
                    "_raw/source.md",
                    "--pages",
                    "entities/new.md",
                ],
                cwd=vault,
            )
            self.assertEqual(second.returncode, 0, second.stderr)

            data = json.loads((vault / ".manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(list(data["sources"]), [str(source.resolve())])
            entry = data["sources"][str(source.resolve())]
            self.assertEqual(entry["content_hash"], "sha256:" + hashlib.sha256(source.read_bytes()).hexdigest())
            self.assertEqual(entry["pages_produced"], ["entities/new.md", "entities/old.md"])
            self.assertEqual(data["stats"]["total_sources_ingested"], 1)
            self.assertEqual(data["stats"]["total_pages"], 2)

    def test_record_refreshes_hash_after_source_change_without_duplicate_rows(self) -> None:
        with tempfile.TemporaryDirectory(prefix=".ledger-manifest-", dir=ROOT) as raw:
            vault = Path(raw)
            source = vault / "source.md"
            source.write_text("one\n", encoding="utf-8")
            command = [
                PYTHON,
                str(ROOT / "scripts/manifest.py"),
                "record",
                str(vault),
                str(source),
                "--pages",
                "page.md",
            ]
            self.assertEqual(run(command).returncode, 0)
            source.write_text("two\n", encoding="utf-8")
            self.assertEqual(run(command).returncode, 0)
            data = json.loads((vault / ".manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(len(data["sources"]), 1)
            self.assertEqual(
                data["sources"][str(source.resolve())]["content_hash"],
                "sha256:" + hashlib.sha256(source.read_bytes()).hexdigest(),
            )


class QmdMaintenanceTests(unittest.TestCase):
    def test_routine_maintenance_reports_backlog_without_embedding(self) -> None:
        with tempfile.TemporaryDirectory(prefix=".ledger-qmd-", dir=ROOT) as raw:
            temp = Path(raw)
            log = temp / "calls.log"
            fake_qmd = temp / "qmd"
            fake_qmd.write_text(
                "#!/bin/sh\n"
                "printf '%s\\n' \"$*\" >> \"$QMD_TEST_LOG\"\n"
                "case \"$1\" in\n"
                "  collection) printf '%s\\n' 'wiki (qmd://wiki/)' 'shattered-sea (qmd://shattered-sea/)' 'legacy-ss (qmd://legacy-ss/)' ;;\n"
                "  status) printf '%s\\n' 'Total:    10 files indexed' 'Vectors: 2 embedded' 'Pending: 8 need embedding (run qmd embed)' 'wiki (qmd://wiki/)' 'shattered-sea (qmd://shattered-sea/)' 'legacy-ss (qmd://legacy-ss/)' ;;\n"
                "  search) printf '%s\\n' 'Hinewai wiki/entities/npc/hinewai.md' ;;\n"
                "esac\n",
                encoding="utf-8",
            )
            fake_qmd.chmod(fake_qmd.stat().st_mode | stat.S_IXUSR)
            env = os.environ.copy()
            env["PATH"] = f"{temp}:{env['PATH']}"
            env["QMD_TEST_LOG"] = str(log)
            result = run([str(ROOT / "scripts/qmd-maintain.sh")], env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("embeddings: pending 8", result.stdout)
            self.assertNotIn("embed", log.read_text(encoding="utf-8"))

            result = run([str(ROOT / "scripts/qmd-maintain.sh"), "--embed"], env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            calls = log.read_text(encoding="utf-8")
            self.assertIn("embed -c wiki --max-docs-per-batch 128 --max-batch-mb 16", calls)


if __name__ == "__main__":
    unittest.main()


LEDGER = ROOT / "scripts" / "error-ledger.py"


class ErrorLedgerTests(unittest.TestCase):
    """scripts/error-ledger.py over a scratch errors.md (contracts/error-ledger.md, data-model §1)."""

    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory(prefix=".ledger-")
        self.root = Path(self._tmp.name)
        self.addCleanup(self._tmp.cleanup)

    def ledger(self, *args: str, cwd: Path | None = None) -> tuple[int, dict]:
        proc = run([PYTHON, str(LEDGER), "--root", str(self.root), *args], cwd=cwd or self.root)
        out = proc.stdout.strip()
        try:
            data = json.loads(out) if out else {}
        except ValueError:
            data = {"raw": out}
        return proc.returncode, data

    def append(self, source: str, cause: str, sitting: str = "lint: a", *extra: str) -> tuple[int, dict]:
        return self.ledger("error", "append", "--source", source, "--cause", cause, "--sitting", sitting, *extra)

    def raw(self) -> str:
        path = self.root / "errors.md"
        return path.read_text(encoding="utf-8") if path.exists() else ""

    def test_exact_match_attaches_and_other_causes_create(self) -> None:
        code, first = self.append(".vale.ini", "Vale E100 on CoDM")
        self.assertEqual((code, first["status"], first["occurrence_index"], first["occurrences"]), (0, "created", 0, 1))
        code, same = self.append(".vale.ini", "  Vale E100 on CoDM ", "lint: b")
        self.assertEqual((same["status"], same["id"], same["occurrence_index"], same["occurrences"]),
                         ("attached", first["id"], 1, 2))
        _, reworded = self.append(".vale.ini", "Vale E100 on the CoDM style")
        self.assertEqual(reworded["status"], "created")
        self.assertNotEqual(reworded["id"], first["id"])
        _, other = self.append("scripts/wiki", "Vale E100 on CoDM")
        self.assertEqual(other["status"], "created")
        _, repeat = self.append(".vale.ini", "Vale E100 on CoDM", "lint: b")
        self.assertEqual((repeat["status"], repeat["id"]), ("already_done", first["id"]))
        entry = json.loads(self.raw().splitlines()[2])
        self.assertEqual(sorted(entry), ["cause", "evidence", "id", "source"])
        self.assertEqual(entry["evidence"][0], {"sitting": "lint: a", "detail": "Vale E100 on CoDM"})
        self.assertTrue(self.raw().startswith("# Error ledger\n\n"))

    def test_attach_within_one_source_and_refuse_across_sources(self) -> None:
        _, first = self.append(".vale.ini", "Vale E100 on CoDM")
        code, attached = self.append(".vale.ini", "Deprecated rule silenced", "lint: c", "--attach", first["id"],
                                     "--detail", "DM Thesis passed")
        self.assertEqual((code, attached["status"], attached["id"]), (0, "attached", first["id"]))
        before = self.raw()
        for target in (first["id"], "e-999"):
            code, refused = self.append("scripts/wiki", "Other", "lint: d", "--attach", target)
            self.assertEqual(code, 2)
            self.assertEqual(refused["status"], "error")
            self.assertTrue(refused["hint"] and refused["example"])
        self.assertEqual(self.raw(), before)

    def test_detach_undoes_an_attach_and_keeps_the_last_occurrence(self) -> None:
        _, first = self.append(".vale.ini", "Vale E100 on CoDM")
        self.append(".vale.ini", "Vale E100 on CoDM", "lint: b")
        code, out = self.ledger("error", "detach", "--id", first["id"], "--index", "1")
        self.assertEqual((code, out["status"], out["occurrences"]), (0, "detached", 1))
        code, out = self.ledger("error", "detach", "--id", first["id"], "--index", "1")
        self.assertEqual((code, out["status"]), (0, "already_done"))
        code, out = self.ledger("error", "detach", "--id", first["id"], "--index", "0")
        self.assertEqual(code, 2)
        self.assertIn("drain", out["hint"])

    def test_cause_fixed_flag_is_rejected_with_example(self) -> None:
        _, first = self.append(".vale.ini", "Vale E100 on CoDM")
        before = self.raw()
        code, out = self.ledger("error", "drain", "--id", first["id"], "--cause-fixed", "true")
        self.assertEqual(code, 2)
        self.assertEqual(out["error"], "--cause-fixed was removed")
        self.assertEqual(out["example"], "python3 scripts/error-ledger.py error drain --id e-212")
        self.assertTrue(out["hint"])
        self.assertEqual(self.raw(), before)

    def test_list_reports_entries_recurrence_and_missing_sources(self) -> None:
        _, a = self.append(".vale.ini", "Vale E100 on CoDM", "lint: a")
        self.append(".vale.ini", "Vale E100 on CoDM", "lint: b")
        self.append(".vale.ini", "Vale E100 on CoDM", "lint: b", "--detail", "again")
        _, b = self.append("external:codex-cli", "usage limit", "eval: x")
        path = self.root / "errors.md"
        rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()[2:]]
        rows[1]["source"] = "scripts/no-such-script"
        path.write_text("# Error ledger\n\n" + "\n".join(json.dumps(r, sort_keys=True) for r in rows) + "\n", encoding="utf-8")
        code, out = self.ledger("error", "list")
        self.assertEqual(code, 0)
        self.assertEqual(sorted(out), ["entries", "missing_sources", "recurrence"])
        self.assertEqual(out["recurrence"], {"total": 2, "by_sitting": {"lint: b": 2}})
        self.assertEqual(out["missing_sources"], [b["id"]])
        self.assertEqual([e["id"] for e in out["entries"]], [a["id"], b["id"]])
        proc = run([PYTHON, str(LEDGER), "--root", str(self.root), "error", "list", "--ids-only"], cwd=self.root)
        self.assertEqual(proc.stdout.split(), [a["id"], b["id"]])

    def test_source_is_required_and_checked(self) -> None:
        code, out = self.ledger("error", "append", "--cause", "x", "--sitting", "s")
        self.assertEqual(code, 2)
        self.assertIn("--source", out["error"])
        self.assertTrue(out["example"])
        code, out = self.append("scripts/no-such-script", "x")
        self.assertEqual((code, out["status"]), (2, "error"))
        self.assertEqual(self.raw(), "")

    def test_drain_and_dry_run(self) -> None:
        code, planned = self.append(".vale.ini", "Vale E100 on CoDM", "lint: a", "--dry-run")
        self.assertEqual((code, planned["status"], self.raw()), (0, "planned", ""))
        _, first = self.append(".vale.ini", "Vale E100 on CoDM")
        self.append(".vale.ini", "Vale E100 on CoDM", "lint: b")
        before = self.raw()
        for args in (("detach", "--id", first["id"], "--index", "1"), ("drain", "--id", first["id"])):
            code, out = self.ledger("error", *args, "--dry-run")
            self.assertEqual((code, out["status"]), (0, "planned"))
            self.assertIn("planned", out)
            self.assertEqual(self.raw(), before)
        _, out = self.ledger("error", "drain", "--id", first["id"])
        self.assertEqual(out["status"], "drained")
        _, out = self.ledger("error", "drain", "--id", first["id"])
        self.assertEqual(out["status"], "already_done")

    def test_runs_from_any_cwd(self) -> None:
        elsewhere = self.root / "deep" / "dir"
        elsewhere.mkdir(parents=True)
        proc = run([PYTHON, str(LEDGER), "error", "list"], cwd=elsewhere)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertIn("entries", json.loads(proc.stdout))
