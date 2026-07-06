"""
Universal Observatory Operating System
Validation Service v0.1

Purpose:
Validate structural consistency across Observatory components.

Boundary:
Validation checks internal consistency.
Validation does not establish truth, authority, correctness, or proof.

UNKNOWN -> HOLD
"""

from __future__ import annotations

from datetime import datetime, timezone
from typing import Any, Callable, Dict, List

from .inspectable import Inspectable


Validator = Callable[[], Dict[str, Any]]


class ValidationService(Inspectable):
    """
    Aggregates structural validation reports.

    Validators should return structured reports and avoid
    interpretive or authoritative claims.
    """

    def __init__(self):
        self.validators: Dict[str, Validator] = {}

    def register_validator(self, name: str, validator: Validator) -> None:
        self.validators[name] = validator

    def run_validator(self, name: str, validator: Validator) -> Dict[str, Any]:
        try:
            report = validator()
            return {
                "validator": name,
                "status": report.get("status", "OBSERVED"),
                "report": report,
            }
        except Exception as exc:
            return {
                "validator": name,
                "status": "VALIDATION_ERROR",
                "error": str(exc),
            }

    def inspect(self) -> Dict[str, Any]:
        reports = {
            name: self.run_validator(name, validator)
            for name, validator in self.validators.items()
        }

        errors = [
            name
            for name, report in reports.items()
            if report["status"] == "VALIDATION_ERROR"
        ]

        failures = [
            name
            for name, report in reports.items()
            if report["status"] == "FAIL"
        ]

        if errors:
            overall_status = "ERROR"
        elif failures:
            overall_status = "FAIL"
        else:
            overall_status = "PASS"

        return {
            "service": "ValidationService",
            "version": "v0.1",
            "status": "OBSERVED",
            "overall_status": overall_status,
            "inspection_time": datetime.now(timezone.utc).isoformat(),
            "validators_total": len(self.validators),
            "validation_errors": len(errors),
            "validation_failures": len(failures),
            "validators": reports,
            "boundary": "VALIDATION_DOES_NOT_IMPLY_TRUTH",
            "unknown_policy": "UNKNOWN -> HOLD",
        }