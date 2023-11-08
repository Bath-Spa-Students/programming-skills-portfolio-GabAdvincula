#Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, 
#Give the parameter for the country a default value.
#Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city , country = 'Philippines'):
    msg =f"{city.title()} is part of  {country.title()}."
    print(msg)

describe_city('Cebu')
describe_city('Ajman', 'United Arab Emirates')
describe_city('Quezon')