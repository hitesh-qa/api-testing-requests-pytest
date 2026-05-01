import pytest
from utils.api_client import APIClient

@pytest.fixture
def client(base_url):
    return APIClient(base_url)

def test_delete_user(client):
    response = client.delete("/users/2")
    assert response.status_code == 204

def test_delete_non_existing_user(client):
    response = client.delete("/users/999")
    assert response.status_code == 204

# test_delete_user -> deletes user with id 2, expect 204(no content)
#test_delete_non_existing_user -> deletes user that doesn't exist, reqres.in still return 204