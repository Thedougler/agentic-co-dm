# Vale Style Contract

**Branch**: `024-creative-linting` | **Date**: 2026-09-17

## Style Package: `CoDM`

Custom Vale style for the agentic-co-dm creative linter. Each rule is one YAML file at `styles/CoDM/<ID>.yml`.

### Configuration (`.vale.ini`)

The repository `.vale.ini` is the sole Vale package and scope authority. The linter MUST pass this file to Vale and MUST NOT duplicate its package list in `rules/registry.yml`, `package.json`, or Python code.

```ini
StylesPath = styles
MinAlertLevel = suggestion
Packages = ai-tells, proselint, Readability, Harper

[wiki/*.md]
BasedOnStyles = CoDM, ai-tells, proselint, Readability, Harper

[wiki/_raw/*.md]
BasedOnStyles =

[wiki/_staging/*.md]
BasedOnStyles = ai-tells, proselint

[wiki/_archive/*.md]
BasedOnStyles =

[tests/fixtures/creative_lint/**/*.md]
BasedOnStyles = CoDM

[wiki/templates/*.md]
BasedOnStyles =
```

The `wiki/` scope inherits the installed packages plus the custom `CoDM` style. Raw and archive pages are excluded; staging intentionally keeps only the configured prose packages; creative fixtures run the custom rule style without applying unrelated prose packages. Scope exclusions match existing `lint_wiki.py` `SKIP_DIRS` where applicable.

### Rule File Convention

Each Vale rule file MUST:
1. Be named `<RULE_ID>.yml` (e.g., `AGENCY001.yml`)
2. Use a Vale extension point (`extends: existence|substitution|conditional|occurrence|script`)
3. Set `message` to include the rule ID for traceability
4. Set `level` to the closest Vale equivalent of the registry severity (for Vale's own filtering)
5. Set `scope` appropriately for the rule's target (e.g., `text` for body content, `raw` for full file)

### Severity Mapping (Vale level assignment)

Vale has three levels. Map to the closest for Vale's internal filtering — the Python orchestrator uses the registry severity as authoritative.

| Registry severity | Vale level |
|---|---|
| BLOCK | `error` |
| REPAIR | `error` |
| REVIEW | `warning` |
| WARN | `suggestion` |
| INFO | `suggestion` |

### Invocation

The Python orchestrator calls Vale as:

```bash
vale --output=JSON --config=.vale.ini [files...]
```

For bundle-scoped runs, the orchestrator determines which files to pass based on path arguments. Vale's glob-based configuration in `.vale.ini` handles style application.

### Custom Vale Vocab (optional)

If needed, `styles/config/vocabularies/CoDM/` can define accept/reject word lists for consistency checks. Not required for Phase 1.
