"""
test_orangehrmheadless.py contains all the test cases
"""

from headless_orangehrm import HeadlessTesting
from headless_orangehrm import HRMData

# create object from HeadlessTesting Class
myChrome = HeadlessTesting(HRMData.url)

def test_start():
    assert myChrome.start() == True
    print("SUCCESS: Automation Started!")

def test_validate_username_input_box():
    assert myChrome.validate_username_input_box() == True
    print("SUCCESS : Username Input Box is visible!")

def test_validate_password_input_box():
    assert myChrome.validate_password_input_box() == True
    print("SUCCESS : Password Input Box is visible!")

def test_validate_login_button():
    assert myChrome.validate_login_button() == True
    print("SUCCESS : Login Button is visible!")

def test_validate_login():
    assert myChrome.validate_login() == HRMData.dashboard_url
    print("SUCCESS : Logged in!")

def test_shutdown():
    assert myChrome.shutdown() == None
    print("SUCCESS : Automation Closed!")