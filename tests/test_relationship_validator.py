from uos.services.validators.relationship_validator import (
    RelationshipValidator,
)


def test_relationship_validator():

    relationships = [
        {
            "source": "OBJ-000000001",
            "target": "OBJ-000000002",
            "relationship": "CONNECTED_TO",
        },
        {
            "source": "OBJ-000000002",
            "target": "OBJ-000000003",
            "relationship": "DEPENDS_ON",
        },
    ]

    validator = RelationshipValidator(relationships)

    report = validator.validate()

    assert report["status"] == "PASS"
    assert report["relationships"] == 2
    assert report["missing_source"] == 0
    assert report["missing_target"] == 0
    assert report["missing_relationship"] == 0