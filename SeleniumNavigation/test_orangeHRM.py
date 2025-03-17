from OrangeHRMLogin import OrangeAutomation

# creating an object from OrangeAutomation
url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
myHRMAutomation = OrangeAutomation(url)

def test_valid_login():
    expected_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    assert  myHRMAutomation.login_automation() == expected_url
    print("Test Case Passed: Logged in!")
