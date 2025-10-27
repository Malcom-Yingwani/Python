# PASSING AN ARBITRARY NUMBER OF ARGS

def make_pizza(*toppings): # * converts the arguments into a tupple
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# MIXING POSITIONAL AND ARBITRARY ARGUMENTS

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}"
              
              )
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# USING ARBITRARY KEYWORD ARGUMENTS

def build_profile(first, last, **user_info): # ** formats arguments as dictionary
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['info_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein', location = 'princeton', field = 'physics')

print(user_profile)