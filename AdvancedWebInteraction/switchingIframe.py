"""
Switching iframe and fetch the content

https://jqueryui.com/droppable/

"""

# import all the necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class SwitchIframe:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(5)

    def fetchText(self):

        # switching iframe to fetch content inside
        frame_element = self.driver.find_element(By.XPATH, '//*[@id="content"]/iframe')

        self.driver.switch_to.frame(frame_element)

        drop_element = self.driver.find_element(By.XPATH, '//*[@id="droppable"]/p')

        fetched_text = drop_element.text

        print(fetched_text)

    def shutdown(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://jqueryui.com/droppable/"
    myiframe = SwitchIframe(url)
    myiframe.start()
    myiframe.fetchText()
    myiframe.shutdown()

