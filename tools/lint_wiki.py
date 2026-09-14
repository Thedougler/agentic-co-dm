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

OWNER_LIFECYCLES = {"draft", "proposed", "accepted", "rejected", "canon"}
DEFAULT_LIFECYCLES = set(OWNER_LIFECYCLES)
DEFAULT_RELATIONSHIPS = {
    "extends", "implements", "contradicts", "derived_from", "uses", "replaces", "related_to"
}
REQUIRED = ("title", "category", "tags", "sources", "created", "updated")
CAMPAIGN_REQUIRED = ("type", "lifecycle", "reveal")
OWNER_TYPES = {
    "npc", "pc", "place", "faction", "item", "creature", "vehicle", "spell",
    "lore", "quest", "region",
    "session-prep", "session", "recap", "work",
}
CAMPAIGN_TYPES = set(OWNER_TYPES)
HARD_KEYS = (
    "broken_links",
    "missing_frontmatter",
    "bad_type",
    "bad_lifecycle",
    "typed_relationships",
    "pc_identity_mismatch",
    "spaced_basename",
    "aruhe_prefix_basename",
    "illegal_basename",
    "duplicate_stems",
)
PC_ROLE = re.compile(r"^(pc|player character|player)$", re.I)
TOKEN = re.compile(r"`([^`]+)`")
RESERVED_FILES = {"AGENTS.md", "index.md", "log.md", "hot.md"}
SKIP_DIRS = {".obsidian", "_archive", "_archives", "_raw", "_readouts", "_meta", "templates"}
# Closed set: common ability/stat wikilinks are not HARD broken_links (no auto-pages).
MECHANIC_LINK_ALLOWLIST = {
    "strength", "dexterity", "constitution", "intelligence", "wisdom", "charisma",
    "speed", "initiative", "proficiency", "condition",
}

SNAKE_TOKEN = re.compile(r"[A-Za-z][A-Za-z0-9]*(?:_[A-Za-z0-9]+)+")
TABLE_ROW = re.compile(r"^\s*\|.*\|\s*$")
LIST_BOLD_SNAKE = re.compile(
    r"^\s*(?:[-*+]|\d+[.)])\s+\*\*(" + SNAKE_TOKEN.pattern + r")\*\*"
)


def body_after_frontmatter(text: str) -> tuple[int, str]:
    """Return (1-based start line of body, body text). FM block is excluded."""
    if not text.startswith("---\n"):
        return 1, text
    match = re.search(r"\n---\s*(?:\n|$)", text[4:])
    if not match:
        return 1, text
    # body begins after the closing --- line
    after = match.end()  # relative to text[4:]
    body_offset = 4 + after
    start_line = text[:body_offset].count("\n") + 1
    return start_line, text[body_offset:]


def classify_table_cell(cell: str) -> tuple[str, str] | None:
    """If cell is only a snake_case label (bare/bt/bold), return (token, kind)."""
    s = cell.strip()
    if not s:
        return None
    if "attachments/" in s:
        return None
    if re.search(r"https?://|www\.", s):
        return None
    # entire cell is a wikilink / embed — not a DM label
    if re.fullmatch(r"!?\[\[[^\]]+\]\]", s):
        return None
    m = re.fullmatch(r"\*\*(" + SNAKE_TOKEN.pattern + r")\*\*", s)
    if m:
        return m.group(1), "table_bold"
    m = re.fullmatch(r"`(" + SNAKE_TOKEN.pattern + r")`", s)
    if m:
        return m.group(1), "table_bt"
    m = re.fullmatch(SNAKE_TOKEN.pattern, s)
    if m:
        return m.group(0), "table_bare"
    return None


def find_snake_case_labels(text: str) -> list[dict[str, object]]:
    """Soft findings for user-facing snake_case table/list labels (not YAML)."""
    start_line, body = body_after_frontmatter(text)
    findings: list[dict[str, object]] = []
    in_fence = False
    lines = body.splitlines()
    for i, line in enumerate(lines):
        line_no = start_line + i
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if "attachments/" in line:
            continue
        if TABLE_ROW.match(line):
            # drop leading/trailing empty from split on pipes
            cells = line.strip().strip("|").split("|")
            for cell in cells:
                hit = classify_table_cell(cell)
                if hit:
                    token, kind = hit
                    findings.append({"page": None, "line": line_no, "token": token, "kind": kind})
            continue
        m = LIST_BOLD_SNAKE.match(line)
        if m:
            findings.append({"page": None, "line": line_no, "token": m.group(1), "kind": "list_bold"})
    return findings


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


def parse_owner_schema(path: Path) -> tuple[set[str], set[str]]:
    types: set[str] = set()
    lifecycles: set[str] = set()
    if not path.is_file():
        return types, lifecycles
    for line in path.read_text(encoding="utf-8").splitlines():
        stripped = line.lstrip()
        tokens = TOKEN.findall(line)
        if stripped.startswith("| `type`"):
            types.update(token for token in tokens if token != "type")
        elif stripped.startswith("| `lifecycle`"):
            lifecycles.update(token for token in tokens if token != "lifecycle")
    return types, lifecycles


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
    def candidates_for(value: str) -> list[str]:
        key = normalize(value)
        found = list(lookup.get(key, []))
        if "/" in key:
            found.extend(lookup.get(Path(key).name, []))
            found.extend(rel for rel in pages if normalize(rel) == key)
        return sorted(set(found))

    candidates = candidates_for(raw)
    if candidates:
        return candidates
    # Exact miss: retry once after stripping a leading English article.
    stripped = re.sub(r"^(the|a|an)\s+", "", raw.strip(), count=1, flags=re.I)
    if stripped and stripped != raw.strip():
        return candidates_for(stripped)
    return []


def links(text: str) -> list[str]:
    # Ignore wikilinks that appear only inside inline code spans.
    scrubbed = TOKEN.sub(lambda m: " " * len(m.group(0)), text)
    return [m.group(1).split("|", 1)[0].strip() for m in re.finditer(r"(?<!!)\[\[([^\]]+)\]\]", scrubbed)]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("vault", type=Path, nargs="?", default=Path("wiki"))
    parser.add_argument("--json", action="store_true", help="emit JSON")
    parser.add_argument("--hard-only", action="store_true", help="exit nonzero only on HARD findings")
    parser.add_argument("--schema-source", type=Path, help="Owner AGENTS.md (default: <vault>/AGENTS.md)")
    parser.add_argument("--allow-lifecycle", action="append", default=[])
    parser.add_argument("--allow-relationship-type", action="append", default=[])
    parser.add_argument("--required-trust-field", action="append", choices=("base_confidence", "lifecycle", "lifecycle_changed", "updated"), default=["base_confidence", "lifecycle"])
    parser.add_argument("--today", default=dt.date.today().isoformat(), help="ISO date for stale-page checks")
    return parser.parse_args()


def pc_identity_mismatches(pages: dict[str, dict]) -> list[dict[str, object]]:
    """HARD: role PC / non-empty player: must be type pc under entities/pc/."""
    out: list[dict[str, object]] = []
    for rel, item in pages.items():
        fields = item["fields"]
        typ = (fields.get("type") or "").strip("\"'")
        role = (fields.get("role") or "").strip("\"'")
        player_raw = fields.get("player")
        player_val = (player_raw or "").strip().strip("\"'")
        has_player = player_raw is not None and bool(player_val)
        if not (PC_ROLE.match(role) or has_player):
            continue
        parts = Path(rel).parts
        under_pc = len(parts) >= 2 and parts[0] == "entities" and parts[1] == "pc"
        under_npc = len(parts) >= 2 and parts[0] == "entities" and parts[1] == "npc"
        if typ == "npc" or under_npc or typ != "pc" or not under_pc:
            out.append({
                "page": rel,
                "type": typ or None,
                "role": role or None,
                "has_player": has_player,
                "path": rel,
            })
    return out


ILLEGAL_BASENAME_CHARS = re.compile(r'[/\\:*?"<>|\x00-\x1f]')
ARUHE_PREFIX = re.compile(r"^Aruhe\s*-\s*", re.I)
SNAKE_OWNER_STEM = re.compile(r"^[a-z0-9]+(_[a-z0-9]+)+$")

def illegal_basename_issues(stem: str) -> list[str]:
    """Forbidden basename stem characters/shape (spaces reported separately)."""
    reasons: list[str] = []
    if ILLEGAL_BASENAME_CHARS.search(stem):
        reasons.append("forbidden_char")
    if stem != stem.strip():
        reasons.append("edge_whitespace")
    if any(ord(ch) < 32 for ch in stem):
        reasons.append("control_char")
    return reasons


def spaced_basenames(pages: dict[str, dict]) -> list[dict[str, object]]:
    """HARD: any whitespace in live page Path.stem (kebab standard #80/#72)."""
    out: list[dict[str, object]] = []
    for rel, item in pages.items():
        if item["fields"].get("redirects_to"):
            continue
        if "attachments" in Path(rel).parts:
            continue
        stem = Path(rel).stem
        if any(ch.isspace() for ch in stem):
            out.append({"page": rel, "stem": stem})
    return out


def aruhe_prefix_basenames(pages: dict[str, dict]) -> list[dict[str, object]]:
    """HARD: leading Aruhe - / Aruhe - / Aruhe- on live basenames/stems."""
    out: list[dict[str, object]] = []
    for rel, item in pages.items():
        if item["fields"].get("redirects_to"):
            continue
        if "attachments" in Path(rel).parts:
            continue
        stem = Path(rel).stem
        if ARUHE_PREFIX.match(stem):
            out.append({"page": rel, "stem": stem})
    return out


def illegal_basenames(pages: dict[str, dict]) -> list[dict[str, object]]:
    """HARD: forbidden characters / edge whitespace / controls in live stems."""
    out: list[dict[str, object]] = []
    for rel in pages:
        if "attachments" in Path(rel).parts:
            continue
        stem = Path(rel).stem
        reasons = illegal_basename_issues(stem)
        if reasons:
            out.append({"page": rel, "stem": stem, "reasons": reasons})
    return out


def duplicate_stems(pages: dict[str, dict]) -> list[dict[str, object]]:
    """HARD: vault-wide unique stems (casefold); attachments skipped."""
    groups: dict[str, list[str]] = collections.defaultdict(list)
    for rel in pages:
        if "attachments" in Path(rel).parts:
            continue
        stem = Path(rel).stem
        groups[stem.casefold()].append(rel)
    return [
        {"stem": Path(members[0]).stem, "pages": sorted(members)}
        for _key, members in sorted(groups.items())
        if len(members) > 1
    ]


def snake_case_owner_basenames(pages: dict[str, dict]) -> list[dict[str, object]]:
    """Soft: snake_case owner basenames under entities/{type}/ only (kebab not flagged)."""
    out: list[dict[str, object]] = []
    for rel in pages:
        parts = Path(rel).parts
        if len(parts) < 3 or parts[0] != "entities":
            continue
        if parts[1] not in OWNER_TYPES:
            continue
        stem = Path(rel).stem
        if SNAKE_OWNER_STEM.fullmatch(stem):
            out.append({"page": rel, "stem": stem, "kind": "snake"})
    return out



def main() -> int:
    args = parse_args()
    vault = args.vault.resolve()
    pages, lookup = load(vault)
    schema_path = args.schema_source.resolve() if args.schema_source else vault / "AGENTS.md"
    owner_types, owner_lifecycles = parse_owner_schema(schema_path)
    types = CAMPAIGN_TYPES | owner_types
    lifecycles = DEFAULT_LIFECYCLES | owner_lifecycles | set(args.allow_lifecycle)
    relationships = DEFAULT_RELATIONSHIPS | set(args.allow_relationship_type)
    result: dict[str, object] = {
        "scope": {"vault": str(vault), "pages": len(pages), "excluded_dirs": sorted(SKIP_DIRS)},
        "schema": {
            "source": str(schema_path) if schema_path.is_file() else None,
            "allowed_types": sorted(types),
            "allowed_lifecycles": sorted(lifecycles),
            "allowed_relationship_types": sorted(relationships),
            "required_trust_fields": args.required_trust_field,
            "hard": list(HARD_KEYS),
        },
        "findings": {},
    }
    findings: dict[str, Any] = result["findings"]  # type: ignore[assignment]

    missing = {rel: [key for key in REQUIRED + CAMPAIGN_REQUIRED if key not in item["fields"]]
               for rel, item in pages.items()}
    findings["missing_frontmatter"] = {
        rel: fields
        for rel, fields in missing.items()
        if fields and not pages[rel]["fields"].get("redirects_to")
    }
    findings["missing_summary"] = [rel for rel, item in pages.items() if not item["fields"].get("summary")]
    findings["long_summary"] = [{"page": rel, "chars": len(item["fields"]["summary"])} for rel, item in pages.items() if len(item["fields"].get("summary", "")) > 200]
    findings["bad_lifecycle"] = [{"page": rel, "value": item["fields"].get("lifecycle")} for rel, item in pages.items() if item["fields"].get("lifecycle") and item["fields"]["lifecycle"].strip("\"'") not in lifecycles]
    findings["bad_type"] = [{"page": rel, "value": item["fields"].get("type")} for rel, item in pages.items() if item["fields"].get("type") and item["fields"]["type"].strip("\"'") not in types]
    findings["pc_identity_mismatch"] = pc_identity_mismatches(pages)
    findings["pc_tag_on_npc"] = [
        {"page": rel, "type": (item["fields"].get("type") or "").strip("\"'") or None, "path": rel}
        for rel, item in pages.items()
        if (item["fields"].get("type") or "").strip("\"'") == "npc"
        and "pc" in {t.casefold() for t in scalar_list(item["block"], "tags")}
        and not (
            PC_ROLE.match((item["fields"].get("role") or "").strip("\"'"))
            or (
                item["fields"].get("player") is not None
                and bool((item["fields"].get("player") or "").strip().strip("\"'"))
            )
        )
    ]
    findings["spaced_basename"] = spaced_basenames(pages)
    findings["aruhe_prefix_basename"] = aruhe_prefix_basenames(pages)
    findings["illegal_basename"] = illegal_basenames(pages)
    findings["duplicate_stems"] = duplicate_stems(pages)
    findings["snake_case_owner_basename"] = snake_case_owner_basenames(pages)
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
    for rel, body in documents.items():
        reserved_page = Path(rel).name in RESERVED_FILES
        for raw in links(body):
            if normalize(raw) in MECHANIC_LINK_ALLOWLIST:
                continue
            targets = resolve(raw, pages, lookup)
            if len(targets) == 1:
                incoming[targets[0]] += 1
                edges.append((rel, targets[0]))
            elif not targets and not reserved_page:
                # Skip HARD broken_links from reserved non-content (AGENTS/index/log/hot).
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

    snake_case_labels: list[dict[str, object]] = []
    for rel, item in pages.items():
        for hit in find_snake_case_labels(item["text"]):
            hit = dict(hit)
            hit["page"] = rel
            snake_case_labels.append(hit)
    findings["snake_case_labels"] = snake_case_labels

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
    hard_fail = any(int(counts.get(key, 0) or 0) > 0 for key in HARD_KEYS)
    result["hard_fail"] = hard_fail
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
    if args.hard_only:
        return 1 if hard_fail else 0
    return 1 if any(counts.values()) else 0


if __name__ == "__main__":
    raise SystemExit(main())
