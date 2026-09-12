"""markdownlint producer (W87): pymarkdown's Python API, not a Node binary
subprocess.

The legacy invocation shelled `node_modules/.bin/markdownlint-obsidian
--output-formatter json` and parsed its stdout as one JSON blob. On a large
batch (359+ files) that blob exceeds the OS pipe buffer (~64KB), truncating
stdout mid-stream and crashing the run with malformed JSON — no flag or
buffering trick fixes this from the calling side, since the truncation
happens at the pipe itself, below Python's control. `pymarkdown`
(`pymarkdownlnt` on PyPI) carries the same MD### rule ids as a proper
in-process Python API (`PyMarkdownApi.scan_path`), so there is no subprocess,
no pipe, and no truncation ceiling.

Only markdownlint-obsidian's built-in MD/OFM checks are reported here — the
`customRules` harness in `.obsidian-linter.jsonc` that hosted every
W-numbered rule (W12, W27, W111, ...) has no equivalent in pymarkdown; each
of those rules is a native `wiki_cli.rules` module instead, so nothing is
lost by pymarkdown's lack of an OFM/custom-rule concept.

MD013 (line length) is disabled: this vault's Obsidian convention is one
paragraph per source line, unwrapped, confirmed from `vault/campaigns/`
canon pages down to `vault/stories/` skill docs — real page bodies run past
1000 characters on a single line by design, and Obsidian's own soft-wrap
renders them regardless of source line length. A GFM table row is a single
line by the format's own syntax and can never be wrapped to fit any
line-length cap; `W102` (`table_too_wide.py`) already governs table width
by column count, the dimension that actually scrolls in Obsidian's reading
pane. MD013's 80-character default check has no target in this repo.

MD033 (inline HTML) is disabled: agent-facing docs (skills, templates,
`vault/refs/`) write fill-in-the-blank placeholders as bare angle brackets
(`<Working title>`, `<reason>`, `<entities grounded>`) — CommonMark's own
inline-HTML production can't distinguish those from a real tag, and
pymarkdown has no allowlist mechanism for arbitrary multi-word placeholder
text (only fixed element names). A real stray HTML tag is a much rarer
defect in this hand-authored corpus than the placeholder convention is
common, and `obsidian-markdown`'s own skill guidance already tells authors
not to write HTML in the first place.

MD026 (trailing punctuation in headings) is disabled and MD029 (ordered
list item prefix) is configured with `allow_extended_start_values`: a
`guideline-recreator`-produced `guide` page (`external-guides.md`)
faithfully reproduces a real external source's own structure, and a
source like *The Elements of Style* numbers its rules 1-18 as full
sentences ending in a period (`### Rule 13. Omit needless words.`) split
across more than one section heading — a skill's own digest of that same
source continues the identical numbering across its own section break
(`vault/stories/.claude/skills/writing-clearly-and-concisely/`). Diverging
from the source's own punctuation or restarting its numbering at each
section would be unfaithful, not a style fix.

MD028 (blank line inside blockquote) is disabled: in Obsidian a fully blank
line is the *only* thing that ends a callout and starts a new one, while a
lone `>` line keeps the following paragraph inside the same callout
(`vault/.claude/skills/obsidian-markdown/references/callouts-syntax.md`).
Two consecutive callouts — three `> [!check]` blocks stacking DCs down a
moment page — are therefore separated by exactly the blank line MD028
objects to, and every alternative it would accept merges them into one box:
the lone `>` swallows the second callout's `[!check]` as literal text, and
an HTML-comment separator is barred outright by this vault's
standard-Obsidian-only rule. The pattern MD028 flags here is the correct
syntax, not a defect.

MD036 (emphasis instead of a heading) is disabled: pymarkdown (unlike
legacy markdownlint) fires MD036 inside list items too, but a list item
can never render as a heading regardless — this repo's own convention
bolds an ordered-list item's full text to flag it as one of a rule set's
few load-bearing entries (`writing-clearly-and-concisely/SKILL.md`'s
`**Use active voice**`), a real distinction MD036 can't tell from a
mislabeled heading.

MD041 (first line should be a top-level heading) is disabled for
`docs/guardrails/**`, every `CLAUDE.md` and `AGENTS.md` (a `CLAUDE.md` is
often just `@AGENTS.md`, so the kit block with its comment-then-prose
opener lives in the `AGENTS.md`), and performative siblings
(`-narration-` / `-dialogue-` in the filename): `docs/guardrails/_FORMAT.md`
F11 mandates that a guardrail doc opens with an optional HTML comment
plus a "You are here because…" trigger-restatement line, and the kit's
`CLAUDE.md` KIT CORE block opens the same way — both carry no H1 by
design. MD041 has no allowlist for that shape, and every other corpus
file keeps MD041 enabled.

MD022 (blank lines around headings) is filtered only for root `hot.md`:
that file is an append-only LLM-wiki recency log whose own contract is one
`## [date] type | short note` heading per entry. Blank lines double the
line cost of the hot set without adding structure the reader or an agent
uses; every other markdown file keeps MD022 enabled.
"""

from __future__ import annotations

import re
from pathlib import Path

from pymarkdown.api import PyMarkdownApi, PyMarkdownApiException

from wiki_cli.config import Config
from wiki_cli.contracts import Corpus, Finding, ProducerRuleDoc, Severity, Tier

FAMILY_ID = "W87"
VERSION = "1"
PURE = True

_DISABLED_RULES: tuple[str, ...] = ("MD013", "MD033", "MD026", "MD028", "MD036")
"""Rules `_build_api` turns off for every target — see its docstring for
why each. Also the whole of this producer's out-of-file config: pymarkdown
reads no config file here, so `config_fingerprint` is a constant derived
from this tuple, and any other change to `_build_api` is covered by
bumping `VERSION`."""

_GUARDRAILS_DISABLED_RULES: tuple[str, ...] = ("MD041",)
"""Additionally disabled for `docs/guardrails/**` and CLAUDE.md targets."""


def config_fingerprint(repo_root: Path) -> str:
    """This producer's disabled-rule set. A constant — no config file
    exists to stat, so a change to any other `_build_api` setting is
    carried by `VERSION` instead."""
    del repo_root
    return ",".join((*_DISABLED_RULES, *_GUARDRAILS_DISABLED_RULES))


RULE_DOCS: tuple[ProducerRuleDoc, ...] = (
    ProducerRuleDoc(
        id=FAMILY_ID,
        tier=Tier.CONTENT_SHAPE,
        severity=Severity.WARNING,
        fix=(
            "Fix the markdown defect the MD### code at the head of the message names, at the "
            "reported line (e.g. `MD009` trailing spaces, `MD022` blanks around a heading). "
            "Disabling the code in this module's `_build_api()` is not a fix."
        ),
    ),
)

_BUILTIN_RULE_CODE_RE = re.compile(r"^(MD|OFM)\d+$")
"""markdownlint-obsidian's own built-in checks always carry this shape
(MD### core rules, OFM### Obsidian-flavored extensions). pymarkdown only
ever emits MD### ids (it has no OFM concept) — the OFM half of this pattern
is kept so a rule_id shaped like the legacy engine's never silently changes
meaning, and so this stays the single filter both engines can share."""

_MARKDOWN_SUFFIXES = {".md", ".markdown"}
"""The orchestrator fans the same `targets` list out to every registered
producer (see `orchestrator.py`'s module docstring), so a non-markdown
target (e.g. a `.mjs` fixture bound for the oxlint producer) routinely
reaches this one too. The legacy binary tolerated that silently; pymarkdown
does not — `scan_path` on a path outside its markdown-extension filter
raises `PyMarkdownApiNoFilesFoundException`. Skipping non-markdown targets
before scanning keeps this producer a no-op on them, same as before."""


def _build_api() -> PyMarkdownApi:
    """Shared rule-disable baseline — see the module docstring for why each
    is disabled. `run()` builds a second instance off this for
    `docs/guardrails/**` targets rather than chaining onto one shared
    instance, since `disable_rule_by_identifier` mutates in place."""
    api = PyMarkdownApi().enable_extension_by_identifier("front-matter")
    for rule_code in _DISABLED_RULES:
        api = api.disable_rule_by_identifier(rule_code)
    return api.set_boolean_property(
        "plugins.md029.allow_extended_start_values", True
    ).set_string_property("plugins.md025.front_matter_title", "no-such-frontmatter-key")


def _is_allowed_hot_log_spacing(rel_path: str, rule_code: str) -> bool:
    return rel_path == "hot.md" and rule_code == "MD022"


def _no_h1_by_design(name: str, posix_path: str) -> bool:
    """True for the files `_FORMAT.md` F11 and the kit's own shape leave
    without an H1 — see the module docstring's MD041 note."""
    return (
        "/docs/guardrails/" in posix_path
        or name in {"CLAUDE.md", "AGENTS.md"}
        or "-narration-" in name
        or "-dialogue-" in name
    )


def autofix(targets: list[Path]) -> None:
    """Apply pymarkdown's own fix mode to `targets`, in place.

    This producer's whole family is mechanical markdown repair (MD009
    trailing spaces, MD022 blanks around a heading), so every finding it
    can repair itself is one no agent should ever read. Called by
    `wiki_cli.autofix`, which has already dropped `docs/guardrails/**` and
    honours `--no-fix`/`--json`; the same rule-disable baseline `run` scans
    with is what fixes here, so the pass can never repair a rule this
    module turns off. A file pymarkdown refuses is left as it is — the
    scan that follows reports it.
    """
    markdown_targets = [t for t in targets if t.suffix.lower() in _MARKDOWN_SUFFIXES]
    if not markdown_targets:
        return

    api = _build_api()
    guardrails_api = _build_api()
    for rule_code in _GUARDRAILS_DISABLED_RULES:
        guardrails_api = guardrails_api.disable_rule_by_identifier(rule_code)

    for target in markdown_targets:
        resolved = target.resolve()
        target_api = (
            guardrails_api
            if _no_h1_by_design(resolved.name, resolved.as_posix())
            else api
        )
        try:
            target_api.fix_path(str(resolved))
        except PyMarkdownApiException:
            continue


def run(config: Config, targets: list[Path], corpus: Corpus) -> list[Finding]:
    """Run pymarkdown's built-in MD checks over `targets`.

    `targets` are absolute paths under the repo. Each target is scanned
    individually via `PyMarkdownApi.scan_path` — no subprocess, no shared
    stdout buffer to truncate. The `front-matter` extension is enabled so
    a page's YAML frontmatter block isn't misread as document content
    (matching markdownlint-obsidian's own frontmatter awareness — without
    it, pymarkdown flags the frontmatter delimiters themselves under
    MD003/MD022/MD041). MD013 (line length), MD033 (inline HTML), and MD026
    (trailing heading punctuation) are disabled, MD028 (blank line inside
    blockquote) and MD036 (emphasis instead of
    a heading) are disabled, and MD029 (ordered list item prefix) allows a
    list to start past 1 — see the module docstring. An empty `targets`
    list is a no-op.

    MD025 (`plugins/rule_md_025.py`) treats a frontmatter key named
    `front_matter_title` (default: `"title"`) as an implicit top-level
    heading, so it double-counts against the body's own `# <Name>` H1 on
    every page whose template declares a `title:` frontmatter key — which
    is every page under `vault/_templates/`, present or empty. pymarkdown
    rejects an empty string for this option (it reads as "unset the
    default", not "disable the behavior"), so it's repointed at a key no
    template declares instead, which is the only way to turn the check
    off without also disabling MD025 entirely.

    `docs/guardrails/**` targets and every `CLAUDE.md` additionally
    disable MD041 — see the module docstring.
    `PyMarkdownApi.disable_rule_by_identifier` mutates and returns `self`
    rather than a new instance, so the MD041-disabled variant is built as
    its own `PyMarkdownApi()` off `_build_api()` rather than chained onto
    the shared `api` below, which would leak the disable onto every
    other target.
    """
    del config  # this producer's invocation is fully determined by pymarkdown's own rule defaults
    if not targets:
        return []

    repo_root = corpus.repo_root
    api = _build_api()
    guardrails_api = _build_api()
    for rule_code in _GUARDRAILS_DISABLED_RULES:
        guardrails_api = guardrails_api.disable_rule_by_identifier(rule_code)

    findings: list[Finding] = []
    for target in targets:
        if target.suffix.lower() not in _MARKDOWN_SUFFIXES:
            continue
        rel_path = str(target.resolve().relative_to(repo_root))
        name = Path(rel_path).name
        target_api = guardrails_api if _no_h1_by_design(name, f"/{rel_path}") else api
        try:
            result = target_api.scan_path(str(target))
        except PyMarkdownApiException as error:
            raise RuntimeError(f"pymarkdown scan of {target} failed: {error}") from error

        for failure in result.scan_failures:
            rule_code = failure.rule_id or ""
            if not _BUILTIN_RULE_CODE_RE.match(rule_code):
                continue  # a custom W-rule finding — a native rules/*.py module already reports it
            rel_path = str(Path(failure.scan_file).resolve().relative_to(repo_root))
            if _is_allowed_hot_log_spacing(rel_path, rule_code):
                continue
            findings.append(
                Finding(
                    rule_id=FAMILY_ID,
                    file=rel_path,
                    line=int(failure.line_number or 1),
                    message=f"{rule_code}: {failure.rule_description}",
                    severity=Severity.WARNING,
                    tier=Tier.CONTENT_SHAPE,
                    producer="markdownlint",
                    column=int(failure.column_number or 1),
                    fixable=False,
                )
            )
    return findings
