"""Ported from npm's W75 (`utils/scripts/lint-rules/w75-doc-pointer-resolves.mjs`).

Agent-facing docs (skills, their `references/`, subagent specs, templates,
`docs/guardrails/`, `vault/refs/`, and `CLAUDE.md` at any depth) point each
other at files by path. A relative path resolves only for a reader already
sitting in the right directory — but every agent runs with cwd at the repo
root, so a path that resolves from neither the repo root nor the file's own
directory is unusable from anywhere, which is the state that costs a real
read (a top-level directory renamed/retired while other files kept citing
the old name).

Placeholders (`_templates/<type>.md`, `sessions/NNN/transcript.md`) are not
pointers and never fire, nor are URLs or a global/absolute path (a skill
outside this repo, e.g. `~/.claude/skills/writing-for-agents/SKILL.md`,
which this rule has no standing to resolve).

`MIGRATION-LOG.md` and `PROJECT-NOTES.md` are excluded: F15 makes them
project-authored archives whose entries document a path as it was at the
time of writing, never rewritten — a dead pointer there is the historical
record working, not rot.

Not pure — the finding depends on the real filesystem (`corpus.repo_root`
and this file's own directory), not just this file's own bytes.
"""

from __future__ import annotations

import re
from collections.abc import Iterable

from wiki_cli.contracts import Corpus, FileRule, Finding, Page, Severity, Tier, register

_SCOPED_PATH_RE = re.compile(
    r"(^|/)(\.claude/(skills|agents|rules)/|_templates/|docs/guardrails/|vault/refs/)"
    r"|(^|/)CLAUDE\.md$"
)
_F15_ARCHIVES = frozenset({"MIGRATION-LOG.md", "PROJECT-NOTES.md"})

# A backticked path token (a `.md` file OR a bare directory reference ending
# in `/`), and a markdown-link target — the shapes a pointer takes in these
# docs. Anchors (`page.md#Heading`) resolve on the file part.
_BACKTICK_POINTER_RE = re.compile(r"`([^`\s()]+(?:\.md|/))(#[^`]*)?`")
_LINK_POINTER_RE = re.compile(r"\]\(([^)\s#]+\.md)(#[^)]*)?\)")

# A token standing in for a path the author cannot know yet. Covers the
# bare digit-run form (`NNN`) and the session/episode-prefixed form
# (`sNN`, `eNN`) alike — both are this repo's numbered-slug convention,
# never a real lowercase-hyphenated filename (W75 is case-sensitive on
# purpose: `N` only matches the placeholder digit stand-in, not prose).
_PLACEHOLDER_RE = re.compile(r"[<>*{}]|\b[a-zA-Z]?N{2,}\b")
_URL_RE = re.compile(r"^(https?:|mailto:)")
_ABSOLUTE_RE = re.compile(r"^[~/]")


@register
class DocPointerResolvesRule(FileRule):
    """Ported from npm's W75 (`utils/scripts/lint-rules/w75-doc-pointer-resolves.mjs`)."""

    id = "W75"
    tier = Tier.STRUCTURAL
    severity = Severity.WARNING
    fix = (
        "Repoint the pointer to the target's repo-root-relative path "
        "(find it with `git ls-files | grep <basename>`), or delete the "
        "pointer if the file is gone."
    )
    producer = "wiki"
    pure = False
    """Depends on the real filesystem (repo root + this file's own
    directory), not just this file's own bytes."""
    version = "2"

    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]:
        rel = page.rel_path
        if not _SCOPED_PATH_RE.search("/" + rel):
            return
        if rel.rsplit("/", 1)[-1] in _F15_ARCHIVES:
            return

        repo_root = corpus.repo_root
        own_dir = (repo_root / rel).parent

        for line_no, text in page.body_lines():
            for pattern in (_BACKTICK_POINTER_RE, _LINK_POINTER_RE):
                for match in pattern.finditer(text):
                    target = match.group(1)
                    if _PLACEHOLDER_RE.search(target):
                        continue
                    if _URL_RE.match(target):
                        continue
                    if _ABSOLUTE_RE.match(target):
                        continue
                    if (repo_root / target).exists():
                        continue
                    if (own_dir / target).exists():
                        continue

                    basename = target.rsplit("/", 1)[-1]
                    yield self.finding(
                        file=rel,
                        line=line_no,
                        column=text.find(target) + 1,
                        message=(
                            f"pointer `{target}` resolves from neither the repo root "
                            "nor this file's own directory, so an agent following it "
                            'gets "file does not exist" — repoint it to the target\'s '
                            "repo-root-relative path (find it with `git ls-files | "
                            f"grep {basename}`), or delete the pointer if the file is gone"
                        ),
                    )
