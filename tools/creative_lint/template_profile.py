"""Heading checks against the page's template: extra sections and section order.

Required sections, callouts, and image layout: tools/wiki_ops/template_contracts.py.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from .finding import Finding


def _frontmatter(text: str) -> dict[str, Any]:
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    try:
        value = yaml.safe_load(text[4:end]) or {}
    except yaml.YAMLError:
        value = {}
    return value if isinstance(value, dict) else {}


def resolve_template(page_file: str | Path, *, root: str | Path | None = None) -> Path | None:
    """Resolve the page's template from the templates' own type/kind frontmatter."""
    from tools.wiki_ops.template_contracts import template_for

    page = Path(page_file)
    base = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    metadata = _frontmatter(page.read_text(encoding="utf-8")) if page.is_file() else {}
    return template_for(base, str(metadata.get("type", "")), str(metadata.get("kind", "")))

def compare_page(page_file: str | Path, template_file: str | Path, *, root: str | Path | None = None) -> list[Finding]:
    """Wrap derive_contract + check_conformance as Finding objects."""
    from tools.wiki_ops.template_contracts import check_conformance, derive_contract

    page = Path(page_file)
    root_path = Path(root) if root is not None else Path(__file__).resolve().parents[2]
    page_text = page.read_text(encoding="utf-8")
    contract = derive_contract(template_file)
    findings: list[Finding] = []
    try:
        filename = page.resolve().relative_to(root_path.resolve()).as_posix()
    except ValueError:
        filename = page.as_posix()
    for item in check_conformance(page, page_text, contract):
        action = item.get("repair_action")
        if isinstance(action, str):
            action = {"kind": action}
        elif not isinstance(action, dict):
            action = None
        findings.append(Finding(
            rule_id=str(item.get("rule_id") or item.get("rule")),
            result="fail",
            severity=str(item.get("severity") or "REPAIR"),
            location={"file": filename, "line": max(1, int(item.get("line") or 1))},
            evidence=str(item.get("evidence") or item.get("reason") or ""),
            reason=str(item.get("reason") or ""),
            repair_target=item.get("repair_target"),
            evaluator="symbolic",
            repair_class=str(item.get("repair_class") or "agent_repair"),
            repair_action=action,
        ))
    return findings


def template_conformance(page_file: str | Path, *, root: str | Path | None = None) -> tuple[Path | None, list[Finding]]:
    page = Path(page_file)
    template = resolve_template(page, root=root)
    return template, compare_page(page, template, root=root) if template else []


compare = compare_page
