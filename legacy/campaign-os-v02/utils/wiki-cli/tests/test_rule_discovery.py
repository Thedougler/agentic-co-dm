"""Auto-discovery: importing wiki_cli.rules registers every rule module."""

from __future__ import annotations

import pkgutil

import wiki_cli.rules as rules_pkg
from wiki_cli.contracts import registry


def test_every_rules_module_is_imported_and_registered():
    modules = [m.name for m in pkgutil.iter_modules(rules_pkg.__path__)]
    assert "frontmatter_schema" in modules
    assert "W84" in registry()


def test_registry_count_matches_module_count():
    modules = [
        m.name for m in pkgutil.iter_modules(rules_pkg.__path__) if not m.name.startswith("_")
    ]
    assert len(registry()) >= len(modules)
