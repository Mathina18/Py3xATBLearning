# 6. Trying to Update on a Delete ID -> 404

import pytest
import allure
import requests


@pytest.fixture()
@allure.title("Create a new Booking")
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
    # get the response Body and Verify the JSON, Booking ID is not None
    data = response.json()
    booking_id = data["bookingid"]
    print(f"Created Booking ID: {booking_id}")
    print(data)
    return booking_id


@allure.title("#TC6 - Trying to update a deleted booking ID")
@pytest.mark.integration
def test_delete_request(create_token, create_booking):
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking
    DELETE_URL = URL + str(booking_id)
    cookie_value = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)

    #Delete the booking
    delete_response = requests.delete(url=DELETE_URL, headers=headers)
    assert delete_response.status_code == 201
    print(f"Deleted booking id:{booking_id}")

    # Try to update the deleted booking
    UPDATE_URL = DELETE_URL

    update_payload = {
        "firstname": "anis",
        "lastname": "farveen",
    }
    update_response = requests.patch(url=UPDATE_URL, headers=headers, json=update_payload)
    assert update_response.status_code == 405
    assert "text/plain" in update_response.headers["Content-Type"]
    print(f"Update Response Status Code: {update_response.status_code}")
    print(f"Update Response Body: {update_response.text}")



