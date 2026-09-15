#!/usr/bin/env python3
"""Validate the PC owner-page shape for feature 020."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
TEMPLATE = ROOT / "wiki/templates/pc.md"
PC_DIR = ROOT / "wiki/entities/pc"
ARCHIVE_DIR = ROOT / "wiki/_archive"
OWNERS = (
    "jean-claude-tabarnack.md",
    "perrin-black-jaw.md",
    "catarina-davirelli.md",
    "crissdalynn-khinriss.md",
    "delmar-fisk.md",
)
REQUIRED_FRONTMATTER = (
    "title",
    "category",
    "tags",
    "sources",
    "created",
    "updated",
    "type",
    "lifecycle",
    "reveal",
    "campaign",
    "visibility",
    "summary",
    "player",
    "class_levels",
    "level",
    "ac",
    "hp_max",
    "init_mod",
    "pp",
    "speed",
    "cssclasses",
)
SPINE = (
    "Identity",
    "Combat Stats",
    "Ability Scores",
    "Skills",
    "Actions",
    "Spells",
    "Inventory",
    "Features",
    "Connections",
    "Stated Goals",
    "Session Log",
    "Art",
)
REQUIRED_H2 = (
    "Identity",
    "Combat Stats",
    "Ability Scores",
    "Skills",
    "Actions",
    "Inventory",
    "Features",
)
FORBIDDEN_H2 = (
    "Voice",
    "At a Glance",
    "Sheet",
    "Combat Profile",
    "Abilities",
)
ABILITY_PAIR = ("Ability Scores", "Skills")
EMBED = re.compile(r"!\[\[[^\]]+\]\]|!\[[^\]]*\]\([^)]+\)")
ACTION_SUBHEADINGS = ("Attacks", "Actions", "Bonus Actions", "Reactions")
FEATURE_SUBHEADINGS = ("Traits", "Class Features", "Feats")
SPELL_SUBHEADINGS = ("Spellcasting", "Cantrips", "Prepared or Known", "Slots or Casting Resources")
INVENTORY_SUBHEADINGS = ("Attuned", "Carried", "Stowed", "Currency")
FENCE_OPEN = re.compile(r"^(?P<ticks>`{3,})(?P<info>\S.*)?\s*$")
FENCE_CLOSE = re.compile(r"^(`{3,})\s*$")


def fail(message: str, errors: list[str]) -> None:
    errors.append(message)


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        return {}
    values: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip()
    return values


def body_without_comments(text: str) -> str:
    return re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)


def headings(text: str, level: int) -> list[str]:
    prefix = "#" * level + " "
    return [line[len(prefix) :].strip() for line in body_without_comments(text).splitlines() if line.startswith(prefix)]


def section(text: str, heading: str, level: int = 2) -> str:
    body = body_without_comments(text)
    marks = "#" * level
    match = re.search(rf"^{marks} {re.escape(heading)}\s*$", body, re.MULTILINE)
    if not match:
        return ""
    tail = body[match.end() :]
    next_heading = re.search(rf"^{marks} ", tail, re.MULTILINE)
    return tail[: next_heading.start() if next_heading else len(tail)]


def nonempty_body(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    rows = [line for line in stripped.splitlines() if line.strip().startswith("|") and not re.match(r"^\|\s*-+", line.strip())]
    if rows and all(re.match(r"^\|(?:\s*\|)+\s*$", row.replace("---", "").replace(":", "")) or re.search(r"\|\s+\|", row) and not re.search(r"\|\s*\S", row[row.find("|") + 1 :]) for row in rows[1:] or rows):
        data_rows = rows[1:] if len(rows) > 1 else []
        if data_rows and all(not re.search(r"[A-Za-z0-9\[\]]", row) for row in data_rows):
            return False
    return True


def parse_fences(text: str) -> list[tuple[int, str, str]]:
    """Return (tick_count, info, inner) for each fence, outermost first via nested scan."""
    lines = text.splitlines()
    found: list[tuple[int, str, str]] = []

    def walk(start: int, end: int, min_close: int) -> int:
        i = start
        while i < end:
            open_match = FENCE_OPEN.match(lines[i] or "")
            if not open_match or FENCE_CLOSE.match(lines[i] or "") and not (open_match.group("info") or "").strip():
                i += 1
                continue
            info = (open_match.group("info") or "").strip()
            ticks = len(open_match.group("ticks"))
            if ticks < min_close:
                i += 1
                continue
            j = i + 1
            close_at = None
            while j < end:
                close_match = FENCE_CLOSE.match(lines[j] or "")
                if close_match and len(close_match.group(1)) >= ticks:
                    close_at = j
                    break
                j += 1
            if close_at is None:
                found.append((ticks, info, "\n".join(lines[i + 1 : end])))
                return end
            inner = "\n".join(lines[i + 1 : close_at])
            found.append((ticks, info, inner))
            walk(i + 1, close_at, ticks + 1)
            i = close_at + 1
        return i

    walk(0, len(lines), 3)
    return found


def col_parents(text: str) -> list[tuple[int, str]]:
    return [(ticks, inner) for ticks, info, inner in parse_fences(text) if info.split()[0] == "col" if info]


def col_children(inner: str) -> list[tuple[int, str]]:
    return [(ticks, body) for ticks, info, body in parse_fences(inner) if info.split()[0] == "col-md" if info]


def child_h2(body: str) -> list[str]:
    return [line[3:].strip() for line in body.splitlines() if line.startswith("## ")]


def heading_in_columns(parents: list[tuple[int, str]], heading: str) -> bool:
    for _, inner in parents:
        for _, child_body in col_children(inner):
            if heading in child_h2(child_body):
                return True
    return False


def validate_columns(text: str, label: str, errors: list[str]) -> None:
    body = body_without_comments(text)
    if "[!col]" in body:
        fail(f"{label}: uses prohibited [!col] syntax", errors)
    parents = col_parents(body)
    pair_headings: list[set[str]] = []
    portrait_pair = False
    for parent_ticks, inner in parents:
        children = col_children(inner)
        if len(children) != 2:
            fail(f"{label}: parent col fence lacks two nested col-md fences", errors)
            continue
        _left_ticks, left_body = children[0]
        _right_ticks, right_body = children[1]
        for child_ticks, _child_body in children:
            if parent_ticks <= child_ticks:
                fail(f"{label}: parent col fence is not longer than child col-md fences", errors)
        left_h2 = child_h2(left_body)
        right_h2 = child_h2(right_body)
        names = set(left_h2 + right_h2)
        pair_headings.append(names)
        if "Identity" in names and "Combat Stats" in names:
            fail(f"{label}: pairs Identity with Combat Stats", errors)
        if "Connections" in names and "Session Log" in names:
            fail(f"{label}: pairs Connections with Session Log", errors)
        if right_h2 == ["Identity"] and not left_h2:
            if EMBED.search(left_body):
                portrait_pair = True
            else:
                fail(f"{label}: empty portrait column", errors)
    if set(ABILITY_PAIR) not in pair_headings:
        fail(f"{label}: missing nested pair {sorted(ABILITY_PAIR)}", errors)
    if heading_in_columns(parents, "Combat Stats"):
        fail(f"{label}: Combat Stats is not full-width", errors)
    if EMBED.search(body):
        if not portrait_pair:
            fail(f"{label}: missing featured portrait + Identity pair", errors)
    elif heading_in_columns(parents, "Identity"):
        fail(f"{label}: Identity is not full-width when no pictures exist", errors)
    first_parent_at = body.find("````col")
    narration_at = body.find("> [!narration] Narration")
    if first_parent_at != -1 and narration_at != -1 and narration_at > first_parent_at:
        fail(f"{label}: Narration callout is inside column fences", errors)


def validate_spine(text: str, label: str, errors: list[str], *, title: str, template: bool) -> None:
    h2 = headings(text, 2)
    for forbidden in FORBIDDEN_H2:
        if forbidden in h2:
            fail(f"{label}: contains obsolete {forbidden} heading", errors)
    present = [name for name in h2 if name in SPINE]
    expected = [name for name in SPINE if name in h2]
    if present != expected:
        fail(f"{label}: D&D Beyond spine order is {present}", errors)
    for name in REQUIRED_H2:
        if name not in h2:
            fail(f"{label}: missing required heading {name}", errors)
    if title == "Delmar Fisk" and "Spells" in h2:
        fail(f"{label}: non-caster retains Spells section", errors)
    if not template:
        for name in ("Spells", "Connections", "Stated Goals", "Session Log", "Art"):
            if name in h2 and not nonempty_body(section(text, name)):
                fail(f"{label}: empty optional section {name}", errors)
        for heading, subs in (
            ("Actions", ACTION_SUBHEADINGS),
            ("Features", FEATURE_SUBHEADINGS),
            ("Spells", SPELL_SUBHEADINGS),
            ("Inventory", INVENTORY_SUBHEADINGS),
        ):
            if heading not in h2:
                continue
            body = section(text, heading)
            for sub in subs:
                if re.search(rf"^### {re.escape(sub)}\s*$", body, re.MULTILINE) and not nonempty_body(section(body, sub, 3)):
                    fail(f"{label}: empty optional subsection {sub}", errors)


def validate_page(path: Path, errors: list[str], template: bool = False) -> None:
    label = str(path.relative_to(ROOT))
    text = path.read_text()
    clean = body_without_comments(text)
    data = frontmatter(text)
    if not data:
        fail(f"{label}: missing frontmatter", errors)
    for key in REQUIRED_FRONTMATTER:
        if key not in data:
            fail(f"{label}: missing frontmatter key {key}", errors)
    if data.get("type") != "pc":
        fail(f"{label}: type must be pc", errors)
    if "pc-sheet" not in data.get("cssclasses", ""):
        fail(f"{label}: cssclasses must include pc-sheet", errors)
    if not re.search(r"^# (?:\{\{title\}\}|[^#].+)$", clean, re.MULTILINE):
        fail(f"{label}: missing title H1", errors)
    if not template and len(headings(text, 1)) != 1:
        fail(f"{label}: expected exactly one H1", errors)
    if "> [!narration] Narration" not in clean:
        fail(f"{label}: missing player-safe Narration callout", errors)
    if re.search(r"DM thesis", clean, re.IGNORECASE):
        fail(f"{label}: contains required DM thesis", errors)
    if "\\n" in clean:
        fail(f"{label}: contains literal escaped newline", errors)
    validate_spine(text, label, errors, title=data.get("title", ""), template=template)
    validate_columns(text, label, errors)
    if not template:
        identity = section(text, "Identity")
        combat = section(text, "Combat Stats")
        if "Player" not in identity or "Class" not in identity:
            fail(f"{label}: missing player or class identity", errors)
        for needle in ("AC", "HP", "Initiative"):
            if needle not in combat:
                fail(f"{label}: Combat Stats missing {needle}", errors)
        if "| Ability | Score | Mod | Save |" not in clean:
            fail(f"{label}: missing Ability Scores table", errors)
        if "|         |" in clean or "|      |" in clean:
            fail(f"{label}: contains an empty placeholder row", errors)
        owner_slug = re.sub(r"[^a-z0-9-]", "", data.get("title", "").lower().replace(" ", "-").replace("'", ""))
        if owner_slug and f"wiki/_archive/{owner_slug}.md" not in text:
            fail(f"{label}: source lineage does not name the owner archive", errors)


def main() -> int:
    errors: list[str] = []
    if not TEMPLATE.is_file():
        fail(f"missing template: {TEMPLATE}", errors)
    else:
        validate_page(TEMPLATE, errors, template=True)
    actual = sorted(path.name for path in PC_DIR.glob("*.md")) if PC_DIR.is_dir() else []
    if actual != sorted(OWNERS):
        fail(f"live PC owner set differs: expected {sorted(OWNERS)}, found {actual}", errors)
    for owner in OWNERS:
        path = PC_DIR / owner
        if path.is_file():
            validate_page(path, errors)
        else:
            fail(f"missing owner page: {path}", errors)
    if ARCHIVE_DIR.is_dir():
        for path in PC_DIR.glob("*-abilities.md"):
            fail(f"live satellite duplicate: {path}", errors)
    result = {"feature": "020-pc-page-redesign", "checked": len(OWNERS) + 1, "errors": errors}
    if "--json" in sys.argv[1:]:
        print(json.dumps(result, indent=2))
    elif errors:
        print("PC contract: FAIL")
        print("\n".join(f"- {error}" for error in errors))
    else:
        print(f"PC contract: PASS ({result['checked']} files)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
