"""A page's frontmatter against its `type:`'s template — the first rule
ported from the npm engine (ADR-0041), matching `utils/scripts/
lint-frontmatter-schema.mjs`'s real rule id (`W84`, see `parity.py`) and its
notion of "required key": a template's top-level frontmatter key is
required unless its own line carries a `# OPTIONAL` comment
(`utils/scripts/lint-rules/lib/templates.mjs`'s `extractRequiredKeys`,
matched here regex-for-regex).

Template resolution deliberately does NOT reproduce npm's current
behaviour: npm's resolver (`lib/templates.mjs`'s `TEMPLATES_DIR =
"_templates"`, joined against the repo root) looks for `<repo-root>/
_templates` — a path retired by "moved templates and assets to the base of
the obsidian vault" (commit 3965ec667) — so it resolves to nothing for
every real page today, a confirmed, pre-existing, out-of-scope defect (see
task-18-report.md's Concerns). This port resolves templates from their
real, current location instead: `vault/_templates/**/_<type>*.md`.

`owner_skill` carries through to the instantiated page (ADR-0044) and is
marked `# OPTIONAL` in every template, so it lands in the allowed set and
not the required one — a page written before that decision still
validates.
"""

from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register
from wiki_cli.markdown import split_frontmatter
from wiki_cli.query.schema import all_templates, resolve_template, template_keys


@register
class FrontmatterSchemaRule(FileRule):
    """Ported from npm's W84 (`utils/scripts/lint-frontmatter-schema.mjs`)."""

    id = "W84"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Add the missing key(s) with a real value, drop any key the template "
        "doesn't declare, or fix type:/subtype: if it's a typo — see the "
        "page's governing template under vault/_templates/."
    )
    producer = "wiki"
    pure = False
    """Depends on the template catalog under vault/_templates/, not just
    this file's own bytes."""
    version = "1"

    def __init__(self) -> None:
        self._templates_cache: tuple[Path, list[Path]] | None = None
        self._parsed_cache: dict[Path, tuple[frozenset[str], frozenset[str]]] = {}

    def _all_templates(self, templates_root: Path) -> list[Path]:
        if self._templates_cache is not None and self._templates_cache[0] == templates_root:
            return self._templates_cache[1]
        found = all_templates(templates_root)
        self._templates_cache = (templates_root, found)
        return found

    def _resolve_template(
        self, templates_root: Path, page_type: str, subtype: str | None
    ) -> Path | None:
        return resolve_template(
            templates_root, page_type, subtype, self._all_templates(templates_root)
        )

    def _keys_for(self, template_path: Path) -> tuple[frozenset[str], frozenset[str]]:
        cached = self._parsed_cache.get(template_path)
        if cached is not None:
            return cached
        raw = template_path.read_text(encoding="utf-8")
        fm_text, _body, _body_start = split_frontmatter(raw)
        result = template_keys(fm_text or "")
        self._parsed_cache[template_path] = result
        return result

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        page_type = page.type
        if page_type is None:
            return

        subtype_value = page.frontmatter.get("subtype")
        subtype = subtype_value if isinstance(subtype_value, str) else None

        templates_root = load_config().templates_root
        template_path = self._resolve_template(templates_root, page_type, subtype)
        if template_path is None:
            subtype_part = f' subtype:"{subtype}"' if subtype else ""
            yield self.finding(
                file=page.rel_path,
                line=1,
                message=(
                    f'No template resolves for type:"{page_type}"{subtype_part} — '
                    f"create a template under {templates_root}/, or fix the "
                    "type:/subtype: value if it's a typo"
                ),
            )
            return

        required, allowed = self._keys_for(template_path)
        present = {key for key in page.frontmatter if isinstance(key, str)}

        for key in sorted(required - present):
            yield self.finding(
                file=page.rel_path,
                line=page.line_of(key),
                message=f'Missing required frontmatter key "{key}" (see {template_path})',
            )
        for key in sorted(present - allowed):
            yield self.finding(
                file=page.rel_path,
                line=page.line_of(key),
                message=f'Unknown frontmatter key "{key}" — not declared by {template_path}',
            )
