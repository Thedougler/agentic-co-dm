"""A ``yaml.safe_load`` drop-in whose bool resolution matches the JS
reference engine's ``yaml`` package (YAML 1.2 core schema: only
``true``/``false`` resolve to booleans) instead of PyYAML's default YAML 1.1
resolver (which also treats ``on``/``off``/``yes``/``no`` as booleans).

Extracted from ``loadouts.py`` (issue #49, which hit this for
``{kind: advantage, on: attack}`` modifiers) so every vault-content YAML
call site can share one loader rather than re-deriving it — issue #66 found
``statblock.py``, ``spells.py``, ``profile.py`` and ``lint/rules.py`` all
still calling plain ``yaml.safe_load``, which misparses an unquoted
``on:`` key as the boolean key ``True`` the moment such content is actually
read. Five real loadout files author this literally (Perrin, Delmar,
Crissdalynn, Catarina, Jean-Claude): the YAML is valid and the files are the
DM's — fix the loader, not the content."""

from __future__ import annotations

import re
from typing import Any

import yaml


class _YamlLoader(yaml.SafeLoader):
    """``yaml.SafeLoader`` with YAML 1.1's ``on``/``off``/``yes``/``no``
    boolean words disabled — matches the YAML 1.2 core-schema boolean
    resolution the reference engine's parser (the JS ``yaml`` package) uses,
    where only ``true``/``false`` resolve to booleans. Without this, an
    unquoted ``on:`` key in an ``{kind: advantage, on: attack}`` modifier —
    real content authors this literally
    (``perrin-black-jaw.loadouts.yaml``) — resolves to the boolean key
    ``True``, not the string ``"on"``, and the modifier fails to validate."""


_YamlLoader.yaml_implicit_resolvers = {
    key: [(tag, regexp) for tag, regexp in resolvers if tag != "tag:yaml.org,2002:bool"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}
_YamlLoader.add_implicit_resolver(  # type: ignore[no-untyped-call]  # types-pyyaml stub gap
    "tag:yaml.org,2002:bool", re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$"), list("tTfF")
)


def safe_load(raw: str) -> Any:
    """``yaml.safe_load`` with the YAML-1.2-only bool resolver above. Use
    this, never ``yaml.safe_load``, for any YAML read from vault content
    (a statblock fence, a loadout file) — the same rule ``loadouts.py``
    already followed before this module existed."""
    return yaml.load(raw, Loader=_YamlLoader)
