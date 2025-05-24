from selenium.webdriver.common.by import By

class Locators:
    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")
    inventory = (By.CLASS_NAME, "inventory_list") # validating all products displayed