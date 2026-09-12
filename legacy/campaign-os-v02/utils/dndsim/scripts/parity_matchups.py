"""The fixed matchup set issue #52's statistical parity harness runs (issue
#52's own acceptance criterion: "A committed fixed matchup set spans single
combatants, parties, and a legendary creature").

Every combatant here is built from a **real** vault page — PC sheets under
``vault/campaigns/shattered-sea/pcs/character-sheets/*-sheet.md`` and creature pages
under ``vault/srd/monsters/`` — never a hand-invented stat line, so a
number reported by this harness traces back to the same content a DM
actually plays against. ``combatant_from_page`` does the real work: parse
the page's ```statblock fence with
:func:`~dndsim.rules.dnd5e_2014.statblock.parse_statblock_page` for
``ac``/``hp``/``name``, then re-parse its raw ``actions:`` entries with
:func:`~dndsim.rules.dnd5e_2014.attack_string.parse_action_category` to pick
one named attack's ``to_hit``/``damage``/``reach``/``range`` — the physical-
shape fields :class:`~dndsim.rules.dnd5e_2014.fixture.CombatantSpec` needs
for positioning, and the opportunity-attack/legendary-action fallback
(neither driven by a compiled kit yet — see ``combat.py``). ``combatant_
from_page`` (issue #60) additionally tries
:func:`~dndsim.profile.load_compiled_statblock` /
:func:`~dndsim.rules.dnd5e_2014.compile.compile_statblock` and attaches the
result via ``compiled=`` when it succeeds — this is what makes ``run_combat``
fight with the page's real kit (Perrin's Longsword vs. Green-Flame Blade,
Cure Wounds/Healing Word, Cutting Words/Pack Tactics Strike; the Grung Elite
Warrior's dagger/shortbow Multiattack) rather than the single flat attack
below. Every PC sheet in ``PARTY_PATHS`` compiles through that path as of
commit 2f4fc502 (the pydantic ``extra_forbidden``/duplicate-``id`` bugs
this docstring used to name are fixed); a combatant that still fails to
compile falls back to the flat attack profile below, unchanged, with a
printed warning rather than aborting the harness.

**A structural simplification, not a Divergence.** ``CombatantSpec`` models
one flat attack profile per combatant (`fixture.py`'s own docstring: "the
two-combatant walking skeleton's implicit shape") — a real statblock's full
Multiattack routine (Otar's Bite + 3 Claw + Tongue Lash) collapses to its
single most-representative attack (Claw, the one used most often). This is
an existing, accepted harness/content-authoring limitation of
``run_combat``'s current combatant model, not a behavior difference between
engines, so it is not recorded in ``DIVERGENCES.md``.

**The one genuine Divergence this matchup set surfaces**: see the
``otar-the-foul`` matchup below and ``DIVERGENCES.md``'s "Lair-action
default activation" entry.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass, replace
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

import re  # noqa: E402

import yaml  # noqa: E402

from dndsim.profile import ProfileError, load_compiled_statblock  # noqa: E402
from dndsim.rules.dnd5e_2014.attack_string import parse_action_category  # noqa: E402
from dndsim.rules.dnd5e_2014.compile import CompiledStatblock  # noqa: E402
from dndsim.rules.dnd5e_2014.dice import parse_dice_expr  # noqa: E402
from dndsim.rules.dnd5e_2014.fixture import CombatantSpec, make_combatant  # noqa: E402
from dndsim.rules.dnd5e_2014.statblock import (  # noqa: E402
    StatblockParseError,
    extract_statblock_fence,
    parse_statblock_page,
)
from dndsim.rules.dnd5e_2014.sweep import primary_attack  # noqa: E402

DIVERGENCES_PATH = Path(__file__).resolve().parent.parent / "DIVERGENCES.md"

_DIVERGENCE_FENCE_RE = re.compile(r"```divergence\n(.*?)\n```", re.DOTALL)


def simulate_time_excluded_matchups(path: Path) -> set[str]:
    """Union of ``measured.matchups[].id`` across every ``category:
    simulate-time`` ```divergence fence in *path*."""
    text = path.read_text()
    excluded: set[str] = set()
    for fence_text in _DIVERGENCE_FENCE_RE.findall(text):
        entry = yaml.safe_load(fence_text)
        if not isinstance(entry, dict) or entry.get("category") != "simulate-time":
            continue
        for matchup in entry.get("measured", {}).get("matchups") or []:
            excluded.add(matchup["id"])
    return excluded


DM_INTEL = REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "pcs" / "character-sheets"

PERRIN_PATH = DM_INTEL / "perrin-black-jaw-sheet.md"
CATARINA_PATH = DM_INTEL / "catarina-davirelli-sheet.md"
CRISSDALYNN_PATH = DM_INTEL / "crissdalynn-khinriss-sheet.md"
DELMAR_PATH = DM_INTEL / "delmar-fisk-sheet.md"
JEAN_CLAUDE_PATH = DM_INTEL / "jean-claude-tabarnack-sheet.md"

GRUNG_ELITE_WARRIOR_PATH = REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "monsters" / "grung-elite-warrior.md"
OTAR_PATH = REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "npcs" / "otar-the-foul.md"
ARCHMAGE_PATH = REPO_ROOT / "vault" / "srd" / "monsters" / "archmage.md"
PURPLE_CASTE_ZEALOT_PATH = REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "monsters" / "purple-caste-zealot.md"

# The default party roster `sim-combat party <Y>` resolves — matching it
# exactly is what lets every party matchup below use the literal keyword
# "party" rather than a hand-kept file list that could silently drift.
PARTY_PATHS: tuple[Path, ...] = (
    PERRIN_PATH,
    CATARINA_PATH,
    CRISSDALYNN_PATH,
    DELMAR_PATH,
    JEAN_CLAUDE_PATH,
)


def combatant_from_page(
    path: Path,
    *,
    entity_id: str,
    legendary: bool = False,
    has_lair: bool = False,
) -> CombatantSpec:
    """Build a :class:`CombatantSpec` from one real vault page's ```statblock
    fence. The flat attack profile (``attack_bonus``/damage dice/reach/range
    — the physical shape a positional/opportunity-attack/legendary-window
    fallback still resolves through) is picked automatically by
    :func:`~dndsim.rules.dnd5e_2014.sweep.primary_attack` — the compiled
    routine's first attack step, or the first attack action absent a
    routine — never a hardcoded action name. A hardcoded name breaks the
    moment a page's own weapon/action naming changes (this harness broke on
    exactly that, more than once, before this fix): the sheet's own content
    is what a DM actually plays against, and picking a representative
    attack from it is this module's job, not something every caller should
    have to name by hand and keep in sync."""
    markdown = path.read_text()
    content = parse_statblock_page(markdown, str(path))
    if content is None:
        raise ValueError(f"{path}: no ```statblock fence (or an empty one)")

    compiled: CompiledStatblock | None = None
    try:
        compiled, _block = load_compiled_statblock(markdown, str(path))
    except (StatblockParseError, ProfileError, ValueError, TypeError) as err:
        print(f"parity_matchups: {path}: compiled kit unavailable, using flat attack ({err})")

    if compiled is not None:
        picked = primary_attack(compiled)
        if picked is None:
            raise ValueError(f"{path}: compiled statblock has no attack action to fight with")
        attack_primitive, _name = picked
        parsed = (
            parse_dice_expr(attack_primitive.damage[0].dice) if attack_primitive.damage else None
        )
        return make_combatant(
            entity_id=entity_id,
            name=content.name,
            hp_max=content.hp,
            armor_class=content.ac,
            attack_bonus=attack_primitive.to_hit,
            damage_bonus=parsed.flat if parsed else 0,
            damage_dice_count=parsed.dice[0].count if parsed and parsed.dice else 1,
            damage_dice_sides=parsed.dice[0].sides if parsed and parsed.dice else 4,
            is_melee=attack_primitive.is_melee,
            reach_ft=attack_primitive.reach_ft if attack_primitive.reach_ft is not None else 5.0,
            range_ft=attack_primitive.range_ft,
            range_long_ft=attack_primitive.range_long_ft,
            legendary=legendary,
            has_lair=has_lair,
            compiled=compiled,
        )

    # No compiled kit at all — the same auto-pick, over the raw parsed
    # actions instead of a compiled routine, still never a hardcoded name.
    fence = extract_statblock_fence(markdown)
    assert fence is not None  # content is not None => fence matched above
    try:
        block = yaml.safe_load(fence)
    except yaml.YAMLError as err:
        raise StatblockParseError(f"statblock: YAML parse failed in {path}: {err}") from err
    if not isinstance(block, dict):
        raise ValueError(f"{path}: statblock fence did not parse to a mapping")
    actions, _warnings = parse_action_category(block.get("actions"), "actions")
    attack = next((a for a in actions if a.kind == "attack" and a.damage), None)
    if attack is None:
        raise ValueError(f"{path}: no attack action with damage to fight with")
    parsed = parse_dice_expr(attack.damage[0].dice)
    return make_combatant(
        entity_id=entity_id,
        name=content.name,
        hp_max=content.hp,
        armor_class=content.ac,
        attack_bonus=attack.to_hit,
        damage_bonus=parsed.flat,
        damage_dice_count=parsed.dice[0].count if parsed.dice else 1,
        damage_dice_sides=parsed.dice[0].sides if parsed.dice else 4,
        is_melee=attack.attack_type.startswith("melee"),
        reach_ft=float(attack.reach) if attack.reach is not None else 5.0,
        range_ft=float(attack.range) if attack.range is not None else None,
        range_long_ft=float(attack.range_long) if attack.range_long is not None else None,
        legendary=legendary,
        has_lair=has_lair,
        compiled=None,
    )


def strip_compiled(specs: tuple[CombatantSpec, ...]) -> tuple[CombatantSpec, ...]:
    """The ablation lever every asserted (non-regression-guard) matchup is
    checked against: drop the compiled kit (issue #60's Mechanics,
    Multiattack, spells, reactions) from every combatant on one side,
    leaving only the flat single-attack profile ``fixture.py`` already
    falls back to when a page fails to compile. Constructed entirely
    outside ``src/dndsim/rules`` — never edits the engine — so it is a
    legitimate way to confirm a matchup's win rate is actually sensitive to
    the compiled-kit feature rather than being driven entirely by the flat
    attack shape underneath it."""
    return tuple(replace(spec, compiled=None) for spec in specs)


def _party() -> list[CombatantSpec]:
    return [
        combatant_from_page(
            PERRIN_PATH,
            entity_id="dnd5e_2014:combatant/perrin-black-jaw",
        ),
        combatant_from_page(
            CATARINA_PATH,
            entity_id="dnd5e_2014:combatant/catarina-davirelli",
        ),
        combatant_from_page(
            CRISSDALYNN_PATH,
            entity_id="dnd5e_2014:combatant/crissdalynn-khinriss",
        ),
        combatant_from_page(
            DELMAR_PATH,
            entity_id="dnd5e_2014:combatant/delmar-fisk",
        ),
        combatant_from_page(
            JEAN_CLAUDE_PATH,
            entity_id="dnd5e_2014:combatant/jean-claude-tabarnack",
        ),
    ]


def _grung_elite_warrior(entity_id: str) -> CombatantSpec:
    return combatant_from_page(GRUNG_ELITE_WARRIOR_PATH, entity_id=entity_id)


def _archmage(entity_id: str) -> CombatantSpec:
    # CR12 solo, no legendary actions and no lair — unlike Otar this cannot
    # become a Divergence-excluded matchup, so its win rate is free to
    # stand as real parity evidence rather than a reported-only delta.
    return combatant_from_page(ARCHMAGE_PATH, entity_id=entity_id)


def _purple_caste_zealot(entity_id: str) -> CombatantSpec:
    # Resistance to bludgeoning/piercing/slashing while it has >=1 HP
    # (Toxin Frenzy) roughly doubles its effective HP against every
    # combatant in this file's kit (nothing here deals a non-physical
    # damage type) — the mechanism this matchup set was missing a case for.
    return combatant_from_page(PURPLE_CASTE_ZEALOT_PATH, entity_id=entity_id)


def _otar() -> CombatantSpec:
    # legendary=True exercises the legendary-action window and Otar's own
    # Rubble Surge reaction (reactions are exercised generically by any
    # melee combatant via opportunity attacks — no per-statblock wiring
    # needed for that half). has_lair=True is what makes this matchup a
    # Divergence: see the module docstring and DIVERGENCES.md.
    return combatant_from_page(
        OTAR_PATH,
        entity_id="dnd5e_2014:combatant/otar-the-foul",
        legendary=True,
        has_lair=True,
    )


@dataclass(frozen=True, slots=True)
class Matchup:
    """One fixed-seed comparison point: dndsim's own combatants plus the
    literal old-engine ``sim-combat <old_x> <old_y>`` positional args that
    resolve to the *same* real vault pages.

    ``regression_guard`` (issue #64) marks a matchup that sits at or near
    the 0/1 ceiling by design — kept because a ceiling case is still a
    valid check that nothing has regressed, but explicitly **not**
    evidence that the two engines agree on anything a real fight would
    turn on: it trivially passes regardless of whether either engine
    executes most of a compiled kit. Every matchup with
    ``regression_guard=False`` is required to demonstrably move under
    :func:`strip_compiled`'s ablation (``scripts/parity_harness.py``'s
    ``run_ablation_check``) — that requirement is what makes it
    "asserted, discriminating" rather than "trivially passing" in the
    harness report, per issue #64's acceptance criteria."""

    id: str
    description: str
    party: tuple[CombatantSpec, ...]
    enemies: tuple[CombatantSpec, ...]
    old_x: str
    old_y: str
    regression_guard: bool = False


def build_matchups() -> list[Matchup]:
    """Constructed lazily (not a module-level constant) since every
    combatant here is parsed from a live vault page — building the set is
    itself a real parse, and a corpus edit should be visible on the next
    run rather than needing a process restart."""
    return [
        Matchup(
            id="dnd5e_2014:combatant/perrin-black-jaw-vs-dnd5e_2014:combatant/grung-elite-warrior",
            description=(
                "Single combatant vs. single combatant — a real PC against an ordinary creature. "
                "Reclassified as a regression guard (issue #65): as #63 fixed the party's own kit "
                "this matchup drifted to the ceiling and its ablation delta (compiled kit "
                "stripped) fell to +0.0258, under the ±0.03 materiality threshold — it no longer "
                "discriminates (issue #64's own rule for that shape). Kept as a check that "
                "nothing regresses, not as parity evidence."
            ),
            party=(
                combatant_from_page(
                    PERRIN_PATH,
                    entity_id="dnd5e_2014:combatant/perrin-black-jaw",
                ),
            ),
            enemies=(_grung_elite_warrior("dnd5e_2014:combatant/grung-elite-warrior"),),
            old_x=str(PERRIN_PATH),
            old_y=str(GRUNG_ELITE_WARRIOR_PATH),
            regression_guard=True,
        ),
        Matchup(
            id="dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/grung-elite-warrior",
            description=(
                "Full party vs. a single ordinary enemy. Regression guard — the full 5-PC "
                "party overwhelms one CR2 opponent regardless of engine correctness, so this "
                "pins at the ceiling on both engines and has no resolving power (issue #64)."
            ),
            party=tuple(_party()),
            enemies=(_grung_elite_warrior("dnd5e_2014:combatant/grung-elite-warrior"),),
            old_x="party",
            old_y=str(GRUNG_ELITE_WARRIOR_PATH),
            regression_guard=True,
        ),
        Matchup(
            id="dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/grung-elite-warrior-x2",
            description=(
                "Full party vs. multiple ordinary enemies. Regression guard — same ceiling "
                "shape as the single-enemy case above (issue #64)."
            ),
            party=tuple(_party()),
            enemies=(
                _grung_elite_warrior("dnd5e_2014:combatant/grung-elite-warrior-a"),
                _grung_elite_warrior("dnd5e_2014:combatant/grung-elite-warrior-b"),
            ),
            old_x="party",
            old_y=f"{GRUNG_ELITE_WARRIOR_PATH}:2",
            regression_guard=True,
        ),
        Matchup(
            id="dnd5e_2014:combatant/party-vs-dnd5e_2014:combatant/otar-the-foul",
            description=(
                "Full party vs. a legendary creature with a reaction and (dndsim-side only, "
                "the Divergence this matchup exists to surface) a forced lair action."
            ),
            party=tuple(_party()),
            enemies=(_otar(),),
            old_x="party",
            old_y=str(OTAR_PATH),
        ),
        # Issue #64: the three matchups above give this set exactly one
        # combatant-pair with any resolving power (the 1v1 above) — both
        # party matchups pin at the p=1.0000 ceiling on both engines, so
        # "2 of 3 pass" was never evidence the engines agree on anything a
        # real fight would exercise. The three below are chosen, and
        # ablation-checked in scripts/parity_harness.py, specifically to
        # sit away from both 0 and 1.
        Matchup(
            id="dnd5e_2014:combatant/delmar-fisk-vs-dnd5e_2014:combatant/purple-caste-zealot",
            description=(
                "Single PC vs. a single enemy it genuinely loses to more often than not: "
                "Delmar's the party's squishiest melee combatant (AC16, HP30) against a "
                "CR3 zealot with resistance to his only damage type while it has any HP "
                "left (issue #64)."
            ),
            party=(
                combatant_from_page(
                    DELMAR_PATH,
                    entity_id="dnd5e_2014:combatant/delmar-fisk",
                ),
            ),
            enemies=(_purple_caste_zealot("dnd5e_2014:combatant/purple-caste-zealot"),),
            old_x=str(DELMAR_PATH),
            old_y=str(PURPLE_CASTE_ZEALOT_PATH),
        ),
        Matchup(
            id=(
                "dnd5e_2014:combatant/party-vs-"
                "dnd5e_2014:combatant/archmage-and-purple-caste-zealot"
            ),
            description=(
                "Full party vs. a mixed CR12 solo plus a durable, physically-resistant "
                "CR3 — opposition tuned toward roughly even odds on both engines (not "
                "just one), and a fight long enough (round_cap=20, ~10 rounds observed) "
                "that resource spending matters rather than ending in two rounds. A "
                "single archmage alone and five zealots alone were both tried first: the "
                "archmage-only fight left the old engine's win rate too close to its own "
                "ceiling to trust, and five zealots pinned the old engine at a flat "
                "p=1.0000 outright (their damage-type resistance appears not to move the "
                "old engine's win rate the way it moves dndsim's) — this pairing is what "
                "measured away from 0 and 1 on *both* engines (issue #64)."
            ),
            party=tuple(_party()),
            enemies=(
                _archmage("dnd5e_2014:combatant/archmage"),
                _purple_caste_zealot("dnd5e_2014:combatant/purple-caste-zealot"),
            ),
            old_x="party",
            old_y=f"{ARCHMAGE_PATH},{PURPLE_CASTE_ZEALOT_PATH}",
        ),
    ]
