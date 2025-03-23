"""
Launch google
Perform a search using some search term
Print the Title
"""

# install all necessary dependencies
from selenium import  webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys # perform any keyboard actions
from time import sleep

class Data:
    url = "https://www.google.com"
    search_term = "Selenium Webdriver"

class Locators:
    search_locator = 'q' # name

class ChromeAPIDemo(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def perform_search(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        sleep(3)

        # enter search term
        search_box = self.driver.find_element(by=By.NAME, value= Locators.search_locator)
        search_box.send_keys(Data.search_term)
        sleep(2)

        search_box.send_keys(Keys.ENTER)
        sleep(5)

        print("Page Title:", self.driver.title)

if __name__ == "__main__":
    mysearch = ChromeAPIDemo()
    mysearch.perform_search()



