"""oxlint producer (W82): shells the same config the legacy JS engine used
for JS/mjs lint (`utils/scripts/lib/lint-findings.mjs`'s `runOxlint`), but
the `oxlint` binary itself comes from the `oxlint` PyPI package (a Python
wrapper distributing the standalone Rust binary) — `uv add oxlint` installs
it into the venv, so linting no longer depends on `npm install`.

Foreign tool, so its own `--format=json` shape is normalized here rather
than at the source the way this repo's own scripts emit the shared payload
directly. `caller`-supplied `targets` decide scope — per the migration
audit (`utils/wiki-cli/rules-audit.md`), that is `utils/scripts/**` and any
other surviving JS/TS in the repo, "keep for the surviving codebase" now
that the JS lint pipeline itself is retired (ADR-0041).
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, Finding, ProducerRuleDoc, Severity, Tier

FAMILY_ID = "W82"
VERSION = "1"
PURE = True

_OXLINT_CONFIG = ".oxlintrc.json"
"""oxlint auto-discovers this at the repo root (no `--config` flag). Its
size+mtime is this producer's whole out-of-file config key; a repo without
one fingerprints as absent."""


def config_fingerprint(repo_root: Path) -> str:
    path = repo_root / _OXLINT_CONFIG
    try:
        stat = path.stat()
    except OSError:
        return "absent"
    return f"{stat.st_size}:{stat.st_mtime_ns}"


RULE_DOCS: tuple[ProducerRuleDoc, ...] = (
    ProducerRuleDoc(
        id=FAMILY_ID,
        tier=Tier.STRUCTURAL,
        severity=Severity.ERROR,
        fix=(
            "Fix the JS/mjs defect the slug at the head of the message names (e.g. "
            "`no-unused-vars`): run `node_modules/.bin/oxlint <path> --fix` for the mechanical "
            "ones, hand-fix the rest the same turn. An `oxlint-disable` comment is not a fix."
        ),
    ),
)

_CODE_SLUG_RE = re.compile(r"\(([^)]+)\)")
"""oxlint's `code` field arrives as `"eslint(no-unused-vars)"` — the inner
name is the rule a reader would search for, so it becomes the slug."""

_JS_SUFFIXES = frozenset({".js", ".mjs"})
"""The orchestrator hands every producer the same `targets` list regardless
of file type (`markdownlint.py` and `links.py` self-filter the same way).
oxlint has no built-in "not my file type, skip silently" behavior: given a
non-JS target it prints `No files found to lint...` ahead of the JSON on
stdout, corrupting the parse below. Filtering to JS/mjs here — not to a
`utils/scripts/` directory prefix — matches the migration audit's "keep for
the surviving codebase" scope: whatever JS remains anywhere in the repo,
not only that one directory."""


def autofix(targets: list[Path]) -> None:
    """Apply `oxlint --fix` to `targets`, in place.

    oxlint's own fixer covers the mechanical half of this family (unused
    imports, `prefer-const`, formatting-shaped lints), which is exactly the
    half the `RULE_DOCS` fix line already told an agent to run by hand.
    Called by `wiki_cli.autofix`, which has already dropped
    `docs/guardrails/**` and honours `--no-fix`/`--json`. A missing binary
    or a non-zero exit is not raised here: `run` reports the same targets
    moments later and surfaces the real state.
    """
    js_targets = [target for target in targets if target.suffix in _JS_SUFFIXES]
    if not js_targets:
        return

    binary = shutil.which("oxlint")
    if binary is None:
        return

    subprocess.run(
        [binary, *[str(target) for target in js_targets], "--fix"],
        capture_output=True,
        text=True,
        check=False,
    )


def run(config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]:
    """Run oxlint over `targets`.

    `targets` are absolute paths under the repo. The subprocess is invoked
    exactly like the legacy engine's `runOxlint`: same config
    (`.oxlintrc.json`, auto-discovered — no `--config` flag, cwd is the
    repo root), file arguments relative to that cwd. The binary itself
    comes from the `oxlint` PyPI package installed in this venv, resolved
    via `shutil.which` rather than a `node_modules/.bin/` path. An empty
    `targets` list, or a list with no JS/mjs file in it, is a no-op —
    unlike markdownlint-obsidian, oxlint given zero file arguments still
    only lints its own default globs, but an explicit empty scope from a
    caller of this function means lint nothing, not fall back to a
    default.
    """
    del config  # this producer's invocation is fully determined by the shared config file on disk
    js_targets = [target for target in targets if target.suffix in _JS_SUFFIXES]
    if not js_targets:
        return []

    repo_root = corpus.repo_root
    binary = shutil.which("oxlint")
    if binary is None:
        raise FileNotFoundError(
            "oxlint binary not found on PATH — install it: `uv add oxlint`"
        )

    rel_args = [str(target.resolve().relative_to(repo_root)) for target in js_targets]
    result = subprocess.run(
        [binary, *rel_args, "--format=json"],
        cwd=repo_root,
        capture_output=True,
        text=True,
        check=False,
    )
    try:
        payload = json.loads(result.stdout)
    except json.JSONDecodeError as error:
        raise RuntimeError(
            f"oxlint output unparseable ({error}); "
            f"first 300 bytes of stdout: {result.stdout[:300]!r}; "
            f"stderr: {result.stderr[:300]!r}"
        ) from error

    findings: list[Finding] = []
    for diagnostic in payload.get("diagnostics") or []:
        rel_path = diagnostic.get("filename")
        if not rel_path:
            continue
        code = diagnostic.get("code") or ""
        match = _CODE_SLUG_RE.search(code)
        slug = match.group(1) if match else (code or "oxlint")
        message = diagnostic.get("message", "")
        help_text = diagnostic.get("help")
        if help_text:
            message = f"{message} — {help_text}"
        severity = Severity.WARNING if diagnostic.get("severity") == "warning" else Severity.ERROR
        line = 1
        labels = diagnostic.get("labels") or []
        if labels:
            span = labels[0].get("span") or {}
            line = int(span.get("line") or 1)
        findings.append(
            Finding(
                rule_id=FAMILY_ID,
                file=rel_path,
                line=line,
                message=f"{slug}: {message}",
                severity=severity,
                tier=Tier.STRUCTURAL,
                producer="oxlint",
                fixable=False,
            )
        )
    return findings
