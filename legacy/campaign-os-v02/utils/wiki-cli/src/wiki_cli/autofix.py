"""The autofix pass: every mechanical repair, applied before rules judge
the file (ADR-0064).

A finding an agent can only act on by re-typing a deterministic transform
is a finding that should never have been printed. So each target file is
repaired first — every registered `Autofix` (`contracts.Autofix`) plus each
external tool's own fix mode — the repaired text is written back, and only
then do the rules evaluate. A defect the pass removed is simply gone from
the report; the file's new state is announced once, so an agent holding a
stale in-context copy knows to Read it again.

Two rules govern what the pass touches:

- `docs/guardrails/**` is never autofixed. Those files carry `_FORMAT.md`
  F15 version-bump pairs, so a byte written by anything other than the
  editing agent desynchronises the pair.
- The pass runs at most `MAX_PASSES` rounds over one file. Each `Autofix`
  is idempotent on its own (`tests/test_rule_contract.py`), so the rounds
  exist only to settle one fix uncovering another's input; a file still
  changing after the cap keeps its last state and the remaining defects
  report normally.

`Autofix.apply` is `str -> str`, which is what makes it testable in
isolation. A repair needing the file's path (a rule scoped to `vault/`) or
the corpus (a link whose correct target is another page's frontmatter)
reads them from `current_context()` — a `ContextVar` this module sets
around every `apply` call. Outside the pass the context is `None`, and such
an `Autofix` returns its input unchanged rather than guessing.
"""

from __future__ import annotations

import hashlib
import importlib
from collections.abc import Callable, Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

from wiki_cli.contracts import all_rules

if TYPE_CHECKING:
    from wiki_cli.contracts import Corpus

ToolAutofix = Callable[[list[Path]], None]
"""A producer module's own fix mode: repair these paths in place."""

GUARDRAILS_PREFIX = "docs/guardrails/"
"""Never autofixed — see the module docstring."""

MAX_PASSES = 3
"""Rounds over one file before the pass gives up and lets the rules report."""

REWRITTEN_LINE = "FILE REWRITTEN by autofix — Read it again"
"""Printed once per report whenever any file was rewritten."""


@dataclass(frozen=True)
class FixContext:
    """What an `Autofix` may know beyond the text it is repairing."""

    rel_path: str
    corpus: Corpus | None = None


_CONTEXT: ContextVar[FixContext | None] = ContextVar("wiki_cli_fix_context", default=None)


def current_context() -> FixContext | None:
    """The file being repaired, or None when `apply` runs outside the pass."""
    return _CONTEXT.get()


@contextmanager
def fixing(context: FixContext) -> Iterator[None]:
    """Bind `context` for every `Autofix.apply` called inside the block."""
    token = _CONTEXT.set(context)
    try:
        yield
    finally:
        _CONTEXT.reset(token)


def is_exempt(rel_path: str) -> bool:
    """True for a path the pass must leave byte-identical."""
    return rel_path.replace("\\", "/").startswith(GUARDRAILS_PREFIX)


def repair_text(
    rel_path: str,
    text: str,
    corpus: Corpus | None = None,
    allowed_producers: set[str] | None = None,
) -> tuple[str, int]:
    """Apply every registered `Autofix` to `text` until it stops changing.

    Returns the repaired text and how many distinct rules changed it. Pure
    over `text` — the caller owns the write. `allowed_producers` mirrors
    `run_lint`'s own execution gating: a run narrowed to one producer
    repairs only that producer's defects.
    """
    import wiki_cli.rules  # noqa: F401  registers every rule; imported here because a rule module imports this one

    rules = [
        (rule.id, rule.autofix)
        for rule in all_rules()
        if rule.autofix is not None
        and (allowed_producers is None or rule.producer in allowed_producers)
    ]
    if not rules:
        return text, 0

    changed_by: set[str] = set()
    current = text
    with fixing(FixContext(rel_path=rel_path, corpus=corpus)):
        for _round in range(MAX_PASSES):
            before_round = current
            for rule_id, autofix in rules:
                after = autofix.apply(current)
                if after != current:
                    changed_by.add(rule_id)
                    current = after
            if current == before_round:
                break
    return current, len(changed_by)


def _tool_autofixers(allowed: set[str] | None) -> list[tuple[str, ToolAutofix]]:
    """(family id, module-level `autofix` callable) for every producer that
    declares one — pymarkdown's fix mode, oxlint's `--fix`. A producer
    without an `autofix` attribute simply has no fix mode."""
    from wiki_cli.producers import all_producer_meta  # see repair_text

    found: list[tuple[str, ToolAutofix]] = []
    for family_id, meta in sorted(all_producer_meta().items()):
        if allowed is not None and family_id not in allowed:
            continue
        module = importlib.import_module(meta.run.__module__)
        tool_fix = getattr(module, "autofix", None)
        if tool_fix is not None:
            found.append((family_id, tool_fix))
    return found


def _digest(path: Path) -> str | None:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return None


def run_autofix(
    git_root: Path,
    rel_paths: list[str],
    corpus: Corpus | None = None,
    allowed_producers: set[str] | None = None,
) -> dict[str, int]:
    """Repair every non-exempt target in place.

    Returns `{rel_path: fixes applied}` for the files actually rewritten —
    the report's `FIXED` lines. A file the pass could not read or write is
    skipped silently: an unreadable target is the rules' finding to make,
    never a crash that costs the whole run.
    """
    targets = [rp for rp in rel_paths if not is_exempt(rp)]
    if not targets:
        return {}

    fixed: dict[str, int] = {}

    for rel in targets:
        path = git_root / rel
        try:
            original = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        repaired, count = repair_text(rel, original, corpus, allowed_producers)
        if repaired == original or count == 0:
            continue
        try:
            path.write_text(repaired, encoding="utf-8")
        except OSError:
            continue
        fixed[rel] = count

    tool_targets = [git_root / rel for rel in targets]
    before = {path: _digest(path) for path in tool_targets}
    for _family_id, tool_fix in _tool_autofixers(allowed_producers):
        tool_fix(tool_targets)
    for path in tool_targets:
        after = _digest(path)
        if after is None or after == before[path]:
            continue
        rel = str(path.relative_to(git_root))
        fixed[rel] = fixed.get(rel, 0) + 1

    return fixed
