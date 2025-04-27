"""
This test_login file contains all the test cases related to login page

Use driver_setup() function must be passed
"""

from PageObjects.login_page import LoginPage
from PageObjects.base_page import BasePage
from TestData.data import Data
from TestLocator.locator import Locators
from Configuration.conftest import driver_setup

def test_title(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)

    assert base_page.fetch_title() == "Swag Labs"
    print("SUCCESS: Title is valid")


def test_url(driver_setup):
    driver_setup.get(Data.url)
    base_page = BasePage(driver_setup)

    assert base_page.fetch_url() == "https://www.saucedemo.com/v1/index.html"
    print("URL is valid!")

def test_valid_login(driver_setup):
    driver_setup.get(Data.url)
    login_page = LoginPage(driver_setup)

    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()

    assert "https://www.saucedemo.com/v1/inventory.html" == driver_setup.current_url
    print("SUCCESS: Login is valid!")




