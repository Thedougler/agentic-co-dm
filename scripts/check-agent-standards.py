#!/usr/bin/env python3
"""Check agent-facing instruction standards (AGENT001–AGENT003)."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]

AGENT001_PHRASES = (
    "## Work gate",
    "dm-gated",
    "file nothing until accept",
    "wiki write after DM accept",
    "Work-propose",
    "wait for accept",
)

KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FR_LINE = re.compile(r"^[-*]\s+\*\*FR-[0-9]+\*\*\s*:", re.M)
AGENT_FACING = re.compile(r"agent-facing", re.I)
REGISTRY_ID = re.compile(r"\b[A-Z]+[0-9]{3}\b")


def _findings_agent001(root: Path) -> list[dict]:
    findings: list[dict] = []
    paths: list[Path] = []
    for rel in ("AGENTS.md", "wiki/AGENTS.md"):
        p = root / rel
        if p.is_file():
            paths.append(p)
    docs = root / "docs" / "agents"
    if docs.is_dir():
        paths.extend(sorted(docs.rglob("*.md")))
    skills = root / ".agents" / "skills"
    if skills.is_dir():
        paths.extend(sorted(skills.rglob("*.md")))
    for path in paths:
        text = path.read_text(encoding="utf-8")
        for phrase in AGENT001_PHRASES:
            if phrase in text:
                findings.append(
                    {
                        "id": "AGENT001",
                        "path": _rel(root, path),
                        "reason": f"forbidden_phrase:{phrase}",
                    }
                )
    return findings


def _rel(root: Path, path: Path) -> str:
    try:
        return str(path.relative_to(root)).replace("\\", "/")
    except ValueError:
        return str(path)


def _kebab_parts_ok(parts: tuple[str, ...]) -> bool:
    return all(KEBAB.fullmatch(part) for part in parts)


def _agent002_ok(rel: str) -> bool:
    rel = rel.replace("\\", "/")
    if rel in {"AGENTS.md", "wiki/AGENTS.md", ".omp/AGENTS.md"}:
        return True
    if rel.startswith(".agents/skills/"):
        rest = rel[len(".agents/skills/") :]
        parts = rest.split("/")
        if len(parts) < 2:
            return False
        skill_dir, *tail = parts
        if not KEBAB.fullmatch(skill_dir):
            return False
        if tail == ["SKILL.md"]:
            return True
        if not tail:
            return False
        filename = tail[-1]
        stem, dot, ext = filename.rpartition(".")
        if dot != ".":
            return False
        if not KEBAB.fullmatch(stem):
            return False
        return _kebab_parts_ok(tuple(tail[:-1]))
    if rel.startswith("docs/agents/"):
        rest = rel[len("docs/agents/") :]
        parts = rest.split("/")
        filename = parts[-1]
        stem, dot, ext = filename.rpartition(".")
        if dot != ".":
            return False
        if not KEBAB.fullmatch(stem):
            return False
        return _kebab_parts_ok(tuple(parts[:-1]))
    return False


def _iter_agent_facing_files(root: Path) -> list[Path]:
    files: list[Path] = []
    for rel in ("AGENTS.md", "wiki/AGENTS.md", ".omp/AGENTS.md"):
        p = root / rel
        if p.is_file():
            files.append(p)
    skills = root / ".agents" / "skills"
    if skills.is_dir():
        files.extend(
            p
            for p in sorted(skills.rglob("*"))
            if p.is_file() and p.name != ".DS_Store" and "__pycache__" not in p.parts
        )
    docs = root / "docs" / "agents"
    if docs.is_dir():
        files.extend(
            p
            for p in sorted(docs.rglob("*"))
            if p.is_file() and p.name != ".DS_Store" and "__pycache__" not in p.parts
        )
    return files


def _findings_agent002(root: Path) -> list[dict]:
    findings: list[dict] = []
    for path in _iter_agent_facing_files(root):
        rel = _rel(root, path)
        if not _agent002_ok(rel):
            findings.append({"id": "AGENT002", "path": rel, "reason": "ad_hoc_path"})
    return findings


def _fr_blocks(text: str) -> list[str]:
    lines = text.splitlines()
    blocks: list[str] = []
    current: list[str] | None = None
    in_fr = False
    for line in lines:
        if re.match(r"^#{1,3}\s+Functional Requirements\b", line, re.I):
            in_fr = True
            continue
        if in_fr and re.match(r"^#{1,3}\s+", line) and not re.match(
            r"^#{1,3}\s+Functional Requirements\b", line, re.I
        ):
            if current:
                blocks.append("\n".join(current))
                current = None
            in_fr = False
            continue
        if not in_fr:
            continue
        if FR_LINE.match(line):
            if current:
                blocks.append("\n".join(current))
            current = [line]
        elif current is not None:
            if line.startswith(" ") or line.startswith("\t") or not line.strip():
                current.append(line)
            elif line.startswith("- ") or line.startswith("* "):
                blocks.append("\n".join(current))
                current = [line] if FR_LINE.match(line) else None
                if current is None and "agent-facing" in line.lower():
                    # non-FR bullet; ignore
                    pass
            else:
                current.append(line)
    if current:
        blocks.append("\n".join(current))
    return blocks


def _findings_agent003(root: Path) -> list[dict]:
    findings: list[dict] = []
    registry_path = root / "rules" / "registry.yml"
    ids: set[str] = set()
    if registry_path.is_file():
        data = yaml.safe_load(registry_path.read_text(encoding="utf-8")) or {}
        for rule in data.get("rules") or []:
            rid = rule.get("id")
            if rid:
                ids.add(str(rid))
    specs = root / "specs"
    if not specs.is_dir():
        return findings
    for spec in sorted(specs.glob("*/spec.md")):
        text = spec.read_text(encoding="utf-8")
        for block in _fr_blocks(text):
            if not AGENT_FACING.search(block):
                continue
            cited = REGISTRY_ID.findall(block)
            if not any(cid in ids for cid in cited):
                findings.append(
                    {
                        "id": "AGENT003",
                        "path": _rel(root, spec),
                        "reason": "agent_facing_fr_missing_registry_id",
                    }
                )
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=str(ROOT))
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = Path(args.root)
        findings = _findings_agent001(root) + _findings_agent002(root) + _findings_agent003(root)
        payload = {
            "status": "findings" if findings else "clean",
            "findings": findings,
            "count": len(findings),
        }
    except (OSError, yaml.YAMLError, AttributeError) as exc:
        print(json.dumps({"status": "error", "error": str(exc)}))
        return 2
    print(json.dumps(payload, indent=2, sort_keys=True))
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
