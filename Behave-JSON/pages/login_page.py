from locators.web_locators import Locators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, timeout=10)

    def login(self, username, password):
        self.driver.find_element(*Locators.username).clear()
        self.driver.find_element(*Locators.username).send_keys(username)
        self.driver.find_element(*Locators.password).clear()
        self.driver.find_element(*Locators.password).send_keys(password)
        self.driver.find_element(*Locators.login_button).click()

    def login_successful(self):
        try:
            self.wait.until(EC.presence_of_element_located(Locators.inventory))
            return True
        except (TimeoutException, NoSuchElementException):
            return False
