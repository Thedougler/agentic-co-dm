"""The Primitive contract's generic registry (issue #43)."""

from __future__ import annotations

from dndsim.core.primitive import Primitive, primitives


def test_registering_a_primitive_class_needs_no_core_edit() -> None:
    class DummyPrimitive(Primitive):
        pass

    primitives.register_value("test:primitive/dummy", DummyPrimitive)
    assert primitives.get("test:primitive/dummy") is DummyPrimitive
    assert "test:primitive/dummy" in primitives


def test_primitive_is_a_bare_marker_with_no_declared_attributes() -> None:
    non_dunder = {name for name in vars(Primitive) if not name.startswith("__")}
    assert non_dunder == set()
