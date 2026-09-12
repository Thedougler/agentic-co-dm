"""W23 — play pages carry play callouts, docs/meta pages carry generic
ones. Ported from `utils/scripts/lint-rules/w23-callout-type-by-path.mjs`.

Three independent checks over the same page:
1. A `[!check]` callout needs a title — the pictured place, person, or object.
2. A generic callout (`[!note]`, `[!warning]`, ...) on a play page must
   convert to a play type — unless it is a `CONTRADICTION`/`RESOLVED`
   canon-review marker, or the vendored SRD/doc-family carve-out below.
3. A bare "DC <n>" in prose outside a callout, on a play page, belongs in
   a `[!check]`/`[!mechanic]` instead (skipped inside the run-guide
   template's "At a Glance" compression section, which legitimately
   indexes DCs whose real callout lives in the scene file).

Path families: PLAY_ROOTS pages default to play callouts; DOC_ROOTS pages
(sys/, the vendored SRD spell/monster/item dirs, and five migrated SRD
equipment-rules pages) default to the generic set instead — third-party
reference material read like docs, not authored campaign prose.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_FENCE_MARK_RE = re.compile(r"^\s*(`{3,}|~{3,})(.*)$")
_CLOSING_ONLY_RE = re.compile(r"^\s*(`+|~+)\s*$")
_CALLOUT_OPENER_RE = re.compile(r"^>\s*\[!([A-Za-z][A-Za-z0-9-]*)\][-+]?\s*(.*)$")
_DC_RE = re.compile(r"\bDC\s?\d+\b")
_STEP_MARKER_RE = re.compile(r"\bDC\d+:")
"""The campaign drafting guide writes its per-step transcript markers as
`DC1: <content>` — the same convention as `DS1:`/`RG1:`/`SC1:`/`FK1:` on its
sibling guides, where the prefix is just the type's initials. A real
difficulty class never carries a colon directly after the number, so
stripping this form before the bare-DC search below costs no coverage."""
_HEADING2_RE = re.compile(r"^##\s+(.+)$")

_PLAY_ROOTS = ("vault/", "pcs/", "sessions/")
_RULES_EQUIPMENT_DOCS = (
    "vault/srd/rules/equipment.md",
    "vault/srd/rules/adventuring-gear.md",
    "vault/srd/rules/mounts-vehicles.md",
    "vault/srd/rules/tools.md",
    "vault/srd/rules/weapons.md",
)
_DOC_ROOTS = (
    "sys/",
    "vault/srd/spells/",
    "vault/srd/monsters/",
    "vault/srd/items/",
    *_RULES_EQUIPMENT_DOCS,
)
_ITEM_DOC_ROOTS = ("vault/srd/items/", *_RULES_EQUIPMENT_DOCS)
_EXCLUDED_PREFIXES = (
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
)
_EXCLUDED_EXACT = ("vault/campaigns/shattered-sea/dm-voice-script.md",)

_REPLACEMENT_HINTS = {
    "caution": "[!mechanic] (hazard/trap) or [!dm] (secret/handling)",
    "warning": "[!mechanic] (hazard/trap) or [!dm] (secret/handling)",
    "danger": "[!mechanic]",
    "important": "[!dm] (handling note) or [!mechanic] (stat line)",
    "note": "[!dm], or plain prose if not moment-scoped",
    "tip": "[!dm], or plain prose if not moment-scoped",
    "success": "one [!check] with tiered **Success:**/**Failure:** lines",
    "failure": "one [!check] with tiered **Success:**/**Failure:** lines",
}


def _fenced_flags(lines: list[str]) -> list[bool]:
    flags = [False] * len(lines)
    open_char: str | None = None
    open_len = 0
    for i, line in enumerate(lines):
        if open_char is None:
            match = _FENCE_MARK_RE.match(line)
            if match:
                open_char = match.group(1)[0]
                open_len = len(match.group(1))
                flags[i] = True
            continue
        flags[i] = True
        close = _CLOSING_ONLY_RE.match(line)
        if close and close.group(1)[0] == open_char and len(close.group(1)) >= open_len:
            open_char = None
            open_len = 0
    return flags


@register
class CalloutTypeByPath(FileRule):
    id = "W23"
    version = "3"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        "Convert the callout to match the page family, move a bare DC into a "
        "[!check]/[!mechanic], or add a Skill — Label title."
    )
    producer = "wiki"
    pure = True

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus  # accepted for interface parity; this rule is per-file.
        rel = page.rel_path.replace("\\", "/")
        if not rel.endswith(".md"):
            return
        if any(rel.startswith(prefix) for prefix in _EXCLUDED_PREFIXES) or rel in _EXCLUDED_EXACT:
            return
        # Skill/agent trees under the vault are agent-instruction prose, not
        # play pages — a `DC1:` checklist-echo ID there is not a difficulty
        # class (same genre carve-out .vale.ini makes for .claude/skills/).
        if "/.claude/" in rel:
            return

        on_doc_page = any(rel.startswith(root) for root in _DOC_ROOTS)
        on_play_page = not on_doc_page and any(rel.startswith(root) for root in _PLAY_ROOTS)
        if not on_play_page and not on_doc_page:
            return

        config = load_config()
        play_callouts = {c.lower() for c in config.threshold_list("PLAY_CALLOUTS")}
        doc_callouts = {c.lower() for c in config.threshold_list("DOC_CALLOUTS")}

        body = list(page.body_lines())
        texts = [text for _, text in body]
        fenced = _fenced_flags(texts)

        if on_play_page:
            in_at_a_glance = False
            for idx, (file_line, text) in enumerate(body):
                heading = _HEADING2_RE.match(text)
                if heading:
                    in_at_a_glance = heading.group(1).strip().lower().startswith("at a glance")
                if fenced[idx] or text.lstrip().startswith(">") or text.lstrip().startswith("<!--"):
                    continue
                if in_at_a_glance:
                    continue
                if _DC_RE.search(_STEP_MARKER_RE.sub("", text)):
                    yield self.finding(
                        file=page.rel_path,
                        line=file_line,
                        message=(
                            "DC in bare prose — a roll-gated branch belongs in a [!check], a "
                            "standing rule in a [!mechanic] (vault/campaigns/.claude/skills/callouts)"
                        ),
                    )

        for idx, (file_line, text) in enumerate(body):
            if fenced[idx]:
                continue
            match = _CALLOUT_OPENER_RE.match(text)
            if match is None:
                continue
            call_type = match.group(1).lower()
            title = match.group(2).strip()

            if call_type == "check" and not title:
                yield self.finding(
                    file=page.rel_path,
                    line=file_line,
                    message=(
                        '[!check] needs a title — name the pictured place, '
                        "person, or object "
                        "(vault/campaigns/.claude/skills/callouts/references/check.md)"
                    ),
                )

            if on_play_page:
                if call_type in play_callouts or call_type == "visual-aid":
                    continue
                if call_type == "warning" and title.startswith("CONTRADICTION"):
                    continue
                if call_type == "success" and title.startswith("RESOLVED"):
                    continue
                hint = _REPLACEMENT_HINTS.get(
                    call_type, "a play type (vault/campaigns/.claude/skills/callouts)"
                )
                yield self.finding(
                    file=page.rel_path,
                    line=file_line,
                    message=f'Generic callout "[!{call_type}]" on a play page — convert to {hint}',
                )
            elif (
                call_type in play_callouts
                and call_type not in doc_callouts
                and not any(rel.startswith(root) for root in _ITEM_DOC_ROOTS)
            ):
                yield self.finding(
                    file=page.rel_path,
                    line=file_line,
                    message=(
                        f'Play callout "[!{call_type}]" on a docs/meta page — use the generic '
                        "set (vault/campaigns/.claude/skills/callouts/references/generic-types.md)"
                    ),
                )
