"""
Working with AJAX Forms Page
https://testpages.eviltester.com/styled/basic-ajax-test.html

Automation Flow
1. Open the page
2. Select a category to update the languages asynchronously
3. Fetch all the category with its languages
4. Print in the console
"""

# import all the necessary dependencies
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException


class Locators:
    category_locator = 'combo1' # ID
    ajax_loader_locator = '//span[@style="display: block;"]' # XPATH
    language_locator = 'combo2' # ID

class Data:
    url = "https://testpages.eviltester.com/styled/basic-ajax-test.html"

class AJAXForms(Locators, Data):

    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # created wait object
        self.wait = WebDriverWait(self.driver, 15)

    def form_handling(self):
        try:
            # launching the website
            self.driver.get(Data.url)
            self.driver.maximize_window()

            # creating select object
            initial_select = Select(self.driver.find_element(by=By.ID, value=Locators.category_locator))

            # create a categories list to select all
            categories = ["Web", "Desktop", "Server"]

            # iterate all the categories and select the languages
            for category in categories:
                category_element = self.driver.find_element(by=By.ID, value=Locators.category_locator)
                Select(category_element).select_by_visible_text(category)

                # fetch the languages after its loaded asynchronously
                self.wait.until(EC.invisibility_of_element_located((By.XPATH, '//span[@style="display: block;"]')))

                # wait for language to be present in the page
                self.wait.until(EC.presence_of_all_elements_located((By.XPATH, '//select[@id="combo2"]/option')))

                # find the language element and fetch all the options
                language_element = self.driver.find_element(by=By.ID, value=Locators.language_locator)

                # use list comprehension
                languages = [option.text for option in Select(language_element).options]

                # without list comprehension
                # languages = []
                # for option in Select(language_element).options:
                #     languages.append(option.text)

                print(f"Category: {category}")
                for language in languages:
                    print(f"Language: {language}")
                print("-------------------------")

            self.driver.quit()

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: ", error)

if __name__ == "__main__":
    myAJAX = AJAXForms()
    myAJAX.form_handling()


