# dictionaries in dictionaries
cities = {
    'johannesburg' : {
        'country': 'south africa',
        'population': 6_445_000,
        'fun fact': "Nicknamed 'eGoli'",
        },
    'cape town': {
        'country': 'south africa',
        'population': 4_772_846,
        'fun fact': "Everyday at noon the historic 'Noon Gun' is fired.",
        },
    'durban':{
        'country': 'south africa',
        'population': 3_720_953,
        'fun fact': "Known as 'Surf City'",
    },

    }

for city, city_info in cities.items():
    print(f'\nCity: {city.title()}')
    print(f'Country: {city_info['country'].title()}')
    print(f'Population: {city_info['population']}')
    print(f'Fun Fact: {city_info['fun fact']} ')