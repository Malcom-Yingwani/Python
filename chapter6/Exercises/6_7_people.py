person_0 = {
    'first_name': 'david',
    'last_name': 'smith',
    'age': 25,
    'city': 'johannesburg'
    }
person_1 = {
    'first_name': 'athi',
    'last_name': 'mqgibelo',
    'age': 36,
    'city': 'orange farm',
    }
person_2 = {
    'first_name': 'athe',
    'last_name': 'mtangayi',
    'age': 20,
    'city': 'ntabankulu',
    }

people = [person_0, person_1, person_2]

for person in people:
    print('\nEverything we know about this man:')
    print(f'First Name: {person['first_name'].title()}')
    print(f'Last Name: {person['last_name'].title()}')
    print(person['age'])
    print(f'City: {person['city'].title()}')