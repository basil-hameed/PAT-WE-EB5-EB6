from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False) # launches nightly version
    page = browser.new_page()
    page.goto("https://www.guvi.in")
    print(page.title())
    browser.close()
