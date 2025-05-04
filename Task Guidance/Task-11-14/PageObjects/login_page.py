from selenium.webdriver.common.by import By
from PageObjects.base_page import BasePage
from TestLocators.locators import Locators
from TestData.data import Data

class LoginPage(BasePage):
    # store all the locators
    username_input = (By.ID, Locators.username_input_locator)
    password_input = (By.ID, Locators.password_input_locator)
    login_button = (By.ID, Locators.login_button_locator)

    def enter_username(self, username):
        self.enter_text(self.username_input, Data.username)

    def enter_password(self, password):
        self.enter_text(self.password_input, Data.password)

    def click_login(self):
        self.click(self.login_button)

    def validate_username(self):
        return self.is_visible(self.username_input)
    
    def validate_password(self):
        return self.is_visible(self.password_input)
    