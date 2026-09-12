"""Registry-wide contract every rule and producer rule-doc must satisfy.

The reader of a lint finding is an agent in the middle of another task. It
gets one `message` line and one `FIX` line, and must act from those alone.
These tests hold that contract: a finished sentence (no trailing ellipsis), a
`fix` short enough to read (<=240 chars), phrased as an order rather than a
suggestion, and — where a rule carries an `Autofix` — a repair that is safe to
run twice.
"""

from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import TYPE_CHECKING

import pytest

import wiki_cli.producers as producers_pkg
import wiki_cli.rules as rules_pkg
from wiki_cli.autofix import FixContext, fixing
from wiki_cli.contracts import Autofix, all_rules

if TYPE_CHECKING:
    from wiki_cli.contracts import BaseRule, ProducerRuleDoc

FIX_MAX_CHARS = 240
"""A `FIX` line an agent reads mid-task. Longer guidance moves to a
`vault/refs/lint/` guide page, which `report._guide_pointers` links instead."""

HEDGE_PHRASES = ("consider", "should", "may want", "it is recommended", "try to")
"""A `fix` states the repair as an order. These words make it optional."""

IMPERATIVE_VERBS = frozenset(
    {
        "add",
        "break",
        "close",
        "collapse",
        "convert",
        "delete",
        "demote",
        "embed",
        "escape",
        "extract",
        "fill",
        "fix",
        "hoist",
        "hook",
        "insert",
        "keep",
        "lowercase",
        "make",
        "merge",
        "move",
        "name",
        "point",
        "prune",
        "put",
        "quote",
        "re-read",
        "regenerate",
        "re-verify",
        "remove",
        "rename",
        "reorder",
        "replace",
        "repoint",
        "retarget",
        "rewrite",
        "run",
        "set",
        "split",
        "stage",
        "strip",
        "supply",
        "wikilink",
        "write",
    }
)
"""Openers a `fix` may start with. A new rule needing a verb not listed here
adds it — the list is the contract, not a guess at English."""

AUTOFIX_FIXTURES = (
    "",
    "# Heading\n\nA plain body line.\n",
    "---\ntype: ref\nstatus: draft\naliases: []\n---\n\n# Title\n\nBody with a [[wikilink]].\n",
    "---\ntype: npc\n---\n\n> [!note]\n> A callout line.\n\n| a | b |\n| - | - |\n| 1 | 2 |\n",
    "No frontmatter, trailing spaces   \nand a second line.\n",
)
"""Texts every registered `Autofix` is run against."""

AUTOFIX_PATHS = (
    "vault/campaigns/shattered-sea/npcs/example.md",
    "docs/agents/example.md",
    ".claude/skills/example/SKILL.md",
)
"""Paths every fixture is repaired under. An `Autofix` scoped to one root
(`zsh_unsafe_glob`'s `docs/`, `path_wikilink`'s `vault/`) reads its path
from `autofix.current_context()`, so a single path would leave half the
registry running its no-op branch instead of its real transform."""

_WORD_RE = re.compile(r"\w+")
_FRONTMATTER_RE = re.compile(r"\A---\r?\n.*?\r?\n---\r?\n", re.DOTALL)


def _rules() -> list[BaseRule]:
    return all_rules()


def _producer_docs() -> list[ProducerRuleDoc]:
    return list(producers_pkg.all_rule_docs().values())


def _fix_texts() -> list[tuple[str, str]]:
    """(rule id, `fix` text) for every rule class and producer rule doc."""
    pairs = [(rule.id, rule.fix) for rule in _rules()]
    pairs += [(doc.id, doc.fix) for doc in _producer_docs()]
    return pairs


def _body_of(text: str) -> str:
    return _FRONTMATTER_RE.sub("", text)


def _static_text(node: ast.expr) -> str | None:
    """The literal text of a message expression, or None when it is built at
    runtime from a call this test cannot evaluate."""
    if isinstance(node, ast.Constant):
        return node.value if isinstance(node.value, str) else None
    if isinstance(node, ast.JoinedStr):
        parts = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
            else:
                parts.append("\x00")
        return "".join(parts)
    return None


def _message_literals() -> list[tuple[str, int, str]]:
    """(file, line, literal text) for every `message=` argument written as a
    literal in a rule or producer module."""
    found: list[tuple[str, int, str]] = []
    for package in (rules_pkg, producers_pkg):
        for path in sorted(Path(package.__path__[0]).glob("*.py")):
            tree = ast.parse(path.read_text(encoding="utf-8"))
            for node in ast.walk(tree):
                if not isinstance(node, ast.Call):
                    continue
                for keyword in node.keywords:
                    if keyword.arg != "message":
                        continue
                    text = _static_text(keyword.value)
                    if text is not None:
                        found.append((path.name, keyword.value.lineno, text))
    return found


def test_message_literals_are_found():
    """Guards the AST walk itself: a scan that silently matched nothing would
    make every message assertion below pass for the wrong reason."""
    assert len(_message_literals()) > 50


@pytest.mark.parametrize(("filename", "line", "text"), _message_literals())
def test_message_does_not_trail_off(filename: str, line: int, text: str):
    assert not text.rstrip().endswith("…"), f"{filename}:{line} message trails off"


@pytest.mark.parametrize(("rule_id", "fix"), _fix_texts())
def test_fix_fits_one_reading(rule_id: str, fix: str):
    assert len(fix) <= FIX_MAX_CHARS, (
        f"{rule_id} fix is {len(fix)} chars; move the detail to "
        f"vault/refs/lint/{rule_id.lower()}.md and keep the imperative core"
    )


@pytest.mark.parametrize(("rule_id", "fix"), _fix_texts())
def test_fix_opens_with_an_imperative_verb(rule_id: str, fix: str):
    opener = fix.split()[0].strip(":,.;").split("/")[0].lower()
    assert opener in IMPERATIVE_VERBS, (
        f"{rule_id} fix opens with {opener!r}; open with an imperative verb "
        f"(add it to IMPERATIVE_VERBS when the verb is new)"
    )


@pytest.mark.parametrize(("rule_id", "fix"), _fix_texts())
def test_fix_states_the_repair_rather_than_suggesting_it(rule_id: str, fix: str):
    lowered = fix.lower()
    hedges = [phrase for phrase in HEDGE_PHRASES if re.search(rf"\b{re.escape(phrase)}\b", lowered)]
    assert not hedges, f"{rule_id} fix hedges with {hedges}"


@pytest.mark.parametrize(("rule_id", "fix"), _fix_texts())
def test_fix_does_not_trail_off(rule_id: str, fix: str):
    assert not fix.rstrip().endswith("…"), f"{rule_id} fix trails off"


def test_every_rule_id_is_unique():
    ids = [rule.id for rule in _rules()] + [doc.id for doc in _producer_docs()]
    duplicates = sorted({rule_id for rule_id in ids if ids.count(rule_id) > 1})
    assert not duplicates, f"duplicate rule ids: {duplicates}"


@pytest.mark.parametrize("rule", _rules(), ids=lambda rule: rule.id)
def test_version_is_a_digit_string(rule: BaseRule):
    assert rule.version.isdigit(), f"{rule.id} version {rule.version!r} is not a digit string"


def _autofix_rules() -> list[BaseRule]:
    return [rule for rule in _rules() if rule.autofix is not None]


@pytest.mark.parametrize("rule", _autofix_rules(), ids=lambda rule: rule.id)
def test_autofix_is_idempotent(rule: BaseRule):
    autofix: Autofix = rule.autofix  # pyright: ignore[reportAssignmentType]
    for rel_path in AUTOFIX_PATHS:
        with fixing(FixContext(rel_path=rel_path)):
            for text in AUTOFIX_FIXTURES:
                once = autofix.apply(text)
                assert autofix.apply(once) == once, (
                    f"{rule.id} autofix changes its own output under {rel_path}"
                )


@pytest.mark.parametrize("rule", _autofix_rules(), ids=lambda rule: rule.id)
def test_syntax_autofix_keeps_every_word(rule: BaseRule):
    autofix: Autofix = rule.autofix  # pyright: ignore[reportAssignmentType]
    if autofix.scope != "syntax":
        pytest.skip("frontmatter-scope autofix may rewrite values")
    for rel_path in AUTOFIX_PATHS:
        with fixing(FixContext(rel_path=rel_path)):
            for text in AUTOFIX_FIXTURES:
                before = _WORD_RE.findall(_body_of(text))
                after = _WORD_RE.findall(_body_of(autofix.apply(text)))
                assert after == before, (
                    f"{rule.id} autofix changed the body's words under {rel_path}"
                )


def test_every_autofix_declares_a_known_scope():
    """Guards the two tests above: a scope typo would silently route a
    body-rewriting fix past the word-preservation check."""
    scopes = {rule.autofix.scope for rule in _autofix_rules() if rule.autofix is not None}
    assert scopes, "no rule declares an Autofix"
    assert scopes <= {"frontmatter", "syntax"}, f"unknown autofix scope: {scopes}"
