def describe_city(city, country = "south africa"):
    """Prints a statement about where a city is located"""
    print(f"{city.title()} is in {country.title()}")

describe_city("johanesburg")
describe_city(city="new york", country="usa")
describe_city("hong kong", "china")