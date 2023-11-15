#Given a Python list, write a program to remove all occurrences of item 20.
#Given list: [5, 20, 15, 20, 25, 50, 20]

list = [5, 20, 15, 20, 25, 50, 20]

while 20 in list:
    list.remove(20)

print("Updated list:", list)