# MODIFYING A LIST IN A FUNCTION

# Example 1

# Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)

# Example 2

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""

    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# PREVENTING MODIFICATION OF A LIST. CREATING A COPY

# Example 3
print("---Example 3----")
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
copy_of_list = unprinted_designs[:]

print_models(copy_of_list, completed_models)
show_completed_models(completed_models)

print(f"\nOriginal list: {unprinted_designs}")
print(f"Copy or original list: {copy_of_list}")
