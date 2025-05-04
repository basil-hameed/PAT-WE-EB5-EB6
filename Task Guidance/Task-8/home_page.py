from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class HomePage:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("https://demoblaze.com/index.html")
        sleep(3)

    def perform_login(self):
        
        # click login button
        login_menu = self.driver.find_element(by=By.ID, value= 'login2')
        login_menu.click()
        sleep(3)

        username_box = self.driver.find_element(by=By.ID, value= 'loginusername')
        username_box.send_keys("eb56@gmail.com")

        password_box = self.driver.find_element(by=By.ID, value= 'loginpassword')
        password_box.send_keys("tester@123")      

        login_button = self.driver.find_element(by=By.XPATH, value= '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        login_button.click()
        sleep(3)


    def fetch_page_title(self):
        title = self.driver.title
        print("Title of the page is,", title)
        return title

    def fetch_page_url(self):
        page_url = self.driver.current_url
        print("The URL is,", page_url)
        return page_url

    def fetch_page_content(self):
        webpage_content = self.driver.page_source

        with open('webpage_task8.txt', 'w') as file:
            file.write(webpage_content)
        print("Page content added inside the file!")
