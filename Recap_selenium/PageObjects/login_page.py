"""
This login page contains all the methods related to the login actions, like enter_username etc.,
"""

from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocator.locator import Locators
from TestData.data import Data

class LoginPage(BasePage):
    # Storing all the Locators
    USERNAME_INPUT = (By.ID, Locators.username_locator)
    PASSWORD_INPUT = (By.ID, Locators.password_locator)
    LOGIN_BUTTON = (By.ID, Locators.login_button_locator)

    def enter_username(self, username):
        self.enter_text(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)
