"""
Extract the dynamically updated world population
https://www.worldometers.info/world-population/

1. launch the website
2. fetch the current world population
3. fetch the total births today
4. print the results continuously in the console
"""

# import all necessary dependencies
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ERROR_URL

class Locators:
    pass

class Data:
    url = "https://www.worldometers.info/world-population/"

class WorldPopulation(Data, Locators):
    def __init__(self):
        # creating driver object
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 15)

    def start(self):
        try:
            self.driver.get(Data.url)
            self.driver.maximize_window()
            # self.driver.implicitly_wait(15)
            return True
        except ERROR_URL as error:
            print("Error launching page!", error)

    # fetch current world population
    def get_world_population(self):
        try:
            # create an empty list to store web elements
            total_population = []

            # using while loop for continuous iteration
            while True:
                # get total_population count web element
                total_population_count = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="col-span-3"]//span[@class="rts-counter"]')))

                # append the elements into list
                total_population.append(total_population_count)

                # Iterate to print the text present in the element
                for data in total_population:
                    print(f"Current World Population: {data.text}")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: Problem fetching the data!", error)

    # fetch the total births today
    def get_total_births_today(self):
        try:
            # create birth_today list to store the web element
            birth_today = []

            # using while loop for continuous iteration
            while True:
                # get total_birth_count_element
                total_birth_count = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Births today"]//parent::div//span[@class="rts-counter text-2xl font-bold"]')))
                # append the elements into list
                birth_today.append(total_birth_count)

                # Iterate to print the text present in the element
                for data in birth_today:
                    print(f"Today's Birth : {data.text}")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: Data not fetched", error)


if __name__ == "__main__":
    world_population = WorldPopulation()
    world_population.start()
    # call the method separately to print in console
    # world_population.get_world_population()
    world_population.get_total_births_today()
