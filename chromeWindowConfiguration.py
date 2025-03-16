"""
Open the chrome browser in 640 * 450 (width * height) configuration

Don't use service object
"""

# install all necessary dependencies
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

class Locators:
    username_locator = '//input[@name="username"]' # xpath
    password_locator = '//input[@name="password"]' # xpath
    login_locator = '//div[@class="oxd-form-actions orangehrm-login-action"]/button' # xpath

class ChromeWindowSize(Data, Locators):

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument(f"--window-size=640,450")
        self.driver = webdriver.Chrome(options=chrome_options)

    def window_automation(self):
        self.driver.get(Data.url)
        sleep(5)

        # enter the username in orangehrm portal
        username_box = self.driver.find_element(by=By.XPATH, value=Locators.username_locator)
        username_box.send_keys(Data.username)

        # enter the password in orangehrm portal
        password_box = self.driver.find_element(by=By.XPATH, value=Locators.password_locator)
        password_box.send_keys(Data.password)

        # click the login button
        login_button = self.driver.find_element(by=By.XPATH, value=Locators.login_locator)
        login_button.click()

        sleep(5)

        window_size = self.driver.get_window_size()
        print("Window Width", window_size['width'])
        print("WIndow Height", window_size['height'])

        print("SUCCESS, Window launched with desired size!")

if __name__ == "__main__":
    mychrome = ChromeWindowSize()
    mychrome.window_automation()