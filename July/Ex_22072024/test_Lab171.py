import pytest
import allure
@allure.title("TC#1 - to verify 1-1 is equal to 0")
@allure.description("This is a smoke test to check 1-1 is equal to 0")
@pytest.mark.smoke
def test_sub1():
    assert 1-1 == 0


@allure.title("TC#2 - to verify 2-1 is equal to 1")
@allure.description("This is a regression test to check 2-1 is equal to 1")
@pytest.mark.regression
def test_sub2():
    assert 2 - 1 == 1


@allure.title("TC#3 - to verify 4-1 is equal to 3")
@allure.description("This is a smoke test to check 4-1 is equal to 3")
@pytest.mark.smoke
def test_sub3():
    assert 4 - 1 == 3


@allure.title("TC#4 - to verify 1-1 is not equal to 0")
@allure.description("This is a sanity test to check 1-1 is not equal to 0")
@pytest.mark.sanity
def test_sub4():
    assert 1 - 1 != 0

@pytest.mark.skip(reason="not selected, just skip")
def test_sub4():
    assert 1 - 1 != 0
