"""A per-type template's governed frontmatter spine against
`vault/_templates/_refs/_ref.md`'s authority, ported from
`utils/scripts/lint-rules/w55-template-spine-consistency.mjs` (rule id
`W55`): required spine keys must appear in the default's relative order
(per-type keys freely interleaved), `publish` must start `false`, and
`status` must start at a `STATUS_ENUM` value. A template with no `status:`
key is derived/machine-written data and carries no governed spine.

LEGACY-BUG (file-scope gate, confirmed empirically 2026-08-09): npm's
`.obsidian-linter.jsonc` unconditionally `ignores` `vault/_templates/**`
even for an explicit single-file CLI argument (`markdownlint-obsidian
vault/_templates/_srd/_monster.md` returns `[]` for every custom rule, not
just W55) — so W55 structurally never fires against a real template in the
npm engine, regardless of its own detection logic. This port reproduces
the legacy rule's own literal file-scope check (`rel.startswith
("_templates/")`), which likewise never matches a real repo-root-relative
path (`vault/_templates/...`) — so live-vault parity holds at 0 diffs on
both sides for the same structural reason. The detection logic below is
real and exercised by this port's own fixtures, which use a bare
`_templates/...` rel_path to reach it.

The legacy rule's secondary "reorder fix" block (a full occupied-line
remap purely in service of its autofix `insertText` payload) is not
ported, for the same reason `required_headings.py` drops W5's own reorder
autofix: this repo's `contracts.py` has no fix-application mechanism to
drive it. The primary out-of-order detection (the LIS-based `onError` per
misplaced key) is ported in full.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli import templates
from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SKIP_FILES: frozenset[str] = frozenset({"_templates/CLAUDE.md", "_templates/_refs/_ref.md"})
_EXCLUDED_SPINE_KEYS: frozenset[str] = frozenset(
    {"summary", "tier", "campaigns", "title", "author"}
)


def _in_order_keys(present: list[str], positions: list[int]) -> set[str]:
    """Longest increasing subsequence over `positions` (O(n^2), small n) —
    the present spine keys that are already in relative order; every other
    present key is "out of order", same algorithm as the legacy rule."""
    count = len(positions)
    if count == 0:
        return set()
    lis_len = [1] * count
    prev = [-1] * count
    for i in range(count):
        for j in range(i):
            if positions[j] < positions[i] and lis_len[j] + 1 > lis_len[i]:
                lis_len[i] = lis_len[j] + 1
                prev[i] = j
    best = max(range(count), key=lambda i: lis_len[i])
    result: set[str] = set()
    cursor = best
    while cursor != -1:
        result.add(present[cursor])
        cursor = prev[cursor]
    return result


@register
class TemplateSpineRule(FileRule):
    """Ported from npm's W55 (`utils/scripts/lint-rules/w55-template-spine-consistency.mjs`)."""

    id = "W55"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Reorder/add the missing governed spine key(s) to match "
        "vault/_templates/_refs/_ref.md's order; start publish: false and "
        "status: at a STATUS_ENUM value."
    )
    producer = "wiki"
    pure = False
    """Depends on the template catalog under vault/_templates/, not just
    this file's own bytes."""
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md") or not rel.startswith("_templates/"):
            return  # see module docstring's LEGACY-BUG note
        if rel in _SKIP_FILES:
            return

        spine = templates.default_spine(load_config().templates_root)
        if spine is None:
            return

        if "status" not in page.frontmatter:
            return  # derived-data template, no governed spine

        required_spine = [key for key in spine.spine_keys if key not in _EXCLUDED_SPINE_KEYS]
        keys = [key for key in page.frontmatter if isinstance(key, str)]
        present = [key for key in required_spine if key in page.frontmatter]
        missing = [key for key in required_spine if key not in page.frontmatter]

        for key in missing:
            yield self.finding(
                file=rel,
                line=page.body_start_line,
                message=(
                    f'missing spine key "{key}" — every governed template carries the '
                    f"full spine ({spine.template_path})"
                ),
            )

        positions = [keys.index(key) for key in present]
        in_order = _in_order_keys(present, positions)
        expected = ", ".join(required_spine)
        for key in present:
            if key in in_order:
                continue
            yield self.finding(
                file=rel,
                line=page.line_of(key),
                message=(
                    f'spine key "{key}" is out of order — the governed spine follows '
                    f"{spine.template_path}'s order: {expected}"
                ),
            )

        if "publish" in page.frontmatter and page.frontmatter.get("publish") is not False:
            yield self.finding(
                file=rel,
                line=page.line_of("publish"),
                message=(
                    f'templates start "publish: false" — publishing is default-deny '
                    f"({spine.template_path})"
                ),
            )

        status_enum = load_config().threshold_list("STATUS_ENUM")
        status_value = page.frontmatter.get("status")
        if status_value is not None and status_value not in status_enum:
            yield self.finding(
                file=rel,
                line=page.line_of("status"),
                message=(
                    f'templates start "status:" at a STATUS_ENUM value '
                    f'({" | ".join(status_enum)}), got "{status_value}" ({spine.template_path})'
                ),
            )
