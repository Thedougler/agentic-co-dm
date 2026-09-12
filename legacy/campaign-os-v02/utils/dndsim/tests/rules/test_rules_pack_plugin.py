"""AC (issue #55): "2014 and 2024 install as separate Rules packs,
discovered through the plugin group." Both are real entry points in the
``dndsim.rules`` group (``pyproject.toml``'s
``[project.entry-points."dndsim.rules"]``) — this test drives the exact
discovery mechanism ``dndsim.plugins.load_rules_packs`` itself uses
(``importlib.metadata.entry_points``), the same way
``tests/ai/test_policy_plugin.py`` proves the Policy group.
"""

from __future__ import annotations

from importlib.metadata import entry_points


def test_both_editions_are_declared_entry_points_in_the_rules_group() -> None:
    names = {ep.name for ep in entry_points(group="dndsim.rules")}
    assert names == {"dnd5e_2014", "dnd5e_2024"}


def test_dnd5e_2024_register_delegates_to_2014_and_is_idempotent() -> None:
    """`dnd5e_2024/__init__.py`'s `register()` calls `dnd5e_2014.register()`
    itself rather than relying on `dndsim.plugins.load_rules_packs` having
    already loaded 2014's own entry point too — a genuinely standalone
    installable pack (ADR-0007), not merely "2014 plus a flag" that only
    works loaded second. Calling it more than once (as this process's
    other test modules already have, each doing their own
    `plugins.load_rules_packs()`) must never raise
    `DuplicateRegistrationError` — every module's own registration runs
    once, at that module's first import, no matter how many times
    `register()` itself is called."""
    import dndsim.rules.dnd5e_2024 as dnd5e_2024
    from dndsim.rules.dnd5e_2024.exhaustion import RULES_ID
    from dndsim.rules.exhaustion import exhaustion_rules

    dnd5e_2024.register()
    dnd5e_2024.register()
    assert RULES_ID in exhaustion_rules
