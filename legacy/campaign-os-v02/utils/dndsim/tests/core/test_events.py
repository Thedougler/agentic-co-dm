from __future__ import annotations

from dndsim.core.events import Event, EventBus


def test_publish_calls_subscribed_handler() -> None:
    bus = EventBus()
    received: list[Event] = []
    bus.subscribe("on_thing", received.append)
    bus.publish(Event("on_thing", payload={"x": 1}))
    assert len(received) == 1
    assert received[0].payload == {"x": 1}


def test_publish_no_handlers_is_a_no_op() -> None:
    bus = EventBus()
    bus.publish(Event("unheard"))  # must not raise


def test_handlers_called_in_registration_order() -> None:
    bus = EventBus()
    order: list[str] = []
    bus.subscribe("e", lambda _: order.append("first"))
    bus.subscribe("e", lambda _: order.append("second"))
    bus.publish(Event("e"))
    assert order == ["first", "second"]


def test_unsubscribe_stops_delivery() -> None:
    bus = EventBus()
    received: list[Event] = []
    handler = received.append
    bus.subscribe("e", handler)
    bus.unsubscribe("e", handler)
    bus.publish(Event("e"))
    assert received == []


def test_handler_count() -> None:
    bus = EventBus()
    assert bus.handler_count("e") == 0
    bus.subscribe("e", lambda _: None)
    assert bus.handler_count("e") == 1
