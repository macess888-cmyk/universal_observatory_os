"""
Universal Observatory Operating System
Structural Inspection Service v0.1

Purpose:
Coordinate the Observatory's structural validators.

Boundary:
This service composes structural inspections.

It does not establish:

- truth
- authority
- causation
- correctness
- proof

UNKNOWN -> HOLD
"""

from __future__ import annotations

from typing import Any, Dict

from uos.services.validators.identity_validator import IdentityValidator
from uos.services.validators.registry_validator import RegistryValidator
from uos.services.validators.relationship_validator import RelationshipValidator
from uos.services.validators.evidence_validator import EvidenceValidator
from uos.services.validators.timeline_validator import TimelineValidator
from uos.services.validators.graph_validator import GraphValidator


class StructuralInspectionService:
    """
    Coordinates first-generation structural validators.
    """

    def inspect(
        self,
        identities,
        registry,
        relationships,
        evidence,
        timeline,
        graph,
    ) -> Dict[str, Any]:

        reports = {
            "identity": IdentityValidator(identities).validate(),
            "registry": RegistryValidator(registry).validate(),
            "relationships": RelationshipValidator(
                relationships
            ).validate(),
            "evidence": EvidenceValidator(
                evidence
            ).validate(),
            "timeline": TimelineValidator(
                timeline
            ).validate(),
            "graph": GraphValidator(
                graph
            ).validate(),
        }

        overall = "PASS"

        for report in reports.values():

            if report["status"] != "PASS":
                overall = "FAIL"
                break

        return {
            "inspection": "StructuralInspection",
            "status": overall,
            "reports": reports,
            "validator_count": len(reports),
            "boundary": (
                "STRUCTURAL_INSPECTION_DOES_NOT_IMPLY_TRUTH"
            ),
            "unknown_policy": "UNKNOWN -> HOLD",
        }