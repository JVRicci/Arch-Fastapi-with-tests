from fastapi.testclient import TestClient
import pytest
from pytest import mark
from src.main.server.server import app


@pytest.fixture
def client():
    return TestClient(app)


# @mark.skip(reason="Endpoint not implemented yet")
def test_create_user(client: TestClient):
    # given
    user_data = {
        "username": "testuser",
        "age": 25,
        "email": "testuser@example.com",
        "uf": "SP",
    }
    # when
    response = client.post("/users/", json=user_data)
    # then
    assert response.status_code == 201
