from typing import Dict, List, Optional

from .evidence import ObservableEvidence


class EvidenceRegistry:
    """
    Registry for ObservableEvidence objects.

    Responsibilities:

    - Store evidence
    - Retrieve evidence
    - Search evidence
    - Preserve evidence

    The registry does NOT determine truth, proof, authority,
    correctness, or interpretation.
    """

    def __init__(self):
        self._evidence: Dict[str, ObservableEvidence] = {}

    # ---------------------------------------------------------
    # Basic Operations
    # ---------------------------------------------------------

    def add(self, evidence: ObservableEvidence) -> ObservableEvidence:
        self._evidence[evidence.evidence_id] = evidence
        return evidence

    def get(self, evidence_id: str) -> Optional[ObservableEvidence]:
        return self._evidence.get(evidence_id)

    def exists(self, evidence_id: str) -> bool:
        return evidence_id in self._evidence

    def remove(self, evidence_id: str) -> bool:
        if evidence_id in self._evidence:
            del self._evidence[evidence_id]
            return True
        return False

    # ---------------------------------------------------------
    # Collection
    # ---------------------------------------------------------

    def all(self) -> List[ObservableEvidence]:
        return list(self._evidence.values())

    def count(self) -> int:
        return len(self._evidence)

    # ---------------------------------------------------------
    # Relationship Queries
    # ---------------------------------------------------------

    def find_supporting(self, target_id: str) -> List[ObservableEvidence]:
        return [
            evidence
            for evidence in self._evidence.values()
            if target_id in evidence.supports
        ]

    def find_contradicting(self, target_id: str) -> List[ObservableEvidence]:
        return [
            evidence
            for evidence in self._evidence.values()
            if target_id in evidence.contradicts
        ]

    def find_context(self, target_id: str) -> List[ObservableEvidence]:
        return [
            evidence
            for evidence in self._evidence.values()
            if target_id in evidence.contextualizes
        ]

    def find_questions(self, target_id: str) -> List[ObservableEvidence]:
        return [
            evidence
            for evidence in self._evidence.values()
            if target_id in evidence.questions
        ]

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def by_type(self, evidence_type: str) -> List[ObservableEvidence]:
        return [
            evidence
            for evidence in self._evidence.values()
            if evidence.evidence_type == evidence_type
        ]

    # ---------------------------------------------------------
    # Inspection
    # ---------------------------------------------------------

    def inspect(self) -> dict:
        type_counts = {}

        for evidence in self._evidence.values():
            evidence_type = evidence.evidence_type
            type_counts[evidence_type] = (
                type_counts.get(evidence_type, 0) + 1
            )

        return {
            "registry": "EvidenceRegistry",
            "status": "ACTIVE",
            "total_evidence": self.count(),
            "evidence_types": type_counts,
        }