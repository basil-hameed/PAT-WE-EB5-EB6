"""
Open firefox browser in desired size 640 * 450 configuration

Same Login Process in NopCommerce
"""
# install all necessary dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class Data:
    url = "https://demo.nopcommerce.com/login"
    email = "test16@gmail.com"
    password = "test@123"

class Locators:
    email_locator = '//input[@id="Email"]'
    password_locator = '//input[@id="Password"]'
    login_locator = '//button[contains(text(), "Log in")]'

class FirefoxWindowSize(Data, Locators):

    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument(f"--width=640")
        firefox_options.add_argument(f"--height=450")
        self.driver = webdriver.Firefox(options=firefox_options)

    def window_automation(self):
        self.driver.get(Data.url)
        sleep(5)

        # enter the username in nopcommerce page
        email_box = self.driver.find_element(by=By.XPATH, value=Locators.email_locator)
        email_box.send_keys(Data.email)

        # enter the password in nopcommerce page
        password_box = self.driver.find_element(by=By.XPATH, value=Locators.password_locator)
        password_box.send_keys(Data.password)

        # click the login button
        login_button = self.driver.find_element(by=By.XPATH, value=Locators.login_locator)
        login_button.click()

        sleep(5)

        window_size = self.driver.get_window_size()

        self.driver.quit()
        print("Window Width: ", window_size['width'])
        print("Window Height: ", window_size['height'])

        print("SUCCESS, Firefox launched with exact size!")

if __name__ == "__main__":
    myfirefox = FirefoxWindowSize()
    myfirefox.window_automation()