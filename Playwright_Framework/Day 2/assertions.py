"""
Using playwright assertions

Open the browser
Navigate to https://www.saucedemo.com/
Validate the page title
Check username field is present
Fill user name and password
Validate that username and password added in the page
Click login button
Validate the current url
Validate any product whether it is visible on the page
Check the total count of products
Close the browser

Assertions:
1. Asserting the page title
2. Assert if username field is present
3. Assert if username and password added
4. Assert the current url
5. Assert the product is visible
6. Assert the total count of products
"""

# import playwright
from playwright.sync_api import sync_playwright
from playwright.sync_api import expect # used for assertions

def assertion_demo():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Navigate to sauce demo website
        page.goto("https://www.saucedemo.com/")

        # Assertion 1 - Validating the page title
        expect(page).to_have_title("Swag Labs")

        # Assertion 2 - Check username field is present
        username_field = page.locator("#user-name")
        expect(username_field).to_be_visible()

        # Fill username and password
        page.fill('#user-name', "standard_user")
        page.fill('#password', "secret_sauce")

        # Assertion 3 - Validate username and password added
        expect(username_field).to_have_value("standard_user")

        password_field = page.locator('#password')
        expect(password_field).to_have_value("secret_sauce")

        # Click login button
        page.click("#login-button")

        # Assertion 4 - Validate the url after login
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

        # Assertion 5 - Check the product is visible
        product = page.locator("//div[contains(text(), 'Sauce Labs Backpack')]")
        expect(product).to_be_visible()

        # Assertion 6 - Validate the total count of products
        products = page.locator(".inventory_item_name ")
        expect(products).to_have_count(7)

        print("All assertions passed successfully!")

        # close the browser
        browser.close()


if __name__ == "__main__":
    assertion_demo()



