"""
Launching the edge browser with a specific url "https://www.guvi.in/"
"""

# import all necessary modules
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep

class EdgeAutomation:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        sleep(8)

    def shutdown(self):
        self.driver.quit()

if __name__ == "__main__":
    url = "https://www.guvi.in/"
    myEdge = EdgeAutomation(url)
    myEdge.start()
    myEdge.shutdown()
    