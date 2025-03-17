# Creating a function


# def my_function():
#     print("Hello, I'm a function")

# my_function()    # calling a function

def greet():
    print("Greetings to all")

# greet()


# Functions will return some data
def sum_function():
    a = 5
    b = 2
    return a + b #7

def sub_funtion():
    a = 5
    b = 2
    return a - b #3

# sum_function() + sub_funtion()


# def my_function():
#     a = 10
#     return 5 * a

# print(my_function())



# Pass some values inside a function
def new_function(num):
    return 5 * num

# print(new_function(40))


def add_function(num1, num2, num3):
    print("Add function executed!")
    return num1 + num2 + num3

# add_function(4, 5, 2)


"""
Write a function to calculate the total length of a given string

string_data = "python programming"
"""

def string_length(data):
    return len(data)

# print(string_length("python programming"))


def string_length(data):
    count = 0

    for char in data:
        count += 1 # count = count + 1
    return count

# print(string_length("python programming"))


"""
write a function to get the character frequency of elements of a list 
list_data = ['a', 'c', 'a', 'e', 'f', 'g' , 'i', 'f']

output = a - 2, c - 1
"""

def get_frequency(data):
    frequency = {}

    for char in data:
        if char in frequency:
            frequency[char] = frequency[char] + 1
        else:
            frequency[char] = 1
    return frequency

list_data = ['a', 'c', 'a', 'e', 'f', 'g' , 'i', 'f']
# print(get_frequency(list_data))


# def full_name(first_name):
#     print(first_name, "Peter")

# full_name("Emil")
# full_name("Tom")
# full_name("Jack")




"""
Used + operator
EmilPeter
TomPeter
JackPeter

Used , between names
Emil Peter
Tom Peter
Jack Peter
"""


# def my_function1(first_name, last_name):
#     print(first_name, last_name)

# my_function1("Tom", "Peter")


# Arbitrary Arguments 

def my_function(*kids):
    print("The first child is ", kids[0])

# my_function("Emil", "Tom", "peter", "sham", "kenny")


# Keyword Arguments

def function2(child3, child2, child1):
    print("The youngest child is ", child3)

# function2(child1="Emil", child2= "Tom", child3= "Peter")


# Kwargs

def function3(**kid):
    print("His last name age is ", kid["age"])

# function3(first_name = "Tom", last_name = "Peter", age = 32)


# Closure functions

def outer_function(msg):
    def inner_function():
        print("This is my message", msg)
    return inner_function

# print(outer_function("Hello, Closure!"))
# <function outer_function.<locals>.inner_function at 0x00000150FCE58900>

closure = outer_function("Hello, Closure!")
# closure()

def wrapper(chocolate):
    def chocolate_functn():
        print("The content is" , chocolate)
    return chocolate_functn

get_chocky = wrapper("Chocolate")
# get_chocky()


# Callback function

def greet(name):
    print("Hello", name)

def execute_callback(callback1, first_name):
    callback1(first_name) # greet("Alice")

# execute_callback(greet, "Alice")


def sum_function(num3):
    print("The sum is", 10 + 2 + num3)

def execute_sum(my_callback,num3):
    my_callback(num3)

# execute_sum(sum_function, 5) 

# Recursion - A function calling itself again and again

def recursive_factorial(num):
    if num == 1:
        return num
    else:
        return num * recursive_factorial(num - 1)
    
number = 8
# print(recursive_factorial(number))


# Creating a file using 'x' mode
def create_file(file_name):
    file = open(file_name, 'x')
    file.close()

my_file_name = "batch_file.txt"
# create_file(my_file_name)

# Writing data into a text file
def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()

my_file_name = "my_new_file.txt"
my_data = "Python Programming"
# write_data(my_file_name, my_data)


# Adding data without over riding

def append_data(file_name, data):
    file = open(file_name, 'a')
    file.write(data)
    file.close()

my_file_name = "my_new_file.txt"
my_data = "Adding new data"
# append_data(my_file_name, my_data)

# file_name = "my_new_file.txt"
# data = "Updated Data"
# file = open(file_name, 'a')
# file.write(data)
# file.close()

# Reading file content using "r" mode

def read_file(file_name):
    file = open(file_name, "r")
    for data in file:
        print(data)

my_file_name = "new.txt"
# read_file(my_file_name)

def read_file1(file_name):
    file = open(file_name, "r")
    return file.read()

my_file_name = "new.txt"
print(read_file1(my_file_name))

