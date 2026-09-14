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
)
SPINE = (
    "At a Glance",
    "Connections",
    "Sheet",
    "Combat Profile",
    "Abilities",
    "Spells",
    "Inventory",
    "Session Log",
    "Art",
)
ABILITY_HEADINGS = ("Traits", "Features", "Actions", "Bonus Actions", "Reactions", "Feats")
SPELL_HEADINGS = ("Spellcasting", "Cantrips", "Prepared or Known", "Slots or Casting Resources")
INVENTORY_HEADINGS = ("Attuned", "Carried", "Stowed", "Currency")


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


def section(text: str, heading: str) -> str:
    body = body_without_comments(text)
    match = re.search(rf"^## {re.escape(heading)}\s*$", body, re.MULTILINE)
    if not match:
        return ""
    tail = body[match.end() :]
    next_heading = re.search(r"^## ", tail, re.MULTILINE)
    return tail[: next_heading.start() if next_heading else len(tail)]


def validate_columns(text: str, label: str, errors: list[str]) -> None:
    body = body_without_comments(text)
    if "[!col]" in body:
        fail(f"{label}: uses prohibited [!col] syntax", errors)
    lines = body.splitlines()
    parent_opens = [i for i, line in enumerate(lines) if line == "```col"]
    parent_closes = [i for i, line in enumerate(lines) if line == "```" and i > 0 and lines[i - 1] != "```col-md"]
    child_opens = [i for i, line in enumerate(lines) if line == "```col-md"]
    child_closes = [i for i, line in enumerate(lines) if line == "```" and i > 0 and lines[i - 1] != "```col"]
    if len(parent_opens) != 2:
        fail(f"{label}: expected two parent col fences, found {len(parent_opens)}", errors)
    if len(child_opens) != 4:
        fail(f"{label}: expected four child col-md fences, found {len(child_opens)}", errors)
    if "```col-md\n## At a Glance" not in body or "```col-md\n## Connections" not in body:
        fail(f"{label}: identity headings are not inside child columns", errors)
    if "```col-md\n## Sheet" not in body or "```col-md\n## Combat Profile" not in body:
        fail(f"{label}: mechanical headings are not inside child columns", errors)
    for open_index in parent_opens:
        close_index = next((i for i in range(open_index + 1, len(lines)) if lines[i] == "```"), None)
        if close_index is None:
            fail(f"{label}: unterminated parent col fence", errors)
            continue
        child_text = "\n".join(lines[open_index + 1 : close_index])
        if "```col-md" not in child_text:
            fail(f"{label}: parent col fence lacks nested col-md fences", errors)


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
    if not re.search(r"^# (?:\{\{title\}\}|[^#].+)$", clean, re.MULTILINE):
        fail(f"{label}: missing title H1", errors)
    if not template and len(headings(text, 1)) != 1:
        fail(f"{label}: expected exactly one H1", errors)
    if "> [!narration] Narration" not in clean:
        fail(f"{label}: missing player-safe Narration callout", errors)
    if re.search(r"^## Voice\s*$", clean, re.MULTILINE) or re.search(r"^# .*Voice", clean, re.MULTILINE):
        fail(f"{label}: contains obsolete Voice heading", errors)
    if "\\n" in clean:
        fail(f"{label}: contains literal escaped newline", errors)
    if not template:
        validate_columns(text, label, errors)
        if "## At a Glance" not in clean or "**DM thesis:**" not in clean:
            fail(f"{label}: missing At a Glance thesis", errors)
        if "**Player**" not in clean or "**Class / Level**" not in clean:
            fail(f"{label}: missing player or class identity", errors)
        if "## Sheet" not in clean or "| Ability | Score | Mod | Save |" not in clean:
            fail(f"{label}: missing canonical Sheet table", errors)
        if "| Combat skim | Value |" not in clean:
            fail(f"{label}: missing canonical combat skim", errors)
        for heading in ("Abilities", "Inventory"):
            if not section(text, heading).strip():
                fail(f"{label}: empty required section {heading}", errors)
        if "## Spells" not in clean and data.get("title") != "Delmar Fisk":
            fail(f"{label}: missing Spells despite castable-resource owner", errors)
        if "## Spells" in clean and data.get("title") == "Delmar Fisk":
            fail(f"{label}: non-caster retains Spells section", errors)
        if "|         |" in clean or "|      |" in clean:
            fail(f"{label}: contains an empty placeholder row", errors)
        for optional_heading in ("Connections", "Combat Profile", "Session Log", "Art"):
            if f"## {optional_heading}" in clean and not section(text, optional_heading).strip():
                fail(f"{label}: empty optional section {optional_heading}", errors)
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
