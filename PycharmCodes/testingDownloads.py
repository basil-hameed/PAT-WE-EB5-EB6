"""
launch the firefox browser and fetch the title and url
validate them with expected data
https://www.python.org/downloads/
"""

# import all necessary modules
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


# using OOP's approach, creating proper classes and methods for writing my automation scripts

class PythonAutomation:
    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    # start method to launch automation
    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)

    # validate data method to check title and url
    def validate_data(self):
        # validating title
        expected_title = "Download Python | Python.org"
        actual_title = self.driver.title

        # validating url
        expected_url = "https://www.python.org/downloads/"
        actual_url = self.driver.current_url

        if expected_title == actual_title and expected_url == actual_url:
            print("Test Case Passed!")
        else:
            print("Test Case Failed")

    # create shutdown method to close the browser instance
    def shutdown(self):
        self.driver.quit()


if __name__ == "__main__":
    url = "https://www.python.org/downloads"
    pydownloads = PythonAutomation(url)
    pydownloads.start()
    pydownloads.validate_data()
    pydownloads.shutdown()

