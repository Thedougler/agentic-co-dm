"""W126 — agent-process language never leaks into content pages.

A wiki content page (anything under `vault/` outside the agent-guidance
trees) states world facts and mechanics for the table. Which skill designs
a crossing, which command lints a page, which subagent drafts what — that
is process, and it lives in the process layer (`.claude/` skills and
rules, `vault/refs/` guidance), never in the page a DM or player reads.
Frontmatter is exempt: governed keys like `owner_skill:` carry paths by
design. Fenced code blocks are exempt for the same reason W22 states —
an example snippet is documentation, not a live defect.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_LEAK_PATTERNS: tuple[tuple[re.Pattern[str], str], ...] = (
    (re.compile(r"`[a-z0-9-]+`\s+skill\b"), "names a skill"),
    (re.compile(r"\bSKILL\.md\b"), "references SKILL.md"),
    (re.compile(r"\.claude/"), "references the .claude/ tree"),
    (re.compile(r"\bchain-load\b"), "says chain-load"),
    (re.compile(r"\bsubagents?\b"), "references subagents"),
    (re.compile(r"\bnpm run \S"), "embeds an npm run command"),
    (re.compile(r"\bthe Agent tool\b"), "references the Agent tool"),
)

_FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")


@register
class ProcessLeakRule(FileRule):
    """Agent-process language on a wiki content page."""

    id = "W126"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Delete the process sentence from the page; the fact of who designs "
        "or lints content belongs in the owning skill, rule, or vault/refs/ "
        "guidance, not on the page itself."
    )
    producer = "wiki"
    pure = True
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus

        rel = page.rel_path
        if not rel.startswith("vault/"):
            return
        # Process layer: agent-guidance trees and vault/refs/ guidance
        # legitimately name skills and commands.
        if "/.claude/" in rel or rel.startswith("vault/refs/"):
            return
        if rel.startswith("vault/_templates/"):
            return
        # CLAUDE.md/AGENTS.md files are the process layer wherever they live.
        if rel.endswith(("/CLAUDE.md", "/AGENTS.md")):
            return

        in_fence = False
        for offset, line in enumerate(page.body.splitlines()):
            if _FENCE_RE.match(line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            for pattern, label in _LEAK_PATTERNS:
                if pattern.search(line):
                    yield self.finding(
                        file=rel,
                        line=page.body_start_line + offset,
                        message=(
                            f"agent-process language on a content page ({label}) — "
                            "process lives in .claude/ or vault/refs/, never on the "
                            "page a DM or player reads"
                        ),
                    )
                    break
