"""
Navigating in the guvi page
https://www.guvi.in/
"""

# import all the necessary modules/dependencies
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class GuviAutomation:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def start_automation(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)
        print("URL 1 : ", self.driver.current_url)

    def click_login(self):
        self.driver.find_element(By.ID, 'login-btn').click()
        sleep(5)
        print("URL 2 : ", self.driver.current_url)

    def click_signup(self):
        self.driver.find_element((By.CLASS_NAME, 'signup')).click()
        sleep(5)
        print("URL x : ", self.driver.current_url)

    def move_backward(self):
        self.driver.back()
        print("URL 3 : ", self.driver.current_url)
        sleep(5)

    def move_forward(self):
        self.driver.forward()
        print("URL 4 : ", self.driver.current_url)
        sleep(5)

    def shutdown(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.guvi.in/"
    myGuvi = GuviAutomation(url)
    myGuvi.start_automation()
    myGuvi.click_login()
    myGuvi.move_backward()
    myGuvi.move_forward()
    myGuvi.shutdown()

"""
URL 1 :  https://www.guvi.in/
URL 2 :  https://www.guvi.in/sign-in/
URL 3 :  https://www.guvi.in/
URL 4 :  https://www.guvi.in/sign-in/
"""