"""
Perform pop up dialog handling

No need for Switch to Alerts or Action Chains
https://the-internet.herokuapp.com/entry_ad
"""

# import all necessary dependencies
from selenium import  webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Data:
    url = "https://the-internet.herokuapp.com/entry_ad"

class Locators:
    popup_locator = '//div[@class="modal"]' # XPATH
    close_button_locator = '//div[@class="modal-footer"]/p' # XPATH

class HandlePopup(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def handle_dialog_popup(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        sleep(5)

        # check whether the modal dialog popup appears, then click close button
        if self.driver.find_element(by=By.XPATH, value=Locators.popup_locator).is_displayed():
            self.driver.find_element(by=By.XPATH, value=Locators.close_button_locator).click()
            sleep(4)

            print("SUCCESS, Dialog popup handled")

        else:
            print("Error handling popup!")

if __name__ == "__main__":
    mypopup = HandlePopup()
    mypopup.handle_dialog_popup()