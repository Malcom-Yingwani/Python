# Confirmed users
# Usinf while loops with lists and dictionaries

# Start with users that need to be verified, and an empty list to hold confirmed users.

# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []

# verify each User
# move each user to confirmed

# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()

#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)

# # Display all confirmed users.

# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

#------------------------------------------------------------------------------------------

# Removing all instances of a specific value.

# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)

# while 'cat' in pets:
#     pets.remove('cat')
#     print(pets)

# print("\nUpdated list")
# print(pets)

#------------------------------------------------------------------------------------------

# Filling a dictionary with user input

responses = {}
# Ser a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary
    responses[name] = response

    # Find out if anyone else id going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
       polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")


# Summary

# The program asks each person for their name.

# It then asks which mountain they would like to climb.

# Each answer is saved in a dictionary, with the name as the key and the mountain as the value.

# The program keeps asking for more responses until the user says “no.”

# When done, it prints all the names and the mountains they want to climb.