"""
Selecting an item from the dropdown

Tamilnadu

"""
# import dependencies
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

class HandleDropDown:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(4)

    def select_value(self):
        select = Select(self.driver.find_element(By.ID, 'state'))

        # select by visible_text
        # select.select_by_visible_text('Kerala')

        # select by values
        # select.select_by_value('Haryana')

        select.select_by_index(1)
        sleep(5)

        print("Selected Kerala from drop down!")

    def shutdown(self):
        self.driver.quit()


if __name__ == "__main__":
    url = "https://suman-dynamic-html-form.netlify.app/"
    handle_dropdown = HandleDropDown(url)
    handle_dropdown.start()
    handle_dropdown.select_value()
    handle_dropdown.shutdown()
