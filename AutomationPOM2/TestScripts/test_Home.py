import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.HomePage import HomePage1
from TestData.data import OrangeHRMData


class TestHome:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(OrangeHRMData.orange_url)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()


    def test_login(self, booting_function):
        assert HomePage1.login(self) == True
        print("SUCCESS: Logged In (Positive)")

    def test_invalid_login(self, booting_function):
        assert HomePage1.invalid_login(self) == True
        print("SUCCESS: Not Logged In (Negative)")

