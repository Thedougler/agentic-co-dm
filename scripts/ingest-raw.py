#!/usr/bin/env python3
"""Promote named wiki/_raw campaign drops without improvising the bookkeeping.

Examples:
  python3 scripts/ingest-raw.py wiki/_raw/source.md
  python3 scripts/ingest-raw.py wiki/_raw/one.md wiki/_raw/two.md --wiki wiki --skip-qmd
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import shutil
import subprocess
from datetime import date
from pathlib import Path


def frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    _, raw, body = text.split("---\n", 2)
    fields: dict[str, str] = {}
    for line in raw.splitlines():
        if ":" in line and not line.startswith(" "):
            key, value = line.split(":", 1)
            fields[key] = value.strip().strip('"')
    return fields, body.lstrip("\n")


def title_from(path: Path, fields: dict[str, str], body: str) -> str:
    if fields.get("title"):
        return fields["title"]
    match = re.search(r"^#\s+(.+)$", body, re.MULTILINE)
    return match.group(1).strip() if match else path.stem


def yaml_list(value: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9_-]*", value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("sources", nargs="+", type=Path)
    parser.add_argument("--wiki", type=Path, default=Path("wiki"))
    parser.add_argument("--skip-qmd", action="store_true")
    args = parser.parse_args()
    wiki = args.wiki.resolve()
    today = date.today().isoformat()
    manifest_path = wiki / ".manifest.json"
    manifest = json.loads(manifest_path.read_text())
    produced: list[tuple[Path, str]] = []
    archive = wiki / "_archive"  # vault archive only — no repo-root _archive
    archive.mkdir(exist_ok=True)

    for source_arg in args.sources:
        source = source_arg.resolve()
        if not source.is_file() or source.parent != wiki / "_raw":
            raise SystemExit(f"source must be a file directly inside {wiki / '_raw'}: {source}")
        fields, body = frontmatter(source.read_text())
        title = title_from(source, fields, body)
        kind = {"location": "place", "monster": "creature", "lore": "item"}.get(
            fields.get("type", ""), fields.get("type", "place")
        )
        if kind not in {"place", "creature", "item", "npc", "faction"}:
            raise SystemExit(f"unsupported campaign type {kind!r} in {source}")
        tags = yaml_list(fields.get("tags", "")) or ["shattered-sea", "aruhe"]
        if "shattered-sea" not in tags:
            tags.insert(0, "shattered-sea")
        if "aruhe" not in tags:
            tags.append("aruhe")
        summary = fields.get("summary", "")
        target = wiki / "entities" / source.name
        lines = [
            "---", f"title: {title}", "category: entities",
            f"tags: [{', '.join(tags)}]", f"sources: [\"{source.name}\"]",
            f"created: {today}", f"updated: {today}", f"type: {kind}",
            "reveal: unrevealed", "campaign: shattered-sea",
            f"visibility: {fields.get('visibility', 'dm')}", f"summary: {summary}", "---", "",
        ]
        target.write_text("\n".join(lines) + body)
        rel = str(target.relative_to(wiki))
        manifest[str(source)] = {
            "content_hash": "sha256:" + hashlib.sha256(source.read_bytes()).hexdigest(),
            "last_ingested": f"{today}T00:00:00Z", "pages_produced": [rel],
            "pages_created": [rel], "pages_updated": [], "source_type": "document",
            "project": fields.get("campaign", "shattered-sea"),
        }
        destination = archive / source.name
        if destination.exists():
            destination = archive / f"{source.stem} (2){source.suffix}"
        shutil.move(source, destination)
        produced.append((source, rel))

    stats = manifest.setdefault("stats", {})
    stats["total_sources_ingested"] = stats.get("total_sources_ingested", 0) + len(produced)
    stats["total_pages"] = stats.get("total_pages", 0) + len(produced)
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n")
    index = wiki / "index.md"
    index.write_text(index.read_text().replace("## Entities\n", "## Entities\n" + "".join(
        f"- [[{Path(rel).stem}]] — Ingested campaign entity.\n" for _, rel in produced
    ), 1))
    log = wiki / "log.md"
    with log.open("a") as handle:
        for source, _ in produced:
            handle.write(f'\n- [{today}T00:00:00Z] INGEST source="{source}" pages_updated=0 pages_created=1 mode=append\n')
    (wiki / "hot.md").write_text(
        f"---\ntitle: Hot Cache\nupdated: {today}\n---\n## Recent Activity\n"
        f"Ingested {len(produced)} campaign raw page(s).\n## Active Threads\n## Key Takeaways\n## Flagged Contradictions\n"
    )
    if not args.skip_qmd:
        subprocess.run(["scripts/qmd-maintain.sh"], cwd=wiki.parent, check=True)
    print(f"filed {len(produced)} page(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
