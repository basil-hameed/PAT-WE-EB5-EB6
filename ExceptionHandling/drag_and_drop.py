"""
Perform drag and drop using action chains

https://qavbox.github.io/demo/dragndrop/
"""

# import all necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from time import sleep

# Action Chains
from selenium.webdriver.common.action_chains import ActionChains

# classes to store data and locators
class Data:
    url = "https://qavbox.github.io/demo/dragndrop/"

class Locators:
    source = 'draggable' #ID
    target = 'droppable' #ID

class DragandDrop(Data, Locators):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # create an action_chain object by passing the driver into the ActionChains class
        self.action = ActionChains(self.driver)


    def drag_drop(self):
        try:
            self.driver.get(Data.url)
            self.driver.maximize_window()
            sleep(5)

            source_element = self.driver.find_element(by=By.ID, value=Locators.source)
            target_element = self.driver.find_element(by=By.ID, value=Locators.target)

            # perform drag and drop
            self.action.drag_and_drop(source_element, target_element).perform()

            print("Successful Drag and Drop")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

        finally:
            self.driver.quit()

if __name__ == "__main__":
    my_actions = DragandDrop()
    my_actions.drag_drop()