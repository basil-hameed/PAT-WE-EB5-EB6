
## Python Program

```python
import random

choices = ['rock', 'paper', 'scissors']
computer_choice = random.choice(choices)
player_choice = input().lower()

if player_choice not in choices:
    print("Invalid choice!")
elif player_choice == computer_choice:
    print("It's a tie! Both chose", player_choice)
elif (player_choice == 'rock' and computer_choice == 'scissors') or \
     (player_choice == 'paper' and computer_choice == 'rock') or \
     (player_choice == 'scissors' and computer_choice == 'paper'):
    print("You win! Computer chose", computer_choice)
else:
    print("You lose! Computer chose", computer_choice)


#Guessing Number Game

import random

num_guess = random.randint(1,20) 


while True:
    user_guess = int(input())

    if user_guess < num_guess:
        print("Too Low, Try Again")
    elif user_guess > num_guess:
        print("Too High, Try Again")
    else:
        print("Congrats, You found correct Number")
        break
```

## 1. Split List into Even and Odd Numbers
**Problem**: Given a list, split it into two lists: one with even numbers and another with odd numbers.

```python
numbers = [12, 43, 65, 32, 88, 91, 40]
even = [x for x in numbers if x % 2 == 0]
odd = [x for x in numbers if x % 2 != 0]
print("Even Numbers:", even)
print("Odd Numbers:", odd)
```

---

## 2. Extract Prime Numbers from List
**Problem**: Count and extract all prime numbers from the list.

```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [12, 43, 65, 32, 88, 91, 40]
primes = [x for x in numbers if is_prime(x)]
print("Prime Numbers:", primes)
```

---

## 3. Find Happy Numbers in List
**Problem**: Find how many numbers are happy numbers.

```python
def is_happy(n):
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d)**2 for d in str(n))
    return n == 1

numbers = [10, 7, 13, 19, 28, 100, 111]
happy = [x for x in numbers if is_happy(x)]
print("Happy Numbers:", happy)
```

---

## 4. Sum of First and Last Digit
**Problem**: Write a Python program to find the sum of the first and last digit of an integer.

```python
def sum_first_last(n):
    n = str(n)
    return int(n[0]) + int(n[-1])

number = 12345
print("Sum of First and Last Digit:", sum_first_last(number))
```

---

## 5. Coin Change Problem for Rs.10
**Problem**: Find all ways to make Rs. 10 using Rs.1, Rs.2, Rs.5, and Rs.10 coins.

```python
for i in range(11):
    for j in range(6):
        for k in range(3):
            for l in range(2):
                if i*1 + j*2 + k*5 + l*10 == 10:
                    print(f"1Rs: {i}, 2Rs: {j}, 5Rs: {k}, 10Rs: {l}")
```

---

## 6. Find Duplicates in Three Lists
**Problem**: Find common elements (duplicates) in three lists.

```python
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6]
list3 = [5, 6, 7, 8]

duplicates = list(set(list1) & set(list2) & set(list3))
print("Common Elements:", duplicates)
```

---

## 7. First Non-Repeating Element
**Problem**: Find the first non-repeating element in a list.

```python
nums = [4, 5, 1, 2, 0, 4, 5, 2]
for num in nums:
    if nums.count(num) == 1:
        print("First Non-Repeating Element:", num)
        break
```

---

## 8. Minimum Element in Sorted & Rotated List
**Problem**: Find the minimum element in a sorted and rotated list.

```python
def find_min(lst):
    low, high = 0, len(lst) - 1
    while low < high:
        mid = (low + high) // 2
        if lst[mid] > lst[high]:
            low = mid + 1
        else:
            high = mid
    return lst[low]

rotated = [30, 40, 50, 10, 20]
print("Minimum Element:", find_min(rotated))
```

---

## 9. Triplet Sum Problem
**Problem**: Find triplet in list whose sum equals a given value.

```python
arr = [10, 20, 30, 9]
target = 59
found = False
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        for k in range(j+1, len(arr)):
            if arr[i] + arr[j] + arr[k] == target:
                print("Triplet Found:", arr[i], arr[j], arr[k])
                found = True
if not found:
    print("No such triplet found")
```

---

## 10. Sub-list with Zero Sum
**Problem**: Check if there is a sub-list with sum equal to zero.

```python
def has_zero_sum_sublist(arr):
    seen = set()
    total = 0
    for num in arr:
        total += num
        if total == 0 or total in seen:
            return True
        seen.add(total)
    return False

lst = [4, 2, -3, 1, 6]
print("Sub-list with Zero Sum Exists:", has_zero_sum_sublist(lst))
```

---


### **1. Filter People Aged 18 or Older and Map Names**

```python
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 19}
]

adults = list(filter(lambda person: person['age'] >= 18, people))
names = list(map(lambda person: person['name'], adults))
print("Names of adults:", names)
```

---

### **2. Use `reduce` and Lambda to Calculate Product**

```python
from functools import reduce

numbers = [2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print("Product of numbers:", product)
```

---

### **3. List Comprehension with Lambda for Squares of Even Numbers**

```python
nums = [1, 2, 3, 4, 5, 6]
squares = [x**2 for x in nums if (lambda n: n % 2 == 0)(x)]
print("Squares of even numbers:", squares)
```

---

### **4. Lambda to Check if String is a Number**

```python
is_number = lambda s: s.isdigit()
print(is_number("1234"))  # True
print(is_number("12.34")) # False (because '.' is not digit)
```

*To allow decimal numbers too:*

```python
is_number = lambda s: s.replace('.', '', 1).isdigit() and s.count('.') <= 1
```

---

### **5. Extract Year, Month, Day from `datetime`**

```python
from datetime import datetime

dt = datetime.datetime.now()
get_parts = lambda d: (d.year, d.month, d.day)
print("Date parts:", get_parts(dt))
```

---

### **6. Lambda to Generate Fibonacci Series up to n Terms**

```python
fib = lambda n: [0, 1][:n] + [sum(x) for x in zip(
    [0, 1][:n], [0, 1][:n][1:])] if n > 2 else [0, 1][:n]

# A more complete approach:
fibonacci = lambda n: [0, 1] + [0]*(n-2) if n > 1 else [0][:n]
fibonacci_series = lambda n: fibonacci(n) if n <= 2 else [
    0, 1] + [reduce(lambda acc, _: acc + [acc[-1] + acc[-2]], range(n - 2), [0, 1])[2:]][0]

print("Fibonacci series (6 terms):", fibonacci_series(6))
```

---

## OOP's Basics

```python
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance  # encapsulated

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return self.get_balance() * self.interest_rate / 100

class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, min_balance):
        super().__init__(account_number, balance)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.min_balance:
            super().withdraw(amount)
        else:
            print("Cannot withdraw beyond minimum balance")


# Employee Management
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        return self.salary

class RegularEmployee(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.salary + self.bonus

class ContractEmployee(Employee):
    def __init__(self, name, hourly_rate, hours_worked):
        super().__init__(name, 0)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked

class Manager(Employee):
    def __init__(self, name, salary, incentives):
        super().__init__(name, salary)
        self.incentives = incentives

    def calculate_salary(self):
        return self.salary + self.incentives


# Vehicle Rental
class Vehicle:
    def __init__(self, model, rental_rate):
        self.model = model
        self.rental_rate = rental_rate

    def calculate_rental(self, days):
        return self.rental_rate * days

class Car(Vehicle):
    def __init__(self, model, rental_rate, ac_charge):
        super().__init__(model, rental_rate)
        self.ac_charge = ac_charge

    def calculate_rental(self, days):
        return (self.rental_rate + self.ac_charge) * days

class Bike(Vehicle):
    def __init__(self, model, rental_rate):
        super().__init__(model, rental_rate)

class Truck(Vehicle):
    def __init__(self, model, rental_rate, load_charge):
        super().__init__(model, rental_rate)
        self.load_charge = load_charge

    def calculate_rental(self, days):
        return (self.rental_rate + self.load_charge) * days
```


Selenium with Pytest 
---

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class PytestIntegr:

  def __init__(self):
    # Create a instance of the Chromedriver
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    self.driver.maximize_window()
    # time delay
    time.sleep(3)

  def perform_login(self):
    # Navigate given URL
    self.driver.get('https://www.saucedemo.com/')
    
    # Find username and password and login
    self.driver.find_element(By.ID, 'user-name').send_keys('standard_user')
    self.driver.find_element(By.ID, 'password').send_keys('secret_sauce')
    self.driver.find_element(By.ID, 'login-button').click()

    # time delay
    time.sleep(3)

 def get_title(self):
    # Get the title of webpage
    title = driver.title
    print(f'Title of the webpage: {title}')

 def get_url(self):
    # Get current URL of the webpage
    current_url = driver.current_url
    print(f'Current URL of the webpage: {current_url}')

def fetch_page_content(self):
    # Extract entire contents of webpage and save to a text file
    webpage_content = driver.page_source
    
    with open('webpage_task_11.txt', 'w') as file:
        file.write(webpage_content)
    
    # time delay
    time.sleep(4)
    
    print("Webpage content saved as text file successfully")

  def close_browser(self)
    # Close browser window
    self.driver.close()

myautom = PytestIntegr()
myautom.perform_login()
myautom.get_title()
myautom.get_url()
myautom.fetch_page_content()
myautom.close_browser()
```


Exceptions and Action Chains
---

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

 
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/droppable/")

frame_element = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")

driver.switch_to.frame(frame_element)
sleep(2)

#select the ID and XPATH,CSS selectors 
drag_elem=driver.find_element(By.ID,"draggable")
sleep(2)

drop_elem=driver.find_element(By.ID, "droppable")
sleep(2)

ActionChains(driver).drag_and_drop(drag_elem, drop_elem).perform()
sleep(4)

print('Drag and Drop Performed')
 
```


## Data Driven & Keyword Driven Testing Framework
---
```python
TestScripts/test_login
class TestDDTF:
    def test_login_excel(self):
        # binding the file path and sheet number
        self.excel_file = Data.excel_file
        self.sheet_number = Data.sheet_number

        # create excel object passing the file and sheet number
        self.excel = Excel_Function(self.excel_file, self.sheet_number)

        # Initialize Driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # launch the browser and maximize window
        self.driver.get(Data.url)
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(10)

        # get the total row values
        self.rows = self.excel.row_count()

        # using for loop to iterate row by row values
        for row in range(2, self.rows + 1):
            username = self.excel.read_data(row, 5)
            password = self.excel.read_data(row, 6)

            # enter the username read from the excel file
            self.driver.find_element(by=By.NAME, value=Locators.username_locator).send_keys(username)

            # enter the password read from the excel file
            self.driver.find_element(by=By.NAME, value=Locators.password_locator).send_keys(password)

            # click the login button
            login_click = self.wait.until(EC.element_to_be_clickable((By.XPATH,Locators.login_button_locator)))
            login_click.click()

            # Main validation logic of login testing (PASS/FAIL)
            if Data.dashboard_url in self.driver.current_url:
                print("SUCCESS: Login successful")
                self.excel.write_data(row, 7, "TEST PASS")
                self.driver.find_element(by=By.XPATH,value=Locators.drop_down_selector).click()
                self.driver.find_element(by=By.XPATH,value=Locators.logout).click()


            elif Data.url in self.driver.current_url:
                print("FAIL: Login failed")
                self.excel.write_data(row, 7, "TEST FAIL")
                self.driver.refresh()

        self.driver.quit()

```

AJAX Dynamic Elements
---

```python
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ERROR_URL


class Data:
    url = "https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"

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
                total_population_count = self.wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="counter-ticker is-size-2-mobile"]')))

                # append the elements into list
                total_population.append(total_population_count)

                # Iterate to print the text present in the element
                for data in total_population:
                    print(f"Current World Population: {data.text}")

        except (NoSuchElementException, ElementNotVisibleException) as error:
            print("ERROR: Problem fetching the data!", error)



if __name__ == "__main__":
    world_population = WorldPopulation()
    world_population.start()
    world_population.get_world_population()
```

---
