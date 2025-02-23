from reviewed_code import factorial

def test_factorial_negative():
    assert factorial(-1) == "Factorial is not defined for negative numbers."

def test_factorial_zero():
    assert factorial(0) == 1

def test_factorial_one():
    assert factorial(1) == 1

def test_factorial_positive():
    assert factorial(5) == 120

def test_factorial_larger_number():
    assert factorial(10) == 3628800

def test_factorial_large_number():
    assert factorial(20) == 2432902008176640000