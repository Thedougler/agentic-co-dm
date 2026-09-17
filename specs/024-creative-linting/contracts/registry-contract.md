# Registry Contract

**Branch**: `024-creative-linting` | **Date**: 2026-09-17

## Rule Registry (`rules/registry.yml`)

The registry is the single source of truth for all rule metadata (FR-012). Skills, `AGENTS.md`, and agent prompts reference rules by ID — they MUST NOT duplicate rule logic or prose.

### Loading

```python
from tools.creative_lint.registry import Registry

registry = Registry.load("rules/registry.yml")
rule = registry.get("AGENCY001")       # RuleDefinition or KeyError
rules = registry.by_category("agency") # list[RuleDefinition]
rules = registry.active()              # lifecycle == ACTIVE only
```

### Validation (on load)

1. Parse YAML via PyYAML
2. For each entry, validate required fields: `id`, `title`, `category`, `scope`, `severity`, `evaluator`, `lifecycle`, `message`
3. Reject duplicate IDs (error with both entries identified)
4. Validate `id` format: `^[A-Z]+\d{3}$`
5. Validate enums: `category`, `scope`, `severity`, `evaluator`, `lifecycle`
6. Enforce severity ceiling: `category in (scene, diversity)` → `severity <= WARN`
7. Validate `vale_style` file exists when `evaluator: vale`
8. Validate `conflicts` and `depends` reference valid IDs (warning, not error)

### API

```python
@dataclass
class RuleDefinition:
    id: str
    title: str
    category: str          # wiki|canon|temporal|agency|retrieval|scene|diversity
    scope: str             # content|frontmatter|corpus|file
    severity: str          # BLOCK|REPAIR|REVIEW|WARN|INFO
    evaluator: str         # vale|symbolic|retrieval|semantic|human
    lifecycle: str         # DRAFT|SHADOW|ACTIVE
    message: str
    vale_style: str | None
    repair: str | None
    tags: list[str]
    auto_repair: bool          # true for safe automatic repairs (dirty-file queue inclusion)
    conflicts: list[str]
    depends: list[str]

class Registry:
    @classmethod
    def load(cls, path: str | Path) -> "Registry": ...
    def get(self, rule_id: str) -> RuleDefinition: ...
    def by_category(self, category: str) -> list[RuleDefinition]: ...
    def by_evaluator(self, evaluator: str) -> list[RuleDefinition]: ...
    def active(self) -> list[RuleDefinition]: ...
    def shadow(self) -> list[RuleDefinition]: ...
    def all_ids(self) -> set[str]: ...
    def validate(self) -> list[str]:
        """Return list of validation errors. Empty = valid."""
```

## Bundle Registry (`rules/bundles.yml`)

### Loading

```python
from tools.creative_lint.bundles import BundleRegistry

bundles = BundleRegistry.load("rules/bundles.yml")
bundle = bundles.get("session-prep")  # BundleDefinition or KeyError
rules = bundle.resolve(registry)      # list[tuple[RuleDefinition, effective_severity]]
```

### API

```python
@dataclass
class BundleDefinition:
    name: str
    description: str
    block: list[str]       # categories at BLOCK gate
    review: list[str]      # categories at REVIEW gate
    diagnostics: list[str] # categories at WARN gate

    def resolve(self, registry: Registry) -> list[tuple[RuleDefinition, str]]:
        """Resolve to (rule, effective_severity) pairs.
        Effective severity = min(rule.severity, gate_ceiling).
        Only ACTIVE rules included. SHADOW rules recorded separately."""
```
