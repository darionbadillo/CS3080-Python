"""
Homework 5 - Exercise 2
Name: Darion Badillo
Date: 03/22/2023
Description of your program: This program creates a generator that provides the first n tuples of a pythagorean triplet
"""
import math as m


# Generator function that generates pythagorean triplets
def pyt():
    for y in range(100):
        for x in range(1, y):
            hyp = m.pow(x, 2) + m.pow(y, 2)
            if m.sqrt(hyp) % 1 == 0:
                hyp = int(m.sqrt(hyp))
                yield x, y, hyp


# Sequence function that appends each tuple found to a list
def take(n, seq):
    seq = iter(seq)
    result = []
    try:
        for i in range(n):
            result.append(next(seq))
    except StopIteration:
        pass
    return result


# stores generated sequence in a list
triplets = take(10, pyt())

# Neatly prints all triplets found in specified range
for triplet in triplets:
    print(*triplet)

