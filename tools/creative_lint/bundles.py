"""Task-specific rule bundle loading and severity gates."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from .constants import CATEGORIES
from .registry import Registry, RuleDefinition
from .severity import min_severity

GATES = {"block": "BLOCK", "review": "REVIEW", "diagnostics": "WARN"}


@dataclass(frozen=True, slots=True)
class BundleDefinition:
    name: str
    description: str = ""
    block: list[str] | None = None
    review: list[str] | None = None
    diagnostics: list[str] | None = None

    def __post_init__(self) -> None:
        for field_name in ("block", "review", "diagnostics"):
            if getattr(self, field_name) is None:
                object.__setattr__(self, field_name, [])

    def resolve(self, registry: Registry) -> list[tuple[RuleDefinition, str]]:
        categories: dict[str, str] = {}
        for gate, category_names in (("block", self.block), ("review", self.review), ("diagnostics", self.diagnostics)):
            for category in category_names or []:
                if category in categories:
                    raise ValueError(f"bundle {self.name} places category {category} more than once")
                if category not in CATEGORIES:
                    raise ValueError(f"bundle {self.name} contains unknown category {category}")
                categories[category] = GATES[gate]
        return [
            (rule, min_severity(rule.severity, categories[rule.category]))
            for rule in registry.rules
            if rule.lifecycle == "ACTIVE" and rule.category in categories
        ]

    def categories(self) -> set[str]:
        return set(self.block or []) | set(self.review or []) | set(self.diagnostics or [])


class BundleRegistry:
    def __init__(self, bundles: list[BundleDefinition], *, path: Path | None = None):
        self.bundles = {bundle.name: bundle for bundle in bundles}
        self.path = path

    @classmethod
    def load(cls, path: str | Path) -> "BundleRegistry":
        path = Path(path)
        try:
            raw = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (OSError, yaml.YAMLError) as exc:
            raise ValueError(f"could not load bundles {path}: {exc}") from exc
        raw = raw or {}
        entries = raw.get("bundles", raw) if isinstance(raw, dict) else raw
        if isinstance(entries, list):
            names: set[str] = set()
            mapped: dict[str, Any] = {}
            for item in entries:
                if not isinstance(item, dict) or not item.get("name"):
                    raise ValueError("each bundle entry must contain a name")
                name = str(item["name"])
                if name in names:
                    raise ValueError(f"duplicate bundle name {name}")
                names.add(name)
                mapped[name] = item
            entries = mapped
        if not isinstance(entries, dict):
            raise ValueError("bundle registry must contain a mapping under 'bundles'")
        bundles: list[BundleDefinition] = []
        for name, value in entries.items():
            if not isinstance(value, dict):
                raise ValueError(f"bundle {name} must be a mapping")
            bundles.append(BundleDefinition(
                name=str(name), description=str(value.get("description", "")),
                block=[str(x) for x in value.get("block", []) or []],
                review=[str(x) for x in value.get("review", []) or []],
                diagnostics=[str(x) for x in value.get("diagnostics", []) or []],
            ))
        registry = cls(bundles, path=path)
        errors = registry.validate()
        if errors:
            raise ValueError("invalid bundle registry:\n" + "\n".join(errors))
        return registry

    def get(self, name: str) -> BundleDefinition:
        try:
            return self.bundles[name]
        except KeyError as exc:
            raise KeyError(f"unknown bundle {name}; available: {', '.join(self.available())}") from exc

    def available(self) -> list[str]:
        return sorted(self.bundles)

    def memberships(self, category: str) -> list[tuple[str, str]]:
        return [
            (name, gate)
            for name, bundle in self.bundles.items()
            for gate in ("block", "review", "diagnostics")
            if category in (getattr(bundle, gate) or [])
        ]

    def validate(self) -> list[str]:
        errors: list[str] = []
        for bundle in self.bundles.values():
            locations: dict[str, str] = {}
            for gate in ("block", "review", "diagnostics"):
                for category in getattr(bundle, gate) or []:
                    if category not in CATEGORIES:
                        errors.append(f"bundle {bundle.name}: invalid category {category!r}")
                    if category in locations:
                        errors.append(
                            f"bundle {bundle.name}: category {category} appears in "
                            f"{locations[category]} and {gate}"
                        )
                    locations[category] = gate
        return errors
