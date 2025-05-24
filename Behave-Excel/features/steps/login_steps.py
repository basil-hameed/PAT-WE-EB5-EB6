from behave import given, when, then
from utils.excel_utils import ExcelUtil
from pages.login_page import LoginPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

@given("the Excel file is loaded")
def step_impl(context):
    # creating webdriver by passing webdriver manager
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    # navigating to the url
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    # creating excel object by passing the path & sheet name
    context.excel = ExcelUtil("D:\\Automation\\PAT-EB-6\\Behave-Excel\\data\\test_data.xlsx", "Sheet1")
    # creating login page object by passing the driver
    context.login_page = LoginPage(context.driver)


@when("I try to login with all data sets")
def step_impl(context):
    for i in range(2, context.excel.row_count() + 1):
        username = context.excel.read_data(i, 1)
        password = context.excel.read_data(i, 2)
        context.login_page.login(username, password)

        if context.login_page.is_login_successful():
            context.excel.write_data(i, 3, "Pass")
            context.driver.back()
        else:
            context.excel.write_data(i, 3, "Fail")
            context.driver.refresh()

@then("the login results are updated")
def step_impl(context):
    context.driver.quit()





