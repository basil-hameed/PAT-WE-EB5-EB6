"""
Test Case for Valid Login

1. Open the browser
2. Navigate to the url
3. Enter username
4. Enter password
5. Click login button
6. Validate the login successfull

"""

# import playwright
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import browser


def test_valid_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # navigate to url
        page.goto("https://www.saucedemo.com/")

        # enter username and password
        page.fill("#user-name", "standard_user")
        page.fill("#password", "secret_sauce")

        # click login button
        page.click("#login-button")

        # Assertion  - Validate the url after login
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")