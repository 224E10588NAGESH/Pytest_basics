from add import add

def test_add_positive():
    assert add(10, 20) == 30

def test_add_negative():
    assert add(5, -5) == 0

def test_add_zero():
    assert add(0, 10) == 10

def test_add_mixed():
    assert add(-5, 10) == 5

def test_add_float():
    assert add(2.5, 2.5) == 5.0
