from uos.services.validators.evidence_validator import (
    EvidenceValidator,
)


def test_evidence_validator():

    evidence = [
        {
            "identity": "EVID-000000001",
            "target": "OBJ-000000001",
            "type": "photograph",
        },
        {
            "identity": "EVID-000000002",
            "target": "REL-000000001",
            "type": "document",
        },
    ]

    validator = EvidenceValidator(evidence)

    report = validator.validate()

    assert report["status"] == "PASS"
    assert report["evidence_records"] == 2
    assert report["missing_identity"] == 0
    assert report["missing_target"] == 0
    assert report["missing_type"] == 0