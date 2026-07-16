from addition import add, subtract, multiply, divide

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5        #True

def test_add_zero():
    assert add(0, 5) == 5

def teat_add_positive_and_negative():
    assert add(5, -3) == 2

def test_add_floats():
    assert add(2.5, 3.1) == 5.6

def test_subtract():
    assert subtract(5, 3) == 2  # This test is intentionally incorrect to demonstrate a failing test case

def test_subract_negative_numbers():
    assert subtract(-5, -3) == -2  # This test is intentionally incorrect to demonstrate a failing test case

def test_multiply():
    assert multiply(4, 5) == 20  # This test is intentionally incorrect to demonstrate a failing test case

def test_multiply_zero():
    assert multiply(0, 5) == 0  # This test is intentionally incorrect to demonstrate a failing test case

def test_divide():
    assert divide(6, 3) == 2

def test_divide_zero():
    try:
        divide(5,0)
    except ZeroDivisionError:
        pass
    else:
        assert False, "Expected ZeroDivision"
