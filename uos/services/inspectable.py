"""
Universal Observatory Operating System
Inspectable Protocol v0.1

Purpose:
Define the common inspection contract for Observatory components.

Boundary:
Inspection reports observable state.

Inspection does not establish:
- truth
- authority
- correctness
- proof

UNKNOWN -> HOLD
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Dict


class Inspectable(ABC):
    """
    Common inspection contract.

    Any component implementing this interface should be able
    to describe its current observable state without making
    interpretive or authoritative claims.
    """

    @abstractmethod
    def inspect(self) -> Dict[str, Any]:
        """
        Return a structured inspection report.

        Inspection should describe observable state only.
        """
        raise NotImplementedError