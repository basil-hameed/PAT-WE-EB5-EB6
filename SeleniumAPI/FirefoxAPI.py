# Firefox API Example

# Launching firefox and navigate to a website

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep


class Data:
    url = "https://www.google.com"

class FirefoxAPIDemo(Data):
    def __init__(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def launch_google(self):
        try:
            self.driver.get(Data.url)
            self.driver.maximize_window()
            sleep(3)

            print("Page Title:", self.driver.title)

        finally:
            self.driver.quit()


if __name__ == "__main__":
    mygoogle = FirefoxAPIDemo()
    mygoogle.launch_google()

