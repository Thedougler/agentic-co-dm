"""Lint output as an instruction list (ADR-0064).

Every line `render` prints is either something the tool already did
(`FIXED`, `FILE REWRITTEN`) or something the agent does next (a finding,
its inline `FIX`, `GUIDE`, `SUPPRESSED`, `NEXT`). Nothing names a tier, a
severity, or a ratchet state: an agent acts on the output without parsing
it and without a vocabulary lesson.

Two shapes, chosen by `sweep`:

- A scoped run (`wiki lint <paths>`) lists findings. Each rule's ≤240-char
  imperative `FIX` prints indented under that rule's FIRST occurrence;
  later occurrences of the same rule are the finding line alone.
- A full corpus pass (`wiki sweep`) is a dispatch manifest: one line
  per dirty file — `<path> — <n> findings (<top rule ids>)` — capped at
  `_MANIFEST_CAP` lines, since a whole-corpus per-finding listing is
  something to narrow, never something to read.

Messages print whole. The ≤240-char cap is enforced at authoring time by
the rule contract, so nothing here truncates.

Two caps keep a scoped body bounded by construction: `_PER_RULE_CAP` (one
chatty rule collapses to 8 lines plus an overflow line) and
`_MAX_DISPLAY_LINES` (many distinct rules each firing once). `--all`
(`all_hits=True`) disables both.

The one deliberate I/O this otherwise pure function performs is the GUIDE
check: `Path("vault/refs/lint/<id>.md").is_file()`, relative to the
process's current working directory — correct when `wiki` runs from the
repo root.

`finding_to_json` and `exit_code` live here too: both are pure
`LintResult`/`Finding` -> value mappings the CLI only needs to print or
`sys.exit`, testable without shelling the CLI.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path
from typing import TYPE_CHECKING

from wiki_cli.autofix import REWRITTEN_LINE
from wiki_cli.contracts import TIER_ORDER, registry
from wiki_cli.producers import all_rule_docs

if TYPE_CHECKING:
    from wiki_cli.contracts import Finding
    from wiki_cli.orchestrator import LintResult

_PER_RULE_CAP = 8
"""A single rule shows at most this many hits before overflowing."""

_MAX_DISPLAY_LINES = 15
"""Global cap on finding+overflow lines in a scoped report, excluding the
header, the inline FIX lines, and the trailers."""

_MANIFEST_CAP = 40
"""A sweep manifest lists at most this many files; the rest roll into one
`+<k> more files` line."""

_MANIFEST_RULE_IDS = 3
"""Rule ids named per manifest line, chattiest first."""

GUIDE_DIR = Path("vault/refs/lint")

_GUIDE_FAMILY: dict[str, str] = {
    "W22": "w22-w23-callouts.md",
    "W23": "w22-w23-callouts.md",
    "W25": "w25-w75-wikilinks.md",
    "W75": "w25-w75-wikilinks.md",
    "W84": "w84-frontmatter-schema.md",
    "W86": "w86-vale-prose.md",
    "W114": "w114-w116-transclusion.md",
    "W116": "w114-w116-transclusion.md",
    "W119": "w119-grandfather-link.md",
    "W120": "w120-section-count-outlier.md",
    "W123": "w123-link-footer-section.md",
}
"""Rule ids whose guidance doc under `GUIDE_DIR` is not named for the id alone —
a family sharing one doc, or an id carrying a `/` that would otherwise nest the
doc in a subdirectory. A rule id absent from this map falls back to its own
lowercased id as the filename (`_guide_pointers`)."""

_NEXT_CLEAN = "NEXT: nothing — clean"
_NEXT_FIX = "NEXT: fix the findings above, then re-run"
_NEXT_NARROW = "NEXT: fix the files above one at a time — wiki lint <path>"


def render(
    result: LintResult,
    *,
    all_hits: bool = False,
    quiet: bool = False,
    suppressed: int = 0,
    sweep: bool = False,
) -> str:
    """The instruction list for one lint run. Pure over `result` except for
    the GUIDE check's filesystem probe (module docstring).

    `suppressed` is how many baselined findings the caller withheld from
    `result.findings` (ADR-0062). It prints as one trailing SUPPRESSED line
    naming the command that lists them; `quiet` compresses it to a header
    token instead.

    `sweep=True` renders the dispatch manifest instead of a finding list —
    what `wiki sweep` passes.
    """
    findings = sorted(result.findings, key=_display_order)
    fixed_lines = _fixed_lines(result.fixed)

    if quiet:
        head = f"LINT {_scope(result)} — {len(findings)} findings"
        if suppressed:
            head = f"{head} · {suppressed:,} suppressed"
        return "\n".join([*fixed_lines, head])

    suppressed_line = _suppressed_line(suppressed)

    if not findings:
        lines = [*fixed_lines, f"LINT {_scope(result)} — clean"]
        if suppressed_line:
            lines.append(suppressed_line)
        lines.append(_NEXT_CLEAN)
        return "\n".join(lines)

    lines = [*fixed_lines, f"LINT {_scope(result)} — {len(findings)} findings"]

    if sweep:
        lines.extend(_manifest(findings))
        next_line = _NEXT_NARROW
    else:
        body, rule_ids = _finding_body(findings, all_hits=all_hits)
        lines.extend(body)
        if result.stats.files == 1:
            lines.extend(_guide_pointers(rule_ids))
        next_line = _NEXT_FIX

    if suppressed_line:
        lines.append(suppressed_line)
    lines.append(next_line)

    return "\n".join(lines)


def _display_order(finding: Finding) -> tuple[int, str, int, str]:
    """Worst blast radius first, then by file and line — the order that
    tells a fixing agent which work comes first."""
    return (TIER_ORDER.index(finding.tier), finding.file, finding.line, finding.rule_id)


def _fixed_lines(fixed: dict[str, int]) -> list[str]:
    """One `FIXED` line per rewritten file, then the single rewrite notice.

    These lead the report, before any finding: they state what the tool
    already did, and the notice tells an agent its in-context copy of those
    files is stale (`autofix.py`). They print even on an otherwise clean
    run — a silent rewrite is the one thing an agent cannot recover from.

    Capped at `_MANIFEST_CAP` like the manifest itself: a sweep repairs
    hundreds of files at once, and a per-file list that long buries the
    findings it precedes.
    """
    if not fixed:
        return []
    ordered = sorted(fixed.items())
    lines = [f"FIXED {path}: {count:,} mechanical fixes" for path, count in ordered[:_MANIFEST_CAP]]
    extra = len(ordered) - _MANIFEST_CAP
    if extra > 0:
        lines.append(f"FIXED +{extra} more files — see git diff")
    lines.append(REWRITTEN_LINE)
    return lines


def _suppressed_line(suppressed: int) -> str | None:
    """ADR-0062: baselined old debt never lists itself — it collapses to
    one trailing line naming the command that does."""
    if suppressed <= 0:
        return None
    return f"SUPPRESSED: {suppressed:,} baselined findings — run: wiki drain --over"


def finding_to_json(finding: Finding) -> dict[str, object]:
    """The per-finding JSON shape. `rule`/`path` (not `rule_id`/`file`)
    because `parity.py`'s `run_wiki_lint` reads those names."""
    return {
        "rule": finding.rule_id,
        "path": finding.file,
        "line": finding.line,
        "message": finding.message,
        "severity": finding.severity.value,
        "tier": finding.tier.value,
        "producer": finding.producer,
        "fixable": finding.fixable,
    }


def exit_code(result: LintResult) -> int:
    """0 clean, 1 findings (ADR-0064). Call this on the UNFILTERED
    `run_lint` result — the `--rule` display filter never changes it
    (ADR-0023). Exit 2 is the CLI's own
    usage/config/internal-error code and never reaches here."""
    return 1 if result.findings else 0


def _scope(result: LintResult) -> str:
    """How many files the run judged."""
    files = result.stats.files
    return "1 file" if files == 1 else f"{files} files"


def _finding_body(findings: list[Finding], *, all_hits: bool) -> tuple[list[str], list[str]]:
    """The scoped body: finding lines, each rule's inline FIX under its
    first occurrence, per-rule overflow markers, and one rollup line for
    anything past the global cap. Returns (lines, rule ids in
    first-appearance order)."""
    line_width = max(len(str(f.line)) for f in findings)
    per_rule_cap = None if all_hits else _PER_RULE_CAP
    total_by_rule = Counter(f.rule_id for f in findings)

    shown: list[Finding] = []
    shown_count: Counter[str] = Counter()
    for finding in findings:
        if per_rule_cap is None or shown_count[finding.rule_id] < per_rule_cap:
            shown.append(finding)
            shown_count[finding.rule_id] += 1
    last_index = {finding.rule_id: i for i, finding in enumerate(shown)}

    entries: list[tuple[str, int, str]] = []
    for i, finding in enumerate(shown):
        entries.append((_finding_line(finding, line_width), 1, finding.rule_id))
        overflow = total_by_rule[finding.rule_id] - shown_count[finding.rule_id]
        if overflow and last_index[finding.rule_id] == i:
            entries.append(
                (f"   … {overflow} more {finding.rule_id} (--all)", overflow, finding.rule_id)
            )

    kept = entries if all_hits else entries[:_MAX_DISPLAY_LINES]

    lines: list[str] = []
    rule_ids: list[str] = []
    seen: set[str] = set()
    for text, _represents, rule_id in kept:
        lines.append(text)
        if rule_id not in seen:
            seen.add(rule_id)
            rule_ids.append(rule_id)
            lines.append(f"   FIX {rule_id}: {fix_text(rule_id)}")

    represented = sum(represents for _text, represents, _rule_id in kept)
    leftover = len(findings) - represented
    if leftover:
        lines.append(f"… {leftover} more findings (--all)")
    return lines, rule_ids


def _finding_line(finding: Finding, line_width: int) -> str:
    """One finding, message whole — the rule contract caps message length
    at authoring time, so nothing is elided here."""
    return (
        f"{finding.file}:{str(finding.line).ljust(line_width)}  "
        f"{finding.rule_id}  {finding.message}"
    )


def _manifest(findings: list[Finding]) -> list[str]:
    """The sweep's dispatch manifest: one line per dirty file, worst first,
    naming the rule ids to dispatch against. Capped — a whole-corpus
    per-finding listing is something to narrow, not to read."""
    by_file: dict[str, Counter[str]] = {}
    for finding in findings:
        by_file.setdefault(finding.file, Counter())[finding.rule_id] += 1
    ordered = sorted(by_file.items(), key=lambda item: (-sum(item[1].values()), item[0]))

    lines = []
    for path, rules in ordered[:_MANIFEST_CAP]:
        top = ", ".join(rule_id for rule_id, _n in rules.most_common(_MANIFEST_RULE_IDS))
        lines.append(f"{path} — {sum(rules.values())} findings ({top})")
    extra = len(ordered) - _MANIFEST_CAP
    if extra > 0:
        lines.append(f"+{extra} more files — narrow with wiki lint <path>")
    return lines


def fix_text(rule_id: str) -> str:
    """A rule's imperative remediation, from its own `fix` ClassVar (the
    registry, not `Finding` — `Finding` carries no remediation text). An id
    an external producer emits owns no rule class, so its `fix` comes from
    that producer module's `RULE_DOCS`
    (`wiki_cli.producers.all_rule_docs`) instead."""
    source = registry().get(rule_id) or all_rule_docs().get(rule_id)
    if source is None:
        return "no fix guidance registered for this rule"
    return source.fix


def _guide_pointers(rule_ids: list[str]) -> list[str]:
    """Single-file target only (caller gates on `stats.files == 1`). One
    `GUIDE:` pointer per displayed rule whose guidance doc exists, in
    first-appearance order. Rule ids sharing a family doc (`_GUIDE_FAMILY`)
    point at the same path; a rule id absent from that map falls back to its
    own lowercased id."""
    lines = []
    seen_paths: set[Path] = set()
    for rule_id in rule_ids:
        filename = _GUIDE_FAMILY.get(rule_id, f"{rule_id.lower()}.md")
        guide_path = GUIDE_DIR / filename
        if guide_path in seen_paths:
            continue
        if guide_path.is_file():
            lines.append(f"GUIDE: {guide_path}")
            seen_paths.add(guide_path)
    return lines
