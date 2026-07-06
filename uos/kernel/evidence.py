from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class ObservableEvidence:
    """
    ObservableEvidence represents recorded support for an observation,
    relationship, event, object, question, or claim.

    Evidence does not imply proof, authority, causation, or explanation.
    """

    evidence_id: str
    evidence_type: str
    title: str

    description: str = ""
    source: Optional[str] = None

    supports: List[str] = field(default_factory=list)
    contradicts: List[str] = field(default_factory=list)
    contextualizes: List[str] = field(default_factory=list)
    questions: List[str] = field(default_factory=list)

    confidence: str = "UNKNOWN"
    authority: str = "NONE"
    claims_proof: bool = False

    metadata: Dict[str, Any] = field(default_factory=dict)
    created_at: str = field(
        default_factory=lambda: datetime.now(timezone.utc).isoformat()
    )

    def inspect(self) -> Dict[str, Any]:
        return {
            "evidence_id": self.evidence_id,
            "evidence_type": self.evidence_type,
            "title": self.title,
            "supports_count": len(self.supports),
            "contradicts_count": len(self.contradicts),
            "contextualizes_count": len(self.contextualizes),
            "questions_count": len(self.questions),
            "confidence": self.confidence,
            "authority": self.authority,
            "claims_proof": self.claims_proof,
            "status": "OBSERVED",
            "boundary": "EVIDENCE_DOES_NOT_IMPLY_PROOF",
        }

    def to_dict(self) -> Dict[str, Any]:
        return {
            "evidence_id": self.evidence_id,
            "evidence_type": self.evidence_type,
            "title": self.title,
            "description": self.description,
            "source": self.source,
            "supports": self.supports,
            "contradicts": self.contradicts,
            "contextualizes": self.contextualizes,
            "questions": self.questions,
            "confidence": self.confidence,
            "authority": self.authority,
            "claims_proof": self.claims_proof,
            "metadata": self.metadata,
            "created_at": self.created_at,
        }