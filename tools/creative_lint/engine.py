"""Creative lint orchestration across Vale and symbolic evaluators."""
from __future__ import annotations

from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
import re
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
_SKIP_DIRS = frozenset({"_archive", "_archives", "_raw", "_readouts", "_staging", "_meta", "templates", ".obsidian"})


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
            **({"warnings": list(self.warnings)} if self.warnings else {}),
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
        self.shadow_recorder = shadow_recorder or ShadowRecorder(self.root / "rules" / "shadow")

    def _expand_paths(self, paths: Iterable[str | Path] | None) -> list[Path]:
        raw_paths = list(paths or [self.vault])
        selected: list[Path] = []
        for raw in raw_paths:
            path = Path(raw)
            if not path.is_absolute():
                path = (self.root / path).resolve()
            else:
                path = path.resolve()
            if path.is_dir():
                for candidate in path.rglob("*.md"):
                    if not candidate.is_file():
                        continue
                    if _SKIP_DIRS.intersection(candidate.relative_to(path).parts):
                        continue
                    selected.append(candidate)
            elif path.is_file() and path.suffix.lower() == ".md":
                selected.append(path)
        return sorted(set(selected))

    def _rules_for(self, bundle: str | None, rule_ids: set[str] | None) -> tuple[list[tuple[RuleDefinition, str]], list[tuple[RuleDefinition, str]]]:
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
        if bundle:
            try:
                resolved = self.bundles.get(bundle).resolve(self.registry)
            except KeyError as exc:
                raise ValueError(f"unknown bundle {bundle!r}") from exc
            active = []
            for rule, severity in resolved:
                if rule.category in {"scene", "diversity"} and not rule.positive_fixtures:
                    severity = "WARN" if SEVERITY_ORDER.get(severity, 0) > SEVERITY_ORDER["WARN"] else severity
                active.append((rule, severity))
            shadow = [(rule, rule.severity) for rule in self.registry.rules if rule.lifecycle == "SHADOW"]
        else:
            active = []
            shadow = []
            for rule in self.registry.rules:
                if rule.lifecycle == "ACTIVE":
                    severity = rule.severity
                    if rule.category in {"scene", "diversity"} and not rule.positive_fixtures:
                        severity = "WARN" if SEVERITY_ORDER.get(severity, 0) > SEVERITY_ORDER["WARN"] else severity
                    active.append((rule, severity))
                elif rule.lifecycle == "SHADOW":
                    shadow.append((rule, rule.severity))
        if rule_ids is not None:
            active = [(rule, severity) for rule, severity in active if rule.id in rule_ids]
            shadow = [(rule, severity) for rule, severity in shadow if rule.id in rule_ids]
        return active, shadow

    def _applicable(self, finding: Finding, state: dict[str, Any] | None = None) -> bool:
        try:
            rule = self.registry.get(finding.rule_id)
        except KeyError:
            return True
        path = Path(str(finding.location.get("file", "")))
        if not path.is_absolute():
            path = self.root / path
        fields: dict[str, str] = {}
        text = ""
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            if text.startswith("---"):
                for line in text.splitlines()[1:]:
                    if line.strip() == "---":
                        break
                    if ":" in line and not line[:1].isspace():
                        key, value = line.split(":", 1)
                        fields[key.strip()] = value.strip().strip("\"'")
        state = state or {}
        fields.update({str(key): str(value) for key, value in state.items() if value is not None})
        lifecycle = fields.get("lifecycle", fields.get("status", "")).casefold()
        if fields.get("redirects_to") or "redirect stub" in text.casefold():
            return "redirect" not in rule.exemptions
        if fields and rule.applicability and fields.get("type") not in rule.applicability:
            return False
        if any(item.casefold() in {lifecycle, f"lifecycle:{lifecycle}"} for item in rule.exemptions if lifecycle):
            return False
        if "metadata" in rule.exemptions and not text:
            return False
        if "table" in rule.exemptions and "|" in text:
            return False
        body = text.split("---", 2)[-1]
        if "narrative" in rule.structural_scope and text.startswith("---") and not re.search(r"(?mi)^#{1,6}\s+narrative\s*$", text):
            return False
        if rule.id == "SCENE001" and not fields and re.search(r"\b(?:pressure|threat|can|must|clock|risk|choice|deadline)\b", body, re.I):
            return False
        if rule.id == "SCENE001" and re.search(r"\b(?:pressure\s+is|agenda\s+is|player\s+opening\s+is)\b", body, re.I):
            return False

        return True
    def run(self, *, bundle: str | None = None, paths: Iterable[str | Path] | None = None,
            rule_ids: set[str] | None = None, severity_filter: set[str] | None = None,
            session: int | None = None, state: dict[str, Any] | None = None) -> LintResult:
        selected = self._expand_paths(paths)
        active, shadow_rules = self._rules_for(bundle, rule_ids)
        active_ids = {rule.id for rule, _ in active}
        active_overrides = {rule.id: severity for rule, severity in active}
        warnings: list[str] = []

        vale_findings, vale_warnings = run_vale(
            selected, self.registry, root=self.root, severity_overrides=active_overrides
        )
        warnings.extend(vale_warnings)
        findings = [finding for finding in vale_findings if finding.rule_id in active_ids]
        findings.extend(evaluate_symbolic(
            selected, self.registry, root=self.root, vault=self.vault,
            rule_ids=active_ids, severity_overrides=active_overrides,
        ))
        findings = [finding for finding in findings if self._applicable(finding, state)]
        for finding in findings:
            finding.repair_class = getattr(self.registry.get(finding.rule_id), "repair_class", "diagnostic")


        active_by_id = {rule.id: rule for rule, _ in active}
        conflict_pairs: set[tuple[str, str]] = set()
        for rule in active_by_id.values():
            for other in rule.conflicts:
                if other in active_by_id:
                    conflict_pairs.add((min(rule.id, other), max(rule.id, other)))
        for left, right in sorted(conflict_pairs):
            findings.append(Finding(
                "LINT-CONFLICT", "fail", "REVIEW", {"file": "", "line": 1},
                f"Rules {left} and {right} conflict in bundle {bundle or 'all'}",
                "Conflicting rules require DM or agent precedence guidance",
                evaluator="symbolic",
            ))

        shadow_findings: list[Finding] = []
        if shadow_rules:
            shadow_ids = {rule.id for rule, _ in shadow_rules}
            shadow_overrides = {rule.id: severity for rule, severity in shadow_rules}
            shadow_findings.extend(finding for finding in vale_findings if finding.rule_id in shadow_ids)
            shadow_findings.extend(evaluate_symbolic(
                selected, self.registry, root=self.root, vault=self.vault,
                rule_ids=shadow_ids, severity_overrides=shadow_overrides,
            ))
            for finding in shadow_findings:
                finding.severity = shadow_overrides.get(finding.rule_id, finding.severity)
            if self.shadow_recorder:
                self.shadow_recorder.record(shadow_findings)

        waived = 0
        for finding in findings:
            if self.waivers:
                waiver = self.waivers.match(finding, session=session)
                if waiver:
                    finding.waiver = {
                        "rule_id": waiver.rule_id, "target": waiver.target,
                        "reason": waiver.reason, "expires": waiver.expires,
                    }
                    waived += 1
        unfiltered_findings = findings
        actionable = [finding for finding in unfiltered_findings
                      if finding.result == "fail" and finding.waiver is None]
        status = status_from_findings(actionable)
        if severity_filter:
            findings = [finding for finding in findings if finding.severity in severity_filter]
        summary = Counter({severity: 0 for severity in ("BLOCK", "REPAIR", "REVIEW", "WARN", "INFO")})
        for finding in findings:
            if finding.result == "fail" and finding.severity in summary:
                summary[finding.severity] += 1
        summary["waived"] = waived
        return LintResult(
            status=status, bundle=bundle,
            files_checked=len(selected), rules_evaluated=len(active), findings=findings,
            summary=dict(summary), shadow=shadow_findings, warnings=warnings,
        )

    def dirty_queue(self) -> dict[str, Any]:
        """Return safe automatic findings in deterministic smallest-first order."""
        result = self.run(bundle="corpus" if self.bundles else None)
        grouped: dict[str, list[Finding]] = {}
        for finding in result.findings:
            filename = str(finding.location.get("file", ""))
            if filename:
                grouped.setdefault(filename, []).append(finding)
        queue: list[dict[str, int | str]] = []
        excluded = 0
        for filename, findings in grouped.items():
            safe = []
            for finding in findings:
                if finding.result != "fail" or finding.waiver is not None or finding.repair_target is None:
                    continue
                if finding.rule_id.startswith("TMPL"):
                    safe.append(finding)
                    continue
                try:
                    auto_repair = self.registry.get(finding.rule_id).auto_repair
                except KeyError:
                    auto_repair = False
                if auto_repair:
                    safe.append(finding)
            if safe:
                path = self.root / filename
                try:
                    size = path.stat().st_size
                except OSError:
                    size = 0
                queue.append({"file": filename, "size": size, "safe_findings": len(safe)})
            else:
                excluded += 1
        queue.sort(key=lambda item: (int(item["size"]), str(item["file"])))
        return {"queue": queue, "excluded_judgment_only": excluded,
                "total_dirty": len(grouped)}

    def repair_loop(self, *, bundle: str, paths: Iterable[str | Path],
                    repair_callback: Callable[[list[Finding]], Iterable[str | Path] | bool | None],
                    max_iterations: int = 3) -> LintResult:
        current_paths = list(paths)
        result = self.run(bundle=bundle, paths=current_paths)
        initial_rule_ids = {finding.rule_id for finding in result.findings}
        for _ in range(max(0, max_iterations)):
            blocking = [
                finding for finding in result.findings
                if finding.result == "fail" and finding.severity in {"BLOCK", "REPAIR"}
                and finding.waiver is None
            ]
            if not blocking:
                return result
            changed = repair_callback(blocking)
            if changed is False or changed is None:
                break
            if changed is not True:
                current_paths = list(changed)
            result = self.run(bundle=bundle, paths=current_paths, rule_ids=initial_rule_ids)
        return result


def _cap(severity: str, ceiling: str) -> str:
    if severity not in SEVERITY_ORDER or ceiling not in SEVERITY_ORDER:
        raise ValueError(f"unknown severity {severity!r} or ceiling {ceiling!r}")
    return severity if SEVERITY_ORDER[severity] <= SEVERITY_ORDER[ceiling] else ceiling
