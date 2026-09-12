"""Self-configuring subtype/folder partition, ported from
`utils/scripts/lint-rules/w97-subtype-folder-partition.mjs` (rule id
`W97`): no declared mapping — for a directory where at least
`SUBTYPE_PARTITION_MIN_PAGES` sibling `.md` files carry `subtype:` and at
least 95% of those equal the directory's own basename, the directory has
organically become subtype-partitioned (every npc under
`vault/campaigns/shattered-sea/npcs/recurring/` is `subtype: recurring`) —
a page in that directory whose own `subtype:` differs from the consensus
is drift.

A `VaultRule` here (unlike the legacy per-file rule, which re-reads its own
directory's sibling files from disk on every invocation): the whole-corpus
`VaultIndex` already carries every page's parsed frontmatter, so grouping
by parent directory once over `corpus.pages()` is the natural shape and
avoids re-parsing siblings once per member.

`vault/_templates/**` is excluded — see `type_folder_placement.py`'s
docstring for why templates need an explicit guard in this port (npm's
`.obsidian-linter.jsonc` ignores that tree ahead of every custom rule; a
sibling group of same-fork template files, e.g.
`vault/_templates/_campaigns/_location/`, would otherwise be eligible for
its own (spurious) consensus computation).
"""

from __future__ import annotations

from collections import defaultdict
from collections.abc import Iterable
from pathlib import PurePosixPath

from wiki_cli.config import load_config
from wiki_cli.contracts import Corpus, Finding, Page, Severity, Tier, VaultRule, register

_MAJORITY_PCT = 0.95
"""Not in thresholds.json (only SUBTYPE_PARTITION_MIN_PAGES is) — the
legacy module's own `SUBTYPE_PARTITION_MAJORITY_PCT` constant."""


@register
class SubtypeFolderPartitionRule(VaultRule):
    """Ported from npm's W97 (`utils/scripts/lint-rules/w97-subtype-folder-partition.mjs`)."""

    id = "W97"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = (
        "Set subtype: to this directory's consensus value, or move the "
        "page to the sibling folder matching its own subtype."
    )
    producer = "wiki"
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        min_pages = int(load_config().threshold("SUBTYPE_PARTITION_MIN_PAGES"))

        by_dir: dict[str, list[tuple[Page, str]]] = defaultdict(list)
        for page in corpus.pages():
            rel = page.rel_path
            if not rel.startswith("vault/") or rel.startswith("vault/_templates/"):
                continue
            subtype = page.frontmatter.get("subtype")
            if not isinstance(subtype, str):
                continue
            dir_rel = str(PurePosixPath(rel).parent)
            by_dir[dir_rel].append((page, subtype))

        for dir_rel, entries in by_dir.items():
            if len(entries) < min_pages:
                continue
            dir_name = PurePosixPath(dir_rel).name
            matching = sum(1 for _page, subtype in entries if subtype == dir_name)
            if matching / len(entries) < _MAJORITY_PCT:
                continue
            for page, subtype in entries:
                if subtype == dir_name:
                    continue
                yield self.finding(
                    file=page.rel_path,
                    line=page.line_of("subtype"),
                    message=(
                        f"every other page in {dir_rel}/ carries subtype: {dir_name} — "
                        f"set subtype: {dir_name}, or move this page to the sibling "
                        "folder matching its subtype"
                    ),
                )
