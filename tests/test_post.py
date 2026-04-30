import pytest
from utils.api_client import APIClient

@pytest.fixture
def client(base_url):
    return APIClient(base_url)

def test_create_user(client):
    payload = {
        "name": "Hitesh",
        "job": "QA Engineer"
    }
    response = client.post("/users", payload)
    assert response.status_code == 201
    assert response.json()["name"] == "Hitesh"
    assert response.json()["job"] == "QA Engineer"
    assert "id" in response.json()
    assert "createdAt" in response.json()

def test_create_user_missing_field(client):
    payload = {}
    response = client.post("/users", payload)
    assert response.status_code == 201

# test_create_user -> creates a new user, checks name, job, id and createdAt are in response
# test_vreate_user_missing_fields-> senfs empty data, checks API still responds with 201