"""W25's unlinked-entity-mention check (`unlinked_mention.py`), scoped to
`vault/stories/` and `vault/ideas/` instead of W25's whole-`vault/` scope —
both share the detection engine in `scan_unlinked_mentions`. Draft narrative
and raw ideas are exempted from W25 itself (draft-story,
campaign-writers-room own that scope) — this rule reports the same findings
there at warning severity, gating a story/idea edit. The fix is the same
judgment call as W25's: cross-linker resolves the finding; this rule never
inserts a link itself.

A `.claude/skills/` (or `agents/`/`rules/`) subtree nested under either
scoped root is agent-facing instruction prose, not narrative content — it
cross-references other files with plain `[text](path.md)` links (matching
`obsidian-markdown`'s own convention for non-wiki docs), never
`[[wikilinks]]`, so it carries no wikilink duty either, the same call W25
already makes for `CLAUDE.md`.

Not pure — same reason as W25: depends on the whole corpus, not just this
file's own bytes.
"""

from __future__ import annotations

from collections.abc import Iterator

from wiki_cli.config import load_config as _load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.rules.unlinked_mention import scan_unlinked_mentions

_SCOPED_ROOTS = ("vault/stories/", "vault/ideas/")
_AGENT_DOC_MARKER = "/.claude/"


@register
class NarrativeUnlinkedMentionRule(FileRule):
    """W25's unlinked-entity-mention check, scoped to `vault/stories/` and
    `vault/ideas/`. See module docstring."""

    id = "W122"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Wikilink the first natural mention: [[target-slug|Display Text]]."
    producer = "wiki"
    pure = False
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterator[Finding]:
        rel = page.rel_path
        if not any(rel.startswith(root) for root in _SCOPED_ROOTS):
            return
        if _AGENT_DOC_MARKER in ("/" + rel):
            return
        if page.type == "table":
            return

        config = _load_config()
        for mention in scan_unlinked_mentions(page, corpus, config):
            yield self.finding(
                file=rel,
                line=mention.line,
                message=(
                    f'"{mention.name}" resolves to {mention.target_rel_path} but is never '
                    "[[wikilinked]] on this page"
                ),
            )
