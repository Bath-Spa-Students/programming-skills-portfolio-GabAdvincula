#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. 
#print a message saying you’ll add that topping to their pizza.
pizza = "\nWhat topping would you like on your pizza? \nType 'quit' when you are done deciding: "
 
while True:
    topping = input(pizza)
    if topping != 'quit':
     print(f"\nOkay, Pizza will now be cooked with {topping} as your toppings.")
    else:
        break
