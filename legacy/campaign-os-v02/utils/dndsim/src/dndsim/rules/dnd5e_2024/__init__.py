"""D&D 5th Edition (2024) Rules pack.

Discovered through the same ``dndsim.rules`` entry-point group as
``dnd5e_2014`` (ADR-0007; ``pyproject.toml``'s
``[project.entry-points."dndsim.rules"]``) — a second, separately
installed pack, not a mode flag on the first one. This pass's one genuine
divergence from 2014 is Exhaustion (`dnd5e_2024/exhaustion.py`, issue #55);
every mechanic the two editions agree on — conditions, attack/damage/save
resolution, the statblock grammar, the compile pipeline — is 2014's own
registration, reused directly rather than duplicated (`register()` below
delegates to it), matching this issue's own principle: shared where the
editions agree, pack-scoped only where they genuinely differ.
"""

from __future__ import annotations


def register() -> None:
    """Entry point target. Delegates to `dnd5e_2014.register()` for every
    shared registration (safe to call even when `dndsim.plugins.
    load_rules_packs` has already loaded `dnd5e_2014`'s own entry point
    too — a module's registration side effects run once, at that module's
    first import, no matter how many times `register()` itself is called),
    then registers this edition's own Exhaustion numbers."""
    from dndsim.rules.dnd5e_2014 import register as _register_2014

    _register_2014()
    from dndsim.rules.dnd5e_2024 import exhaustion as _exhaustion  # noqa: F401
