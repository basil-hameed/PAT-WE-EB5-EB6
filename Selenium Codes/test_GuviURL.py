"""
Launching the chrome browser with this URL "https://www.guvi.in/" and the validate the URL 
present in the web application
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class TestUrl:

    def __init__(self, guvi_url):
        self.guvi_url = guvi_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(self.guvi_url)
        sleep(5)

    def validate_url(self):
        current_url = self.driver.current_url
        if current_url == self.guvi_url:
            print("Test Case Passed: URL Validated Successfully")
        else:
            print("Test Case Failed")

    def shutdown(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.guvi.in/"
    mytest = TestUrl(url)
    mytest.start()
    mytest.validate_url()
    mytest.shutdown()