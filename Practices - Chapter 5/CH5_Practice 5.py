#Write a Python program to merge two dictionaries into one.
person1 = {
    'First_name': 'James',
    'Last_name': 'Libit',
    'Age': 20,
    'Location': 'Philippines'
}

person2 = {
    'First_name': 'Luke',
    'Last_name': 'Mendoza',
    'Age': 20,
    'Location': 'Indonesia'
}


persons = {}


persons['James'] = person1


persons['Luke'] = person2

print("Merged Dictionary:")
print(persons)