"""Cross-page symbolic checks built on the existing wiki lint loader."""
from __future__ import annotations

import datetime as dt
import re
from pathlib import Path
from typing import Iterable

from tools import lint_wiki

from ..finding import Finding
from ..registry import Registry


def _selected(paths: Iterable[Path], vault: Path) -> list[Path]:
    selected: list[Path] = []
    for raw in paths:
        path = raw if raw.is_absolute() else (Path.cwd() / raw)
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
          text: str | None = None, severity: str | None = None) -> Finding:
    return Finding(rule_id=rule.id, result="fail", severity=severity or rule.severity,
                   location=_location(path, root, line, text), evidence=evidence,
                   reason=rule.message, repair_target=rule.repair, evaluator="symbolic")


def evaluate_symbolic(paths: Iterable[Path], registry: Registry, *, root: Path,
                       vault: Path | None = None, rule_ids: set[str] | None = None,
                       severity_overrides: dict[str, str] | None = None) -> list[Finding]:
    """Evaluate deterministic cross-page rules for selected Markdown files."""
    vault = (vault or root / "wiki").resolve()
    selected = _selected(paths, vault)
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
                                      evidence=f"Missing required frontmatter: {', '.join(missing)}"))
        bad = []
        if fields.get("type") and fields["type"].strip("\"'") not in lint_wiki.CAMPAIGN_TYPES:
            bad.append(f"type={fields['type']}")
        if fields.get("lifecycle") and fields["lifecycle"].strip("\"'") not in lint_wiki.DEFAULT_LIFECYCLES:
            bad.append(f"lifecycle={fields['lifecycle']}")
        if bad and enabled("WIKI002"):
            rule = _rule(registry, "WIKI002")
            if rule:
                findings.append(_make(rule, path=path, root=root,
                                      evidence="Invalid owner field: " + ", ".join(bad)))

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
                                      evidence=f"Missing required frontmatter: {', '.join(missing)}"))
        bad = []
        if fields.get("type") and fields["type"].strip("\"'") not in lint_wiki.CAMPAIGN_TYPES:
            bad.append(f"type={fields['type']}")
        if fields.get("lifecycle") and fields["lifecycle"].strip("\"'") not in lint_wiki.DEFAULT_LIFECYCLES:
            bad.append(f"lifecycle={fields['lifecycle']}")
        if bad and enabled("WIKI002"):
            rule = _rule(registry, "WIKI002")
            if rule:
                findings.append(_make(rule, path=path, root=root,
                                      evidence="Invalid owner field: " + ", ".join(bad)))

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
            if not targets and enabled("RETRIEVAL001"):
                rule = _rule(registry, "RETRIEVAL001")
                if rule:
                    findings.append(_make(rule, path=source, root=root, line=line, text=match.group(0),
                                          evidence=f"Unresolved wikilink: [[{raw}]]"))
                continue
            target = pages[targets[0]]
            target_path = Path(target["path"])
            target_fields = target["fields"]
            lifecycle = str(target_fields.get("lifecycle", "")).strip("\"'").lower()
            if lifecycle in {"rejected", "dead"} and enabled("CANON001"):
                rule = _rule(registry, "CANON001")
                if rule:
                    findings.append(_make(rule, path=source, root=root, line=line, text=match.group(0),
                                          evidence=f"{raw} resolves to {target_path.relative_to(vault)} with lifecycle={lifecycle}"))
            source_type = str(page["fields"].get("type", "")).strip("\"'")
            is_prep = "session" in source.as_posix().lower() or source_type == "session-prep"
            updated = str(target_fields.get("updated", "")).strip("\"'")[:10]
            try:
                age = (dt.date.today() - dt.date.fromisoformat(updated)).days
            except ValueError:
                age = 0
            if is_prep and age > 30 and enabled("CANON002"):
                rule = _rule(registry, "CANON002")
                if rule:
                    findings.append(_make(rule, path=source, root=root, line=line, text=match.group(0),
                                          evidence=f"{raw} canonical page updated {updated} ({age} days stale)"))
    return findings
