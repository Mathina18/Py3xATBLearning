import pytest
import allure
import requests


@allure.title("Create Booking CRUD- Create booking")
@allure.description("TC#1 - Verify the Create Booking")
@pytest.mark.crud
def test_create_booking_positive():
    # To make Request
    # URL
    # Method - POST
    # Headers - Content-type=Application/json
    # Payload / Data / Body - Dict / JSON
    # Auth(No)
    base_URL = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_URL + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=payload)
    assert response.status_code == 200
    responseData = response.json()
    # Response Body  Verification,
    # Headers
    # Status Code
    bookingid = responseData["bookingid"]
    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    firstname = responseData["booking"]["firstname"]
    lastname = responseData["booking"]["lastname"]
    totalprice = responseData["booking"]["totalprice"]
    depositpaid = responseData["booking"]["depositpaid"]
    assert firstname == "Jim"
    assert lastname == "Brown"
    assert totalprice == 111
    assert depositpaid == True

    checkin = responseData["booking"]["bookingdates"]["checkin"]
    checkout = responseData["booking"]["bookingdates"]["checkout"]
    assert checkin == "2018-01-01"
    assert checkout == "2019-01-01"

    # JSON Schema Validation
    # Time Response

@allure.title("Create Booking CRUD-Negative-Verify booking is not created with {} data")
@allure.description("TC#2 - Verify booking is not created with {} data")
@pytest.mark.crud
def test_create_booking_negative_tc1():
        base_URL = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        URL = base_URL + base_path
        headers = {"Content-Type": "application/json"}
        payload = {}
        response = requests.post(url=URL, headers=headers, json=payload)
        print(type(URL))
        print(type(headers))
        print(type(payload))
        assert response.status_code == 500

@allure.title("Create Booking CRUD-Verify booking with totalprice as string")
@allure.description("TC#3 - Verify booking with totalprice as string")
@pytest.mark.crud
def test_create_booking_negative_tc2():
        base_URL = "https://restful-booker.herokuapp.com"
        base_path = "/booking"
        URL = base_URL + base_path
        headers = {"Content-Type": "application/json"}
        payload = {
            "firstname": "Jim",
            "lastname": "Brown",
            "totalprice": -7,
            "depositpaid": True,
            "bookingdates": {
                "checkin": "2018-01-01",
                "checkout": "2019-01-01"
            },
            "additionalneeds": "Breakfast"
        }
        response = requests.post(url=URL, headers=headers, json=payload)
        # Assertions
        assert response.status_code == 200
