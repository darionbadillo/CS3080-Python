"""
Homework 5 - Exercise 1
Name: Darion Badillo
Date: 03/22/2023
Description of your program: This program creates a reverse iterator that iterates through the list backwards
"""


class ReverseIter:

    def __init__(self, n=None):
        self.i = len(n)-1
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n[self.i]:
            result = self.n[self.i]
            self.i -= 1
            return result
        else:
            raise StopIteration()


# Create
forward_list = [3, 4, 5, 6]
reverse = ReverseIter(forward_list)

print(next(reverse))
print(next(reverse))
print(next(reverse))
print(next(reverse))
print(next(reverse))
