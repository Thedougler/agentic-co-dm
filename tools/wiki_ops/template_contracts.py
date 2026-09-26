"""Template-derived page contracts and conformance checks.

The page template in ``wiki/templates/`` is the only source of truth. Nothing here
names a page type, heading, or template file; editing a template changes what the
linter expects.

What a template says, and how it is read:

- Which template a page uses: the template whose frontmatter ``type`` matches the
  page's ``type`` and whose ``kind`` matches the page's ``kind``; otherwise the
  template named ``<type>.md``.
- Sections: every heading in the template (inside column fences too), with its level
  and its parent heading. Order follows the template.
- Section rules: the first word of the HTML comment directly under a heading.
  ``Required.`` means every page carries the section; ``Required when <key> is
  <value>.`` requires it only when that frontmatter key has that value;
  ``Free-form.`` lets pages add their own headings. Every other section is optional.
- Callouts: the callout types that appear in the template.
- Statblock images: a template section that holds a ``statblock`` fence allows one
  overview image, directly before the fence.
- Image subsections: a template section below the title whose only content is child
  headings keeps page images under those child headings.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
_CALLOUT = re.compile(r"^\s*>\s*\[!([^\]]+)\]", re.M)
_COMMENT_START = re.compile(r"^\s*<!--\s*(.*)$")
_REQUIRED_WHEN = re.compile(r"^Required when\s+([\w-]+)\s+is\s+([\w -]+?)\.", re.I)
_IMAGE = re.compile(r"^\s*!\[\[.+?\]\]\s*$")
_FENCE = re.compile(r"^\s*```")
_STATBLOCK_FENCE = re.compile(r"^\s*```statblock\b")


@dataclass(frozen=True)
class TemplateContract:
    template: str
    type: str
    sections: list[dict[str, Any]]
    callouts: dict[str, Any]
    frontmatter: dict[str, Any] = field(default_factory=dict)
    layout: dict[str, Any] = field(default_factory=dict)
    open: bool = False


def _frontmatter_text(text: str) -> tuple[dict[str, Any], str]:
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    try:
        value = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        value = {}
    return (value if isinstance(value, dict) else {}), text[end + 4:]


def _frontmatter(text: str) -> dict[str, str]:
    fields, _body = _frontmatter_text(text)
    return {str(key): "" if value is None else str(value).strip() for key, value in fields.items()}


def _templates_dir(root: str | Path) -> Path:
    base = Path(root)
    for candidate in (base / "wiki" / "templates", base / "templates"):
        if candidate.is_dir():
            return candidate
    return base / "wiki" / "templates"


@lru_cache(maxsize=8)
def _template_index(directory: str) -> tuple[tuple[str, str, str], ...]:
    rows = []
    for path in sorted(Path(directory).glob("*.md")):
        fields = _frontmatter(path.read_text(encoding="utf-8"))
        rows.append((str(path), fields.get("type", "").casefold(), fields.get("kind", "").casefold()))
    return tuple(rows)


def template_for(root: str | Path, entity_type: str, kind: str = "") -> Path | None:
    """Pick the template for a page from the templates' own frontmatter."""
    entity_type, kind = entity_type.strip().casefold(), kind.strip().casefold()
    if not entity_type:
        return None
    directory = _templates_dir(root)
    rows = [row for row in _template_index(str(directory)) if row[1] == entity_type]
    if kind:
        for path, _type, template_kind in rows:
            if template_kind == kind:
                return Path(path)
    default = directory / f"{entity_type}.md"
    return default if default.is_file() else None


def template_types(root: str | Path) -> set[str]:
    """Every page ``type`` some template declares; a new template adds its type."""
    return {row[1] for row in _template_index(str(_templates_dir(root))) if row[1]}


def _section_rule(lines: list[str], index: int) -> dict[str, Any]:
    for line in lines[index + 1:]:
        if not line.strip():
            continue
        comment = _COMMENT_START.match(line)
        if not comment:
            return {}
        text = comment.group(1).strip()
        when = _REQUIRED_WHEN.match(text)
        if when:
            return {"when": {"key": when.group(1).casefold(), "value": when.group(2).strip().casefold()}}
        if re.match(r"^Required\b", text):
            return {"required": True}
        if re.match(r"^Free-form\b", text):
            return {"freeform": True}
        return {}
    return {}


def _is_container(lines: list[str], index: int, level: int) -> bool:
    has_child = False
    in_comment = False
    for line in lines[index + 1:]:
        heading = _HEADING.match(line)
        if heading:
            if len(heading.group(1)) <= level:
                break
            has_child = True
            break
        stripped = line.strip()
        if in_comment:
            in_comment = "-->" not in stripped
            continue
        if stripped.startswith("<!--"):
            in_comment = "-->" not in stripped
            continue
        if stripped and not stripped.startswith("`"):
            return False
    return has_child


@lru_cache(maxsize=64)
def _derive(template_path: str, mtime: float) -> TemplateContract:
    text = Path(template_path).read_text(encoding="utf-8")
    fields, body = _frontmatter_text(text)
    lines = body.splitlines()
    sections: list[dict[str, Any]] = []
    stack: list[tuple[int, str]] = []
    statblock_sections: set[str] = set()
    containers: set[str] = set()
    current = ""
    for index, line in enumerate(lines):
        if _STATBLOCK_FENCE.match(line) and current:
            statblock_sections.add(current)
        heading = _HEADING.match(line)
        if not heading:
            continue
        level, name = len(heading.group(1)), heading.group(2).strip()
        while stack and stack[-1][0] >= level:
            stack.pop()
        section = {"heading": name, "level": level, **_section_rule(lines, index)}
        if stack:
            section["parent"] = stack[-1][1]
        sections.append(section)
        stack.append((level, name))
        current = name
        if level > 1 and _is_container(lines, index, level):
            containers.add(name)
    return TemplateContract(
        template=Path(template_path).name,
        type=str(fields.get("type", "")),
        sections=sections,
        callouts={"allowed": sorted({m.group(1).split("-", 1)[0].split("+", 1)[0].strip().casefold()
                                     for m in _CALLOUT.finditer(body)})},
        layout={"statblock_sections": sorted(statblock_sections), "containers": sorted(containers)},
        open=any(section.get("freeform") for section in sections),
    )


def derive_contract(template_path: str | Path) -> TemplateContract:
    path = Path(template_path)
    return _derive(str(path), path.stat().st_mtime)


def contract_for_type(root: str | Path, entity_type: str, kind: str = "") -> TemplateContract | None:
    template = template_for(root, entity_type, kind)
    return derive_contract(template) if template else None


def contract_for_page(root: str | Path, page_text: str) -> TemplateContract | None:
    fields = _frontmatter(page_text)
    return contract_for_type(root, fields.get("type", ""), fields.get("kind", ""))


def _section_span(lines: list[str], heading: str) -> tuple[int, int, int] | None:
    for index, line in enumerate(lines):
        match = _HEADING.match(line)
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


def _finding(page_path: str | Path, rule_id: str, reason: str, **extra: Any) -> dict[str, Any]:
    return {
        "rule_id": rule_id,
        "file": str(page_path),
        "severity": "REPAIR",
        "repair_class": "human_repair",
        "reason": reason,
        **extra,
    }


def check_layout_conformance(page_path: str | Path, page_text: str,
                             layout: dict[str, Any]) -> list[dict[str, Any]]:
    """Check image placement the template shows, without interpreting page prose."""
    lines = page_text.splitlines()
    findings: list[dict[str, Any]] = []
    for heading in layout.get("statblock_sections", []):
        span = _section_span(lines, heading)
        if not span:
            continue
        start, end, _level = span
        images = [index for index in range(start + 1, end) if _IMAGE.match(lines[index])]
        fences = [index for index in range(start + 1, end) if _FENCE.match(lines[index])]
        if not images or not fences:
            continue
        first_fence = fences[0]
        before = [index for index in images if index < first_fence]
        after = [index for index in images if index > first_fence]
        last_content = next((index for index in range(first_fence - 1, start, -1) if lines[index].strip()), None)
        if len(before) > 1 or after or (before and last_content != before[-1]):
            violation = before[1] if len(before) > 1 else (after[0] if after else before[0])
            findings.append(_finding(page_path, "TMPL006",
                                     f"{heading} allows one overview image directly before the statblock fence; "
                                     "move other images to the art section",
                                     line=violation + 1, section=heading))
    for heading in layout.get("containers", []):
        span = _section_span(lines, heading)
        if not span:
            continue
        start, end, level = span
        child_active = False
        for index in range(start + 1, end):
            child = _HEADING.match(lines[index])
            if child:
                child_active = len(child.group(1)) > level
            elif _IMAGE.match(lines[index]) and not child_active:
                findings.append(_finding(page_path, "TMPL007",
                                         f"{heading} images go under a subsection heading",
                                         line=index + 1, section=heading))
    return findings


def _headings(text: str) -> list[tuple[int, str]]:
    return [(len(m.group(1)), m.group(2).strip()) for m in re.finditer(r"(?m)^(#{1,6})\s+(.+?)\s*$", text)]


def check_conformance(page_path: str | Path, page_text: str, contract: TemplateContract) -> list[dict[str, Any]]:
    fields = _frontmatter(page_text)
    headings = _headings(page_text)
    findings: list[dict[str, Any]] = []
    title = fields.get("title", "")
    for section in contract.sections:
        heading = str(section["heading"]).replace("{{title}}", title)
        occurrences = [index for index, (_level, name) in enumerate(headings) if name == heading]
        when = section.get("when")
        required = section.get("required") is True or (
            isinstance(when, dict) and fields.get(when["key"], "").casefold() == when["value"])
        if required and not occurrences:
            findings.append(_finding(page_path, "TMPL_missing_required",
                                     f"Required section '{heading}' is missing", section=heading))
        if len(occurrences) > 1 and section["level"] > 1:
            findings.append(_finding(page_path, "TMPL_duplicate_section",
                                     f"Section '{heading}' appears more than once", section=heading))
        if occurrences and section["level"] > 1 and any(headings[index][0] != section["level"] for index in occurrences):
            findings.append(_finding(page_path, "TMPL_wrong_level",
                                     f"Section '{heading}' has the wrong heading level", section=heading))
    allowed = set(contract.callouts.get("allowed", []) or [])
    for match in _CALLOUT.finditer(page_text):
        callout = match.group(1).split("-", 1)[0].split("+", 1)[0].strip().casefold()
        if callout not in allowed:
            findings.append(_finding(page_path, "TMPL_disallowed_callout",
                                     f"Callout '[!{callout}]' is not in the {contract.template} template",
                                     callout=callout))
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
