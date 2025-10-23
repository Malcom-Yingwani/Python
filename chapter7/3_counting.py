# While loops

# current_number = 1

# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# Letting the user choose when to quit

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. " #concatinating the prompt allows it to be multilined

# message = ""
# while message != 'quit':
#     message = input(prompt)

#     if message != 'quit':
#         print(message)

#-----------------------------------------------------------------------------------------

# Usiing flags

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "

# active = True
# while active:
#     message = input(prompt)

#     if message == 'quit':
#         active = False
#     else:
#         print(message)

# ----------------------------------------------------------------------------
#  Using break to exit a loop

# prompt = "\nPlease enter the name of a city you have visited:"
# prompt += "\n(Enter 'quit' when you are finished.) "

# while True:
#     city = input(prompt)

#     if city == 'quit':
#         break
#     else:
#         print(f"I'd love to go to {city.title()}!")

# -------------------------------------------------------------------------------

# continue. Returns to beginning of loop based on result

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)    