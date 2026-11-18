from largest import largest

def test_largest_10_5():
    assert largest(10, 5) == 10

def test_largest_5_10():
    assert largest(5, 10) == 10

def test_same_numbers():
    assert largest(7, 7) == 7

def test_negative():
    assert largest(-2, -5) == -2

def test_zero():
    assert largest(0, -1) == 0
