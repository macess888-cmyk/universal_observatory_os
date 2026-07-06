"""
Universal Observatory Operating System
Registry Engine v0.1

Purpose:
Create, store, retrieve, update, search, and export ObservableObjects.

Boundary:
Registry stores observations and objects.
Registry does not decide truth, authority, or explanation.
UNKNOWN -> HOLD
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional
from uos.kernel.identity import next_identity


REGISTRY_DIR = Path("data/registry")
REGISTRY_FILE = REGISTRY_DIR / "objects.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_registry() -> None:
    REGISTRY_DIR.mkdir(parents=True, exist_ok=True)
    if not REGISTRY_FILE.exists():
        REGISTRY_FILE.write_text("[]", encoding="utf-8")


def load_objects() -> List[Dict[str, Any]]:
    ensure_registry()
    return json.loads(REGISTRY_FILE.read_text(encoding="utf-8"))


def save_objects(objects: List[Dict[str, Any]]) -> None:
    ensure_registry()
    REGISTRY_FILE.write_text(json.dumps(objects, indent=2), encoding="utf-8")


def create_object(
    name: str,
    category: str,
    description: str = "",
    domain: str = "",
    scale: str = "",
    status: str = "unknown",
    tags: Optional[List[str]] = None,
) -> Dict[str, Any]:
    timestamp = now_iso()

    obj = {
        "id": next_identity(category),
        "name": name,
        "category": category,
        "description": description,
        "domain": domain,
        "scale": scale,
        "status": status,
        "created_at": timestamp,
        "updated_at": timestamp,
        "version": "0.1",
        "tags": tags or [],
        "relationships": [],
        "observations": [],
        "measurements": [],
        "evidence": [],
        "unknowns": [],
        "questions": [],
        "failures": [],
        "recoveries": [],
        "boundaries": [],
        "confidence": None,
        "uncertainty": None,
        "provenance": "manual_entry",
        "history": [f"{timestamp}: object created"],
        "references": [],
        "notes": "",
    }

    objects = load_objects()
    objects.append(obj)
    save_objects(objects)

    return obj


def get_object(object_id: str) -> Optional[Dict[str, Any]]:
    for obj in load_objects():
        if obj.get("id") == object_id:
            return obj
    return None


def list_objects() -> List[Dict[str, Any]]:
    return load_objects()


def search_objects(query: str) -> List[Dict[str, Any]]:
    query_lower = query.lower()
    results = []

    for obj in load_objects():
        searchable = " ".join(
            str(obj.get(field, ""))
            for field in [
                "id",
                "name",
                "category",
                "description",
                "domain",
                "scale",
                "status",
                "notes",
            ]
        ).lower()

        tags = " ".join(obj.get("tags", [])).lower()

        if query_lower in searchable or query_lower in tags:
            results.append(obj)

    return results


def update_object(object_id: str, updates: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    objects = load_objects()
    timestamp = now_iso()

    for index, obj in enumerate(objects):
        if obj.get("id") == object_id:
            for key, value in updates.items():
                if key not in ["id", "created_at"]:
                    obj[key] = value

            obj["updated_at"] = timestamp
            obj.setdefault("history", []).append(f"{timestamp}: object updated")
            objects[index] = obj
            save_objects(objects)
            return obj

    return None


def delete_object(object_id: str) -> bool:
    """
    Soft-delete by setting status to archived.
    Nothing is silently destroyed.
    """
    updated = update_object(object_id, {"status": "archived"})
    return updated is not None


def add_relationship(object_id: str, relationship: str) -> Optional[Dict[str, Any]]:
    obj = get_object(object_id)
    if obj is None:
        return None

    relationships = obj.get("relationships", [])
    relationships.append(relationship)

    return update_object(object_id, {"relationships": relationships})


def add_boundary(object_id: str, boundary: str) -> Optional[Dict[str, Any]]:
    obj = get_object(object_id)
    if obj is None:
        return None

    boundaries = obj.get("boundaries", [])
    boundaries.append(boundary)

    return update_object(object_id, {"boundaries": boundaries})


def add_unknown(object_id: str, unknown: str) -> Optional[Dict[str, Any]]:
    obj = get_object(object_id)
    if obj is None:
        return None

    unknowns = obj.get("unknowns", [])
    unknowns.append(unknown)

    return update_object(object_id, {"unknowns": unknowns})


def export_registry(export_path: str = "data/registry_export.json") -> str:
    objects = load_objects()
    path = Path(export_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(objects, indent=2), encoding="utf-8")
    return str(path)