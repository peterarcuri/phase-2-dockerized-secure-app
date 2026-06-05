
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "app"))


from app.main import app


def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json == {"status": "healthy"}


def test_home_endpoint():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert response.json["project"] == "phase-2-dockerized-secure-app"





