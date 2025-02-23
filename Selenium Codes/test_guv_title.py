"""
Test script to validate the website title of "https://www.guvi.in/" using chrome browser
"""


# importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TestTitle:

    def __init__(self, url, expected_title):
        self.url = url
        self.expected_title = expected_title
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        sleep(5)

    def validateTitle(self):
        actual_title = self.driver.title
        if actual_title == self.expected_title:
            print("Test Case Passed: Title Validated")
        else:
            print("Test Case Failed")

    def shutdown(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.guvi.in/"
    expected_title = "GUVI | Learn to code in your native language"
    myguvi = TestTitle(url, expected_title)
    myguvi.start()
    myguvi.validateTitle()
    myguvi.shutdown()
