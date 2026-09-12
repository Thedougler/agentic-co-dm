"""Ported from npm's W57 (`utils/scripts/lint-rules/w57-duplicate-basename.mjs`).

Two or more `.md` files anywhere under `vault/` share the exact same
basename in different directories. Obsidian's wikilink resolution is
basename-based, so a bare `[[slug]]` link to either file is genuinely
ambiguous. DETECTION only — which file to rename, and to what, is a
judgment call the legacy module explicitly declines to make.

A `VaultRule`, not a `FileRule`: the collision can only be seen by scanning
the whole corpus at once, not one page at a time.

Exemptions ported verbatim from the legacy module's documented exclusions:
dotdirs/`raw/`/`inbox/` path segments, the ungoverned-campaign-material
prefixes (stories, ideas, PC combat-profile/character-sheets, the
recreated-craft `vault/refs/ideas/` home), the single dm-voice-script.md
exact path, and the three "repeats by design, always linked
path-qualified" shapes: the per-session file scaffold
(`vault/episodes/<dir>/<file>.md`), a content-type's own
`GUIDE.md`/`checklist.md` pair, and the `references/`/`_common/` material
beside it.

Not pure — the finding depends on every other page in the corpus, not just
this file's own bytes.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register

_UNGOVERNED_PREFIXES = (
    "vault/stories/",
    "vault/ideas/",
    "vault/campaigns/shattered-sea/pcs/combat-profile/",
    "vault/campaigns/shattered-sea/pcs/character-sheets/",
    "vault/refs/ideas/",
)
_EXCLUDED_EXACT = "vault/campaigns/shattered-sea/dm-voice-script.md"

_SESSION_SCAFFOLD_RE = re.compile(r"^vault/episodes/[^/]+/[^/]+\.md$")
_DRAFT_GUIDE_RE = re.compile(r"^vault/refs/.*/(GUIDE|checklist)\.md$")
_DRAFT_REFERENCE_RE = re.compile(r"^vault/refs/vault/(_common|.*/references)/[^/]+\.md$")
_EXEMPT_RES = (_SESSION_SCAFFOLD_RE, _DRAFT_GUIDE_RE, _DRAFT_REFERENCE_RE)


def _is_governed(rel_path: str) -> bool:
    if not rel_path.startswith("vault/"):
        return False
    # Subtree instruction files share their basename by convention.
    if rel_path.rsplit("/", 1)[-1] in ("CLAUDE.md", "AGENTS.md"):
        return False
    if any(seg.startswith(".") or seg in ("raw", "inbox") for seg in rel_path.split("/")):
        return False
    if any(rel_path.startswith(prefix) for prefix in _UNGOVERNED_PREFIXES):
        return False
    return rel_path != _EXCLUDED_EXACT


def _is_exempt_shape(paths: list[str]) -> bool:
    """True when one exempt shape accounts for every colliding path."""
    return any(all(regex.match(p) for p in paths) for regex in _EXEMPT_RES)


@register
class DuplicateBasenameRule(VaultRule):
    """Ported from npm's W57 (`utils/scripts/lint-rules/w57-duplicate-basename.mjs`)."""

    id = "W57"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Rename one colliding file to a distinct basename "
        "(this repo's <slug>-<purpose>.md satellite convention)."
    )
    producer = "wiki"
    pure = False
    version = "3"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        by_basename: dict[str, list[str]] = {}
        for page in corpus.pages():
            if not _is_governed(page.rel_path):
                continue
            by_basename.setdefault(page.slug, []).append(page.rel_path)

        for base in sorted(by_basename):
            paths = by_basename[base]
            if len(paths) < 2 or _is_exempt_shape(paths):
                continue

            for rel_path in sorted(paths):
                others = sorted(p for p in paths if p != rel_path)
                yield self.finding(
                    file=rel_path,
                    line=1,
                    message=(
                        f'basename "{base}.md" also exists at {", ".join(others)} — '
                        "Obsidian's wikilink resolution is basename-based, so a bare "
                        f"[[{base}]] link is ambiguous between them; rename one of these "
                        "files to a distinct basename rather than only adding a "
                        "path-qualified [[full/path|display]] wikilink at the call site."
                    ),
                )
