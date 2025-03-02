"""
Homepage - Python selenium codes for performing automation
"""

# import all the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# create classes and methods
class GuviHome:
    def __init__(self, url):
        self.url = url # binding the url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())) # creating a driver object from webdriver

    # creating method to start selenium automation
    def start_automation(self):
        # using exception handling - try except blocks
        try:
            self.driver.get(self.url) # launches the page with url
            self.driver.maximize_window() # maximizes window
            return True
        except:
            print("Error : Unable to start the automation") # printing error statement
            return False

    # creating method to quit the browser instance
    def shutdown(self):
        self.driver.quit() # closes all browser instance

    # creating method to fetch the title
    def fetch_title(self):
        # using conditional statements to get title
        if self.start_automation(): # calling start_automation() method to launch automation
            return self.driver.title # returns the title
        else:
            print("Error: Unable to fetch the title!")
            return False # returns the False


    # creating the method to fetch the url
    def fetch_url(self):
        # using conditional statements
        if self.start_automation():
            return self.driver.current_url # returns the current url
        else:
            print("Error: Unable to fetch the url!")
            return False



