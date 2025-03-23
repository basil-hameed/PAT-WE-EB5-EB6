"""
https://the-internet.herokuapp.com/login

Test Steps:
1. Launch the webpage
2. Click Form Authentication Button
3. Enter username 'tomsmith'
4. Enter password 'SuperSecretPassword!'
5. Click login button
6. print the success message
"""
# import all necessary dependencies

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Data:
    url = "https://the-internet.herokuapp.com/"
    username = "tomsmith"
    password = "SuperSecretPassword!"

class Locators:
    authentication_button = '//a[contains(text(), "Form Authentication")]' # //a[@href="/login"]
    username_textbox = '//input[@id="username"]'
    password_textbox = '//input[@id="password"]'
    login_button_locator = '//button[@class="radius"]'
    message_locator = '//div[@id="flash"]'

class APIChrome(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def validate_login(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        sleep(5)

        # click form authentication
        form_authentication = self.driver.find_element(by=By.XPATH, value=Locators.authentication_button)
        form_authentication.click()
        sleep(3)

        # login steps
        # enter the username
        username_box = self.driver.find_element(by=By.XPATH, value=Locators.username_textbox)
        username_box.send_keys(Data.username)

        # enter the password
        password_box = self.driver.find_element(by=By.XPATH, value=Locators.password_textbox)
        password_box.send_keys(Data.password)

        # click login button
        login_button = self.driver.find_element(by=By.XPATH, value=Locators.login_button_locator)
        login_button.click()
        sleep(5)

        # print the success message
        confirmation_message = self.driver.find_element(by=By.XPATH, value=Locators.message_locator)
        print(confirmation_message.text)


if __name__ == "__main__":
    mychrome = APIChrome()
    mychrome.validate_login()

