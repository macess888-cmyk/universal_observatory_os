"""
Universal Observatory Operating System
Identity Engine v0.1

Purpose:
Generate stable human-readable object identifiers.

Boundary:
Identity provides traceability.
Identity does not establish truth, authority, or validity.

UNKNOWN -> HOLD
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict


IDENTITY_DIR = Path("data/identity")
COUNTERS_FILE = IDENTITY_DIR / "counters.json"


PREFIX_MAP: Dict[str, str] = {
    "object": "OBJ",
    "instrument": "INST",
    "observation": "OBS",
    "evidence": "EVID",
    "unknown": "UNKN",
    "question": "QUES",
    "failure": "FAIL",
    "recovery": "RECV",
    "mission": "MISS",
    "dataset": "DATA",
    "publication": "PUB",
    "model": "MODL",
    "theory": "THRY",
    "simulation": "SIM",
    "relationship": "REL",
    "boundary": "BND",
    "event": "EVT",
}


def ensure_identity_store() -> None:
    IDENTITY_DIR.mkdir(parents=True, exist_ok=True)
    if not COUNTERS_FILE.exists():
        COUNTERS_FILE.write_text("{}", encoding="utf-8")


def load_counters() -> Dict[str, int]:
    ensure_identity_store()
    return json.loads(COUNTERS_FILE.read_text(encoding="utf-8"))


def save_counters(counters: Dict[str, int]) -> None:
    ensure_identity_store()
    COUNTERS_FILE.write_text(json.dumps(counters, indent=2), encoding="utf-8")


def prefix_for_category(category: str) -> str:
    normalized = category.strip().lower()
    return PREFIX_MAP.get(normalized, "OBJ")


def next_identity(category: str = "object") -> str:
    """
    Generate the next stable readable ID for a category.

    Example:
    instrument -> INST-000000001
    question   -> QUES-000000001
    failure    -> FAIL-000000001
    """
    prefix = prefix_for_category(category)
    counters = load_counters()

    current = counters.get(prefix, 0) + 1
    counters[prefix] = current

    save_counters(counters)

    return f"{prefix}-{current:09d}"


def peek_next_identity(category: str = "object") -> str:
    """
    Show what the next identity would be without incrementing.
    """
    prefix = prefix_for_category(category)
    counters = load_counters()
    current = counters.get(prefix, 0) + 1
    return f"{prefix}-{current:09d}"


def reset_identity_counters() -> None:
    """
    Development helper.
    Use only before production data exists.
    """
    save_counters({})