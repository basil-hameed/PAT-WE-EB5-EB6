import pytest
from home_page import HomePage

myautomation = HomePage()

class TestDemo:

    def test_title(self):
        actual_title = myautomation.fetch_page_title() 
        expected_title = "STORE"
        assert actual_title == expected_title

    def test_url(self):
        actual_url = myautomation.fetch_page_url()
        expected_url = "https://demoblaze.com/index.html"

    def test_page_content(self):
        myautomation.fetch_page_content()

