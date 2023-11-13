#Use a loop to print a sentence about each river
major_rivers = { 'congo river' : 'congo',
                 'mekong river': 'china',
                 'amazon river': 'brazil',
          }

# Print a sentence about each river
for river, country in major_rivers.items():
    print(f"The {river} runs through {country}.")

# Print the name of each river
print("\nTRivers included in the dictionary:")
for river in major_rivers.keys():
    print(river)

# Print the name of each country
print("\nCountries included in the dictionary:")
for country in major_rivers.values():
    print(country)
