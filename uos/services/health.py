"""
Universal Observatory Operating System
Health Service v0.1

Purpose:
Inspect the observable health of the Observatory.

Boundary:
Health reports structural condition.
Health does not establish truth, correctness, authority, or proof.

UNKNOWN -> HOLD
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Dict, Optional

from .inspectable import Inspectable


class HealthService(Inspectable):
    """
    Aggregates inspection reports from Observatory components.
    """

    def __init__(
        self,
        registry: Optional[Inspectable] = None,
        relationship_registry: Optional[Inspectable] = None,
        timeline: Optional[Inspectable] = None,
        graph: Optional[Inspectable] = None,
        evidence_registry: Optional[Inspectable] = None,
    ):
        self.registry = registry
        self.relationship_registry = relationship_registry
        self.timeline = timeline
        self.graph = graph
        self.evidence_registry = evidence_registry

    def _inspect_component(
        self,
        name: str,
        component: Optional[Inspectable],
    ) -> Dict[str, Any]:
        if component is None:
            return {
                "component": name,
                "status": "NOT_ATTACHED",
            }

        try:
            return {
                "component": name,
                "status": "OBSERVED",
                "report": component.inspect(),
            }
        except Exception as exc:
            return {
                "component": name,
                "status": "INSPECTION_ERROR",
                "error": str(exc),
            }

    def inspect(self) -> Dict[str, Any]:
        components = {
            "registry": self.registry,
            "relationship_registry": self.relationship_registry,
            "timeline": self.timeline,
            "graph": self.graph,
            "evidence_registry": self.evidence_registry,
        }

        reports = {
            name: self._inspect_component(name, component)
            for name, component in components.items()
        }

        attached = sum(
            1 for report in reports.values()
            if report["status"] == "OBSERVED"
        )

        errors = sum(
            1 for report in reports.values()
            if report["status"] == "INSPECTION_ERROR"
        )

        return {
            "service": "HealthService",
            "version": "v0.1",
            "status": "OBSERVED",
            "inspection_time": datetime.now(timezone.utc).isoformat(),
            "components_total": len(components),
            "components_attached": attached,
            "inspection_errors": errors,
            "components": reports,
            "boundary": "HEALTH_DOES_NOT_IMPLY_CORRECTNESS",
            "unknown_policy": "UNKNOWN -> HOLD",
        }