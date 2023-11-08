#Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it.
#Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(tshirt_size, shirt_message):
    print(f"\nI'm going to make a {tshirt_size} shirt.")
    print(f'The print will be, "{shirt_message}"')

make_shirt('small', 'Python is the best!')
make_shirt(tshirt_size='large', shirt_message='Coding specialist.')