"""
Universal Observatory Operating System
Identity Validator v0.1

Purpose:
Validate Observatory identity integrity.

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

import re
from typing import Any, Dict, Iterable

from uos.services.validatable import Validatable


IDENTITY_PATTERN = re.compile(r"^[A-Z]{3,5}-\d{9}$")


class IdentityValidator(Validatable):
    """
    Validates Observatory identities.

    Checks:

    - format
    - uniqueness
    - presence
    """

    def __init__(self, identities: Iterable[str]):
        self.identities = list(identities)

    def validate(self) -> Dict[str, Any]:

        duplicate_ids = set()
        seen = set()

        invalid_format = []

        missing = 0

        for identity in self.identities:

            if not identity:
                missing += 1
                continue

            if identity in seen:
                duplicate_ids.add(identity)

            seen.add(identity)

            if not IDENTITY_PATTERN.match(identity):
                invalid_format.append(identity)

        status = "PASS"

        if duplicate_ids or invalid_format or missing:
            status = "FAIL"

        return {
            "validator": "IdentityValidator",
            "status": status,
            "total": len(self.identities),
            "duplicates": sorted(duplicate_ids),
            "invalid_format": invalid_format,
            "missing": missing,
            "boundary": "VALIDATION_DOES_NOT_IMPLY_TRUTH",
        }