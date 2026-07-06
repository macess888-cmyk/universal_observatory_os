from uos.services.validators.graph_validator import GraphValidator


def test_graph_validator():

    graph = {
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
    }

    validator = GraphValidator(graph)

    report = validator.validate()

    assert report["status"] == "PASS"
    assert report["nodes"] == 2
    assert report["edges"] == 1
    assert report["missing_nodes"] == 0
    assert report["missing_edges"] == 0