# Write a Python program that uses a function to check if a given number is prime or not.

def prime(number):
    return number > 1 and all(number % i for i in range(2, int(number ** 0.5) + 1))

num = int(input("Enter a number : "))
print(f"{num} {'is' if prime(num) else 'is not'} a prime number.")
