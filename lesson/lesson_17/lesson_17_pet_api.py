import requests

BASE_URL = "https://petstore.swagger.io/v2"
ENDPOINT = "/pet"
HEADERS = {"accept": "*/*",}

def create_pet():
    data = {
        "id": 12345,
        "name": "Tishka",
        "status": "available"
    }

    response = requests.post(
        url=f"{BASE_URL}{ENDPOINT}",
        headers=HEADERS,
        json=data
    )

    return response

def list_pet(pet_id):
    response = requests.get(
        url=f"{BASE_URL}{ENDPOINT}/{pet_id}",
        headers = HEADERS
    )

    return response

def rename_pet():
    data = {
        "id": 12345,
        "name": "Mishka",
        "status": "available"
    }

    response = requests.put(
        url=f"{BASE_URL}{ENDPOINT}",
        headers=HEADERS,
        json=data
    )

    return response

def delete_pet(pet_id):

    response = requests.delete(
        url=f"{BASE_URL}{ENDPOINT}/{pet_id}",
        headers=HEADERS
    )

    return response


