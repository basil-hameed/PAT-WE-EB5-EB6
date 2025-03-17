"""
Calendar date selection in JQuery site

https://jqueryui.com/datepicker/
"""

# import all dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class Data:
    url = "https://jqueryui.com/datepicker/#date-range"
    date = "03/19/2025"

class Locators:
    calendar_frame = '//iframe[@class="demo-frame"]'
    date_input_locator = '//input[@id="from"]'
    date_choice_locator = '//a[@data-date="19"]'

class CalendarAutomation(Data, Locators):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        sleep(5)

    def shutdown(self):
        self.driver.quit()

    def automate_calendar(self):
        try:
            self.start()

            # switch into the iframe
            frame_element = self.driver.find_element(by=By.XPATH, value=Locators.calendar_frame)

            self.driver.switch_to.frame(frame_element)

            # steps to select the exact date
            self.driver.find_element(by=By.XPATH, value=Locators.date_input_locator).click()

            # select the date 19-03-2025
            self.driver.find_element(by=By.XPATH, value=Locators.date_choice_locator).click()
            sleep(5)

            # fetch the date from the input box
            selected_date = self.driver.find_element(by=By.XPATH, value=Locators.date_input_locator)
            fetched_date = selected_date.get_attribute('value')

            return fetched_date

        except Exception as error:
            print("ERROR", error)

# if __name__ == "__main__":
#     mycalendar = CalendarAutomation()
#     mycalendar.automate_calendar()



