"""
Validating the login functionality of nop commerce site
https://demo.nopcommerce.com/login
"""

# import all necessary dependencies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

# create classes and methods
class NopAutomation:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def perform_login(self):
        """
        Enter the email
        Enter the password
        Click the Login Button
        :return:
        """
        self.start_automation()
        self.driver.find_element(By.ID, 'Email').send_keys("test32@gmail.com")
        self.driver.find_element(By.ID, 'Password').send_keys("tester32")

        self.driver.find_element(By.XPATH, '//*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button').click()
        sleep(15)
        return self.driver.current_url

    def shutdown(self):
        self.driver.quit()

# Not necessary with Pytest
# if __name__ == "__main__":
#     url = "https://demo.nopcommerce.com/login"
#     myNopCommerce = NopAutomation(url)
#     myNopCommerce.start_automation()
#     myNopCommerce.perform_login()
#     myNopCommerce.shutdown()
