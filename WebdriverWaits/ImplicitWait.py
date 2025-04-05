"""
Automating facebook page
Using Implicit Wait
(Global Wait)
"""

# install all necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class Data:
    facebook_url = "https://www.facebook.com/"
    username = "tom harris"
    password = "Secret@123"

class Locators:
    username_input_locator = 'email' # ID
    password_input_locator = 'pass' # ID
    login_locator = 'login' # NAME


# create a class inherit the data and locators
class ImplicitExample(Data, Locators):

    def __init__(self):
        self.url = Data.facebook_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def launch_facebook(self):
        try:
            # add the implicit wait
            self.driver.implicitly_wait(10)
            self.driver.get(self.url)
            self.driver.maximize_window()

            # enter username and password
            username = self.driver.find_element(by=By.ID, value=Locators.username_input_locator)
            username.send_keys(Data.username)

            password = self.driver.find_element(by=By.ID, value=Locators.password_input_locator)
            password.send_keys(Data.password)

            # click the login button
            login_button = self.driver.find_element(by=By.NAME, value=Locators.login_locator)
            login_button.click()

            print("SUCCESS, Login")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

if __name__ == "__main__":
    myimplicit = ImplicitExample()
    myimplicit.launch_facebook()