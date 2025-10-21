# writing conditional tests

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

fruit = "Orange"
print(f'\nIs the fruit an apple? \n{fruit.lower() == 'apple'}')
print(f'\nIs the fruit an orange?\n{fruit.lower() == 'orange'}')

age = 18
qualify = age >=21
print(f'\nDoes he qualify for the postion?\n{qualify}')