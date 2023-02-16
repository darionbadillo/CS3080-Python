"""
Homework 2 - Exercise 4_2
Name: Darion Badillo
Date: 02/14/2023
Description of your program: This program contains a guessing game where a randomly generated number is given, and the
user has to guess it correctly. The user will have 10 chances to get it right before the game ends. The game will inform
you if your guess is too high, too low, or correct.
"""
import random as rand


# Randomly generates bounds for the guessing game
def generate_bounds():
    lower = 2
    upper = 1

    # loops until bounds are properly set
    while lower > upper:
        lower = rand.randint(1, 100)
        upper = rand.randint(1, 100)

    if upper - 1 == lower:
        upper = upper + 10

    return lower, upper


# Guessing game takes user input and determines if user is upp
def guess_game(answer, counter):
    user_answer = valid_user_input()
    counter += 1

    # If else statements that determine if user's guess is too high, too low, or correct compared to the correct answer
    if user_answer > answer:
        print('Your guess is too high')
        return False, counter

    elif user_answer < answer:
        print('Your guess is too low')
        return False, counter

    elif user_answer == answer:
        return True, counter


# Tests user input for a valid integer number and will repeat prompt until a valid integer is given while not
# incrementing counter value
def valid_user_input():
    # Boolean control variable
    valid_input = False

    # Loops until valid input is given
    while not valid_input:
        print("Take a guess")
        user_input = input()

        if user_input.isdigit():
            valid_input = True
        else:
            print(f'{user_input} is not a valid number')

    # Returns valid integer guess
    return int(user_input)


# main
lower_bound, upper_bound = generate_bounds()
guess_answer = rand.randint(lower_bound, upper_bound)
counter = 0
correct = False
print(f'I am thinking of a number between {lower_bound} and {upper_bound}')

# Loops 10 times before game ends. Game will break loop early if guess is correct
for i in range(10):

    # Calls game function
    correct, counter = guess_game(guess_answer, counter)

    # breaks if correct
    if correct:
        break

# Prints formatted print statement displaying number of guesses if they guesses correctly
if correct:
    print(f'Good Job! you guessed the number in {counter} guesses!')

# Displays correct answer if not correctly guessed
elif not correct:
    print(f'Sorry I was thinking of {guess_answer}')
