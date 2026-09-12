"""Materialisation phase of the vault organiser (ADR-0049).

Moves cluster members to <anchor_parent>/<anchor_slug>/<member_slug>.md
(the "folder note" pattern). The anchor itself stays in place. Idempotent:
a file already at its target is never re-moved.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from wiki_cli.organizer import ClusterResult

# Locations and factions carry implied ownership: nesting them under an NPC
# or event would invert the containment hierarchy the vault's folder model assumes.
_BLOCKED_UNDER: dict[str, frozenset[str]] = {
    "location": frozenset({"npc", "faction", "event", "quest"}),
    "faction": frozenset({"npc", "event", "quest"}),
}

_PATH_WIKILINK_RE = re.compile(
    r"(!?\[\[)"
    r"([^\]|#\n]+/[^\]|#\n]*)"
    r"([^\]]*?)"
    r"(\]\])"
)


@dataclass(frozen=True, slots=True)
class MoveOp:
    src: str
    dst: str


def _is_eligible(member_path: str, anchor_type: str | None, type_map: dict[str, str]) -> bool:
    """Return False when the member's type is blocked under anchor_type."""
    if anchor_type is None:
        return True
    member_type = type_map.get(member_path)
    if member_type is None:
        return True
    blocked = _BLOCKED_UNDER.get(member_type)
    if blocked is None:
        return True
    return anchor_type not in blocked


def compute_moves(
    result: ClusterResult,
    scope: str | None = None,
    type_map: dict[str, str] | None = None,
) -> list[MoveOp]:
    """Return move ops needed to materialise *result*.

    The anchor page stays in place; each non-anchor member moves to
    ``<anchor_parent>/<anchor_slug>/<member_slug>.md``.

    scope: if given, only clusters whose anchor path starts with this
    prefix, or whose anchor slug equals this value, are processed.
    type_map: optional mapping of rel_path -> page type from the pages table.
    When provided, members whose type is ineligible to nest under the anchor's
    type are skipped (no MoveOp generated).
    """
    moves: list[MoveOp] = []

    for cluster in result.clusters:
        anchor_path = next(
            (m for m in cluster.members if Path(m).stem == cluster.anchor),
            None,
        )
        if anchor_path is None:
            continue

        if scope and not anchor_path.startswith(scope) and cluster.anchor != scope:
            continue

        anchor_parent = Path(anchor_path).parent
        anchor_slug = cluster.anchor
        anchor_type = type_map.get(anchor_path) if type_map else None

        for member in cluster.members:
            if Path(member).stem == anchor_slug:
                continue
            if type_map is not None and not _is_eligible(member, anchor_type, type_map):
                continue
            member_slug = Path(member).stem
            dst = str(anchor_parent / anchor_slug / f"{member_slug}.md")
            if member != dst:
                moves.append(MoveOp(src=member, dst=dst))

    return moves


def apply_moves(moves: list[MoveOp], repo_root: Path) -> None:
    """Move files to target paths and scrub path wikilinks in moved files."""
    for op in moves:
        src = repo_root / op.src
        dst = repo_root / op.dst
        if not src.exists():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        src.rename(dst)

    for op in moves:
        dst_path = repo_root / op.dst
        if dst_path.exists():
            _scrub_path_wikilinks(dst_path)


def _scrub_path_wikilinks(path: Path) -> None:
    """Rewrite path-qualified wikilinks to slug-only in-place."""
    original = path.read_text(encoding="utf-8")
    rewritten = _PATH_WIKILINK_RE.sub(
        lambda m: f"{m.group(1)}{Path(m.group(2).strip()).stem}{m.group(3)}{m.group(4)}",
        original,
    )
    if rewritten != original:
        path.write_text(rewritten, encoding="utf-8")
