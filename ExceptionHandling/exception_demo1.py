"""
Handle exception using try except blocks
https://qavbox.github.io/demo/delay/
"""

# import all necessary dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# use the python selenium exceptions
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchDriverException
from selenium.common.exceptions import TimeoutException
from time import sleep


# create class named Data to store all the data
class Data:
    url = "https://qavbox.github.io/demo/delay/"


# create class named Locators to store all the locators
class Locators:
    tryme_element = 'commit1' #name
    displayed_element = '//h2[@id="delay"]' # xpath

class SeleniumExceptions(Data, Locators):

    def __init__(self):
        # using try except block
        try:
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        except NoSuchDriverException as error:
            print("ERROR: Selenium Driver Error", error)

    def start_automation(self):
        try:
            self.driver.get(Data.url)
            self.driver.maximize_window()
        except TimeoutException as error:
            print("ERROR: Timeout happened", error)

    def click_tryme(self):
        try:
            self.start_automation()

            tryme = self.driver.find_element(by=By.NAME, value=Locators.tryme_element)
            tryme.click()
            sleep(6)

            get_displayed = self.driver.find_element(by=By.XPATH, value=Locators.displayed_element)

            # Fetch the rating text
            print("The text is: ", get_displayed.text)

        except NoSuchElementException as error:
            print("ERROR : Element not found!")

        finally:
            self.driver.quit()


if __name__ == "__main__":
    myexception = SeleniumExceptions()
    myexception.click_tryme()



