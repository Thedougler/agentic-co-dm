"""Typed, agent-safe wiki operation primitives."""

from .scope import Scope, parse_scope
from .mutations import MutationOp, RepairPlan

__all__ = ["Scope", "parse_scope", "MutationOp", "RepairPlan"]
