from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 15

    def find_element(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))
            return web_element
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

    def find_elements(self, locator):
        try:
            web_elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))
            return web_elements
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

    def enter_text(self, locator, text):
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

    def click(self, locator):
        try:
            element = self.find_element(locator)
            element.click()
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

    def is_visible(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return web_element.is_displayed()
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

    def is_enabled(self, locator):
        try:
            web_element = WebDriverWait(self.driver, self.timeout).until(EC.element_to_be_clickable(locator))
            return web_element.is_enabled()
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")

    def fetch_title(self):
        try:
            return self.driver.title
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")  

    def fetch_url(self):
        try:
            return self.driver.current_url
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR")               