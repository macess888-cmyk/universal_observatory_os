from uos.services.validators.identity_validator import IdentityValidator


def test_identity_validator():

    identities = [
        "OBJ-000000001",
        "REL-000000001",
        "EVT-000000001",
        "EVD-000000001",
    ]

    validator = IdentityValidator(identities)

    report = validator.validate()

    assert report["status"] == "PASS"
    assert report["duplicates"] == []
    assert report["missing"] == 0
    assert report["invalid_format"] == []