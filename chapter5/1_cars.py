# If statements
# A simple example

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\n')

# Checking for eqauality
car = 'bmw'
print(f'Is the car a bmw?: {car == 'bmw'}')
print(f'Is the car an audi?: {car == 'audi'}')

# Dealing with case sensitivity
print('\n')
car = 'Audi'
print(car)
print(f'Is the car an Audi?: {car.lower() == 'audi'}')

# Checking for inequalities
print('\n')
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")
    