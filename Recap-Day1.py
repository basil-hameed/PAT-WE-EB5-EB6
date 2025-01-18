# print("Hello World")

# Single Line Comment
# print("My Dear Learners!")

# Write a program to print Python
# Using print() function
# print("Python") # using print() function

"""
Recap Session Going on..


"""

'''
Multi Line Comments
'''

# Python Variables

# name = "Python"
# print(name)

# name1 = "Peter"
# print(name)

# print(name1)

"""
String Data Type - str
"""
# print('hello')
# print("hello")
# print('3.5')


# Assign string to a variable
# name = "Hari"
# print(name)

# String Length
# a = "Hello Guyz" # String
# total_length = len(a) # Int
# print(total_length)

# print(type(total_length))

# Check String
# mystring = "Work smarter until your expectations become reality"
# print("Work" in mystring)

# Slicing Strings
mystring = "Work smarter until your expectations become reality"

# Slicing using index values
# Use Start Index and End Index
# print(mystring[2:8]) 
# rk sma

# print(mystring[5:12])
# print(mystring[-7:])
# print(mystring[2:655])


# Modify Strings
c = "Python World Hello"
# print(c)
# print(c.strip())
# print(c.replace(" ", ""))
# print(c)

# print(c.split(" "))

# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
# print(c)


x = "5"
y = "6"
z = x + y
# print(z)


# Format Strings (f-strings)

name = "Elon Musk" 
age = 36
mycombinedtext = f"My name is {name}, I am {age} years old"
# print(mycombinedtext)

brand = "LG"
value = 25000
mytext = f"My brand is {brand}, and the price is {value}"
# print(mytext)

# Type Conversion or Type Casting
x = 1
y = 2.8
z = "5"

# print(type(x))
# print(type(y))
# print(type(z))

# type casting int to float
a = float(x)
# print(type(a))

# type float to int
b = int(y)
# print(type(b))

# type casting string to int
c = int(z)
# print(type(c))


# Operator Types

# Arithmetic Operators
"""
Addition "+" x + y 
Subtraction "-" x - y
Multiplication "*" x * y
Division "/" x/y
Modulus "%" x%y
Exponentiation "**" 2**4 or 5**2
Floor Division "//" x // y
"""
x = 5
y = 2

# print("Addition: ", x + y) 
# print("Subtraction: ", x - y)
# print("Multiplication: ", x * y)
# print("Division: ", x / y)
# print("Modulus: ", x % y) # Remainder
# print("Exponentiation: ", x ** y) # Power of
# print("Floor Division: ", x // y)

# Assignment Operator

x = 5
# x = x + 3
x //= 3
# print(x)

# Comparison Operator

"""
== Equal x == y
!= Not Equal x != y
< Less than x < y
> Greater than x > y
<= Less than or equal to
>= Greater than or equal to
"""
x = 5
y = 2

# print(x == y)
# print(x != y)

# Logical Operators

"""
and - True if both statments are true
or - True if one of the statements is true
not - Reverse the result returns false if both are true

"""

x = 5

# print(not (x > 2 and x < 10))
# False

# Identity Operators

# is  - True if both the things are same
x = 8
y = 8
# print(x is y)
# True

# is not
x = 8
y = 5
# print(x is not y)
# True

# Membership Operator

"""

in - True if that sequence inside that string
not in - True if that sequence is not in that string
"""

mytxt = "Hi, Learners"
# print("Hi" in mytxt)

# print("Hello" not in mytxt)

# Conditional Statements
raining = False

# if raining:
#     print("Take Umbrella")
# else:
#     print("Dont take Umbrella")

age = 0

# if age > 18:
#     print("Allow them to vote")
# elif age == 0:
#     print("Age is invalid")
# else:
#     print("Dont allow them to vote")

# brand = "Sony"
# price = 32.5

# if brand == "LG":
#     print("Price is", price)
# else:
#     print("Invalid brand")

# mytexts = "Hello, I'm Python"

# if "Hello1" in mytexts:
#     print("Yes, Hello is present in string")
# elif "Python1" in mytexts:
#     print("Yes, Python is present in string")
# elif "hello" not in mytexts:
#     print("hello not in my string")
# else:
#     print("No, Its not present")


# Loops

# For Loops
fruits = ["apple", "banana", "mango"]

# for x in fruits:
#     print(x) # x = "apple", x = "banana" x = "mango"

# name = "banana"
# for i in name:
#     print(i)

mytoys = ["car", "bike", "ball", "remote car", "fan", "duck"]

# for y in mytoys:
#     print(y)

# break statement
# for toys in mytoys:
#     if toys == "fan":
#         continue
#     print(toys)

for toys in mytoys:
    pass

# mynumbers = [2, 8, 5, 6, 8, 9, 10, 25]

# for i in mynumbers:
#     if i == 8:
#         continue
#     print(i)

# Range 

# for i in range(1, 6):
#     print(i)

# 1, 2, 3, 4, 5

# Nested Loops

prop = ["red", "bigger", "tasty"]
fruits = ["apple", "banana", "cherry"]


# for x in prop:
#     for y in fruits:
#         if x + " " + y == "bigger cherry":
#             continue
#         print(x, y)

# While Loops

i = 0
# while i < 6:
#     print(i)
#     i += 1

i = 0

# while i < 10:
#     i += 1
#     if i == 7:
#         continue
#     print(i)

# Get input from user

# user_input = int(input())

# if user_input > 30:
#     print("Num is greater than 30")
# elif user_input < 30:
#     print("Num is lesser than 30")
# else:
#     print("No num")

# Number guessing game

import random

num_to_guess = random.randint(1, 50)

while True:
    user_guess = int(input())

    if user_guess < num_to_guess:
        print("Too Low, Try again")
    elif user_guess > num_to_guess:
        print("Too High, Try again")
    else:
        print("Congrats, Correct guess")
        break

    
