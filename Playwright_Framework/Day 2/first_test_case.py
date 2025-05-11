"""
Open a browser
Navigate to the website “https://www.guvi.in”
Verify the website title
Close the browser
"""

# import necessary playwright dependencies
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect

def test_first_case():
    with sync_playwright() as p: # p for playwright object
        # launch the chromium instance
        browser = p.chromium.launch(headless=False)

        # create a new page
        page = browser.new_page()

        # navigate to the website
        page.goto("https://www.guvi.in")

        # get page title
        page_title = page.title()

        # print in the console
        print(page_title)

        # add assertion through expect
        expect(page).to_have_title("GUVI | Learn to code in your native language")