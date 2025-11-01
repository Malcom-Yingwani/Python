# SAVING AND READING USER-GENERATED DATA

from pathlib import Path
import json

# # EXAMPLE 1

# username = input("What is your name? ")

# path = Path('username.json')
# contents = json.dumps(username)
# path.write_text(contents)
# print(f"We'll remember you when you come back, {username}!")

# # EXAMPLE 2
# path = Path('username.json')
# if path.exists():
#     contents = path.read_text()
#     username = json.loads(contents)
#     print(f"Welcome back, {username}!")
# else:
#     username = input("What is your name? ")
#     contents = json.dumps(username)
#     path.write_text(contents)
#     print(f"We'll remember you when you come back, {username}!")
    
# EXAMPLE 3 (REFACTORING)
# Refactoring into one function
# def greet_user():
#     """Greet the user by name."""
#     path = Path('username.json')
#     if path.exists():
#         contents = path.read_text()
#         username = json.loads(contents)
#         print(f"Welcome back, {username}!")
#     else:
#         username = input("What is your name? ")
#         contents = json.dumps(username)
#         path.write_text(contents)
#         print(f"We'll remember you when you come back, {username}!")
# greet_user()

# Refactoring into multiple functions

def get_stored_username(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
    else:
        return None

def get_new_username(path):
 """Prompt for a new username."""
 username = input("What is your name? ")
 contents = json.dumps(username)
 path.write_text(contents)
 return username

def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username}!")

greet_user()

# Refactoring is the proccess of making the code modular, typically making it shorter and easier to read.

# SUMMARY

# The program greets the user by name and remembers them between runs.

# It checks whether a file named username.json exists.

# If the file exists, it reads the stored username and displays “Welcome back, [username]!”

# If the file does not exist, it asks the user for their name and stores it in username.json for future use.

# It demonstrates the use of:

# File handling with the Path class.

# JSON serialization to store and retrieve data.

# User interaction through input and printed messages.

# Overall, it shows how to create a simple program that remembers user information between sessions.