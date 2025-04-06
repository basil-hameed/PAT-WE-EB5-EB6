"""
Add all the test scripts related to home page
"""

from PageObjects.HomePage import HomePage1

def test_start():
    assert HomePage1().start() == True
    print("SUCCESS: Automation started!")

def test_login():
    assert HomePage1().login() == True
    print("SUCCESS: Logged In!")

def test_shutdown():
    assert HomePage1().shutdown() == None
    print("SUCCESS: Automation executed!")