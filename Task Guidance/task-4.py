"""
1. Python program to split and store odd and even number from a list

Logic:

Any number is even, if the number % 2 == 0
Any number is odd, if the number % 2 != 0
"""

# common_list = [5, 8, 12, 27, 32]

# # using for loop to iterate the values
# for number in common_list:
#     if number % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")

"""
Create two lists to store odd and even numbers
"""

"""
2. Check the number number or not from a numbers_list
"""
# my_list = [3, 62, 45, 100]

# def is_prime_number(num):
#     # prime number should not be less than or equal to 1
#     if num <= 1:
#         return False
#     # starts from 2 upto the square of that number 
#     for value in range(2, int(num**0.5) + 1):
#         if num % value == 0:
#             return False
#     return True

# for item in my_list:
#     print(is_prime_number(item))

"""
3. Happy Number

a number which reaches 1 when replaced by the sum of the square of each digit. 
For example 82 is a happy number. (8² + 2² = 68 -> 6² + 8² = 100 -> 1² + 0² + 0² = 1)

"""

"""
4. Sum of first and last digit of an integer
"""

# my_name = "Tom" # string T - 0, o - 1 and m - 2
# my_int = "456" # int

# print(my_name[1])
# print(my_int[0]) # TypeError: 'int' object is not subscriptable

# print(type(my_int[0]))


# my_number = 4567
# output = 4 + 7 = 11

"""
get user input
convert int to string
now get the first and last digit and sum them
return the values
"""

# user_input = int(input("Enter the number: "))

# # convert int to string
# string_input = str(user_input)

# first_digit = string_input[0]
# last_digit = string_input[-1]

# total = int(first_digit) + int(last_digit)
# print(total)

"""
5. Find all the possible combo to make Rs.10 using Rs.1, Rs.2, Rs.5 and Rs.10
"""

# Nested loops - loops inside loop concept

# for num1 in range(11):
#     for num2 in range(6):
#         for num3 in range(3):
#             for num4 in range(2):
#                 if num1*1 + num2*2 + num3*5 + num4*10 == 10:
#                     print(f"1Rs: {num1}, 2Rs: {num2}, 5Rs: {num3}, 10Rs: {num4}")

