"""
Handling the alerts using action chains
https://qavbox.github.io/demo/alerts/

"""
# import all the necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep

class Data:
    url = "https://qavbox.github.io/demo/alerts/"
    my_data = "hello folks"

class Locators:
    submit_button = '//input[@name="commit"]'
    prompt_me_button = 'prompt' #ID
    confirm_button = 'confirm' # ID

class AlertBox(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_automation(self):
        self.driver.get(Data.url)
        self.driver.maximize_window()
        sleep(5)

    def simple_alert(self):
        try:
            self.start_automation()
            self.driver.find_element(by=By.XPATH, value=Locators.submit_button).click()

            # switch to alert to perform action
            alert_window = self.driver.switch_to.alert

            # accept the alert or click OK
            alert_window.accept()

            print("SUCCESS: OK Button Clicked!")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)
        finally:
            self.driver.quit()

    def prompt_alert(self):
        try:
            self.start_automation()
            self.driver.find_element(by=By.ID, value=Locators.prompt_me_button).click()

            alert_window = self.driver.switch_to.alert
            alert_window.send_keys(Data.my_data)
            sleep(4)

            print("SUCCESS, Prompt entered!")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)
        finally:
            self.driver.quit()

    def confirm_alert(self):
        try:
            self.start_automation()
            self.driver.find_element(by=By.ID, value=Locators.confirm_button).click()

            alert_window = self.driver.switch_to.alert

            alert_window.dismiss()
            sleep(4)

            print("SUCCESS, Handled alert with dismiss!")
        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)
        finally:
            self.driver.quit()


if __name__ == "__main__":
    myalert = AlertBox()
    # myalert.simple_alert()
    # myalert.prompt_alert()
    myalert.confirm_alert()
