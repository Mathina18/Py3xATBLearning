import pytest

@pytest.mark.smoke
def test_sub1():
    assert 1-1 == 0

@pytest.mark.regression
def test_sub2():
    assert 2 - 1 == 1

@pytest.mark.smoke
def test_sub3():
    assert 4 - 1 == 3

@pytest.mark.sanity
def test_sub4():
    assert 1 - 1 != 0

@pytest.mark.skip(reason="not selected, just skip")
def test_sub4():
    assert 1 - 1 != 0
