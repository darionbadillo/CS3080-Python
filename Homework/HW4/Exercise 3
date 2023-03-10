"""
Homework 4 - Exercise 3
Name: Darion Badillo
Date: 03/09/2023
Description of your program: This program explores the use of regular expressions to create a strong password with 
specified parameters
"""
import re


# Checks the password for validity
def password_check(check, strong_password):

    # Uses Regex to create a pattern that checks for one uppercase letter, one lowercase letter, and one number
    check_regex = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])')

    # Uses search to check if check_regex is empty. If it is empty, the password is invalid. If not, password is valid.
    if check_regex.search(check) is not None:

        # Final check to ensure appropriate length
        if len(check) >= 8:
            # sets bool to True to exit loop
            strong_password = True

    return strong_password


# main
print('\n-----')

# Sets bool to false. Control variable
password_strength = False
while password_strength is False:
    print("Your password must be at least 8 characters long, contains both upper and lower case letters, and at least "
          "one number")
    password = input('Please enter a password: ')
    password_strength = password_check(password, password_strength)

    # Prints if password isn't strong enough
    if password_strength is False:
        print("Password not valid. \nPlease try again\n")

print("Password is valid.")
