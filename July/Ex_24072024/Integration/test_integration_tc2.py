#Create a Booking, Delete the Booking with ID and
# Verify using GET request that it should not exist.
import allure
import pytest
import requests


def create_token():
    # token
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print("Token is:", token)
    return token

def create_booking():
    # Booking ID
    print("Create Booking Testcase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Samama",
        "lastname": "Jaman",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)
    print(type(URL))
    print(type(headers))
    print(type(json_payload))

    # Assertions
    assert response.status_code == 200
    # get the reponse Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    print(f"Created Booking ID: {booking_id}")
    print(data)
    return booking_id


@allure.title("#TC2 - Delete the booking and Verify that it should not exist")
@pytest.mark.integration
def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201
    print(f"Deleted Booking ID: {booking_id}")
    # GET request to verify that the booking id does not exist
    response = requests.get(url=DELETE_URL,headers=headers)
    assert response.status_code == 404
    print(f"Verified Booking ID {booking_id} does not exist")

