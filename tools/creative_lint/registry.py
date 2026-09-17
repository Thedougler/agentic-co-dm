"""Repository-owned rule registry and validation."""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from .constants import CATEGORIES, EVALUATORS, LIFECYCLES, RULE_ID_RE, SCOPES, SEVERITIES
from .severity import validate_category_severity

_REQUIRED = ("id", "title", "category", "scope", "severity", "evaluator", "lifecycle", "message")


@dataclass(frozen=True, slots=True)
class RuleDefinition:
    id: str
    title: str
    category: str
    scope: str
    severity: str
    evaluator: str
    lifecycle: str
    message: str
    vale_style: str | None = None
    repair: str | None = None
    tags: list[str] = field(default_factory=list)
    auto_repair: bool = False
    conflicts: list[str] = field(default_factory=list)
    depends: list[str] = field(default_factory=list)
    applicability: list[str] = field(default_factory=list)
    structural_scope: list[str] = field(default_factory=list)
    exemptions: list[str] = field(default_factory=list)
    repair_class: str = "diagnostic"
    positive_fixtures: list[str] = field(default_factory=list)

    @classmethod
    def from_mapping(cls, value: dict[str, Any]) -> "RuleDefinition":
        lists: dict[str, list[str]] = {}
        for key in ("tags", "conflicts", "depends", "applicability", "structural_scope", "exemptions", "positive_fixtures"):
            raw = value.get(key, [])
            if raw is None:
                raw = []
            if not isinstance(raw, list):
                raise ValueError(f"rule {value.get('id', '<unknown>')}: {key} must be a list")
            lists[key] = [str(item) for item in raw]
        auto_repair = value.get("auto_repair", False)
        if not isinstance(auto_repair, bool):
            raise ValueError(f"rule {value.get('id', '<unknown>')}: auto_repair must be boolean")
        repair_class = str(value.get("repair_class", "diagnostic"))
        if repair_class not in {"diagnostic", "human_repair", "deterministic_repair"}:
            raise ValueError(f"rule {value.get('id', '<unknown>')}: invalid repair_class")
        return cls(
            id=str(value["id"]), title=str(value["title"]), category=str(value["category"]),
            scope=str(value["scope"]), severity=str(value["severity"]),
            evaluator=str(value["evaluator"]), lifecycle=str(value["lifecycle"]),
            message=str(value["message"]), vale_style=value.get("vale_style"),
            repair=value.get("repair"), tags=lists["tags"], auto_repair=auto_repair,
            conflicts=lists["conflicts"], depends=lists["depends"],
            applicability=lists["applicability"], structural_scope=lists["structural_scope"],
            exemptions=lists["exemptions"], repair_class=repair_class,
            positive_fixtures=lists["positive_fixtures"],
        )
class Registry:
    def __init__(self, rules: list[RuleDefinition], *, path: Path | None = None):
        self.rules = list(rules)
        self.path = path

    @classmethod
    def load(cls, path: str | Path) -> "Registry":
        path = Path(path)
        try:
            raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            raise ValueError(f"could not load rule registry {path}: {exc}") from exc
        if raw is None:
            raw = []
        entries = raw.get("rules", raw) if isinstance(raw, dict) else raw
        if isinstance(entries, dict):
            entries = [dict(value, id=key) if isinstance(value, dict) and "id" not in value else value
                       for key, value in entries.items()]
        if not isinstance(entries, list):
            raise ValueError("rule registry must contain a list under 'rules'")
        try:
            rules = [RuleDefinition.from_mapping(item) for item in entries]
        except (TypeError, ValueError) as exc:
            raise ValueError(f"invalid rule registry: {exc}") from exc
        registry = cls(rules, path=path)
        errors = registry.validate()
        fatal = [error for error in errors if not error.startswith("warning:")]
        if fatal:
            raise ValueError("invalid rule registry:\n" + "\n".join(fatal))
        return registry

    def get(self, rule_id: str) -> RuleDefinition:
        for rule in self.rules:
            if rule.id == rule_id:
                return rule
        raise KeyError(rule_id)

    def by_category(self, category: str) -> list[RuleDefinition]:
        return [rule for rule in self.rules if rule.category == category]

    def by_evaluator(self, evaluator: str) -> list[RuleDefinition]:
        return [rule for rule in self.rules if rule.evaluator == evaluator]

    def active(self) -> list[RuleDefinition]:
        return [rule for rule in self.rules if rule.lifecycle == "ACTIVE"]

    def shadow(self) -> list[RuleDefinition]:
        return [rule for rule in self.rules if rule.lifecycle == "SHADOW"]

    def all_ids(self) -> set[str]:
        return {rule.id for rule in self.rules}

    def validate(self) -> list[str]:
        errors: list[str] = []
        seen: dict[str, int] = {}
        for index, rule in enumerate(self.rules):
            if rule.id in seen:
                errors.append(f"duplicate rule ID {rule.id} at entries {seen[rule.id]} and {index}")
            seen[rule.id] = index
            if not RULE_ID_RE.fullmatch(rule.id):
                errors.append(f"invalid rule ID {rule.id!r}; expected CATEGORY###")
            if rule.category not in CATEGORIES:
                errors.append(f"{rule.id}: invalid category {rule.category!r}")
            if rule.scope not in SCOPES:
                errors.append(f"{rule.id}: invalid scope {rule.scope!r}")
            if rule.severity not in SEVERITIES:
                errors.append(f"{rule.id}: invalid severity {rule.severity!r}")
            if rule.evaluator not in EVALUATORS:
                errors.append(f"{rule.id}: invalid evaluator {rule.evaluator!r}")
            if rule.lifecycle not in LIFECYCLES:
                errors.append(f"{rule.id}: invalid lifecycle {rule.lifecycle!r}")
            if rule.evaluator == "vale":
                if not rule.vale_style:
                    errors.append(f"{rule.id}: vale_style is required for Vale rules")
                else:
                    style = str(rule.vale_style)
                    if not style.endswith(".yml"):
                        style += ".yml"
                    if self.path:
                        root = self.path.parent.parent if self.path.parent.name == "rules" else self.path.parent
                    else:
                        root = Path.cwd()
                    if not (root / "styles" / style).is_file():
                        errors.append(f"{rule.id}: Vale style does not exist: {rule.vale_style}")
            taste_error = validate_category_severity(rule.category, rule.severity)
            if taste_error:
                errors.append(f"{rule.id}: {taste_error}")
        ids = self.all_ids()
        for rule in self.rules:
            for ref in (*rule.conflicts, *rule.depends):
                if ref not in ids:
                    errors.append(f"warning: {rule.id}: unresolved rule reference {ref}")
        return errors
