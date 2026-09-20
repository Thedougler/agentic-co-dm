"""Universal finding contract shared by every creative-lint evaluator."""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class Finding:
    rule_id: str
    result: str
    severity: str
    location: dict[str, Any]
    evidence: str
    reason: str
    evaluator: str
    repair_target: str | None = None
    waiver: dict[str, Any] | None = None
    repair_class: str = "diagnostic"
    repair_action: dict[str, Any] | None = None
    applicability: list[str] = field(default_factory=list)
    structural_scope: list[str] = field(default_factory=list)
    exemptions: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Return the stable JSON-compatible finding shape."""
        return {
            "rule_id": self.rule_id,
            "result": self.result,
            "severity": self.severity,
            "location": dict(self.location),
            "evidence": self.evidence,
            "reason": self.reason,
            "repair_target": self.repair_target,
            "repair_class": self.repair_class,
            "repair_action": dict(self.repair_action) if self.repair_action else None,
            "applicability": list(self.applicability),
            "structural_scope": list(self.structural_scope),
            "exemptions": list(self.exemptions),
            "evaluator": self.evaluator,
            "waiver": self.waiver,
        }

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Finding":
        if not isinstance(value, dict):
            raise ValueError("finding must be an object")
        required = ("rule_id", "result", "severity", "location", "evidence", "reason", "evaluator")
        missing = [key for key in required if key not in value]
        if missing:
            raise ValueError(f"finding missing required fields: {', '.join(missing)}")
        from .constants import EVALUATORS, RESULTS, SEVERITIES, is_rule_id
        if not is_rule_id(str(value["rule_id"])):
            raise ValueError(f"invalid finding rule ID: {value['rule_id']!r}")
        if value["result"] not in RESULTS:
            raise ValueError(f"invalid finding result: {value['result']!r}")
        if value["severity"] not in SEVERITIES:
            raise ValueError(f"invalid finding severity: {value['severity']!r}")
        if value["evaluator"] not in EVALUATORS:
            raise ValueError(f"invalid finding evaluator: {value['evaluator']!r}")
        location = value["location"]
        if not isinstance(location, dict) or not isinstance(location.get("file"), str):
            raise ValueError("finding location.file must be a string")
        for key in ("line", "col", "end_line", "end_col"):
            if key in location and (not isinstance(location[key], int) or location[key] < 1):
                raise ValueError(f"finding location.{key} must be a positive integer")
        return cls(
            rule_id=str(value["rule_id"]),
            result=str(value["result"]),
            severity=str(value["severity"]),
            location=dict(location),
            evidence=str(value["evidence"]),
            reason=str(value["reason"]),
            evaluator=str(value["evaluator"]),
            repair_target=value.get("repair_target"),
            waiver=value.get("waiver"),
            repair_class=str(value.get("repair_class", "diagnostic")),
            repair_action=dict(value["repair_action"]) if isinstance(value.get("repair_action"), dict) else None,
            applicability=list(value.get("applicability", [])),
            structural_scope=list(value.get("structural_scope", [])),
        )


def finding_from_rule(rule: Any, *, location: dict[str, Any], evidence: str,
                      evaluator: str, severity: str | None = None,
                      result: str = "fail") -> Finding:
    return Finding(
        rule_id=rule.id,
        result=result,
        severity=severity or rule.severity,
        location=location,
        evidence=evidence,
        reason=rule.message,
        evaluator=evaluator,
        repair_target=rule.repair,
        repair_class=getattr(rule, "repair_class", "diagnostic"),
        applicability=list(getattr(rule, "applicability", [])),
        structural_scope=list(getattr(rule, "structural_scope", [])),
        exemptions=list(getattr(rule, "exemptions", [])),
    )
