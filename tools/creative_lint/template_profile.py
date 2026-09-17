"""Runtime-derived template profiles and generic conformance checks."""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from .finding import Finding
from .registry import RuleDefinition

_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)
_CALLOUT = re.compile(r"^>\s*\[!([^\]]+)\]", re.MULTILINE)
_TABLE = re.compile(r"^\|\s*(.+?)\s*\|\s*$", re.MULTILINE)
_MARKER = re.compile(r"(?:```+([^\n]*)|\b(col(?:-md)?|flexGrow)\b)")


def _frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    try:
        value = yaml.safe_load(text[4:end])
    except yaml.YAMLError:
        return {}
    return value if isinstance(value, dict) else {}


def _marker_values(text: str) -> set[str]:
    return {value.strip() for match in _MARKER.findall(text) for value in match if value.strip()}


def _optional_from_comments(text: str, heading: str) -> bool:
    comments = " ".join(re.findall(r"<!--(.*?)-->", text, re.DOTALL)).casefold()
    heading = heading.casefold()
    return heading in comments and ("omit" in comments or "optional" in comments)


def derive_profile(template_file: str | Path) -> dict[str, Any]:
    """Extract the structural baseline directly from a template file."""
    path = Path(template_file)
    text = path.read_text(encoding="utf-8")
    metadata = _frontmatter(text)
    shape: dict[str, dict[str, Any]] = {}
    for key, value in metadata.items():
        value_type = ("boolean" if isinstance(value, bool) else "number" if isinstance(value, (int, float))
                      else "array" if isinstance(value, list) else "string")
        shape[str(key)] = {"type": value_type, "required": True}
    matches = list(_HEADING.finditer(text))
    headings = []
    for index, match in enumerate(matches):
        title = match.group(2).strip()
        next_start = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        section = text[match.end():next_start].casefold()
        optional = _optional_from_comments(text, title) or "omit" in section
        headings.append({"level": len(match.group(1)), "text": title, "optional": optional})
    tables: dict[str, list[str]] = {}
    current = ""
    for line in text.splitlines():
        heading = re.match(r"^(#{1,6})\s+(.+?)\s*$", line)
        if heading:
            current = heading.group(2).strip()
        row = _TABLE.match(line)
        if not row or not current:
            continue
        cells = [cell.strip() for cell in row.group(1).split("|")]
        if cells and not all(set(cell) <= {"-", ":", " "} for cell in cells):
            tables.setdefault(current, cells)
    return {
        "template_file": path.as_posix(),
        "frontmatter_shape": shape,
        "heading_tree": headings,
        "callout_forms": [{"type": match.group(1).strip().lower()} for match in _CALLOUT.finditer(text)],
        "table_headers": tables,
        "formatting_markers": sorted(_marker_values(text)),
    }


def resolve_template(page_file: str | Path, *, root: str | Path | None = None) -> Path | None:
    """Resolve the mapped template from a page's type/kind frontmatter."""
    page = Path(page_file)
    base = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    metadata = _frontmatter(page.read_text(encoding="utf-8"))
    kind = str(metadata.get("kind", "")).strip().casefold()
    type_name = str(metadata.get("type", "")).strip().casefold()
    mapping = {
        "session-prep": kind,
        "place": "city" if kind == "city" else "place",
        "item": "hazard" if kind == "flora hazard" else "item",
        "lore": kind if kind in {"rules", "campaign-state"} else "lore",
        "work": "dm-intelligence" if kind == "dm-intelligence" else "work",
    }
    filename = mapping.get(type_name, type_name)
    candidate = base / "wiki" / "templates" / f"{filename}.md" if filename else None
    return candidate if candidate and candidate.is_file() else None


def _rules() -> dict[str, RuleDefinition]:
    common = {"category": "wiki", "scope": "file", "severity": "REPAIR", "evaluator": "symbolic",
              "lifecycle": "ACTIVE", "vale_style": None, "tags": ["template", "structure"],
              "auto_repair": True, "conflicts": [], "depends": []}
    definitions = {
        "TMPL001": ("Missing required section", "Page is missing a section required by the selected template", "Insert the missing section stub without inventing content"),
        "TMPL002": ("Extra section", "Page contains a section not present in the selected template", "Remove or reconcile the extra structural section after review"),
        "TMPL003": ("Section order mismatch", "Page sections do not follow the selected template order", "Move the section to the template-defined order without changing facts"),
        "TMPL004": ("Frontmatter shape mismatch", "Page frontmatter does not match the selected template shape", "Add or correct structural frontmatter keys without inventing values"),
        "TMPL005": ("Formatting mismatch", "Page is missing a formatting construct required by the selected template", "Restore the template formatting construct without changing prose"),
    }
    return {key: RuleDefinition(id=key, title=title, message=message, repair=repair, **common)
            for key, (title, message, repair) in definitions.items()}


def _finding(rule_id: str, page: Path, root: Path, evidence: str, line: int,
             repair: str | None = None) -> Finding:
    rule = _rules()[rule_id]
    try:
        filename = page.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        filename = page.as_posix()
    return Finding(rule_id=rule_id, result="fail", severity=rule.severity,
                   location={"file": filename, "line": max(1, line)},
                   evidence=evidence, reason=rule.message,
                   repair_target=repair if repair is not None else rule.repair,
                   evaluator="symbolic")


def compare_page(page_file: str | Path, template_file: str | Path, *, root: str | Path | None = None) -> list[Finding]:
    """Compare a page with a derived profile; all repairs are structural-only."""
    page = Path(page_file)
    template = Path(template_file)
    root_path = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    page_text = page.read_text(encoding="utf-8")
    profile = derive_profile(template)
    page_headings = [match.group(2).strip() for match in _HEADING.finditer(page_text)
                     if len(match.group(1)) >= 2]
    expected = [item["text"] for item in profile["heading_tree"] if item["level"] >= 2 and not item["optional"]]
    findings: list[Finding] = []
    for title in expected:
        if title not in page_headings:
            findings.append(_finding("TMPL001", page, root_path, f"Missing required section: '## {title}'", 1,
                                     f"Insert '## {title}' section stub after the title heading"))
    template_headings = [item["text"] for item in profile["heading_tree"] if item["level"] >= 2]
    extras = [title for title in page_headings if title not in template_headings]
    for title in extras:
        line = next((index for index, text in enumerate(page_text.splitlines(), 1)
                     if re.match(r"^#{2,6}\s+" + re.escape(title) + r"\s*$", text)), 1)
        findings.append(_finding("TMPL002", page, root_path, f"Extra section: '{title}'", line))
    present = [title for title in page_headings if title in template_headings]
    expected_present = [title for title in template_headings if title in present]
    if present != expected_present and len(present) > 1:
        findings.append(_finding("TMPL003", page, root_path, "Section order differs from selected template", 1))
    metadata = _frontmatter(page_text)
    missing = [key for key, shape in profile["frontmatter_shape"].items()
               if shape["required"] and key not in metadata]
    if missing:
        findings.append(_finding("TMPL004", page, root_path,
                                 "Missing template frontmatter keys: " + ", ".join(missing), 1))
    template_markers = {marker for marker in profile["formatting_markers"] if marker in {"col", "col-md", "flexGrow"}}
    if template_markers and not (template_markers & _marker_values(page_text)):
        findings.append(_finding("TMPL005", page, root_path, "Missing template formatting marker", 1))
    expected_callouts = {item["type"] for item in profile["callout_forms"]}
    actual_callouts = {match.group(1).strip().lower() for match in _CALLOUT.finditer(page_text)}
    for callout in sorted(expected_callouts - actual_callouts):
        findings.append(_finding("TMPL005", page, root_path, f"Missing callout form: {callout}", 1))
    return findings


def template_conformance(page_file: str | Path, *, root: str | Path | None = None) -> tuple[Path | None, list[Finding]]:
    page = Path(page_file)
    template = resolve_template(page, root=root)
    return template, compare_page(page, template, root=root) if template else []


profile_from_template = derive_profile
compare = compare_page
