"""
Working with HTML Tables

"""
# import dependencies
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

class HandleTables:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        sleep(4)

    def get_table_value(self):
        table_data = self.driver.find_element(By.XPATH, '//*[@id="content"]/table[1]/tbody/tr[4]/td[3]')

        print("Fetched Table Data Value : ", table_data.text)

    def get_all_row_value(self):

        table_rows = self.driver.find_elements(By.XPATH, '//*[@id="content"]/table[1]/tbody/tr[5]/td')
        for row_data in table_rows:
            print("Fetched Table Row Value : ", row_data.text)

    def get_all_header_value(self):

        table_headers = self.driver.find_elements(By.XPATH, '//*[@id="content"]/table[1]/tbody/tr[1]/th')
        for header_data in table_headers:
            print("Fetched Table Header Value : ", header_data.text)

    def shutdown(self):
        self.driver.quit()


if __name__ == "__main__":
    url = "https://afd.calpoly.edu/web/sample-tables"
    handle_dropdown = HandleTables(url)
    handle_dropdown.start()
    handle_dropdown.get_table_value()
    handle_dropdown.get_all_row_value()
    handle_dropdown.get_all_header_value()
    handle_dropdown.shutdown()
