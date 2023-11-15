#Write a Python program that uses the elif statement to determine the season based on the month provided as input.

month = int(input("Please enter the month (1-12): "))

if month == 1 or month == 2 or month == 12:
    season = "Winter"
elif month >= 3 and month <= 5:
    season = "Spring"
elif month >= 6 and month <= 8:
    season = "Summer"
elif month >= 9 and month <= 11:
    season = "Autumn"
else:
    season = "Oh no!! Invalid month"

print(f"The season for month {month} is {season}")