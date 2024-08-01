# 5. Invalid Creation - enter a wrong payload or Wrong JSON.

import pytest
import allure
import requests


@allure.title("Invalid creation- Wrong paylod or JSON ")
def test_wrong_payload():
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": None,
        "lastname": 876,
        "totalprice": "juy",
        "depositpaid": "True",
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response = requests.put(url=URL, headers=headers, json=json_payload)
    assert response.status_code != 200
    print(f"\nResponse Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
