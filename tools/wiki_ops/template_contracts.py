"""Explicit YAML template contracts and conformance checks."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
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
    version: int = 1
    repeatable: list[str] = field(default_factory=list)

def load_contract(path: str | Path) -> TemplateContract:
    target = Path(path)
    try:
        raw = yaml.safe_load(target.read_text(encoding="utf-8")) or {}
    except (OSError, yaml.YAMLError) as exc:
        raise ValueError(f"could not load template contract {target}: {exc}") from exc
    if not isinstance(raw, dict) or not raw.get("type"):
        raise ValueError("template contract requires type")
    sections = raw.get("sections", [])
    if not isinstance(sections, list):
        raise ValueError("template contract sections must be a list")
    return TemplateContract(
        template=str(raw.get("template", "")),
        type=str(raw["type"]),
        sections=[dict(item) for item in sections if isinstance(item, dict)],
        callouts=dict(raw.get("callouts", {})),
        frontmatter=dict(raw.get("frontmatter", {})),
        version=int(raw.get("version", 1)),
        repeatable=[str(item) for item in raw.get("repeatable", []) or []],
    )


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


def contract_for_type(root: str | Path, entity_type: str) -> TemplateContract | None:
    target = Path(root) / "templates" / "contracts" / f"{entity_type}.yml"
    if target.is_file():
        return load_contract(target)
    return None


def _finding(page_path: str | Path, rule_id: str, reason: str, **extra: Any) -> dict[str, Any]:
    return {
        "rule_id": rule_id,
        "file": str(page_path),
        "severity": "REPAIR",
        "repair_class": "human_repair",
        "reason": reason,
        **extra,
    }


def check_conformance(page_path: str | Path, page_text: str, contract: TemplateContract) -> list[dict[str, Any]]:
    fields = _frontmatter(page_text)
    headings = _headings(page_text)
    names = [name for _level, name in headings]
    lifecycle = fields.get("lifecycle", fields.get("status", "default")).casefold()
    findings: list[dict[str, Any]] = []
    repeatable = set(contract.repeatable)
    for section in contract.sections:
        heading = str(section.get("heading", "")).replace("{{title}}", fields.get("title", ""))
        requirement = "optional"
        when = section.get("when")
        if isinstance(when, dict):
            requirement = str(when.get(lifecycle, when.get("default", "optional"))).casefold()
        elif section.get("required") is True:
            requirement = "required"
        occurrences = [index for index, (_level, name) in enumerate(headings) if name == heading]
        if requirement == "required" and not occurrences:
            findings.append(_finding(page_path, "TMPL_missing_required", f"Required section '{heading}' is missing", section=heading))
        if len(occurrences) > 1 and heading not in repeatable and not section.get("repeatable", False):
            findings.append(_finding(page_path, "TMPL_duplicate_section", f"Section '{heading}' is not repeatable", section=heading))
        expected_level = section.get("level")
        if occurrences and expected_level is not None and any(headings[index][0] != int(expected_level) for index in occurrences):
            findings.append(_finding(page_path, "TMPL_wrong_level", f"Section '{heading}' has the wrong heading level", section=heading))
        parent = section.get("parent")
        if occurrences and parent and parent not in names:
            findings.append(_finding(page_path, "TMPL_missing_parent", f"Section '{heading}' requires parent '{parent}'", section=heading, parent=parent))
    for field_name in contract.frontmatter.get("required", []) or []:
        if field_name not in fields:
            findings.append(_finding(page_path, "TMPL_missing_frontmatter", f"Required frontmatter '{field_name}' is missing", field=field_name))
    allowed = set(contract.callouts.get("allowed", []) or [])
    for match in re.finditer(r"^\s*>\s*\[!([^\]]+)\]", page_text, re.M):
        callout = match.group(1).split("+", 1)[0].strip()
        if allowed and callout not in allowed:
            findings.append(_finding(page_path, "TMPL_disallowed_callout", f"Callout '[!{callout}]' is not allowed for {contract.type}", callout=callout))
    if fields.get("redirects_to"):
        findings.append({
            "rule_id": "TMPL_redirect_stub",
            "file": str(page_path),
            "severity": "REPAIR",
            "repair_class": "deterministic_repair",
            "repair_action": "delete_redirect_stub",
            "action": "delete_redirect_stub",
            "target": fields["redirects_to"],
            "reason": "redirects_to pages are legacy stubs, not canonical entities",
        })
