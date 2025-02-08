# Exception Handling

# try and except block

# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("Error : Division by zero is not possible")

# Multiple exception handling

# try:
#     num = int(input("Enter a Number: "))
#     result = 10 / num
#     print(result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")
# except ValueError:
#     print("Error: Invalid input, Please enter a number!")

# using else and finally
# try:
#     num = int(input("Enter a Number: "))
#     result = 10 / num
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero")
# else:
#     print(f"Result : {result}")
# finally:
#     print(f"Execution Completed")

# Raise Exceptions 

def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18")
    return "Access Granted"

try:
    print(check_age(16))
except ValueError as error:
    print("Exception: ", error)
