"""
1. Create a dictionary with name and age, filter the names under age 18
Then map the remaining names using lambda
"""

# my_dictionary = [
#     {"name" : "Tom", "age" : 25 },
#     {"name" : "Peter", "age" : 17},
#     {"name" : "Charles", "age" : 19}
# ]

# # use filter to get under 18
# minors = list(filter(lambda person : person['age'] <= 18, my_dictionary))
# print(minors)

# # majors filtered out 
# majors = list(filter(lambda person : person['age'] >= 18, my_dictionary))

# # use map to get over 18
# remaining_names = list(map(lambda person : person['name'], majors))
# print(remaining_names)

"""
2. use reduce and lambda to calculate the product of all numbers
"""

# from functools import reduce

# my_numbers_list = [4, 5, 6, 7]

# # get the product
# product = reduce(lambda x, y : x * y, my_numbers_list)
# print(f"Final product : {product}")

"""
3. List comprehension, list of square of even numbers
"""

# my_numbers = [1, 2, 3, 4, 5, 6]

# squares = [num**2 for num in my_numbers if (lambda n : n % 2 == 0) (num)]

# print(f"The squared even number values: {squares}")

"""
4. check given string is a number
"""

# check_number = lambda s : 'int' if s.isdigit() else 'not a number'
# print(check_number(123))
# print(check_number("32"))

"""
5. extract year, month and date from a date time object
"""

# datetime should be imported
# import datetime

# mydatetime = datetime.datetime.now()

# get_specific = lambda dt : (dt.year, dt.month, dt.day)
# print(get_specific(mydatetime))

