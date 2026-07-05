"""
Universal Observatory Operating System
Knowledge Graph Engine v0.1

Purpose:
Provide graph traversal over ObservableObjects and Relationships.

Boundary:
Graph traversal discovers connected structure.
It does not establish truth, causation, authority, or explanation.

UNKNOWN -> HOLD
"""

from __future__ import annotations

from collections import deque
from typing import Dict, List, Set

from core.registry import list_objects
from engines.relationship import list_relationships


def object_index() -> Dict[str, dict]:
    """
    Fast lookup by object ID.
    """
    return {
        obj["id"]: obj
        for obj in list_objects()
    }


def relationship_index() -> List[dict]:
    return [
        rel
        for rel in list_relationships()
        if rel.get("status") != "archived"
    ]


def outgoing(object_id: str) -> List[dict]:
    return [
        rel
        for rel in relationship_index()
        if rel["source"] == object_id
    ]


def incoming(object_id: str) -> List[dict]:
    return [
        rel
        for rel in relationship_index()
        if rel["target"] == object_id
    ]


def neighbors(object_id: str) -> List[str]:

    ids = set()

    for rel in outgoing(object_id):
        ids.add(rel["target"])

    for rel in incoming(object_id):
        ids.add(rel["source"])

    return sorted(ids)


def degree(object_id: str) -> int:
    return len(neighbors(object_id))


def one_hop(object_id: str):

    graph = object_index()

    results = []

    for neighbor in neighbors(object_id):

        if neighbor in graph:

            results.append(graph[neighbor])

    return results


def bfs(start_id: str,
        max_depth: int = 3):

    graph = object_index()

    visited: Set[str] = set()

    queue = deque()

    queue.append((start_id, 0))

    traversal = []

    while queue:

        node, depth = queue.popleft()

        if node in visited:
            continue

        visited.add(node)

        traversal.append({
            "depth": depth,
            "id": node,
            "name": graph.get(node, {}).get("name", "UNKNOWN")
        })

        if depth >= max_depth:
            continue

        for nxt in neighbors(node):

            if nxt not in visited:

                queue.append((nxt, depth + 1))

    return traversal


def graph_statistics():

    objects = list_objects()

    relationships = relationship_index()

    return {

        "objects": len(objects),

        "relationships": len(relationships),

        "average_degree":

            (
                sum(
                    degree(obj["id"])
                    for obj in objects
                )
                / len(objects)
            )

            if objects else 0
    }

def dangling_relationships() -> List[dict]:
    """
    Return relationships where source or target does not exist
    in the object registry.
    """
    graph = object_index()
    dangling = []

    for rel in relationship_index():
        source_exists = rel["source"] in graph
        target_exists = rel["target"] in graph

        if not source_exists or not target_exists:
            dangling.append({
                "relationship_id": rel["id"],
                "source": rel["source"],
                "target": rel["target"],
                "type": rel["type"],
                "source_exists": source_exists,
                "target_exists": target_exists,
            })

    return dangling