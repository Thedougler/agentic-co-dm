"""Ported from npm's W81 (`utils/scripts/lint-rules/w81-claude-md-kit-budget.mjs`).

Root `CLAUDE.md` over its guardrails-kit budget (`docs/guardrails/_FORMAT.md`
F3/F4):

- F3. CLAUDE.md hard budget: <=15 iron rules, 1 routing table, kit core +
  footer <=60 lines. Adding a rule over budget requires demoting one to a
  guardrail doc in the same edit.
- F4. NEVER/ALWAYS/MUST in caps: at most 5 lines in CLAUDE.md, reserved for
  irreversible damage. Scope: kit zones only — `## Project` lines keep
  their original casing and do not count.

Kit zones are read from the marker comments the kit itself writes
(`<!-- BEGIN KIT CORE ... -->` / `<!-- END KIT CORE -->`, same for
FOOTER), never from line numbers — the `## Project` zone between them
grows and shifts, and F4 explicitly excludes it from the CAPS count. A
CLAUDE.md with no markers at all (a subtree CLAUDE.md, which is pure
`## Project` content) is out of scope entirely — F3/F4 budget the kit, and
a subtree file has no kit zone to budget. Root-only: a subtree CLAUDE.md
(any `rel_path` other than exactly `CLAUDE.md`) never fires even when its
own content is over these budgets.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.claude_pointer import resolve_at_pointer_text
from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_FORMAT_DOC = "docs/guardrails/_FORMAT.md"

_KIT_BEGIN_RE = re.compile(r"<!--\s*BEGIN KIT (CORE|FOOTER)\b")
_KIT_END_RE = re.compile(r"<!--\s*END KIT (CORE|FOOTER)\s*-->")
_CAPS_RE = re.compile(r"\b(NEVER|ALWAYS|MUST)\b")
_HEADING_RE = re.compile(r"^##\s")
_IRON_RULES_HEADING_RE = re.compile(r"^##\s+Iron rules\s*$")
_BULLET_RE = re.compile(r"^-\s")
_ROUTING_TABLE_HEADER_RE = re.compile(r"^\|\s*The moment you\.\.\.")


def _kit_zone_lines(lines: list[str]) -> list[tuple[int, int]] | None:
    """Line indexes (0-based, inclusive) covered by BEGIN/END marker pairs.
    `None` when the file carries no kit markers at all."""
    zones: list[tuple[int, int]] = []
    start: int | None = None
    for i, line in enumerate(lines):
        if _KIT_BEGIN_RE.search(line):
            start = i
        elif _KIT_END_RE.search(line) and start is not None:
            zones.append((start, i))
            start = None
    return zones if zones else None


def _count_iron_rules(lines: list[str]) -> int:
    """Bullets directly under the `## Iron rules` heading, stopping at the
    next `##` heading — a continuation line of a wrapped bullet is not a
    rule."""
    in_section = False
    count = 0
    for line in lines:
        if _HEADING_RE.match(line):
            if in_section:
                break
            in_section = bool(_IRON_RULES_HEADING_RE.match(line))
            continue
        if in_section and _BULLET_RE.match(line):
            count += 1
    return count


@register
class ClaudeMdKitBudgetRule(FileRule):
    """Ported from npm's W81 (`utils/scripts/lint-rules/w81-claude-md-kit-budget.mjs`)."""

    id = "W81"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Demote an iron rule to the guardrail doc that owns its "
        "checklist, downgrade a NEVER/ALWAYS/MUST to sentence case, or "
        "move a kit-zone rule's detail into its guardrail doc and leave "
        "the one-line compressed form here — all in the same edit."
    )
    producer = "wiki"
    pure = True
    """Reads wiki.toml's KIT_MAX_* thresholds too; captured by
    Config.fingerprint (the cache key)."""
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if page.rel_path != "CLAUDE.md":
            return

        lines = resolve_at_pointer_text(page.raw, corpus.repo_root).split("\n")
        zones = _kit_zone_lines(lines)
        if zones is None:
            return

        config = load_config()
        max_iron_rules = int(config.threshold("KIT_MAX_IRON_RULES"))
        max_caps_lines = int(config.threshold("KIT_MAX_CAPS_LINES"))
        max_zone_lines = int(config.threshold("KIT_MAX_ZONE_LINES"))

        iron_rules = _count_iron_rules(lines)
        if iron_rules > max_iron_rules:
            yield self.finding(
                file=page.rel_path,
                line=1,
                message=(
                    f"CLAUDE.md has {iron_rules} iron rules (budget {max_iron_rules}) "
                    "— demote one to the guardrail doc that owns its checklist in "
                    f"this same edit, per {_FORMAT_DOC} F3. Never merge two rules "
                    "onto one line to dodge the cap (budget: wiki.toml [thresholds] "
                    "KIT_MAX_IRON_RULES)"
                ),
            )

        caps_lines = 0
        zone_lines = 0
        for start, end in zones:
            zone_lines += end - start + 1
            for i in range(start, end + 1):
                if _CAPS_RE.search(lines[i]):
                    caps_lines += 1

        if caps_lines > max_caps_lines:
            yield self.finding(
                file=page.rel_path,
                line=1,
                message=(
                    f"CLAUDE.md's kit zones carry {caps_lines} NEVER/ALWAYS/MUST "
                    f"lines (budget {max_caps_lines}) — downgrade one to sentence "
                    "case in this same edit; caps are reserved for irreversible "
                    "damage (data loss, killed processes, pushed history, "
                    f"secrets), per {_FORMAT_DOC} F4. Lines in the `## Project` "
                    "zone keep their own casing and are not counted (budget: "
                    "wiki.toml [thresholds] KIT_MAX_CAPS_LINES)"
                ),
            )

        if zone_lines > max_zone_lines:
            yield self.finding(
                file=page.rel_path,
                line=1,
                message=(
                    f"CLAUDE.md's kit core + footer total {zone_lines} lines "
                    f"(budget {max_zone_lines}) — move a rule's detail into the "
                    "guardrail doc that owns it and leave the one-line compressed "
                    f"form here, per {_FORMAT_DOC} F3 (budget: wiki.toml "
                    "[thresholds] KIT_MAX_ZONE_LINES)"
                ),
            )

        table_count = sum(1 for line in lines if _ROUTING_TABLE_HEADER_RE.match(line))
        if table_count > 1:
            yield self.finding(
                file=page.rel_path,
                line=1,
                message=(
                    f"CLAUDE.md carries {table_count} routing tables "
                    f"({_FORMAT_DOC} F3 allows 1) — merge the rows into the "
                    "single table; two tables means an agent matches against "
                    "whichever it reads first"
                ),
            )
