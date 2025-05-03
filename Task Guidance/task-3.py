"""
Guessing and Word Scrample Sample Code
"""

# for randomly choosing any values
import random

# setup the range of values 
number_guess = random.randint(1, 10)


while True:
    user_guessing = int(input("Enter the number(1-10)"))

    # use if else condition to verify
    if user_guessing > number_guess:
        print("Too High")
    elif user_guessing < number_guess:
        print("Too Low")
    else:
        print("Guessing Matched!")
        break

# Text guessing game

import random

my_choices = ["rock", "paper", "scissor"]

system_guess = random.choice(my_choices)

user_guess = input("Enter the choice - rock, paper, scissor")

while True:
    if user_guess not in my_choices:
        print("Not in my choices!")
        break
    elif user_guess != system_guess:
        print("Wrong Guess!")
    else:
        print("Right Guess!")
        break