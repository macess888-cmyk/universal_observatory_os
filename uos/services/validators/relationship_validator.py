"""
Universal Observatory Operating System
Relationship Validator v0.1

Purpose:
Validate structural integrity of observable relationships.

Boundary:
Validation evaluates structural consistency only.

Validation does not establish:

- truth
- authority
- causation
- correctness
- proof

UNKNOWN -> HOLD
"""

from __future__ import annotations

from typing import Any, Dict

from uos.services.validatable import Validatable


class RelationshipValidator(Validatable):
    """
    Validates relationship records.

    Checks:

    - source exists
    - target exists
    - relationship type exists
    """

    def __init__(self, relationships):
        self.relationships = relationships

    def validate(self) -> Dict[str, Any]:

        missing_source = 0
        missing_target = 0
        missing_type = 0

        for rel in self.relationships:

            if not rel.get("source"):
                missing_source += 1

            if not rel.get("target"):
                missing_target += 1

            if not rel.get("relationship"):
                missing_type += 1

        status = "PASS"

        if (
            missing_source
            or missing_target
            or missing_type
        ):
            status = "FAIL"

        return {
            "validator": "RelationshipValidator",
            "status": status,
            "relationships": len(self.relationships),
            "missing_source": missing_source,
            "missing_target": missing_target,
            "missing_relationship": missing_type,
            "boundary": "VALIDATION_DOES_NOT_IMPLY_CAUSATION",
            "unknown_policy": "UNKNOWN -> HOLD",
        }