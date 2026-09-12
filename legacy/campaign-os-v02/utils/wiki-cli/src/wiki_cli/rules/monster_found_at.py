"""A `type: monster` page's `found_at:` must name at least
`MONSTER_FOUND_AT_MIN` region-scale locations, each resolving to a real
`type: location` or `type: route` page, ported from `utils/scripts/lint-rules/w125-
monster-found-at.mjs` (rule id `W125`).

An absent `found_at:` (the key itself missing) is the frontmatter-schema
gate's own finding (W84) and stays silent here, same convention as W118's
empty-string skip. Thematic fit (which locations to pick) is a judgment
call this rule can't make — `vault/refs/vault/monster/references/
ecology.md` is the reference.

An entry naming a location page nobody has written yet warns instead of
erroring: the fix belongs in the missing file. An entry resolving to the
wrong `type:` is a different defect and stays an error.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SOURCE_DOC = "_templates/monster.md § found_at"
_TEMPLATES_PREFIX = "vault/_templates/"
_WIKILINK_PREFIX_RE = re.compile(r"^\[\[([^\]|]+)")


def _strip_wikilink(value: str) -> str:
    """`[[path/to/target|display]]` -> `target`'s last path segment — the
    same basename-or-full-path styles this vault's own wikilinks mix.
    Ported from `lib/vaultIndex.mjs`'s `stripWikilink`."""
    unquoted = value.strip().strip("'\"")
    match = _WIKILINK_PREFIX_RE.match(unquoted)
    target = (match.group(1) if match else unquoted).strip()
    segments = target.split("/")
    return segments[-1] if segments else target


@register
class MonsterFoundAtRule(FileRule):
    """Ported from npm's W125 (`utils/scripts/lint-rules/w125-monster-found-at.mjs`)."""

    id = "W125"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Add wikilinks to >=2 type: location pages, picked for thematic fit "
        "(vault/refs/vault/monster/references/ecology.md); an entry whose target "
        "page is not written yet warns until that page lands."
    )
    producer = "wiki"
    pure = False
    """Depends on the vault-wide link graph (corpus.resolve), not just this
    file's own bytes."""
    version = "3"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path
        if not rel.endswith(".md") or not rel.startswith("vault/"):
            return
        if rel.startswith(_TEMPLATES_PREFIX):
            return
        if page.type != "monster":
            return

        frontmatter = page.frontmatter
        if "found_at" not in frontmatter:
            return  # key absence is the frontmatter-schema gate's finding (W84)

        found_at = frontmatter.get("found_at")
        line = page.line_of("found_at")
        entries = found_at if isinstance(found_at, list) else [found_at]
        real = [entry for entry in entries if isinstance(entry, str) and entry.strip() != ""]

        minimum = int(load_config().threshold("MONSTER_FOUND_AT_MIN"))
        if len(real) < minimum:
            yield self.finding(
                file=rel,
                line=line,
                message=(
                    f"found_at: names {len(real)} location(s) — a monster page needs "
                    f"at least {minimum}, picked for thematic fit per "
                    f"vault/refs/vault/monster/references/ecology.md ({_SOURCE_DOC})"
                ),
            )
            return

        for raw in real:
            slug = _strip_wikilink(raw)
            hit = corpus.resolve(slug) if slug else None
            if hit is None:
                yield self.finding(
                    file=rel,
                    line=line,
                    message=(
                        f'found_at: entry "{raw}" points at a page that does not exist '
                        f"yet — write that location page, or repoint the entry if the "
                        f"target is misspelled ({_SOURCE_DOC})"
                    ),
                    severity=Severity.WARNING,
                )
                continue
            if hit.type not in ("location", "route"):
                yield self.finding(
                    file=rel,
                    line=line,
                    message=(
                        f'found_at: entry "{raw}" resolves to a type: '
                        f"{hit.type or 'unknown'} page, not a location or route — point it at "
                        "the region-scale location or route page where this creature is "
                        f"actually found ({_SOURCE_DOC})"
                    ),
                )
