#Store the locations in a list. Make sure the list is not in alphabetical order.
places = ['Rome' , 'Sydney Opera House' , 'Grand Canyon' , 'Maldives']

#Print your list in its original order.
print(f"Original Order: {places}")
#Use sorted() to print your list in alphabetical order without modifying the actual list.
print(f"\nAlphabetical Order: {(sorted(places))}")
#Show that your list is still in its original order by printing it.
print(f"\nOriginal Order: {places}")
# Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
print(f"\nReversed Alphabetical Order: {(sorted(places ,reverse=True))}")
#Show that your list is still in its original order by printing it again.
print(f"\nOriginal Order: {places}")
#Use reverse() to change the order of your list. Print the list to show that its order has changed.
print(f"\nReversed Order: {places.reverse() or places}")
#Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
print(f"\nOrignal  Order: {places.reverse() or places}")
#se sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
print(f"\nAlphabetical Order: {places.sort() or places}")
#Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.
print(f"\nReversed Alphabetical Order: {places.sort(reverse=True) or places}")
