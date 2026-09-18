"""Build Vale's accepted proper-noun vocabulary from live wiki owners."""
from __future__ import annotations

import os
import re
import tempfile
from pathlib import Path

from tools.lint_wiki import load

VOCAB_RELATIVE = Path("styles/config/vocabularies/CoDM/accept.txt")
_STOPWORDS = {
    "a", "an", "and", "at", "by", "for", "from", "in", "of", "on", "or", "the", "to", "with",
}
_REGEX_META = re.compile(r"([\\.^$*+?{}\[\]|()])")


def _escape_term(value: str) -> str:
    return _REGEX_META.sub(r"\\\1", value)


def _owner_terms(value: str) -> set[str]:
    value = re.sub(r"\s+", " ", value.strip())
    if not value or len(value) < 2:
        return set()
    terms = {value}
    for word in re.findall(r"[A-Za-z][A-Za-z0-9'’-]*", value):
        if word.casefold() not in _STOPWORDS and (word[:1].isupper() or len(value.split()) == 1):
            terms.add(word)
    return terms


def proper_nouns(vault: Path) -> list[str]:
    pages, _ = load(vault)
    terms: set[str] = set()
    for page in pages.values():
        terms.update(_owner_terms(str(page.get("title") or "")))
        for alias in page.get("aliases") or []:
            terms.update(_owner_terms(str(alias)))
        path = page.get("path")
        if isinstance(path, Path) and "-" in path.stem:
            terms.add(path.stem)
    return sorted(terms, key=lambda value: (value.casefold(), value))


def render_vocab(vault: Path) -> str:
    lines = [
        "# Generated from live wiki page titles and aliases.",
        "# Do not hand-edit; wiki-lint refreshes this Vale vocabulary.",
        *( _escape_term(term) for term in proper_nouns(vault)),
        "",
    ]
    return "\n".join(lines)


def refresh_vocab(root: Path, vault: Path) -> Path:
    destination = (root / VOCAB_RELATIVE).resolve()
    destination.parent.mkdir(parents=True, exist_ok=True)
    content = render_vocab(vault)
    if destination.is_file() and destination.read_text(encoding="utf-8") == content:
        return destination
    with tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", dir=destination.parent, prefix=".accept-", delete=False
    ) as handle:
        handle.write(content)
        temporary = Path(handle.name)
    try:
        os.replace(temporary, destination)
    finally:
        temporary.unlink(missing_ok=True)
    return destination
