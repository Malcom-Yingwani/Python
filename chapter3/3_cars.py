# Organising lists
# Using the sort () method. Permanantly changes the list

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sorting in reverse alphabetical order
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Sorting temporarily
print("\nHere is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\n Here is the original list again:")
print(cars)

print("\n")

# Printing list in reverse order
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

# Finding Length of a list
print(len(cars))