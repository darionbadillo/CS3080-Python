"""
Homework 4 - Exercise 1
Name: Darion Badillo
Date: 03/09/2023
Description of your program: This program uses classes and objects to calculate the area, diagonal, perimeter, or diameter
of a Rectangle, Square, or Circle.
"""
import math


# Holds the dimensions of a rectangle
class Rectangle:

    # Initializer / Instance Attributes
    def __init__(self, length, width):
        self.length = float(length)
        self.width = float(width)

    # Calculates the area
    def area(self):
        return self.length * self.width

    # Calculates the diagonal
    def diagonal(self):
        return math.sqrt(math.pow(self.width, 2) + math.pow(self.length, 2))

    # Calculates the perimeter
    def perimeter(self):
        return 2 * self.length + 2 * self.width


# Holds the dimensions of a square
class Square(Rectangle):

    # Initializer / Instance Attributes
    def __init__(self, length):
        super().__init__(length, length)

    # Calculates the diagonal
    def diagonal(self):
        return math.sqrt(2) * self.length


# Holds the dimensions for a circle
class Circle:

    # Initializer / Instance Attributes
    def __init__(self, radius):
        self.radius = float(radius)

    def area(self):
        return math.pi * math.pow(self.radius, 2)

    def diameter(self):
        return 2 * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


# main

# Creates a rectangle object with pre-determined dimensions
rectangle = Rectangle(20, 10)

# Uses class method to determine diagonal
rectangle_diagonal = rectangle.diagonal()

# Divides the rectangle_diagonal by 2 which will be used for the radius of a circle
radius = rectangle_diagonal / 2

# Creates a circle object
circle = Circle(radius)

# Calculates perimeter of the circle
circle_perimeter = circle.perimeter()

print(f'Rectangle Dimensions: L = {round(rectangle.length)}, W = {round(rectangle.width)}\n'
      f'Rectangle Diagonal: {round(rectangle_diagonal, 2)}\n'
      f'Radius of circle given by Rectangle Diagonal / 2: {round(radius, 2)}\n'
      f'Circle perimeter: {round(circle_perimeter, 2)}')
