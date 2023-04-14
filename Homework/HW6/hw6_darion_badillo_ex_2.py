"""
Homework 6 - Exercise 2
Name: Darion Badillo
Date: 04/14/2023
Conclusion: Using a functools.lru_cache call before the countCalls decorator cut the amount of calls exponentially.
"""
import functools


def countCalls(func):
    @functools.wraps(func)
    def wrapperCountCalls(*args, **kwargs):
        wrapperCountCalls.numCalls += 1
        print("Call {} of {}".format(wrapperCountCalls.numCalls, func.__name__))
        return func(*args, **kwargs)
    wrapperCountCalls.numCalls = 0
    return wrapperCountCalls


@functools.lru_cache(None)
@countCalls
def fibonacci(num):
    if num < 2:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


numFib = int(input("Please enter a number: "))
print(fibonacci(numFib))



