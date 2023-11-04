#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the


pet = [
    {'kind': 'Dog', 'name': 'Zeus', 'age': 7, 'owner': 'Angelo'},
    {'kind': 'Dog', 'name': 'Snow', 'age': 9, 'owner': 'Bella'},
    {'kind': 'Cat', 'name': 'Garfield', 'age': 4, 'owner': 'Luke'},
    {'kind': 'Fish', 'name': 'Goldie', 'age': 1, 'owner': 'Amira'},
]

# Loop through the list and print information about each pet
for pet in pet:
    kind = pet["kind"]
    age = pet["age"]
    owner = pet["owner"]
    print(f"Pet:{kind}")
    print(f"Age:{age} years old")
    print(f"Owner:{owner}")
    print()