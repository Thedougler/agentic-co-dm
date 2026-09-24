"""Cross-page symbolic checks built on the existing wiki lint loader."""
from __future__ import annotations
import difflib
import re
from pathlib import Path
from typing import Iterable

from tools import lint_wiki

from ..finding import Finding
from ..registry import Registry


def _selected(paths: Iterable[Path], vault: Path, root: Path) -> list[Path]:
    selected: list[Path] = []
    for raw in paths:
        path = raw if raw.is_absolute() else (root / raw)
        path = path.resolve()
        if path.is_dir():
            selected.extend(sorted(p for p in path.rglob("*.md") if p.is_file()))
        elif path.is_file() and path.suffix.lower() == ".md":
            selected.append(path)
    return sorted(set(selected))


def _rule(registry: Registry, rule_id: str):
    try:
        return registry.get(rule_id)
    except KeyError:
        return None


def _location(path: Path, root: Path, line: int = 1, text: str | None = None) -> dict[str, object]:
    try:
        filename = path.resolve().relative_to(root.resolve()).as_posix()
    except ValueError:
        filename = path.as_posix()
    result: dict[str, object] = {"file": filename, "line": max(1, line)}
    if text is not None:
        result["text"] = text
    return result


def _make(rule, *, path: Path, root: Path, evidence: str, line: int = 1,
          text: str | None = None, severity: str | None = None,
          evaluator: str = "symbolic") -> Finding:
    return Finding(rule_id=rule.id, result="fail", severity=severity or rule.severity,
                   location=_location(path, root, line, text), evidence=evidence,
                   reason=rule.message, repair_target=rule.repair, evaluator=evaluator)


def evaluate_symbolic(paths: Iterable[Path], registry: Registry, *, root: Path,
                       vault: Path | None = None, rule_ids: set[str] | None = None,
                       severity_overrides: dict[str, str] | None = None) -> list[Finding]:
    """Evaluate deterministic cross-page rules for selected Markdown files."""
    root = root.resolve()
    vault = (vault or root / "wiki").resolve()
    selected = _selected(paths, vault, root)
    selected_set = {p.resolve() for p in selected}
    findings: list[Finding] = []
    pages, lookup = lint_wiki.load(vault) if vault.is_dir() else ({}, {})

    def enabled(rule_id: str) -> bool:
        return rule_ids is None or rule_id in rule_ids

    # WIKI001/WIKI002 use the existing owner-schema parser without changing its output.
    # File mode also accepts paths outside the active vault. Parse their local
    # frontmatter so WIKI rules remain useful for generated, pre-filed output.
    for path in selected:
        try:
            relative = path.relative_to(vault).as_posix()
        except ValueError:
            relative = None
        if relative is not None and relative in pages:
            continue
        text = path.read_text(encoding="utf-8")
        block, fields = lint_wiki.frontmatter(text)
        missing = [key for key in (*lint_wiki.REQUIRED, *lint_wiki.CAMPAIGN_REQUIRED) if key not in fields]
        if missing and enabled("WIKI001"):
            rule = _rule(registry, "WIKI001")
            if rule:
                findings.append(_make(rule, path=path, root=root,
                                      evidence=f"Missing required frontmatter: {', '.join(missing)}",
                                      evaluator="lint_wiki"))
        bad = []
        if fields.get("type") and fields["type"].strip("\"'") not in lint_wiki.CAMPAIGN_TYPES:
            bad.append(f"type={fields['type']}")
        if bad and enabled("WIKI002"):
            rule = _rule(registry, "WIKI002")
            if rule:
                findings.append(_make(rule, path=path, root=root,
                                      evidence="Invalid owner field: " + ", ".join(bad),
                                      evaluator="lint_wiki"))

    for path in selected:
        try:
            relative = path.relative_to(vault).as_posix()
        except ValueError:
            continue
        page = pages.get(relative)
        if page is None:
            continue
        fields = page["fields"]
        missing = [key for key in (*lint_wiki.REQUIRED, *lint_wiki.CAMPAIGN_REQUIRED) if key not in fields]
        if missing and enabled("WIKI001"):
            rule = _rule(registry, "WIKI001")
            if rule:
                findings.append(_make(rule, path=path, root=root,
                                      evidence=f"Missing required frontmatter: {', '.join(missing)}",
                                      evaluator="lint_wiki"))
        bad = []
        if fields.get("type") and fields["type"].strip("\"'") not in lint_wiki.CAMPAIGN_TYPES:
            bad.append(f"type={fields['type']}")
        if bad and enabled("WIKI002"):
            rule = _rule(registry, "WIKI002")
            if rule:
                findings.append(_make(rule, path=path, root=root,
                                      evidence="Invalid owner field: " + ", ".join(bad),
                                      evaluator="lint_wiki"))

    # Cross-page links are evaluated only for selected source files.
    for rel, page in pages.items():
        source = Path(page["path"]).resolve()
        if source not in selected_set:
            continue
        body = page["text"]
        for match in re.finditer(r"(?<!!)\[\[([^\]]+)\]\]", body):
            raw = match.group(1).split("|", 1)[0].strip()
            targets = lint_wiki.resolve(raw, pages, lookup)
            line = body[:match.start()].count("\n") + 1
            normalized = lint_wiki.normalize(raw)
            if not targets:
                if enabled("RETRIEVAL001"):
                    rule = _rule(registry, "RETRIEVAL001")
                    if rule:
                        candidates = sorted({candidate for key, values in lookup.items()
                                             if normalized and len(key) >= 4
                                             and difflib.SequenceMatcher(None, normalized, key).ratio() >= 0.9
                                             for candidate in values})
                        repair = (f"Retarget [[{raw}]] to [[{candidates[0]}]]"
                                  if len(candidates) == 1 else None)
                        findings.append(Finding(rule_id=rule.id, result="fail", severity=rule.severity,
                                                location=_location(source, root, line, match.group(0)),
                                                evidence=f"Unresolved wikilink: [[{raw}]]",
                                                reason=rule.message, repair_target=repair,
                                                evaluator="lint_wiki"))
                continue
    return findings


def evaluate_templates(paths: Iterable[Path], *, root: Path,
                       rule_ids: set[str] | None = None) -> list[Finding]:
    """Evaluate template drift using the profile derived from the mapped template."""
    from ..template_profile import template_conformance

    findings: list[Finding] = []
    for path in _selected(paths, root / "wiki", root):
        _, page_findings = template_conformance(path, root=root)
        findings.extend(finding for finding in page_findings
                        if rule_ids is None or finding.rule_id in rule_ids)
    return findings
