"""
Use conftest.py to manage the webdriver setup and teardown

Centralizes webdriver setup and use this for all the test cases
"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# the driver_setup() function is common for all test cases
@pytest.fixture(scope="function")
def driver_setup():
    # setup webdriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()