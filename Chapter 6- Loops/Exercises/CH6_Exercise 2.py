#If a person is under the age of 3, the ticket is free.
#If they are between 3 and 12, the ticket is $10.
#If they are over age 12, the ticket is $15. \
#Write a loop in which you ask users their  age, and then tell them the cost of their movie ticket.

age_regulation = ("Hi, good day! As per theater regulations, may I ask what your age is? \ntype quit if your finished: ")

while True:
    age = input(age_regulation)
    if age =='quit':
      break
    age = int(age)
    if age < 3:
      print(" As per theater age regulations , the ticket is still free.")
    elif age < 13:
      print("As per theater age regulations ,  we will be charging 10$ for the ticket.")
    else:
      print ("As per theater age regulations, we will be charging 15$ for the ticket") 