"""Parser for 2014 and 2024 SRD-worded action ``desc`` strings (issues #41, #42).

Handles the 2014 attack clause ("Melee Weapon Attack: +7 to hit, ..." /
"Hit: N (dice) type damage") and 2014 save clause ("DC N <Ability> saving
throw"), plus the 2024 attack clause ("Melee Attack Roll: +7, reach 5 ft. N
(dice) type damage"), the 2024 save clause ("<Ability> Saving Throw: DC N"),
and its labeled Failure/Success/"Failure or Success" outcome clauses. Both
grammars are auto-detected per action from the shape of its ``desc`` and
are never merged into one pattern. Anything outside both grammars becomes
``kind="unmodeled"`` — the parser never guesses mechanics it cannot read.

Multiattack: :func:`parse_multiattack` ports ``parseMultiattack`` — an
ordered routine built from the Multiattack action's own ``desc`` plus the
block's sibling action names. ``parse_action`` itself still only
*classifies* a Multiattack action to ``kind="multiattack"`` (grammar-era
agnostic); building its routine is a whole-statblock-level concern (the
routine references other actions by name), matching where the JS reference
keeps it — ``statblock-parse.mjs``'s ``parsed.routine``, not a field on the
multiattack action itself. A caller assembling an action list is expected
to filter ``kind == "multiattack"`` entries out of the main ``actions``
category, mirroring ``main.actions.filter(a => a.kind !== 'multiattack')``
in ``statblock-parse.mjs``.

Deliberately NOT ported here (later slice — see the reference file's own
comments):

- The ``sim:`` extension namespace — issue #43.
"""

from __future__ import annotations

import re
from typing import Annotated, Any, Final, Literal

from pydantic import BaseModel, ConfigDict, Field

from dndsim.rules.dnd5e_2014.conditions import CONDITION_TAGS as CONDITION_TAGS

_RECHARGE_RE = re.compile(r"\(\s*Recharge\s+(\d)(?:\s*[-–]\s*(\d))?\s*\)", re.IGNORECASE)
_PER_DAY_RE = re.compile(r"\(\s*(\d+)\s*/\s*Day\s*\)", re.IGNORECASE)
_COSTS_RE = re.compile(
    r"\(\s*Costs\s+(\d+)\s+Actions?\s*(?:,\s*Recharge\s+(\d)(?:\s*[-–]\s*(\d))?\s*)?\)",
    re.IGNORECASE,
)
_SPACES_RE = re.compile(r"\s{2,}")
_TRAILING_COMMA_RE = re.compile(r",\s*$")

_DAMAGE_GROUP_RE = re.compile(
    r"(?:\d+\s*\(([^)]+)\)\s+(\w+)|(?<!\S)(\d+)(?![d\d])(?!\s*\()\s+(\w+))\s+damage"
)
_SAVE_CLAUSE_RE = re.compile(r"DC\s+(\d+)\s+(\w+)\s+saving throw", re.IGNORECASE)
_SAVING_THROW_RE = re.compile(r"saving throw", re.IGNORECASE)

_AREA_RE = re.compile(
    r"each\s+(?:creature|humanoid or beast|humanoid|target)[^.]*?within\s+(\d+)\s+feet",
    re.IGNORECASE,
)
_CONE_RE = re.compile(r"(\d+)-foot\s+cone", re.IGNORECASE)
_SPHERE_RE = re.compile(r"(\d+)-foot-radius\s+sphere", re.IGNORECASE)

_MULTIATTACK_DESC_RE = re.compile(r"^\s*(?:the\s+\S+|\w[\w\s,'-]*?)\s+makes\s+", re.IGNORECASE)
_ATTACK_WORD_RE = re.compile(r"attack", re.IGNORECASE)
_MULTIATTACK_NAME_RE = re.compile(r"multiattack", re.IGNORECASE)

_ATK_RE = re.compile(
    r"(Melee or Ranged|Melee|Ranged)\s+(Weapon|Spell)\s+Attack(?:\s*\([^)]*\))?:"
    r"\s*([+-]\d+)\s+to hit",
    re.IGNORECASE,
)
_HIT_SPLIT_RE = re.compile(r"Hit:\s*", re.IGNORECASE)
_REACH_RE = re.compile(r"reach\s+(\d+)\s*ft", re.IGNORECASE)
_RANGE_RE = re.compile(r"range\s+(\d+)(?:/(\d+))?\s*ft", re.IGNORECASE)
_CONDITIONAL_DAMAGE_RE = re.compile(
    r"If the target is (\w+),\s+it (?:also )?takes\s+\d+\s*\(([^)]+)\)\s+(\w+)\s+damage",
    re.IGNORECASE,
)
_GRAPPLE_RE = re.compile(r"target is Grappled\s*\(escape DC\s+(\d+)\)", re.IGNORECASE)
_RESTRAINED_RE = re.compile(r"and Restrained", re.IGNORECASE)
_ADVANTAGE_IF_RE = re.compile(
    r"advantage on this attack roll if the target is (\w+)", re.IGNORECASE
)

_AUTODAMAGE_RE = re.compile(
    r"(?:One|Each|The)\s[^.]*?takes\s+\d+\s*\(([^)]+)\)\s+(\w+)\s+damage", re.IGNORECASE
)
_TAKES_PAREN_RE = re.compile(r"takes\s+\d+\s*\(", re.IGNORECASE)
_DC_RE = re.compile(r"DC\s+\d+", re.IGNORECASE)
_REQUIRES_CONDITION_RE = re.compile(r"One\s+(\w+)\s+creature", re.IGNORECASE)
_HALF_DAMAGE_RE = re.compile(r"half as much", re.IGNORECASE)
_HALF_DAMAGE_STRIP_RE = re.compile(r"or half as much[^.]*", re.IGNORECASE)

# --- 2024 SRD grammar (issue #42) ---------------------------------------

_ATK_2024_RE = re.compile(
    r"\*?(Melee or Ranged|Melee|Ranged)\s+Attack Roll:\*?\s*([+-]\d+)", re.IGNORECASE
)
_SAVE_CLAUSE_2024_RE = re.compile(r"\*?(\w+)\s+Saving Throw\*?:\s*DC\s+(\d+)", re.IGNORECASE)
_RIDER_SCOPE_SPLIT_RE = re.compile(r"\.\s+(?=Whenever\b|At the (?:start|end)\b)", re.IGNORECASE)
_COND_2024_RE = re.compile(
    r"has the (\w+)(?: and (\w+))? conditions?(?:\s*\(escape DC\s+(\d+)\))?", re.IGNORECASE
)
_FAILURE_LABEL_RE = re.compile(r"\*?Failure:\*?", re.IGNORECASE)
_FAILURE_OR_SUCCESS_LABEL_RE = re.compile(r"\*?Failure or Success\*?:", re.IGNORECASE)
_SUCCESS_LABEL_RE = re.compile(r"\*?Success:\*?", re.IGNORECASE)
_FAILURE_STRIP_RE = re.compile(r"^\*?Failure:\*?\s*", re.IGNORECASE)
_SUCCESS_STRIP_RE = re.compile(r"^\*?Success:\*?\s*", re.IGNORECASE)
_HALF_DAMAGE_2024_RE = re.compile(r"half\s+damage|half as much", re.IGNORECASE)

_NUMBER_WORDS: Final[dict[str, int]] = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
}
_MULTIATTACK_ALTERNATIVES_SPLIT_RE = re.compile(
    r"\.\s*(?:it|she|he|they) can replace", re.IGNORECASE
)
_WITH_FORM_RE = re.compile(r"makes\s+(\w+)\s+attacks?\s+with\s+its\s+([\w\s'-]+)", re.IGNORECASE)
_MULTIATTACK_COUNT_WORD_ALT: Final[str] = "|".join(_NUMBER_WORDS)


def _strip_spaces(dice: str) -> str:
    return re.sub(r"\s+", "", dice)


class ActionUsage(BaseModel):
    """Usage riders parsed out of an action's name (recharge, N/day, legendary cost)."""

    model_config = ConfigDict(frozen=True)

    recharge: tuple[int, int] | None = None
    per_day: int | None = None
    legendary_cost: int | None = None


def parse_name_usage(name: str) -> tuple[str, ActionUsage]:
    """Split usage riders out of an action NAME: recharge, N/day, legendary cost."""
    clean = name
    recharge: tuple[int, int] | None = None
    per_day: int | None = None
    legendary_cost: int | None = None

    m = _RECHARGE_RE.search(clean)
    if m:
        lo = int(m.group(1))
        hi = lo if m.group(2) is None else int(m.group(2))
        recharge = (lo, hi)
        clean = (clean[: m.start()] + clean[m.end() :]).strip()

    m = _PER_DAY_RE.search(clean)
    if m:
        per_day = int(m.group(1))
        clean = (clean[: m.start()] + clean[m.end() :]).strip()

    m = _COSTS_RE.search(clean)
    if m:
        legendary_cost = int(m.group(1))
        if m.group(2) is not None:
            lo = int(m.group(2))
            recharge = (lo, lo if m.group(3) is None else int(m.group(3)))
        clean = (clean[: m.start()] + clean[m.end() :]).strip()

    clean = _TRAILING_COMMA_RE.sub("", _SPACES_RE.sub(" ", clean)).strip()
    return clean, ActionUsage(recharge=recharge, per_day=per_day, legendary_cost=legendary_cost)


def _condition_tags_in(text: str) -> list[str]:
    lower = text.lower()
    return [tag for tag in CONDITION_TAGS if tag in lower]


def _condition_riders_2024(text: str) -> list[OnHitEffect]:
    """2024-grammar "has the X condition [(escape DC N)]" riders, scanned all.

    Also handles the plural pair "has the X and Y conditions" (no escape DC
    on either word in that shape) — port of the reference file's ``addRider``
    closure plus its ``condRe.exec`` loop.
    """
    riders: list[OnHitEffect] = []
    seen: set[str] = set()

    def add_rider(word: str, escape_dc: str | None) -> None:
        effect = word.lower()
        if effect not in CONDITION_TAGS or effect in seen:
            return
        seen.add(effect)
        riders.append(
            OnHitEffect(effect=effect, escape_dc=int(escape_dc) if escape_dc is not None else None)
        )

    for m in _COND_2024_RE.finditer(text):
        second = m.group(2)
        add_rider(m.group(1), m.group(3) if second is None else None)
        if second is not None:
            add_rider(second, None)
    return riders


class DamageGroup(BaseModel):
    model_config = ConfigDict(frozen=True)

    dice: str
    type: str


def _damage_groups(text: str) -> list[DamageGroup]:
    """All "N (dice) type damage" or bare "N type damage" groups, in order."""
    groups: list[DamageGroup] = []
    for m in _DAMAGE_GROUP_RE.finditer(text):
        dice = m.group(1) if m.group(1) is not None else m.group(3)
        kind = m.group(2) if m.group(2) is not None else m.group(4)
        groups.append(DamageGroup(dice=_strip_spaces(dice), type=kind.lower()))
    return groups


class _SaveClause(BaseModel):
    model_config = ConfigDict(frozen=True)

    dc: int
    save: str


def _save_clause(text: str) -> _SaveClause | None:
    """First "DC N <Ability> saving throw" in a string (2014 SRD grammar)."""
    m = _SAVE_CLAUSE_RE.search(text)
    if m is None:
        return None
    return _SaveClause(dc=int(m.group(1)), save=m.group(2)[:3].lower())


def _save_clause_2024(text: str) -> _SaveClause | None:
    """First "<Ability> Saving Throw: DC N" in a string (2024 SRD grammar —

    ability and DC swap order vs. 2014, and the label is capitalized).
    """
    m = _SAVE_CLAUSE_2024_RE.search(text)
    if m is None:
        return None
    return _SaveClause(dc=int(m.group(2)), save=m.group(1)[:3].lower())


class _LabeledClauses2024(BaseModel):
    model_config = ConfigDict(frozen=True)

    target: str
    failure: str
    success: str


def _labeled_clauses_2024(text: str) -> _LabeledClauses2024:
    """Split 2024's "<target clause>. *Failure:* ... *Success:* ... [*Failure

    or Success*: ...]" into its three labeled parts (any may be empty).
    """
    failure_m = _FAILURE_LABEL_RE.search(text)
    both_m = _FAILURE_OR_SUCCESS_LABEL_RE.search(text)
    success_m = _SUCCESS_LABEL_RE.search(text)
    failure_idx = failure_m.start() if failure_m else -1
    both_idx = both_m.start() if both_m else -1
    success_idx = success_m.start() if success_m else -1

    target = text[: len(text) if failure_idx == -1 else failure_idx]
    failure = ""
    success = ""
    if failure_idx != -1:
        if success_idx != -1 and success_idx > failure_idx:
            failure_end = success_idx
        elif both_idx != -1 and both_idx > failure_idx:
            failure_end = both_idx
        else:
            failure_end = len(text)
        failure = _FAILURE_STRIP_RE.sub("", text[failure_idx:failure_end])
    if success_idx != -1:
        success_end = both_idx if both_idx != -1 and both_idx > success_idx else len(text)
        success = _SUCCESS_STRIP_RE.sub("", text[success_idx:success_end])
    return _LabeledClauses2024(target=target, failure=failure, success=success)


class TargetClause(BaseModel):
    model_config = ConfigDict(frozen=True)

    area: bool
    count: int | None = None
    radius: int | None = None
    cone: int | None = None


def _target_clause(text: str) -> TargetClause:
    area = _AREA_RE.search(text)
    if area:
        return TargetClause(area=True, radius=int(area.group(1)))
    cone = _CONE_RE.search(text)
    if cone:
        return TargetClause(area=True, cone=int(cone.group(1)))
    sphere = _SPHERE_RE.search(text)
    if sphere:
        return TargetClause(area=True, radius=int(sphere.group(1)))
    return TargetClause(area=False, count=1)


class OnHitEffect(BaseModel):
    model_config = ConfigDict(frozen=True)

    effect: str
    escape_dc: int | None = None
    # A re-save/re-roll rider (issue #63's save_ends interlock) — carried
    # through, never parsed here (prose carries no save_ends clause; only
    # `sim:`-authored content and the spell library populate this), so a
    # save-driven condition this rider grants can end early instead of
    # applying once and persisting for the rest of the fight.
    save_ends: dict[str, Any] | None = None


class ConditionalDamage(BaseModel):
    model_config = ConfigDict(frozen=True)

    condition: str
    dice: str
    type: str


class SaveRider(BaseModel):
    """An "on-hit" save gated by an attack ("... and the target must succeed on a DC N save")."""

    model_config = ConfigDict(frozen=True)

    dc: int
    save: str
    effects: list[OnHitEffect] = Field(default_factory=list)
    note: str | None = None


class AttachedSave(BaseModel):
    """The save clause attached to an autodamage action."""

    model_config = ConfigDict(frozen=True)

    dc: int
    save: str
    effects: list[OnHitEffect] = Field(default_factory=list)


class OnFail(BaseModel):
    model_config = ConfigDict(frozen=True)

    damage: list[DamageGroup] = Field(default_factory=list)
    effects: list[OnHitEffect] = Field(default_factory=list)


class ActionBase(BaseModel):
    model_config = ConfigDict(frozen=True)

    name: str
    desc: str
    usage: ActionUsage = Field(default_factory=ActionUsage)
    warnings: list[str] = Field(default_factory=list)


class AttackAction(ActionBase):
    kind: Literal["attack"] = "attack"
    attack_type: str
    to_hit: int
    reach: int | None = None
    range: int | None = None
    range_long: int | None = None
    damage: list[DamageGroup]
    on_hit_effects: list[OnHitEffect] = Field(default_factory=list)
    conditional_damage: list[ConditionalDamage] = Field(default_factory=list)
    on_hit_save: SaveRider | None = None
    advantage_if: str | None = None


class AutodamageAction(ActionBase):
    kind: Literal["autodamage"] = "autodamage"
    damage: list[DamageGroup]
    targets: TargetClause
    requires_target_condition: str | None = None
    attached_save: AttachedSave | None = None


class SaveAction(ActionBase):
    kind: Literal["save"] = "save"
    dc: int
    save: str
    targets: TargetClause
    on_fail: OnFail = Field(default_factory=OnFail)
    half_on_save: bool = False


class MultiattackAction(ActionBase):
    kind: Literal["multiattack"] = "multiattack"


class UnmodeledAction(ActionBase):
    kind: Literal["unmodeled"] = "unmodeled"


Action = Annotated[
    AttackAction | AutodamageAction | SaveAction | MultiattackAction | UnmodeledAction,
    Field(discriminator="kind"),
]


def parse_action(raw_name: str | None, raw_desc: str | None) -> Action:
    """Parse one action ``{name, desc}`` pair into a normalized :data:`Action`.

    Kinds: ``attack`` | ``save`` | ``autodamage`` | ``multiattack`` |
    ``unmodeled``. ``warnings`` collects anything recognized only partially.
    """
    name, usage = parse_name_usage(raw_name or "")
    desc = (raw_desc or "").strip()

    def unmodeled(warning: str | None = None) -> UnmodeledAction:
        return UnmodeledAction(
            name=name, desc=desc, usage=usage, warnings=[warning] if warning else []
        )

    if (
        _MULTIATTACK_DESC_RE.match(desc)
        and _ATTACK_WORD_RE.search(desc)
        and _MULTIATTACK_NAME_RE.search(name)
    ):
        return MultiattackAction(name=name, desc=desc, usage=usage)

    # 1. Attack line: "Melee Weapon Attack: +8 to hit, ..." with optional
    #    parenthetical ("Melee Weapon Attack (tongue): +6 to hit").
    atk = _ATK_RE.search(desc)
    if atk:
        after_hit = desc[atk.start() :]
        hit_split = _HIT_SPLIT_RE.search(after_hit)
        if not hit_split:
            return unmodeled("attack line without Hit: clause")
        hit_text = after_hit[hit_split.start() :]
        damage = _damage_groups(hit_text)
        if len(damage) == 0:
            return unmodeled("attack Hit: clause without parseable damage")

        atk_range = "melee" if "melee" in atk.group(1).lower() else "ranged"
        attack_type = f"{atk_range}_{atk.group(2).lower()}"
        on_hit_effects: list[OnHitEffect] = []
        conditional_damage: list[ConditionalDamage] = []
        combined_damage = [damage[0]]

        reach_m = _REACH_RE.search(desc)
        range_m = _RANGE_RE.search(desc)

        # "plus N (dice) type damage" — every group after the first, unless
        # it belongs to a conditional sentence handled below.
        conditional_m = _CONDITIONAL_DAMAGE_RE.search(hit_text)
        for g in damage[1:]:
            if conditional_m and _strip_spaces(conditional_m.group(2)) == g.dice:
                continue
            combined_damage.append(g)
        if conditional_m:
            conditional_damage.append(
                ConditionalDamage(
                    condition=conditional_m.group(1).lower(),
                    dice=_strip_spaces(conditional_m.group(2)),
                    type=conditional_m.group(3).lower(),
                )
            )

        # Grapple/restrain riders: "target is Grappled (escape DC 16) and
        # Restrained".
        grapple_m = _GRAPPLE_RE.search(hit_text)
        if grapple_m:
            on_hit_effects.append(OnHitEffect(effect="grappled", escape_dc=int(grapple_m.group(1))))
            if _RESTRAINED_RE.search(hit_text):
                on_hit_effects.append(OnHitEffect(effect="restrained"))

        # Save rider after the hit: "and the target must succeed on a DC 17
        # Strength saving throw or be pulled/grappled/poisoned..."
        on_hit_save: SaveRider | None = None
        extra_warnings: list[str] = []
        rider_save = _save_clause(hit_text)
        if rider_save:
            saving_throw_m = _SAVING_THROW_RE.search(hit_text)
            assert saving_throw_m is not None  # _save_clause matched "saving throw"
            after_save = hit_text[saving_throw_m.start() :]
            tags = [t for t in _condition_tags_in(after_save) if t != "grappled" or not grapple_m]
            if len(tags) == 0:
                extra_warnings.append(
                    "on-hit save with no recognized condition — effect text kept verbatim"
                )
                on_hit_save = SaveRider(
                    dc=rider_save.dc, save=rider_save.save, effects=[], note=after_save.strip()
                )
            else:
                on_hit_save = SaveRider(
                    dc=rider_save.dc,
                    save=rider_save.save,
                    effects=[OnHitEffect(effect=t) for t in tags],
                )

        # Conditional advantage: "has advantage on this attack roll if the
        # target is Grappled".
        adv_if_m = _ADVANTAGE_IF_RE.search(desc)
        advantage_if = f"target_has:{adv_if_m.group(1).lower()}" if adv_if_m else None

        return AttackAction(
            name=name,
            desc=desc,
            usage=usage,
            warnings=extra_warnings,
            attack_type=attack_type,
            to_hit=int(atk.group(3)),
            reach=int(reach_m.group(1)) if reach_m else None,
            range=int(range_m.group(1)) if range_m else None,
            range_long=int(range_m.group(2)) if range_m and range_m.group(2) is not None else None,
            damage=combined_damage,
            on_hit_effects=on_hit_effects,
            conditional_damage=conditional_damage,
            on_hit_save=on_hit_save,
            advantage_if=advantage_if,
        )

    # 1b. 2024 attack line: "Melee Attack Roll: +11, reach 10 ft. 13 (2d6 + 6)
    #     Slashing damage" — no "to hit", no "Hit:" label, damage follows the
    #     reach/range clause directly.
    atk2024 = _ATK_2024_RE.search(desc)
    if atk2024:
        after_roll = desc[atk2024.end() :]
        damage_2024 = _damage_groups(after_roll)

        # 2024 condition riders: every "has the <X> condition", each
        # optionally followed by "(escape DC N)". Real prose separates a
        # second rider with ", and it has the ..." or a whole following
        # sentence (purple-worm, kraken, chain-devil, roc, tarrasque in
        # vault/srd/monsters/), and a rider may carry no escape DC at all
        # (tarrasque Tail: Prone) — so scan them all rather than
        # pattern-matching one connective. Scanned only up to the first save
        # clause so a save-gated condition stays on the save rider, not the
        # unconditional on-hit list. Checked before the no-damage bailout
        # below — a rider-only attack line with zero damage groups (e.g.
        # Roper's Tentacle: grapple + poison, no damage dice at all) is a
        # real attack, not unmodeled prose.
        # Riders are read only from the on-hit scope: a sentence opening
        # with "Whenever ..." / "At the start/end ..." begins downstream
        # periodic or maintenance text (otyugh's long-rest re-save), not
        # part of the hit.
        rider_scope = _RIDER_SCOPE_SPLIT_RE.split(after_roll)[0]
        saving_throw_2024_m = _SAVING_THROW_RE.search(rider_scope)
        if saving_throw_2024_m is None:
            condition_text = rider_scope
        else:
            condition_text = rider_scope[: saving_throw_2024_m.start()]
        condition_riders_2024 = _condition_riders_2024(condition_text)

        if len(damage_2024) == 0 and len(condition_riders_2024) == 0:
            return unmodeled("2024 attack roll line without parseable damage")

        atk_range_2024 = "melee" if "melee" in atk2024.group(1).lower() else "ranged"
        attack_type_2024 = f"{atk_range_2024}_weapon"
        combined_damage_2024 = [damage_2024[0]] if damage_2024 else []

        reach_m2 = _REACH_RE.search(desc)
        range_m2 = _RANGE_RE.search(desc)

        # "plus N (dice) type damage" — every group after the first, unless
        # it belongs to a conditional sentence handled below (same shape as
        # 2014).
        conditional_m2 = _CONDITIONAL_DAMAGE_RE.search(after_roll)
        conditional_damage_2024: list[ConditionalDamage] = []
        for g in damage_2024[1:]:
            if conditional_m2 and _strip_spaces(conditional_m2.group(2)) == g.dice:
                continue
            combined_damage_2024.append(g)
        if conditional_m2:
            conditional_damage_2024.append(
                ConditionalDamage(
                    condition=conditional_m2.group(1).lower(),
                    dice=_strip_spaces(conditional_m2.group(2)),
                    type=conditional_m2.group(3).lower(),
                )
            )

        # Save rider after the hit (2014 or 2024 clause shape) — runs even
        # when condition riders matched (an action can carry both); a
        # condition already captured unconditionally above stays off the
        # save's list. Probed inside rider_scope only, so a downstream
        # maintenance save never attaches to the hit.
        rider_save_2024 = _save_clause(rider_scope) or _save_clause_2024(rider_scope)
        on_hit_save_2024: SaveRider | None = None
        if rider_save_2024:
            assert saving_throw_2024_m is not None
            after_save_2024 = rider_scope[saving_throw_2024_m.start() :]
            already = {e.effect for e in condition_riders_2024}
            tags_2024 = [t for t in _condition_tags_in(after_save_2024) if t not in already]
            on_hit_save_2024 = SaveRider(
                dc=rider_save_2024.dc,
                save=rider_save_2024.save,
                effects=[OnHitEffect(effect=t) for t in tags_2024],
            )

        return AttackAction(
            name=name,
            desc=desc,
            usage=usage,
            attack_type=attack_type_2024,
            to_hit=int(atk2024.group(2)),
            reach=int(reach_m2.group(1)) if reach_m2 else None,
            range=int(range_m2.group(1)) if range_m2 else None,
            range_long=(
                int(range_m2.group(2)) if range_m2 and range_m2.group(2) is not None else None
            ),
            damage=combined_damage_2024,
            on_hit_effects=condition_riders_2024,
            conditional_damage=conditional_damage_2024,
            on_hit_save=on_hit_save_2024,
        )

    # 2. Autodamage: "One Grappled creature takes 28 (4d12) bludgeoning
    #    damage..." — damage without an attack roll or a save gating it.
    auto = _AUTODAMAGE_RE.search(desc)
    save = _save_clause(desc)
    # A "*Failure:*"-labeled desc with a 2024 save clause is a 2024 save
    # action, full stop — an incidental "takes N (dice) damage" phrase in
    # its flavor/failure text (invisible-stalker's Vortex) must not
    # pre-empt it into autodamage. The positional tiebreak below likewise
    # has to see a save clause of either grammar era.
    save2024_probe = _save_clause_2024(desc)
    is_labeled_2024_save = save2024_probe is not None and bool(_FAILURE_LABEL_RE.search(desc))
    save_or_2024 = save or save2024_probe
    autodamage_wins = not is_labeled_2024_save and save_or_2024 is None
    if not is_labeled_2024_save and save_or_2024 is not None and auto is not None:
        takes_m = _TAKES_PAREN_RE.search(desc)
        dc_m = _DC_RE.search(desc)
        autodamage_wins = (
            takes_m is not None and dc_m is not None and takes_m.start() < dc_m.start()
        )
    if auto and autodamage_wins:
        auto_damage = [DamageGroup(dice=_strip_spaces(auto.group(1)), type=auto.group(2).lower())]
        targets = _target_clause(desc)
        req_m = _REQUIRES_CONDITION_RE.search(desc)
        requires_target_condition = (
            req_m.group(1).lower() if req_m and req_m.group(1).lower() in CONDITION_TAGS else None
        )
        attached_save: AttachedSave | None = None
        if save:
            saving_throw_m = _SAVING_THROW_RE.search(desc)
            assert saving_throw_m is not None
            after_save = desc[saving_throw_m.start() :]
            attached_save = AttachedSave(
                dc=save.dc,
                save=save.save,
                effects=[OnHitEffect(effect=t) for t in _condition_tags_in(after_save)],
            )
        return AutodamageAction(
            name=name,
            desc=desc,
            usage=usage,
            damage=auto_damage,
            targets=targets,
            requires_target_condition=requires_target_condition,
            attached_save=attached_save,
        )

    # 3. Save-based action: "must succeed on a DC 16 Constitution saving
    #    throw or take/or be ..."
    if save:
        saving_throw_m = _SAVING_THROW_RE.search(desc)
        assert saving_throw_m is not None
        after_save = desc[saving_throw_m.start() :]
        dmg = _damage_groups(after_save)
        on_fail_damage = [dmg[0]] if dmg else []
        half_on_save = bool(_HALF_DAMAGE_RE.search(after_save)) if dmg else False
        stripped = _HALF_DAMAGE_STRIP_RE.sub("", after_save)
        tags = _condition_tags_in(stripped)
        on_fail_effects = [OnHitEffect(effect=t) for t in tags]
        if len(dmg) == 0 and len(tags) == 0:
            return unmodeled("save with no parseable damage or condition")
        return SaveAction(
            name=name,
            desc=desc,
            usage=usage,
            dc=save.dc,
            save=save.save,
            targets=_target_clause(desc),
            on_fail=OnFail(damage=on_fail_damage, effects=on_fail_effects),
            half_on_save=half_on_save,
        )

    # 3b. 2024 save-based action: "<Ability> Saving Throw: DC N, <target>.
    #     *Failure:* <damage/effects>. *Success:* <half damage or nothing>."
    save_2024 = _save_clause_2024(desc)
    if save_2024:
        saving_throw_m2 = _SAVING_THROW_RE.search(desc)
        assert saving_throw_m2 is not None  # _save_clause_2024 matched "Saving Throw"
        after_label = desc[saving_throw_m2.start() :]
        clauses = _labeled_clauses_2024(after_label)
        dmg2024 = _damage_groups(clauses.failure)
        on_fail_damage2024 = [dmg2024[0]] if dmg2024 else []
        half_on_save2024 = bool(_HALF_DAMAGE_2024_RE.search(clauses.success))
        tags2024 = _condition_tags_in(clauses.failure)
        on_fail_effects2024 = [OnHitEffect(effect=t) for t in tags2024]
        if len(dmg2024) == 0 and len(tags2024) == 0:
            return unmodeled("2024 save action with no parseable damage or condition")
        return SaveAction(
            name=name,
            desc=desc,
            usage=usage,
            dc=save_2024.dc,
            save=save_2024.save,
            targets=_target_clause(clauses.target),
            on_fail=OnFail(damage=on_fail_damage2024, effects=on_fail_effects2024),
            half_on_save=half_on_save2024,
        )

    return unmodeled()


class RoutineStep(BaseModel):
    """One ordered step of a Multiattack routine: N uses of a sibling action.

    ``alternatives`` carries the "with its dagger or shortbow" preference
    form's un-chosen options (empty for the ordinary count-per-name form).
    """

    model_config = ConfigDict(frozen=True)

    ref: str
    count: int
    alternatives: list[str] = Field(default_factory=list)


def parse_multiattack(desc: str, action_names: list[str]) -> list[RoutineStep] | None:
    """Parse a Multiattack action's ``desc`` into an ordered routine.

    ``action_names`` are the sibling action names (already usage-stripped)
    to fuzzy-match against — port of the reference file's
    ``parseMultiattack``. Unmatched phrasing returns ``None`` (the caller
    warns); this function never guesses.
    """
    lower = desc.lower()
    # Strip trailing alternatives: "It can replace ..." — preference only.
    main = _MULTIATTACK_ALTERNATIVES_SPLIT_RE.split(lower)[0]

    # Form A/C: "<count> <Name> attack(s)" per clause, including the
    # colon-list "makes three attacks: one Bite, one Claw, and one Tongue
    # Lash".
    steps: list[tuple[str, int, int]] = []
    for name_raw in action_names:
        name = name_raw.lower()
        if name in ("multiattack", ""):
            continue
        pattern = re.compile(
            rf"({_MULTIATTACK_COUNT_WORD_ALT}|a|\d+)\s+{re.escape(name)}"
            r"(?=\s+attacks?|\s*[,.]|\s+and\b|$)"
        )
        for m in pattern.finditer(main):
            word = m.group(1)
            if word in _NUMBER_WORDS:
                count = _NUMBER_WORDS[word]
            elif word == "a":
                count = 1
            else:
                count = int(word)
            steps.append((name_raw, count, m.start()))
    if steps:
        steps.sort(key=lambda s: s[2])
        return [RoutineStep(ref=ref, count=count) for ref, count, _order in steps]

    # Form B: "makes two attacks with its dagger or shortbow" — count
    # applies to a choice; encode as first-listed preference.
    with_form = _WITH_FORM_RE.search(main)
    if with_form:
        with_word = with_form.group(1)
        with_count: int | None = _NUMBER_WORDS.get(with_word)
        if with_count is None:
            try:
                with_count = int(with_word)
            except ValueError:
                with_count = None
        if with_count is not None:
            options = [o.strip() for o in re.split(r"\s+or\s+", with_form.group(2))]
            matched: list[str] = []
            for opt in options:
                for n in action_names:
                    if n.lower() == opt or opt in n.lower():
                        matched.append(n)
                        break
            if matched:
                return [RoutineStep(ref=matched[0], count=with_count, alternatives=matched[1:])]
    return None


_LEGENDARY_PREAMBLE_NAME_RE = re.compile(r"^Legendary Actions$", re.IGNORECASE)
_LEGENDARY_PREAMBLE_DESC_RE = re.compile(r"can take (\d+|\w+) legendary actions?\b", re.IGNORECASE)


def _is_legendary_preamble(category: str, raw: dict[str, Any]) -> bool:
    """Port of ``parseActionList``'s ``isPreamble`` check (grammar-era-agnostic)."""
    if category != "legendary_actions":
        return False
    name = raw.get("name") or ""
    desc = raw.get("desc") or ""
    return (
        name == ""
        or bool(_LEGENDARY_PREAMBLE_NAME_RE.match(name))
        or bool(_LEGENDARY_PREAMBLE_DESC_RE.search(desc))
    )


def legendary_actions_per_round(entries: list[dict[str, Any]] | None) -> int:
    """How many legendary actions this creature takes per round, from its
    own ``legendary_actions`` fence category's preamble entry. The
    preamble's own count wins when present (``"can take N legendary
    actions"``); absent an explicit count but with at least one named
    legendary action, the SRD default of 3 applies; zero named legendary
    actions means this creature isn't legendary at all.
    """
    if not entries:
        return 0
    named_count = 0
    for raw in entries:
        if not isinstance(raw, dict):
            continue
        if not _is_legendary_preamble("legendary_actions", raw):
            named_count += 1
            continue
        desc = raw.get("desc") or ""
        m = _LEGENDARY_PREAMBLE_DESC_RE.search(desc)
        if m and m.group(1).isdigit():
            return int(m.group(1))
    return 3 if named_count > 0 else 0


def parse_action_category(
    entries: list[dict[str, Any]] | None, category: str
) -> tuple[list[Action], list[str]]:
    """Parse one action category's raw ``{name, desc}`` entries.

    ``category`` is one of ``actions``/``bonus_actions``/``reactions``/
    ``legendary_actions`` — a statblock fence's four action lists. Skips a
    legendary-actions preamble entry (``_is_legendary_preamble``) and, for
    the ``"actions"`` category only, a ``kind="multiattack"`` entry —
    mirroring ``main.actions.filter(a => a.kind !== 'multiattack')`` in
    ``statblock-parse.mjs``. A Multiattack action survives only to build a
    routine (:func:`parse_multiattack`) — a whole-statblock-level concern
    the caller resolves separately, against this category's own action
    names, not this function.

    Returns ``(actions, warnings)``. Every action this grammar could not
    model contributes a warning here — "an explicitly unmodeled action
    carrying a warning, never a silent drop" (issue #41's acceptance
    criterion) — plus every partial-recognition warning an individual
    action itself carries.
    """
    actions: list[Action] = []
    warnings: list[str] = []
    for raw in entries or []:
        if not isinstance(raw, dict) or _is_legendary_preamble(category, raw):
            continue
        action = parse_action(raw.get("name"), raw.get("desc"))
        if category == "actions" and action.kind == "multiattack":
            continue
        if action.kind == "unmodeled":
            warnings.append(
                f"unmodeled {category.replace('_', ' ')}: {action.name} — supply mechanics "
                "via a per-action sim: block on the page, or creature_overrides in a loadout "
                "file for a scenario-specific tweak"
            )
        for w in action.warnings:
            warnings.append(f"{action.name}: {w}")
        actions.append(action)
    return actions, warnings
