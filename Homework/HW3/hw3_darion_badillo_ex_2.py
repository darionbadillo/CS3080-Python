"""
Homework 3 - Exercise 2
Name: Darion Badillo
Date: 02/23/2023
Description of your program: THis program takes user input of a string and then counts
all occurrences of each character in the string
"""
import pprint


# Takes string and counts all occurrences of each letter
def count_occurrences(phrase):
    count_string = {}
    # Takes one letter at a time and stores it into a variable
    for i in range(len(phrase)):
        count = 0
        letter = str(phrase[i])
        # Compares previously acquired character and compares to the rest of the string
        for j in range(len(phrase)):
            # Increments count value for each occurrence of letter
            if letter is phrase[j]:
                count += 1
                # Stores letter and count value into a dictionary
            if j == (len(phrase)-1):
                count_string[letter] = {count}

    return count_string


# main

# Takes user input for string
phrase = input("Please enter a string: ")

# Sends string to count_occurrences function which returns character count
occurrences = count_occurrences(phrase)

# Prints occurrences dictionary
pprint.pprint(occurrences)
