"""W147 — duplicate uid: values across vault pages.

Two checks:
1. Two or more non-template pages share the same uid: value.
2. A non-template page carries a uid: that matches a template's uid:
   (the page was cp'd from the template without regenerating the uid).

A VaultRule: the collision requires the whole corpus.
"""

from __future__ import annotations

from collections.abc import Iterable

from wiki_cli.contracts import Corpus, Finding, Severity, Tier, VaultRule, register


def _is_template(rel_path: str) -> bool:
    return rel_path.startswith("vault/_templates/")


@register
class DuplicateUidRule(VaultRule):
    """W147 — duplicate or template-inherited uid: value."""

    id = "W147"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = "Regenerate with `uuidgen | tr A-Z a-z`."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, corpus: Corpus) -> Iterable[Finding]:
        # Collect uid -> list of (rel_path, line) for templates and pages.
        template_uids: dict[str, list[str]] = {}
        page_uids: dict[str, list[tuple[str, int]]] = {}

        for page in corpus.pages():
            uid = page.frontmatter.get("uid")
            if not isinstance(uid, str) or not uid.strip():
                continue
            uid_val = uid.strip()
            if _is_template(page.rel_path):
                template_uids.setdefault(uid_val, []).append(page.rel_path)
            else:
                page_uids.setdefault(uid_val, []).append(
                    (page.rel_path, page.line_of("uid"))
                )

        # Check 1: page uid duplicates another page's uid.
        for uid_val in sorted(page_uids):
            entries = page_uids[uid_val]
            if len(entries) < 2:
                continue
            for rel_path, line in sorted(entries):
                others = sorted(p for p, _ in entries if p != rel_path)
                yield self.finding(
                    file=rel_path,
                    line=line,
                    message=(
                        f"uid: {uid_val} is shared with "
                        f'{", ".join(others)} — each page must have a '
                        "globally unique uid"
                    ),
                )

        # Check 2: page uid matches a template uid.
        for uid_val in sorted(page_uids):
            if uid_val not in template_uids:
                continue
            template_paths = template_uids[uid_val]
            for rel_path, line in sorted(page_uids[uid_val]):
                yield self.finding(
                    file=rel_path,
                    line=line,
                    message=(
                        f"uid: {uid_val} matches template "
                        f'{", ".join(sorted(template_paths))} — '
                        "page was copied from the template without "
                        "regenerating its uid"
                    ),
                )
