"""Five-level severity ordering and result status semantics."""
from __future__ import annotations

from collections.abc import Iterable

from .constants import SEVERITIES

# Larger means more action is required; min_severity therefore caps a rule.
SEVERITY_ORDER = {"INFO": 0, "WARN": 1, "REVIEW": 2, "REPAIR": 3, "BLOCK": 4}
TASTE_CATEGORIES = frozenset({"scene", "diversity"})
TASTE_CEILING = "WARN"


def min_severity(left: str, right: str) -> str:
    if left not in SEVERITY_ORDER or right not in SEVERITY_ORDER:
        raise ValueError(f"unknown severity: {left!r} or {right!r}")
    return left if SEVERITY_ORDER[left] <= SEVERITY_ORDER[right] else right


def validate_category_severity(category: str, severity: str) -> str | None:
    if category in TASTE_CATEGORIES and SEVERITY_ORDER.get(severity, -1) > SEVERITY_ORDER[TASTE_CEILING]:
        return f"{category} rules cannot exceed {TASTE_CEILING} severity (got {severity})"
    return None


def status_from_findings(findings: Iterable[object]) -> str:
    severities = {
        getattr(finding, "severity", None)
        for finding in findings
        if getattr(finding, "result", "fail") == "fail"
    }
    if severities & {"BLOCK", "REPAIR"}:
        return "repair_required"
    if "REVIEW" in severities:
        return "review_needed"
    return "clean"


def validate_severity(value: str) -> None:
    if value not in SEVERITIES:
        raise ValueError(f"invalid severity {value!r}; expected one of {sorted(SEVERITIES)}")
