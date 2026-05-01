import pytest
BASE_URL = "https://reqres.in/api"

@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

#BASE_URL -> stores the API website address
#base_url fixture -> gives this URL to every test that needs it
#Much simpler than Project 1 - no browser needed!