"""
Perform Form Filling and Login Automation in OrangeHRM Website
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Fill username and password
click the login button
validating the url
"""

# import necessary modules
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class OrangeAutomation:

    # Test Data
    username = "Admin"
    password = "admin123"

    # Test Locators
    username_locator = 'username' # name
    password_locator = 'password' # name
    button_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' # xpath

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(4)

    def shutdown(self):
        self.driver.quit()

    def login_automation(self):
        # exception handling
        try:
            self.start()
            # fill the username
            self.driver.find_element(by=By.NAME, value=self.username_locator).send_keys(self.username)

            # fill the password
            self.driver.find_element(by=By.NAME, value=self.password_locator).send_keys(self.password)

            # click the login button
            self.driver.find_element(by=By.XPATH, value=self.button_locator).click()
            sleep(5)

            if self.driver.current_url == "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index":
                print("SUCCESS : Login")
                return self.driver.current_url
            else:
                print("ERROR : Unable to Login")
                return False

        except Exception as e:
            print("ERROR : Automation Flow Error", e)
            return False
        finally:
            self.shutdown()
