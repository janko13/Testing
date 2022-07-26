from main import *
import pytest

# test
def test_total_empty() -> None:
    # total of empty should be 0.0
    assert total([]) == 0.0

def test_total_one() -> None:
    assert total([110.0]) == 110.0

def test_total_many() -> None:
    assert total([110.0, 1, 33.4]) == 144.4

def test_join_empty() -> None:
    assert join([], "/") == ""

def test_join_one() -> None:
    assert join([5], "/") == "5"

def test_join_many() -> None:
    assert join([5,6,7], "/") == "5/6/7"

def test_join_empty_delimmeter() -> None:
    assert join([5,6,7], "") == "567"

