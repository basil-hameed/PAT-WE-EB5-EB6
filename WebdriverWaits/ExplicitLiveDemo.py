"""
Automate the facebook page
https://www.facebook.com/

Use python selenium, explicit wait, chrome desired capabilities 640 * 450
"""
# add all necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# exceptions import
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

# explicit waits import
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome option
from selenium.webdriver.chrome.options import Options as ChromeOptions

class Data:
    facebook_url = "https://www.facebook.com/"
    username = "Anderson"
    password = "Secret@23"

class Locators:
    username_input_locator = 'email' # ID
    password_input_locator = 'pass' # ID
    login_button_locator = 'login' # NAME

# create class and inherit the data and locators
class ExplicitDemo(Data, Locators):

    def __init__(self):
        self.url = Data.facebook_url

        # options object
        self.chrome_options = ChromeOptions()
        self.chrome_options.add_argument(f"--window-size={640},{450}")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 10)

    def launch_automation(self):
        try:
            self.driver.get(self.url)

            # enter username and password
            username = self.wait.until(EC.presence_of_element_located((By.ID, Locators.username_input_locator)))
            username.send_keys(Data.username)

            password = self.wait.until(EC.presence_of_element_located((By.ID, Locators.password_input_locator)))
            password.send_keys(Data.password)

            # click the login button
            login = self.wait.until(EC.element_to_be_clickable((By.NAME, Locators.login_button_locator)))
            login.click()

            print("SUCCESS, Login performed!")


        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

if __name__ == "__main__":
    myexplicitdemo = ExplicitDemo()
    myexplicitdemo.launch_automation()
