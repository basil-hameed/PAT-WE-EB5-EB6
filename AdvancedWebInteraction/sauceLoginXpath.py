"""
Automation Logic using Xpath in Swag Labs

Launch the website https://www.saucedemo.com/
Sleep time of 5 secs
Enter the username standard_user
Enter the password secret_sauce
Click login button
Validate the successful login

"""

# import all the necessary dependencies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Data:
    url = "https://www.saucedemo.com/"
    username = "standard_user"
    password = "secret_sauce"

class Locator:
    username_locator = '//input[@id="user-name"]'
    password_locator = '//input[@id="password"]'
    login_button_locator = '//input[@id="login-button"]'
    products_locator = "//span[contains(text(), 'Products')]"

class SwagAutomation(Data, Locator):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        sleep(5)

    def shutdown(self):
        self.driver.quit()

    def validate_login(self):
        # enter the username
        username_element = self.driver.find_element(by=By.XPATH, value=Locator.username_locator)
        username_element.send_keys(Data.username)

        # enter the password
        password_element = self.driver.find_element(by=By.XPATH, value=Locator.password_locator)
        password_element.send_keys(Data.password)

        # click login
        login_button = self.driver.find_element(by=By.XPATH, value=Locator.login_button_locator)
        login_button.click()
        sleep(5)

        #validate the login
        products_element = self.driver.find_element(by=By.XPATH, value=Locator.products_locator)
        products_text = products_element.text

        # using assert to validate "Products" displayed in homepage
        assert products_text == "Products"
        print("SUCCESS: Test Passed!")

if __name__ == "__main__":
    myswag = SwagAutomation()
    myswag.start()
    myswag.validate_login()
    myswag.shutdown()




