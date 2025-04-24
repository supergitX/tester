from reviewed_code import factorial
import pytest

def test_factorial_valid_input():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6

def test_factorial_invalid_input():
    assert factorial(-1) == "Factorial is not defined for negative numbers."
    assert factorial(-5) == "Factorial is not defined for negative numbers."

def test_factorial_edge_cases():
    assert factorial(0) == 1
    assert factorial(1) == 1
    with pytest.raises(TypeError):
        factorial(None)
    with pytest.raises(TypeError):
        factorial("")

def test_factorial_large_input():
    assert factorial(20) == 2432902008176640000

def test_factorial_invalid_input_type():
    with pytest.raises(TypeError):
        factorial("five")
    with pytest.raises(TypeError):
        factorial([5])
    with pytest.raises(TypeError):
        factorial({"n": 5})

def test_factorial_float_input():
    with pytest.raises(TypeError):
        factorial(5.5)

def test_factorial_negative_zero():
    assert factorial(-0) == "Factorial is not defined for negative numbers."