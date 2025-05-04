from PageObjects.base_page import BasePage
from PageObjects.login_page import LoginPage
from TestData.data import Data
from Configuration.conftest import driver

def test_title(driver):
    driver.get(Data.url)
    base_page = BasePage(driver)

    assert base_page.fetch_title() == "Swag Labs"
    print("SUCCESS, Title is valid!")

def test_url(driver):
    driver.get(Data.url)
    base_page = BasePage(driver)

    assert base_page.fetch_url() == Data.url
    print("SUCCESS, URL is valid!")

def test_login(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)

    login_page.enter_username(Data.username)
    login_page.enter_password(Data.password)
    login_page.click_login()

    assert Data.dashboard_url == driver.current_url
    print("SUCCESS: Login Successful")

def test_validate_password_input(driver):
    driver.get(Data.url)
    login_page = LoginPage(driver)

    password_input_box = login_page.validate_password()
    assert password_input_box == True
    print("SUCCESS: Password input box is validated!")
