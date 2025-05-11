# TestScripts/test_login.py

import pytest
from playwright.sync_api import expect
from PageObjects.login_page import LoginPage
from TestData.data import Data

# setup and teardown
@pytest.fixture(scope="function")
def login_page():
    # setup
    page = LoginPage()
    yield page
    # teardown
    page.close()


class TestOrangeHRMLogin:
    def test_valid_login(self, login_page):
        # navigate to login page
        login_page.navigate()

        # perform login with valid credentials
        login_page.login(Data.username, Data.password)

        # assertion - check if dashboard is visible
        expect(login_page.page).to_have_url(Data.dashboard_url)
        print("SUCCESS: OrangeHRM Logged in!")

    def test_invalid_login(self, login_page):
        # navigate to login page
        login_page.navigate()

        # perform login with invalid credentials
        login_page.login(Data.invalid_username, Data.invalid_password)

        # assertion
        expect(login_page.page).not_to_have_url(Data.dashboard_url)
        print("SUCCESS: Not Logged in!")