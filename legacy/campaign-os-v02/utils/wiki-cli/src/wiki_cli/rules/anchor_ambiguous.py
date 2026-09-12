"""New rule: wiki/anchor-ambiguous — two competing spatial anchors, no override.

A page whose `location:` and `within:` frontmatter keys both resolve to
distinct pages in the corpus has two candidate spatial anchors. Without an
explicit `anchor:` key the vault organiser cannot determine which anchor to
use for cluster assignment without falling back to centrality comparison.
This rule surfaces the tie so the DM can add an explicit override."""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register

_SPATIAL_KEYS = ("location", "within")


def _fm_target_name(value: str) -> str:
    """Normalize a frontmatter wikilink value to a resolvable slug."""
    text = value.strip()
    if text.startswith("[[") and text.endswith("]]"):
        text = text[2:-2]
    return text.split("|", 1)[0].strip()


@register
class AnchorAmbiguousRule(VaultRule):
    """Two or more distinct spatial anchors with no explicit override."""

    id = "wiki/anchor-ambiguous"
    tier = Tier.CONTENT_SHAPE
    severity = Severity.WARNING
    fix = "Add anchor: <slug> to name the primary spatial anchor explicitly"
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        for page in corpus.pages():
            if page.frontmatter.get("anchor") is not None:
                continue

            resolved_paths: dict[str, str] = {}
            for key in _SPATIAL_KEYS:
                raw = page.frontmatter.get(key)
                if not isinstance(raw, str) or not raw.strip():
                    continue
                target_name = _fm_target_name(raw)
                if not target_name:
                    continue
                resolved = corpus.resolve(target_name)
                if resolved is not None and resolved.rel_path != page.rel_path:
                    resolved_paths[key] = resolved.rel_path

            if len(set(resolved_paths.values())) < 2:
                continue

            anchor_names = " vs ".join(
                f"{key}: [[{page.frontmatter.get(key)}]]" for key in resolved_paths
            )
            yield self.finding(
                file=page.rel_path,
                line=1,
                message=(
                    f"anchor ambiguous: {anchor_names} — "
                    "add anchor: to name the primary"
                ),
            )
