"""
Launch firefox browser in Incognito Mode

Automate login demoblaze website
"""

# import all necessary dependencies
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep

class Data:
    url = "https://demoblaze.com/index.html"
    username = "tester37@gmail.com"
    password = "admin@123"

class Locators:
    username_locator = '//input[@id="loginusername"]'
    password_locator = '//input[@id="loginpassword"]'
    login_button_locator = '//button[contains(text(), "Log in")]'
    login_item = '//a[@id="login2"]'

class FirefoxIncognito(Data, Locators):

    def __init__(self):
        firefox_options = Options()
        firefox_options.add_argument("-private")
        self.driver = webdriver.Firefox(options=firefox_options)

    def launchIncognito(self):
        try:
            self.driver.get(Data.url)
            self.driver.maximize_window()
            sleep(5)

            # click login to open login window
            login_menu = self.driver.find_element(by=By.XPATH, value=Locators.login_item)
            login_menu.click()
            sleep(2)

            # enter the username of demoblaze website
            username_box = self.driver.find_element(by=By.XPATH, value=Locators.username_locator)
            username_box.send_keys(Data.username)

            # enter the password of demoblaze site
            password_box = self.driver.find_element(by=By.XPATH, value=Locators.password_locator)
            password_box.send_keys(Data.password)

            # click the log in button
            login_button = self.driver.find_element(by=By.XPATH, value=Locators.login_button_locator)
            login_button.click()

            sleep(5)

            print("SUCCESS, Firefox launched in incognito mode!")

        except Exception as error:
            print("ERROR", error)

        finally:
            self.driver.quit()

if __name__ == "__main__":
    myfirefox = FirefoxIncognito()
    myfirefox.launchIncognito()



