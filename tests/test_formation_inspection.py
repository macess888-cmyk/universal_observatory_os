from uos.services.formation_inspection import (
    FormationInspectionService,
)


def test_formation_inspection():

    formation = {
        "name": "Sample Formation",
        "identities": [
            "OBJ-000000001",
        ],
        "registry": [
            {
                "identity": "OBJ-000000001",
            }
        ],
        "relationships": [
            {
                "source": "OBJ-000000001",
                "target": "OBJ-000000002",
                "relationship": "CONNECTED_TO",
            }
        ],
        "evidence": [
            {
                "identity": "EVID-000000001",
                "target": "OBJ-000000001",
                "type": "document",
            }
        ],
        "timeline": [
            {
                "identity": "EVT-000000001",
                "timestamp": "2026-07-06T12:00:00Z",
                "event_type": "OBSERVED",
                "target": "OBJ-000000001",
            }
        ],
        "graph": {
            "nodes": [
                "OBJ-000000001",
                "OBJ-000000002",
            ],
            "edges": [
                (
                    "OBJ-000000001",
                    "OBJ-000000002",
                )
            ],
        },
    }

    service = FormationInspectionService()

    report = service.inspect(formation)

    assert report["status"] == "PASS"
    assert report["formation_name"] == "Sample Formation"