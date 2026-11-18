from login import validate_login

def test_valid_login():
    assert validate_login("Nagesh", "Nagesh@588") == "Login Successful"

def test_IT_password():
    assert validate_login("ITTEAM", "Sang@1974") == "Login Successful"

def test_HCS_username():
    assert validate_login("HCS", "Sang@1974") == "Login Successful"

def test_blank_username():
    assert validate_login("", "admin123") == "Login Failed"

def test_blank_password():
    assert validate_login("admin", "") == "Login Failed"
