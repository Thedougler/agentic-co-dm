"""Typed, agent-safe wiki operation primitives."""

from .cli import EXIT_ERROR, EXIT_OK, EXIT_REJECTED, configured_vault, emit_json, resolve_vault
from .identity import PageIdentity, resolve_identity, scan_identities
from .index_ops import insert_index_entry, mutate_index, parse_index, remove_index_entry, replace_index_entry
from .manifest_ops import ManifestTransition, apply_transition, update_manifest
from .mutations import MutationOp, RepairPlan, apply_mutation, parse_sections, section_hash
from .repair_plans import build_plan, plan_json, snapshot
from .scope import Scope, parse_scope
from .template_contracts import TemplateContract, check_conformance, contract_for_type, load_contract

from .transactions import Transaction

__all__ = [
    "EXIT_ERROR",
    "EXIT_OK",
    "EXIT_REJECTED",
    "configured_vault",
    "emit_json",
    "resolve_vault",
    "PageIdentity",
    "resolve_identity",
    "scan_identities",
    "Scope",
    "parse_scope",
    "MutationOp",
    "RepairPlan",
    "apply_mutation",
    "parse_sections",
    "section_hash",
    "Transaction",
    "TemplateContract",
    "load_contract",
    "contract_for_type",
    "check_conformance",
    "build_plan",
    "plan_json",
    "snapshot",
    "parse_index",
    "replace_index_entry",
    "remove_index_entry",
    "insert_index_entry",
    "mutate_index",
    "ManifestTransition",
    "apply_transition",
    "update_manifest",
]
