"""The lint baseline: a suppression list with a legible over-floor view
(ADR-0062).

`.claude/wiki-baseline.json` holds a per-file, per-rule floor on
warning-severity finding counts. Error severity is a presence gate and is
never baselined.

The floor is read three ways:

- `partition` splits a sweep's findings into what a report shows and how
  many it suppresses. A (file, rule) pair's first `floor` warnings are old
  debt and are suppressed; anything past the floor is the actionable
  queue and is shown.
- `over_entries` names every (file, rule) pair above its floor with its
  delta — the triage list `wiki drain --over` prints. `check` and
  `ratchet_token` are thin wrappers over it.
- `auto_sync_down` runs after every `wiki sweep`: it lowers each entry
  to `min(live, floor)` and drops entries for files no longer in the
  corpus, so the floor follows reality without a fixing agent ever
  touching the file.

A floor rises only through `seed`/`promote` (`wiki debt accept --force`) —
orchestrator/human maintenance, never part of a fixing agent's task.

JSON shape (flat):

    {"<rel_path>": {"<rule_id>": <count>, ...}, ...}
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import TYPE_CHECKING

from wiki_cli.contracts import Severity

if TYPE_CHECKING:
    from collections.abc import Iterable, Sequence

    from wiki_cli.contracts import Finding

BASELINE_PATH = Path(".claude/wiki-baseline.json")
"""Repo-root-relative path to the baseline file."""


def load_baseline(repo_root: Path) -> dict[str, dict[str, int]]:
    """The current floor, or `{}` when no baseline has ever been seeded."""
    path = repo_root / BASELINE_PATH
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def save_baseline(repo_root: Path, data: dict[str, dict[str, int]]) -> None:
    """Write `data` with sorted file and rule keys, creating the parent
    directory (`.claude/`) if needed."""
    path = repo_root / BASELINE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def _live_counts(findings: Sequence[Finding]) -> dict[str, dict[str, int]]:
    """Warning-severity finding counts per file per rule. Error severity is
    a presence gate elsewhere and never counts toward the ratchet."""
    counts: dict[str, dict[str, int]] = {}
    for finding in findings:
        if finding.severity is not Severity.WARNING:
            continue
        rules = counts.setdefault(finding.file, {})
        rules[finding.rule_id] = rules.get(finding.rule_id, 0) + 1
    return counts


def auto_sync_down(
    repo_root: Path, findings: list[Finding], corpus: Iterable[str] | None = None
) -> None:
    """Lower every existing baseline entry to `min(live, floor)`, and drop
    any entry whose file is absent from `corpus` (deleted or renamed — its
    floor would otherwise linger forever, while the file's new path counts
    as fully over floor). Never raises a floor and never creates a new
    entry — a rule/file pair absent from the baseline stays absent until
    `seed`/`promote` adds it.

    Call this only with `findings` and `corpus` from a COMPLETE corpus pass
    (`wiki sweep`). A scoped run's `findings` covers just its targets, and
    the live 0 it reports for every other file reads here as "fixed".
    """
    baseline = load_baseline(repo_root)
    if not baseline:
        return
    live = _live_counts(findings)
    known = None if corpus is None else set(corpus)
    for rel_path in list(baseline):
        if known is not None and rel_path not in known:
            del baseline[rel_path]
            continue
        rules = baseline[rel_path]
        for rule_id in list(rules):
            live_count = live.get(rel_path, {}).get(rule_id, 0)
            floor = min(live_count, rules[rule_id])
            if floor <= 0:
                del rules[rule_id]
            else:
                rules[rule_id] = floor
        if not rules:
            del baseline[rel_path]
    save_baseline(repo_root, baseline)


def over_entries(
    repo_root: Path, findings: list[Finding], *, only_paths: Iterable[str] | None = None
) -> list[tuple[str, str, int]]:
    """Every `(rel_path, rule_id, delta)` whose live warning count exceeds
    its floor, `delta` being how far above. A missing floor entry is floor
    0. `only_paths` restricts the comparison to those rel_paths — what a
    scoped run needs, so its verdict covers exactly its own targets.

    Sorted by descending delta, then path, then rule id.
    """
    baseline = load_baseline(repo_root)
    live = _live_counts(findings)
    scope = None if only_paths is None else set(only_paths)
    entries: list[tuple[str, str, int]] = []
    for rel_path, rules in live.items():
        if scope is not None and rel_path not in scope:
            continue
        floor_rules = baseline.get(rel_path, {})
        for rule_id, count in rules.items():
            delta = count - floor_rules.get(rule_id, 0)
            if delta > 0:
                entries.append((rel_path, rule_id, delta))
    entries.sort(key=lambda entry: (-entry[2], entry[0], entry[1]))
    return entries


def check(
    repo_root: Path, findings: list[Finding], *, only_paths: Iterable[str] | None = None
) -> tuple[bool, int]:
    """`(ok, over_count)`: `ok` is True when no live warning count exceeds
    its baseline floor. `over_count` is the number of (file, rule) pairs
    currently above their floor — `over_entries` names them."""
    over = len(over_entries(repo_root, findings, only_paths=only_paths))
    return over == 0, over


def partition(repo_root: Path, findings: list[Finding]) -> tuple[list[Finding], int]:
    """`(shown, suppressed_count)`. A (file, rule) pair's first `floor`
    warning findings are baselined old debt and are suppressed; every
    warning past the floor is shown, as is every error. Input order is
    preserved in `shown`."""
    baseline = load_baseline(repo_root)
    if not baseline:
        return list(findings), 0
    remaining = {
        rel_path: dict(rules) for rel_path, rules in baseline.items() if rel_path and rules
    }
    shown: list[Finding] = []
    suppressed = 0
    for finding in findings:
        budget = remaining.get(finding.file, {}).get(finding.rule_id, 0)
        if finding.severity is Severity.WARNING and budget > 0:
            remaining[finding.file][finding.rule_id] = budget - 1
            suppressed += 1
            continue
        shown.append(finding)
    return shown, suppressed


def seed(repo_root: Path, findings: list[Finding]) -> None:
    """Write the baseline from scratch: floor = current live warning
    counts. Orchestrator/human maintenance only — the CLI gates this
    behind `--force`."""
    save_baseline(repo_root, _live_counts(findings))


def promote(repo_root: Path, findings: list[Finding]) -> None:
    """Update every floor to current live counts — what `wiki debt accept`
    calls. A synonym for `seed` in practice, kept as its own name for API
    clarity at call sites ("accept today's counts as the new floor",
    distinct from `seed`'s "create the baseline from nothing")."""
    seed(repo_root, findings)


def ratchet_token(
    repo_root: Path,
    findings: list[Finding],
    *,
    only_paths: Iterable[str] | None = None,
    scoped: bool = False,
) -> str:
    """The one-token ratchet summary for a report header. Over floor, the
    token names the command that lists the offending pairs. `scoped=True`
    marks a verdict computed over `only_paths` alone, so a scoped run's
    token is never mistaken for a whole-vault one."""
    ok, over = check(repo_root, findings, only_paths=only_paths)
    suffix = " (scoped)" if scoped else ""
    if ok:
        return f"ratchet OK{suffix}"
    return f"ratchet +{over} over floor{suffix} — run: wiki drain --over"
