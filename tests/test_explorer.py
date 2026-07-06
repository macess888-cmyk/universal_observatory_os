from uos.services.explorer import ExplorerService


def test_explorer():

    report = {
        "formation_name": "Demo Formation",
        "status": "PASS",
        "structural_report": {
            "validator_count": 6,
        },
    }

    explorer = ExplorerService()

    view = explorer.explore(report)

    assert view["view"] == "Explorer"
    assert view["status"] == "PASS"
    assert view["validators"] == 6
    assert "Identity" in view["available_sections"]