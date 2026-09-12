"""Ported from npm's W18 (`utils/scripts/lint-rules/w18-redirect-resolution.mjs`).

A redirect stub's `redirects_to:` frontmatter value must resolve to an
existing, non-stub page — a target that resolves to nothing (dangling) or
to another page that is itself a redirect stub (chained) both fire. Only
the immediate hop is checked: `redirects_to:` is a frontmatter-only value,
never parsed as a wikilink node by the engine, so it can only be resolved
against the corpus's name index, mirroring the legacy module's own
`lib/vaultIndex.mjs` lookup.

Not pure — resolution depends on the whole corpus, not just this file's
own bytes.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SCOPED_PREFIXES = ("vault/", "pcs/")
"""Legacy SCOPED_ROOTS. `pcs/` no longer exists as a real top-level dir in
this repo (PCs live under vault/campaigns/shattered-sea/pcs/) but is kept
for legacy fidelity — it never matches anything today."""

_EXCLUDED_PREFIXES = (
    "sys/",
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
)
_EXCLUDED_EXACT = "vault/campaigns/shattered-sea/dm-voice-script.md"

_WIKILINK_WRAP_RE = re.compile(r"^\[\[([^\]|#]+)")


def _redirect_target_key(raw: str) -> str:
    """Strip a `[[target|display]]`/`[[target#heading]]` wrapper down to the
    bare target, then take its last path segment — same shape as the legacy
    module's inline regex, ahead of a case-insensitive corpus lookup."""
    stripped = raw.strip()
    match = _WIKILINK_WRAP_RE.match(stripped)
    target = match.group(1) if match else stripped
    return target.split("/")[-1].strip()


def _in_scope(rel_path: str) -> bool:
    if not any(rel_path.startswith(prefix) for prefix in _SCOPED_PREFIXES):
        return False
    if any(rel_path.startswith(prefix) for prefix in _EXCLUDED_PREFIXES):
        return False
    return rel_path != _EXCLUDED_EXACT


@register
class RedirectResolutionRule(FileRule):
    """Ported from npm's W18 (`utils/scripts/lint-rules/w18-redirect-resolution.mjs`)."""

    id = "W18"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = "Repoint redirects_to: at the surviving canonical page, not a dangling target or another stub."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        if not _in_scope(page.rel_path):
            return

        target = page.frontmatter.get("redirects_to")
        if not isinstance(target, str) or not target.strip():
            return

        key = _redirect_target_key(target)
        resolved = corpus.resolve(key)

        if resolved is None:
            yield self.finding(
                file=page.rel_path,
                line=page.line_of("redirects_to"),
                message=(
                    f'redirects_to: "{target}" doesn\'t resolve to any page (dangling redirect)'
                ),
            )
            return

        if resolved.frontmatter.get("redirects_to"):
            yield self.finding(
                file=page.rel_path,
                line=page.line_of("redirects_to"),
                message=(
                    f'redirects_to: "{target}" resolves to {resolved.rel_path}, which is '
                    "itself a redirect stub (redirect chain) — point at the surviving "
                    "canonical page"
                ),
            )
