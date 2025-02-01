def function_name(name):
        print("hello world")
        print(name)

my_name = "Sham"
# function_name(my_name)

# Lambda Syntax

# variable_name = lambda arguments : expression


"""
Print some text in the console/terminal
1. Normal Function
2. Lambda Function
"""

# normal function

def display_name(data):
    return data

# print(display_name("hello learners"))

# lambda function

result = lambda data : data

# print(result("hello learners"))

x = lambda a : a * 10
# print(x(25))

"""
1. Write a program to square a number
"""

def square_number(data):
      result = data * data
      return result

# print(square_number(5))


# lambda function

result = lambda data : data ** 2
# print(result(5))

"""
2. Write a program to add two numbers
"""

def add_numbers(num1, num2):
      result = num1 + num2
      return result

# print(add_numbers(2, 5))

add_two_numbers = lambda num_1, num_2 : num_1 + num_2
# print(add_two_numbers(2, 5))

"""
3. Write a program to count number of digits in a number
data = 123 ==> "123"
output = 3
"""

def count_digit(data):
      length = len(str(data))
      return length

# print(count_digit(123))


count_digits = lambda data : len(str(data))
# print(count_digits(123))


"""
4. Write a program to find the maximum of three numbers (max() function )
"""

def max_three_numbers(num1, num2, num3):
      return max(num1, num2, num3)

# print(max_three_numbers(200, 5987, 65))

result = lambda num1, num2, num3 : max(num1, num2, num3)
# print(result(200, 5987, 65))

"""
5. Write a program to check a given number is odd or even
# """

# def check_odd_even(num):
# rint(square_numbers(num_list))

# for num in num_list:
#       print(square_numbers(num))      if num % 2 == 0:
#             return "Even"
#       else:
#         return "Odd"
      
# print(check_odd_even(26))


result = lambda num : num % 2

# print(result(4))

# print(result(5))


# Map Function

"""
Write a program using map() to square a list of numbers
data = [20, 30, 40]
"""

def square_numbers(data):
      return data * data

num_list = [20, 30, 40]

# map function
lambda_function = lambda data : data * data

result1 = list(map(square_numbers, num_list))
# print(result1)

result2 = list(map(lambda_function, num_list))
# print(result2)

"""
2. Write a program using map() function convert all strings into upper case
"""

# my_data = "hello"
# print(my_data.upper())

data = ['peter', 'richard', 'paul', 'sham']

upper_case = lambda data : str.upper(data)

result = list(map(upper_case, data))
# print(result)


"""
3. Write a program to calculate the length of each word in a list

my_data = ["python", "mysql", "testing"]
output_list = [6, 5, 7]
"""
# input data
my_string_list = ["python", "mysql", "testing"]

# creating lambda function
length_my_data = lambda my_data : len(my_data)

# using map function and created result list
result = list(map(length_my_data,my_string_list))
# print(result)


def len_word(string1):
    return (len(string1))


string12 = ["python","sql","java","javascript"]
result12 = list(map(len_word,string12))
# print(result12)


# Filter Function

"""
1. Write a program to filter the odd numbers from a list
"""

my_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# normal function to filter the numbers
def even_numbers(my_numbers_list):
      result = []

      for num in my_numbers_list: # 1, 2, 3, 4
            if num % 2 == 0:
                  result.append(num)
      return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(even_numbers(my_list))

# lambda function
lambda_func = lambda num : num % 2 == 0
result = list(filter(lambda_func, my_list))
# print(result)

"""
2. Write a program using filter() to filter out all negative numbers from a list
"""

my_num_list = [1, 23, 5, -98, -28, 52, 36]

filter_negative_nums = lambda data : data > 0

result = list(filter(filter_negative_nums, my_num_list))
# print(result)


# Reduce() function

from functools import reduce

numbers = [1, 2, 3, 4]

# type 1
my_reduce = lambda x, y : x + y

"""
Reduce function

num = [1, 2, 3, 4]
1, 2, = 3
3, 3 = 6
6, 4 = 10
"""

result = reduce(my_reduce, numbers)
# print(result)

# type 2 with an initializer

result = reduce(my_reduce, numbers, 10)

"""
10, 1 = 11
11, 2 = 13
13, 3 = 16
16, 4 = 20
"""
# print(result) 



# Iterator
data = [10, 20, 30, 40]

# iterating inside the items
# for num in data:
    # print(num)

# using iterator method
my_iterator = iter(data)
# print(my_iterator)

# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))
# print(next(my_iterator))


# tuple object 

my_tuple = ("apple", "mango", "cherry")

tuple_iterator = iter(my_tuple)
# print(tuple_iterator)

# print(next(tuple_iterator))
# print(next(tuple_iterator))
# print(next(tuple_iterator))


"""
Create an iterator that returns numbers starting with 1 , and 
each sequence will increase one by one
"""

class MyNumbers:
      def __iter__(self):
            self.a = 1
            return self
      
      def __next__(self):
            x = self.a
            self.a = self.a + 1
            return x
      
myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# Python Generators

# def my_generator(number):
#       result = 0
#       while result < number:
#             yield result
#             result = result + 1

# print(my_generator(5))

# using for loop for printing values
# for i in my_generator(200):
    #   print(i)

    
"""
1. Write a program to yield square of numbers

"""

# def square_numbers(num):
#       n = 1
#       while n < num:
#             yield n ** 2
#             n += 1

# for data in square_numbers(15):
#       print(data)

"""
2. Write a program to yield reverse of a string
"""

# def reverse_string(data):
#       for index in range(len(data)-1, -1, -1):
#             yield data[index]

# for data in reverse_string("guvigeeksnetwork"):
    #   print(data)


# Decorators

# def my_decorator(func):
#     def wrapper():
#           print("Something is happening before the function!")
#           func()
#           print("Something is happening after the function!")
#     return wrapper

# type 1
# @my_decorator
# def say_hello():
#       print("hello")

# say_hello()

# # type 2
# decorated_func = my_decorator(say_hello)
# decorated_func()

# output
# Something is happening before the function!
# hello
# Something is happening after the function!



# Regex - Regular Expressions

import re

"""
First 5 are Capital letters
Next 4 chars are numbers 
Last one is a Capital letter
"""
def validate_pancard(pancard_no):
      pattern = r"^[A-Z]{5}[0-9]{4}[A-Z]{1}$"

      if re.match(pattern, pancard_no):
            return True
      else:
            return False

# print(validate_pancard("BAJPC4350M2"))

def validate_random(data): #python32
      pattern = r"^[a-z]{6}[0-9]{2}$"

      if re.match(pattern, data):
            return True
      else:
            return False
# print(validate_random("python32"))

def validate_email_id(data):
      pattern = r"^[a-z0-9_.]+@[a-z0-9]+\.[a-z]{2,6}"

      if re.match(pattern, data):
            return True
      else:
            return False

print(validate_email_id("demo@gmail.com"))
