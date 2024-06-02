from CS50_P.CS50_5.square import square
import CS50_P.CS50_5.square as square 
import pytest
# pytest test_square.py

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")