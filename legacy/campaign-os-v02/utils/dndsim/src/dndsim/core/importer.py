"""The Importer contract (ADR-0009): authored content stays in the vault.

An Importer reads one kind of authored fence (the Fantasy Statblocks
` ```statblock ` block, and others a Rules pack may add later) and
normalizes it — never a rival content store. This module holds only the generic contract
and its registry; a Rules pack supplies every concrete Importer and every
normalized content shape, since the fence's key vocabulary is ruleset
knowledge (ADR-0007).

``T`` is the normalized content type a given Importer produces — deliberately
unconstrained here, since the shape of "normalized statblock content" is
Rules-pack knowledge the core may not name.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import ClassVar

from dndsim.core.registry import Registry


class Importer[T](ABC):
    """Reads one authored-content fence and normalizes it, or raises loudly."""

    id: ClassVar[str]

    @abstractmethod
    def parse(self, text: str, source_path: str) -> T | None:
        """Normalize ``text`` (the source page's full markdown).

        Returns ``None`` when the page carries an empty fence (a stub, not
        an error). Raises on a missing required key or a value the format
        cannot make sense of, naming the offending key and ``source_path``.
        """


importers: Registry[type[Importer[object]]] = Registry("dndsim.importers")
