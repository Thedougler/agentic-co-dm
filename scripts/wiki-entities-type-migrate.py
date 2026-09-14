#!/usr/bin/env python3
"""Migrate flat wiki/entities/{Name}.md into depth-1 type folders.

Formula (ASE wiki-entities-type-migrate, depth 1):
  Live owner pages: wiki/entities/{name}.md -> wiki/entities/{type}/{name}.md
  from frontmatter `type`. category stays `entities`.

  Allowed entity types: npc, pc, place, faction, item, creature, vehicle,
  spell, lore, quest, region, work.

  Redirects: if page has redirects_to and the target has a typed live page,
  dest is that type folder; else wiki/entities/_redirects/{name}.md.

  Journal types session-prep|session|recap -> journal homes, NOT entities/{type}/.
  Session-prep dest: wiki/journal/sessions/<campaign-slug>/<session-number>/
  keeping filename when known from FM or filename; else needs_journal_home
  (do not invent a folder on apply).

  Skip _archive, _raw, attachments. Depth <= 1. No synonym/rarity/facet dirs.

Usage:
  python3 scripts/wiki-entities-type-migrate.py --dry-run [--wiki wiki]
  python3 scripts/wiki-entities-type-migrate.py --apply [--wiki wiki]

Dry-run always exits 0 (even with needs_journal_home). Apply exits nonzero
on collisions or refused moves. Idempotent: second dry-run is empty after apply.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from dataclasses import asdict, dataclass
from pathlib import Path

ALLOWED_ENTITY_TYPES = frozenset(
    {
        "npc",
        "pc",
        "place",
        "faction",
        "item",
        "creature",
        "vehicle",
        "spell",
        "lore",
        "quest",
        "region",
        "work",
    }
)
JOURNAL_TYPES = frozenset({"session-prep", "session", "recap"})
SKIP_DIR_NAMES = frozenset({"_archive", "_raw", "attachments"})

FM_BLOCK = re.compile(r"\A---\n(.*?)\n---\n?", re.DOTALL)
FM_TYPE = re.compile(r"^type:\s*[\"']?([^\"'\n#]+)", re.MULTILINE)
FM_REDIRECTS = re.compile(r"^redirects_to:\s*[\"']?(.+?)[\"']?\s*$", re.MULTILINE)
FM_CAMPAIGN = re.compile(r"^campaign:\s*[\"']?([^\"'\n#]+)", re.MULTILINE)
FM_SESSION = re.compile(
    r"^(?:session(?:[_-]?number)?|session_num):\s*[\"']?([^\"'\n#]+)",
    re.MULTILINE | re.IGNORECASE,
)
# Session-<n>-... or ...-Session-<n>...
FILENAME_SESSION = re.compile(r"(?i)(?:^|[^\w])Session-(\d+)(?:-|$)")
WIKILINK_TARGET = re.compile(r"^\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]$")
# Path-qualified embeds/links that point at flat entities/Name(.md)
PATH_LINK = re.compile(
    r"(!?\[\[)"
    r"(?:wiki/)?"
    r"(entities/([^\]|#/]+?)(?:\.md)?)"
    r"((?:#[^\]|]*)?(?:\|[^\]]*)?\]\])"
)


@dataclass
class Move:
    src: str
    dest: str | None
    type: str | None
    reason: str


def parse_frontmatter(text: str) -> str:
    m = FM_BLOCK.match(text)
    return m.group(1) if m else ""


def fm_field(fm: str, pattern: re.Pattern[str]) -> str | None:
    m = pattern.search(fm)
    if not m:
        return None
    return m.group(1).strip().strip("\"'")


def parse_redirect_target(raw: str) -> str | None:
    raw = raw.strip().strip("\"'")
    m = WIKILINK_TARGET.match(raw)
    if m:
        return m.group(1).strip()
    if raw.startswith("[[") and raw.endswith("]]"):
        inner = raw[2:-2]
        return inner.split("|", 1)[0].split("#", 1)[0].strip()
    if raw:
        return raw
    return None


def session_number_from(path: Path, fm: str) -> str | None:
    raw = fm_field(fm, FM_SESSION)
    if raw:
        digits = re.search(r"\d+", raw)
        if digits:
            return str(int(digits.group(0)))
    m = FILENAME_SESSION.search(path.name)
    if m:
        return str(int(m.group(1)))
    return None


def campaign_slug_from(fm: str) -> str | None:
    raw = fm_field(fm, FM_CAMPAIGN)
    if not raw:
        return None
    slug = raw.strip().lower().replace("_", "-").replace(" ", "-")
    return slug or None


def rel_posix(wiki: Path, path: Path) -> str:
    return path.resolve().relative_to(wiki.resolve()).as_posix()


def build_type_index(entities: Path) -> dict[str, str]:
    """Map page stem / title basename -> allowed type for live pages.

    Prefers typed folders; also indexes flat files that have an allowed type.
    Redirect stubs (redirects_to) are not indexed as typed targets.
    """
    index: dict[str, str] = {}
    if not entities.is_dir():
        return index

    for typed_dir in sorted(entities.iterdir()):
        if not typed_dir.is_dir():
            continue
        if typed_dir.name.startswith("_") or typed_dir.name in SKIP_DIR_NAMES:
            continue
        if typed_dir.name not in ALLOWED_ENTITY_TYPES:
            continue
        for page in typed_dir.glob("*.md"):
            index[page.stem] = typed_dir.name

    for page in entities.glob("*.md"):
        text = page.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        if fm_field(fm, FM_REDIRECTS):
            continue
        t = fm_field(fm, FM_TYPE)
        if t in ALLOWED_ENTITY_TYPES:
            index.setdefault(page.stem, t)
    return index


def plan_moves(wiki: Path) -> list[Move]:
    entities = wiki / "entities"
    if not entities.is_dir():
        return []

    type_index = build_type_index(entities)
    moves: list[Move] = []

    for src in sorted(entities.glob("*.md"), key=lambda p: p.name.lower()):
        # Only flat depth-0 owners; skip anything already nested.
        text = src.read_text(encoding="utf-8", errors="replace")
        fm = parse_frontmatter(text)
        page_type = fm_field(fm, FM_TYPE)
        redirects_raw = fm_field(fm, FM_REDIRECTS)
        src_rel = rel_posix(wiki, src)

        if redirects_raw is not None:
            target_name = parse_redirect_target(redirects_raw)
            target_type = type_index.get(target_name) if target_name else None
            if target_type in ALLOWED_ENTITY_TYPES:
                dest = entities / target_type / src.name
                moves.append(
                    Move(
                        src=src_rel,
                        dest=rel_posix(wiki, dest),
                        type=target_type,
                        reason="redirect_typed_target",
                    )
                )
            else:
                dest = entities / "_redirects" / src.name
                moves.append(
                    Move(
                        src=src_rel,
                        dest=rel_posix(wiki, dest),
                        type=None,
                        reason="redirect_typeless",
                    )
                )
            continue

        if page_type in JOURNAL_TYPES:
            campaign = campaign_slug_from(fm)
            session = session_number_from(src, fm)
            if campaign and session:
                dest = (
                    wiki
                    / "journal"
                    / "sessions"
                    / campaign
                    / session
                    / src.name
                )
                moves.append(
                    Move(
                        src=src_rel,
                        dest=rel_posix(wiki, dest),
                        type=page_type,
                        reason="journal_home",
                    )
                )
            else:
                moves.append(
                    Move(
                        src=src_rel,
                        dest=None,
                        type=page_type,
                        reason="needs_journal_home",
                    )
                )
            continue

        if page_type in ALLOWED_ENTITY_TYPES:
            dest = entities / page_type / src.name
            moves.append(
                Move(
                    src=src_rel,
                    dest=rel_posix(wiki, dest),
                    type=page_type,
                    reason="type_folder",
                )
            )
            continue

        moves.append(
            Move(
                src=src_rel,
                dest=None,
                type=page_type,
                reason="untyped_or_disallowed",
            )
        )

    return moves


def counts_for(moves: list[Move]) -> dict[str, int]:
    c: Counter[str] = Counter()
    for m in moves:
        if m.reason == "type_folder" and m.type:
            c[f"type:{m.type}"] += 1
        elif m.reason == "redirect_typed_target":
            c["redirect_typed_target"] += 1
            if m.type:
                c[f"type:{m.type}"] += 1  # also lands in that folder
        elif m.reason == "redirect_typeless":
            c["redirect_typeless"] += 1
        elif m.reason == "journal_home":
            c["journal_home"] += 1
        elif m.reason == "needs_journal_home":
            c["needs_journal_home"] += 1
        elif m.reason == "untyped_or_disallowed":
            c["untyped_or_disallowed"] += 1
        else:
            c[m.reason] += 1
    c["total"] = len(moves)
    c["actionable"] = sum(1 for m in moves if m.dest)
    return dict(c)


def git_aware_rename(src: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            ["git", "mv", "--", str(src), str(dest)],
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        src.replace(dest)


def rewrite_path_links(wiki: Path, old_to_new: dict[str, str]) -> int:
    """Rewrite path-qualified [[entities/Name]] / embeds to new typed paths.

    Title-only [[Name]] left alone. Returns number of files changed.
    """
    if not old_to_new:
        return 0

    # Map stem -> new entities-relative path without .md
    stem_to_new: dict[str, str] = {}
    for old_rel, new_rel in old_to_new.items():
        # old_rel like entities/Foo.md
        old_path = Path(old_rel)
        if old_path.suffix == ".md" and old_path.parts[:1] == ("entities",):
            new_no_md = new_rel[:-3] if new_rel.endswith(".md") else new_rel
            stem_to_new[old_path.stem] = new_no_md

    if not stem_to_new:
        return 0

    changed_files = 0
    for path in sorted(wiki.rglob("*.md")):
        if any(part in SKIP_DIR_NAMES for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")

        def repl(match: re.Match[str]) -> str:
            prefix, _full_old, stem, suffix = match.groups()
            new_rel = stem_to_new.get(stem)
            if not new_rel:
                return match.group(0)
            return f"{prefix}{new_rel}{suffix}"

        new_text, n = PATH_LINK.subn(repl, text)
        if n:
            path.write_text(new_text, encoding="utf-8")
            changed_files += 1
    return changed_files


def apply_moves(wiki: Path, moves: list[Move]) -> tuple[list[dict], list[str]]:
    """Apply actionable moves. Returns (applied records, error messages)."""
    errors: list[str] = []
    applied: list[dict] = []
    old_to_new: dict[str, str] = {}

    # Collision / existence checks first (atomic refuse).
    for m in moves:
        if not m.dest:
            continue
        dest = wiki / m.dest
        if dest.exists():
            errors.append(f"collision: dest exists: {m.dest} (from {m.src})")

    if errors:
        return [], errors

    for m in moves:
        if not m.dest:
            continue
        src = wiki / m.src
        dest = wiki / m.dest
        if not src.is_file():
            errors.append(f"missing source: {m.src}")
            continue
        git_aware_rename(src, dest)
        old_to_new[m.src] = m.dest
        applied.append(asdict(m))

    if errors:
        return applied, errors

    rewrite_path_links(wiki, old_to_new)
    return applied, []


def emit_report(moves: list[Move], mode: str) -> None:
    payload = {
        "mode": mode,
        "moves": [asdict(m) for m in moves],
        "counts": counts_for(moves),
    }
    print(json.dumps(payload, indent=2, sort_keys=False))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--dry-run",
        action="store_true",
        help="Plan moves and print JSON; exit 0 even with needs_journal_home",
    )
    mode.add_argument(
        "--apply",
        action="store_true",
        help="mkdir + git-aware rename + rewrite path-qualified entity links",
    )
    parser.add_argument(
        "--wiki",
        type=Path,
        default=Path("wiki"),
        help="Wiki root (default: ./wiki)",
    )
    args = parser.parse_args()
    wiki = args.wiki.resolve()
    if not wiki.is_dir():
        print(f"wiki root not found: {wiki}", file=sys.stderr)
        return 2

    moves = plan_moves(wiki)

    if args.dry_run:
        emit_report(moves, "dry-run")
        return 0

    # --apply
    collisions = [m for m in moves if m.dest and (wiki / m.dest).exists()]
    if collisions:
        emit_report(moves, "apply-refused-collision")
        for m in collisions:
            print(f"collision: {m.src} -> {m.dest}", file=sys.stderr)
        return 1

    applied, errors = apply_moves(wiki, moves)
    report_moves = [
        Move(**row) if isinstance(row, dict) else row for row in applied
    ]
    # Include non-applied needs_journal_home / untyped in report for visibility
    skipped = [m for m in moves if not m.dest]
    emit_report(report_moves + skipped, "apply")
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
