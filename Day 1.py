# This is a single line comment
# print("My Dear Python Learners!")


"""
Hi
This
is 
a 
multiline
comments
"""

'''
Hi
I
am
also 
a
multiline
comment
'''

# Creating a variable

# name = "Python"
# country = "India"

# print(type(country))
# print(name)

# Get the string length (includes space)
name = "Hello World"
# print(len(name))


b = "intro to python"
# whats the length?
# print(len(b))

# Slicing Strings
c = "Hello World!"
# print(c[2:8])

# print(c[6:11])
# World

# print(c[0:6])
# Hello

# print(c[4:])

# print(c[-5:-2])

# c = "Hello World!"

# total_length = len(c)

# print(c[total_length - 1])
# print(c[-1])

# upper() method modifies the string into upper case
a = "Hello World"
# print(a.upper())


# lower() method modifies the string into lower case
a = "Hello World"
# print(a.lower())

# strip() method removes any white spaces before and after the string
a = "      Hello, World "
# print(a.strip())

# replace() method replaces a string
a = "Hello"
# print(a.replace("H", "J"))


name = "peter"
age = 36
txt = f"My name is {name}, my age is {age}"
# print(age)
# print(txt)

"""
I am learning Python, in the year 2025
"""
name = "Python"
year = "2025"

txt = f"I am learning {name}, in the year {year}"
# print(name + year)


height = 5.6
# print(type(height))
# <class 'float'>

my_complex = 5j
# print(type(my_complex))
# <class 'complex'>

height = 5.6
# print(type(height))
integer_height = int(height)
# print(type(integer_height))

num = 42
my_float = float(num)
# print(type(my_float))


my_fruits_list = ["apple", "banana", "mango"]
my_random_list = ["python", 2025, 25.5, -5.3]

# print(my_fruits_list[-1])


# modify the items, convert banana to orange
my_fruits_list[1] = "orange"

my_fruits_list[2] = "strawberry" # positive index
my_fruits_list[-1] = "strawberry" # negative index
# print(my_fruits_list)
# apple orange strawberry


my_fruits_list = ["apple", "banana", "mango", "apple", "mango", "mango"]

# using pop() method to remove the last item
# print(len(my_fruits_list))
# my_fruits_list.pop()

# using pop with index to remove the exact item
# my_fruits_list.pop(2)

# using remove() method to remove the mentioned item
# my_fruits_list.remove("apple")
#
# print(my_fruits_list)
# ['banana', 'apple', 'mango']

# my_fruits_list.clear()
# print(my_fruits_list)

# my_tuples = ("apple", "banana", "mango", "apple")
# print(my_tuples)

# # my_tuples[0] = "orange"
# # print(my_tuples)

# """
# Traceback (most recent call last):
#   File "d:\Automation\PAT-EB-6\demo.py", line 150, in <module>
#     my_tuples[0] = "orange"
#     ~~~~~~~~~^^^
# TypeError: 'tuple' object does not support item assignment

# """

# # change tuple to list
# my_list = list(my_tuples)

# # make modifications
# my_list[0] = "orange"

# # change list to tuple
# my_tuples = tuple(my_list)
# print(my_tuples)

# my_set = {"apple", "banana", "mango", "apple", "mango", "mango"}
# print(my_set)

# my_set.remove("mango")
# print(my_set)

# 3
# 2

my_dictionary = {"name" : "Tom", 
                 "age" : 25,
                 "height" : 5.8,
                 "gender" : "male"}


# print(my_dictionary)

# # access the items
# print(my_dictionary.keys())
# print(my_dictionary.values())

# # modify the items with key
# my_dictionary["age"] = 30
# print(my_dictionary)
# print(my_dictionary["gender"])


# # remove items from a dict
# # my_dictionary.pop("gender")
# # print(my_dictionary)

# # for removing the last item
# my_dictionary.popitem()
# print(my_dictionary)


# name = None
# print(name)

