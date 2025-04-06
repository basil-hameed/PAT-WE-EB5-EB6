import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PageObjects.DashboardPage import DashboardPage1
from TestData.data import OrangeHRMData


class TestDashboard:

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(OrangeHRMData.orange_url)
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()

    def test_title(self, booting_function):
        assert DashboardPage1.get_title(self) == "OrangeHRM"
        print("SUCCESS: Dashboard Title Validated")

    def test_url(self, booting_function):
        assert DashboardPage1.get_url(self) == "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
        print("SUCCESS: Dashboard URL Validated")