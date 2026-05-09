from interpreter import interpreter
import pytest

def test_one_plus_one():
    assert interpreter("1 + 1") == 2.0  

def test_two_minus_three():
    assert interpreter("2 - 3") == -1.0 

def test_two_times_two():
    assert interpreter("2 * 2") == 4.0

def test_fifty_divided_by_five():
    assert interpreter("50 / 5") == 10.0

def test_cannot_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        interpreter("1 / 0")

def test_expression_without_spaces():
    assert interpreter("1+2") == 3.0

def test_space_insensitive():
    assert interpreter("  1+ 2") == 3.0

def test_cannot_operate_caracteres():
    with pytest.raises(ValueError):
        interpreter("a - b")
    
    with pytest.raises(ValueError):
        interpreter("a + b")
    
    with pytest.raises(ValueError):
        interpreter("1 / b")
    
    with pytest.raises(ValueError):
        interpreter("a * 1")