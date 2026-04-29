import pytest
from utils.api_client import APIClient

@pytest.fixture
def client(base_url):
    return APIClient(base_url)

def test_get_all_users(client):
    response = client.get("/users?page=2")
    assert response.status_code == 200
    assert "data" in response.json()

def test_get_single_user(client):
    response = client.get("/users/2")
    assert response.status_code == 200
    assert response.json()["data"]["id"] ==2

def test_get_single_user_not_found(client):
    response = client.get("/users/999")
    assert response.status_code == 404

#test_get_all_users -> gets list of users, checks status 200
#test_get_single_user -> gets user with id 2, checks id is correct
#test_get_single_user_not_found -> gets user that doesn't exist, expects 404