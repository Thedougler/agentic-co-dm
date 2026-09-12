"""Ported from npm's W108 (`utils/scripts/lint-rules/w108-guardrail-id-resolves.mjs`).

A guardrail checklist ID that does not resolve, or that exists twice.
`_FORMAT.md` F12:

    F12. Checklist IDs (P1.., C1.., D1.., V1.., E1.., S1.., F1.., M1..,
         RS1.., T-rows) are stable forever — never renumber, never reuse a
         retired ID. ... Compliance is cited by ID + one line of evidence.

F12 makes an ID a permanent address, which is exactly what makes a
dangling one diagnostic. Two directions, one module (they share the ID
table):

  A. A reference `<X>.md <ID>` naming an ID that doc does not define.
     Fires on the referencing line, across every agent-facing path that
     cites kit IDs — `docs/guardrails/`, `.claude/skills/*/(SKILL.md|
     references/**)`, `.claude/rules/`, `vault/refs/`, and any `CLAUDE.md`.
  B. An ID defined twice, in the same doc or across two. Fires on the
     second definition, ordered by file then line. NOT exempted for F15
     archives (only direction A is — an archive still may not silently
     redefine a live ID).

The ID table is built once per repo root by reading `docs/guardrails/*.md`
directly off disk (not via the `Corpus`'s vault-only page index, which
never reaches non-vault paths). `MIGRATION-LOG.md` and `PROJECT-NOTES.md`
are excluded as reference SOURCES only (F15: an archive entry quoting a
since-retired ID is the record working, not rot) — they are still scanned
for ID *definitions* like any other guardrails doc.

Not pure — a `VaultRule`: the table and the reference sweep depend on the
whole repo tree, not one file's bytes.
"""

from __future__ import annotations

import os
import re
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register

_GUARDRAILS_DIR = "docs/guardrails"
_F15_ARCHIVES = frozenset({"MIGRATION-LOG.md", "PROJECT-NOTES.md"})
_FORMAT_DOC = "docs/guardrails/_FORMAT.md"

_SCOPED_PATH_RE = re.compile(
    r"(^|/)(docs/guardrails/|\.claude/skills/[^/]+/(SKILL\.md|references/)|"
    r"\.claude/rules/|vault/refs/)|(^|/)CLAUDE\.md$"
)
_DEFINITION_RE = re.compile(r"^-\s+([A-Z]{1,3}\d+)\.\s")
_REFERENCE_RE = re.compile(r"(?:docs/guardrails/)?\b([A-Z][A-Z_-]*\.md)\s+([A-Z]{1,3}\d+)\b")

_EXCLUDED_DIR_NAMES = frozenset(
    {"node_modules", ".git", "dist", "build", ".venv", "__pycache__", ".wiki-cli", "coverage"}
)


def _find_claude_md_files(repo_root: Path) -> list[Path]:
    """Every `CLAUDE.md` under `repo_root`, pruning heavy/vendored dirs a
    plain `rglob` would otherwise walk into (matches `**/CLAUDE.md`)."""
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(repo_root):
        dirnames[:] = [d for d in dirnames if d not in _EXCLUDED_DIR_NAMES]
        if "CLAUDE.md" in filenames:
            found.append(Path(dirpath) / "CLAUDE.md")
    return found


def _scoped_candidates(repo_root: Path) -> list[Path]:
    """Every real file the legacy engine's `skills` config globs reach —
    the file set `SCOPED_PATH` is checked against."""
    candidates: set[Path] = set()
    candidates.update(repo_root.glob("docs/guardrails/*.md"))
    candidates.update(_find_claude_md_files(repo_root))
    candidates.update(repo_root.glob(".claude/skills/*/SKILL.md"))
    candidates.update(repo_root.glob(".claude/skills/*/references/**/*.md"))
    candidates.update(repo_root.glob(".claude/rules/*.md"))
    candidates.update(repo_root.glob("vault/refs/**/*.md"))
    return sorted(candidates)


def _id_table(repo_root: Path) -> tuple[dict[str, set[str]], list[tuple[str, str, int, str]]]:
    """(by_doc, duplicates). `by_doc`: guardrails-doc basename -> set of IDs
    it defines. `duplicates`: (id, file, line, other_where) for every
    second-or-later definition, ordered by file then line (dict iteration
    order over `sorted(files)` below preserves that)."""
    by_doc: dict[str, set[str]] = {}
    first: dict[str, str] = {}
    duplicates: list[tuple[str, str, int, str]] = []

    guardrails_dir = repo_root / _GUARDRAILS_DIR
    try:
        files = sorted(p.name for p in guardrails_dir.iterdir() if p.suffix == ".md")
    except OSError:
        return by_doc, duplicates  # No guardrails dir (a fixture vault): every check silent.

    for file_name in files:
        ids: set[str] = set()
        by_doc[file_name] = ids
        try:
            lines = (guardrails_dir / file_name).read_text(encoding="utf-8").split("\n")
        except OSError:
            continue
        for index, line in enumerate(lines):
            match = _DEFINITION_RE.match(line)
            if not match:
                continue
            rule_id = match.group(1)
            ids.add(rule_id)
            where = f"{file_name}:{index + 1}"
            if rule_id in first:
                duplicates.append((rule_id, file_name, index + 1, first[rule_id]))
            else:
                first[rule_id] = where

    return by_doc, duplicates


@register
class GuardrailIdResolvesRule(VaultRule):
    """Ported from npm's W108 (`utils/scripts/lint-rules/w108-guardrail-id-resolves.mjs`)."""

    id = "W108"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Point the reference at an ID that exists there, or rename the duplicate "
        "definition to the next free ID in its prefix series."
    )
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        repo_root = corpus.repo_root
        by_doc, duplicates = _id_table(repo_root)
        if not by_doc:
            return

        # Direction B — a second definition of an ID. Not F15-exempted.
        for rule_id, file_name, line, other in duplicates:
            yield self.finding(
                file=f"{_GUARDRAILS_DIR}/{file_name}",
                line=line,
                message=(
                    f"{rule_id} is defined twice ({other}) — rename one to the next free "
                    f"ID in its prefix series ({_FORMAT_DOC} F12: never renumber, never reuse)"
                ),
            )

        # Direction A — every `<X>.md <ID>` reference in every scoped file.
        for path in _scoped_candidates(repo_root):
            try:
                rel_path = str(path.relative_to(repo_root))
            except ValueError:
                continue
            basename = rel_path.rsplit("/", 1)[-1]
            in_guardrails = f"/{_GUARDRAILS_DIR}/" in f"/{rel_path}"
            if in_guardrails and basename in _F15_ARCHIVES:
                continue

            try:
                lines = path.read_text(encoding="utf-8").split("\n")
            except OSError:
                continue
            for index, line in enumerate(lines):
                for match in _REFERENCE_RE.finditer(line):
                    doc_file, ref_id = match.group(1), match.group(2)
                    ids = by_doc.get(doc_file)
                    if ids is None:
                        continue  # not a guardrails doc — out of this rule's standing
                    if ref_id in ids:
                        continue
                    known = ", ".join(sorted(ids)[:5]) or "none"
                    yield self.finding(
                        file=rel_path,
                        line=index + 1,
                        column=line.index(match.group(0)) + 1,
                        message=(
                            f"reference to {doc_file} {ref_id} does not resolve — point it at "
                            f"an ID that exists there (defined: {known}) or add the rule; F12 "
                            "makes IDs stable forever, so an unresolved one means a renumber "
                            "happened"
                        ),
                    )
