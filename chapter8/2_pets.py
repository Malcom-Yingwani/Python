# # Different ways of passing arguments in fucntions

# # 1) Positional arguments

# def describe_pet(animal_type, pet_name):
#     """Display information about a pet."""

#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")


# describe_pet('hamster', 'harry')


# # 2) KEYWORD ARGUMENTS
# describe_pet(animal_type="hamster", pet_name="harry")
# describe_pet(pet_name="sally", animal_type="dog")

# 3) DEFAULT VALUES

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet."""

    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")


describe_pet(pet_name="willie")
describe_pet('will')
describe_pet(pet_name="fluffy", animal_type="cat") # default arguements only run if no argument is provided


# 4) EQUIVALENT FUNCTION CALLS

# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')


