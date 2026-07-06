"""
Universal Observatory Operating System
Formation Inspection Service v0.1

Purpose:
Inspect an observable Formation as a coherent structure.

Boundary:
Formation inspection composes existing structural inspections.

It does not establish:

- truth
- authority
- explanation
- prediction
- causation

UNKNOWN -> HOLD
"""

from __future__ import annotations

from typing import Any, Dict

from uos.services.structural_inspection import (
    StructuralInspectionService,
)


class FormationInspectionService:
    """
    First-generation Formation inspection.
    """

    def __init__(self):
        self.structural = StructuralInspectionService()

    def inspect(self, formation: Dict[str, Any]) -> Dict[str, Any]:

        structural_report = self.structural.inspect(
            identities=formation.get("identities", []),
            registry=formation.get("registry", []),
            relationships=formation.get("relationships", []),
            evidence=formation.get("evidence", []),
            timeline=formation.get("timeline", []),
            graph=formation.get(
                "graph",
                {"nodes": [], "edges": []},
            ),
        )

        status = structural_report["status"]

        return {
            "inspection": "FormationInspection",
            "status": status,
            "formation_name": formation.get(
                "name",
                "Unnamed Formation",
            ),
            "structural_report": structural_report,
            "boundary": (
                "FORMATION_INSPECTION_DOES_NOT_IMPLY_UNDERSTANDING"
            ),
            "unknown_policy": "UNKNOWN -> HOLD",
        }