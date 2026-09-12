#!/usr/bin/env python3
"""Fail if campaign wiki pages or the ingest manifest are missing required fields."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "wiki"
SKIP_DIRS = {".obsidian", "_raw", "_archive", "_meta", "templates"}
SKIP_FILES = {"AGENTS.md", "index.md", "log.md", "hot.md"}
TYPES = {"npc", "place", "faction", "item", "creature", "session", "recap", "work"}
LIFECYCLES = {"draft", "proposed", "accepted", "rejected", "canon"}
REVEALS = {"unrevealed", "revealed"}
REQUIRED = (
    "title",
    "category",
    "tags",
    "sources",
    "created",
    "updated",
    "type",
    "lifecycle",
    "reveal",
)


def frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    keys: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if ":" not in line or line.startswith(" ") or line.startswith("-"):
            continue
        key, _, value = line.partition(":")
        keys[key.strip()] = value.strip()
    return keys


def check_pages() -> list[str]:
    errors: list[str] = []
    pages = 0
    for path in sorted(VAULT.rglob("*.md")):
        rel = path.relative_to(VAULT)
        if rel.parts[0] in SKIP_DIRS or path.name in SKIP_FILES:
            continue
        pages += 1
        keys = frontmatter(path.read_text(encoding="utf-8"))
        if keys is None:
            errors.append(f"{rel}: missing YAML frontmatter")
            continue
        for field in REQUIRED:
            if field not in keys:
                errors.append(f"{rel}: missing {field}")
        kind = keys.get("type", "").strip().strip('"')
        life = keys.get("lifecycle", "").strip().strip('"')
        reveal = keys.get("reveal", "").strip().strip('"')
        if kind and kind not in TYPES:
            errors.append(f"{rel}: bad type {kind!r}")
        if life and life not in LIFECYCLES:
            errors.append(f"{rel}: bad lifecycle {life!r}")
        if reveal and reveal not in REVEALS:
            errors.append(f"{rel}: bad reveal {reveal!r}")
    if pages == 0:
        errors.append("no campaign pages under wiki/")
    return errors


def check_manifest() -> list[str]:
    errors: list[str] = []
    manifest_path = VAULT / ".manifest.json"
    if not manifest_path.exists():
        return ["wiki/.manifest.json missing"]
    data = json.loads(manifest_path.read_text(encoding="utf-8"))
    sources = {k: v for k, v in data.items() if k not in {"version", "stats"} and isinstance(v, dict)}
    if not sources:
        errors.append("manifest has no source entries")
    for source, meta in sources.items():
        if not Path(source).is_file():
            errors.append(f"manifest source missing on disk: {source}")
        digest = meta.get("content_hash", "")
        if not isinstance(digest, str) or not digest.startswith("sha256:") or len(digest) != 71:
            errors.append(f"{source}: bad content_hash")
        pages = meta.get("pages_produced")
        if not pages:
            errors.append(f"{source}: empty pages_produced")
        else:
            for page in pages:
                if not (VAULT / page).is_file():
                    errors.append(f"{source}: missing page {page}")
    index = (VAULT / "index.md").read_text(encoding="utf-8")
    log = (VAULT / "log.md").read_text(encoding="utf-8")
    if "INGEST" not in log:
        errors.append("wiki/log.md has no INGEST line")
    if "Session 01 - Recap" not in index:
        errors.append("wiki/index.md missing Session 01 - Recap")
    return errors


def main() -> int:
    errors = check_pages() + check_manifest()
    if errors:
        print("check_wiki_pages: FAIL")
        for err in errors:
            print(f"  {err}")
        return 1
    print("check_wiki_pages: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
