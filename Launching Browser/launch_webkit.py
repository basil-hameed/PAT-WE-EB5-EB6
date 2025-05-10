from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.webkit.launch(headless=False) # lauching headed mode
    page = browser.new_page() # create new page

    page.goto("https://www.guvi.in") # launch guvi website
    print(page.title()) # get the page title
    browser.close() # closing browser