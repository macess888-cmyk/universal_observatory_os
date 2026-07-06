"""
Universal Observatory Operating System
Formation Report v0.1

Purpose:
Produce a stable report from a completed Formation Inspection.

Boundary:
Reports preserve inspection results.

Reports do not establish:

- truth
- authority
- correctness
- causation
- explanation

UNKNOWN -> HOLD
"""

from __future__ import annotations

from typing import Any, Dict
from copy import deepcopy


class FormationReport:
    """
    Immutable-style report wrapper for Formation Inspection.
    """

    def create(
        self,
        inspection_report: Dict[str, Any],
    ) -> Dict[str, Any]:

        report = deepcopy(inspection_report)

        return {
            "report": "FormationReport",
            "status": report["status"],
            "formation_name": report["formation_name"],
            "inspection": report["inspection"],
            "structural_report": report["structural_report"],
            "boundary":
                "REPORT_DOES_NOT_IMPLY_INTERPRETATION",
            "unknown_policy": "UNKNOWN -> HOLD",
        }