#Write a Python program to iterate through both the keys and values of a dictionary and print them 

personal_info = {
    'First_name': 'Gab',
    'Last_name': 'Advincula',
    'Age': '20',
    'Birthday': 'March 8, 2003',
    'Location': 'United Arab Emirates'
}


for key, value in personal_info.items():
    print(f'{key}: {value}')