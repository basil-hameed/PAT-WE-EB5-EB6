"""
Automate facebook page with fluent wait
Adding polling_frequency and ignored exceptions
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import ElementNotInteractableException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Data:
    username = "Tom Harris"
    password = "Secret@23"
    facebook_url = "https://www.facebook.com/"

class Locators:
    username_input_locator = 'email' # ID
    password_input_locator = 'pass' # ID
    login_button_locator = 'login' # NAME

class FluentExample(Data, Locators):
    def __init__(self):
        self.url = Data.facebook_url
        # create driver object and pass the service
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # create the wait object and pass driver and timeout
        self.wait = WebDriverWait(self.driver, 10, poll_frequency=5, ignored_exceptions=[ElementNotInteractableException])

    def launch_facebook(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()

            # enter the username and password
            username = self.wait.until(EC.presence_of_element_located((By.ID, Locators.username_input_locator)))
            username.send_keys(Data.username)

            password = self.wait.until(EC.presence_of_element_located((By.ID, Locators.password_input_locator)))
            password.send_keys(Data.password)

            # click the login button
            login_button = self.wait.until(EC.element_to_be_clickable((By.NAME, Locators.login_button_locator)))
            login_button.click()

            print("SUCCESS: Automated facebook page!")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)


if __name__ == "__main__":
    myfluent = FluentExample()
    myfluent.launch_facebook()