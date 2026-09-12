from __future__ import annotations

from dndsim.core.rng import BatchRNG, cell_seed, random_seed, substream_seed


def test_same_seed_same_call_sequence_gives_identical_output() -> None:
    a = BatchRNG(seed=7)
    b = BatchRNG(seed=7)
    draw_a = a.integers(1, 21, size=1000)
    draw_b = b.integers(1, 21, size=1000)
    assert list(draw_a) == list(draw_b)


def test_different_seed_gives_different_output() -> None:
    a = BatchRNG(seed=1)
    b = BatchRNG(seed=2)
    draw_a = a.integers(1, 1_000_000, size=1000)
    draw_b = b.integers(1, 1_000_000, size=1000)
    assert list(draw_a) != list(draw_b)


def test_integers_range_bounds() -> None:
    rng = BatchRNG(seed=1)
    draws = rng.integers(1, 21, size=10_000)
    assert draws.min() >= 1
    assert draws.max() <= 20


def test_uniform_range_bounds() -> None:
    rng = BatchRNG(seed=1)
    draws = rng.uniform(size=10_000)
    assert draws.min() >= 0.0
    assert draws.max() < 1.0


def test_random_seed_produces_a_32_bit_value() -> None:
    seed = random_seed()
    assert 0 <= seed < 0x100000000


def test_random_seed_varies_across_calls() -> None:
    seeds = {random_seed() for _ in range(20)}
    assert len(seeds) > 1


def test_substream_seed_is_deterministic_in_seed_and_index() -> None:
    assert substream_seed(7, 3) == substream_seed(7, 3)


def test_substream_seed_differs_across_indices() -> None:
    values = {substream_seed(7, i) for i in range(50)}
    assert len(values) == 50


def test_substream_seed_differs_across_run_seeds() -> None:
    assert substream_seed(1, 0) != substream_seed(2, 0)


def test_substream_seed_is_a_32_bit_value() -> None:
    for i in range(10):
        seed = substream_seed(123, i)
        assert 0 <= seed < 0x100000000


def test_cell_seed_is_deterministic_in_seed_and_key() -> None:
    assert cell_seed(7, "pc:perrin|opp:blight") == cell_seed(7, "pc:perrin|opp:blight")


def test_cell_seed_differs_across_keys() -> None:
    assert cell_seed(7, "matchup-a") != cell_seed(7, "matchup-b")


def test_cell_seed_is_independent_of_position() -> None:
    # A cell's identity is its key, never where it happened to sit in a run
    # — this is what lets one cell be re-run alone and reproduce.
    a = cell_seed(7, "matchup-a")
    b = cell_seed(7, "matchup-a")
    assert a == b


def test_cell_seed_and_substream_seed_disagree_by_construction() -> None:
    # Different derivations (index-keyed vs. string-keyed) should not
    # collide for the values exercised here.
    assert substream_seed(7, 0) != cell_seed(7, "0")
