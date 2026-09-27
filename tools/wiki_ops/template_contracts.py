"""Template-derived page contracts and conformance checks.

The page template in ``wiki/templates/`` is the only source of truth. Nothing here
names a page type, heading, or template file; editing a template changes what the
linter expects.

What a template says, and how it is read:

- Which template a page uses: the template whose frontmatter ``type`` matches the
  page's ``type`` and whose ``kind`` matches the page's ``kind``; otherwise the
  template named ``<type>.md``.
- Regions: a heading, or a standalone HTML comment whose previous non-blank line
  is not a heading. The first HTML comment that starts the region is the marker.
- Marker text inside ``<!--`` ``-->``: ``Required.``; ``Required when {key} is
  {value}.``; ``Free-form.``; starts with ``Optional`` (absence is not a finding);
  anything else is an author note.
- Job of a region: the heading the marker sits on; else each ``**Label.**`` named
  in the comment, or if none named, each following ``**Label.**``; else the next
  markdown table; else non-empty prose.
- ``{Name}`` / ``{{title}}`` in a template heading is a repeating optional pattern
  at that level under the same parent. Those page headings are not extra.
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
_LABEL = re.compile(r"^\*\*(.+?)\.\*\*")
_NAMED_LABEL = re.compile(r"\*\*(.+?)\.\*\*")
_TABLE = re.compile(r"^\s*\|")
_PLACEHOLDER = re.compile(r"(?<!\{)\{[^{}]+\}(?!\})")


@dataclass(frozen=True)
class TemplateContract:
    template: str
    type: str
    sections: list[dict[str, Any]]
    callouts: dict[str, Any]
    frontmatter: dict[str, Any] = field(default_factory=dict)
    layout: dict[str, Any] = field(default_factory=dict)
    open: bool = False
    jobs: list[dict[str, Any]] = field(default_factory=list)
    placeholders: list[dict[str, Any]] = field(default_factory=list)
    freeform: list[dict[str, Any]] = field(default_factory=list)



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


def _comment_body(line: str) -> str | None:
    match = _COMMENT_START.match(line)
    if not match:
        return None
    return match.group(1).split("-->", 1)[0].strip()


def _marker_rule(text: str) -> dict[str, Any]:
    when = _REQUIRED_WHEN.match(text)
    if when:
        return {"when": {"key": when.group(1).casefold(), "value": when.group(2).strip().casefold()}}
    if re.match(r"^Required\b", text):
        return {"required": True}
    if re.match(r"^Free-form\b", text):
        return {"freeform": True}
    if re.match(r"^Optional\b", text, re.I):
        return {"optional": True}
    return {}


def _section_rule(lines: list[str], index: int) -> dict[str, Any]:
    for line in lines[index + 1:]:
        if not line.strip():
            continue
        comment = _comment_body(line)
        if comment is None:
            return {}
        return _marker_rule(comment)
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


def _is_heading(line: str) -> bool:
    return bool(_HEADING.match(line))


def _previous_nonblank_is_heading(lines: list[str], index: int) -> bool:
    for line in reversed(lines[:index]):
        if not line.strip():
            continue
        return _is_heading(line)
    return False


def _region_end(lines: list[str], start: int) -> int:
    for index in range(start + 1, len(lines)):
        if _is_heading(lines[index]):
            return index
        comment = _comment_body(lines[index])
        if comment is not None and not _previous_nonblank_is_heading(lines, index):
            return index
    return len(lines)


def _named_labels(text: str) -> list[str]:
    return [match.group(1).strip() for match in _NAMED_LABEL.finditer(text)]


def _jobs_for_region(lines: list[str], start: int, end: int, marker: dict[str, Any],
                     heading: str | None) -> list[dict[str, Any]]:
    if marker.get("optional") or marker.get("freeform") or not marker:
        return []
    base = {key: marker[key] for key in ("required", "when") if key in marker}
    if heading:
        return [{"kind": "heading", "name": heading, **base}]
    comment = _comment_body(lines[start]) or ""
    named = _named_labels(comment)
    if named:
        return [{"kind": "label", "name": name, **base} for name in named]
    labels = []
    for line in lines[start + 1:end]:
        match = _LABEL.match(line.strip())
        if match:
            labels.append({"kind": "label", "name": match.group(1).strip(), **base})
    if labels:
        return labels
    for index in range(start + 1, end):
        if _TABLE.match(lines[index]):
            return [{"kind": "table", "name": "table", "line": index, **base}]
    for index in range(start + 1, end):
        stripped = lines[index].strip()
        if stripped and _comment_body(lines[index]) is None:
            return [{"kind": "prose", "name": "prose", **base}]
    return []


@lru_cache(maxsize=64)
def _derive(template_path: str, mtime: float) -> TemplateContract:
    text = Path(template_path).read_text(encoding="utf-8")
    fields, body = _frontmatter_text(text)
    lines = body.splitlines()
    sections: list[dict[str, Any]] = []
    jobs: list[dict[str, Any]] = []
    freeform: list[dict[str, Any]] = []
    placeholders: list[dict[str, Any]] = []

    stack: list[tuple[int, str]] = []
    statblock_sections: set[str] = set()
    containers: set[str] = set()
    current = ""
    seen_standalone: set[int] = set()
    for index, line in enumerate(lines):
        if _STATBLOCK_FENCE.match(line) and current:
            statblock_sections.add(current)
        heading = _HEADING.match(line)
        if heading:
            level, name = len(heading.group(1)), heading.group(2).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            parent = stack[-1][1] if stack else None
            rule = _section_rule(lines, index)
            section = {"heading": name, "level": level, **rule}
            sections.append(section)

            if parent:
                section["parent"] = parent
            if _PLACEHOLDER.search(name):
                section["placeholder"] = True
                placeholders.append({"heading": name, "level": level, "parent": parent})
            if rule.get("freeform"):
                freeform.append({"level": level + 1, "parent": name})
            jobs.extend(_jobs_for_region(lines, index, _region_end(lines, index), rule, name))
            stack.append((level, name))
            current = name
            if level > 1 and _is_container(lines, index, level):
                containers.add(name)
            continue
        comment = _comment_body(line)
        if comment is None or index in seen_standalone or _previous_nonblank_is_heading(lines, index):
            continue
        seen_standalone.add(index)
        marker = _marker_rule(comment)
        if marker.get("freeform"):
            parent_level, parent_name = stack[-1] if stack else (1, None)
            freeform.append({"level": parent_level + 1, "parent": parent_name})
        jobs.extend(_jobs_for_region(lines, index, _region_end(lines, index), marker, None))
    return TemplateContract(
        template=Path(template_path).name,
        type=str(fields.get("type", "")),
        sections=sections,
        callouts={"allowed": sorted({m.group(1).split("-", 1)[0].split("+", 1)[0].strip().casefold()
                                     for m in _CALLOUT.finditer(body)})},
        frontmatter=dict(fields),
        layout={"statblock_sections": sorted(statblock_sections), "containers": sorted(containers)},
        open=bool(freeform),
        jobs=jobs,
        placeholders=placeholders,
        freeform=freeform,

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


def _finding(page_path: str | Path, rule_id: str, reason: str, *,
             repair_class: str = "agent_repair", repair_target: str | None = None,
             **extra: Any) -> dict[str, Any]:
    payload = {
        "rule_id": rule_id,
        "rule": rule_id,
        "file": str(page_path),
        "severity": "REPAIR",
        "repair_class": repair_class,
        "reason": reason,
        **extra,
    }
    if repair_target:
        payload["repair_target"] = repair_target
    return payload


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
            findings.append(_finding(
                page_path, "TMPL006",
                f"{heading} allows one overview image directly before the statblock fence; "
                "move other images to the art section",
                line=violation + 1, section=heading,
                repair_target="Keep one overview image directly before the statblock fence and move the others to the template's image section",
            ))
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
                findings.append(_finding(
                    page_path, "TMPL007",
                    f"{heading} images go under a subsection heading",
                    line=index + 1, section=heading,
                    repair_target="Nest each image under the subsection heading the template shows",
                ))
    return findings


def _headings(text: str) -> list[tuple[int, str, int, str | None]]:
    rows: list[tuple[int, str, int, str | None]] = []
    stack: list[tuple[int, str]] = []
    for index, line in enumerate(text.splitlines()):
        match = _HEADING.match(line)
        if not match:
            continue
        level, name = len(match.group(1)), match.group(2).strip()
        while stack and stack[-1][0] >= level:
            stack.pop()
        parent = stack[-1][1] if stack else None
        rows.append((level, name, index + 1, parent))
        stack.append((level, name))
    return rows


def _job_required(job: dict[str, Any], fields: dict[str, str]) -> bool:
    if job.get("optional") or job.get("freeform"):
        return False
    when = job.get("when")
    if isinstance(when, dict):
        return fields.get(when["key"], "").casefold() == when["value"]
    return job.get("required") is True


def _label_present(text: str, name: str) -> bool:
    pattern = re.compile(rf"^\*\*{re.escape(name)}\.\*\*", re.M)
    return bool(pattern.search(text))


def _label_empty(text: str, name: str) -> bool:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        match = _LABEL.match(line.strip())
        if not match or match.group(1).strip() != name:
            continue
        rest = line.strip()[match.end():].strip()
        if rest and _comment_body(rest) is None:
            return False
        end = len(lines)
        for following in range(index + 1, len(lines)):
            stripped = lines[following].strip()
            if _LABEL.match(stripped) or _is_heading(lines[following]) or _comment_body(lines[following]) is not None:
                end = following
                break
        for following in range(index + 1, end):
            stripped = lines[following].strip()
            if stripped and _comment_body(lines[following]) is None:
                return False
        return True
    return False




def _heading_empty(lines: list[str], heading: str) -> bool:
    span = _section_span(lines, heading)
    if not span:
        return False
    start, end, _level = span
    for index in range(start + 1, end):
        stripped = lines[index].strip()
        if stripped and _comment_body(lines[index]) is None and not _is_heading(lines[index]):
            return False
    return True


def _placeholder_allows(contract: TemplateContract, level: int, parent: str | None, title: str) -> bool:
    for item in contract.placeholders:
        item_parent = str(item.get("parent") or "").replace("{{title}}", title) or None
        if item["level"] == level and item_parent == parent:
            return True
    return False


def _freeform_allows(contract: TemplateContract, level: int, parent: str | None, title: str) -> bool:
    for item in contract.freeform:
        item_parent = str(item.get("parent") or "").replace("{{title}}", title) or None
        if item["level"] == level and item_parent == parent:
            return True
    return False


def _has_prose(text: str) -> bool:
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or _comment_body(line) is not None or _is_heading(line):
            continue
        if _LABEL.match(stripped) or stripped.startswith(">"):
            continue
        return True
    return False



def check_conformance(page_path: str | Path, page_text: str, contract: TemplateContract) -> list[dict[str, Any]]:
    fields = _frontmatter(page_text)
    headings = _headings(page_text)
    lines = page_text.splitlines()
    findings: list[dict[str, Any]] = []
    title = fields.get("title", "")
    template = contract.template
    path = f"wiki/templates/{template}"
    named = []
    for section in contract.sections:
        heading = str(section["heading"]).replace("{{title}}", title)
        if section.get("placeholder"):
            continue
        named.append((section["level"], heading, section.get("parent")))
        occurrences = [row for row in headings if row[1] == heading]
        when = section.get("when")
        required = section.get("required") is True or (
            isinstance(when, dict) and fields.get(when["key"], "").casefold() == when["value"])
        if required and not occurrences:
            findings.append(_finding(
                page_path, "TMPL_missing_required",
                f"Required section '{heading}' is missing",
                section=heading,
                repair_target=f"Add heading {'#' * section['level']} {heading} from {path}; fill it from page facts.",
            ))
        if len(occurrences) > 1 and section["level"] > 1:
            findings.append(_finding(
                page_path, "TMPL_duplicate_section",
                f"Section '{heading}' appears more than once",
                section=heading,
                repair_target=f"Keep one '{heading}' section; fold the duplicate into it.",
            ))
        if (len(occurrences) == 1 and section["level"] > 1
                and occurrences[0][0] != section["level"]):
            findings.append(_finding(
                page_path, "TMPL_wrong_level",
                f"Section '{heading}' has the wrong heading level",
                section=heading, line=occurrences[0][2],
                repair_class="deterministic_repair",
                repair_action={
                    "kind": "set_heading_level",
                    "heading": heading,
                    "expected_level": section["level"],
                    "level": section["level"],
                },
            ))
        if required and occurrences and _heading_empty(lines, heading):
            findings.append(_finding(
                page_path, "TMPL_empty_required",
                f"Required section '{heading}' is empty",
                section=heading,
                repair_target=f"Write the required {heading} from page facts.",
            ))
    for job in contract.jobs:
        if job.get("kind") == "heading" or not _job_required(job, fields):
            continue
        name = str(job["name"])
        if job["kind"] == "label":
            if not _label_present(page_text, name):
                findings.append(_finding(
                    page_path, "TMPL_missing_job",
                    f"Required '{name}' is missing",
                    section=name,
                    repair_target=f"Add required {name} from {path}; fill it from page facts.",
                ))
            elif _label_empty(page_text, name):
                findings.append(_finding(
                    page_path, "TMPL_empty_required",
                    f"Required '{name}' is empty",
                    section=name,
                    repair_target=f"Write the required {name} from page facts.",
                ))
        elif job["kind"] == "table":
            if not any(_TABLE.match(line) for line in lines):
                findings.append(_finding(
                    page_path, "TMPL_missing_job",
                    "Required table is missing",
                    repair_target=f"Add required table from {path}; fill it from page facts.",
                ))
        elif job["kind"] == "prose":
            if not _has_prose(page_text):
                findings.append(_finding(
                    page_path, "TMPL_missing_job",
                    "Required prose is missing",
                    repair_target=f"Add required prose from {path}; fill it from page facts.",
                ))
    allowed_names = {heading for _level, heading, _parent in named}
    extras = []
    present_template: list[str] = []
    for level, name, line, parent in headings:
        if name in allowed_names:
            if level >= 2:
                present_template.append(name)
            continue
        if _freeform_allows(contract, level, parent, title) or _placeholder_allows(contract, level, parent, title):
            continue
        extras.append(name)
        findings.append(_finding(
            page_path, "TMPL002",
            f"Heading '{name}' is not in {path}",
            line=line, section=name,
            repair_target=f"Conform headings to {path}; keep page facts.",
        ))

    expected_present = [heading for _level, heading, _parent in named if heading in present_template]
    if present_template != expected_present and len(present_template) > 1:
        permutation = not extras and sorted(present_template) == sorted(expected_present)
        extra_kwargs: dict[str, Any] = {}
        if permutation:
            extra_kwargs["repair_class"] = "deterministic_repair"
            extra_kwargs["repair_action"] = {"kind": "reorder_sections", "order": expected_present}
        findings.append(_finding(
            page_path, "TMPL003",
            "Page sections do not follow the selected template order",
            repair_target="Move existing sections to template order; change no facts",
            **extra_kwargs,
        ))
    allowed = set(contract.callouts.get("allowed", []) or [])
    for match in _CALLOUT.finditer(page_text):
        callout = match.group(1).split("-", 1)[0].split("+", 1)[0].strip().casefold()
        if callout not in allowed:
            findings.append(_finding(
                page_path, "TMPL_disallowed_callout",
                f"Callout '[!{callout}]' is not in the {contract.template} template",
                callout=callout,
                repair_target="Use a callout type the template shows, or drop it.",
            ))
    findings.extend(check_layout_conformance(page_path, page_text, contract.layout))
    if fields.get("redirects_to"):
        findings.append({
            "rule_id": "TMPL_redirect_stub",
            "rule": "TMPL_redirect_stub",
            "file": str(page_path),
            "severity": "REPAIR",
            "repair_class": "deterministic_repair",
            "repair_action": "delete_redirect_stub",
            "action": "delete_redirect_stub",
            "target": fields["redirects_to"],
            "reason": "redirects_to pages are legacy stubs, not canonical entities",
        })
    return findings
