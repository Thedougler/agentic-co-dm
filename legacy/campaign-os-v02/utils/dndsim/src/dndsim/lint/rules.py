"""W-statblock-simulatable and W-combatant-block, ported off
``utils/scripts/lint-rules/w-statblock-simulatable.mjs`` and
``w-combatant-block.mjs`` (ADR-0010; issue #57).

Faithful ports: same scope, same rule identifiers, so a committed ratchet
floor carries over untouched. Scope is deliberately the same surface the
reference JS rules actually gated on — native fence keys (:func:`~dndsim.
rules.dnd5e_2014.statblock.parse_statblock_page`) plus the attack-grammar
drift check (:func:`~dndsim.rules.dnd5e_2014.attack_string.
parse_action_category`) — not the full ``sim:`` extension namespace.
:mod:`dndsim.rules.dnd5e_2014.sim_extension`'s ``parse_sim_block``/
``parse_action_sim`` validate the whole namespace, which is a wider surface
than the reference lint rules gated on — so the ``sim:`` block is read here
for its ``side`` field only, off the raw YAML dict, keeping this port's
findings identical to the JS rules' findings. That module's own
``tests/rules/test_sim_extension.py::
test_every_real_vault_sim_block_validates`` is what holds the live corpus to
the full schema.

W-spell-simulatable (``w-spell-simulatable.mjs``) stays on
markdownlint-obsidian — dndsim has no spell parser yet (issue #48).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from dndsim.lint.findings import Finding
from dndsim.rules.dnd5e_2014.attack_string import parse_action_category
from dndsim.rules.dnd5e_2014.statblock import (
    StatblockContent,
    StatblockParseError,
    extract_statblock_fence,
    parse_statblock_page,
)
from dndsim.rules.dnd5e_2014.yaml_safe import safe_load as _yaml_safe_load

STATBLOCK_ROOTS = ("vault/srd/monsters/", "vault/campaigns/shattered-sea/monsters/")
DM_INTEL_ROOT = "vault/campaigns/shattered-sea/pcs/character-sheets/"

# Mirrors differential_harness.py's ACTION_CATEGORIES — every action list a
# statblock fence can carry.
ACTION_CATEGORIES: tuple[str, ...] = ("actions", "bonus_actions", "reactions", "legendary_actions")
# The attack-grammar-drift check itself only ever looked at
# actions+bonusActions+legendary.actions (statblock-parse.mjs never surfaces
# reactions there either) — kept as its own tuple so the two lists can't
# silently drift apart from each other.
_DRIFT_CHECK_CATEGORIES: tuple[str, ...] = ("actions", "bonus_actions", "legendary_actions")

_ATTACK_LEAD_RE = re.compile(r"\battack:\s*[+-]?\d+|\bto hit\b|\battack roll:", re.IGNORECASE)
_RETIRED_COMBATANT_FENCE_RE = re.compile(r"^```combatant\s*$", re.MULTILINE)
_COMBATANT_HEADING_RE = re.compile(r"^## Combatant Block$", re.MULTILINE)
_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)


def _read_frontmatter(text: str) -> dict[str, Any]:
    match = _FRONTMATTER_RE.match(text)
    if match is None:
        return {}
    data = _yaml_safe_load(match.group(1))
    return data if isinstance(data, dict) else {}


def _raw_block(text: str) -> dict[str, Any] | None:
    """The fence's raw YAML dict, or ``None`` for no/empty/non-mapping fence."""
    fence = extract_statblock_fence(text)
    if fence is None:
        return None
    block = _yaml_safe_load(fence)
    return block if isinstance(block, dict) else None


def _parse_full(text: str, source: str) -> tuple[StatblockContent, dict[str, Any]]:
    """Native-fence parse plus the raw fence dict, for the attack-grammar
    check and a plain (unvalidated) read of ``sim.side``.

    Raises :class:`StatblockParseError` naming the offending field. Caller
    must already have confirmed a non-empty fence
    (:func:`~dndsim.rules.dnd5e_2014.statblock.extract_statblock_fence`
    returns non-``None``).
    """
    content = parse_statblock_page(text, source)
    assert content is not None
    block = _raw_block(text) or {}
    return content, block


def lint_statblock_page(path: Path, rel: str) -> list[Finding]:
    """Port of ``w-statblock-simulatable.mjs``.

    Every non-empty ``` ```statblock ``` fence under ``vault/srd/monsters/``
    or ``vault/campaigns/shattered-sea/monsters/`` must parse (native fence keys), and any
    action whose desc reads as an attack line must keep the SRD attack
    grammar the sim parses.
    """
    if not rel.startswith(STATBLOCK_ROOTS):
        return []
    text = path.read_text()
    if extract_statblock_fence(text) is None:
        return []  # no block or stub fence — fine

    def error(message: str) -> list[Finding]:
        return [
            Finding(
                rule_code="statblock-simulatable",
                rule_name="W-statblock-simulatable",
                severity="error",
                line=1,
                column=1,
                message=message,
            )
        ]

    try:
        _content, block = _parse_full(text, rel)
    except StatblockParseError as err:
        return error(f"statblock does not parse: {err}")

    findings: list[Finding] = []
    everything = []
    for category in _DRIFT_CHECK_CATEGORIES:
        actions, _warnings = parse_action_category(block.get(category), category)
        everything.extend(actions)

    # Only the LEAD of a desc is checked — a real attack line always opens
    # with its attack-roll phrase; a mid-paragraph mention (a Spellcasting
    # trait's aside) is prose describing the caster's stat block, not an
    # attack line the sim missed.
    for action in everything:
        if action.kind != "unmodeled":
            continue
        lead = action.desc[:40]
        if _ATTACK_LEAD_RE.search(lead):
            findings.append(
                Finding(
                    rule_code="statblock-simulatable",
                    rule_name="W-statblock-simulatable",
                    severity="error",
                    line=1,
                    column=1,
                    message=(
                        f'action "{action.name}" reads as an attack but does not match the SRD '
                        "attack grammar the sim parses — fix the desc wording "
                        "(statblock-format.md)"
                    ),
                )
            )
    return findings


def lint_combatant_block(path: Path, rel: str) -> list[Finding]:
    """Port of ``w-combatant-block.mjs``.

    A character sheet under ``DM_INTEL_ROOT`` (``subtype: character-sheet``) must carry a
    "## Combatant Block" section whose ```statblock fence validates with
    ``sim: { side: party }``. The retired ```combatant fence is a hard error
    wherever it survives, checked vault-wide (unscoped), same as the
    reference rule.
    """
    text = path.read_text()

    def error(message: str) -> list[Finding]:
        return [
            Finding(
                rule_code="combatant-block",
                rule_name="W-combatant-block",
                severity="error",
                line=1,
                column=1,
                message=message,
            )
        ]

    if _RETIRED_COMBATANT_FENCE_RE.search(text):
        return error(
            "retired ```combatant fence found — migrate to the unified ```statblock fence "
            "(_templates/pc-sheet.md §9)"
        )

    if not rel.startswith(DM_INTEL_ROOT):
        return []
    frontmatter = _read_frontmatter(text)
    if frontmatter.get("subtype") != "character-sheet":
        return []

    if _COMBATANT_HEADING_RE.search(text) is None:
        return error('missing "## Combatant Block" section (_templates/pc-sheet.md §9)')
    if extract_statblock_fence(text) is None:
        return error(
            "Combatant Block has no ```statblock fence content (schema: "
            "statblock-format.md)"
        )

    try:
        _content, block = _parse_full(text, rel)
    except StatblockParseError as err:
        return error(f"combatant block invalid: {err}")

    # Read directly off the raw fence dict, not through the strict sim:
    # model — see module docstring on why parse_sim_block isn't used here.
    sim_raw = block.get("sim")
    side = sim_raw.get("side", "enemy") if isinstance(sim_raw, dict) else "enemy"
    if side != "party":
        return error(f'Combatant Block must set sim.side: party for a PC sheet (got "{side}")')
    return []


def lint_file(path: Path, rel: str) -> list[Finding]:
    """Every finding dndsim owns for one file — both rules, in rule order."""
    return lint_statblock_page(path, rel) + lint_combatant_block(path, rel)
