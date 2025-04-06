from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from TestData.data import OrangeHRMData
from TestLocators.locators import OrangeHRMLocators

class DashboardPage1:
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def get_title(self):
        title = self.driver.title
        return title

    def get_url(self):
        url = self.driver.current_url
        return url

