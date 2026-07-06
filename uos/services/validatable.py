"""
Universal Observatory Operating System
Validatable Protocol v0.1

Purpose:
Define the common validation contract for Observatory components.

Boundary:
Validation evaluates structural consistency.

Validation does not establish:
- truth
- authority
- correctness
- proof
- causation

UNKNOWN -> HOLD
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class Validatable(ABC):
    """
    Common validation contract.

    Any component implementing this interface should be able
    to evaluate its own structural consistency and return
    a structured validation report.
    """

    @abstractmethod
    def validate(self) -> Dict[str, Any]:
        """
        Return a structured validation report.

        Validation should report structural consistency only.

        It must not make authoritative or interpretive claims.
        """
        raise NotImplementedError