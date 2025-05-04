"""
Bank Account - OOPS

BaseClass - 
BankAccount

Attributes - account_number, balance

Methods - deposit() , withdraw()

Subclasses - 
SavingsAccount

Attributes - interest_rate

Methods - calculate_interest()

"""

# create base class 
class BankAccount:

    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.__balance = balance

    # passing amount to deposit
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount # self.balance = self.balance - amount

    def get_balance(self):
        return self.__balance

# using inheritance, inherit attributes and methods from parent class to child class
class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate


    def calculate_interest(self):
        # total balance * interest rate / 100
        return self.get_balance() * self.interest_rate / 100
    
# create an object
myaccount = SavingsAccount(456, 50000, 5)
print(myaccount.calculate_interest())