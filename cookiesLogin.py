"""
Automate sauce demo page
and collect cookies
Using cookies to login
"""

# import all necessary dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
import json

class Data:
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"
    inventory_url = "https://www.saucedemo.com/inventory.html"

class Locators:
    username_locator = '//input[@id="user-name"]'
    password_locator = '//input[@id="password"]'
    login_button_locator = '//input[@id="login-button"]'


class CookiesLogin(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome()

    def login_and_save_cookies(self):
        self.driver.get(Data.url)

        # enter username, password and click login button
        self.driver.find_element(by=By.XPATH, value=Locators.username_locator).send_keys(Data.username)
        self.driver.find_element(by=By.XPATH, value=Locators.password_locator).send_keys(Data.password)
        self.driver.find_element(by=By.XPATH, value=Locators.login_button_locator).click()
        sleep(5)

        # save the cookies
        cookies = self.driver.get_cookies()
        with open("cookies.json", "w") as file:
            json.dump(cookies, file)

        print("Cookies are saved succesfully!")


    def login_using_cookies(self):
        self.driver.get(Data.url)

        # Load Cookies
        with open("cookies.json", "r") as file:
            cookies = json.load(file)
            for cookie in cookies:
                self.driver.add_cookie(cookie)

        sleep(5)

        # check inventory page
        self.driver.get(Data.inventory_url)
        sleep(5)

        print("Logged in with cookies!")
        self.driver.quit()

if __name__ == "__main__":
    mycookies = CookiesLogin()
    # mycookies.login_and_save_cookies()
    mycookies.login_using_cookies()
