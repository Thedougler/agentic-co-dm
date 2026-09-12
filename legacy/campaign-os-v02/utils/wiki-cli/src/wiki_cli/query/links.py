"""Link-graph read functions for `wiki links in|out|breakdown|orphans` —
pure functions over `QueryContext` plus `Row`s, no CLI/typer concerns."""

from __future__ import annotations

from typing import TYPE_CHECKING

from wiki_cli.query.filters import Row
from wiki_cli.query.runtime import QueryContext, rows_for

if TYPE_CHECKING:
    from wiki_cli.index import VaultIndex


def backlinks(ctx: QueryContext, rel_path: str) -> list[Row]:
    """Pages linking TO `rel_path` — one `Row` per source page."""
    all_rows = {row.rel_path: row for row in rows_for(ctx)}
    linkers = ctx.index.links_to(rel_path)
    return [all_rows[lp] for lp in linkers if lp in all_rows]


def outlinks(ctx: QueryContext, rel_path: str) -> list[Row]:
    """Pages `rel_path` links to (resolved targets only, de-duplicated)."""
    all_rows = {row.rel_path: row for row in rows_for(ctx)}
    targets = ctx.index.links_from(rel_path)
    seen: set[str] = set()
    result: list[Row] = []
    for raw in targets:
        base = raw.split("#", 1)[0]
        resolved = ctx.index.resolve(base)
        if resolved is not None and resolved.rel_path not in seen:
            seen.add(resolved.rel_path)
            row = all_rows.get(resolved.rel_path)
            if row is not None:
                result.append(row)
    return result


def breakdown(
    ctx: QueryContext, to_rows: list[Row], from_rows: list[Row] | None = None
) -> list[tuple[Row, int, list[str]]]:
    """Per `to` page: `(row, backlink_count, sorted_source_rel_paths)`.
    Sources restricted to `from_rows` when given. Sorted ascending by count
    (least-linked first — the balance view)."""
    from_set = {row.rel_path for row in from_rows} if from_rows is not None else None
    results: list[tuple[Row, int, list[str]]] = []
    for row in to_rows:
        sources = list(ctx.index.links_to(row.rel_path))
        if from_set is not None:
            sources = [source for source in sources if source in from_set]
        results.append((row, len(sources), sorted(sources)))
    results.sort(key=lambda entry: entry[1])
    return results


def orphans(ctx: QueryContext, rows: list[Row]) -> list[Row]:
    """Pages with `links-in == 0` within the given `rows`."""
    del ctx  # kept for interface parity with the other functions here
    return [row for row in rows if row.computed.get("links-in", 0) == 0]


def spread(
    ctx: QueryContext,
    to_rows: list[Row],
    from_rows: list[Row],
) -> list[tuple[str, str | None, str, int]]:
    """Surface under-represented targets so the DM can place sources for
    exploration variety — not an auto-balancer.

    Returns: (source_rel_path, current_target_or_None, suggested_target,
    suggested_target_current_count)

    For each `from` source, finds which `to` target it currently links to.
    Unlinked sources get the least-represented target as a starting-point
    suggestion; already-linked sources keep their current target unless the
    gap is stark (> 2), flagging it for the DM to consider.
    """
    to_set = {row.rel_path for row in to_rows}
    from_set = {row.rel_path for row in from_rows}
    counts: dict[str, int] = {}
    for row in to_rows:
        sources = ctx.index.links_to(row.rel_path)
        counts[row.rel_path] = len([source for source in sources if source in from_set])

    results: list[tuple[str, str | None, str, int]] = []

    for src_row in from_rows:
        current: str | None = None
        for link_target in ctx.index.links_from(src_row.rel_path):
            base = link_target.split("#", 1)[0]
            resolved = ctx.index.resolve(base)
            if resolved and resolved.rel_path in to_set:
                current = resolved.rel_path
                break

        least_key = min(counts, key=lambda key: counts[key])
        least_count = counts[least_key]

        if current is None:
            suggested = least_key
            counts[suggested] += 1
            results.append((src_row.rel_path, None, suggested, counts[suggested]))
        else:
            current_count = counts.get(current, 0)
            if current_count - least_count > 2:
                suggested = least_key
                counts[suggested] += 1
                counts[current] -= 1
                results.append((src_row.rel_path, current, suggested, counts[suggested]))
            else:
                results.append((src_row.rel_path, current, current, counts.get(current, 0)))

    return results


def redundant(index: VaultIndex) -> list[tuple[str, str, str, int]]:
    """`(source, section, target_rel_path, count)` for every link occurrence
    repeated more than once from the same section of the same page."""
    results: list[tuple[str, str, str, int]] = []
    for page in index.pages():
        for target, _raw_target, section, count in index.links_detail(page.rel_path):
            if count > 1 and target is not None:
                results.append((page.rel_path, section, target, count))
    return results
