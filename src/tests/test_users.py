import pytest
from fastapi.testclient import TestClient
from src.main.server import server


@pytest.fixture
def client():
    return TestClient(server)


def test_create_user(client: TestClient):
    # given
    user_data = {"username": "testuser", "email": "testuser@example.com"}
    # when
    response = client.post("/users/", json=user_data)
    # then
    assert response.status_code == 201
    data = response.json()
    assert data["username"] == user_data["username"]
    assert data["email"] == user_data["email"]
