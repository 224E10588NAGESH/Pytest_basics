from reverse import reverse_string

def test_reverse_name():
    assert reverse_string("Nagesh") == "hsegaN"

def test_reverse_word():
    assert reverse_string("python") == "nohtyp"

def test_empty():
    assert reverse_string("") == ""

def test_single_char():
    assert reverse_string("A") == "A"

def test_numbers():
    assert reverse_string("123") == "321"
