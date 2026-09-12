"""Entities and attributes with a generic modifier stack.

An :class:`Entity` is a bag of :class:`Attribute` values, resource pools, and
tags, identified by a stable ``namespace:type/slug`` id (see
docs/adr/0007-dndsim-engine-is-rules-agnostic.md). Neither this module nor
anything else under ``dndsim.core`` knows what an attribute *means* — a Rules
pack decides which named attributes exist at all.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Literal

ModifierOp = Literal["add", "mul", "override"]


@dataclass(frozen=True, slots=True)
class Modifier:
    """One entry in an attribute's modifier stack.

    ``source`` identifies what applied the modifier (an id, for later
    removal/inspection) and is opaque to the core.
    """

    source: str
    op: ModifierOp
    value: float


@dataclass(slots=True)
class Attribute:
    """A named numeric value plus a stack of modifiers.

    Resolution order: start from ``base``, sum every ``"add"`` modifier, then
    multiply by the product of every ``"mul"`` modifier, then — if any
    ``"override"`` modifier is present — replace the result with the value of
    the last ``"override"`` modifier in the stack.
    """

    name: str
    base: float
    modifiers: list[Modifier] = field(default_factory=list)

    def add(self, source: str, op: ModifierOp, value: float) -> None:
        self.modifiers.append(Modifier(source=source, op=op, value=value))

    def remove_source(self, source: str) -> None:
        self.modifiers = [m for m in self.modifiers if m.source != source]

    def value(self) -> float:
        total = self.base + sum(m.value for m in self.modifiers if m.op == "add")
        for m in self.modifiers:
            if m.op == "mul":
                total *= m.value
        overrides = [m.value for m in self.modifiers if m.op == "override"]
        if overrides:
            return overrides[-1]
        return total


@dataclass(slots=True)
class Entity:
    """A stable-id participant in a simulation.

    ``attributes`` holds scalar, per-entity values (an entity's attack bonus
    is the same in every universe of a batch); anything that diverges across
    universes belongs in a resource pool (:mod:`dndsim.core.resources`) or
    other batched state instead.
    """

    id: str
    name: str
    attributes: dict[str, Attribute] = field(default_factory=dict)
    tags: set[str] = field(default_factory=set)

    def attr(self, name: str) -> Attribute:
        try:
            return self.attributes[name]
        except KeyError:
            raise KeyError(f"entity {self.id!r} has no attribute {name!r}") from None

    def has_tag(self, tag: str) -> bool:
        return tag in self.tags
