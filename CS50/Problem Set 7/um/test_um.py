from um import count
import pytest

def main():
    test_um()

def test_um():
    assert count("UM!") == 1
    assert count("UM! Hello, um.") == 2
    assert count("Hello, UM!") == 1
    assert count("Bye, um!") == 1
    assert count("UMie!") == 0
    assert count("AM!") == 0
