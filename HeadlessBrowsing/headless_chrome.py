"""
Perform headless automation in chrome browser

Launch the headless chrome
Fetch the title and url
Quit the browser instance

"""

# import all the necessary dependencies
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class ChromeHeadless:

    def __init__(self, url):
        self.url = url

        # code for headless browsing in Firefox
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        # chrome webdriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)


    def start(self):
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            sleep(3)
            print("PROCESS 1 : Chrome browser is working!")
            return True

        except Exception as error:
            print("ERROR : Automation Failed!", error)

    def shutdown(self):
        print("PROCESS 2 : Automation Closed!")
        self.driver.quit()

    def fetch_url(self):
            if self.start():
                return self.driver.current_url
            else:
                return False


    def fetch_title(self):
            if self.start():
                return self.driver.title
            else:
                return False

if __name__ == "__main__":
    guvi_url = "https://www.guvi.in/courses/"
    myheadless = ChromeHeadless(guvi_url)
    print(myheadless.fetch_url())
    print(myheadless.fetch_title())
    myheadless.shutdown()

"""
PROCESS 1 : Chrome browser is working!
https://www.guvi.in/courses/?current_tab=paidcourse
PROCESS 1 : Chrome browser is working!
GUVI | courses
PROCESS 2 : Automation Closed!
"""



