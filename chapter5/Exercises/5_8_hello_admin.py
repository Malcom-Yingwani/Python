# if statements and looping through lists
users = ['peter', 'john', 'james', 'admin', 'simon']

if not users: 
        print('We need to find some users!')
else:
    for user in users:

        if user == 'admin':
            print('Hello Admin, would you like to see a status report?')
        else:
            print(f'Hello {user.title()}, thank you for logging in again')        
