from uos.services.health import HealthService


def test_health_service_exists():

    health = HealthService()

    report = health.inspect()

    assert report["service"] == "HealthService"
    assert report["version"] == "v0.1"
    assert report["status"] == "OBSERVED"

    assert report["components_total"] == 5
    assert report["components_attached"] == 0
    assert report["inspection_errors"] == 0

    print(report)