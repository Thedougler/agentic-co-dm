"""Closed vocabularies for creative linting configuration and output."""
from __future__ import annotations

import re

RULE_ID_RE = re.compile(r"^(?:[A-Z]+\d{3}|VALE_[A-Za-z0-9_.-]+)$")
CATEGORIES = frozenset({"wiki", "canon", "temporal", "agency", "retrieval", "scene", "diversity"})
SCOPES = frozenset({"content", "frontmatter", "corpus", "file"})
SEVERITIES = frozenset({"BLOCK", "REPAIR", "REVIEW", "WARN", "INFO"})
EVALUATORS = frozenset({"vale", "symbolic", "retrieval", "semantic", "human", "lint_wiki"})
LIFECYCLES = frozenset({"DRAFT", "SHADOW", "ACTIVE"})
RESULTS = frozenset({"pass", "fail", "abstain"})


def is_rule_id(value: str) -> bool:
    return bool(RULE_ID_RE.fullmatch(value))
