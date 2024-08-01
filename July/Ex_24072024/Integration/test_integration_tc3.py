# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.

import pytest
import allure
import requests


@pytest.fixture()
@allure.title("Get all booking IDs")
def get_all_booking_id():
    URL = "https://restful-booker.herokuapp.com/booking"
    response = requests.get(url=URL)
    assert response.status_code == 200
    data = response.json()
    booking_id = data[0]['bookingid']
    print(f"Booking ID: {booking_id}")
    return booking_id


@allure.title("#TC3 - Update a booking and verify using GET by ID")
@pytest.mark.integration
def test_get_update_and_put_request(create_token, get_all_booking_id):
    booking_id = get_all_booking_id
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/" + str(booking_id)
    UPDATE_URL = base_url + base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "Mathina",
        "lastname": "Jaman",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Dinner"
    }
    update_response = requests.put(url=UPDATE_URL, headers=headers, json=json_payload)
    assert update_response.status_code == 200
    assert "application/json" in update_response.headers["Content-Type"]
    update_data = update_response.json()
    print(f"updated booking data:{update_data}")

    # Verify the update using GET request by ID
    get_response = requests.get(url=UPDATE_URL)
    assert get_response.status_code == 200
    assert "application/json" in get_response.headers["Content-Type"]
    updated_data = get_response.json()
    print(f"Verified data:{updated_data}")
    assert updated_data["firstname"] == "Mathina"
    assert updated_data["lastname"] == "Jaman"
    assert updated_data["totalprice"] == 111
    assert updated_data["depositpaid"] == True
    assert updated_data["bookingdates"]["checkin"] == "2018-01-01"
    assert updated_data["bookingdates"]["checkout"] == "2019-01-01"
    assert updated_data["additionalneeds"] == "Dinner"


