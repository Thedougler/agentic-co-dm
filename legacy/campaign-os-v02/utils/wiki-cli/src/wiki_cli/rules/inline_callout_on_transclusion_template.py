"""W137 — inline play callout on a page whose template expects callout-fragment
transclusion.

When a type's template has migrated from inline callout placeholders to
``![[slug-narration-…]]`` / ``![[slug-dialogue-…]]`` (or leftover
``![[slug-c0N]]``) embeds, an inline ``[!read-aloud]`` or ``[!dialogue]``
is a migration candidate. Mechanical callouts stay inline (ADR-0056).

Prior art: W23 (``callout_type_by_path.py``) — same "check callout against
template expectation" pattern.
"""

from __future__ import annotations

import re
from collections.abc import Iterable
from functools import cache
from pathlib import Path

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.markdown import split_frontmatter
from wiki_cli.query.schema import resolve_template

_CALLOUT_OPENER_RE = re.compile(r"^>\s*\[!([A-Za-z][A-Za-z0-9-]*)\][-+]?\s*(.*)$")
_FRAGMENT_FILE_RE = re.compile(r"-c\d{2,}\.md$")
_TEMPLATE_EMBED_RE = re.compile(
    r"!\[\[[^\]]*(?:-c\d{2,}|-narration-|-dialogue-)[^\]]*\]\]"
)
_EXTRACT_CALLOUTS = frozenset({"read-aloud", "narration", "dialogue"})

_PLAY_ROOTS = ("vault/", "pcs/", "sessions/")
_EXCLUDED_PREFIXES = (
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
)
_EXCLUDED_EXACT: frozenset[str] = frozenset({"vault/campaigns/shattered-sea/dm-voice-script.md"})


@cache
def _template_has_transclusion(templates_root: Path, type_name: str, subtype: str | None) -> bool:
    """True when the type's template body contains at least one callout-fragment embed.

    Cached per (templates_root, type, subtype) — templates do not change mid-run.
    """
    path = resolve_template(templates_root, type_name, subtype)
    if path is None:
        return False
    raw = path.read_text(encoding="utf-8")
    _, body, _ = split_frontmatter(raw)
    return bool(_TEMPLATE_EMBED_RE.search(body))


@register
class InlineCalloutOnTransclusionTemplate(FileRule):
    """Flags inline play callouts on pages whose type template uses transclusion."""

    id = "W137"
    version = "1"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        "Extract the spoken text into a type: narration or type: dialogue "
        "sibling and replace with ![[slug-narration-<role>]] "
        "(.claude/skills/narration, .claude/skills/dialogue)"
    )
    producer = "wiki"
    pure = False

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path.replace("\\", "/")
        if not rel.endswith(".md"):
            return
        if _FRAGMENT_FILE_RE.search(rel):
            return
        if any(rel.startswith(p) for p in _EXCLUDED_PREFIXES) or rel in _EXCLUDED_EXACT:
            return
        if "/.claude/" in rel:
            return
        if not any(rel.startswith(root) for root in _PLAY_ROOTS):
            return

        page_type = page.type
        if not page_type:
            return
        if page_type in {"narration", "dialogue"}:
            return

        config = load_config(corpus.repo_root)
        subtype = page.frontmatter.get("subtype")
        subtype_str = subtype if isinstance(subtype, str) else None
        if not _template_has_transclusion(config.templates_root, page_type, subtype_str):
            return

        for file_line, text in page.body_lines():
            match = _CALLOUT_OPENER_RE.match(text)
            if match is None:
                continue
            call_type = match.group(1).lower()
            if call_type not in _EXTRACT_CALLOUTS:
                continue
            yield self.finding(
                file=page.rel_path,
                line=file_line,
                message=(
                    f"Inline [!{call_type}] on a page whose template expects "
                    "a narration/dialogue sibling — extract to "
                    f"![[slug-{call_type if call_type == 'dialogue' else 'narration'}-<role>]] "
                    "(.claude/skills/narration)"
                ),
            )
