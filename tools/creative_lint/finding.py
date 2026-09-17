"""Universal finding contract shared by every creative-lint evaluator."""
from __future__ import annotations

from dataclasses import dataclass
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
            "evaluator": self.evaluator,
            "waiver": self.waiver,
        }

    @classmethod
    def from_dict(cls, value: dict[str, Any]) -> "Finding":
        required = ("rule_id", "result", "severity", "location", "evidence", "reason", "evaluator")
        missing = [key for key in required if key not in value]
        if missing:
            raise ValueError(f"finding missing required fields: {', '.join(missing)}")
        return cls(
            rule_id=str(value["rule_id"]),
            result=str(value["result"]),
            severity=str(value["severity"]),
            location=dict(value["location"]),
            evidence=str(value["evidence"]),
            reason=str(value["reason"]),
            evaluator=str(value["evaluator"]),
            repair_target=value.get("repair_target"),
            waiver=value.get("waiver"),
        )


def finding_from_rule(rule: Any, *, location: dict[str, Any], evidence: str,
                      evaluator: str, severity: str | None = None,
                      result: str = "fail") -> Finding:
    """Construct a finding from a RuleDefinition-like object."""
    return Finding(
        rule_id=rule.id,
        result=result,
        severity=severity or rule.severity,
        location=location,
        evidence=evidence,
        reason=rule.message,
        repair_target=rule.repair,
        evaluator=evaluator,
    )
