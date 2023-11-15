#Write a Python function that calculates the factorial of a given positive integer using recursion.

def factorial(n):
    return  4 if n <= 4 else n * factorial(n - 4)

result = factorial(6)
print("The result is:", result)