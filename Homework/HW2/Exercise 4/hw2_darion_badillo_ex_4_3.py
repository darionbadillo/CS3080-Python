"""
Homework 2 - Exercise 4_3
Name: Darion Badillo
Date: 02/14/2023
Description of your program: This program contains a guessing game where a randomly generated number is given, and the
computer has to guess it correctly. The computer has 10 chances to get it right before the game ends. With each guess,
the answer will become more accurate.
"""
import random as rand


# Randomly generates bounds for the guessing game
def generate_bounds():
    lower = 2

    lower = rand.randint(1, 1000)
    upper = lower + 500

    return lower, upper


# Guessing game takes user input and determines if user is upp
def guess_game(answer, counter, lower, upper, guessed_answers):

    # While loop that calls valid_user_input to check current answer against already existing answer
    # New answer will be given answer already exists
    new_answer = False
    if guessed_answers:
        while not new_answer:
            random_answer = rand.randint(lower, upper)
            new_answer = valid_user_input(random_answer, guessed_answers)
            if not new_answer:
                print(f'{random_answer} has already been made')

    # Allows the computer to make a first guess
    if not guessed_answers:
        random_answer = rand.randint(lower, upper)

    counter += 1

    # If else statements that determine if the guess is too high, too low, or correct compared to the correct answer
    if random_answer > answer:
        print(f'{random_answer} is too high')
        # Sets the new upper bound to the guess to allow for a more accurate guess
        upper = random_answer
        guessed_answers.append(random_answer)
        return False, counter, guessed_answers, lower, upper

    elif random_answer < answer:
        print(f'{random_answer} is too low')
        # Sets the new lower bound to the guess to allow for a more accurate guess
        lower = random_answer
        guessed_answers.append(random_answer)
        return False, counter, guessed_answers, lower, upper

    elif random_answer == answer:
        return True, counter, guessed_answers, lower, upper


# Tests user input for a valid integer number and will repeat prompt until a valid integer is given while not
# incrementing counter value
def valid_user_input(random_answer, existing_answers):
    # Boolean control variable
    valid_input = True

    # Loops through existing answers to check if random answer has already been used
    for item in range(0, len(existing_answers)):
        if int(random_answer) == int(existing_answers[item]):
            valid_input = False

    # Returns valid integer guess
    return valid_input


# main
lower_bound, upper_bound = generate_bounds()
guess_answer = rand.randint(lower_bound, upper_bound)
guessed_answers = []
counter = 0
correct = False

print(f'I am thinking of a number between {lower_bound} and {upper_bound}')

# Loops 10 times before game ends. Game will break loop early if guess is correct
for i in range(10):

    # Calls game function
    correct, counter, guessed_answers, lower_bound, upper_bound = guess_game(guess_answer, counter, lower_bound, upper_bound, guessed_answers)

    # breaks if correct
    if correct:
        break

# Prints formatted print statement displaying number of guesses if they guesses correctly
if correct:
    print(f'Good Job! You guessed the correct number {guess_answer} in {counter} guesses!')

# Displays correct answer if not correctly guessed
elif not correct:
    print(f'Sorry I was thinking of {guess_answer}')
