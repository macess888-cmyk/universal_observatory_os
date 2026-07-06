"""
Universal Observatory Operating System
Graph Validator v0.1

Purpose:
Validate structural integrity of an observable graph.

Boundary:
Validation evaluates graph structure only.

Validation does not establish:

- truth
- authority
- causation
- interpretation
- completeness

UNKNOWN -> HOLD
"""

from __future__ import annotations

from typing import Any, Dict

from uos.services.validatable import Validatable


class GraphValidator(Validatable):

    def __init__(self, graph):
        self.graph = graph

    def validate(self) -> Dict[str, Any]:

        missing_nodes = 0
        missing_edges = 0

        if "nodes" not in self.graph:
            missing_nodes = 1

        if "edges" not in self.graph:
            missing_edges = 1

        node_count = len(self.graph.get("nodes", []))
        edge_count = len(self.graph.get("edges", []))

        status = "PASS"

        if missing_nodes or missing_edges:
            status = "FAIL"

        return {
            "validator": "GraphValidator",
            "status": status,
            "nodes": node_count,
            "edges": edge_count,
            "missing_nodes": missing_nodes,
            "missing_edges": missing_edges,
            "boundary": "VALIDATION_DOES_NOT_IMPLY_GRAPH_CORRECTNESS",
            "unknown_policy": "UNKNOWN -> HOLD",
        }