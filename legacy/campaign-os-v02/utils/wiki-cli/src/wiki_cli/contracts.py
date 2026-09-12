"""Core types every rule, producer, and command in the CLI is written against.

A rule is a class, not a function: it carries its own identity, tier, severity,
and remediation text, and stamps them onto every finding it emits. `fix` lives
on the rule and is reported once per rule; `message` lives on the finding and
says what is wrong at one line. That split is what keeps a whole-vault report
readable instead of repeating the same remediation paragraph per hit.
"""

from __future__ import annotations

import abc
from collections.abc import Callable, Iterable, Iterator, Mapping, Sequence
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path
from typing import ClassVar, Literal, NamedTuple, Protocol, runtime_checkable


class Tier(StrEnum):
    """Blast radius. Tiers run in declaration order and gate the next one."""

    STRUCTURAL = "structural"
    CONTENT_SHAPE = "content-shape"
    PROSE = "prose"


TIER_ORDER: tuple[Tier, ...] = (Tier.STRUCTURAL, Tier.CONTENT_SHAPE, Tier.PROSE)


class Severity(StrEnum):
    """Every finding gates the exit code. WARNING may be baselined as debt
    (ADR-0062); ERROR never may."""

    ERROR = "error"
    WARNING = "warning"


class When(StrEnum):
    """The moment a rule earns its runtime.

    EDIT answers "is the file I just wrote correct?" from that file alone.
    SWEEP answers a question shaped by the whole corpus or by git history —
    duplication across pages, a summary that drifted from a body, a page
    whose `updated:` went stale. A SWEEP rule is worth running on a
    scheduled or whole-vault pass, not after every edit.
    """

    EDIT = "edit"
    SWEEP = "sweep"


@dataclass(frozen=True, slots=True)
class Autofix:
    """A pure text -> text repair for one rule.

    `apply` takes the file's whole raw text and returns the repaired text.
    It must be idempotent: `apply(apply(x)) == apply(x)`. `scope` names
    what part of the file it is allowed to touch — "frontmatter" repairs
    keys and values above the `---` fence, "syntax" repairs markup and must
    leave the body's word sequence unchanged.
    """

    scope: Literal["frontmatter", "syntax"]
    apply: Callable[[str], str]


class ProducerRuleDoc(NamedTuple):
    """A `BaseRule`'s reportable metadata for a rule id an external producer
    emits instead of a registered rule class.

    A producer is a plain `run()` function, not a `BaseRule` subclass, so its
    rule ids never reach `_REGISTRY` and `report.fix_text` has no `fix`
    text to print for them. Each producer module declares one of these per
    rule id it emits (`RULE_DOCS`, collected by
    `wiki_cli.producers.all_rule_docs`); `tier` and `severity` name what the
    family reports at, which for a producer whose per-finding severity varies
    (vale, oxlint, dndsim) is its gating default, not a promise about every
    finding.
    """

    id: str
    tier: Tier
    severity: Severity
    fix: str
    when: When = When.EDIT
    """Matches `BaseRule.when` — SWEEP for a producer whose question is
    corpus- or git-shaped rather than answerable from one edited file."""

    @property
    def baselineable(self) -> bool:
        """Matches `BaseRule.baselineable`: warnings may be baselined, errors
        never are."""
        return self.severity is Severity.WARNING


@dataclass(frozen=True, slots=True)
class Page:
    """One markdown file, parsed once and shared by every rule that sees it."""

    rel_path: str
    raw: str
    frontmatter: Mapping[str, object]
    body: str
    body_start_line: int
    """1-indexed line of the file at which `body` begins."""
    frontmatter_lines: Mapping[str, int] = field(default_factory=dict)
    """Top-level frontmatter key -> 1-indexed line, so findings point at the real key."""
    parse_error: str | None = None
    """Set when the frontmatter block exists but is not valid YAML. Unparseable
    frontmatter is a finding for a rule to report, never a crash mid-sweep."""

    @property
    def type(self) -> str | None:
        value = self.frontmatter.get("type")
        return value if isinstance(value, str) else None

    @property
    def slug(self) -> str:
        return Path(self.rel_path).stem

    def line_of(self, key: str) -> int:
        """Line of a top-level frontmatter key, or 1 when it is absent."""
        return self.frontmatter_lines.get(key, 1)

    def body_lines(self) -> Iterator[tuple[int, str]]:
        """(1-indexed file line, text) for each body line — never body-relative."""
        for offset, text in enumerate(self.body.splitlines()):
            yield self.body_start_line + offset, text


@dataclass(frozen=True, slots=True)
class Finding:
    """One problem at one place. Carries everything a report or fixer needs."""

    rule_id: str
    file: str
    line: int
    message: str
    severity: Severity
    tier: Tier
    producer: str
    column: int = 1
    fixable: bool = False


@runtime_checkable
class Corpus(Protocol):
    """The vault, indexed once per run. Implemented by `wiki_cli.index`."""

    repo_root: Path

    def pages(self) -> Sequence[Page]: ...

    def resolve(self, name: str) -> Page | None:
        """Resolve a wikilink target (slug, alias, or title) case-insensitively."""
        ...

    def by_type(self, page_type: str) -> Sequence[Page]: ...

    def links_from(self, rel_path: str) -> Sequence[str]:
        """Wikilink targets appearing in this page, as written."""
        ...

    def links_to(self, rel_path: str) -> Sequence[str]:
        """Relative paths of pages whose wikilinks resolve to this page."""
        ...


class BaseRule(abc.ABC):
    """Identity and metadata shared by both rule protocols."""

    id: ClassVar[str]
    tier: ClassVar[Tier]
    severity: ClassVar[Severity]
    fix: ClassVar[str]
    """Remediation, emitted once per rule in the report legend."""
    producer: ClassVar[str] = "wiki"
    fixable: ClassVar[bool] = False
    pure: ClassVar[bool] = False
    """True only when the result depends on this file's bytes alone — the sole
    precondition under which a finding may be cached against a content hash."""
    version: ClassVar[str] = "1"
    """Bump when the rule's logic changes; participates in the cache key."""
    when: ClassVar[When] = When.EDIT
    """EDIT for a rule answerable from the edited file; SWEEP for one whose
    question is corpus- or git-shaped."""
    baselineable: ClassVar[bool] = False
    """True when existing hits may be frozen into a baseline instead of fixed.
    Set automatically from `severity` — warnings yes, errors never — unless a
    subclass declares it in its own class body."""
    autofix: ClassVar[Autofix | None] = None
    """A pure text -> text repair, when this rule has one."""

    def __init_subclass__(cls, **kwargs: object) -> None:
        """Derive `baselineable` from `severity` so no rule hand-declares it."""
        super().__init_subclass__(**kwargs)
        if "baselineable" in cls.__dict__:
            return
        severity = getattr(cls, "severity", None)
        if severity is not None:
            cls.baselineable = severity is Severity.WARNING

    def finding(
        self,
        *,
        file: str,
        line: int,
        message: str,
        column: int = 1,
        fixable: bool | None = None,
        severity: Severity | None = None,
    ) -> Finding:
        """`severity` is a per-finding override for a rule that checks
        several distinct contracts under one id — W139 reports its missing
        lifecycle/pressure/if_ignored fields at its own severity and its
        prescribed-player-action phrasing at a lower one."""
        return Finding(
            rule_id=self.id,
            file=file,
            line=line,
            message=message,
            severity=self.severity if severity is None else severity,
            tier=self.tier,
            producer=self.producer,
            column=column,
            fixable=self.fixable if fixable is None else fixable,
        )


class FileRule(BaseRule):
    """Judges one page. Gets the corpus too, but must not depend on it when `pure`."""

    page_level: ClassVar[bool] = True
    """True when this rule requires page-schema frontmatter (type:, etc.).
    Fragment files (matching wiki.toml CALLOUT_FRAGMENT_PATTERN) skip all
    page_level rules, checked centrally in orchestrator.py rather than
    per-rule so new rules are excluded automatically."""

    @abc.abstractmethod
    def check(self, page: Page, corpus: Corpus) -> Iterable[Finding]: ...


class VaultRule(BaseRule):
    """Judges the corpus as a whole — duplicate basenames, graph integrity, orphans."""

    pure: ClassVar[bool] = False

    @abc.abstractmethod
    def check(self, corpus: Corpus) -> Iterable[Finding]: ...


_REGISTRY: dict[str, BaseRule] = {}


def register[R: BaseRule](cls: type[R]) -> type[R]:
    """Class decorator. Instantiates the rule once and files it by id."""
    instance: BaseRule = cls()
    if instance.id in _REGISTRY:
        raise ValueError(f"duplicate rule id {instance.id!r}")
    _REGISTRY[instance.id] = instance
    return cls


def registry() -> Mapping[str, BaseRule]:
    return dict(_REGISTRY)


def all_rules() -> list[BaseRule]:
    return sorted(_REGISTRY.values(), key=lambda r: (TIER_ORDER.index(r.tier), r.id))
