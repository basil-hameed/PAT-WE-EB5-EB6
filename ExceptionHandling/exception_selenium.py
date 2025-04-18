"""
Handle exception using try except blocks
https://www.guvi.in/
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
    url = "https://www.guvi.in/"


# create class named Locators to store all the locators
class Locators:
    rating_element = '//p[@class="⭐️1gjhl2-0 text-xl sm:text-2xl font-bold"]' # xpath

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

    def guvi_homepage(self):
        try:
            self.start_automation()
            get_rating = self.driver.find_element(by=By.XPATH, value=Locators.rating_element)

            # Fetch the rating text
            print("Overall Rating is: ", get_rating.text)

        except NoSuchElementException as error:
            print("ERROR : Element not found!")

        finally:
            self.driver.quit()


if __name__ == "__main__":
    myexception = SeleniumExceptions()
    myexception.guvi_homepage()



