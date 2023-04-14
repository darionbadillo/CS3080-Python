"""
Homework 4 - Exercise 2
Name: Darion Badillo
Date: 03/09/2023
Description of your program: This program explores the use of regular expressions to match text to an email or phone
number and neatly prints all found data
"""
import pyperclip as pc
import re


# Uses regex to create a pattern that then searches for valid phone numbers
def is_phone_number(text):

    # regex number pattern
    phone_num_regex = re.compile(r'\d{3}-\d{3}-\d{4}|\d{3}\s\d{3}\s\d{4}|\d{3}.\d{3}.\d{4}')
    numbers = phone_num_regex.findall(text)
    return numbers


# Uses regex to create a pattern that will match most email addresses
def is_email(text):

    # regex email pattern
    email_regex = re.compile(r'[a-zA-Z0-9.%+_-]+@[a-zA-Z0-9_]+\.[a-zA-Z]{2,3}')

    emails = email_regex.findall(text)
    return emails


# main
print('Please copy a page to the clipboard.\n'
      'The program will start once something new has been copied.')
pasted_text = pc.waitForPaste()

phone_list = is_phone_number(pasted_text)
address_list = is_email(pasted_text)

# Neatly prints phone numbers
print("\nPhone numbers found:\n------------")
for line in phone_list:
    print(line)

# Neatly prints email addresses
print("\nEmail addresses found:\n------------")
for line in address_list:
    print(line)
