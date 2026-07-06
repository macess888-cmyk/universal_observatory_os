"""
Universal Observatory Operating System
Relationship Engine v0.1

Purpose:
Create, manage, inspect, and search relationships between
ObservableObjects.

Boundary:
Relationships represent observed or asserted connections.
They do not establish causation, authority, or truth.

UNKNOWN -> HOLD
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from uos.kernel.identity import next_identity


RELATIONSHIP_DIR = Path("data/relationships")
RELATIONSHIP_FILE = RELATIONSHIP_DIR / "relationships.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_store() -> None:
    RELATIONSHIP_DIR.mkdir(parents=True, exist_ok=True)
    if not RELATIONSHIP_FILE.exists():
        RELATIONSHIP_FILE.write_text("[]", encoding="utf-8")


def load_relationships() -> List[Dict[str, Any]]:
    ensure_store()
    return json.loads(RELATIONSHIP_FILE.read_text(encoding="utf-8"))


def save_relationships(data: List[Dict[str, Any]]) -> None:
    ensure_store()
    RELATIONSHIP_FILE.write_text(
        json.dumps(data, indent=2),
        encoding="utf-8",
    )


def create_relationship(
    source_id: str,
    relationship_type: str,
    target_id: str,
    confidence: Optional[float] = None,
    evidence: Optional[List[str]] = None,
    notes: str = "",
) -> Dict[str, Any]:

    timestamp = now_iso()

    relationship = {
        "id": next_identity("relationship"),
        "source": source_id,
        "type": relationship_type.upper(),
        "target": target_id,
        "created_at": timestamp,
        "updated_at": timestamp,
        "confidence": confidence,
        "evidence": evidence or [],
        "boundaries": [],
        "history": [
            f"{timestamp}: relationship created"
        ],
        "notes": notes,
        "status": "observed",
        "version": "0.1",
    }

    relationships = load_relationships()
    relationships.append(relationship)
    save_relationships(relationships)

    return relationship


def list_relationships() -> List[Dict[str, Any]]:
    return load_relationships()


def get_relationship(
    relationship_id: str,
) -> Optional[Dict[str, Any]]:

    for rel in load_relationships():
        if rel["id"] == relationship_id:
            return rel

    return None


def relationships_for_object(
    object_id: str,
) -> List[Dict[str, Any]]:

    return [
        rel
        for rel in load_relationships()
        if rel["source"] == object_id
        or rel["target"] == object_id
    ]


def search_relationship_type(
    relationship_type: str,
) -> List[Dict[str, Any]]:

    relationship_type = relationship_type.upper()

    return [
        rel
        for rel in load_relationships()
        if rel["type"] == relationship_type
    ]


def add_boundary(
    relationship_id: str,
    boundary: str,
) -> Optional[Dict[str, Any]]:

    relationships = load_relationships()

    timestamp = now_iso()

    for index, rel in enumerate(relationships):

        if rel["id"] == relationship_id:

            rel.setdefault("boundaries", []).append(boundary)
            rel.setdefault("history", []).append(
                f"{timestamp}: boundary added ({boundary})"
            )

            rel["updated_at"] = timestamp

            relationships[index] = rel
            save_relationships(relationships)

            return rel

    return None


def update_relationship_status(
    relationship_id: str,
    status: str,
) -> Optional[Dict[str, Any]]:

    relationships = load_relationships()
    timestamp = now_iso()

    for index, rel in enumerate(relationships):
        if rel["id"] == relationship_id:
            rel["status"] = status
            rel["updated_at"] = timestamp
            rel.setdefault("history", []).append(
                f"{timestamp}: relationship status changed to {status}"
            )
            relationships[index] = rel
            save_relationships(relationships)
            return rel

    return None