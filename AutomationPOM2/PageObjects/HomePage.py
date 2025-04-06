from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from TestData.data import OrangeHRMData
from TestLocators.locators import OrangeHRMLocators

class HomePage1:
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def login(self):
        # enter username
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.username_locator).send_keys(OrangeHRMData.username)

        # enter password
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.password_locator).send_keys(OrangeHRMData.password)

        # click login button
        self.driver.find_element(by=By.XPATH, value=OrangeHRMLocators.login_button_locator).click()

        return True

    def invalid_login(self):
        # enter username
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.username_locator).send_keys(OrangeHRMData.username)

        # enter password
        self.driver.find_element(by=By.NAME, value=OrangeHRMLocators.password_locator).send_keys(OrangeHRMData.invalid_password)

        # click login button
        self.driver.find_element(by=By.XPATH, value=OrangeHRMLocators.login_button_locator).click()

        return True