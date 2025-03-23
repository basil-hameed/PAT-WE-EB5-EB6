"""
Based on user input, use chrome/firefox api's

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

# For Chrome APIs
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

# For Firefox APIs
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from selenium.webdriver.common.by import By
from time import sleep

# class to store all data values
class Data:
    url = "https://the-internet.herokuapp.com/"
    username = "tomsmith"
    password = "SuperSecretPassword!"

# class to store all locator values
class Locators:
    authentication_button = '//a[contains(text(), "Form Authentication")]' # //a[@href="/login"]
    username_textbox = '//input[@id="username"]'
    password_textbox = '//input[@id="password"]'
    login_button_locator = '//button[@class="radius"]'
    message_locator = '//div[@id="flash"]'

# class inherited with Data and Locators
class APIDemo(Data, Locators):

    def __init__(self, browser_name):
        # If chrome browser, setup chrome related service and options
        if browser_name.lower() == "chrome":
            chrome_options = ChromeOptions()
            chrome_options.add_argument("--headless")
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        # Elif firefox browser, setup firefox related service and options
        elif browser_name.lower() == "firefox":
            firefox_options = FirefoxOptions()
            firefox_options.add_argument("--headless")
            self.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()), options=firefox_options)
        # Else unknown browser name throws ValueError
        else:
            raise ValueError("Unsupported Browser!")


    def validate_login(self):
        # open the heroku website
        self.driver.get(Data.url)
        self.driver.maximize_window()
        sleep(5)

        # click on form authentication
        form_button = self.driver.find_element(by=By.XPATH, value=Locators.authentication_button)
        form_button.click()
        sleep(4)

        # login process enter username, password and click login button
        username_box = self.driver.find_element(by=By.XPATH, value=Locators.username_textbox)
        username_box.send_keys(Data.username)
        sleep(2)

        password_box = self.driver.find_element(by=By.XPATH, value=Locators.password_textbox)
        password_box.send_keys(Data.password)
        sleep(2)

        login_button = self.driver.find_element(by=By.XPATH, value=Locators.login_button_locator)
        login_button.click()
        sleep(5)

        # print the success message
        confirmation_message = self.driver.find_element(by=By.XPATH, value=Locators.message_locator)
        print(confirmation_message.text)


if __name__ == "__main__":
    # select based on preferred api's
    # browser_input = "chrome"
    browser_input = "firefox"
    myautomation = APIDemo(browser_input)
    myautomation.validate_login()
