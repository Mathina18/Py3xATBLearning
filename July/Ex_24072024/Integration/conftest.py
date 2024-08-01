import allure
import pytest
import requests


@pytest.fixture()
@allure.title("Create an authentication token")
def create_token():
    URL = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    data = response.json()
    token = data["token"]
    print(f"Generated Token: {token}")
    return token
