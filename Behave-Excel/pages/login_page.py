from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        self.wait.until(EC.presence_of_element_located((By.ID, "user-name"))).clear()
        self.driver.find_element(By.ID, 'user-name').send_keys(username)
        self.driver.find_element(By.ID, 'password').clear()
        self.driver.find_element(By.ID, 'password').send_keys(password)
        self.driver.find_element(By.ID, 'login-button').click()

    def is_login_successful(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_list')))
            return True
        except TimeoutException:
            return False