"""New rule (no npm parity) — wiki-lint migration plan Task 30.

A page A's `parent:`/`within:` frontmatter names a containing page B, but B's
body never links back to A — the containment relationship reads one-way: a
reader who opens B has no path down to A, only A has a path up to B.

Real-vault false-positive tuning (what counts as "the relevant section" on
B, whether a table/list mention should satisfy the symmetry) needs real
instances to audit against, so a hit is baselineable debt meanwhile.

A `VaultRule`, not a `FileRule`: the check needs `corpus.links_to` — every
other page's outbound links — not just the one page's own bytes.

Not pure — the finding depends on the whole corpus's link graph.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register

_CONTAINMENT_FIELDS = ("parent", "within")


def _target_name(value: str) -> str:
    """`[[slug]]`, `[[slug|Display]]`, `[[slug#Heading]]`, a bare slug, or a
    bare display name -> the resolvable name, brackets/alias/heading
    stripped. `corpus.resolve` handles slug/alias/title matching from there."""
    text = value.strip()
    if text.startswith("[[") and text.endswith("]]"):
        text = text[2:-2]
    text = text.replace("\\|", "|").split("|", 1)[0]
    return text.split("#", 1)[0].strip()


@register
class BacklinkSymmetryRule(VaultRule):
    """New rule (wiki-lint migration plan Task 30, no npm parity)."""

    id = "wiki/backlink-symmetry"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Add a [[child]] wikilink to the parent/container page's body"
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        for child in corpus.pages():
            for field_name in _CONTAINMENT_FIELDS:
                raw = child.frontmatter.get(field_name)
                if not isinstance(raw, str) or not raw.strip():
                    continue

                target_name = _target_name(raw)
                if not target_name:
                    continue

                container = corpus.resolve(target_name)
                if container is None or container.rel_path == child.rel_path:
                    continue

                backlinkers = corpus.links_to(child.rel_path)
                if container.rel_path in backlinkers:
                    continue

                yield self.finding(
                    file=container.rel_path,
                    line=1,
                    message=(
                        f"[[{child.slug}]] declares {field_name}: [[{container.slug}]] but "
                        f"this page never links back — add a [[{child.slug}]] wikilink in "
                        "the relevant section"
                    ),
                )
