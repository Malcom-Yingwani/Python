# Importing an entire module

from car_module import ElectricCar
from car_module import Car

my_leaf = ElectricCar("nissan", "leaf", 2024)
print(my_leaf.get_descriptive_name())

my_mustang = Car('ford', 'mustang', 2024)
print(my_mustang.get_descriptive_name())
            
