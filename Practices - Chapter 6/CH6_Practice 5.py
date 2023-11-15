#Write a Python program that uses a while loop to find the largest number among a series of  user-input values until they enter '0' to exit the loop.

largest_number = 0

while True:
    user_input = float(input("Enter a number (enter '0' to exit the loop): "))
    
    if user_input == 0:
        break
    
    largest_number = max(largest_number, user_input)

print("The largest number is:", largest_number)