"""
Homework 1
Name: Darion Badillo
Date: 1/31/2023
Description of your program: This program asks three questions before displaying a secret message
"""
import random as rand
import math


# Holds all the questions and flags for the three questions to be answered
def questions_three(q1, q2, q3, total):
    print(f"You have answered {total} questions correctly!")

    # For loop that loops through and asks questions depending on the amount of questions that have been answered
    # correctly
    for i in range(3):

        # 1st question never changes its answer. The answer is automatically put into lowercase for ease of verification
        # if statements for all three questions validates if the question has been answered successfully to exclude them
        # on the next loop around, if necessary
        if i == 0 and q1 is False:
            answer = input("\nWhat is the UCCS mascot?\n")
            answer = answer.lower()

            # If statement that will update the bool and increment the total correct questions answered if answered
            # correctly or will inform if the answer is wrong
            if "mountain lion" in answer:
                q1 = True
                total = total + 1
                print("Correct!")
            else:
                print("Wrong!")

        # 2nd question asks a remainder operation using the modulo operator. This question changes everytime
        elif i == 1 and q2 is False:

            # Uses random module to generate random numbers for different equations each loop around
            num1 = rand.randint(8, 25)
            num2 = rand.randint(3, 7)
            modulo_answer = int(num1 % num2)

            # Asks input from the user and casts input to an int
            answer = int(input(f"\nWhat is the remainder of {num1} divided by {num2}?\n"))

            # If statement that will update the bool and increment the total correct questions answered if answered
            # correctly or will inform if the answer is wrong
            if modulo_answer == answer:
                q2 = True
                total = total + 1
                print(f"Correct! The answer was {str(modulo_answer)}")
            else:
                print(f"Incorrect! The answer is {str(modulo_answer)}")

        # 3rd question asks for the answer to a math equation with randomly generated ints
        elif i == 2 and q3 is False:

            # Uses random module to generate random numbers for different equations each loop around
            num1 = rand.randint(1, 10)
            num2 = rand.randint(1, 10)
            num3 = rand.randint(1, 10)
            num4 = rand.randint(1, 10)

            # Casts equation_answer to a float and rounds the answer to 2 decimal places using math module
            equation_answer = float(num1 * num2 / num3 + num4)
            equation_answer = round(equation_answer, 2)

            print(f"\nAnswer the equation to the accuracy of two decimal places:\n{num1} * {num2} / {num3} + {num4}")

            # Casts user input to a float
            answer = float(input())

            # If statement that will update the bool and increment the total correct questions answered if answered
            # correctly or will inform if the answer is wrong
            if answer == equation_answer:
                q3 = True
                total = total + 1
                print(f"Correct! The answer is {equation_answer}")
            else:
                print(f"Incorrect! The answer was {equation_answer}")

    # Returns the four variables that will be used to control the next function call
    return q1, q2, q3, total


# main
# Booleans and variables
questions_answered, Q1, Q2, Q3 = False, False, False, False
correct_total = 0

print("Welcome!")
print("You will be asked three questions. "
      "All must be answered correctly."
      "Once a question is correctly answered, that question will be removed and counted."
      "Once all are answered correctly, a secret message will appear! Good luck!")

# Main while loop using a boolean control variable. Once all questions have been answered correctly, the boolean flag
# will be caught and loop will exit\
while not questions_answered:

    # If statement that updates the while control variable to exit the loop
    if Q1 and Q2 and Q3:
        questions_answered = True
        # This break is unnecessary, but it ensures that the code executes as intended
        break
    else:

        # Calls the function that will iterate through and ask the questions
        Q1, Q2, Q3, correct_total = questions_three(Q1, Q2, Q3, correct_total)
        continue

print("\nYou answered all questions successfully!\nThe secret phrase is \"Python is awesome!\""
      "\nHave a good day!")
