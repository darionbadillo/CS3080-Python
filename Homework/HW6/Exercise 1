"""
Homework 6 - Exercise 1
Name: Darion Badillo
Date: 04/14/2023
Description of your program: This program uses decorators with an optional argument that will wait for whatever
amount of user defined seconds to execute
"""
import functools
import time


def superDecorator(seconds=1):
    print(f'I will sleep for {seconds}')

    def slowDown(func):
        """Sleep 1 second before calling the function"""
        @functools.wraps(func)
        def wrapperSlowDown(*args, **kwargs):
            time.sleep(seconds)
            return func(*args, **kwargs)
        return wrapperSlowDown
    return slowDown


@superDecorator(seconds=int(input("Please enter the amount of time to wait: ")))
def goodMorning():
    print("I am awake")


goodMorning()
