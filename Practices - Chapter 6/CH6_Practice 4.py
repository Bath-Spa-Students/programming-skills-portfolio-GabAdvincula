#Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

persons = ['Simon', 'Dempster', 'Adam', 'Edgar']
for person in persons:
    if person == 'Edgar':
        print(f"Found {person}. ")
        break
    print(f"Finding {person}...")

print("Finished.")