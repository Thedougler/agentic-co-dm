"""ADR-0007: the core holds zero D&D knowledge and never imports a Rules pack."""

from __future__ import annotations

import re
from pathlib import Path

import dndsim.core

CORE_DIR = Path(dndsim.core.__file__).parent

# Whole-word, case-insensitive: naming any of these in core is a rules leak.
FORBIDDEN_WORDS = [
    "armor_class",
    "armour_class",
    r"\bac\b",
    "hit_points",
    r"\bhp\b",
    "saving_throw",
    "advantage",
    "disadvantage",
    "condition",
    "spell",
    "d20",
]


# core/__init__.py's own docstring states the ADR-0007 exclusion list by
# name — that's the rule being described, not a violation of it.
_EXEMPT = {"__init__.py"}


def _core_source_files() -> list[Path]:
    return sorted(p for p in CORE_DIR.rglob("*.py") if p.name not in _EXEMPT)


def test_core_has_source_files() -> None:
    assert _core_source_files(), f"expected .py files under {CORE_DIR}"


def test_core_never_imports_a_rules_pack() -> None:
    for path in _core_source_files():
        text = path.read_text()
        assert "dndsim.rules" not in text, f"{path} imports a Rules pack"


def test_core_names_no_dnd_vocabulary() -> None:
    for path in _core_source_files():
        text = path.read_text().lower()
        for word in FORBIDDEN_WORDS:
            match = re.search(word, text)
            assert match is None, f"{path} names forbidden D&D vocabulary: {word!r}"
