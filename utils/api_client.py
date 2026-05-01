import requests
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("API_KEY")

class APIClient:

    def __init__(self, base_url):
        self.base_url = base_url
        self.headers = {"x-api-key": API_KEY}

    def get(self, endpoint):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers)

    def post(self, endpoint, data):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=data, headers=self.headers)

    def put(self, endpoint, data):
        return requests.put(
            f"{self.base_url}{endpoint}",
            json=data, headers=self.headers)

    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}",
                               headers=self.headers)

#get -> fetches data from API
#post -> creates new data
#put -> updates existing data
#delete -> deletes data