from __future__ import annotations

from dndsim.core.entity import Attribute, Entity


def test_attribute_base_value_only() -> None:
    attr = Attribute(name="x", base=10)
    assert attr.value() == 10


def test_attribute_add_modifiers_sum() -> None:
    attr = Attribute(name="x", base=10)
    attr.add("item:ring", "add", 2)
    attr.add("buff:bless", "add", 3)
    assert attr.value() == 15


def test_attribute_mul_applies_after_add() -> None:
    attr = Attribute(name="x", base=10)
    attr.add("buff:a", "add", 10)
    attr.add("buff:b", "mul", 2)
    assert attr.value() == 40  # (10 + 10) * 2


def test_attribute_override_wins() -> None:
    attr = Attribute(name="x", base=10)
    attr.add("buff:a", "add", 100)
    attr.add("effect:polymorph", "override", 1)
    assert attr.value() == 1


def test_attribute_override_last_one_wins() -> None:
    attr = Attribute(name="x", base=10)
    attr.add("a", "override", 1)
    attr.add("b", "override", 2)
    assert attr.value() == 2


def test_remove_source_drops_only_its_modifiers() -> None:
    attr = Attribute(name="x", base=10)
    attr.add("buff:a", "add", 5)
    attr.add("buff:b", "add", 7)
    attr.remove_source("buff:a")
    assert attr.value() == 17


def test_entity_attr_lookup() -> None:
    entity = Entity(id="ns:type/slug", name="Test", attributes={"x": Attribute("x", 5)})
    assert entity.attr("x").value() == 5


def test_entity_attr_missing_raises_key_error() -> None:
    entity = Entity(id="ns:type/slug", name="Test")
    try:
        entity.attr("missing")
    except KeyError as exc:
        assert "missing" in str(exc)
    else:
        raise AssertionError("expected KeyError")


def test_entity_tags() -> None:
    entity = Entity(id="ns:type/slug", name="Test", tags={"flying"})
    assert entity.has_tag("flying")
    assert not entity.has_tag("burrowing")
