"""Ported from npm's W76 (`utils/scripts/lint-rules/w76-outside-wiki-family-reference.mjs`).

A `vault/**` page must not wikilink or markdown-link a local file outside
this repo's governed wiki family: `vault/` (incl. its PC and episode
subtrees) and `_templates/`. A reference into `inbox/`, `raw/`, `docs/`,
`utils/`, `.claude/`, or any other top-level directory either breaks
silently on the next reorg, or leaks process/tooling material into canon
prose.

`!`-prefixed embed syntax is excluded outright: an embed renders media
inline for the reader rather than pointing them at another page to follow,
so it carries none of the family-boundary risk a citation does. A bare
target with no `/` carries no directory information to classify at all —
resolving at all is W18's concern, not this one's.

Not pure — resolution walks the real filesystem under `corpus.repo_root`,
not just this file's own bytes.
"""

from __future__ import annotations

import posixpath
import re
from collections.abc import Iterable
from pathlib import Path

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_ALLOWED_TOP = {"vault", "_templates"}

# (bang, target) — wikilink, with the `[[path|display]]` pipe form and a
# `#Heading` anchor both stripped from the captured target.
_WIKILINK_TARGET_RE = re.compile(r"(!?)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
# (bang, target) — markdown link/image: `[display](target)`, `![alt](target "title")`.
_LINK_TARGET_RE = re.compile(r'(!?)\[[^\]]*\]\(([^)\s#]+)(?:#[^)]*)?(?:\s+"[^"]*")?\)')


def _resolve_target_rel_path(raw_target: str, repo_root: Path, own_dir_rel: str) -> str | None:
    """Resolve `raw_target` to its repo-root-relative path (real if it
    exists, otherwise the lexically-normalized literal) — or `None` when
    the target carries no directory information to classify at all (a
    bare, unresolved name; W18's concern, not this rule's)."""
    target = raw_target.strip()
    if not target:
        return None
    if re.match(r"^(https?:|mailto:)", target):
        return None  # external, out of scope
    if re.match(r"^[~/]", target):
        return None  # absolute/home path — not a repo-relative pointer

    has_slash = "/" in target
    is_dir_relative = bool(re.match(r"^\.\.?/", target))
    candidates = [target]
    if not re.search(r"\.[a-zA-Z0-9]+$", target):
        candidates.append(f"{target}.md")

    # A `../`/`./`-prefixed target declares itself directory-relative — it
    # never means "repo-root-relative", so it is never tried against
    # repo_root (a deep-enough `../../../` chain can otherwise walk
    # straight out of repo_root into whatever real directory sits above it).
    if not is_dir_relative:
        for candidate in candidates:
            normalised = posixpath.normpath(candidate)
            if (repo_root / normalised).exists():
                return normalised
        # Obsidian's vault root is vault/, so a path-shaped wikilink written
        # on a vault page is vault-relative
        # (`[[campaigns/shattered-sea/npcs/agata]]`, not
        # `[[vault/campaigns/...]]`). Resolve that form too, or every
        # disambiguating full-path link on every page reads as outside the
        # family.
        for candidate in candidates:
            normalised = posixpath.normpath(posixpath.join("vault", candidate))
            if (repo_root / normalised).exists():
                return normalised

    for candidate in candidates:
        normalised = posixpath.normpath(posixpath.join(own_dir_rel, candidate))
        if (repo_root / normalised).exists():
            return normalised

    if not has_slash:
        return None  # bare, unresolved — ambiguous, not this rule's concern

    if is_dir_relative:
        return posixpath.normpath(posixpath.join(own_dir_rel, target))
    return posixpath.normpath(target)


def _is_outside_family(resolved_rel: str) -> bool:
    segments = resolved_rel.split("/")
    if len(segments) == 1:
        return True  # a root-level file is never inside the wiki family
    return segments[0] not in _ALLOWED_TOP


@register
class OutsideWikiFamilyRule(FileRule):
    """Ported from npm's W76 (`utils/scripts/lint-rules/w76-outside-wiki-family-reference.mjs`)."""

    id = "W76"
    tier = Tier.STRUCTURAL
    severity = Severity.ERROR
    fix = "Repoint the reference to a page inside vault/ or _templates/, never a path outside the wiki family."
    producer = "wiki"
    pure = False
    version = "1"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path
        if not rel.startswith("vault/") or not rel.endswith(".md"):
            return

        own_dir_rel = posixpath.dirname(rel)
        lines = page.raw.split("\n")
        in_code_fence = False

        for idx, line in enumerate(lines):
            if line.strip().startswith("```"):
                in_code_fence = not in_code_fence
                continue
            if in_code_fence:
                continue

            for pattern in (_WIKILINK_TARGET_RE, _LINK_TARGET_RE):
                for match in pattern.finditer(line):
                    bang, raw_target = match.group(1), match.group(2)
                    if bang == "!":
                        continue  # embed, not a followable reference

                    # A `[[target\|Display]]` wikilink inside a table cell
                    # escapes its pipe so the table parser doesn't read it
                    # as a column separator; strip the trailing backslash
                    # the negated character class otherwise swallows.
                    raw_target = re.sub(r"\\$", "", raw_target)

                    resolved_rel = _resolve_target_rel_path(raw_target, corpus.repo_root, own_dir_rel)
                    if resolved_rel is None or not _is_outside_family(resolved_rel):
                        continue

                    stem = Path(raw_target.strip()).stem.lower()
                    found = corpus.resolve(stem)

                    column = line.find(raw_target) + 1
                    if found is not None:
                        message = (
                            f"`{raw_target}` references a file outside the wiki family "
                            f"(vault/, _templates/) — a same-named page exists at "
                            f"`{found.rel_path}`; repoint the reference there"
                        )
                    else:
                        message = (
                            f"`{raw_target}` references a file outside the wiki family "
                            "(vault/, _templates/) and no same-named page exists inside it — "
                            "remove the reference and rewrite the surrounding sentence, or "
                            "move the real file into the wiki family if it belongs in canon"
                        )

                    yield self.finding(file=rel, line=idx + 1, column=column, message=message)
