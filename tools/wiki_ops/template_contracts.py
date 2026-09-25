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
    layout: dict[str, Any] = field(default_factory=dict)
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
        layout=dict(raw.get("layout", {})),
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


_IMAGE = re.compile(r"^\s*!\[\[.+?\]\]\s*$")
_FENCE = re.compile(r"^\s*```")


def _section_span(lines: list[str], heading: str) -> tuple[int, int, int] | None:
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if not match or match.group(2).strip() != heading:
            continue
        level = len(match.group(1))
        end = len(lines)
        for following, candidate in enumerate(lines[index + 1:], index + 1):
            next_heading = re.match(r"^(#{1,6})\s+", candidate)
            if next_heading and len(next_heading.group(1)) <= level:
                end = following
                break
        return index, end, level
    return None


def check_layout_conformance(page_path: str | Path, page_text: str,
                             layout: dict[str, Any]) -> list[dict[str, Any]]:
    """Check contract-declared placement rules without interpreting page prose."""
    lines = page_text.splitlines()
    findings: list[dict[str, Any]] = []
    statblock = layout.get("statblock", {})
    statblock_span = _section_span(lines, "Statblock")
    if statblock.get("image_position") == "immediately_before_fence" and statblock_span:
        start, end, _level = statblock_span
        images = [index for index in range(start + 1, end) if _IMAGE.match(lines[index])]
        fences = [index for index in range(start + 1, end) if _FENCE.match(lines[index])]
        if images and fences:
            first_fence = fences[0]
            before = [index for index in images if index < first_fence]
            after = [index for index in images if index > first_fence]
            last_content = next((index for index in range(first_fence - 1, start, -1)
                                 if lines[index].strip()), None)
            max_images = statblock.get("max_images_before_fence")
            too_many = isinstance(max_images, int) and len(before) > max_images
            if not before or too_many or last_content != before[-1] or after:
                reason = (
                    f"Statblock permits at most {max_images} overview image immediately before the statblock fence; "
                    "move remaining images to Art subsections"
                    if isinstance(max_images, int)
                    else "Statblock images must be immediately before the statblock fence"
                )
                violation_line = before[max_images] if too_many else images[0]
                findings.append(_finding(
                    page_path,
                    "TMPL006",
                    reason,
                    line=violation_line + 1,
                    section="Statblock",
                ))
    art = layout.get("art", {})
    art_span = _section_span(lines, "Art")
    if art.get("embeds_require_subsections") and art_span:
        start, end, art_level = art_span
        child_active = False
        for index in range(start + 1, end):
            heading = re.match(r"^(#{1,6})\s+", lines[index])
            if heading:
                child_active = len(heading.group(1)) > art_level
            elif _IMAGE.match(lines[index]) and not child_active:
                findings.append(_finding(
                    page_path,
                    "TMPL007",
                    "Art embeds must be nested under a subsection heading",
                    line=index + 1,
                    section="Art",
                ))
    return findings


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
    status = fields.get("status", "default").casefold()
    findings: list[dict[str, Any]] = []
    repeatable = set(contract.repeatable)
    for section in contract.sections:
        heading = str(section.get("heading", "")).replace("{{title}}", fields.get("title", ""))
        requirement = "optional"
        when = section.get("when")
        if isinstance(when, dict):
            requirement = str(when.get(status, when.get("default", "optional"))).casefold()
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
    findings.extend(check_layout_conformance(page_path, page_text, contract.layout))
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
    return findings
