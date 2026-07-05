"""
Universal Observatory Operating System
Timeline Engine v0.1

Purpose:
Record immutable events for objects, relationships, failures, recoveries,
questions, observations, and other Observatory activity.

Boundary:
Timeline records that something happened.
Timeline does not establish truth, causation, authority, or explanation.

UNKNOWN -> HOLD
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from engines.identity import next_identity


TIMELINE_DIR = Path("data/timeline")
TIMELINE_FILE = TIMELINE_DIR / "events.json"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def ensure_store() -> None:
    TIMELINE_DIR.mkdir(parents=True, exist_ok=True)
    if not TIMELINE_FILE.exists():
        TIMELINE_FILE.write_text("[]", encoding="utf-8")


def load_events() -> List[Dict[str, Any]]:
    ensure_store()
    return json.loads(TIMELINE_FILE.read_text(encoding="utf-8"))


def save_events(events: List[Dict[str, Any]]) -> None:
    ensure_store()
    TIMELINE_FILE.write_text(json.dumps(events, indent=2), encoding="utf-8")


def record_event(
    subject_id: str,
    event_type: str,
    description: str,
    actor: str = "system",
    evidence: Optional[List[str]] = None,
    metadata: Optional[Dict[str, Any]] = None,
) -> Dict[str, Any]:
    timestamp = now_iso()

    event = {
        "id": next_identity("event"),
        "subject_id": subject_id,
        "event_type": event_type.upper(),
        "description": description,
        "actor": actor,
        "created_at": timestamp,
        "evidence": evidence or [],
        "metadata": metadata or {},
        "boundaries": [],
        "status": "recorded",
        "version": "0.1",
        "notes": "",
    }

    events = load_events()
    events.append(event)
    save_events(events)

    return event


def list_events() -> List[Dict[str, Any]]:
    return load_events()


def events_for_subject(subject_id: str) -> List[Dict[str, Any]]:
    return [
        event
        for event in load_events()
        if event.get("subject_id") == subject_id
    ]


def search_events(query: str) -> List[Dict[str, Any]]:
    query_lower = query.lower()
    results = []

    for event in load_events():
        searchable = " ".join(
            str(event.get(field, ""))
            for field in [
                "id",
                "subject_id",
                "event_type",
                "description",
                "actor",
                "status",
                "notes",
            ]
        ).lower()

        if query_lower in searchable:
            results.append(event)

    return results


def add_boundary(event_id: str, boundary: str) -> Optional[Dict[str, Any]]:
    events = load_events()

    for index, event in enumerate(events):
        if event.get("id") == event_id:
            event.setdefault("boundaries", []).append(boundary)
            events[index] = event
            save_events(events)
            return event

    return None