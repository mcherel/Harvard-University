import pytest
from fuel import convert, gauge

def main():
    test_convert()
    test_gauge()


def test_convert():
    assert convert("3/4") == 75
    assert convert("1/3") == 33
    assert convert("2/3") == 67
    assert convert("0/100") == 0
    assert convert("1/100") == 1
    assert convert("100/100") == 100
    with pytest.raises(ValueError):
        convert("dog/cat")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_gauge():
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(98) == "98%"
    assert gauge(2) == "2%"


if __name__ == "__main__":
    main()
