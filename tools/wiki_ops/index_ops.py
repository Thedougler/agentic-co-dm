"""Newline-safe structured operations for wiki/index.md."""
from __future__ import annotations

import re
from pathlib import Path

ENTRY_RE = re.compile(r"^-\s+\[\[([^\]|#]+)(?:\|[^\]]+)?\]\].*$")


def parse_index(text: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    seen: set[str] = set()
    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\r\n")
        match = ENTRY_RE.match(stripped)
        if match:
            slug = match.group(1).rsplit("/", 1)[-1]
            if slug.casefold() in seen:
                raise ValueError(f"malformed index: duplicate entry {slug}")
            seen.add(slug.casefold())
            rows.append((slug, line))
            continue
        if stripped.lstrip().startswith("-") and ("[[" in stripped or "[" in stripped):
            raise ValueError(f"malformed index entry: {stripped}")
    if text.strip() and not rows and "[[" in text:
        raise ValueError("malformed index: no parseable entries")
    return rows


def replace_index_entry(text: str, slug: str, new_entry: str) -> str:
    lines = text.splitlines(keepends=True)
    found = False
    for index, line in enumerate(lines):
        match = ENTRY_RE.match(line.rstrip("\r\n"))
        if match and match.group(1).rsplit("/", 1)[-1] == slug:
            newline = "\r\n" if line.endswith("\r\n") else "\n" if line.endswith("\n") else ""
            lines[index] = new_entry.rstrip("\r\n") + newline
            found = True
            break
    if not found:
        raise ValueError(f"index entry not found: {slug}")
    return "".join(lines)


def remove_index_entry(text: str, slug: str) -> str:
    lines = text.splitlines(keepends=True)
    kept = []
    removed = False
    for line in lines:
        match = ENTRY_RE.match(line.rstrip("\r\n"))
        if match and match.group(1).rsplit("/", 1)[-1] == slug:
            removed = True
            continue
        kept.append(line)
    if not removed:
        raise ValueError(f"index entry not found: {slug}")
    return "".join(kept)


def insert_index_entry(text: str, entry: str) -> str:
    lines = text.splitlines(keepends=True)
    new = entry.rstrip("\r\n") + ("\n" if "\r\n" not in text else "\r\n")
    match = ENTRY_RE.match(new.rstrip("\r\n"))
    if not match:
        raise ValueError("malformed index entry")
    slug = match.group(1).rsplit("/", 1)[-1]
    if any((m := ENTRY_RE.match(line.rstrip("\r\n"))) and m.group(1).rsplit("/", 1)[-1] == slug for line in lines):
        raise ValueError(f"index entry already exists: {slug}")
    parse_index(text)
    target_key = slug.casefold()
    insert_at = len(lines)
    for index, line in enumerate(lines):
        current = ENTRY_RE.match(line.rstrip("\r\n"))
        if current and current.group(1).rsplit("/", 1)[-1].casefold() > target_key:
            insert_at = index
            break
    lines.insert(insert_at, new)
    return "".join(lines)


def mutate_index(path: str | Path, operation: str, **kwargs: str) -> str:
    target = Path(path)
    text = target.read_text(encoding="utf-8")
    if operation == "replace":
        return replace_index_entry(text, kwargs["slug"], kwargs["new_entry"])
    if operation == "remove":
        return remove_index_entry(text, kwargs["slug"])
    if operation == "insert":
        return insert_index_entry(text, kwargs["entry"])
    raise ValueError(f"unknown index operation: {operation}")
