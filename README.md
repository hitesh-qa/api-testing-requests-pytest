# API  Testing - Requests + Pytest

Automated REST API test suite for reqres.in using Python Requests library + Pytest.

## What This Project Covers
- GET request tests (fetch users, single user, not found)
- POST request tests (create user, missing fields)
- PUT request tests (update user, single field update)
- DELETE request tests (delete user, non existing user)
- Reusable API client utility class
- Environment variable for API key security

## Tech Stack
- Python
- Requests library
- Pytest

## Project Structure
- tests/ -> Test cases (GET, POST, PUT, DELETE)
- utils/ -> Reusable APIClient class
- conftest.py -> Base URL fixture
- .env -> API key (not uploaded to GitHub)

## How to Run 
1. pip install -r requirements.txt
2. Create .env file with your API key:
    API_KEY=your_reqres_api_key
3. pytest tests/ -v

## Test Results
9 tests passing
- 3 GET tests
- 2 POST tests
- 2 PUT tests
- 2 DELETE tests