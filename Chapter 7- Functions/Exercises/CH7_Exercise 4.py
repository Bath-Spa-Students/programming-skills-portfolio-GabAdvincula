#Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(tshirt_size = 'large' , shirt_message = 'I love python'):
    print(f"\nI'm going to make a {tshirt_size} shirt.")
    print(f'The print will be, "{shirt_message}"')

make_shirt()
make_shirt(tshirt_size='medium')
make_shirt('small', 'We can do this!!.')