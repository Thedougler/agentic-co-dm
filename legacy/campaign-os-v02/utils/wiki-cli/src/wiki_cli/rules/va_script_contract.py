"""Ported from npm's W61 (`utils/scripts/lint-rules/w61-va-script-contract.mjs`).

`vault/campaigns/shattered-sea/pcs/va-scripts/*.md` are performed
screenplays, not governed wiki pages — no frontmatter, no type schema
(README.md § `vault/campaigns/shattered-sea/pcs/va-scripts/**` exemption).
This rule enforces `script-writer` SKILL.md's own § Format rules that have
no clean off-the-shelf fit: no frontmatter/heading/bullet, a
direction/meta-note line is italicized parentheses `*(...)*` (bare `(...)`
flagged as inconsistent), no `direction:` label, no runaway-long direction
(`VA_SCRIPT_DIRECTION_MAX_WORDS`), and no dialogue line repeats verbatim
anywhere in the file.

The banned delivery-narration/performer-instruction phrase lists
(`VA_SCRIPT_DELIVERY_PHRASES` / `VA_SCRIPT_INSTRUCTION_PHRASES`) moved to
Vale existence checks in the legacy system (`.vale-hard.ini`,
`docs/vale-styles/CampaignOS/VaScriptDeliveryPhrases.yml` /
`VaScriptInstructionPhrases.yml`) — a fixed-phrase scan needs no
structural/stateful logic, so this rule does not re-implement it; porting
it here would diverge from the legacy module's own real behaviour, not
match it. This rule does NOT enforce the two fixed Meta-notes' exact
wording or position either — that is judgment the skill's own contract
owns, unenforceable by a per-line scan that doesn't track phase structure.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

SCOPED_ROOT = "vault/campaigns/shattered-sea/pcs/va-scripts/"
_HEADING_RE = re.compile(r"^#{1,6}\s")
_BULLET_RE = re.compile(r"^[-*]\s")
_ITALIC_PAREN_LINE_RE = re.compile(r"^\*\((.*)\)\*$")
_BARE_PAREN_LINE_RE = re.compile(r"^\((.*)\)$")
_DIRECTION_LABEL_RE = re.compile(r"^direction\s*:", re.IGNORECASE)
# The two fixed Meta-notes (script-writer SKILL.md § Format) are full
# sentences by design — exempt from the Direction word cap. Matched loosely
# on their fixed opening words since the character name varies.
_META_NOTE_RE = re.compile(r"^(as yourself|try to stay as\b)", re.IGNORECASE)


@register
class VaScriptContractRule(FileRule):
    """Ported from npm's W61 (`w61-va-script-contract.mjs`)."""

    id = "W61"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = (
        "Strip frontmatter/headings/bullets, italicize every direction as "
        "*(...)*, drop any \"direction:\" label, tighten runaway directions, "
        "and make sure no dialogue line repeats verbatim (script-writer "
        "SKILL.md § Format)."
    )
    producer = "wiki"
    pure = True
    """Reads wiki.toml's VA_SCRIPT_DIRECTION_MAX_WORDS threshold too;
    captured by Config.fingerprint (the cache key)."""
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        del corpus
        rel = page.rel_path
        if not rel.endswith(".md"):
            return
        if not rel.startswith(SCOPED_ROOT):
            return

        direction_max_words = int(load_config().threshold("VA_SCRIPT_DIRECTION_MAX_WORDS"))

        # Body rules see frontmatter-stripped lines — `body_start_line > 1`
        # is Page's own signal that a frontmatter block was present and cut.
        if page.body_start_line > 1:
            yield self.finding(
                file=rel,
                line=1,
                message=(
                    "voice-script carries frontmatter — the file is the performed lines only, "
                    "no frontmatter/status/publish fields (vault/campaigns/.claude/skills/"
                    "script-writer/SKILL.md § Output)"
                ),
            )

        body = list(page.body_lines())
        seen_dialogue: dict[str, int] = {}

        for idx, (line_no, line) in enumerate(body):
            trimmed = line.strip()
            if not trimmed:
                continue

            if _HEADING_RE.match(trimmed):
                yield self.finding(
                    file=rel,
                    line=line_no,
                    message=(
                        "voice-script has a heading — no header, no section labels anywhere "
                        "in the file (script-writer SKILL.md § Format)"
                    ),
                )
                continue
            if _BULLET_RE.match(trimmed):
                yield self.finding(
                    file=rel,
                    line=line_no,
                    message=(
                        "voice-script has a bullet list line — the file is dialogue and "
                        "direction lines only, no lists (script-writer SKILL.md § Format)"
                    ),
                )
                continue

            bare_match = _BARE_PAREN_LINE_RE.match(trimmed)
            if bare_match:
                yield self.finding(
                    file=rel,
                    line=line_no,
                    message=(
                        f'direction/meta-note "{trimmed}" is not italicized — wrap it as '
                        f'`*({bare_match.group(1)})*` (script-writer SKILL.md § Format)'
                    ),
                )
                continue

            paren_match = _ITALIC_PAREN_LINE_RE.match(trimmed)
            if paren_match:
                inner = paren_match.group(1)
                word_count = len([w for w in inner.strip().split() if w])
                if _DIRECTION_LABEL_RE.match(inner):
                    yield self.finding(
                        file=rel,
                        line=line_no,
                        message=(
                            f'direction "{trimmed}" carries a "direction:" label — a direction '
                            "is the cue itself, nothing else (script-writer SKILL.md § Format)"
                        ),
                    )
                elif word_count > direction_max_words and not _META_NOTE_RE.match(inner.strip()):
                    yield self.finding(
                        file=rel,
                        line=line_no,
                        message=(
                            f'direction "{trimmed}" is too long/explanatory (max '
                            f"{direction_max_words} words) — an adverb, emotion word, or short "
                            '"like X" comparison, never backstory or motive (script-writer '
                            "SKILL.md § Format)"
                        ),
                    )
                next_text = body[idx + 1][1] if idx + 1 < len(body) else None
                if next_text is not None and next_text.strip() != "":
                    yield self.finding(
                        file=rel,
                        line=line_no,
                        message=(
                            f'direction "{trimmed}" has no blank line before the text it '
                            "precedes — a single newline collapses into the same paragraph "
                            "when rendered, merging the direction into the dialogue "
                            "(script-writer SKILL.md § Format)"
                        ),
                    )
                continue

            # Dialogue line from here on. Delivery-narration/performer-
            # instruction phrase bans live in Vale now — this rule only
            # tracks state (verbatim repetition) a fixed-phrase existence
            # check can't express.
            if trimmed in seen_dialogue:
                yield self.finding(
                    file=rel,
                    line=line_no,
                    message=(
                        f"dialogue line repeats verbatim from line {seen_dialogue[trimmed]} — "
                        "every line is new text, no line is ever reused (script-writer "
                        "SKILL.md § Format)"
                    ),
                )
            else:
                seen_dialogue[trimmed] = line_no
