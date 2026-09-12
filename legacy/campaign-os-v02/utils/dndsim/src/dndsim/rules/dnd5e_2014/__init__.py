"""D&D 5th Edition (2014) Rules pack.

Everything ruleset-specific (attack rolls, armour class, damage dice) lives
under this package, never in ``dndsim.core`` — ADR-0007. Discovered through
the ``dndsim.rules`` entry-point group declared in ``pyproject.toml``.
"""

from __future__ import annotations


def register() -> None:
    """Entry point target: importing these modules registers their contents."""
    from dndsim.rules.dnd5e_2014 import compile as _compile  # noqa: F401
    from dndsim.rules.dnd5e_2014 import conditions as _conditions  # noqa: F401
    from dndsim.rules.dnd5e_2014 import death_saves as _death_saves  # noqa: F401
    from dndsim.rules.dnd5e_2014 import exhaustion as _exhaustion  # noqa: F401
    from dndsim.rules.dnd5e_2014 import mechanics as _mechanics  # noqa: F401
    from dndsim.rules.dnd5e_2014 import primitives as _primitives  # noqa: F401
    from dndsim.rules.dnd5e_2014 import sim_extension as _sim_extension  # noqa: F401
    from dndsim.rules.dnd5e_2014 import spells as _spells  # noqa: F401
    from dndsim.rules.dnd5e_2014 import statblock as _statblock  # noqa: F401
