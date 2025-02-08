"""
Restaurant System
The user can access the menu item and price
but not the profit 

The buyer adds the menu item, price and profit

"""

# Base class
class MenuItem:
    def __init__(self, name, price, profit):
        self.name = name # public attribute
        self.price = price # public attribute
        self.__profit = profit  # private attribute


# Child Class or Derived Class
class SpecialMenuItem(MenuItem):
    def __init__(self, name, price, profit, special):
        super().__init__(name, price, profit)
        self.special = special

    def display_item(self):
        try:
            return f"Name :{self.name}, Price : {self.price}"
        except ValueError:
            return f"Error : Value Error occured in display item"
