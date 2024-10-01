from plates import is_valid as valid
import sys

def main():
    if not (test_len() and test_zero() and test_first_two() and test_isalphanum()):
        sys.exit(1)
    sys.exit(0)

def test_len():
    assert valid("A") == False
    assert valid("OUTATIME") == False
    assert valid("AD22") == True # 2-6 == True
    assert valid("AD22222") == False
    assert valid("") == False


def test_isalphanum():
    assert valid("cs.,50") == False
    assert valid("_____") == False
    assert valid("R.I.P.") == False
    assert valid("HeLlLo") == True
    assert valid("Hel10") == True
    assert valid("") == False
    assert valid("     ") == False



def test_zero():
    assert valid("Z0000") == False
    assert valid("ZORR0") == False
    assert valid("HELP10") == True
    assert valid("00000") == False

def test_first_two():
    assert valid("22H00") == False
    assert valid("2H00") == False
    assert valid("H1000") == False
    assert valid("HH100") == True
    assert valid("100") == False
    assert valid("23") == False
    assert valid("cs") == True

def test_number_placement():
    assert valid("HELLO1") == True
    assert valid("H3LLO1") == False
    assert valid("H3LL01") == False
    assert valid("3LL01") == False
    assert valid("HH") == True
    assert valid("50") == False
    assert valid("CS50") == True
    assert valid("CS05") == False
    assert valid("CS50p") == False


if __name__ == "__main__":
    main()
