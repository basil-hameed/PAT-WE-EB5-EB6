# PageObjects/login_page.py
# import playwright
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from TestData.data import Data

class LoginPage:

    def __init__(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        # Locators
        self.username_input = self.page.locator('input[name="username"]') # Attribute
        self.password_input = self.page.locator('input[name="password"]') # Attribute
        self.login_button = self.page.locator("//button[text()=' Login ']") # Xpath
        self.error_message = self.page.locator("//p[text()='Invalid credentials']") # Xpath

    def navigate(self):
        self.page.goto(Data.orangehrm_url)
        expect(self.username_input).to_be_visible()

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def error_message(self):
        expect(self.error_message).to_be_visible()
        return self.error_message.text_content()

    def close(self):
        self.browser.close()
        self.playwright.stop()
