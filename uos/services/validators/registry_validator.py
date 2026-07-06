"""
Universal Observatory Operating System
Registry Validator v0.1

Purpose:
Validate the structural integrity of an Observatory Registry.

Boundary:
Validation evaluates structural consistency only.

Validation does not establish:
- truth
- authority
- correctness
- proof

UNKNOWN -> HOLD
"""

from __future__ import annotations

from typing import Any, Dict

from uos.services.validatable import Validatable


class RegistryValidator(Validatable):
    """
    Validates a registry of observable objects.

    Checks:

    - unique identities
    - missing identities
    - total object count
    """

    def __init__(self, registry):
        self.registry = registry

    def validate(self) -> Dict[str, Any]:

        duplicate_ids = []
        missing_ids = []

        seen = set()

        total = 0

        for obj in self.registry:

            total += 1

            identity = obj.get("identity")

            if not identity:
                missing_ids.append(obj)
                continue

            if identity in seen:
                duplicate_ids.append(identity)

            seen.add(identity)

        status = "PASS"

        if duplicate_ids or missing_ids:
            status = "FAIL"

        return {
            "validator": "RegistryValidator",
            "status": status,
            "objects": total,
            "duplicates": sorted(set(duplicate_ids)),
            "missing_identity": len(missing_ids),
            "boundary": "VALIDATION_DOES_NOT_IMPLY_TRUTH",
            "unknown_policy": "UNKNOWN -> HOLD",
        }