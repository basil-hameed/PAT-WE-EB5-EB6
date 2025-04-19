from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from Utilities.yaml_functions import YAMLReader
from TestLocators.locators import Locators

class TestSauceKDTF:

    def test_sauce_login(self):
        file_name = "D:\Automation\PAT-EB-6\KDTF_EB\TestData\config.yaml"

        # create yaml reader object by passing the file name
        yaml_reader = YAMLReader(file_name)

        # create driver object by passing the service
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        try:
            driver.get(yaml_reader.reader()['url'])
            driver.maximize_window()
            driver.implicitly_wait(10)

            # automation flow to perform login
            # enter the username
            driver.find_element(by=By.ID, value=Locators.username_locator).send_keys(yaml_reader.reader()['username'])

            # enter the password
            driver.find_element(by=By.ID, value=Locators.password_locator).send_keys(yaml_reader.reader()['password'])

            # click the login button
            driver.find_element(by=By.ID, value=Locators.login_button_locator).click()

            # validation login
            if yaml_reader.reader()['dashboard_url'] in driver.current_url:
                print("SUCCESS: Login successful")
            else:
                print("FAIL: Login failure")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

        finally:
            driver.quit()
