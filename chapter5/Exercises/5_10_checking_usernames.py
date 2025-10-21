# Handling usernames 

current_users = ['peter', 'james', 'john', 'paul', 'timothy']
new_users = ['silus', 'pilate', 'JAMES', 'sproul', 'timothy']

current_users_lower = [user.lower() for user in current_users]
for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f'Sorry, the username {new_user.title()} is already taken. Please enter a new username')
    else:
        print('The username is available')