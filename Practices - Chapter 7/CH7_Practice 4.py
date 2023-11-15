#Write a Python program that defines a function to calculate the area of a circle, and then calls that function with a given radius.

import math

def calculate(radius):
    return math.pi * radius ** 2


radius = 2
area = calculate(radius)

print("The area of the circle is:", area)