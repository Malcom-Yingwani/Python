# Importing multiple classes from a module 

# from car_module import Car, ElectricCar

# my_mustang = Car('ford', 'mustang', 2024)
# print(my_mustang.get_descriptive_name())
# my_leaf = ElectricCar('nissan', 'leaf', 2024)
# print(my_leaf.get_descriptive_name())

# Impirting an entire module

# import car_module 

# my_mustang = car_module.Car("ford", "mustang", 2024)
# print(my_mustang.get_descriptive_name())

# my_leaf = car_module.Car("nissan", "leaf", 2024)
# print(my_leaf.get_descriptive_name())

from car_module import *

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

# Summary

# The program imports all classes from the car_module file.

# It creates a new Car object with the make “ford,” model “mustang,” and year “2024.”

# The program prints the descriptive name of the Ford Mustang.

# It then creates an ElectricCar object with the make “nissan,” model “leaf,” and year “2024.”

# Finally, it prints the descriptive name of the Nissan Leaf.
