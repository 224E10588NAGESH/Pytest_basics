(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_even.py -v
============================= test session starts ==============================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                              

test_even.py::test_even_2 PASSED                                         [ 20%]
test_even.py::test_even_10 PASSED                                        [ 40%]
test_even.py::test_odd_5 PASSED                                          [ 60%]
test_even.py::test_zero PASSED                                           [ 80%]
test_even.py::test_negative_even PASSED                                  [100%]

============================== 5 passed in 0.01s ===============================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_even.py -v
============================= test session starts ==============================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                              

test_even.py::test_even_2 PASSED                                         [ 20%]
test_even.py::test_even_10 FAILED                                        [ 40%]
test_even.py::test_odd_5 FAILED                                          [ 60%]
test_even.py::test_zero PASSED                                           [ 80%]
test_even.py::test_negative_even PASSED                                  [100%]

=================================== FAILURES ===================================
_________________________________ test_even_10 _________________________________

    def test_even_10():
>       assert is_even(1) == True
E       assert False == True
E        +  where False = is_even(1)

test_even.py:7: AssertionError
__________________________________ test_odd_5 __________________________________

    def test_odd_5():
>       assert is_even(5) == True
E       assert False == True
E        +  where False = is_even(5)

test_even.py:10: AssertionError
=========================== short test summary info ============================
FAILED test_even.py::test_even_10 - assert False == True
FAILED test_even.py::test_odd_5 - assert False == True
========================= 2 failed, 3 passed in 0.04s ==========================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_reverse.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_reverse.py::test_reverse_name PASSED                                                                                                                                                               [ 20%]
test_reverse.py::test_reverse_word PASSED                                                                                                                                                               [ 40%]
test_reverse.py::test_empty PASSED                                                                                                                                                                      [ 60%]
test_reverse.py::test_single_char PASSED                                                                                                                                                                [ 80%]
test_reverse.py::test_numbers PASSED                                                                                                                                                                    [100%]

============================================================================================== 5 passed in 0.01s ==============================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_largest.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_largest.py::test_largest_10_5 PASSED                                                                                                                                                               [ 20%]
test_largest.py::test_largest_5_10 PASSED                                                                                                                                                               [ 40%]
test_largest.py::test_same_numbers PASSED                                                                                                                                                               [ 60%]
test_largest.py::test_negative PASSED                                                                                                                                                                   [ 80%]
test_largest.py::test_zero PASSED                                                                                                                                                                       [100%]

============================================================================================== 5 passed in 0.01s ==============================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_login.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_login.py::test_valid_login FAILED                                                                                                                                                                  [ 20%]
test_login.py::test_invalid_password PASSED                                                                                                                                                             [ 40%]
test_login.py::test_invalid_username PASSED                                                                                                                                                             [ 60%]
test_login.py::test_blank_username PASSED                                                                                                                                                               [ 80%]
test_login.py::test_blank_password PASSED                                                                                                                                                               [100%]

================================================================================================== FAILURES ===================================================================================================
______________________________________________________________________________________________ test_valid_login _______________________________________________________________________________________________

    def test_valid_login():
>       assert validate_login("admin", "admin123") == "Login Successful"
E       AssertionError: assert 'Login Failed' == 'Login Successful'
E         
E         - Login Successful
E         + Login Failed

test_login.py:4: AssertionError
=========================================================================================== short test summary info ===========================================================================================
FAILED test_login.py::test_valid_login - AssertionError: assert 'Login Failed' == 'Login Successful'
========================================================================================= 1 failed, 4 passed in 0.04s =========================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_login.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_login.py::test_valid_login PASSED                                                                                                                                                                  [ 20%]
test_login.py::test_invalid_password PASSED                                                                                                                                                             [ 40%]
test_login.py::test_invalid_username PASSED                                                                                                                                                             [ 60%]
test_login.py::test_blank_username PASSED                                                                                                                                                               [ 80%]
test_login.py::test_blank_password PASSED                                                                                                                                                               [100%]

============================================================================================== 5 passed in 0.02s ==============================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_login.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_login.py::test_valid_login PASSED                                                                                                                                                                  [ 20%]
test_login.py::test_invalid_password FAILED                                                                                                                                                             [ 40%]
test_login.py::test_invalid_username PASSED                                                                                                                                                             [ 60%]
test_login.py::test_blank_username PASSED                                                                                                                                                               [ 80%]
test_login.py::test_blank_password PASSED                                                                                                                                                               [100%]

================================================================================================== FAILURES ===================================================================================================
____________________________________________________________________________________________ test_invalid_password ____________________________________________________________________________________________

    def test_invalid_password():
>       assert validate_login("ITTEAM", "Sang@1974") == "Login Successful"

test_login.py:7: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

username = 'ITTEAM', password = 'Sang@1974'

    def validate_login(username, password):
        if username == "Nagesh" and password == "Nagesh@588":
            return "Login Successful"
    
>       elif username == "ITTEAM" and Password == "Sang@1974":
E       NameError: name 'Password' is not defined

login.py:5: NameError
=========================================================================================== short test summary info ===========================================================================================
FAILED test_login.py::test_invalid_password - NameError: name 'Password' is not defined
========================================================================================= 1 failed, 4 passed in 0.04s =========================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_login.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_login.py::test_valid_login PASSED                                                                                                                                                                  [ 20%]
test_login.py::test_invalid_password FAILED                                                                                                                                                             [ 40%]
test_login.py::test_invalid_username PASSED                                                                                                                                                             [ 60%]
test_login.py::test_blank_username PASSED                                                                                                                                                               [ 80%]
test_login.py::test_blank_password PASSED                                                                                                                                                               [100%]

================================================================================================== FAILURES ===================================================================================================
____________________________________________________________________________________________ test_invalid_password ____________________________________________________________________________________________

    def test_invalid_password():
>       assert validate_login("ITTEAM", "Sang@1974") == "Login Successful"
E       AssertionError: assert 'Login successful' == 'Login Successful'
E         
E         - Login Successful
E         ?       ^
E         + Login successful
E         ?       ^

test_login.py:7: AssertionError
=========================================================================================== short test summary info ===========================================================================================
FAILED test_login.py::test_invalid_password - AssertionError: assert 'Login successful' == 'Login Successful'
========================================================================================= 1 failed, 4 passed in 0.03s =========================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_login.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_login.py::test_valid_login PASSED                                                                                                                                                                  [ 20%]
test_login.py::test_invalid_password PASSED                                                                                                                                                             [ 40%]
test_login.py::test_invalid_username PASSED                                                                                                                                                             [ 60%]
test_login.py::test_blank_username PASSED                                                                                                                                                               [ 80%]
test_login.py::test_blank_password PASSED                                                                                                                                                               [100%]

============================================================================================== 5 passed in 0.01s ==============================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_login.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_login.py::test_valid_login PASSED                                                                                                                                                                  [ 20%]
test_login.py::test_IT_password PASSED                                                                                                                                                                  [ 40%]
test_login.py::test_HCS_username FAILED                                                                                                                                                                 [ 60%]
test_login.py::test_blank_username PASSED                                                                                                                                                               [ 80%]
test_login.py::test_blank_password PASSED                                                                                                                                                               [100%]

================================================================================================== FAILURES ===================================================================================================
______________________________________________________________________________________________ test_HCS_username ______________________________________________________________________________________________

    def test_HCS_username():
>       assert validate_login("HCS", "Sang@1974") == "Login Failed"
E       AssertionError: assert 'Login Successful' == 'Login Failed'
E         
E         - Login Failed
E         + Login Successful

test_login.py:10: AssertionError
=========================================================================================== short test summary info ===========================================================================================
FAILED test_login.py::test_HCS_username - AssertionError: assert 'Login Successful' == 'Login Failed'
========================================================================================= 1 failed, 4 passed in 0.03s =========================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % pytest test_login.py -v
============================================================================================= test session starts =============================================================================================
platform darwin -- Python 3.13.5, pytest-8.3.4, pluggy-1.5.0 -- /opt/anaconda3/bin/python
cachedir: .pytest_cache
rootdir: /Users/knagesh/Desktop/Pytest files
plugins: anyio-4.7.0
collected 5 items                                                                                                                                                                                             

test_login.py::test_valid_login PASSED                                                                                                                                                                  [ 20%]
test_login.py::test_IT_password PASSED                                                                                                                                                                  [ 40%]
test_login.py::test_HCS_username PASSED                                                                                                                                                                 [ 60%]
test_login.py::test_blank_username PASSED                                                                                                                                                               [ 80%]
test_login.py::test_blank_password PASSED                                                                                                                                                               [100%]

============================================================================================== 5 passed in 0.01s ==============================================================================================
(base) knagesh@Ks-MacBook-Air Pytest files % 
