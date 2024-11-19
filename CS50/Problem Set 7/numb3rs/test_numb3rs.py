from numb3rs import validate


def test_validate():
    assert validate("255.255.255.255") == True
    assert validate("256.255.255.255") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("1.2.3.4") == True
    assert validate("249.249.249.249") == True
    assert validate("500.500.500.500") == False
    assert validate("199.911.288.882") == False
