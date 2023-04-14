"""
Homework 5 - Exercise 3
Name: Darion Badillo
Date: 03/22/2023
Description of your program: This program creates a custom generator range function that yields the individual values
and saves memory
"""


# Generator range function
def genrange(stop, start=0, step=1):
    n = start
    x = step
    while n < stop:
        yield n
        n = n + x


# Iterates through genrange using a generator expression
gen = (x * 1 for x in genrange(10, 3, 2))
print(type(gen))
for x in gen:
    print(x)
