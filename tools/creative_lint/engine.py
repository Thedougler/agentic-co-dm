"""Creative lint orchestration across Vale and symbolic evaluators."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Callable, Iterable

from .bundles import BundleRegistry, GATES
from .finding import Finding
from .registry import Registry, RuleDefinition
from .severity import SEVERITY_ORDER, status_from_findings
from .shadow import ShadowRecorder
from .vale_adapter import run_vale
from .waivers import WaiverRegistry
from .evaluators.symbolic import evaluate_symbolic

ROOT = Path(__file__).resolve().parents[2]


@dataclass(slots=True)
class LintResult:
    status: str
    bundle: str | None
    files_checked: int
    rules_evaluated: int
    findings: list[Finding] = field(default_factory=list)
    summary: dict[str, int] = field(default_factory=dict)
    shadow: list[Finding] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "bundle": self.bundle,
            "files_checked": self.files_checked,
            "rules_evaluated": self.rules_evaluated,
            "findings": [finding.to_dict() for finding in self.findings],
            "summary": dict(self.summary),
            "shadow": [finding.to_dict() for finding in self.shadow],
            **({"warnings": self.warnings} if self.warnings else {}),
        }


class LintEngine:
    def __init__(self, registry: Registry, bundles: BundleRegistry | None = None, *, root: Path | None = None,
                 vault: Path | None = None, waivers: WaiverRegistry | None = None,
                 shadow_recorder: ShadowRecorder | None = None):
        self.registry = registry
        self.bundles = bundles
        self.root = (root or ROOT).resolve()
        self.vault = (vault or self.root / "wiki").resolve()
        self.waivers = waivers
        self.shadow_recorder = shadow_recorder

    def _expand_paths(self, paths: Iterable[str | Path] | None) -> list[Path]:
        raw_paths = list(paths or [self.vault])
        selected: list[Path] = []
        skip_dirs = {"_archive", "_archives", "_raw", "_readouts", "_staging", "_meta", "templates", ".obsidian"}
        for raw in raw_paths:
            path = Path(raw)
            if not path.is_absolute():
                path = (Path.cwd() / path).resolve()
            if path.is_dir():
                selected.extend(sorted(
                    p for p in path.rglob("*.md")
                    if p.is_file() and not set(p.relative_to(path).parts) & skip_dirs
                ))
            elif path.is_file() and path.suffix.lower() == ".md":
                selected.append(path)
        return sorted(set(selected))

    def _rules_for(self, bundle: str | None, rule_ids: set[str] | None) -> tuple[list[tuple[RuleDefinition, str]], list[RuleDefinition]]:
        if bundle:
            if self.bundles is None:
                raise ValueError("bundle registry is not configured")
            definition = self.bundles.get(bundle)
            categories: dict[str, str] = {}
            for gate in ("block", "review", "diagnostics"):
                for category in getattr(definition, gate) or []:
                    if category in categories:
                        raise ValueError(f"bundle {bundle} places category {category} more than once")
                    categories[category] = GATES[gate]
            active = [(rule, _cap(rule.severity, categories[rule.category]))
                      for rule in self.registry.rules
                      if rule.lifecycle == "ACTIVE" and rule.category in categories]
            shadow = [rule for rule in self.registry.rules if rule.lifecycle == "SHADOW" and rule.category in categories]
        else:
            active = [(rule, rule.severity) for rule in self.registry.rules if rule.lifecycle == "ACTIVE"]
            shadow = [rule for rule in self.registry.rules if rule.lifecycle == "SHADOW"]
        if rule_ids is not None:
            active = [(rule, severity) for rule, severity in active if rule.id in rule_ids]
            shadow = [rule for rule in shadow if rule.id in rule_ids]
        return active, shadow

    def run(self, *, bundle: str | None = None, paths: Iterable[str | Path] | None = None,
            rule_ids: set[str] | None = None, severity_filter: set[str] | None = None,
            session: int | None = None) -> LintResult:
        selected = self._expand_paths(paths)
        active, shadow_rules = self._rules_for(bundle, rule_ids)
        active_ids = {rule.id for rule, _ in active}
        severity_overrides = {rule.id: severity for rule, severity in active}
        warnings: list[str] = []
        vale_findings, vale_warnings = run_vale(
            [path for path in selected if path.suffix.lower() == ".md"], self.registry,
            root=self.root, severity_overrides=severity_overrides)
        warnings.extend(vale_warnings)
        findings = [finding for finding in vale_findings if finding.rule_id in active_ids]
        symbolic_findings = evaluate_symbolic(selected, self.registry, root=self.root, vault=self.vault,
                                              rule_ids=active_ids, severity_overrides=severity_overrides)
        for finding in symbolic_findings:
            finding.severity = severity_overrides.get(finding.rule_id, finding.severity)
        findings.extend(symbolic_findings)
        # Rules requiring unavailable semantic/human services abstain explicitly.
        evaluated_ids = {finding.rule_id for finding in findings}
        for rule, severity in active:
            if rule.evaluator in {"semantic", "human", "retrieval"} and rule.id not in evaluated_ids:
                findings.append(Finding(rule_id=rule.id, result="abstain", severity=severity,
                                        location={"file": "", "line": 1}, evidence="evaluator_unavailable",
                                        reason=rule.message, repair_target=rule.repair, evaluator=rule.evaluator))
        # Conflicts are surfaced instead of selecting a creative winner.
        active_by_id = {rule.id: rule for rule, _ in active}
        conflict_pairs = set()
        for rule in active_by_id.values():
            for other in rule.conflicts:
                if other in active_by_id:
                    conflict_pairs.add(tuple(sorted((rule.id, other))))
        for left, right in sorted(conflict_pairs):
            findings.append(Finding("LINT-CONFLICT", "fail", "REVIEW", {"file": "", "line": 1},
                                    f"Rules {left} and {right} conflict in bundle {bundle or 'all'}",
                                    "Conflicting rules require DM or agent precedence guidance",
                                    evaluator="symbolic"))
        # SHADOW findings are evaluated and recorded but never enter active output.
        shadow_findings: list[Finding] = []
        if shadow_rules:
            shadow_ids = {rule.id for rule in shadow_rules}
            shadow_findings = [finding for finding in vale_findings if finding.rule_id in shadow_ids]
            symbolic_shadow = evaluate_symbolic(selected, self.registry, root=self.root, vault=self.vault,
                                                rule_ids=shadow_ids)
            shadow_findings.extend(symbolic_shadow)
            if self.shadow_recorder:
                self.shadow_recorder.record(shadow_findings)
        waived = 0
        for finding in findings:
            if self.waivers:
                waiver = self.waivers.match(finding, session=session)
                if waiver:
                    finding.waiver = {"rule_id": waiver.rule_id, "target": waiver.target,
                                      "reason": waiver.reason, "expires": waiver.expires}
                    waived += 1
        if severity_filter:
            findings = [finding for finding in findings if finding.severity in severity_filter]
        summary = Counter({severity: 0 for severity in ("BLOCK", "REPAIR", "REVIEW", "WARN", "INFO")})
        for finding in findings:
            if finding.result == "fail":
                summary[finding.severity] += 1
        summary["waived"] = waived
        actionable = [finding for finding in findings if finding.result == "fail" and finding.waiver is None]
        return LintResult(status=status_from_findings(actionable), bundle=bundle,
                          files_checked=len(selected), rules_evaluated=len(active), findings=findings,
                          summary=dict(summary), shadow=shadow_findings, warnings=warnings)

    def repair_loop(self, *, bundle: str, paths: Iterable[str | Path],
                    repair_callback: Callable[[list[Finding]], Iterable[str | Path] | bool | None],
                    max_iterations: int = 3) -> LintResult:
        current_paths = list(paths)
        result = self.run(bundle=bundle, paths=current_paths)
        for _ in range(max(0, max_iterations)):
            blocking = [finding for finding in result.findings
                        if finding.result == "fail" and finding.severity in {"BLOCK", "REPAIR"}
                        and finding.waiver is None]
            if not blocking:
                return result
            changed = repair_callback(blocking)
            if changed is False or changed is None:
                break
            if changed is not True:
                current_paths = list(changed)
            result = self.run(bundle=bundle, paths=current_paths)
        return result


def _cap(severity: str, ceiling: str) -> str:
    return severity if SEVERITY_ORDER[severity] <= SEVERITY_ORDER[ceiling] else ceiling
