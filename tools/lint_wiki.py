#!/usr/bin/env python3
"""Run deterministic health checks against the active portion of an Obsidian vault.

The bundled CLI currently scans archived copies and treats Obsidian aliases as
broken links. This tool keeps the lint scope explicit and resolves links by
path, filename, title, or alias without requiring third-party packages.
"""
from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import re
from pathlib import Path
from typing import Any
DEFAULT_LIFECYCLES = {"draft", "reviewed", "verified", "disputed", "archived"}
DEFAULT_RELATIONSHIPS = {
    "extends", "implements", "contradicts", "derived_from", "uses", "replaces", "related_to"
}
REQUIRED = ("title", "category", "tags", "sources", "created", "updated")
CAMPAIGN_REQUIRED = ("type", "lifecycle", "reveal")
CAMPAIGN_TYPES = {
    "npc", "place", "faction", "item", "creature", "vehicle", "spell",
    "session-prep", "session", "recap", "work",
}
RESERVED_FILES = {"AGENTS.md", "index.md", "log.md", "hot.md"}
SKIP_DIRS = {".obsidian", "_archive", "_archives", "_raw", "_readouts", "_meta", "templates"}


def frontmatter(text: str) -> tuple[str | None, dict[str, str]]:
    if not text.startswith("---\n"):
        return None, {}
    match = re.search(r"\n---\s*(?:\n|$)", text[4:])
    if not match:
        return None, {}
    end = 4 + match.start()
    block = text[4:end]
    fields: dict[str, str] = {}
    for line in block.splitlines():
        item = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if item and not line.startswith((" ", "-")):
            fields[item.group(1)] = item.group(2).strip()
    return block, fields


def scalar_list(block: str, key: str) -> list[str]:
    inline = re.search(rf"^{re.escape(key)}:\s*\[(.*?)\]\s*$", block, re.M)
    if inline:
        return [x.strip().strip("\"'") for x in inline.group(1).split(",") if x.strip()]
    match = re.search(rf"^{re.escape(key)}:\s*$([\s\S]*?)(?=^\w[\w-]*:|\Z)", block, re.M)
    if not match:
        return []
    return [m.group(1).strip().strip("\"'") for m in re.finditer(r"^\s*-\s+(.+)$", match.group(1), re.M)]


def normalize(value: str) -> str:
    value = value.split("#", 1)[0].strip().replace("\\", "/")
    value = re.sub(r"\.md$", "", value, flags=re.I)
    return value.casefold()


def load(vault: Path) -> tuple[dict[str, dict], dict[str, list[str]]]:
    pages: dict[str, dict] = {}
    lookup: dict[str, list[str]] = collections.defaultdict(list)
    for path in sorted(vault.rglob("*.md")):
        rel = path.relative_to(vault)
        if path.name in RESERVED_FILES or set(rel.parts) & SKIP_DIRS:
            continue
        text = path.read_text(encoding="utf-8")
        block, fields = frontmatter(text)
        title = fields.get("title", "").strip("\"'")
        aliases = scalar_list(block or "", "aliases")
        rel_key = rel.as_posix()
        pages[rel_key] = {"path": path, "text": text, "block": block or "", "fields": fields, "title": title, "aliases": aliases}
        keys = {normalize(path.stem), normalize(title), *(normalize(a) for a in aliases)}
        for key in keys:
            if key:
                lookup[key].append(rel_key)
    return pages, lookup


def resolve(raw: str, pages: dict[str, dict], lookup: dict[str, list[str]]) -> list[str]:
    key = normalize(raw)
    candidates = list(lookup.get(key, []))
    if "/" in key:
        candidates.extend(lookup.get(Path(key).name, []))
        candidates.extend(rel for rel in pages if normalize(rel) == key)
    return sorted(set(candidates))


def links(text: str) -> list[str]:
    return [m.group(1).split("|", 1)[0].strip() for m in re.finditer(r"(?<!!)\[\[([^\]]+)\]\]", text)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path, nargs="?", default=Path("wiki"))
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--allow-lifecycle", action="append", default=[])
    parser.add_argument("--allow-relationship-type", action="append", default=[])
    parser.add_argument("--required-trust-field", action="append", choices=("base_confidence", "lifecycle", "lifecycle_changed", "updated"), default=["base_confidence", "lifecycle"])
    parser.add_argument("--today", default=dt.date.today().isoformat(), help="ISO date for stale-page checks")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    vault = args.vault.resolve()
    pages, lookup = load(vault)
    lifecycles = DEFAULT_LIFECYCLES | set(args.allow_lifecycle)
    relationships = DEFAULT_RELATIONSHIPS | set(args.allow_relationship_type)
    result: dict[str, object] = {
        "scope": {"vault": str(vault), "pages": len(pages), "excluded_dirs": sorted(SKIP_DIRS)},
        "schema": {"allowed_lifecycles": sorted(lifecycles), "allowed_relationship_types": sorted(relationships), "required_trust_fields": args.required_trust_field},
        "findings": {},
    }
    findings: dict[str, Any] = result["findings"]  # type: ignore[assignment]

    missing = {rel: [key for key in REQUIRED + CAMPAIGN_REQUIRED if key not in item["fields"]]
               for rel, item in pages.items()}
    findings["missing_frontmatter"] = {rel: fields for rel, fields in missing.items() if fields}
    findings["missing_summary"] = [rel for rel, item in pages.items() if not item["fields"].get("summary")]
    findings["long_summary"] = [{"page": rel, "chars": len(item["fields"]["summary"])} for rel, item in pages.items() if len(item["fields"].get("summary", "")) > 200]
    findings["bad_lifecycle"] = [{"page": rel, "value": item["fields"].get("lifecycle")} for rel, item in pages.items() if item["fields"].get("lifecycle") and item["fields"]["lifecycle"].strip("\"'") not in lifecycles]
    findings["bad_type"] = [{"page": rel, "value": item["fields"].get("type")} for rel, item in pages.items() if item["fields"].get("type") and item["fields"]["type"].strip("\"'") not in CAMPAIGN_TYPES]
    findings["missing_trust"] = [{"page": rel, "missing": [key for key in args.required_trust_field if not item["fields"].get(key)]} for rel, item in pages.items() if any(not item["fields"].get(key) for key in args.required_trust_field)]

    documents = {}
    for path in sorted(vault.rglob("*.md")):
        rel = path.relative_to(vault)
        if set(rel.parts) & SKIP_DIRS:
            continue
        documents[rel.as_posix()] = path.read_text(encoding="utf-8")
    title_groups: dict[str, list[str]] = collections.defaultdict(list)
    for rel, item in pages.items():
        title = normalize(item["title"])
        if title:
            title_groups[title].append(rel)
    findings["duplicate_titles"] = [
        {"title": title, "pages": sorted(members)}
        for title, members in sorted(title_groups.items()) if len(members) > 1
    ]

    broken: list[dict[str, object]] = []
    incoming = collections.Counter()
    edges: list[tuple[str, str]] = []
    for rel, text in documents.items():
        for raw in links(text):
            targets = resolve(raw, pages, lookup)
            if len(targets) == 1:
                incoming[targets[0]] += 1
                edges.append((rel, targets[0]))
            elif not targets:
                broken.append({"page": rel, "target": raw})
    findings["broken_links"] = broken
    findings["orphan_pages"] = [rel for rel in pages if incoming[rel] == 0]
    index_targets = set()
    for raw in links(documents.get("index.md", "")):
        targets = resolve(raw, pages, lookup)
        if len(targets) == 1:
            index_targets.add(targets[0])
    findings["index_issues"] = {
        "missing_from_index": sorted(set(pages) - index_targets),
        "broken_links": [item for item in broken if item["page"] == "index.md"],
    }


    relationship_findings: list[dict[str, object]] = []
    for rel, item in pages.items():
        entries = re.findall(r"^\s*-\s*target:\s*[\"']?\[\[([^\]|]+)(?:\|[^\]]+)?\]\][\"']?\s*\n\s*type:\s*([^\s#]+)", item["block"], re.M)
        for index, (target, kind) in enumerate(entries):
            targets = resolve(target, pages, lookup)
            if kind not in relationships:
                relationship_findings.append({"page": rel, "index": index, "issue": "invalid_type", "value": kind})
            if not targets:
                relationship_findings.append({"page": rel, "index": index, "issue": "broken_target", "target": target})
            elif len(targets) > 1:
                relationship_findings.append({"page": rel, "index": index, "issue": "ambiguous_target", "target": target, "matches": targets})
            if rel in targets:
                relationship_findings.append({"page": rel, "index": index, "issue": "self_reference", "target": target})
    findings["typed_relationships"] = relationship_findings

    provenance: list[dict[str, object]] = []
    for rel, item in pages.items():
        if not item["fields"].get("provenance") and not re.search(r"\^\[(?:inferred|ambiguous)\]", item["text"]):
            continue
        claims = [line for line in item["text"].splitlines() if re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|#{1,6}\s+)", line)]
        total = max(1, len(claims))
        inferred = sum("^[inferred]" in line for line in claims) / total
        ambiguous = sum("^[ambiguous]" in line for line in claims) / total
        issues = []
        if ambiguous > 0.15:
            issues.append("ambiguous_over_15_percent")
        if inferred > 0.40 and not item["fields"].get("sources"):
            issues.append("unsourced_synthesis")
        if issues:
            provenance.append({"page": rel, "inferred": round(inferred, 3), "ambiguous": round(ambiguous, 3), "issues": issues})
    findings["provenance"] = provenance

    by_tag: dict[str, set[str]] = collections.defaultdict(set)
    for rel, item in pages.items():
        for tag in scalar_list(item["block"], "tags"):
            by_tag[tag].add(rel)
    fragmented = []
    edge_set = {tuple(sorted(edge)) for edge in edges if edge[0] != edge[1]}
    for tag, members in sorted(by_tag.items()):
        if len(members) < 5:
            continue
        possible = len(members) * (len(members) - 1) // 2
        actual = sum(1 for edge in edge_set if set(edge) <= members)
        cohesion = actual / possible if possible else 0
        if cohesion < 0.15:
            fragmented.append({"tag": tag, "pages": len(members), "links": actual, "cohesion": round(cohesion, 3)})
    findings["fragmented_tags"] = fragmented

    try:
        today = dt.date.fromisoformat(args.today)
    except ValueError as exc:
        raise SystemExit(f"invalid --today: {exc}") from exc
    stale = []
    for rel, item in pages.items():
        value = item["fields"].get("updated", "").strip("\"'")[:10]
        try:
            age = (today - dt.date.fromisoformat(value)).days
        except ValueError:
            continue
        if age > 90:
            stale.append({"page": rel, "updated": value, "days": age, "lifecycle": item["fields"].get("lifecycle", "")})
    findings["stale_pages"] = stale

    def count(key: str, value: Any) -> int:
        if key == "missing_frontmatter":
            return len(value)
        if isinstance(value, dict):
            return sum(len(item) if isinstance(item, list) else 1 for item in value.values())
        return len(value)

    counts = {key: count(key, value) for key, value in findings.items()}
    result["counts"] = counts
    if args.json:
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Wiki lint scope: {len(pages)} pages ({vault})")
        for key, value in counts.items():
            print(f"{key}: {value}")
        for key in ("missing_frontmatter", "missing_trust", "broken_links", "orphan_pages", "typed_relationships", "stale_pages"):
            items = findings[key]
            if items:
                print(f"\n{key}")
                for item in items if isinstance(items, list) else items.values():
                    print(f"- {item}")
    return 1 if any(counts.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
