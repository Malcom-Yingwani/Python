# Functions 
# Defining a function

def greet_user():
    """Display a simple greeting.""" # This is called a docstring, describes what the function does. Generates documentation for the function, shown when you hover over it
    print("Hello!")


greet_user()


# Passing information to a function
def greet_user(username):
    """Display a simple greeting"""
    print(f"Hello, {username.title()}!")


greet_user('malcom')

