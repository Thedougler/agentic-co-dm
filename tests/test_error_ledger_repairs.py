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
                "lifecycle: proposed\n"
                "reveal: unrevealed\n"
                "---\n\n# Note\n",
                encoding="utf-8",
            )
            other = temp / "other.md"
            other.write_text(note.read_text(encoding="utf-8"), encoding="utf-8")

            scripts = [
                "scripts/lint-wiki-write",
                "scripts/lint-obsidian-markdown",
                "scripts/lint-literal-newlines",
            ]
            for script in scripts:
                with self.subTest(script=script, form="positional-file"):
                    self.assertEqual(run([str(ROOT / script), str(note)]).returncode, 0)
                with self.subTest(script=script, form="flag-file"):
                    self.assertEqual(run([str(ROOT / script), "--path", str(note)]).returncode, 0)
                with self.subTest(script=script, form="positional-directory"):
                    self.assertEqual(run([str(ROOT / script), str(scope)]).returncode, 0)
                with self.subTest(script=script, form="equal-dual"):
                    result = run([str(ROOT / script), str(note), "--path", str(note)])
                    self.assertEqual(result.returncode, 0)
                with self.subTest(script=script, form="missing"):
                    result = run([str(ROOT / script), str(temp / "missing.md")])
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("path not found", result.stderr)
                with self.subTest(script=script, form="conflict"):
                    result = run([str(ROOT / script), str(note), "--path", str(other)])
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("different paths", result.stderr)


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
