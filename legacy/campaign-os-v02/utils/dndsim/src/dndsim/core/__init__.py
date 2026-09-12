"""The rules-agnostic engine core.

Nothing under ``dndsim.core`` may import from ``dndsim.rules`` or name a
ruleset concept (armour class, hit points, conditions, saving throws, ...).
See docs/adr/0007-dndsim-engine-is-rules-agnostic.md.
"""
