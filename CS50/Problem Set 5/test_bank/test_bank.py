import pytest
# pytest test_bank.py
from bank import value

def test_zero_match():
    assert value("") == 100
    assert value("What's up?") == 100

def test_hello():
    assert value("HELLO") == 0
    assert value("hello") == 0

def test_partial_match():
    assert value("How are you ?") == 20
    assert value("Hi") == 20