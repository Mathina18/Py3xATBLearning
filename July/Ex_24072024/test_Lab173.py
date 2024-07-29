import pytest
import allure
import requests

@allure.title("Test GET Request- Restful BOOKER Project#1")
@allure.description("TC#1 -> Verify that GET request with ID Works")
@allure.tag("Regression", "p0")
@allure.label("Owner","Mathina")
@allure.testcase("TC#4")
def test_single_request_by_id():
    url = "https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    print(responseData.json())
    assert responseData.status_code == 200
