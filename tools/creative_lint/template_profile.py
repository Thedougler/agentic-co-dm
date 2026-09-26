"""Heading checks against the page's template: extra sections and section order.

Required sections, callouts, and image layout: tools/wiki_ops/template_contracts.py.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import yaml

from .finding import Finding
from .registry import RuleDefinition

_HEADING = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


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


def resolve_template(page_file: str | Path, *, root: str | Path | None = None) -> Path | None:
    """Resolve the page's template from the templates' own type/kind frontmatter."""
    from tools.wiki_ops.template_contracts import template_for

    page = Path(page_file)
    base = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    metadata = _frontmatter(page.read_text(encoding="utf-8"))
    return template_for(base, str(metadata.get("type", "")), str(metadata.get("kind", "")))


def _rules() -> dict[str, RuleDefinition]:
    common = {"category": "wiki", "scope": "file", "severity": "REPAIR", "evaluator": "symbolic",
              "lifecycle": "ACTIVE", "vale_style": None, "tags": ["template", "structure"],
              "auto_repair": False, "conflicts": [], "depends": []}
    definitions = {
        "TMPL002": ("Extra section", "Page contains a section not present in the selected template", "Rename the section to the template heading that holds its job, or fold it into that section"),
        "TMPL003": ("Section order mismatch", "Page sections do not follow the selected template order", "Move the section to the template-defined order without changing facts"),
        "TMPL006": ("Statblock image layout", "Statblock allows at most one overview image immediately before the statblock fence; remaining images belong in Art subsections", "Keep at most one overview image before the statblock fence and move remaining images to Art subsections"),
        "TMPL007": ("Art subsection structure", "Art embeds are not nested under a subsection heading", "Nest each Art embed under a role subsection"),
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
    """Compare page headings with the template's: extra sections and section order."""
    from tools.wiki_ops.template_contracts import derive_contract

    page = Path(page_file)
    root_path = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    page_text = page.read_text(encoding="utf-8")
    contract = derive_contract(template_file)
    page_title = str(_frontmatter(page_text).get("title", "")).strip()
    template_headings = [str(item["heading"]).replace("{{title}}", page_title)
                         for item in contract.sections if item["level"] >= 2]
    page_headings = [match.group(2).strip() for match in _HEADING.finditer(page_text)
                     if len(match.group(1)) >= 2]
    findings: list[Finding] = []
    if not contract.open:
        for title in page_headings:
            if title in template_headings:
                continue
            line = next((index for index, text in enumerate(page_text.splitlines(), 1)
                         if re.match(r"^#{2,6}\s+" + re.escape(title) + r"\s*$", text)), 1)
            findings.append(_finding("TMPL002", page, root_path, f"Extra section: '{title}'", line))
    present = [title for title in page_headings if title in template_headings]
    expected_present = [title for title in template_headings if title in present]
    if present != expected_present and len(present) > 1:
        findings.append(_finding("TMPL003", page, root_path, "Section order differs from selected template", 1))
    return findings


def template_conformance(page_file: str | Path, *, root: str | Path | None = None) -> tuple[Path | None, list[Finding]]:
    page = Path(page_file)
    template = resolve_template(page, root=root)
    return template, compare_page(page, template, root=root) if template else []


compare = compare_page
