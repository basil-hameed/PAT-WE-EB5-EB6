# OOP's

# To create a class, use the keyword class

class MyClass: # StudentName,  TotalCount
    student_name = "Richard"
    total_count = 35

# Create an object 
student = MyClass()
# print(student.student_name)
# print(student.total_count)

# create a class person with parameters name and age

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet_person(self):
        print(f"Hello, My name is {self.name} and my age is {self.age}")

person1 = Person("John", 25)
# print(person1.name)   
# print(person1.age)
# person1.greet_person()

# another person
person2 = Person("Ravi", 22)
# print(person2.name) 
# print(person2.age)  
# person2.greet_person()


# Instance Method

class Student:
    def __init__(self, name):
        self.name = name
        
    # instance method
    def greet(self):
        return f"Hello, {self.name}"
    
my_student = Student("Alice")
# print(my_student.greet()) # calls the instance method

# Class Method

class MyClass:
    count = 0

    def __init__(self, name):
        self.name = name
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count
    
object1 = MyClass("Alice")
# object1.get_count()
# print(MyClass.get_count()) # calling the class method


# Static Method
class MyClass:

    @staticmethod
    def greet(message):
        return f"Message: {message}"
    
# print(MyClass.greet("Hello World!"))

# Overloading addition operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # overloading the + operator
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# point1 = Point(1, 2)
# point2 = Point(3, 4)
# result = point1 + point2
# print(result)

# Overloading multiplication operator

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # overloading the + operator
    def __mul__(self, other):
        return Point(self.x * other.x, self.y * other.y)
    
    def __repr__(self):
        return f"Point({self.x}, {self.y})"


# point1 = Point(1, 2)
# point2 = Point(3, 4)
# result = point1 * point2
# print(result)

# Python Inheritance

# Parent Class
class Person: 
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)       

# Child class
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.gradyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, self.gradyear)

student1 = Student("Mike", "Thomson", 2025)
# student1.welcome()

# Multiple Inheritance

class Calculation1:
    def summation(self, a, b):
        return a + b
    
class Calculation2:
    def multiplication(self, a, b):
        return a * b

class Derived(Calculation1, Calculation2):
    def divide(self, a, b):
        return a/b

my_object = Derived()
# print(my_object.summation(10, 20))
# print(my_object.multiplication(10, 20))
# print(my_object.divide(10, 20))


# Polymorphism

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring")
plane1 = Plane("Boeing", "747")

# car1.move()

# for x in (car1, boat1, plane1):
#     x.move()

"""
Drive
Sail
Fly
"""

# Encapsulation

class Base:
    def __init__(self):
        self._a = 5 # protected member

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        print("Calling protected member of base class :", self._a)

        self._a = 10
        print("Calling modified protected member outside base class :", self._a)

# x = Derived()


# Private member

class Base:
    def __init__(self):
        self._a = 5 # protected member
        self.__b = 8 # private member

class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        # print("Calling protected member of base class :", self._a)
        print("Calling private member of base class :", self.__b)

# x = Derived()

# Abstraction

from abc import ABC

class Polygon(ABC):

    #abstract method
    def sides(self):
        pass # dont have any body

class Triangle(Polygon):
    def sides(self):
        print("Triangle has 3 sides")

class Pentagon(Polygon):
    def sides(self):
        print("Pentagon has 5 sides")

my_traingle = Triangle()
# my_traingle.sides()

my_pentagon = Pentagon()
# my_pentagon.sides()

# Triangle has 3 sides
# Triangle has 3 sides

# Mini Project

"""
Calculate the ride fare based on the type of ride and distance
Inheritance and Polymorphism
Type - Regular Ride (50 + (additional distance * 10)) and Premium Ride (100 + add dist * 20)

"""
# Base Class
class Ride:
    def __init__(self, distance, base_fare):
        self.distance = distance
        self.base_fare = base_fare

    def calculate_fare(self):
        return self.base_fare + (self.distance * 10)
    
# sub class
class RegularRide(Ride):
    def __init__(self, distance, base_fare):
        super().__init__(distance, base_fare)

    def calculate_fare(self):
        return self.base_fare + (self.distance * 10)
    
# subclass
class PremiumRide(Ride):
    def __init__(self, distance, base_fare):
        super().__init__(distance, base_fare)

    def calculate_fare(self):
        return self.base_fare + (self.distance * 20)
    
regular_ride = RegularRide(10, 50)
premium_ride = PremiumRide(10, 80)

# print(regular_ride.calculate_fare())
# print(premium_ride.calculate_fare())


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
        print(f"Name :{self.name}, Price : {self.price}")

    
# seller adding some menu item
item = SpecialMenuItem("Pasta", 300, 20, "Vegan")


# user access
print(f"Menu Item Name: {item.name}")
print(f"Price: {item.price}")
# print(f"Profit: {item.__profit}")

item.display_item()

        
