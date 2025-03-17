"""
headless_orangehrm.py contains the selenium automation methods
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Validating the username text box
Validating the password text box
Validating the login button
Validating the login
"""

# import all necessary dependencies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class HRMData:
    # Test Data
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
    username = "Admin"
    password = "admin123"

class HRMLocators:
    # Test Locators
    username_input_locator = 'username' #name locator
    password_input_locator = 'password' #name locator
    login_button_locator = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' # xpath locator


class HeadlessTesting:
    def __init__(self, url):
        self.url = url

        # enable headless browsing using chrome browser
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        # webdriver headless chrome
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    def start(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            sleep(4)
            return True
        except Exception as error:
            print("ERROR : Automation Failed!", error)
            return False

    def shutdown(self):
        self.driver.quit()
        return None

    def validate_username_input_box(self):
        username_input_box = self.driver.find_element(by=By.NAME, value=HRMLocators.username_input_locator)
        if username_input_box.is_displayed():
            return True
        else:
            return False

    def validate_password_input_box(self):
        password_input_box = self.driver.find_element(by=By.NAME, value=HRMLocators.password_input_locator)
        if password_input_box.is_displayed():
            return True
        else:
            return False

    def validate_login_button(self):
        login_button = self.driver.find_element(by=By.XPATH, value=HRMLocators.login_button_locator)
        if login_button.is_displayed():
            return True
        else:
            return False


    def validate_login(self):
        try:
            self.driver.find_element(by=By.NAME, value=HRMLocators.username_input_locator).send_keys(HRMData.username)
            sleep(2)
            self.driver.find_element(by=By.NAME, value=HRMLocators.password_input_locator).send_keys(HRMData.password)
            sleep(2)
            self.driver.find_element(by=By.XPATH, value=HRMLocators.login_button_locator).click()
            sleep(4)
            if self.driver.current_url == HRMData.dashboard_url:
                return self.driver.current_url
            else:
                return False

        except Exception as error:
            print("ERROR : Login Failed", error)
