#Make a list called sandwich_orders and fill it with the names of various sandwiches.
#Make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order.
#Move it to the list of finished sandwiches. 
#After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['egg sandwich','tuna  sandwich','grilled cheese sandwich','bacon sandwich']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm preparing your {current_sandwich}.")
    finished_sandwiches.append(current_sandwich)

print("\n")
for sandwich in finished_sandwiches:
    print(f"I prepared and made a {sandwich}.")