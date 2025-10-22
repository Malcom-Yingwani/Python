# Looping through a dictionary
# Looping through all key-value pairs
user_0 = {
    'username': 'erfemi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f'\nKey: {key}')
    print(f'Value: {value}')

print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

# Looping through keys
print()

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

for name in favorite_languages.keys(): # for name in favorite_languages: would also have worked, looping through keys is the default if not specified
 print(name.title())

# Accessing key by using the current key

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
       language = favorite_languages[name].title()
    print(f"\t{name.title()}, I see you love {language}!")

# Looping through a dictionary in a particular order
print()

favorite_languages = {
   'jen': 'python',
   'sarah': 'c',
   'edward': 'rust',
   'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
   print(f'{name.title()}, thank you for taking the poll.')

# Looping through all values in a dictionary

print('The following languages have been mentioned:')
for language in favorite_languages.values():
   print(language.title())

# Using set to extract unique values from a dictionary

print('The following unique languages were mentioned')
for language in set(favorite_languages.values()):
   print(language.title())

# Building a set directly
languages = {'python', 'rust', 'python', 'c'}
print(languages)