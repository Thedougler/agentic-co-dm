from __future__ import annotations

import threading
import time
from collections.abc import Callable

import pytest

from dndsim.core.threaded import run_threaded


def test_serial_and_threaded_produce_identical_results() -> None:
    cells = [(lambda i=i: i * i) for i in range(20)]
    serial = run_threaded(cells, max_workers=1)
    threaded = run_threaded(cells, max_workers=4)
    assert serial == threaded == [i * i for i in range(20)]


def test_results_land_at_the_calling_cells_index_regardless_of_finish_order() -> None:
    # Cell 0 sleeps longest, cell N-1 shortest — if results were written in
    # completion order rather than by index, this would come back reversed.
    def make_cell(i: int, delay: float) -> Callable[[], int]:
        def _cell() -> int:
            time.sleep(delay)
            return i

        return _cell

    n = 8
    cells: list[Callable[[], int]] = [make_cell(i, (n - i) * 0.01) for i in range(n)]
    result = run_threaded(cells, max_workers=n)
    assert result == list(range(n))


def test_output_identical_across_several_thread_counts() -> None:
    cells = [(lambda i=i: i + 1) for i in range(50)]
    results = {workers: run_threaded(cells, max_workers=workers) for workers in (1, 2, 5, 16)}
    expected = list(range(1, 51))
    for workers, result in results.items():
        assert result == expected, f"workers={workers} diverged"


def test_cells_actually_run_on_separate_threads_when_workers_over_one() -> None:
    seen: set[int] = set()
    lock = threading.Lock()

    def make_cell() -> Callable[[], int]:
        def _cell() -> int:
            with lock:
                seen.add(threading.get_ident())
            time.sleep(0.01)
            return 0

        return _cell

    run_threaded([make_cell() for _ in range(8)], max_workers=4)
    assert len(seen) > 1


def test_max_workers_below_one_raises() -> None:
    with pytest.raises(ValueError):
        run_threaded([lambda: 1], max_workers=0)


def test_empty_cells_returns_empty_list() -> None:
    assert run_threaded([], max_workers=4) == []
