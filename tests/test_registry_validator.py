from uos.services.validators.registry_validator import RegistryValidator


def test_registry_validator():

    registry = [
        {"identity": "OBJ-000000001"},
        {"identity": "OBJ-000000002"},
        {"identity": "REL-000000001"},
    ]

    validator = RegistryValidator(registry)

    report = validator.validate()

    assert report["status"] == "PASS"
    assert report["objects"] == 3
    assert report["duplicates"] == []
    assert report["missing_identity"] == 0