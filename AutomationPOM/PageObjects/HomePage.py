"""
Contains all the methods relevant to the home page
https://opensource-demo.orangehrmlive.com/web/index.php/auth/login

Automation Flow
1. Enter username
2. Enter password
3. Click login button
4. Validation
"""

# import all necessary dependencies
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

# import the data and locators package
from TestData.data import OrangeHRMData
from TestLocators.locators import OrangeHRMLocators


class HomePage1():
    # create the driver object
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # homepage relevant methods
    def start(self):
        self.driver.implicitly_wait(10)
        self.driver.get(OrangeHRMData.orange_url)
        self.driver.maximize_window()
        return True

    def login(self):
        # enter username
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.username_locator).send_keys(OrangeHRMData.username)

        # enter password
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.password_locator).send_keys(OrangeHRMData.password)

        # click login button
        self.driver.find_element(by=By.XPATH, value=OrangeHRMLocators.login_button_locator).click()

        return True

    def shutdown(self):
        self.driver.quit()
        return None