"""
Explain handling waits using demo TODO MVC app

1. wait_for_selector()
2. wait_for_timeout()
3. wait_until
"""

# import the playwright
from playwright.sync_api import sync_playwright

def handle_wait():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Navigate to the website
        page.goto("https://demo.playwright.dev/todomvc")

        # Example 1 - wait_for_selector
        # wait until the element appears on the page
        page.wait_for_selector("h1")
        print("Element is visible")


        # Example 2 - Using wait for timeout()
        page.wait_for_timeout(3000) # 3000 for 3 seconds
        print("Waited for 3 seconds")


        # Example 3 - Using wait_until
        page.goto("https://demo.playwright.dev/todomvc", wait_until="domcontentloaded")
        print("DOM Content Loaded Successfully")


        # Example 4 - Using locator and wait_for
        web_element = page.locator("text=This is just a demo of TodoMVC for testing, not the ")
        web_element.wait_for(timeout=5000)
        print("Text 'This is just a demo of TodoMVC for testing, not the ' is present!")

if __name__ == "__main__":
    handle_wait()