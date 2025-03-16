"""
Open chrome browser in incognito and perform automation

Test Steps:
Orangehrm login
"""

# install necessary dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from time import sleep

# create Data and Locator classes separately
class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

class Locators:
    username_locator = '//input[@name="username"]'
    password_locator = '//input[@name="password"]'
    login_locator = '//div[@class="oxd-form-actions orangehrm-login-action"]/button'

class ChromeIncognito(Data, Locators):

    def __init__(self):
        # creating a chrome options object
        chrome_options = Options()
        chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=chrome_options)

    def launchIncognito(self):
        self.driver.get(Data.url)
        sleep(5)

        # enter username
        username_box = self.driver.find_element(by=By.XPATH, value=Locators.username_locator)
        username_box.send_keys(Data.username)

        # enter password
        password_box = self.driver.find_element(by=By.XPATH, value=Locators.password_locator)
        password_box.send_keys(Data.password)

        # click login
        login_button = self.driver.find_element(by=By.XPATH, value=Locators.login_locator)
        login_button.click()

        sleep(5)

        print("SUCCESS, Chrome launched in incognito mode!")

if __name__ == "__main__":
    mychrome = ChromeIncognito()
    mychrome.launchIncognito()










