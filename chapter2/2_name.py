# using variables

message = "Hello Python world"
print(message)

message = "Hello Python Crash Course world!"
print(message)

# Strings

'This is a string'
"This is a string"

'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

# Changing case

name = "ada lovelace"
print(name.title())


name = "Ada Lovelace"
print(name.upper())
print(name.lower())

# Using variables in strings

first_name = "malcom"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

print(f"Hello, {full_name.title()}!")

# Adding white space with tabs or newlines

print("Python")
print("\tPython")

print("Language:\nPython\nC\n\tJavaScript")

print('\n')

# Removing Prefixes
nostarch_url = 'https://nostarch.com'
simple_url = (nostarch_url.removeprefix('https://'))
print(simple_url)

