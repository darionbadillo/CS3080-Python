"""
Homework 6 - Exercise 3
Name: Darion Badillo
Date: 04/14/2023
Description of your program: This program takes user input from the COMMAND LINE (not run program) and
takes two keywords: save and list. "save" automatically takes what is in your computer's clipboard and
saves it to a persistent dictionary with the word given after "save". "list" prints all keywords. If
neither keywords are given, the text saved under this keyword is copied to the clipboard. Remember to present
a word AFTER save in order to save the text in clipboard to accessible place.
EXAMPLE: >mcb.py save item
"""
import pyperclip
import sys
import shelve


with shelve.open('clipboard') as cb:

    if sys.argv[1] == 'save':
        cb[sys.argv[2]] = pyperclip.paste()

    elif sys.argv[1] == "list":
        for x in cb.keys():
            print(x)
    else:
        pyperclip.copy(cb.get(sys.argv[1]))

cb.close()
