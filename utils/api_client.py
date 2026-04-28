import requests

class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, endpoint):
        return requests.get(f"{self.base_url}{endpoint}")
    def post(self, endpoint, data):
        return requests.post(f"{self.base_url}{endpoint}", json=data)
    def put(self, endpoint, data):
        return requests.put(f"{self.base_url}{endpoint}", json=data)
    def delete(self, endpoint):
        return requests.delete(f"{self.base_url}{endpoint}")

#get -> fetches data from API
#post -> creates new data
#put -> updates existing data
#delete -> deletes data