"""
Testing register_reminder endpoint
"""

from fastapi.testclient import TestClient
from app.main import app
import pytest  # type: ignore

client = TestClient(app)


@pytest.fixture
def test_client():
    return TestClient(app)


def test_read_root(test_client):  # pylint: disable=redefined-outer-name
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}


def test_store_prompts(test_client):  # pylint: disable=redefined-outer-name
    data = [
        {"role": "user", "content": "I like to walk."},
        {"role": "user", "content": "I run nearly every day."},
    ]
    response = test_client.post("/store-prompts", json=data)
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_register_reminder(test_client):  # pylint: disable=redefined-outer-name
    reminder_data = {
        "type": "daily",
        "time_at_request_utc": "2024-09-28T12:00:00Z",
        "time_after_minutes": 30,
        "time_after_hours": 1,
        "cycle": "weekly",
        "todo_message": "Water the plants",
    }
    response = test_client.post("/register-reminder", json=reminder_data)
    # assert isinstance(response) is not type(None)
    assert response.status_code == 200
    assert "type" in response.json()
