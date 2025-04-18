"""
Launching the chrome browser with a specific url "https://www.guvi.in/"
"""

# importing the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# Always follow oops concept
class MyAutomation:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # launch the browser instance
    def start(self):
        self.driver.get(self.url)
        sleep(5)
        print(self.driver.title)

    # close all the browser instances
    def shutdown(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.guvi.in/"
    myautomation = MyAutomation(url)
    myautomation.start()
    myautomation.shutdown()