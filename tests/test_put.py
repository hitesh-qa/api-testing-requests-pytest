import pytest
from utils.api_client import APIClient

@pytest.fixture
def client(base_url):
    return APIClient(base_url)

def test_update_user(client):
    payload = {
        "name": "Hitesh Updated",
        "job": "Senior QA Engineer"
    }
    response = client.put("/users/2", payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Hitesh Updated"
    assert response.json()["job"] == "Senior QA Engineer"
    assert "updatedAt" in response.json()

def test_update_user_single_field(client):
    payload = {
        "name": "Hitesh"
    }
    response = client.put("/users/2", payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Hitesh"

# test_update_user -> updates name and job, checks response
# test_update_user_single_field -> updates only name,checks response