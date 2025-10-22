# Poll Example
people_to_poll = ['jen', 'sarah', 'edward', 'phil']

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    }

for name in people_to_poll:
    if name in favorite_languages.keys():
        print(f'Thank you {name.title()} for answering the poll')
    elif name not in favorite_languages.keys():
        print(f'{name.title()}, please answer the poll')