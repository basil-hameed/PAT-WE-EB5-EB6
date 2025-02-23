"""
Launching the firefox browser with a specific url "https://www.guvi.in/"
"""

# Import necessary modules
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class FirefoxAutomation:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        sleep(8)

    def shutdown(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.guvi.in/"
    myfirefox = FirefoxAutomation(url)
    myfirefox.start()
    myfirefox.shutdown()

    

