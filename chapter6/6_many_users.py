# A dictionary in a Dictionary
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f'{user_info['first']} {user_info['last']}'
    location = user_info['location']

    print(f'\tFull name: {full_name.title()}')
    print(f'\tLocation: {location.title()}')

# The outer dictionary users maps each username (like 'aeinstein') to another dictionary containing that person’s details.
# Each inner dictionary holds keys like 'first', 'last', and 'location'.
# The for loop goes through each user:
# Prints the username.
# Combines the first and last names into a full name.
# Prints the formatted full name and location with proper capitalization.