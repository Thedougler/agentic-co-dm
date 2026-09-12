"""Plugin-group discovery.

Rules packs declare themselves under the ``dndsim.rules`` entry-point group
(see ``pyproject.toml``'s ``[project.entry-points."dndsim.rules"]``) so an
out-of-tree package can install one without an engine change (ADR-0007).
:func:`load_rules_packs` loads every declared pack once; each pack's
``register()`` entry point is responsible for registering its own Mechanics
into :data:`dndsim.core.mechanic.mechanics`.

Policies declare themselves the same way, under ``dndsim.policies`` (issue
#44) — :func:`load_policies` loads every declared Policy into
:data:`dndsim.core.policy.policies` once.
"""

from __future__ import annotations

from dndsim.core.policy import policies
from dndsim.core.registry import Registry

rules_packs: Registry[None] = Registry("dndsim.rules")


def load_rules_packs() -> None:
    rules_packs.load_entry_points()


def load_policies() -> None:
    policies.load_entry_points()
