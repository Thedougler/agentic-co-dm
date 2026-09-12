"""Every real PC sheet compiles.

Regression guard for the primitive-construction bug: `ModifierBase` allows
extras (the reference never key-checks a modifier), so an authored key that
no Modifier class declared arrived as a pydantic extra. `model_fields` does
not report extras, so an authored `id` bypassed the id-to-ref rename and
collided with the compiled instance's own identity, and any other extra hit
the generated Primitive's `extra="forbid"`. Three of the five party sheets
failed to compile, and a sweep silently skipped them.

Walks live vault pages rather than fixtures on purpose — the same reason
the differential harness does. A fixture copy cannot catch a real sheet
drifting away from what the Modifier vocabulary declares.
"""

from __future__ import annotations

from pathlib import Path

import pytest

from dndsim import plugins
from dndsim.profile import load_compiled_statblock

plugins.load_rules_packs()

REPO_ROOT = Path(__file__).resolve().parents[4]
SHEET_DIR = REPO_ROOT / "vault" / "campaigns" / "shattered-sea" / "pcs" / "character-sheets"


def _sheets() -> list[Path]:
    return sorted(SHEET_DIR.glob("*-sheet.md"))


def test_the_party_sheets_are_actually_discovered() -> None:
    """A discovery break must fail loudly, not pass vacuously."""
    assert len(_sheets()) >= 5


@pytest.mark.parametrize("sheet", _sheets(), ids=lambda p: p.name)
def test_real_pc_sheet_compiles(sheet: Path) -> None:
    compiled = load_compiled_statblock(sheet.read_text(encoding="utf-8"), str(sheet))
    assert compiled is not None


def test_an_authored_key_no_primitive_can_hold_names_itself() -> None:
    """An unknown key must be named, never dropped and never opaque."""
    from dndsim.rules.dnd5e_2014.primitives import modifier_to_primitive
    from dndsim.rules.dnd5e_2014.sim_extension import BonusAttackModifier

    modifier = BonusAttackModifier.model_validate(
        {"kind": "bonus_attack", "attack": "unarmed", "no_such_key": 1}
    )
    with pytest.raises(ValueError, match=r"no field for authored key\(s\) \['no_such_key'\]"):
        modifier_to_primitive(modifier, "dnd5e_2014:primitive/bonus_attack/probe")
