from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_list_users():
    response = client.get("/api/v1/users")
    assert response.status_code == 200
    assert "users" in response.json()


def test_create_user():
    response = client.post(
        "/api/v1/users",
        json={"name": "Test User", "email": "test@nullzone.ai"},
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Test User"
