"""
Homework 2 - Exercise 1
Name: Darion Badillo
Date: 02/14/2023
Description of your program: This program allows a user to enter a number that will be used in the function collatz().
The collatz function will determine if a number is even or odd and will manipulate the number depending on its state.
The program will manipulate the number as many times as necessary until the number reaches '1'.
"""


def collatz(number):
    # Use a breakpoint in the code line below to debug your script.
    if number % 2 == 0:
        return number / 2
    else:
        return 3 * number + 1


# main

number = input("Enter number: \n")

while number != 1:
    number = collatz(int(number))
    print(number)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
