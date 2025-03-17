"""
Perform window switch using window ID in Cowin Website
https://www.cowin.gov.in/

Launch cowin website
Get the homepage window handle
Click the dashboard
Get all the window handles
Then switched to the newly opened window and close
And finally close the browser instance
"""

# import all the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# create classes and methods
class MyCowin:

    # Test Locators
    dashboard_locator = '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[2]/a'

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def switch_window(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(4)

        # Get the homepage window handle
        homepage_window_handle = self.driver.current_window_handle
        print("Cowin Homepage Window ID :", homepage_window_handle)

        # Click the Dashboard button
        self.driver.find_element(By.XPATH, self.dashboard_locator).click()

        # Get all the window handles
        all_window_handles = self.driver.window_handles
        print("All Handles :", all_window_handles)

        # Logic for switching window
        for window in all_window_handles:
            if window != homepage_window_handle:
                self.driver.switch_to.window(window)
                print(f"Switched to Window : {window}")
                sleep(3)
                self.driver.close() # closing the current window
                print(f"Closed Window : {window}")
                sleep(3)
                break

        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.cowin.gov.in/"
    myCowinAutomation = MyCowin(url)
    myCowinAutomation.switch_window()


"""
Cowin Homepage Window ID : F4B4BA13F44580FE3136A0353D614174
All Handles : ['F4B4BA13F44580FE3136A0353D614174', 'CBE06624A80F0C074FF2DF361290EA85']
Switched to Window : CBE06624A80F0C074FF2DF361290EA85
Closed Window : CBE06624A80F0C074FF2DF361290EA85
"""