"""Thread-count-independent execution of independent work cells (ADR-0012).

Free-threaded CPython (``3.14t``, no GIL) was chosen specifically so
independent cells — separate matchups in a sweep, separate members of a GA
population — can run across real OS threads with no state pickled between
them and no interpreter-level serialization forcing them back onto one
core. What this module adds on top of that: a cell's *result* lands at its
own index in the returned list regardless of which order threads finish
in, so the list a caller gets back is identical no matter how many workers
processed it. Thread count is purely a performance knob; it must never be
read as an input to what gets computed — only how fast.
"""

from __future__ import annotations

from collections.abc import Callable, Sequence
from concurrent.futures import ThreadPoolExecutor
from typing import cast


def run_threaded[T](cells: Sequence[Callable[[], T]], max_workers: int = 1) -> list[T]:
    """Run each zero-argument callable in ``cells``, in ``cells`` order.

    ``max_workers <= 1`` (the default) or fewer than two cells runs serially
    with no thread pool constructed at all — identical to the threaded path's
    output, just without the parallelism.
    """
    if max_workers < 1:
        raise ValueError(f"max_workers must be >= 1, got {max_workers}")
    if max_workers == 1 or len(cells) <= 1:
        return [cell() for cell in cells]

    results: list[T | None] = [None] * len(cells)
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = [pool.submit(cell) for cell in cells]
        for index, future in enumerate(futures):
            results[index] = future.result()
    return cast(list[T], results)
