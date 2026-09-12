from __future__ import annotations

import numpy as np

from dndsim.core.tags import BatchTags


def test_unknown_tag_reads_as_all_false() -> None:
    tags = BatchTags(size=3)
    assert list(tags.has("never_added")) == [False, False, False]


def test_add_sets_masked_universes() -> None:
    tags = BatchTags(size=3)
    tags.add("x", np.array([True, False, True]))
    assert list(tags.has("x")) == [True, False, True]


def test_remove_clears_masked_universes() -> None:
    tags = BatchTags(size=3)
    tags.add("x", np.array([True, True, True]))
    tags.remove("x", np.array([True, False, False]))
    assert list(tags.has("x")) == [False, True, True]
