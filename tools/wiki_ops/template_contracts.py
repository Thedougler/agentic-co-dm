"""Explicit YAML template contracts and conformance checks."""
from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

@dataclass(frozen=True)
class TemplateContract:
    template: str
    type: str
    sections: list[dict[str, Any]]
    callouts: dict[str, Any]
    frontmatter: dict[str, Any]


def load_contract(path: str | Path) -> TemplateContract:
    target = Path(path)
    try:
        raw = yaml.safe_load(target.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        raise ValueError(f"could not load template contract {target}: {exc}") from exc
    if not isinstance(raw, dict) or not raw.get("type"):
        raise ValueError("template contract requires type")
    return TemplateContract(str(raw.get("template", "")), str(raw["type"]), list(raw.get("sections", [])), dict(raw.get("callouts", {})), dict(raw.get("frontmatter", {})))


def _frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    result: dict[str, str] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if ":" in line and not line[:1].isspace():
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip("\"'")
    return result


def _headings(text: str) -> list[tuple[int, str]]:
    return [(len(m.group(1)), m.group(2).strip()) for m in re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*$", text)]


def check_conformance(page_path: str | Path, page_text: str, contract: TemplateContract) -> list[dict[str, Any]]:
    fields = _frontmatter(page_text)
    headings = _headings(page_text)
    names = {name for _level, name in headings}
    lifecycle = fields.get("lifecycle", fields.get("status", "default"))
    findings: list[dict[str, Any]] = []
    for section in contract.sections:
        heading = str(section.get("heading", "")).replace("{{title}}", fields.get("title", ""))
        requirement = "optional"
        if isinstance(section.get("when"), dict):
            requirement = str(section["when"].get(lifecycle, section["when"].get("default", "optional")))
        elif section.get("required") is True:
            requirement = "required"
        if heading not in names and requirement == "required":
            findings.append({"rule_id": "TMPL_missing_required", "file": str(page_path), "severity": "REPAIR", "section": heading, "repair_class": "human_repair", "reason": f"Required section '{heading}' is missing"})
    required = contract.frontmatter.get("required", [])
    for field in required:
        if field not in fields:
            findings.append({"rule_id": "TMPL_missing_frontmatter", "file": str(page_path), "severity": "REPAIR", "field": field, "repair_class": "human_repair", "reason": f"Required frontmatter '{field}' is missing"})
    allowed = set(contract.callouts.get("allowed", []))
    if allowed:
        for match in re.finditer(r"^\s*>\s*\[!([^\]]+)\]", page_text, re.M):
            callout = match.group(1).split("+", 1)[0].strip()
            if callout not in allowed:
                findings.append({"rule_id": "TMPL_disallowed_callout", "file": str(page_path), "severity": "REPAIR", "callout": callout, "repair_class": "human_repair", "reason": f"Callout '[!{callout}]' is not allowed for {contract.type}"})
    return findings
