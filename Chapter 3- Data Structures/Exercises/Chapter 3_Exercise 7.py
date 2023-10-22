places = ['Rome' , 'Sydney Opera House' , 'Grand Canyon' , 'Maldives']

print(f"Original Order: {places}")
print(f"\nAlphabetical Order: {(sorted(places))}")
print(f"\nOriginal Order: {places}")
print(f"\nReversed Alphabetical Order: {(sorted(places ,reverse=True))}")
print(f"\nOriginal Order: {places}")
print(f"\nReversed Order: {places.reverse() or places}")
print(f"\nOrignal  Order: {places.reverse() or places}")
print(f"\nAlphabetical Order: {places.sort() or places}")
print(f"\nReversed Alphabetical Order: {places.sort(reverse=True) or places}")