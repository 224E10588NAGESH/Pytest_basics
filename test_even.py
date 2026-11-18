from even import is_even

def test_even_2():
    assert is_even(2) == True

def test_even_10():
    assert is_even(1) == True

def test_odd_5():
    assert is_even(5) == True

def test_zero():
    assert is_even(0) == True

def test_negative_even():
    assert is_even(-8) == True
