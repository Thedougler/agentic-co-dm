"""The Primitive contract: the closed vocabulary boundary compiled content may not cross.

A Primitive is one member of the closed vocabulary of effects the engine
can execute and the planner can value (docs/CONTEXT.md § Combat simulation
— Primitive). Content composes Primitives; content never introduces one —
enforced by requiring every Primitive kind to resolve through
:data:`primitives` rather than a hand-written branch anywhere else in the
codebase (the same registration-replaces-dispatch shape as
:data:`dndsim.core.mechanic.mechanics` and :data:`dndsim.core.importer.importers`).

This module holds only the marker base and its registry. What a Primitive
actually *is* is 5e knowledge a Rules pack supplies (ADR-0007); the core may
not name any of it here.
"""

from __future__ import annotations

from dndsim.core.registry import Registry


class Primitive:
    """Marker base for one compiled, executable effect step.

    Concrete shape (fields, validation) is Rules-pack knowledge — this
    class intentionally declares none, so subclassing it costs nothing
    from ``dndsim.core`` and cannot leak rules vocabulary here. Not an ABC:
    it has no abstract method to enforce (the contract is "resolves through
    :data:`primitives`", not a required method), and a bare marker needs no
    instantiation guard.
    """


primitives: Registry[type[Primitive]] = Registry("dndsim.primitives")
