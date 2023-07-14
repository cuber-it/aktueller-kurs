import requests
import json

# The base URL of our API
BASE_URL = 'http://localhost:5000/resource'

def create_resource(data):
    response = requests.post(BASE_URL, json=data)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")

def get_resource(id):
    response = requests.get(f"{BASE_URL}/{id}")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")

def update_resource(id, data):
    response = requests.put(f"{BASE_URL}/{id}", json=data)
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")

def delete_resource(id):
    response = requests.delete(f"{BASE_URL}/{id}")
    print(f"Status code: {response.status_code}")
    print(f"Response: {response.json()}")

if __name__ == "__main__":
    # Create a new resource
    create_resource({"name": "John Doe"})
    # Get the resource we just created
    get_resource(1)
    # Update the resource
    update_resource(1, {"name": "Jane Doe"})
    # Delete the resource
    delete_resource(1)
