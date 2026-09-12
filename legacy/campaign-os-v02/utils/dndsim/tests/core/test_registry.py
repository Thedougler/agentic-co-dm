from __future__ import annotations

import pytest

from dndsim.core.registry import DuplicateRegistrationError, Registry


def test_register_decorator_then_get() -> None:
    reg: Registry[type] = Registry("test.group")

    @reg.register("ns:kind/thing")
    class Thing:
        pass

    assert reg.get("ns:kind/thing") is Thing


def test_duplicate_registration_raises() -> None:
    reg: Registry[str] = Registry("test.group")
    reg.register_value("ns:kind/thing", "a")
    with pytest.raises(DuplicateRegistrationError):
        reg.register_value("ns:kind/thing", "b")


def test_get_missing_raises_key_error() -> None:
    reg: Registry[str] = Registry("test.group")
    with pytest.raises(KeyError, match="ns:kind/missing"):
        reg.get("ns:kind/missing")


def test_contains_and_len_and_iteration() -> None:
    reg: Registry[str] = Registry("test.group")
    reg.register_value("a", "va")
    reg.register_value("b", "vb")
    assert "a" in reg
    assert "z" not in reg
    assert len(reg) == 2
    assert set(reg) == {"a", "b"}
    assert dict(reg.items()) == {"a": "va", "b": "vb"}
    assert set(reg.values()) == {"va", "vb"}
