from uos.services.validators.timeline_validator import TimelineValidator


def test_timeline_validator():

    events = [
        {
            "identity": "EVT-000000001",
            "timestamp": "2026-07-06T12:00:00Z",
            "event_type": "OBSERVATION_CREATED",
            "target": "OBS-000000001",
        },
        {
            "identity": "EVT-000000002",
            "timestamp": "2026-07-06T12:05:00Z",
            "event_type": "EVIDENCE_ATTACHED",
            "target": "EVID-000000001",
        },
    ]

    validator = TimelineValidator(events)

    report = validator.validate()

    assert report["status"] == "PASS"
    assert report["events"] == 2
    assert report["missing_identity"] == 0
    assert report["missing_timestamp"] == 0
    assert report["missing_event_type"] == 0
    assert report["missing_target"] == 0